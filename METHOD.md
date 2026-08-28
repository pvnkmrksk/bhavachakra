# How the words were found

Back to the [wheels](README.md).

## The lookup

```
GET https://rala-search.rala-search.workers.dev/?q=<english word>

{ "query": str,
  "count": int,
  "results": [ { "kannada", "definition", "type", "source" } ] }
```

Calls were made one at a time with 0.35 s between them and without the `X-Rala-Intent: primary` header, so none of this reached rala's own search analytics. [alar.ink](https://alar.ink) was never queried: Alar arrives here only through rala's reversal of it.

rala matches whole words against definition text, so a query only finds the exact form the dictionary happens to use: `annoyed` returns nothing, `annoy` returns thirteen entries. [`scripts/rala.py`](scripts/rala.py) fixes this client-side with a morphological expander: 26 suffix rules, longest first, doubled-consonant undo, and one level of recursion so `playfully → playful → play`.

```
loneliness  → loneliness, lonely, lone
frustrated  → frustrated, frustrat, frustrate
victimised  → victimised, victimise, victimize
stopped     → stopped, stopp, stoppe, stop
```

Of the 52 words that first came back empty, morphology alone recovered 38. The last 14 needed hand-picked synonyms, `repelled → repulse`, `boredom → tedium`, `skeptical → sceptic`, which stemming cannot reach, and which is the argument for a thesaurus layer inside the worker rather than in every client.

## What came back, for ಭಾವಚಕ್ರ

| | count | meaning |
|---|---:|---|
| `direct` | 73 | the dictionary's top hit is the word on the wheel |
| `shaped` | 45 | rala had it, but buried in technical noise or in another register |
| `gap` | 12 | no usable entry; the word comes from Kannada usage |
| | **130** | |

Where rala is excellent: fear, anger and grief. Seven graded fear words, four for doubt, and ತೇಜೋವಧೆ, "the murder of someone's lustre", for *humiliate*.

Where it falls down it falls down structurally, because rala's bulk is Padakanaja, which is administrative, legal, scientific and agricultural:

| query | what rala returned |
|---|---|
| `stressed` | ಪ್ರತಿಬಲ, tensile stress, shear stress |
| `confused` | ತುಕ್ಕುಗೆಂಪು, the confused flour beetle |
| `let down` | ಹಾಲೊಸರಿಕೆ, milk let-down, the dairy term |
| `loving` | ನೆರಳು ಪ್ರಿಯ, shade-loving, of plants |
| `depressed` | ದಲಿತ, ಶೋಷಿತ, from the phrase "depressed classes" |
| `accepted` | ಅಂಗೀಕೃತ ಟೆಂಡರ್, accepted tender |
| `tired` | ದಣಿದ ಮಣ್ಣು, tired soil |
| `critical` | ಕ್ರಾಂತಿಕೋನ: critical angle |
| `proud / inspired / boredom / threatened` | nothing at all |

## Every lookup

Raw responses are in [`data/rala-responses.json`](data/rala-responses.json), keyed by query. The trail behind each word on ಭಾವಚಕ್ರ is in [`data/sources.json`](data/sources.json) and reproduced here.

