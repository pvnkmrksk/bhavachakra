# ಭಾವಚಕ್ರ · a feeling wheel in Kannada

**[Open the wheel →](https://pvnkmrksk.github.io/bhavachakra/)**

The English feeling wheel, taken through a Kannada dictionary and then argued with. Each of the 130 Kannada words on it came out of [**rala**](https://pvnkmrksk.github.io/rala/) — 478,680 English→Kannada entries, reversed from [Alar](https://alar.ink) and Padakanaja — and was then kept, reshaped, or thrown out and replaced with what a Kannada speaker would actually say.

Everything is in flat JSON and CSV under [`data/`](data/) if you want the words without the page.

## The lookup

```
GET https://rala-search.rala-search.workers.dev/?q=<english word>

{ "query": str,
  "count": int,
  "results": [ { "kannada", "definition", "type", "source" } ] }
```

Calls were made one at a time with 0.35 s between them, and without the `X-Rala-Intent: primary` header, so none of this landed in rala's own search analytics. [alar.ink](https://alar.ink) itself was never queried — Alar reaches this wheel only through rala's reversal of it.

rala matches whole words against definition text, so a query only finds the exact form the dictionary happens to use: `annoyed` returns nothing, `annoy` returns thirteen entries. [`scripts/rala.py`](scripts/rala.py) works around this with a morphological expander that strips `-ness`, `-ly`, `-ed`, `-ing`, `-ful`, `-ity` and friends, and retries. Of the 52 words that first came back empty, morphology alone recovered 38. The last 14 needed hand-picked synonyms — `repelled → repulse`, `boredom → tedium`, `skeptical → sceptic` — which is the part a dictionary API cannot do for you, and the part a thesaurus layer would fix.

## What came back

| | count | meaning |
|---|---:|---|
| `direct` | 73 | **rala's own answer** — the dictionary's top hit is the word on the wheel |
| `shaped` | 45 | **reshaped** — rala had it, but buried in technical noise or in the wrong register |
| `gap` | 12 | **dictionary gap** — no usable entry; the word comes from Kannada usage |
| | **130** | |

Where rala is excellent: fear, anger and grief. Seven graded fear words (ಅಂಜಿಕೆ, ಹೆದರಿಕೆ, ದಿಗಿಲು, ಗಾಬರಿ, ಆತಂಕ, ಭೀತಿ, ಭಯ), four for doubt, and ತೇಜೋವಧೆ — "the murder of someone's lustre" — for *humiliate*.

Where it falls down, it falls down structurally: rala's bulk is Padakanaja, which is administrative, legal, scientific and agricultural. So —

| query | what rala returned |
|---|---|
| `stressed` | ಪ್ರತಿಬಲ — tensile stress, shear stress (materials engineering) |
| `confused` | ತುಕ್ಕುಗೆಂಪು — the confused flour beetle |
| `let down` | ಹಾಲೊಸರಿಕೆ — milk let-down, the dairy term |
| `loving` | ನೆರಳು ಪ್ರಿಯ — shade-loving, of plants |
| `depressed` | ದಲಿತ, ಶೋಷಿತ — from the colonial phrase "depressed classes" |
| `accepted` | ಅಂಗೀಕೃತ ಟೆಂಡರ್ — accepted tender |
| `tired` | ದಣಿದ ಮಣ್ಣು — tired soil |
| `critical` | ಕ್ರಾಂತಿಕೋನ — critical angle |
| `proud / inspired / boredom / threatened` | nothing at all |

## The wheel

Seven core feelings, each with branches and leaves. `status` is defined in the table above; **rala's hits** are the dictionary candidates that were actually considered, trimmed to the short ones.

### ಸಂತೋಷ · Happy — *santōṣa*

| ring | English | ಕನ್ನಡ | roman | status | rala's hits |
|---|---|---|---|---|---|
| core | Happy | **ಸಂತೋಷ** | *santōṣa* | `direct` | ಸಂತೋಷದ, ಸಂತುಷ್ಟ, ಖುಷಿಯಾದ, ನೆಮ್ಮದಿಯ, ಭಾಗ್ಯವಂತನಾದ |
| branch | Playful | **ತುಂಟತನ** | *ṭuṇṭatana* | `gap` | ದ್ರೋಹ ಮಾಡು ⟨foul play⟩, ನಾಟಕಕಾರ ⟨playwright⟩, ಚಕ್ಕರ್ ಕೊಡು ⟨play truant⟩ |
| leaf | Aroused | **ಉದ್ರೇಕ** | *udrēka* | `shaped` | ಉದ್ರೇಕಗೊಳ್ಳು, ಪ್ರಚೋದಿಸು, ಕೆರಳಿಸು |
| leaf | Cheeky | **ಕೀಟಲೆ** | *kīṭale* | `shaped` | ಉದ್ಧಟ, ಒರಟುತನದ, ದುರಹಂಕಾರದ |
| branch | Content | **ತೃಪ್ತಿ** | *tṛpti* | `shaped` | ತೃಪ್ತ, ತೃಪ್ತಿ, ಪರಿವಿಡಿ ⟨table of contents⟩, ತೇವಾಂಶ ⟨moisture content⟩ |
| leaf | Free | **ನಿರಾಳ** | *nirāḷa* | `shaped` | ಮುಕ್ತ, ಸ್ವತಂತ್ರ, ಕರಮುಕ್ತ ⟨duty-free⟩ |
| leaf | Joyful | **ಹಿಗ್ಗು** | *higgu* | `shaped` | ಸಂತೋಷ, ಉಲ್ಲಾಸ, ಹರ್ಷ |
| branch | Interested | **ಆಸಕ್ತಿ** | *āsakti* | `direct` | ಆಸಕ್ತಿ ಇರುವ, ಸಂಬಂಧವುಳ್ಳ, ಪಕ್ಷಪಾತದ ⟨interested party⟩ |
| leaf | Curious | **ಕುತೂಹಲ** | *kutūhala* | `direct` | ಕುತೂಹಲಕಾರಿ, ಕುತೂಹಲವುಳ್ಳ |
| leaf | Inquisitive | **ಜಿಜ್ಞಾಸೆ** | *jijñāse* | `shaped` | ಕೆದಕುವ, ಶೋಧಿಸುವ, ವಿಚಾರಮಾಡುವ |
| branch | Proud | **ಹೆಮ್ಮೆ** | *hemme* | `gap` | — |
| leaf | Successful | **ಸಾರ್ಥಕ** | *sārthaka* | `shaped` | ಯಶಸ್ವಿ, ವಿಜಯಿ, ವಿಜೇತ |
| leaf | Confident | **ಆತ್ಮವಿಶ್ವಾಸ** | *ātma-viśvāsa* | `direct` | ವಿಶ್ವಾಸವುಳ್ಳ, ನೆಚ್ಚಿಕೆಯ, ಧೈರ್ಯದ |
| branch | Accepted | **ಒಪ್ಪಿಗೆ** | *oppige* | `gap` | ಅಂಗೀಕೃತ ಟೆಂಡರ್ ⟨accepted tender⟩, ಅಂಗೀಕೃತ ಠೇವಣಿ ⟨accepted deposit⟩, ಸ್ವೀಕೃತ |
| leaf | Respected | **ಗೌರವ** | *gaurava* | `shaped` | ಆ ಸಂಬಂಧವಾದ ⟨with respect to⟩, ಸಂಬಂಧಿಸಿದಂತೆ ⟨in respect of⟩ |
| leaf | Valued | **ಮನ್ನಣೆ** | *mannaṇe* | `shaped` | ಏಕಮೌಲ್ಯ ⟨single-valued⟩, ಮೌಲ್ಯ ಸಂದಾಯ ⟨value payable⟩ |
| branch | Powerful | **ಶಕ್ತಿ** | *śakti* | `direct` | ಶಕ್ತಿಶಾಲಿ, ಶಕ್ತಿವಂತ, ಶಕ್ತನಾದ |
| leaf | Courageous | **ಧೈರ್ಯ** | *dhairya* | `direct` | ಧೈರ್ಯದ, ಕೆಚ್ಚೆದೆಯ, ಎದೆಗಾರಿಕೆಯ |
| leaf | Creative | **ಸೃಜನಶೀಲತೆ** | *sṛjanaśīlate* | `direct` | ಸೃಜನಾತ್ಮಕ, ರಚನಾತ್ಮಕ |
| branch | Peaceful | **ನೆಮ್ಮದಿ** | *nemmadi* | `shaped` | ಶಾಂತಿಯ, ಶಾಂತಿಯುತ |
| leaf | Loving | **ಪ್ರೀತಿ** | *prīti* | `gap` | ನೆರಳು ಪ್ರಿಯ ⟨shade-loving⟩ |
| leaf | Thankful | **ಕೃತಜ್ಞತೆ** | *kṛtajñate* | `direct` | ಕೃತಜ್ಞ, ಕೃತಜ್ಞನಾದ |
| branch | Trusting | **ನಂಬಿಕೆ** | *nambike* | `shaped` | ನಂಬಿಕೆ, ವಿಶ್ವಾಸ, ನ್ಯಾಸ ಖಾತೆ ⟨trust account⟩, ಟ್ರಸ್ಟ್ ಆಡಳಿತ |
| leaf | Sensitive | **ಸೂಕ್ಷ್ಮ** | *sūkṣma* | `direct` | ಸೂಕ್ಷ್ಮಗ್ರಾಹಿ, ಸಂವೇದನಾಶೀಲ, ಸೂಕ್ಷ್ಮ |
| leaf | Intimate | **ಸಲಿಗೆ** | *salige* | `direct` | ಸಲಿಗೆ, ಅನ್ಯೋನ್ಯ, ಆತ್ಮೀಯ, ನಿಕಟ |
| branch | Optimistic | **ಆಶಾವಾದ** | *āśāvāda* | `direct` | ಆಶಾವಾದದ, ಆಶಾಪೂರ್ಣ |
| leaf | Hopeful | **ಭರವಸೆ** | *bharavase* | `direct` | ಭರವಸೆಯ, ಆಶಾದಾಯಕ |
| leaf | Inspired | **ಸ್ಫೂರ್ತಿ** | *sphūrti* | `gap` | — |

<details><summary>Reading — why these words and not the dictionary's</summary>

- **ಸಂತೋಷ** *(Happy)* — rala also returns ಭಾಗ್ಯವಂತ / ಅದೃಷ್ಟಶಾಲಿ — 'lucky'. English *happy* still carries its old root *hap*, chance. Kannada keeps luck and gladness in separate words.
- **ತುಂಟತನ** *(Playful)* — A clean miss. rala only knows *play* as the noun — foul play, playwright, child's play. The felt state is ತುಂಟತನ, the mischief of a child you are not actually angry with.
- **ಉದ್ರೇಕ** *(Aroused)* — In Kannada ಉದ್ರೇಕ is not primarily erotic — a crowd, a temper and a nerve can all be ಉದ್ರಿಕ್ತ. It means charged, and the charge can go either way.
- **ಕೀಟಲೆ** *(Cheeky)* — rala's ಉದ್ಧಟ / ದುರಹಂಕಾರ are genuinely insulting. Cheeky is affectionate — that is ಕೀಟಲೆ, teasing you are allowed to do.
- **ತೃಪ್ತಿ** *(Content)* — The right word was in there, sitting under moisture content and table of contents. ತೃಪ್ತಿ is satiety — the feeling after a meal, and after a life.
- **ನಿರಾಳ** *(Free)* — ಮುಕ್ತ and ಸ್ವತಂತ್ರ are freedoms of status — liberated, independent, tax-exempt. The *feeling* of free is ನಿರಾಳ: unclenched, the breath after the weight comes off.
- **ಹಿಗ್ಗು** *(Joyful)* — ಹರ್ಷ and ಉಲ್ಲಾಸ are correct and Sanskritic. ಹಿಗ್ಗು is the native verb-noun: to swell. Joy as something that expands you.
- **ಜಿಜ್ಞಾಸೆ** *(Inquisitive)* — ಕೆದಕುವ is prying — poking at what isn't yours. ಜಿಜ್ಞಾಸೆ is the honourable version: the wish to know, the word used for philosophical enquiry.
- **ಹೆಮ್ಮೆ** *(Proud)* — rala returns nothing at all for *proud*. And Kannada would resist a single answer anyway: ಹೆಮ್ಮೆ is warm pride in someone, ಅಭಿಮಾನ is pride-as-loyalty, ಅಹಂಕಾರ is the pride that has gone bad. English collapses all three.
- **ಸಾರ್ಥಕ** *(Successful)* — ಯಶಸ್ವಿ is the outcome — you won. ಸಾರ್ಥಕ is the feeling — it had meaning, it was worth it. Only one of those belongs on an emotion wheel.
- **ಆತ್ಮವಿಶ್ವಾಸ** *(Confident)* — Literally 'self-trust'. Kannada builds confidence out of the same root as trusting another person.
- **ಒಪ್ಪಿಗೆ** *(Accepted)* — Every hit is procurement paperwork. And Kannada has no noun for *the felt state of being accepted* — you say it as something others did: ನನ್ನನ್ನು ಒಪ್ಪಿಕೊಂಡರು, 'they took me in'. The feeling lives in a verb, not a noun.
- **ಗೌರವ** *(Respected)* — rala only found the clerical *in respect of*. ಗೌರವ is the real word, and in Kannada it is something you give, actively, not something you passively have.
- **ಮನ್ನಣೆ** *(Valued)* — ಮೌಲ್ಯ is price. ಮನ್ನಣೆ is being recognised and given your due — the thing people leave jobs for the lack of.
- **ಧೈರ್ಯ** *(Courageous)* — ಧೈರ್ಯ is steadiness under fear. The native alternatives rala offers are more physical: ಕೆಚ್ಚು is heat in the chest, ಎದೆಗಾರಿಕೆ is literally chest-having.
- **ನೆಮ್ಮದಿ** *(Peaceful)* — The single most important correction on this wheel. ಶಾಂತಿ is peace as the absence of war — treaties, ceasefires, ಶಾಂತಿ ಸಭೆ. ನೆಮ್ಮದಿ is peace of mind, and it is what people actually pray for.
- **ಪ್ರೀತಿ** *(Loving)* — The only match in 478,680 entries was a botany term for shade-loving plants. Kannada is not short of love words — ಪ್ರೀತಿ, ಮಮತೆ, ವಾತ್ಸಲ್ಯ, ಅಕ್ಕರೆ, ಒಲವು — the dictionary just isn't built to find them from English.
- **ಕೃತಜ್ಞತೆ** *(Thankful)* — Literally 'knowing what was done'. Gratitude as accurate memory.
- **ನಂಬಿಕೆ** *(Trusting)* — Buried under thirty entries of trust deeds and trust accounts. ನಂಬಿಕೆ also means belief and superstition — in Kannada, trusting a person and believing a thing are one act.
- **ಸೂಕ್ಷ್ಮ** *(Sensitive)* — ಸೂಕ್ಷ್ಮ means fine-grained, subtle-perceiving. Calling someone ಸೂಕ್ಷ್ಮ is praise — unlike English 'sensitive', which is half an accusation.
- **ಸಲಿಗೆ** *(Intimate)* — ಸಲಿಗೆ has no English word. It is the earned licence to be informal with someone — to tease them, take their food, drop the honorific. Intimacy defined as permission, not as feeling.
- **ಭರವಸೆ** *(Hopeful)* — ಭರವಸೆ is also the word for a promise or an assurance. Hope, in Kannada, is something somebody gave you.
- **ಸ್ಫೂರ್ತಿ** *(Inspired)* — No result. ಸ್ಫೂರ್ತಿ is the everyday word — a sudden welling-up, the same root as a spark.

</details>

### ಅಚ್ಚರಿ · Surprised — *accari*

| ring | English | ಕನ್ನಡ | roman | status | rala's hits |
|---|---|---|---|---|---|
| core | Surprised | **ಅಚ್ಚರಿ** | *accari* | `direct` | ಆಶ್ಚರ್ಯ, ವಿಸ್ಮಯ, ಅನಿರೀಕ್ಷಿತ, ಹಠಾತ್ ತನಿಖೆ ⟨surprise inspection⟩ |
| branch | Startled | **ಬೆಚ್ಚು** | *beccu* | `direct` | ಚಕಿತಗೊಳಿಸು, ಗಾಬರಿಪಡಿಸು, ಬೆದರಿಸು |
| leaf | Shocked | **ಆಘಾತ** | *āghāta* | `direct` | ಆಘಾತ, ದಿಗಿಲುಂಟುಮಾಡು, ವಿದ್ಯುದಾಘಾತ ⟨electric shock⟩ |
| leaf | Dismayed | **ಎದೆಗುಂದು** | *edegundu* | `direct` | ಎದೆಗುಂದಿಸು, ಅಧೈರ್ಯ, ದಿಗಿಲು, ಹತಾಶೆ |
| branch | Confused | **ಗೊಂದಲ** | *gondala* | `shaped` | ತುಕ್ಕುಗೆಂಪು ⟨confused flour beetle⟩ |
| leaf | Disillusioned | **ಭ್ರಮನಿರಸನ** | *bhrama-nirasana* | `direct` | ಭ್ರಮನಿರಸನಗೊಂಡ |
| leaf | Perplexed | **ಕಂಗೆಡು** | *kaṅgeḍu* | `direct` | ಕಂಗೆಡಿಸು, ವಿಭ್ರಾಂತಿ ತರು |
| branch | Amazed | **ಬೆರಗು** | *beragu* | `direct` | ಬೆರಗುಗೊಳಿಸು, ಆಶ್ಚರ್ಯಗೊಳ್ಳು, ಚಕಿತನಾಗು |
| leaf | Astonished | **ವಿಸ್ಮಯ** | *vismaya* | `direct` | ವಿಸ್ಮಯವನ್ನುಂಟುಮಾಡು, ಅಚ್ಚರಿಗೊಳಿಸು |
| leaf | Awe | **ಭಯಭಕ್ತಿ** | *bhaya-bhakti* | `direct` | ಭಯಮಿಶ್ರಿತ ಗೌರವ, ಭಯ ತುಂಬಿದ ಗೌರವ |
| branch | Excited | **ಉತ್ಸಾಹ** | *utsāha* | `direct` | ಉತ್ತೇಜಿತ, ಉದ್ರಿಕ್ತ, ಉತ್ಸಾಹ |
| leaf | Eager | **ತವಕ** | *tavaka* | `direct` | ತವಕ, ಕಾತರದ, ಉತ್ಸುಕ, ಉತ್ಕಟ |
| leaf | Energetic | **ಹುರುಪು** | *hurupu* | `direct` | ಹುರುಪು, ಉತ್ಸಾಹ, ಶಕ್ತಿಯುತವಾದ |

<details><summary>Reading — why these words and not the dictionary's</summary>

- **ಅಚ್ಚರಿ** *(Surprised)* — ಅಚ್ಚರಿ is the native word, ಆಶ್ಚರ್ಯ the Sanskrit one everyone also uses. Kept ಅಚ್ಚರಿ at the centre because the wheel should sound like speech, not a textbook.
- **ಬೆಚ್ಚು** *(Startled)* — ಬೆಚ್ಚಿಬೀಳು — to be startled and drop. Kannada builds the flinch out of a fall.
- **ಎದೆಗುಂದು** *(Dismayed)* — Literally 'the chest sinks'. Kannada names the physical event and leaves you to infer the feeling — it does this constantly.
- **ಗೊಂದಲ** *(Confused)* — The dictionary's one match for *confused* is a species of beetle. ಗೊಂದಲ is the real word, and it also means a noisy crowd — confusion as too many voices at once.
- **ಭ್ರಮನಿರಸನ** *(Disillusioned)* — 'The dispelling of the illusion' — a precise philosophical term doing everyday emotional work.
- **ಕಂಗೆಡು** *(Perplexed)* — ಕಣ್ + ಕೆಡು: the eyes go bad. To be at a loss is, literally, to lose your sight of it.
- **ಭಯಭಕ್ತಿ** *(Awe)* — rala could only define it as a phrase: 'respect mixed with fear'. But Kannada does have the compound — ಭಯಭಕ್ತಿ, fear-and-devotion, the standard word for how one stands before a deity or a formidable elder. Awe as a social posture, not a private thrill.
- **ತವಕ** *(Eager)* — ತವಕ and ಕಾತರ are both eagerness with an edge of ache — waiting that has begun to hurt slightly.

</details>

### ಬೇಸರ · Bad — *bēsara*

| ring | English | ಕನ್ನಡ | roman | status | rala's hits |
|---|---|---|---|---|---|
| core | Bad | **ಬೇಸರ** | *bēsara* | `gap` | ಕೆಟ್ಟ, ದುರ್ವರ್ತನೆ ⟨bad behaviour⟩, ವಸೂಲಾಗದ ಸಾಲ ⟨bad debt⟩, ವೈಮನಸ್ಯ ⟨bad blood⟩ |
| branch | Bored | **ಬೇಜಾರು** | *bējāru* | `gap` | — |
| leaf | Indifferent | **ಉದಾಸೀನ** | *udāsīna* | `direct` | ಉದಾಸೀನ, ಅಸಡ್ಡೆಯ, ತಟಸ್ಥ |
| leaf | Apathetic | **ನಿರಾಸಕ್ತಿ** | *nirāsakti* | `direct` | ನಿರಾಸಕ್ತ, ಆಸಕ್ತಿಯಿಲ್ಲದ, ಭಾವಶೂನ್ಯ |
| branch | Busy | **ಧಾವಂತ** | *dhāvanta* | `shaped` | ಕಾರ್ಯಮಗ್ನ, ಬಿಡುವಿಲ್ಲದ, ನಿರತ |
| leaf | Pressured | **ಒತ್ತಡ** | *ottaḍa* | `direct` | ಒತ್ತಡ, ರಕ್ತ ಒತ್ತಡ ⟨blood pressure⟩, ವಾತಾವರಣದ ಒತ್ತಡ |
| leaf | Rushed | **ಆತುರ** | *ātura* | `shaped` | ಧಾವಿಸು, ಮುನ್ನುಗ್ಗು, ತೀವ್ರಗತಿ |
| branch | Stressed | **ತಳಮಳ** | *taḷamaḷa* | `shaped` | ಒತ್ತಡ, ಪ್ರತಿಬಲ ⟨tensile stress⟩, ಕರ್ತನ ಪ್ರತಿಬಲ ⟨shear stress⟩ |
| leaf | Overwhelmed | **ಹೈರಾಣ** | *hairāṇa* | `shaped` | ಮುಳುಗಿಹೋಗು, ಭಾವಪರವಶಗೊಳ್ಳು |
| leaf | Restless | **ಚಡಪಡಿಕೆ** | *caḍapaḍike* | `direct` | ಚಡಪಡಿಸುವ, ತಳಮಳ, ವ್ಯಾಕುಲ, ಅಶಾಂತ |
| branch | Tired | **ಆಯಾಸ** | *āyāsa* | `shaped` | ದಣಿದ ಮಣ್ಣು ⟨tired soil⟩ |
| leaf | Sleepy | **ಜೋಂಪು** | *jōmpu* | `shaped` | ತೂಕಡಿಸುವ, ನಿದ್ದೆ, ಜಡನಾದ |
| leaf | Unfocused | **ಅನ್ಯಮನಸ್ಕ** | *anya-manaska* | `direct` | ಅನ್ಯಮನಸ್ಕ, ಏಕಾಗ್ರತೆಯಿಲ್ಲದ, ಮರೆಗುಳಿ |

<details><summary>Reading — why these words and not the dictionary's</summary>

- **ಬೇಸರ** *(Bad)* — The hardest sector. Kannada's ಕೆಟ್ಟ is moral or qualitative — a bad man, spoiled milk — and cannot be a feeling. But look at what the English wheel actually files under 'Bad': bored, busy, stressed, tired. That whole zone has one Kannada name, ಬೇಸರ — a fused weariness-with-things that English needs four words to circle.
- **ಬೇಜಾರು** *(Bored)* — No entry for *boredom*. ಬೇಜಾರು covers bored, mildly sad, and fed-up in one breath. 'ಬೇಜಾರಾಗಿದೆ' could be any of the three and the listener works it out from your face.
- **ಉದಾಸೀನ** *(Indifferent)* — In philosophy ಉದಾಸೀನ is the sage's equanimity. In an argument it is the coldest insult available.
- **ಧಾವಂತ** *(Busy)* — rala's words describe a schedule. ಧಾವಂತ describes what the schedule does to you — the harried forward-lean of someone always mid-errand.
- **ಒತ್ತಡ** *(Pressured)* — Same word for atmospheric pressure, blood pressure, and social pressure. Kannada did not borrow 'stress' — it extended 'push'.
- **ಆತುರ** *(Rushed)* — ಆತುರ is haste as a character flaw as much as a state — 'ಆತುರಗಾರನಿಗೆ ಬುದ್ಧಿ ಮಟ್ಟ', the hasty man is short on sense.
- **ತಳಮಳ** *(Stressed)* — Every single hit was materials engineering. ತಳಮಳ is the churn — the word for boiling liquid and for a mind that will not settle.
- **ಹೈರಾಣ** *(Overwhelmed)* — English uses one *overwhelmed* in two places on this wheel. Kannada splits them by how you are swamped: ಹೈರಾಣ is worn down to nothing by too much work; ಕಳವಳ, over in ಭಯ, is being swamped by dread.
- **ಚಡಪಡಿಕೆ** *(Restless)* — Onomatopoeic — the sound of a fish on dry ground, or a body that cannot stay in the chair.
- **ಆಯಾಸ** *(Tired)* — The only match was agronomy: exhausted soil. ಆಯಾಸ is bodily fatigue; ದಣಿವು is the gentler, more native version.
- **ಜೋಂಪು** *(Sleepy)* — ಜೋಂಪು is the specific drowse that comes over you sitting still in the afternoon — not sleep, the slide toward it.
- **ಅನ್ಯಮನಸ್ಕ** *(Unfocused)* — 'Other-minded' — your mind is somewhere, just not here. Kinder than 'distracted', which implies something pulled you.

</details>

### ಭಯ · Fearful — *bhaya*

| ring | English | ಕನ್ನಡ | roman | status | rala's hits |
|---|---|---|---|---|---|
| core | Fearful | **ಭಯ** | *bhaya* | `direct` | ಭಯ, ಹೆದರಿಕೆ, ಅಂಜಿಕೆ, ಭೀತಿ, ದಿಗಿಲು, ಆತಂಕ, ಗಾಬರಿ |
| branch | Scared | **ಹೆದರಿಕೆ** | *hedarike* | `direct` | ಹೆದರಿಕೆ, ಗಾಬರಿ, ಭೀತಿ, ಬೆದರುಗೊಂಬೆ ⟨scarecrow⟩ |
| leaf | Helpless | **ಅಸಹಾಯಕತೆ** | *asahāyakate* | `direct` | ಅಸಹಾಯಕ, ದಿಕ್ಕಿಲ್ಲದ, ತಬ್ಬಲಿ |
| leaf | Frightened | **ಅಂಜಿಕೆ** | *añjike* | `direct` | ಹೆದರಿಸು, ಭಯಪಡಿಸು, ದಿಗಿಲುಗೊಳಿಸು |
| branch | Anxious | **ಆತಂಕ** | *ātaṅka* | `direct` | ಆತಂಕಗೊಂಡ, ವ್ಯಾಕುಲತೆ, ಚಿಂತಾಕ್ರಾಂತ, ತಲ್ಲಣಗೊಂಡ |
| leaf | Worried | **ಚಿಂತೆ** | *cinte* | `direct` | ಚಿಂತೆ, ಕಳವಳ, ಆತಂಕ, ಪೇಚಾಟ |
| leaf | Overwhelmed | **ಕಳವಳ** | *kaḷavaḷa* | `shaped` | ಕಳವಳಗೊಂಡ, ವ್ಯಾಕುಲ |
| branch | Insecure | **ಅಭದ್ರತೆ** | *abhadrate* | `direct` | ಅಭದ್ರ, ಅಸುರಕ್ಷಿತ, ರಕ್ಷಣೆ ರಹಿತ |
| leaf | Inadequate | **ಕೊರತೆ** | *korate* | `shaped` | ಸಾಕಾಗದ, ಅಸಮರ್ಥ, ಕೊರತೆಯುಳ್ಳ |
| leaf | Inferior | **ಕೀಳರಿಮೆ** | *kīḷarime* | `shaped` | ಕೀಳು, ಕಳಪೆ, ಕೆಳದರ್ಜೆಯ |
| branch | Weak | **ದುರ್ಬಲ** | *durbala* | `direct` | ದುರ್ಬಲ, ಬಲಹೀನ, ನಿರ್ಬಲ |
| leaf | Worthless | **ನಿಷ್ಪ್ರಯೋಜಕ** | *niṣprayōjaka* | `shaped` | ಅಯೋಗ್ಯ |
| leaf | Insignificant | **ಕ್ಷುಲ್ಲಕ** | *kṣullaka* | `direct` | ಕ್ಷುಲ್ಲಕ, ಅತ್ಯಲ್ಪ, ನಿಕೃಷ್ಟ |
| branch | Rejected | **ತಿರಸ್ಕಾರ** | *tiraskāra* | `shaped` | ಸೋತ ಅಭ್ಯರ್ಥಿ ⟨rejected candidate⟩, ತಿರಸ್ಕರಿಸತಕ್ಕದ್ದು, ಹಕ್ಕು ಸಾಧನೆಗಳು ⟨rejected claims⟩ |
| leaf | Excluded | **ಬಹಿಷ್ಕಾರ** | *bahiṣkāra* | `gap` | — |
| leaf | Persecuted | **ಕಿರುಕುಳ** | *kirukuḷa* | `direct` | ಕಿರುಕುಳ ಕೊಡು, ಪೀಡಿಸು, ಹಿಂಸಿಸು |
| branch | Threatened | **ಬೆದರಿಕೆ** | *bedarike* | `gap` | — |
| leaf | Nervous | **ನಡುಕ** | *naḍuka* | `shaped` | ನಡುಗುವ, ಅಂಜುಬುರುಕ, ನರವ್ಯೂಹ ⟨nervous system⟩ |
| leaf | Exposed | **ಬಟಾಬಯಲು** | *baṭā-bayalu* | `shaped` | ಗುಟ್ಟುರಟ್ಟಾದ, ಸುರಕ್ಷಣೆ ಇಲ್ಲದ, ಬಹಿರಂಗಗೊಳಿಸಿದ |

<details><summary>Reading — why these words and not the dictionary's</summary>

- **ಭಯ** *(Fearful)* — rala's richest sector — seven distinct words on the first page. Kannada grades fear finely: ಅಂಜಿಕೆ (timid), ಹೆದರಿಕೆ (scared), ದಿಗಿಲು (dread), ಗಾಬರಿ (panic), ಆತಂಕ (anxiety), ಭೀತಿ (terror).
- **ಅಸಹಾಯಕತೆ** *(Helpless)* — rala's ದಿಕ್ಕಿಲ್ಲದ is better than the headword: 'without a direction'. Helplessness as having nowhere to turn — literally no compass point.
- **ಆತಂಕ** *(Anxious)* — ಆತಂಕ is now the standard clinical word too. Its older sense is closer to 'impediment' — anxiety as the thing in your way.
- **ಚಿಂತೆ** *(Worried)* — ಚಿಂತೆ is also simply 'thought'. To worry and to think are the same verb, which tells you something.
- **ಕಳವಳ** *(Overwhelmed)* — The second of the split — see ಹೈರಾಣ under ಬೇಸರ. ಕಳವಳ is being flooded by apprehension rather than by workload.
- **ಅಭದ್ರತೆ** *(Insecure)* — Note the frame: Kannada's insecurity is about not being *guarded*, not about self-doubt. The psychological sense is a recent import.
- **ಕೊರತೆ** *(Inadequate)* — ಕೊರತೆ is a shortfall — of rain, of funds, of oneself. The same word, which quietly makes it feel less like a personal verdict.
- **ಕೀಳರಿಮೆ** *(Inferior)* — rala gives only the judgement (ಕೀಳು, low-grade). ಕೀಳರಿಮೆ is the feeling — 'low-self-knowing', the exact and rather beautiful Kannada for an inferiority complex.
- **ನಿಷ್ಪ್ರಯೋಜಕ** *(Worthless)* — rala offers ಅಯೋಗ್ಯ — but in Kannada that is thrown at someone, not felt about oneself. ನಿಷ್ಪ್ರಯೋಜಕ, 'of no use', is what the feeling actually says.
- **ತಿರಸ್ಕಾರ** *(Rejected)* — ತಿರಸ್ಕಾರ is what the other person did. As with ಒಪ್ಪಿಗೆ, Kannada gives you no noun for the receiving end — rejection is only ever described from outside.
- **ಬಹಿಷ್ಕಾರ** *(Excluded)* — No entry. And ಬಹಿಷ್ಕಾರ is heavier than English 'excluded' — it is the word for social boycott and outcasting. In Kannada, being left out has a history attached to it.
- **ಬೆದರಿಕೆ** *(Threatened)* — No entry for the adjective. ಬೆದರಿಕೆ is the threat itself; feeling threatened is said as ಬೆದರಿಕೆ ಇದೆ — 'there is a threat' — placing it outside you rather than inside.
- **ನಡುಕ** *(Nervous)* — Most hits were neuroanatomy. ನಡುಕ is the tremble itself — Kannada again naming the body and letting the feeling follow.
- **ಬಟಾಬಯಲು** *(Exposed)* — ಬಟಾಬಯಲು is open ground with not one thing to hide behind — used for landscape and for people, with no change of tone.

</details>

### ಕೋಪ · Angry — *kōpa*

| ring | English | ಕನ್ನಡ | roman | status | rala's hits |
|---|---|---|---|---|---|
| core | Angry | **ಕೋಪ** | *kōpa* | `direct` | ಕೋಪ, ಸಿಟ್ಟು, ಸಿಡುಕು, ರೋಷ, ಮುನಿಸು, ಕ್ರೋಧ, ತಾಪ |
| branch | Let down | **ಕೈಕೊಟ್ಟರು** | *kai-koṭṭaru* | `gap` | ಹಾಲೊಸರಿಕೆ ⟨milk let-down⟩ |
| leaf | Betrayed | **ದ್ರೋಹ** | *drōha* | `direct` | ದ್ರೋಹ ಮಾಡು, ವಿಶ್ವಾಸಘಾತ, ವಂಚಿಸು |
| leaf | Resentful | **ಅಸಮಾಧಾನ** | *asamādhāna* | `direct` | ಅಸಮಾಧಾನ, ಜಿದ್ದು, ಕರುಬು, ಹಗೆತನ |
| branch | Humiliated | **ಅವಮಾನ** | *avamāna* | `direct` | ಅವಮಾನಿಸು, ತೇಜೋವಧೆ, ಮರ್ಯಾದೆ ಕಳೆ |
| leaf | Disrespected | **ಅಗೌರವ** | *agaurava* | `direct` | ಅಗೌರವ, ಅವಮಾನ, ಉಪೇಕ್ಷೆ, ಅವಮರ್ಯಾದೆ |
| leaf | Ridiculed | **ಅಪಹಾಸ್ಯ** | *apahāsya* | `direct` | ಅಪಹಾಸ್ಯ, ಗೇಲಿ, ಅವಹೇಳನ, ಅಣಕಿಸು |
| branch | Bitter | **ಕಹಿ** | *kahi* | `shaped` | ಹಾಗಲಕಾಯಿ ⟨bitter gourd⟩, ಕಹಿಗುಳಿಗೆ ⟨bitter pill⟩, ಕ್ರೂರ, ಕಠಿಣ |
| leaf | Indignant | **ಆಕ್ರೋಶ** | *ākrōśa* | `shaped` | ಕುಪಿತ, ಕೆರಳಿದ, ರೇಗಿದ |
| leaf | Violated | **ಭಂಗ** | *bhaṅga* | `gap` | ಉಲ್ಲಂಘಿಸು ⟨violate a rule⟩, ಮಾನಭಂಗ ⟨sexual assault⟩ |
| branch | Mad | **ಸಿಟ್ಟು** | *siṭṭu* | `direct` | ಸಿಟ್ಟು, ಹುಚ್ಚು ⟨insane⟩, ಮತಿಗೆಟ್ಟ |
| leaf | Furious | **ರೋಷ** | *rōṣa* | `direct` | ರೋಷಾವೇಶದ, ಕ್ರೋಧಾವಿಷ್ಟ, ಉಗ್ರ, ಪ್ರಚಂಡ |
| leaf | Jealous | **ಹೊಟ್ಟೆಕಿಚ್ಚು** | *hoṭṭe-kiccu* | `shaped` | ಅಸೂಯೆಯ, ಮಾತ್ಸರ್ಯದ |
| branch | Aggressive | **ಆಕ್ರಮಣ** | *ākramaṇa* | `direct` | ಆಕ್ರಮಣಶೀಲ, ಜಗಳಗಂಟ, ಮೇಲೆ ಬೀಳುವ |
| leaf | Provoked | **ಕೆರಳಿಕೆ** | *keraḷike* | `direct` | ಕೆರಳಿಸು, ಕೆಣಕು, ಪ್ರಚೋದಿಸು, ರೇಗಿಸು |
| leaf | Hostile | **ಹಗೆತನ** | *hagetana* | `direct` | ಹಗೆಯ, ವೈರದ, ಶತ್ರುತ್ವದ, ಪ್ರತಿಕೂಲ |
| branch | Frustrated | **ರೇಜಿಗೆ** | *rējige* | `shaped` | ಆಶಾಭಂಗ ಹೊಂದಿದ, ವಿಫಲವಾದ, ಭಗ್ನ, ನಿಷ್ಫಲಗೊಳಿಸು |
| leaf | Infuriated | **ಕೆಂಡಾಮಂಡಲ** | *keṇḍā-maṇḍala* | `shaped` | ರೇಗಿಸು, ಕೆರಳಿಸು |
| leaf | Annoyed | **ಕಿರಿಕಿರಿ** | *kirikiri* | `direct` | ಕಿರಿಕಿರಿಮಾಡು, ರೇಗಿಸು, ಕಾಡಿಸು |
| branch | Distant | **ಬಿಗುಮಾನ** | *bigumāna* | `direct` | ಬಿಗುಮಾನದ, ಸಲಿಗೆ ಇಲ್ಲದ, ದೂರದ |
| leaf | Withdrawn | **ಮುದುಡು** | *muduḍu* | `shaped` | ವಾಪಸ್ಸು ಪಡೆದ ⟨withdrawn application⟩, ಹಿಂದಕ್ಕೆ ಪಡೆದ |
| leaf | Numb | **ಮರಗಟ್ಟುವಿಕೆ** | *maragaṭṭuvike* | `direct` | ಮರಗಟ್ಟಿದ, ಜೋಮುಹಿಡಿದ, ಜಡವಾದ |
| branch | Critical | **ಟೀಕೆ** | *ṭīke* | `shaped` | ಕ್ರಾಂತಿಕೋನ ⟨critical angle⟩, ವಿಷಮ ಮೌಲ್ಯ ⟨critical value⟩, ವಿಮರ್ಶಾತ್ಮಕ |
| leaf | Skeptical | **ಅನುಮಾನ** | *anumāna* | `direct` | ಅನುಮಾನ, ಸಂಶಯ, ಸಂದೇಹ, ಶಂಕೆ |
| leaf | Dismissive | **ಉಡಾಫೆ** | *uḍāphe* | `shaped` | ತಳ್ಳಿಹಾಕು, ನಿರ್ಲಕ್ಷಿಸು, ವಜಾ ಮಾಡು ⟨dismiss from service⟩ |

<details><summary>Reading — why these words and not the dictionary's</summary>

- **ಕೋಪ** *(Angry)* — Kannada separates anger by heat and by intimacy: ಸಿಟ್ಟು is hot and quick, ಕೋಪ is the general word, ಕ್ರೋಧ is grand and destructive, ಸಿಡುಕು is chronic and worn on the face — and ಮುನಿಸು is the anger you only get to have with someone who loves you.
- **ಕೈಕೊಟ್ಟರು** *(Let down)* — rala's single match for *let down* is the dairy term for milk ejection. Kannada has no noun here either — you say ಕೈಕೊಟ್ಟರು, 'they gave me the hand', meaning they withdrew it at the moment you leaned on it.
- **ದ್ರೋಹ** *(Betrayed)* — ದ್ರೋಹ is grave — the word used for treason and for betraying a guru. Kannada does not have a casual register for this.
- **ಅಸಮಾಧಾನ** *(Resentful)* — Literally 'un-settledness' — the negation of ಸಮಾಧಾನ, consolation. Resentment as a grievance that was never talked down.
- **ಅವಮಾನ** *(Humiliated)* — rala's ತೇಜೋವಧೆ is worth keeping: 'the murder of someone's lustre'. Humiliation as an assassination of light.
- **ಅಪಹಾಸ್ಯ** *(Ridiculed)* — ಅಪಹಾಸ್ಯ is 'laughter turned bad' — the same root as ಹಾಸ್ಯ, mirth, which is one of the nine rasas. The wound is that a good thing was aimed at you.
- **ಕಹಿ** *(Bitter)* — rala gives mostly vegetables. But the metaphor is alive in Kannada too — ಮನಸ್ಸಿನಲ್ಲಿ ಕಹಿ, bitterness in the mind — so the taste-word earns its place here on its own terms, not as a calque.
- **ಆಕ್ರೋಶ** *(Indignant)* — rala's words are plain anger. ಆಕ್ರೋಶ is anger with a case to argue — literally an outcry, the anger of protest.
- **ಭಂಗ** *(Violated)* — A real hole. rala's options are either legal (breaking a rule) or the specific term for sexual assault. There is no neutral Kannada for 'I feel violated' — the therapeutic middle register simply hasn't been built yet.
- **ಸಿಟ್ಟು** *(Mad)* — English 'mad' means both furious and insane; so does rala's answer set. Kannada keeps them apart cleanly — ಸಿಟ್ಟು is anger, ಹುಚ್ಚು is madness, and no one confuses them.
- **ಹೊಟ್ಟೆಕಿಚ್ಚು** *(Jealous)* — rala's ಅಸೂಯೆ and ಮಾತ್ಸರ್ಯ are correct and literary. But nobody says them at home. They say ಹೊಟ್ಟೆಕಿಚ್ಚು — belly-fire — and everyone knows exactly which organ is burning.
- **ಆಕ್ರಮಣ** *(Aggressive)* — The full adjective is ಆಕ್ರಮಣಶೀಲ, shortened here to fit. rala's ಜಗಳಗಂಟ — 'quarrel-knot', a person who ties fights — is the everyday version.
- **ಕೆರಳಿಕೆ** *(Provoked)* — ಕೆಣಕು is the good one: to poke a thing that was sitting quietly.
- **ಹಗೆತನ** *(Hostile)* — ಹಗೆ is the old native word for enemy, and it is heavy — the enmity of feuds and epics, not of office politics.
- **ರೇಜಿಗೆ** *(Frustrated)* — rala reads *frustrate* as 'to thwart' — an outcome. Frustration as an ongoing state is ರೇಜಿಗೆ: exasperation at something that keeps not working.
- **ಕೆಂಡಾಮಂಡಲ** *(Infuriated)* — 'A whole mandala of live coals.' One of the finest anger words in the language, and unfindable from English.
- **ಕಿರಿಕಿರಿ** *(Annoyed)* — Onomatopoeia again — the sound of a small grating thing. Kannada builds its minor irritations out of noise.
- **ಬಿಗುಮಾನ** *(Distant)* — rala found it exactly. ಬಿಗುಮಾನ is stiffness held on purpose — reserve that is also a kind of self-regard. And note its opposite in rala's own list: ಸಲಿಗೆ ಇಲ್ಲದ, 'without ಸಲಿಗೆ'.
- **ಮುದುಡು** *(Withdrawn)* — rala only knows withdrawn tenders. ಮುದುಡು is what a leaf or a touched mimosa does — to fold inward. Exactly right for a person.
- **ಮರಗಟ್ಟುವಿಕೆ** *(Numb)* — ಮರ + ಕಟ್ಟು: to turn to wood. Used for a foot that has gone to sleep and for a grief that has stopped registering.
- **ಟೀಕೆ** *(Critical)* — Physics and statistics, mostly. ಟೀಕೆ is fault-finding; ವಿಮರ್ಶೆ, also in the list, is the honourable kind — literary criticism. Kannada distinguishes the two, English does not.
- **ಅನುಮಾನ** *(Skeptical)* — Four graded words for doubt. ಶಂಕೆ leans toward fear, ಸಂಶಯ toward suspicion of a person, ಸಂದೇಹ toward uncertainty about a fact.
- **ಉಡಾಫೆ** *(Dismissive)* — ಉಡಾಫೆ is dismissiveness worn as a style — breezy, unbothered, faintly insulting. ಅಸಡ್ಡೆ and ತಾತ್ಸಾರ are the colder cousins.

</details>

### ಅಸಹ್ಯ · Disgusted — *asahya*

| ring | English | ಕನ್ನಡ | roman | status | rala's hits |
|---|---|---|---|---|---|
| core | Disgusted | **ಅಸಹ್ಯ** | *asahya* | `direct` | ಅಸಹ್ಯ, ಜಿಗುಪ್ಸೆ, ಹೇಸಿಕೆ, ರೋಸು, ವಾಕರಿಕೆ |
| branch | Disapproving | **ಅಸಮ್ಮತಿ** | *asammati* | `direct` | ಅಸಮ್ಮತಿ, ಮೆಚ್ಚದಿರು, ಒಪ್ಪದಿರು |
| leaf | Judgmental | **ಕೊಂಕು** | *koṅku* | `shaped` | ನ್ಯಾಯಾಧೀಶ ⟨judge⟩, ಜಿಲ್ಲಾ ನ್ಯಾಯಾಧೀಶ ⟨district judge⟩, ಖಂಡನೆ |
| leaf | Embarrassed | **ಮುಜುಗರ** | *mujugara* | `direct` | ಮುಜುಗರ ಉಂಟಾದ |
| branch | Disappointed | **ನಿರಾಸೆ** | *nirāse* | `direct` | ನಿರಾಶೆಗೊಂಡ, ಆಶಾಭಂಗ, ಹತಾಶೆ |
| leaf | Appalled | **ದಿಗ್ಭ್ರಮೆ** | *digbhrame* | `direct` | ದಿಗ್ಭ್ರಮೆಗೊಂಡ, ಭೀತ, ಗಾಬರಿಗೊಂಡ |
| leaf | Revolted | **ರೋಸು** | *rōsu* | `shaped` | ದಂಗೆ ⟨rebellion⟩, ಬಂಡಾಯ, ವಿದ್ರೋಹ |
| branch | Awful | **ಅಸಹನೀಯ** | *asahanīya* | `shaped` | ಭಯಾನಕವಾದ, ಭೀಕರ |
| leaf | Nauseated | **ವಾಕರಿಕೆ** | *vākarike* | `direct` | ವಾಕರಿಕೆ, ಓಕರಿಕೆ, ಹೊಟ್ಟೆ ತೊಳಸು |
| leaf | Detestable | **ಹೇಸಿಗೆ** | *hēsige* | `direct` | ಹೇಸು, ಅಸಹ್ಯಪಡು, ಹೇಸಿಗೆ ಪಡು |
| branch | Repelled | **ಜಿಗುಪ್ಸೆ** | *jigupse* | `direct` | ಜಿಗುಪ್ಸೆಗೊಳಿಸು, ಹಿಮ್ಮೆಟ್ಟಿಸು, ವಿಕರ್ಷಿಸು |
| leaf | Horrified | **ದಿಗಿಲು** | *digilu* | `direct` | ದಿಗಿಲುಗೊಳಿಸು, ಭಯಹುಟ್ಟಿಸು, ದಿಕ್ಕುಗೆಡಿಸು |
| leaf | Hesitant | **ಹಿಂಜರಿಕೆ** | *hiñjarike* | `direct` | ಹಿಂಜರಿಯುವ, ಹಿಮ್ಮೆಟ್ಟುವ, ಶಂಕೆಯುಳ್ಳ |

<details><summary>Reading — why these words and not the dictionary's</summary>

- **ಅಸಹ್ಯ** *(Disgusted)* — ಅಸಹ್ಯ literally means 'unbearable' — what cannot be borne. Kannada files disgust under endurance rather than under taste.
- **ಕೊಂಕು** *(Judgmental)* — rala went straight to the judiciary. ಕೊಂಕು is the crooked remark — fault-finding delivered sideways, which is how it usually arrives.
- **ಮುಜುಗರ** *(Embarrassed)* — ಮುಜುಗರ is social awkwardness — the wince at a scene, often on someone else's behalf.
- **ನಿರಾಸೆ** *(Disappointed)* — ನಿರಾಸೆ = ನಿರ್ + ಆಸೆ, de-hoped. ಆಶಾಭಂಗ, also offered, is stronger: hope actually broken.
- **ದಿಗ್ಭ್ರಮೆ** *(Appalled)* — 'Directions-confusion' — the compass spins. Shock that leaves you not knowing which way is which.
- **ರೋಸು** *(Revolted)* — rala took *revolt* politically — every hit is an uprising. ರೋಸಿಹೋಗಿದೆ is the feeling: fed up to the point of nausea.
- **ಅಸಹನೀಯ** *(Awful)* — rala's answers mean terrifying, which is *awe*-ful in the old sense. The modern 'this is awful' is ಅಸಹನೀಯ — unendurable.
- **ವಾಕರಿಕೆ** *(Nauseated)* — ಹೊಟ್ಟೆ ತೊಳಸು — 'the stomach stirs'. Kannada has a full vocabulary for the gut, and uses it for feelings without apology.
- **ಹೇಸಿಗೆ** *(Detestable)* — ಹೇಸಿಗೆ is also literally filth. The moral and the physical are the same word — no metaphor required.
- **ಜಿಗುಪ್ಸೆ** *(Repelled)* — ಜಿಗುಪ್ಸೆ is world-weary revulsion — the disgust that makes people renounce things, not just push a plate away.
- **ಹಿಂಜರಿಕೆ** *(Hesitant)* — ಹಿಂಜರಿ — to slide backwards. The foot that starts to move and then doesn't.

</details>

### ದುಃಖ · Sad — *duḥkha*

| ring | English | ಕನ್ನಡ | roman | status | rala's hits |
|---|---|---|---|---|---|
| core | Sad | **ದುಃಖ** | *duḥkha* | `direct` | ದುಃಖಕರ, ವಿಷಾದಕರ, ಶೋಚನೀಯ, ಕುಗ್ಗಿದ, ಸೊರಗಿದ, ಅಮಂಗಳ ⟨inauspicious⟩ |
| branch | Lonely | **ಒಂಟಿತನ** | *oṇṭitana* | `direct` | ಒಂಟಿ, ಏಕಾಂಗಿ, ಒಬ್ಬನೇ |
| leaf | Isolated | **ಏಕಾಂಗಿತನ** | *ēkāṅgitana* | `shaped` | ಪ್ರತ್ಯೇಕಿಸಿದ, ಬೇರ್ಪಡಿಸಿದ, ಪ್ರತ್ಯೇಕ ಸ್ಥಳ |
| leaf | Abandoned | **ತಬ್ಬಲಿತನ** | *tabbalitana* | `shaped` | ತೊರೆದ ಪ್ರದೇಶ ⟨abandoned area⟩, ತಬ್ಬಲಿ |
| branch | Vulnerable | **ದುರ್ಬಲತೆ** | *durbalate* | `gap` | ಸುಭೇದ್ಯ, ಭೇದ್ಯ, ದುರ್ಬಲ ಸ್ಥಿತಿ ⟨vulnerable stage⟩ |
| leaf | Victimised | **ಬಲಿಪಶು** | *balipaśu* | `direct` | ಬಲಿಪಶುಮಾಡು, ಪೀಡಿಸು, ಸತಾಯಿಸು |
| leaf | Fragile | **ನಾಜೂಕು** | *nājūku* | `direct` | ನಾಜೂಕಾದ, ಭಂಗುರ, ಶಿಥಿಲ |
| branch | Despair | **ಹತಾಶೆ** | *hatāśe* | `direct` | ಹತಾಶೆ, ನಿರಾಶೆ, ಎದೆಗುಂದು, ಆಸೆಗೆಡು |
| leaf | Grief | **ಅಳಲು** | *aḷalu* | `direct` | ಅಳಲು, ಶೋಕ, ಸಂಕಟ, ಕೊರಗು, ವ್ಯಥೆ |
| leaf | Powerless | **ಕೈಲಾಗದತನ** | *kailāgadatana* | `shaped` | ಶಕ್ತಿಹೀನ, ಬಲಹೀನ, ದುರ್ಬಲ |
| branch | Guilty | **ಪಾಪಪ್ರಜ್ಞೆ** | *pāpa-prajñe* | `shaped` | ಅಪರಾಧಿ, ತಪ್ಪಿತಸ್ಥ, ದೋಷಿ, ಅಪರಾಧಿ ಮನೋಭಾವ ⟨guilty mind⟩ |
| leaf | Ashamed | **ನಾಚಿಕೆ** | *nāchike* | `shaped` | ಅವಮಾನಗೊಂಡ, ಮಾನಗೆಟ್ಟ |
| leaf | Remorseful | **ಪಶ್ಚಾತ್ತಾಪ** | *paścāttāpa* | `direct` | ಪಶ್ಚಾತ್ತಾಪ, ಅನುತಾಪ, ಮರುಕ |
| branch | Depressed | **ಖಿನ್ನತೆ** | *khinnate* | `shaped` | ದಲಿತ ವರ್ಗ ⟨depressed classes⟩, ಶೋಷಿತ, ಕುಗ್ಗಿದ, ನಿರುತ್ಸಾಹದ |
| leaf | Inferior | **ಕುಗ್ಗುವಿಕೆ** | *kugguvike* | `shaped` | ಕುಗ್ಗಿದ, ಇಳಿದ, ತಗ್ಗಿದ |
| leaf | Empty | **ಬರಿದುತನ** | *bariduṭana* | `shaped` | ಬರಿದು, ಖಾಲಿ, ಪೊಳ್ಳು, ಶೂನ್ಯ |
| branch | Hurt | **ನೋವು** | *nōvu* | `direct` | ನೋವು, ನೋಯಿಸು, ಗಾಯ, ಸಾಧಾರಣ ಗಾಯ ⟨simple hurt, IPC⟩ |
| leaf | Disappointed | **ಆಶಾಭಂಗ** | *āśābhaṅga* | `direct` | ಆಶಾಭಂಗ, ನಿರಾಶೆಗೊಂಡ |
| leaf | Embarrassed | **ಸಂಕೋಚ** | *saṅkōca* | `shaped` | ಮುಜುಗರ ಉಂಟಾದ |

<details><summary>Reading — why these words and not the dictionary's</summary>

- **ದುಃಖ** *(Sad)* — Note ಅಶುಭ / ಅಮಂಗಳ in rala's list — 'inauspicious'. For a large part of Kannada usage, sadness and bad omen are adjacent ideas; a sad event is an unlucky one.
- **ಒಂಟಿತನ** *(Lonely)* — Kannada draws a line English blurs: ಒಂಟಿತನ is loneliness and it hurts; ಏಕಾಂತ is solitude, chosen, and is good for you. Same 'alone', opposite verdicts.
- **ಏಕಾಂಗಿತನ** *(Isolated)* — rala's words are all quarantine and land-parcels. ಏಕಾಂಗಿ is 'single-bodied' — cut off with no one on your side.
- **ತಬ್ಬಲಿತನ** *(Abandoned)* — ತಬ್ಬಲಿ means orphan, and it is used far past its literal sense — for anyone left without their people. One of the saddest words in the language.
- **ದುರ್ಬಲತೆ** *(Vulnerable)* — The clearest gap on the wheel. Every Kannada option means weak, breachable, at risk — all pejorative. The warm English sense of 'vulnerable', where opening up is a strength, has no Kannada word yet; people say ಮನಸ್ಸು ತೆರೆದಿಡುವುದು, 'to keep the mind open', as a description rather than a name.
- **ಬಲಿಪಶು** *(Victimised)* — 'Sacrificial animal'. Kannada's word for victim comes straight off the altar.
- **ನಾಜೂಕು** *(Fragile)* — ನಾಜೂಕು is fragile-and-fine, a compliment about a person's delicacy. ಭಂಗುರ is the philosophical one: that which is destined to break.
- **ಹತಾಶೆ** *(Despair)* — ಹತ + ಆಶೆ: hope, killed. The word contains the murder.
- **ಅಳಲು** *(Grief)* — rala's whole list is worth reading: ಶೋಕ is formal mourning, ಸಂಕಟ is the chest-squeeze, ಕೊರಗು is the grief that thins you over years, ಅಳಲು is the wail itself.
- **ಕೈಲಾಗದತನ** *(Powerless)* — rala offers strength-less. ಕೈಲಾಗದತನ is the spoken form: 'the state of the hands not managing it'.
- **ಪಾಪಪ್ರಜ್ಞೆ** *(Guilty)* — Every hit is courtroom Kannada — the accused, the convicted. The inner feeling had to be named religiously instead: ಪಾಪಪ್ರಜ್ಞೆ, sin-consciousness. Kannada's guilt is borrowed either from law or from temple; it has no private word of its own.
- **ನಾಚಿಕೆ** *(Ashamed)* — ನಾಚಿಕೆ is one word for shyness, modesty and shame — a bride's ನಾಚಿಕೆ and a thief's are the same noun. English needs three words and grades them differently; Kannada trusts context completely.
- **ಪಶ್ಚಾತ್ತಾಪ** *(Remorseful)* — 'After-heat' — the burn that arrives once the act is over.
- **ಖಿನ್ನತೆ** *(Depressed)* — A striking result: rala's first hits for *depressed* are ದಲಿತ and ಶೋಷಿತ — the colonial administrative phrase 'depressed classes'. The clinical word ಖಿನ್ನತೆ is recent; older Kannada said ಮನಸ್ಸು ಕುಗ್ಗಿದೆ, 'the mind has shrunk'.
- **ಕುಗ್ಗುವಿಕೆ** *(Inferior)* — The English wheel repeats 'inferior' in two branches. Kannada usefully doesn't: under fear it is ಕೀಳರಿಮೆ, a belief about your rank; here under sadness it is ಕುಗ್ಗುವಿಕೆ, simply shrinking.
- **ಬರಿದುತನ** *(Empty)* — rala's ಪೊಳ್ಳು is the good one — hollow, like a grain with nothing inside it. Used of people who look intact.
- **ನೋವು** *(Hurt)* — ನೋವು is bodily pain and emotional pain with no distinction at all. 'ಮನಸ್ಸಿಗೆ ನೋವಾಯಿತು' — it hurt my mind — is the ordinary way to say you were wounded.
- **ಆಶಾಭಂಗ** *(Disappointed)* — The second 'disappointed' on the wheel. ನಿರಾಸೆ over in ಅಸಹ್ಯ is hope that faded; ಆಶಾಭಂಗ is hope that snapped.
- **ಸಂಕೋಚ** *(Embarrassed)* — The other 'embarrassed'. ಮುಜುಗರ is the wince at a social scene; ಸಂಕೋಚ is the shrinking-in-on-yourself, the hesitation to ask, to take, to take up room.

</details>

## ಕನ್ನಡದ್ದೇ ಪದಗಳು — words with nowhere to sit on the wheel

Feelings Kannada names precisely and English can only paraphrase. The wheel is an English object; these are the argument for redrawing one rather than translating it.

| ಕನ್ನಡ | roman | what it means |
|---|---|---|
| **ಮುನಿಸು** | *munisu* | The sulk you are only entitled to with someone who loves you. Anger that wants soothing, not resolution — and would be insulted by an apology that was merely correct. |
| **ಸಲಿಗೆ** | *salige* | The earned licence to be informal with a person: to tease them, eat off their plate, drop the honorific. Intimacy defined as permission rather than as feeling. |
| **ಹೊಟ್ಟೆಕಿಚ್ಚು** | *hoṭṭe-kiccu* | Belly-fire. Envy at someone else's good fortune, located precisely in the stomach — and said out loud, cheerfully, in a way English envy never is. |
| **ಕರುಳು ಚುರುಕ್** | *karuḷu curuk* | 'The intestine stings.' The involuntary gut-twinge of compassion on seeing a child or an animal in distress. Not pity — pity is a judgement; this is a reflex. |
| **ಸಂಕಟ** | *saṅkaṭa* | Anguish felt as constriction — the chest closing. Used equally for a dying person's distress, a moral dilemma, and unbearable news. |
| **ಕಸಿವಿಸಿ** | *kasivisi* | The small squirm when something is subtly off: an unwelcome guest, a joke that landed wrong. Too minor for 'discomfort', too bodily for 'unease'. |
| **ಚಡಪಡಿಕೆ** | *caḍapaḍike* | The fidget of waiting — a body that cannot stay in the chair. Onomatopoeic, and used for a fish out of water without any sense of metaphor. |
| **ವಾತ್ಸಲ್ಯ** | *vātsalya* | Tenderness that flows downward only: parent to child, elder to younger, teacher to student. English 'love' has no direction; this word is nothing but direction. |
| **ಅಭಿಮಾನ** | *abhimāna* | Pride-as-loyalty — for your language, your team, your people. Its second sense is the wound when that loyalty is slighted, so the same word holds the devotion and the injury. |
| **ಸಂಭ್ರಮ** | *sambhrama* | The busy, shared joy of an occasion — a wedding house at 6am. Joy that is plural and slightly frantic, and that no one experiences alone. |
| **ಪುಳಕ** | *puḷaka* | The thrill that stands the body hair on end. Classical poetics treats it as visible evidence of an inner state, which is why it has its own noun. |
| **ಹಂಬಲ** | *hambala* | Yearning toward something absent — a place, a person, a life not lived. Closer to Portuguese *saudade* than to 'longing'. |
| **ಉಮ್ಮಳ** | *ummaḷa* | Grief welling up from below, the moment before it breaks. Names the swell, not the weeping. |
| **ಹಳಹಳಿಕೆ** | *haḷahaḷike* | Regret braided with longing — remorse for something you would, honestly, do again. |
| **ನೆಮ್ಮದಿ** | *nemmadi* | Peace of mind, sharply distinct from ಶಾಂತಿ, peace as the absence of conflict. You can have ಶಾಂತಿ in a house with no ನೆಮ್ಮದಿ in it. |
| **ಅಳುಕು** | *aḷuku* | The small inward flinch of misgiving just before you do the thing anyway. Not fear — a hesitation with a conscience in it. |

## ನವರಸ — the older map, laid over the wheel

| ರಸ | roman | flavour | where it lands on the wheel |
|---|---|---|---|
| **ಶೃಂಗಾರ** | *śṛṅgāra* | love, the erotic | No home on the English wheel at all — desire is not one of its seven. |
| **ಹಾಸ್ಯ** | *hāsya* | mirth, the comic | Only appears on the wheel as ಅಪಹಾಸ್ಯ — laughter aimed at someone. |
| **ಕರುಣ** | *karuṇa* | compassion, pathos | ದುಃಖ covers the grief; the wheel has no place for grief felt on another's behalf. |
| **ರೌದ್ರ** | *raudra* | fury | ಕೋಪ |
| **ವೀರ** | *vīra* | the heroic | Reduced to a single outer petal, ಧೈರ್ಯ, under ಶಕ್ತಿ. |
| **ಭಯಾನಕ** | *bhayānaka* | terror | ಭಯ |
| **ಬೀಭತ್ಸ** | *bībhatsa* | disgust, the odious | ಅಸಹ್ಯ |
| **ಅದ್ಭುತ** | *adbhuta* | wonder | ಅಚ್ಚರಿ |
| **ಶಾಂತ** | *śānta* | repose | The ninth rasa, added late and argued over. The wheel files peace as a kind of happiness; the rasa tradition makes it a state of its own. |

## Files

| path | what's in it |
|---|---|
| [`index.html`](index.html) | the whole site — one file, no build step, no runtime dependencies |
| [`data/wheel.json`](data/wheel.json) | canonical. 7 core objects, each with `kids` (branches), each with `kids` (leaves). Every node has `en`, `kn`, `tr`, `status`, `rala[]`, and often `note`. |
| [`data/wheel.csv`](data/wheel.csv) | the same 130 words flattened — `ring, sector_en, english, kannada, transliteration, status, rala_hits, note` |
| [`data/native.json`](data/native.json) | the untranslatable list — `kn`, `tr`, `gloss` |
| [`data/navarasa.json`](data/navarasa.json) | the nine rasas — `kn`, `tr`, `en`, `map` |
| [`data/rala-responses.json`](data/rala-responses.json) | raw API responses, keyed by query. Provenance for every claim above. |
| [`scripts/rala.py`](scripts/rala.py) | rala client + the morphological expander |
| [`scripts/build.py`](scripts/build.py) | regenerates `index.html`, this README and `wheel.csv` from `data/` |
| [`src/`](src/) | the page's parts — markup, styles, and the SVG wheel renderer |

```bash
python3 scripts/build.py      # rebuild the site and this README
python3 scripts/rala.py loneliness annoyed   # try the expander
```

## Attribution

- Word data from [**rala**](https://github.com/pvnkmrksk/rala), a reversal of [**Alar**](https://alar.ink) by V. Krishna, licensed [ODC-ODbL](https://opendatacommons.org/licenses/odbl/), combined with [Padakanaja](https://padakanaja.karnataka.gov.in/dictionary), Government of Karnataka.
- Wheel structure after Gloria Willcox's Feeling Wheel (1982) and its widely circulated three-ring descendant. The Kannada here is a reinterpretation, not a translation of it.
- Derived data in `data/` is offered under ODbL, matching Alar. The page and code are MIT.