| ಕನ್ನಡ | English slot | status | what rala returned |
|---|---|---|---|
| **ಸಂತೋಷ** | Happy | `direct` | ಸಂತೋಷದ, ಸಂತುಷ್ಟ, ಖುಷಿಯಾದ, ನೆಮ್ಮದಿಯ, ಭಾಗ್ಯವಂತನಾದ |
| **ತುಂಟತನ** | Playful | `gap` | ದ್ರೋಹ ಮಾಡು ⟨foul play⟩, ನಾಟಕಕಾರ ⟨playwright⟩, ಚಕ್ಕರ್ ಕೊಡು ⟨play truant⟩ |
| **ಉದ್ರೇಕ** | Aroused | `shaped` | ಉದ್ರೇಕಗೊಳ್ಳು, ಪ್ರಚೋದಿಸು, ಕೆರಳಿಸು |
| **ಕೀಟಲೆ** | Cheeky | `shaped` | ಉದ್ಧಟ, ಒರಟುತನದ, ದುರಹಂಕಾರದ |
| **ತೃಪ್ತಿ** | Content | `shaped` | ತೃಪ್ತ, ತೃಪ್ತಿ, ಪರಿವಿಡಿ ⟨table of contents⟩, ತೇವಾಂಶ ⟨moisture content⟩ |
| **ನಿರಾಳ** | Free | `shaped` | ಮುಕ್ತ, ಸ್ವತಂತ್ರ, ಕರಮುಕ್ತ ⟨duty-free⟩ |
| **ಹಿಗ್ಗು** | Joyful | `shaped` | ಸಂತೋಷ, ಉಲ್ಲಾಸ, ಹರ್ಷ |
| **ಆಸಕ್ತಿ** | Interested | `direct` | ಆಸಕ್ತಿ ಇರುವ, ಸಂಬಂಧವುಳ್ಳ, ಪಕ್ಷಪಾತದ ⟨interested party⟩ |
| **ಕುತೂಹಲ** | Curious | `direct` | ಕುತೂಹಲಕಾರಿ, ಕುತೂಹಲವುಳ್ಳ |
| **ಕೆದಕು** | Inquisitive | `shaped` | ಕೆದಕುವ, ಶೋಧಿಸುವ, ವಿಚಾರಮಾಡುವ |
| **ಹೆಮ್ಮೆ** | Proud | `gap` | nothing |
| **ಸಾರ್ಥಕ** | Successful | `shaped` | ಯಶಸ್ವಿ, ವಿಜಯಿ, ವಿಜೇತ |
| **ಆತ್ಮವಿಶ್ವಾಸ** | Confident | `direct` | ವಿಶ್ವಾಸವುಳ್ಳ, ನೆಚ್ಚಿಕೆಯ, ಧೈರ್ಯದ |
| **ಒಪ್ಪಿಗೆ** | Accepted | `gap` | ಅಂಗೀಕೃತ ಟೆಂಡರ್ ⟨accepted tender⟩, ಅಂಗೀಕೃತ ಠೇವಣಿ ⟨accepted deposit⟩, ಸ್ವೀಕೃತ |
| **ಗೌರವ** | Respected | `shaped` | ಆ ಸಂಬಂಧವಾದ ⟨with respect to⟩, ಸಂಬಂಧಿಸಿದಂತೆ ⟨in respect of⟩ |
| **ಮನ್ನಣೆ** | Valued | `shaped` | ಏಕಮೌಲ್ಯ ⟨single-valued⟩, ಮೌಲ್ಯ ಸಂದಾಯ ⟨value payable⟩ |
| **ಶಕ್ತಿ** | Powerful | `direct` | ಶಕ್ತಿಶಾಲಿ, ಶಕ್ತಿವಂತ, ಶಕ್ತನಾದ |
| **ಧೈರ್ಯ** | Courageous | `direct` | ಧೈರ್ಯದ, ಕೆಚ್ಚೆದೆಯ, ಎದೆಗಾರಿಕೆಯ |
| **ಹೊಳಹು** | Creative | `direct` | ಸೃಜನಾತ್ಮಕ, ರಚನಾತ್ಮಕ |
| **ನೆಮ್ಮದಿ** | Peaceful | `shaped` | ಶಾಂತಿಯ, ಶಾಂತಿಯುತ |
| **ಪ್ರೀತಿ** | Loving | `gap` | ನೆರಳು ಪ್ರಿಯ ⟨shade-loving⟩ |
| **ಕೃತಜ್ಞತೆ** | Thankful | `direct` | ಕೃತಜ್ಞ, ಕೃತಜ್ಞನಾದ |
| **ನಂಬಿಕೆ** | Trusting | `shaped` | ನಂಬಿಕೆ, ವಿಶ್ವಾಸ, ನ್ಯಾಸ ಖಾತೆ ⟨trust account⟩, ಟ್ರಸ್ಟ್ ಆಡಳಿತ |
| **ಸೂಕ್ಷ್ಮ** | Sensitive | `direct` | ಸೂಕ್ಷ್ಮಗ್ರಾಹಿ, ಸಂವೇದನಾಶೀಲ, ಸೂಕ್ಷ್ಮ |
| **ಸಲಿಗೆ** | Intimate | `direct` | ಸಲಿಗೆ, ಅನ್ಯೋನ್ಯ, ಆತ್ಮೀಯ, ನಿಕಟ |
| **ಭರವಸೆ** | Optimistic | `direct` | ಆಶಾವಾದದ, ಆಶಾಪೂರ್ಣ |
| **ಆಸೆ** | Hopeful | `direct` | ಭರವಸೆಯ, ಆಶಾದಾಯಕ |
| **ಸ್ಫೂರ್ತಿ** | Inspired | `gap` | nothing |
| **ಅಚ್ಚರಿ** | Surprised | `direct` | ಆಶ್ಚರ್ಯ, ವಿಸ್ಮಯ, ಅನಿರೀಕ್ಷಿತ, ಹಠಾತ್ ತನಿಖೆ ⟨surprise inspection⟩ |
| **ಬೆಚ್ಚು** | Startled | `direct` | ಚಕಿತಗೊಳಿಸು, ಗಾಬರಿಪಡಿಸು, ಬೆದರಿಸು |
| **ಆಘಾತ** | Shocked | `direct` | ಆಘಾತ, ದಿಗಿಲುಂಟುಮಾಡು, ವಿದ್ಯುದಾಘಾತ ⟨electric shock⟩ |
| **ಎದೆಗುಂದು** | Dismayed | `direct` | ಎದೆಗುಂದಿಸು, ಅಧೈರ್ಯ, ದಿಗಿಲು, ಹತಾಶೆ |
| **ಗೊಂದಲ** | Confused | `shaped` | ತುಕ್ಕುಗೆಂಪು ⟨confused flour beetle⟩ |
| **ಭ್ರಮೆ ಕಳಚು** | Disillusioned | `direct` | ಭ್ರಮನಿರಸನಗೊಂಡ |
| **ಕಂಗೆಡು** | Perplexed | `direct` | ಕಂಗೆಡಿಸು, ವಿಭ್ರಾಂತಿ ತರು |
| **ಬೆರಗು** | Amazed | `direct` | ಬೆರಗುಗೊಳಿಸು, ಆಶ್ಚರ್ಯಗೊಳ್ಳು, ಚಕಿತನಾಗು |
| **ದಂಗು** | Astonished | `direct` | ವಿಸ್ಮಯವನ್ನುಂಟುಮಾಡು, ಅಚ್ಚರಿಗೊಳಿಸು |
| **ಭಯಭಕ್ತಿ** | Awe | `direct` | ಭಯಮಿಶ್ರಿತ ಗೌರವ, ಭಯ ತುಂಬಿದ ಗೌರವ |
| **ಉತ್ಸಾಹ** | Excited | `direct` | ಉತ್ತೇಜಿತ, ಉದ್ರಿಕ್ತ, ಉತ್ಸಾಹ |
| **ತವಕ** | Eager | `direct` | ತವಕ, ಕಾತರದ, ಉತ್ಸುಕ, ಉತ್ಕಟ |
| **ಹುರುಪು** | Energetic | `direct` | ಹುರುಪು, ಉತ್ಸಾಹ, ಶಕ್ತಿಯುತವಾದ |
| **ಬೇಸರ** | Bad | `gap` | ಕೆಟ್ಟ, ದುರ್ವರ್ತನೆ ⟨bad behaviour⟩, ವಸೂಲಾಗದ ಸಾಲ ⟨bad debt⟩, ವೈಮನಸ್ಯ ⟨bad blood⟩ |
| **ಬೇಜಾರು** | Bored | `gap` | nothing |
| **ಉದಾಸೀನ** | Indifferent | `direct` | ಉದಾಸೀನ, ಅಸಡ್ಡೆಯ, ತಟಸ್ಥ |
| **ಅಸಡ್ಡೆ** | Apathetic | `direct` | ನಿರಾಸಕ್ತ, ಆಸಕ್ತಿಯಿಲ್ಲದ, ಭಾವಶೂನ್ಯ |
| **ಧಾವಂತ** | Busy | `shaped` | ಕಾರ್ಯಮಗ್ನ, ಬಿಡುವಿಲ್ಲದ, ನಿರತ |
| **ಒತ್ತಡ** | Pressured | `direct` | ಒತ್ತಡ, ರಕ್ತ ಒತ್ತಡ ⟨blood pressure⟩, ವಾತಾವರಣದ ಒತ್ತಡ |
| **ಆತುರ** | Rushed | `shaped` | ಧಾವಿಸು, ಮುನ್ನುಗ್ಗು, ತೀವ್ರಗತಿ |
| **ತಳಮಳ** | Stressed | `shaped` | ಒತ್ತಡ, ಪ್ರತಿಬಲ ⟨tensile stress⟩, ಕರ್ತನ ಪ್ರತಿಬಲ ⟨shear stress⟩ |
| **ಹೈರಾಣ** | Overwhelmed | `shaped` | ಮುಳುಗಿಹೋಗು, ಭಾವಪರವಶಗೊಳ್ಳು |
| **ಚಡಪಡಿಕೆ** | Restless | `direct` | ಚಡಪಡಿಸುವ, ತಳಮಳ, ವ್ಯಾಕುಲ, ಅಶಾಂತ |
| **ದಣಿವು** | Tired | `shaped` | ದಣಿದ ಮಣ್ಣು ⟨tired soil⟩ |
| **ತೂಕಡಿಕೆ** | Sleepy | `shaped` | ತೂಕಡಿಸುವ, ನಿದ್ದೆ, ಜಡನಾದ |
| **ಅನ್ಯಮನಸ್ಕ** | Unfocused | `direct` | ಅನ್ಯಮನಸ್ಕ, ಏಕಾಗ್ರತೆಯಿಲ್ಲದ, ಮರೆಗುಳಿ |
| **ಭಯ** | Fearful | `direct` | ಭಯ, ಹೆದರಿಕೆ, ಅಂಜಿಕೆ, ಭೀತಿ, ದಿಗಿಲು, ಆತಂಕ, ಗಾಬರಿ |
| **ಹೆದರಿಕೆ** | Scared | `direct` | ಹೆದರಿಕೆ, ಗಾಬರಿ, ಭೀತಿ, ಬೆದರುಗೊಂಬೆ ⟨scarecrow⟩ |
| **ಅಸಹಾಯಕತೆ** | Helpless | `direct` | ಅಸಹಾಯಕ, ದಿಕ್ಕಿಲ್ಲದ, ತಬ್ಬಲಿ |
| **ಅಂಜಿಕೆ** | Frightened | `direct` | ಹೆದರಿಸು, ಭಯಪಡಿಸು, ದಿಗಿಲುಗೊಳಿಸು |
| **ಆತಂಕ** | Anxious | `direct` | ಆತಂಕಗೊಂಡ, ವ್ಯಾಕುಲತೆ, ಚಿಂತಾಕ್ರಾಂತ, ತಲ್ಲಣಗೊಂಡ |
| **ಚಿಂತೆ** | Worried | `direct` | ಚಿಂತೆ, ಕಳವಳ, ಆತಂಕ, ಪೇಚಾಟ |
| **ಕಳವಳ** | Overwhelmed | `shaped` | ಕಳವಳಗೊಂಡ, ವ್ಯಾಕುಲ |
| **ಅಳುಕು** | Insecure | `direct` | ಅಭದ್ರ, ಅಸುರಕ್ಷಿತ, ರಕ್ಷಣೆ ರಹಿತ |
| **ಕೊರತೆ** | Inadequate | `shaped` | ಸಾಕಾಗದ, ಅಸಮರ್ಥ, ಕೊರತೆಯುಳ್ಳ |
| **ಕೀಳರಿಮೆ** | Inferior | `shaped` | ಕೀಳು, ಕಳಪೆ, ಕೆಳದರ್ಜೆಯ |
| **ದುರ್ಬಲ** | Weak | `direct` | ದುರ್ಬಲ, ಬಲಹೀನ, ನಿರ್ಬಲ |
| **ದಂಡ** | Worthless | `shaped` | ಅಯೋಗ್ಯ |
| **ಲೆಕ್ಕಕ್ಕಿಲ್ಲ** | Insignificant | `direct` | ಕ್ಷುಲ್ಲಕ, ಅತ್ಯಲ್ಪ, ನಿಕೃಷ್ಟ |
| **ತಿರಸ್ಕಾರ** | Rejected | `shaped` | ಸೋತ ಅಭ್ಯರ್ಥಿ ⟨rejected candidate⟩, ತಿರಸ್ಕರಿಸತಕ್ಕದ್ದು, ಹಕ್ಕು ಸಾಧನೆಗಳು ⟨rejected claims⟩ |
| **ಹೊರಗಿಡು** | Excluded | `gap` | nothing |
| **ಕಿರುಕುಳ** | Persecuted | `direct` | ಕಿರುಕುಳ ಕೊಡು, ಪೀಡಿಸು, ಹಿಂಸಿಸು |
| **ಬೆದರಿಕೆ** | Threatened | `gap` | nothing |
| **ನಡುಕ** | Nervous | `shaped` | ನಡುಗುವ, ಅಂಜುಬುರುಕ, ನರವ್ಯೂಹ ⟨nervous system⟩ |
| **ಬಟಾಬಯಲು** | Exposed | `shaped` | ಗುಟ್ಟುರಟ್ಟಾದ, ಸುರಕ್ಷಣೆ ಇಲ್ಲದ, ಬಹಿರಂಗಗೊಳಿಸಿದ |
| **ಕೋಪ** | Angry | `direct` | ಕೋಪ, ಸಿಟ್ಟು, ಸಿಡುಕು, ರೋಷ, ಮುನಿಸು, ಕ್ರೋಧ, ತಾಪ |
| **ಕೈಕೊಟ್ಟರು** | Let down | `gap` | ಹಾಲೊಸರಿಕೆ ⟨milk let-down⟩ |
| **ದ್ರೋಹ** | Betrayed | `direct` | ದ್ರೋಹ ಮಾಡು, ವಿಶ್ವಾಸಘಾತ, ವಂಚಿಸು |
| **ಅಸಮಾಧಾನ** | Resentful | `direct` | ಅಸಮಾಧಾನ, ಜಿದ್ದು, ಕರುಬು, ಹಗೆತನ |
| **ಅವಮಾನ** | Humiliated | `direct` | ಅವಮಾನಿಸು, ತೇಜೋವಧೆ, ಮರ್ಯಾದೆ ಕಳೆ |
| **ಅವಮರ್ಯಾದೆ** | Disrespected | `direct` | ಅಗೌರವ, ಅವಮಾನ, ಉಪೇಕ್ಷೆ, ಅವಮರ್ಯಾದೆ |
| **ಗೇಲಿ** | Ridiculed | `direct` | ಅಪಹಾಸ್ಯ, ಗೇಲಿ, ಅವಹೇಳನ, ಅಣಕಿಸು |
| **ಕಹಿ** | Bitter | `shaped` | ಹಾಗಲಕಾಯಿ ⟨bitter gourd⟩, ಕಹಿಗುಳಿಗೆ ⟨bitter pill⟩, ಕ್ರೂರ, ಕಠಿಣ |
| **ಆಕ್ರೋಶ** | Indignant | `shaped` | ಕುಪಿತ, ಕೆರಳಿದ, ರೇಗಿದ |
| **ಭಂಗ** | Violated | `gap` | ಉಲ್ಲಂಘಿಸು ⟨violate a rule⟩, ಮಾನಭಂಗ ⟨sexual assault⟩ |
| **ಸಿಟ್ಟು** | Mad | `direct` | ಸಿಟ್ಟು, ಹುಚ್ಚು ⟨insane⟩, ಮತಿಗೆಟ್ಟ |
| **ರೊಚ್ಚು** | Furious | `direct` | ರೋಷಾವೇಶದ, ಕ್ರೋಧಾವಿಷ್ಟ, ಉಗ್ರ, ಪ್ರಚಂಡ |
| **ಹೊಟ್ಟೆಕಿಚ್ಚು** | Jealous | `shaped` | ಅಸೂಯೆಯ, ಮಾತ್ಸರ್ಯದ |
| **ಜಗಳಗಂಟ** | Aggressive | `direct` | ಆಕ್ರಮಣಶೀಲ, ಜಗಳಗಂಟ, ಮೇಲೆ ಬೀಳುವ |
| **ಕೆರಳಿಕೆ** | Provoked | `direct` | ಕೆರಳಿಸು, ಕೆಣಕು, ಪ್ರಚೋದಿಸು, ರೇಗಿಸು |
| **ಹಗೆತನ** | Hostile | `direct` | ಹಗೆಯ, ವೈರದ, ಶತ್ರುತ್ವದ, ಪ್ರತಿಕೂಲ |
| **ರೇಜಿಗೆ** | Frustrated | `shaped` | ಆಶಾಭಂಗ ಹೊಂದಿದ, ವಿಫಲವಾದ, ಭಗ್ನ, ನಿಷ್ಫಲಗೊಳಿಸು |
| **ಕೆಂಡಾಮಂಡಲ** | Infuriated | `shaped` | ರೇಗಿಸು, ಕೆರಳಿಸು |
| **ಕಿರಿಕಿರಿ** | Annoyed | `direct` | ಕಿರಿಕಿರಿಮಾಡು, ರೇಗಿಸು, ಕಾಡಿಸು |
| **ಬಿಗುಮಾನ** | Distant | `direct` | ಬಿಗುಮಾನದ, ಸಲಿಗೆ ಇಲ್ಲದ, ದೂರದ |
| **ಮುದುಡು** | Withdrawn | `shaped` | ವಾಪಸ್ಸು ಪಡೆದ ⟨withdrawn application⟩, ಹಿಂದಕ್ಕೆ ಪಡೆದ |
| **ಮರಗಟ್ಟು** | Numb | `direct` | ಮರಗಟ್ಟಿದ, ಜೋಮುಹಿಡಿದ, ಜಡವಾದ |
| **ಟೀಕೆ** | Critical | `shaped` | ಕ್ರಾಂತಿಕೋನ ⟨critical angle⟩, ವಿಷಮ ಮೌಲ್ಯ ⟨critical value⟩, ವಿಮರ್ಶಾತ್ಮಕ |
| **ಅನುಮಾನ** | Skeptical | `direct` | ಅನುಮಾನ, ಸಂಶಯ, ಸಂದೇಹ, ಶಂಕೆ |
| **ಉಡಾಫೆ** | Dismissive | `shaped` | ತಳ್ಳಿಹಾಕು, ನಿರ್ಲಕ್ಷಿಸು, ವಜಾ ಮಾಡು ⟨dismiss from service⟩ |
| **ಅಸಹ್ಯ** | Disgusted | `direct` | ಅಸಹ್ಯ, ಜಿಗುಪ್ಸೆ, ಹೇಸಿಕೆ, ರೋಸು, ವಾಕರಿಕೆ |
| **ಒಪ್ಪದಿರು** | Disapproving | `direct` | ಅಸಮ್ಮತಿ, ಮೆಚ್ಚದಿರು, ಒಪ್ಪದಿರು |
| **ಕೊಂಕು** | Judgmental | `shaped` | ನ್ಯಾಯಾಧೀಶ ⟨judge⟩, ಜಿಲ್ಲಾ ನ್ಯಾಯಾಧೀಶ ⟨district judge⟩, ಖಂಡನೆ |
| **ಮುಜುಗರ** | Embarrassed | `direct` | ಮುಜುಗರ ಉಂಟಾದ |
| **ನಿರಾಸೆ** | Disappointed | `direct` | ನಿರಾಶೆಗೊಂಡ, ಆಶಾಭಂಗ, ಹತಾಶೆ |
| **ಹೌಹಾರು** | Appalled | `direct` | ದಿಗ್ಭ್ರಮೆಗೊಂಡ, ಭೀತ, ಗಾಬರಿಗೊಂಡ |
| **ರೋಸು** | Revolted | `shaped` | ದಂಗೆ ⟨rebellion⟩, ಬಂಡಾಯ, ವಿದ್ರೋಹ |
| **ಘೋರ** | Awful | `shaped` | ಭಯಾನಕವಾದ, ಭೀಕರ |
| **ವಾಕರಿಕೆ** | Nauseated | `direct` | ವಾಕರಿಕೆ, ಓಕರಿಕೆ, ಹೊಟ್ಟೆ ತೊಳಸು |
| **ಹೇಸಿಗೆ** | Detestable | `direct` | ಹೇಸು, ಅಸಹ್ಯಪಡು, ಹೇಸಿಗೆ ಪಡು |
| **ಜಿಗುಪ್ಸೆ** | Repelled | `direct` | ಜಿಗುಪ್ಸೆಗೊಳಿಸು, ಹಿಮ್ಮೆಟ್ಟಿಸು, ವಿಕರ್ಷಿಸು |
| **ದಿಗಿಲು** | Horrified | `direct` | ದಿಗಿಲುಗೊಳಿಸು, ಭಯಹುಟ್ಟಿಸು, ದಿಕ್ಕುಗೆಡಿಸು |
| **ಹಿಂಜರಿಕೆ** | Hesitant | `direct` | ಹಿಂಜರಿಯುವ, ಹಿಮ್ಮೆಟ್ಟುವ, ಶಂಕೆಯುಳ್ಳ |
| **ದುಃಖ** | Sad | `direct` | ದುಃಖಕರ, ವಿಷಾದಕರ, ಶೋಚನೀಯ, ಕುಗ್ಗಿದ, ಸೊರಗಿದ, ಅಮಂಗಳ ⟨inauspicious⟩ |
| **ಒಂಟಿತನ** | Lonely | `direct` | ಒಂಟಿ, ಏಕಾಂಗಿ, ಒಬ್ಬನೇ |
| **ಏಕಾಂಗಿ** | Isolated | `shaped` | ಪ್ರತ್ಯೇಕಿಸಿದ, ಬೇರ್ಪಡಿಸಿದ, ಪ್ರತ್ಯೇಕ ಸ್ಥಳ |
| **ತಬ್ಬಲಿ** | Abandoned | `shaped` | ತೊರೆದ ಪ್ರದೇಶ ⟨abandoned area⟩, ತಬ್ಬಲಿ |
| **ದುರ್ಬಲತೆ** | Vulnerable | `gap` | ಸುಭೇದ್ಯ, ಭೇದ್ಯ, ದುರ್ಬಲ ಸ್ಥಿತಿ ⟨vulnerable stage⟩ |
| **ಬಲಿಪಶು** | Victimised | `direct` | ಬಲಿಪಶುಮಾಡು, ಪೀಡಿಸು, ಸತಾಯಿಸು |
| **ನಾಜೂಕು** | Fragile | `direct` | ನಾಜೂಕಾದ, ಭಂಗುರ, ಶಿಥಿಲ |
| **ಹತಾಶೆ** | Despair | `direct` | ಹತಾಶೆ, ನಿರಾಶೆ, ಎದೆಗುಂದು, ಆಸೆಗೆಡು |
| **ಅಳಲು** | Grief | `direct` | ಅಳಲು, ಶೋಕ, ಸಂಕಟ, ಕೊರಗು, ವ್ಯಥೆ |
| **ಕೈಲಾಗದು** | Powerless | `shaped` | ಶಕ್ತಿಹೀನ, ಬಲಹೀನ, ದುರ್ಬಲ |
| **ಪಾಪಪ್ರಜ್ಞೆ** | Guilty | `shaped` | ಅಪರಾಧಿ, ತಪ್ಪಿತಸ್ಥ, ದೋಷಿ, ಅಪರಾಧಿ ಮನೋಭಾವ ⟨guilty mind⟩ |
| **ನಾಚಿಕೆ** | Ashamed | `shaped` | ಅವಮಾನಗೊಂಡ, ಮಾನಗೆಟ್ಟ |
| **ಪಶ್ಚಾತ್ತಾಪ** | Remorseful | `direct` | ಪಶ್ಚಾತ್ತಾಪ, ಅನುತಾಪ, ಮರುಕ |
| **ಖಿನ್ನತೆ** | Depressed | `shaped` | ದಲಿತ ವರ್ಗ ⟨depressed classes⟩, ಶೋಷಿತ, ಕುಗ್ಗಿದ, ನಿರುತ್ಸಾಹದ |
| **ಕುಗ್ಗು** | Inferior | `shaped` | ಕುಗ್ಗಿದ, ಇಳಿದ, ತಗ್ಗಿದ |
| **ಬರಿದು** | Empty | `shaped` | ಬರಿದು, ಖಾಲಿ, ಪೊಳ್ಳು, ಶೂನ್ಯ |
| **ನೋವು** | Hurt | `direct` | ನೋವು, ನೋಯಿಸು, ಗಾಯ, ಸಾಧಾರಣ ಗಾಯ ⟨simple hurt, IPC⟩ |
| **ಆಶಾಭಂಗ** | Disappointed | `direct` | ಆಶಾಭಂಗ, ನಿರಾಶೆಗೊಂಡ |
| **ಸಂಕೋಚ** | Embarrassed | `shaped` | ಮುಜುಗರ ಉಂಟಾದ |

## One rendering note

Do not use SVG `<textPath>` for Kannada. It positions each glyph separately along the path, which shatters an akshara into base, vowel sign and ottakshara, each rotated on its own: ಅಸಹ್ಯ came out as three unrelated pieces. Labels on the innermost visible ring are upright and never rotated; the outer rings rotate the whole string as one unit, which is safe.

