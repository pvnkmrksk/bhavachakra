# ಭಾವಚಕ್ರ · three feeling wheels in Kannada

**[Open the wheels →](https://pvnkmrksk.github.io/bhavachakra/)**

353 words across three maps of the same territory:

| wheel | built from | words |
|---|---|---:|
| **ಭಾವಚಕ್ರ** *bhava* | the English feeling wheel, translated and then argued with | 130 |
| **ಒಡಲ ಚಕ್ರ** *odalu* | the part of the body Kannada sites each feeling in | 106 |
| **ರಸಚಕ್ರ** *rasa* | the nine rasas of the Nāṭyaśāstra, opened out into daily Kannada | 117 |

The site is for reading the words. This README is the extended cut: it carries the dictionary evidence, the misfires and the counts, which are diagnostics.

## The lookup

```
GET https://rala-search.rala-search.workers.dev/?q=<english word>

{ "query": str,
  "count": int,
  "results": [ { "kannada", "definition", "type", "source" } ] }
```

Calls were made one at a time with 0.35 s between them and without the `X-Rala-Intent: primary` header, so none of this reached rala's own search analytics. [alar.ink](https://alar.ink) was never queried — Alar arrives here only through rala's reversal of it.

rala matches whole words against definition text, so a query only finds the exact form the dictionary happens to use: `annoyed` returns nothing, `annoy` returns thirteen entries. [`scripts/rala.py`](scripts/rala.py) fixes this client-side with a morphological expander — 26 suffix rules, longest first, doubled-consonant undo, and one level of recursion so `playfully → playful → play`.

```
loneliness  → loneliness, lonely, lone
frustrated  → frustrated, frustrat, frustrate
victimised  → victimised, victimise, victimize
stopped     → stopped, stopp, stoppe, stop
```

Of the 52 words that first came back empty, morphology alone recovered 38. The last 14 needed hand-picked synonyms — `repelled → repulse`, `boredom → tedium`, `skeptical → sceptic` — which is the part stemming cannot reach, and the argument for a thesaurus layer inside the worker rather than in every client.

## What rala returned, for ಭಾವಚಕ್ರ

| | count | meaning |
|---|---:|---|
| `direct` | 73 | the dictionary's top hit is the word on the wheel |
| `shaped` | 45 | rala had it, but buried in technical noise or in the wrong register |
| `gap` | 12 | no usable entry; the word comes from Kannada usage |
| | **130** | |

Where rala is excellent: fear, anger and grief. Seven graded fear words, four for doubt, and ತೇಜೋವಧೆ — "the murder of someone's lustre" — for *humiliate*.

Where it falls down it falls down structurally, because rala's bulk is Padakanaja, which is administrative, legal, scientific and agricultural:

| query | what rala returned |
|---|---|
| `stressed` | ಪ್ರತಿಬಲ — tensile stress, shear stress |
| `confused` | ತುಕ್ಕುಗೆಂಪು — the confused flour beetle |
| `let down` | ಹಾಲೊಸರಿಕೆ — milk let-down, the dairy term |
| `loving` | ನೆರಳು ಪ್ರಿಯ — shade-loving, of plants |
| `depressed` | ದಲಿತ, ಶೋಷಿತ — from the phrase "depressed classes" |
| `accepted` | ಅಂಗೀಕೃತ ಟೆಂಡರ್ — accepted tender |
| `tired` | ದಣಿದ ಮಣ್ಣು — tired soil |
| `critical` | ಕ್ರಾಂತಿಕೋನ — critical angle |
| `proud / inspired / boredom / threatened` | nothing at all |

## ಭಾವಚಕ್ರ — the English feeling wheel, translated and then argued with

### ಸಂತೋಷ · Happy — *santōṣa*

| ring | ಕನ್ನಡ | roman | English slot | status | rala's hits |
|---|---|---|---|---|---|
| core | **ಸಂತೋಷ** | *santōṣa* | Happy | `direct` | ಸಂತೋಷದ, ಸಂತುಷ್ಟ, ಖುಷಿಯಾದ, ನೆಮ್ಮದಿಯ, ಭಾಗ್ಯವಂತನಾದ |
| branch | **ತುಂಟತನ** | *ṭuṇṭatana* | Playful | `gap` | ದ್ರೋಹ ಮಾಡು ⟨foul play⟩, ನಾಟಕಕಾರ ⟨playwright⟩, ಚಕ್ಕರ್ ಕೊಡು ⟨play truant⟩ |
| leaf | **ಉದ್ರೇಕ** | *udrēka* | Aroused | `shaped` | ಉದ್ರೇಕಗೊಳ್ಳು, ಪ್ರಚೋದಿಸು, ಕೆರಳಿಸು |
| leaf | **ಕೀಟಲೆ** | *kīṭale* | Cheeky | `shaped` | ಉದ್ಧಟ, ಒರಟುತನದ, ದುರಹಂಕಾರದ |
| branch | **ತೃಪ್ತಿ** | *tṛpti* | Content | `shaped` | ತೃಪ್ತ, ತೃಪ್ತಿ, ಪರಿವಿಡಿ ⟨table of contents⟩, ತೇವಾಂಶ ⟨moisture content⟩ |
| leaf | **ನಿರಾಳ** | *nirāḷa* | Free | `shaped` | ಮುಕ್ತ, ಸ್ವತಂತ್ರ, ಕರಮುಕ್ತ ⟨duty-free⟩ |
| leaf | **ಹಿಗ್ಗು** | *higgu* | Joyful | `shaped` | ಸಂತೋಷ, ಉಲ್ಲಾಸ, ಹರ್ಷ |
| branch | **ಆಸಕ್ತಿ** | *āsakti* | Interested | `direct` | ಆಸಕ್ತಿ ಇರುವ, ಸಂಬಂಧವುಳ್ಳ, ಪಕ್ಷಪಾತದ ⟨interested party⟩ |
| leaf | **ಕುತೂಹಲ** | *kutūhala* | Curious | `direct` | ಕುತೂಹಲಕಾರಿ, ಕುತೂಹಲವುಳ್ಳ |
| leaf | **ಕೆದಕು** | *kedaku* | Inquisitive | `shaped` | ಕೆದಕುವ, ಶೋಧಿಸುವ, ವಿಚಾರಮಾಡುವ |
| branch | **ಹೆಮ್ಮೆ** | *hemme* | Proud | `gap` | — |
| leaf | **ಸಾರ್ಥಕ** | *sārthaka* | Successful | `shaped` | ಯಶಸ್ವಿ, ವಿಜಯಿ, ವಿಜೇತ |
| leaf | **ಆತ್ಮವಿಶ್ವಾಸ** | *ātma-viśvāsa* | Confident | `direct` | ವಿಶ್ವಾಸವುಳ್ಳ, ನೆಚ್ಚಿಕೆಯ, ಧೈರ್ಯದ |
| branch | **ಒಪ್ಪಿಗೆ** | *oppige* | Accepted | `gap` | ಅಂಗೀಕೃತ ಟೆಂಡರ್ ⟨accepted tender⟩, ಅಂಗೀಕೃತ ಠೇವಣಿ ⟨accepted deposit⟩, ಸ್ವೀಕೃತ |
| leaf | **ಗೌರವ** | *gaurava* | Respected | `shaped` | ಆ ಸಂಬಂಧವಾದ ⟨with respect to⟩, ಸಂಬಂಧಿಸಿದಂತೆ ⟨in respect of⟩ |
| leaf | **ಮನ್ನಣೆ** | *mannaṇe* | Valued | `shaped` | ಏಕಮೌಲ್ಯ ⟨single-valued⟩, ಮೌಲ್ಯ ಸಂದಾಯ ⟨value payable⟩ |
| branch | **ಶಕ್ತಿ** | *śakti* | Powerful | `direct` | ಶಕ್ತಿಶಾಲಿ, ಶಕ್ತಿವಂತ, ಶಕ್ತನಾದ |
| leaf | **ಧೈರ್ಯ** | *dhairya* | Courageous | `direct` | ಧೈರ್ಯದ, ಕೆಚ್ಚೆದೆಯ, ಎದೆಗಾರಿಕೆಯ |
| leaf | **ಹೊಳಹು** | *hoḷahu* | Creative | `direct` | ಸೃಜನಾತ್ಮಕ, ರಚನಾತ್ಮಕ |
| branch | **ನೆಮ್ಮದಿ** | *nemmadi* | Peaceful | `shaped` | ಶಾಂತಿಯ, ಶಾಂತಿಯುತ |
| leaf | **ಪ್ರೀತಿ** | *prīti* | Loving | `gap` | ನೆರಳು ಪ್ರಿಯ ⟨shade-loving⟩ |
| leaf | **ಕೃತಜ್ಞತೆ** | *kṛtajñate* | Thankful | `direct` | ಕೃತಜ್ಞ, ಕೃತಜ್ಞನಾದ |
| branch | **ನಂಬಿಕೆ** | *nambike* | Trusting | `shaped` | ನಂಬಿಕೆ, ವಿಶ್ವಾಸ, ನ್ಯಾಸ ಖಾತೆ ⟨trust account⟩, ಟ್ರಸ್ಟ್ ಆಡಳಿತ |
| leaf | **ಸೂಕ್ಷ್ಮ** | *sūkṣma* | Sensitive | `direct` | ಸೂಕ್ಷ್ಮಗ್ರಾಹಿ, ಸಂವೇದನಾಶೀಲ, ಸೂಕ್ಷ್ಮ |
| leaf | **ಸಲಿಗೆ** | *salige* | Intimate | `direct` | ಸಲಿಗೆ, ಅನ್ಯೋನ್ಯ, ಆತ್ಮೀಯ, ನಿಕಟ |
| branch | **ಭರವಸೆ** | *bharavase* | Optimistic | `direct` | ಆಶಾವಾದದ, ಆಶಾಪೂರ್ಣ |
| leaf | **ಆಸೆ** | *āse* | Hopeful | `direct` | ಭರವಸೆಯ, ಆಶಾದಾಯಕ |
| leaf | **ಸ್ಫೂರ್ತಿ** | *sphūrti* | Inspired | `gap` | — |

<details><summary>Reading</summary>

- **ಸಂತೋಷ** *(Happy)* — rala also returns ಭಾಗ್ಯವಂತ / ಅದೃಷ್ಟಶಾಲಿ — 'lucky'. English *happy* still carries its old root *hap*, chance. Kannada keeps luck and gladness in separate words.  
  also said: **ಖುಷಿ** *khuṣi*, gladness, the most casual, **ಹರ್ಷ** *harṣa*, joy, elevated, **ಆನಂದ** *ānanda*, bliss, **ಸಂತಸ** *santasa*, gladness, softer, **ಹಿಗ್ಗು** *higgu*, swelling delight
- **ತುಂಟತನ** *(Playful)* — A clean miss. rala only knows *play* as the noun — foul play, playwright, child's play. The felt state is ತುಂಟತನ, the mischief of a child you are not actually angry with.
- **ಉದ್ರೇಕ** *(Aroused)* — In Kannada ಉದ್ರೇಕ is not primarily erotic — a crowd, a temper and a nerve can all be ಉದ್ರಿಕ್ತ. It means charged, and the charge can go either way.
- **ಕೀಟಲೆ** *(Cheeky)* — rala's ಉದ್ಧಟ / ದುರಹಂಕಾರ are genuinely insulting. Cheeky is affectionate — that is ಕೀಟಲೆ, teasing you are allowed to do.
- **ತೃಪ್ತಿ** *(Content)* — The right word was in there, sitting under moisture content and table of contents. ತೃಪ್ತಿ is satiety — the feeling after a meal, and after a life.  
  also said: **ಸಂತೃಪ್ತಿ** *santṛpti*, full satisfaction, **ತಣಿವು** *taṇivu*, slaked, **ಸಮಾಧಾನ** *samādhāna*, settledness
- **ನಿರಾಳ** *(Free)* — ಮುಕ್ತ and ಸ್ವತಂತ್ರ are freedoms of status — liberated, independent, tax-exempt. The *feeling* of free is ನಿರಾಳ: unclenched, the breath after the weight comes off.
- **ಹಿಗ್ಗು** *(Joyful)* — ಹರ್ಷ and ಉಲ್ಲಾಸ are correct and Sanskritic. ಹಿಗ್ಗು is the native verb-noun: to swell. Joy as something that expands you.
- **ಕೆದಕು** *(Inquisitive)* — ಕೆದಕು is to poke at a thing that was sitting quietly, and it keeps the faint rudeness English *inquisitive* also carries. ಜಿಜ್ಞಾಸೆ is the same impulse with the rudeness taken out.  
  also said: **ಜಿಜ್ಞಾಸೆ** *jijñāse*, the wish to know, **ಕುತೂಹಲ** *kutūhala*, curiosity, **ಶೋಧ** *śōdha*, searching out
- **ಹೆಮ್ಮೆ** *(Proud)* — rala returns nothing at all for *proud*. And Kannada would resist a single answer anyway: ಹೆಮ್ಮೆ is warm pride in someone, ಅಭಿಮಾನ is pride-as-loyalty, ಅಹಂಕಾರ is the pride that has gone bad. English collapses all three.  
  also said: **ಅಭಿಮಾನ** *abhimāna*, pride as loyalty, **ಗರ್ವ** *garva*, pride, tipping toward vanity, **ಅಹಂಕಾರ** *ahaṅkāra*, the pride that has gone bad, **ಗತ್ತು** *gattu*, swagger
- **ಸಾರ್ಥಕ** *(Successful)* — ಯಶಸ್ವಿ is the outcome — you won. ಸಾರ್ಥಕ is the feeling — it had meaning, it was worth it. Only one of those belongs on an emotion wheel.
- **ಆತ್ಮವಿಶ್ವಾಸ** *(Confident)* — Literally 'self-trust'. Kannada builds confidence out of the same root as trusting another person.
- **ಒಪ್ಪಿಗೆ** *(Accepted)* — Every hit is procurement paperwork. And Kannada has no noun for *the felt state of being accepted* — you say it as something others did: ನನ್ನನ್ನು ಒಪ್ಪಿಕೊಂಡರು, 'they took me in'. The feeling lives in a verb, not a noun.
- **ಗೌರವ** *(Respected)* — rala only found the clerical *in respect of*. ಗೌರವ is the real word, and in Kannada it is something you give, actively, not something you passively have.
- **ಮನ್ನಣೆ** *(Valued)* — ಮೌಲ್ಯ is price. ಮನ್ನಣೆ is being recognised and given your due — the thing people leave jobs for the lack of.
- **ಧೈರ್ಯ** *(Courageous)* — ಧೈರ್ಯ is steadiness under fear. The native alternatives rala offers are more physical: ಕೆಚ್ಚು is heat in the chest, ಎದೆಗಾರಿಕೆ is literally chest-having.  
  also said: **ಕೆಚ್ಚು** *keccu*, embers-courage, **ಎದೆಗಾರಿಕೆ** *edegārike*, nerve, **ದಿಟ್ಟತನ** *diṭṭatana*, boldness, **ಛಲ** *chala*, resolve
- **ಹೊಳಹು** *(Creative)* — The flash — the moment a thing occurs to you. Names the event rather than the faculty.  
  also said: **ಸೃಜನಶೀಲತೆ** *sṛjanaśīlate*, creativity, **ಕಲ್ಪನೆ** *kalpane*, imagining, **ಸ್ಫೂರ್ತಿ** *sphūrti*, inspiration
- **ನೆಮ್ಮದಿ** *(Peaceful)* — The single most important correction on this wheel. ಶಾಂತಿ is peace as the absence of war — treaties, ceasefires, ಶಾಂತಿ ಸಭೆ. ನೆಮ್ಮದಿ is peace of mind, and it is what people actually pray for.  
  also said: **ಶಾಂತಿ** *śānti*, peace, as the absence of conflict, **ಸಮಾಧಾನ** *samādhāna*, being consoled, **ನಿರಾಳ** *nirāḷa*, unclenched
- **ಪ್ರೀತಿ** *(Loving)* — The only match in 478,680 entries was a botany term for shade-loving plants. Kannada is not short of love words — ಪ್ರೀತಿ, ಮಮತೆ, ವಾತ್ಸಲ್ಯ, ಅಕ್ಕರೆ, ಒಲವು — the dictionary just isn't built to find them from English.  
  also said: **ಮಮತೆ** *mamate*, attachment-love, **ವಾತ್ಸಲ್ಯ** *vātsalya*, tenderness flowing downward, **ಅಕ್ಕರೆ** *akkare*, fondness, **ಒಲವು** *olavu*, leaning toward
- **ಕೃತಜ್ಞತೆ** *(Thankful)* — Literally 'knowing what was done'. Gratitude as accurate memory.
- **ನಂಬಿಕೆ** *(Trusting)* — Buried under thirty entries of trust deeds and trust accounts. ನಂಬಿಕೆ also means belief and superstition — in Kannada, trusting a person and believing a thing are one act.
- **ಸೂಕ್ಷ್ಮ** *(Sensitive)* — ಸೂಕ್ಷ್ಮ means fine-grained, subtle-perceiving. Calling someone ಸೂಕ್ಷ್ಮ is praise — unlike English 'sensitive', which is half an accusation.
- **ಸಲಿಗೆ** *(Intimate)* — ಸಲಿಗೆ has no English word. It is the earned licence to be informal with someone — to tease them, take their food, drop the honorific. Intimacy defined as permission, not as feeling.  
  also said: **ಆತ್ಮೀಯತೆ** *ātmīyate*, closeness, **ಅನ್ಯೋನ್ಯ** *anyōnya*, mutual, easy with each other, **ನಿಕಟ** *nikaṭa*, near
- **ಭರವಸೆ** *(Optimistic)* — ಭರವಸೆ is also the word for a promise or an assurance. Optimism, in Kannada, is something somebody gave you.  
  also said: **ಆಶಾವಾದ** *āśāvāda*, optimism, as a stance, **ನಿರೀಕ್ಷೆ** *nirīkṣe*, expectation, **ನಂಬಿಕೆ** *nambike*, trust, belief
- **ಆಸೆ** *(Hopeful)* — The plainest possible word: wish, want, hope, all one. Kannada does not separate hoping from wanting.  
  also said: **ಆಶೆ** *āśe*, hope, the Sanskrit form, **ಹಂಬಲ** *hambala*, yearning, **ಬಯಕೆ** *bayake*, wish
- **ಸ್ಫೂರ್ತಿ** *(Inspired)* — No result. ಸ್ಫೂರ್ತಿ is the everyday word — a sudden welling-up, the same root as a spark.

</details>

### ಅಚ್ಚರಿ · Surprised — *accari*

| ring | ಕನ್ನಡ | roman | English slot | status | rala's hits |
|---|---|---|---|---|---|
| core | **ಅಚ್ಚರಿ** | *accari* | Surprised | `direct` | ಆಶ್ಚರ್ಯ, ವಿಸ್ಮಯ, ಅನಿರೀಕ್ಷಿತ, ಹಠಾತ್ ತನಿಖೆ ⟨surprise inspection⟩ |
| branch | **ಬೆಚ್ಚು** | *beccu* | Startled | `direct` | ಚಕಿತಗೊಳಿಸು, ಗಾಬರಿಪಡಿಸು, ಬೆದರಿಸು |
| leaf | **ಆಘಾತ** | *āghāta* | Shocked | `direct` | ಆಘಾತ, ದಿಗಿಲುಂಟುಮಾಡು, ವಿದ್ಯುದಾಘಾತ ⟨electric shock⟩ |
| leaf | **ಎದೆಗುಂದು** | *edegundu* | Dismayed | `direct` | ಎದೆಗುಂದಿಸು, ಅಧೈರ್ಯ, ದಿಗಿಲು, ಹತಾಶೆ |
| branch | **ಗೊಂದಲ** | *gondala* | Confused | `shaped` | ತುಕ್ಕುಗೆಂಪು ⟨confused flour beetle⟩ |
| leaf | **ಭ್ರಮೆ ಕಳಚು** | *bhrame kaḷacu* | Disillusioned | `direct` | ಭ್ರಮನಿರಸನಗೊಂಡ |
| leaf | **ಕಂಗೆಡು** | *kaṅgeḍu* | Perplexed | `direct` | ಕಂಗೆಡಿಸು, ವಿಭ್ರಾಂತಿ ತರು |
| branch | **ಬೆರಗು** | *beragu* | Amazed | `direct` | ಬೆರಗುಗೊಳಿಸು, ಆಶ್ಚರ್ಯಗೊಳ್ಳು, ಚಕಿತನಾಗು |
| leaf | **ದಂಗು** | *daṅgu* | Astonished | `direct` | ವಿಸ್ಮಯವನ್ನುಂಟುಮಾಡು, ಅಚ್ಚರಿಗೊಳಿಸು |
| leaf | **ಭಯಭಕ್ತಿ** | *bhaya-bhakti* | Awe | `direct` | ಭಯಮಿಶ್ರಿತ ಗೌರವ, ಭಯ ತುಂಬಿದ ಗೌರವ |
| branch | **ಉತ್ಸಾಹ** | *utsāha* | Excited | `direct` | ಉತ್ತೇಜಿತ, ಉದ್ರಿಕ್ತ, ಉತ್ಸಾಹ |
| leaf | **ತವಕ** | *tavaka* | Eager | `direct` | ತವಕ, ಕಾತರದ, ಉತ್ಸುಕ, ಉತ್ಕಟ |
| leaf | **ಹುರುಪು** | *hurupu* | Energetic | `direct` | ಹುರುಪು, ಉತ್ಸಾಹ, ಶಕ್ತಿಯುತವಾದ |

<details><summary>Reading</summary>

- **ಅಚ್ಚರಿ** *(Surprised)* — ಅಚ್ಚರಿ is the native word and ಆಶ್ಚರ್ಯ the Sanskrit one; both are in daily use, and this wheel uses the shorter.  
  also said: **ಆಶ್ಚರ್ಯ** *āścarya*, surprise, the Sanskrit form, **ವಿಸ್ಮಯ** *vismaya*, astonishment, **ಬೆರಗು** *beragu*, wonder that stops you
- **ಬೆಚ್ಚು** *(Startled)* — ಬೆಚ್ಚಿಬೀಳು — to be startled and drop. Kannada builds the flinch out of a fall.
- **ಎದೆಗುಂದು** *(Dismayed)* — Literally 'the chest sinks'. Kannada names the physical event and leaves you to infer the feeling — it does this constantly.
- **ಗೊಂದಲ** *(Confused)* — The dictionary's one match for *confused* is a species of beetle. ಗೊಂದಲ is the real word, and it also means a noisy crowd — confusion as too many voices at once.  
  also said: **ಕಕ್ಕಾಬಿಕ್ಕಿ** *kakkābikki*, flustered, **ತಬ್ಬಿಬ್ಬು** *tabbibbu*, thrown, at a loss, **ಗಲಿಬಿಲಿ** *galibili*, muddle
- **ಭ್ರಮೆ ಕಳಚು** *(Disillusioned)* — The illusion comes unfastened. ಕಳಚು is what a bangle does, or a bolt.
- **ಕಂಗೆಡು** *(Perplexed)* — ಕಣ್ + ಕೆಡು: the eyes go bad. To be at a loss is, literally, to lose your sight of it.
- **ದಂಗು** *(Astonished)* — ದಂಗಾದೆ — I was floored. The version of astonishment with your mouth open.  
  also said: **ವಿಸ್ಮಯ** *vismaya*, astonishment, **ಆಶ್ಚರ್ಯ** *āścarya*, surprise, **ಬೆರಗು** *beragu*, wonder, **ದಿಗ್ಭ್ರಮೆ** *digbhrame*, stupefaction
- **ಭಯಭಕ್ತಿ** *(Awe)* — rala could only define it as a phrase: 'respect mixed with fear'. But Kannada does have the compound — ಭಯಭಕ್ತಿ, fear-and-devotion, the standard word for how one stands before a deity or a formidable elder. Awe as a social posture, not a private thrill.
- **ತವಕ** *(Eager)* — ತವಕ and ಕಾತರ are both eagerness with an edge of ache — waiting that has begun to hurt slightly.

</details>

### ಬೇಸರ · Bad — *bēsara*

| ring | ಕನ್ನಡ | roman | English slot | status | rala's hits |
|---|---|---|---|---|---|
| core | **ಬೇಸರ** | *bēsara* | Bad | `gap` | ಕೆಟ್ಟ, ದುರ್ವರ್ತನೆ ⟨bad behaviour⟩, ವಸೂಲಾಗದ ಸಾಲ ⟨bad debt⟩, ವೈಮನಸ್ಯ ⟨bad blood⟩ |
| branch | **ಬೇಜಾರು** | *bējāru* | Bored | `gap` | — |
| leaf | **ಉದಾಸೀನ** | *udāsīna* | Indifferent | `direct` | ಉದಾಸೀನ, ಅಸಡ್ಡೆಯ, ತಟಸ್ಥ |
| leaf | **ಅಸಡ್ಡೆ** | *asaḍḍe* | Apathetic | `direct` | ನಿರಾಸಕ್ತ, ಆಸಕ್ತಿಯಿಲ್ಲದ, ಭಾವಶೂನ್ಯ |
| branch | **ಧಾವಂತ** | *dhāvanta* | Busy | `shaped` | ಕಾರ್ಯಮಗ್ನ, ಬಿಡುವಿಲ್ಲದ, ನಿರತ |
| leaf | **ಒತ್ತಡ** | *ottaḍa* | Pressured | `direct` | ಒತ್ತಡ, ರಕ್ತ ಒತ್ತಡ ⟨blood pressure⟩, ವಾತಾವರಣದ ಒತ್ತಡ |
| leaf | **ಆತುರ** | *ātura* | Rushed | `shaped` | ಧಾವಿಸು, ಮುನ್ನುಗ್ಗು, ತೀವ್ರಗತಿ |
| branch | **ತಳಮಳ** | *taḷamaḷa* | Stressed | `shaped` | ಒತ್ತಡ, ಪ್ರತಿಬಲ ⟨tensile stress⟩, ಕರ್ತನ ಪ್ರತಿಬಲ ⟨shear stress⟩ |
| leaf | **ಹೈರಾಣ** | *hairāṇa* | Overwhelmed | `shaped` | ಮುಳುಗಿಹೋಗು, ಭಾವಪರವಶಗೊಳ್ಳು |
| leaf | **ಚಡಪಡಿಕೆ** | *caḍapaḍike* | Restless | `direct` | ಚಡಪಡಿಸುವ, ತಳಮಳ, ವ್ಯಾಕುಲ, ಅಶಾಂತ |
| branch | **ದಣಿವು** | *daṇivu* | Tired | `shaped` | ದಣಿದ ಮಣ್ಣು ⟨tired soil⟩ |
| leaf | **ತೂಕಡಿಕೆ** | *tūkaḍike* | Sleepy | `shaped` | ತೂಕಡಿಸುವ, ನಿದ್ದೆ, ಜಡನಾದ |
| leaf | **ಅನ್ಯಮನಸ್ಕ** | *anya-manaska* | Unfocused | `direct` | ಅನ್ಯಮನಸ್ಕ, ಏಕಾಗ್ರತೆಯಿಲ್ಲದ, ಮರೆಗುಳಿ |

<details><summary>Reading</summary>

- **ಬೇಸರ** *(Bad)* — The hardest sector. Kannada's ಕೆಟ್ಟ is moral or qualitative — a bad man, spoiled milk — and cannot be a feeling. But look at what the English wheel actually files under 'Bad': bored, busy, stressed, tired. That whole zone has one Kannada name, ಬೇಸರ — a fused weariness-with-things that English needs four words to circle.  
  also said: **ಬೇಜಾರು** *bējāru*, fed up, the same word one register down, **ಸಪ್ಪೆ** *sappe*, flat, unsalted, **ಜಡ** *jaḍa*, inert
- **ಬೇಜಾರು** *(Bored)* — No entry for *boredom*. ಬೇಜಾರು covers bored, mildly sad, and fed-up in one breath. 'ಬೇಜಾರಾಗಿದೆ' could be any of the three and the listener works it out from your face.  
  also said: **ಬೇಸರ** *bēsara*, weary discontent, **ಜಿಗುಪ್ಸೆ** *jigupse*, revulsion, world-weariness, **ಸಪ್ಪೆ** *sappe*, flat
- **ಉದಾಸೀನ** *(Indifferent)* — In philosophy ಉದಾಸೀನ is the sage's equanimity. In an argument it is the coldest insult available.
- **ಅಸಡ್ಡೆ** *(Apathetic)* — Not caring, and not quite bothering to hide that you are not caring.  
  also said: **ನಿರಾಸಕ್ತಿ** *nirāsakti*, disinterest, **ಉದಾಸೀನ** *udāsīna*, indifference, or the cold shoulder, **ತಾತ್ಸಾರ** *tātsāra*, disdain
- **ಧಾವಂತ** *(Busy)* — rala's words describe a schedule. ಧಾವಂತ describes what the schedule does to you — the harried forward-lean of someone always mid-errand.
- **ಒತ್ತಡ** *(Pressured)* — Same word for atmospheric pressure, blood pressure, and social pressure. Kannada did not borrow 'stress' — it extended 'push'.
- **ಆತುರ** *(Rushed)* — ಆತುರ is haste as a character flaw as much as a state — 'ಆತುರಗಾರನಿಗೆ ಬುದ್ಧಿ ಮಟ್ಟ', the hasty man is short on sense.
- **ತಳಮಳ** *(Stressed)* — Every single hit was materials engineering. ತಳಮಳ is the churn — the word for boiling liquid and for a mind that will not settle.
- **ಹೈರಾಣ** *(Overwhelmed)* — English uses one *overwhelmed* in two places on this wheel. Kannada splits them by how you are swamped: ಹೈರಾಣ is worn down to nothing by too much work; ಕಳವಳ, over in ಭಯ, is being swamped by dread.
- **ಚಡಪಡಿಕೆ** *(Restless)* — Onomatopoeic — the sound of a fish on dry ground, or a body that cannot stay in the chair.
- **ದಣಿವು** *(Tired)* — The only match rala had for *tired* was agronomy — ದಣಿದ ಮಣ್ಣು, exhausted soil. ದಣಿವು is used of a body and of a day alike.  
  also said: **ಆಯಾಸ** *āyāsa*, fatigue, **ಬಳಲಿಕೆ** *baḷalike*, exhaustion, **ಸುಸ್ತು** *sustu*, done in
- **ತೂಕಡಿಕೆ** *(Sleepy)* — The nod of the head as you lose the fight.  
  also said: **ಜೋಂಪು** *jōmpu*, the afternoon drowse, **ಮಂಪರು** *mamparu*, half-sleep, **ನಿದ್ದೆ** *nidde*, sleep
- **ಅನ್ಯಮನಸ್ಕ** *(Unfocused)* — 'Other-minded' — your mind is somewhere, just not here. Kinder than 'distracted', which implies something pulled you.

</details>

### ಭಯ · Fearful — *bhaya*

| ring | ಕನ್ನಡ | roman | English slot | status | rala's hits |
|---|---|---|---|---|---|
| core | **ಭಯ** | *bhaya* | Fearful | `direct` | ಭಯ, ಹೆದರಿಕೆ, ಅಂಜಿಕೆ, ಭೀತಿ, ದಿಗಿಲು, ಆತಂಕ, ಗಾಬರಿ |
| branch | **ಹೆದರಿಕೆ** | *hedarike* | Scared | `direct` | ಹೆದರಿಕೆ, ಗಾಬರಿ, ಭೀತಿ, ಬೆದರುಗೊಂಬೆ ⟨scarecrow⟩ |
| leaf | **ಅಸಹಾಯಕತೆ** | *asahāyakate* | Helpless | `direct` | ಅಸಹಾಯಕ, ದಿಕ್ಕಿಲ್ಲದ, ತಬ್ಬಲಿ |
| leaf | **ಅಂಜಿಕೆ** | *añjike* | Frightened | `direct` | ಹೆದರಿಸು, ಭಯಪಡಿಸು, ದಿಗಿಲುಗೊಳಿಸು |
| branch | **ಆತಂಕ** | *ātaṅka* | Anxious | `direct` | ಆತಂಕಗೊಂಡ, ವ್ಯಾಕುಲತೆ, ಚಿಂತಾಕ್ರಾಂತ, ತಲ್ಲಣಗೊಂಡ |
| leaf | **ಚಿಂತೆ** | *cinte* | Worried | `direct` | ಚಿಂತೆ, ಕಳವಳ, ಆತಂಕ, ಪೇಚಾಟ |
| leaf | **ಕಳವಳ** | *kaḷavaḷa* | Overwhelmed | `shaped` | ಕಳವಳಗೊಂಡ, ವ್ಯಾಕುಲ |
| branch | **ಅಳುಕು** | *aḷuku* | Insecure | `direct` | ಅಭದ್ರ, ಅಸುರಕ್ಷಿತ, ರಕ್ಷಣೆ ರಹಿತ |
| leaf | **ಕೊರತೆ** | *korate* | Inadequate | `shaped` | ಸಾಕಾಗದ, ಅಸಮರ್ಥ, ಕೊರತೆಯುಳ್ಳ |
| leaf | **ಕೀಳರಿಮೆ** | *kīḷarime* | Inferior | `shaped` | ಕೀಳು, ಕಳಪೆ, ಕೆಳದರ್ಜೆಯ |
| branch | **ದುರ್ಬಲ** | *durbala* | Weak | `direct` | ದುರ್ಬಲ, ಬಲಹೀನ, ನಿರ್ಬಲ |
| leaf | **ದಂಡ** | *daṇḍa* | Worthless | `shaped` | ಅಯೋಗ್ಯ |
| leaf | **ಲೆಕ್ಕಕ್ಕಿಲ್ಲ** | *lekkakkilla* | Insignificant | `direct` | ಕ್ಷುಲ್ಲಕ, ಅತ್ಯಲ್ಪ, ನಿಕೃಷ್ಟ |
| branch | **ತಿರಸ್ಕಾರ** | *tiraskāra* | Rejected | `shaped` | ಸೋತ ಅಭ್ಯರ್ಥಿ ⟨rejected candidate⟩, ತಿರಸ್ಕರಿಸತಕ್ಕದ್ದು, ಹಕ್ಕು ಸಾಧನೆಗಳು ⟨rejected claims⟩ |
| leaf | **ಹೊರಗಿಡು** | *horagiḍu* | Excluded | `gap` | — |
| leaf | **ಕಿರುಕುಳ** | *kirukuḷa* | Persecuted | `direct` | ಕಿರುಕುಳ ಕೊಡು, ಪೀಡಿಸು, ಹಿಂಸಿಸು |
| branch | **ಬೆದರಿಕೆ** | *bedarike* | Threatened | `gap` | — |
| leaf | **ನಡುಕ** | *naḍuka* | Nervous | `shaped` | ನಡುಗುವ, ಅಂಜುಬುರುಕ, ನರವ್ಯೂಹ ⟨nervous system⟩ |
| leaf | **ಬಟಾಬಯಲು** | *baṭā-bayalu* | Exposed | `shaped` | ಗುಟ್ಟುರಟ್ಟಾದ, ಸುರಕ್ಷಣೆ ಇಲ್ಲದ, ಬಹಿರಂಗಗೊಳಿಸಿದ |

<details><summary>Reading</summary>

- **ಭಯ** *(Fearful)* — rala's richest sector — seven distinct words on the first page. Kannada grades fear finely: ಅಂಜಿಕೆ (timid), ಹೆದರಿಕೆ (scared), ದಿಗಿಲು (dread), ಗಾಬರಿ (panic), ಆತಂಕ (anxiety), ಭೀತಿ (terror).  
  also said: **ಹೆದರಿಕೆ** *hedarike*, being scared, **ಅಂಜಿಕೆ** *añjike*, timidity, **ಭೀತಿ** *bhīti*, terror, **ದಿಗಿಲು** *digilu*, dread, **ಗಾಬರಿ** *gābari*, panic, **ಆತಂಕ** *ātaṅka*, anxiety
- **ಅಸಹಾಯಕತೆ** *(Helpless)* — rala's ದಿಕ್ಕಿಲ್ಲದ is better than the headword: 'without a direction'. Helplessness as having nowhere to turn — literally no compass point.
- **ಆತಂಕ** *(Anxious)* — ಆತಂಕ is now the standard clinical word too. Its older sense is closer to 'impediment' — anxiety as the thing in your way.  
  also said: **ಕಳವಳ** *kaḷavaḷa*, agitation, **ಚಿಂತೆ** *cinte*, worry, thought, **ತಳಮಳ** *taḷamaḷa*, churn, **ವ್ಯಾಕುಲ** *vyākula*, distress
- **ಚಿಂತೆ** *(Worried)* — ಚಿಂತೆ is also simply 'thought'. To worry and to think are the same verb, which tells you something.  
  also said: **ಯೋಚನೆ** *yōcane*, thinking it over, **ಕಾಳಜಿ** *kāḷaji*, care, concern, **ತಲೆಬಿಸಿ** *talebisi*, head-heat
- **ಕಳವಳ** *(Overwhelmed)* — The second of the split — see ಹೈರಾಣ under ಬೇಸರ. ಕಳವಳ is being flooded by apprehension rather than by workload.
- **ಅಳುಕು** *(Insecure)* — The small inward flinch before you do the thing anyway. ಅಭದ್ರತೆ carries the other sense of *insecure* — physically unguarded, a word for buildings and borders.  
  also said: **ಅಭದ್ರತೆ** *abhadrate*, insecurity, of a thing unguarded, **ಹಿಂಜರಿಕೆ** *hiñjarike*, hesitation, **ಶಂಕೆ** *śaṅke*, misgiving with fear in it
- **ಕೊರತೆ** *(Inadequate)* — ಕೊರತೆ is a shortfall — of rain, of funds, of oneself. The same word, which quietly makes it feel less like a personal verdict.
- **ಕೀಳರಿಮೆ** *(Inferior)* — rala gives only the judgement (ಕೀಳು, low-grade). ಕೀಳರಿಮೆ is the feeling — 'low-self-knowing', the exact and rather beautiful Kannada for an inferiority complex.
- **ದಂಡ** *(Worthless)* — Literally waste. 'ನಾನು ದಂಡ' is how the feeling gets said about oneself.  
  also said: **ನಿಷ್ಪ್ರಯೋಜಕ** *niṣprayōjaka*, of no use, **ಅಯೋಗ್ಯ** *ayōgya*, unworthy, **ವ್ಯರ್ಥ** *vyartha*, in vain
- **ಲೆಕ್ಕಕ್ಕಿಲ್ಲ** *(Insignificant)* — 'Not in the count.' Insignificance as an accounting error.  
  also said: **ಕ್ಷುಲ್ಲಕ** *kṣullaka*, trivial, **ಅಲ್ಪ** *alpa*, slight, **ನಿಕೃಷ್ಟ** *nikṛṣṭa*, abject
- **ತಿರಸ್ಕಾರ** *(Rejected)* — ತಿರಸ್ಕಾರ is what the other person did. As with ಒಪ್ಪಿಗೆ, Kannada gives you no noun for the receiving end — rejection is only ever described from outside.
- **ಹೊರಗಿಡು** *(Excluded)* — Kannada says it as something done to you — ಹೊರಗಿಟ್ಟರು, they kept me out. ಬಹಿಷ್ಕಾರ is the same act with a history attached to it.  
  also said: **ಬಹಿಷ್ಕಾರ** *bahiṣkāra*, boycott, outcasting, **ದೂರವಿಡು** *dūraviḍu*, to keep at a distance, **ಪ್ರತ್ಯೇಕಿಸು** *pratyēkisu*, to separate off
- **ಬೆದರಿಕೆ** *(Threatened)* — No entry for the adjective. ಬೆದರಿಕೆ is the threat itself; feeling threatened is said as ಬೆದರಿಕೆ ಇದೆ — 'there is a threat' — placing it outside you rather than inside.  
  also said: **ಹೆದರಿಕೆ** *hedarike*, being scared, **ಬೆಚ್ಚು** *beccu*, a startle, **ಅಪಾಯ** *apāya*, danger
- **ನಡುಕ** *(Nervous)* — Most hits were neuroanatomy. ನಡುಕ is the tremble itself — Kannada again naming the body and letting the feeling follow.
- **ಬಟಾಬಯಲು** *(Exposed)* — ಬಟಾಬಯಲು is open ground with not one thing to hide behind — used for landscape and for people, with no change of tone.

</details>

### ಕೋಪ · Angry — *kōpa*

| ring | ಕನ್ನಡ | roman | English slot | status | rala's hits |
|---|---|---|---|---|---|
| core | **ಕೋಪ** | *kōpa* | Angry | `direct` | ಕೋಪ, ಸಿಟ್ಟು, ಸಿಡುಕು, ರೋಷ, ಮುನಿಸು, ಕ್ರೋಧ, ತಾಪ |
| branch | **ಕೈಕೊಟ್ಟರು** | *kai-koṭṭaru* | Let down | `gap` | ಹಾಲೊಸರಿಕೆ ⟨milk let-down⟩ |
| leaf | **ದ್ರೋಹ** | *drōha* | Betrayed | `direct` | ದ್ರೋಹ ಮಾಡು, ವಿಶ್ವಾಸಘಾತ, ವಂಚಿಸು |
| leaf | **ಅಸಮಾಧಾನ** | *asamādhāna* | Resentful | `direct` | ಅಸಮಾಧಾನ, ಜಿದ್ದು, ಕರುಬು, ಹಗೆತನ |
| branch | **ಅವಮಾನ** | *avamāna* | Humiliated | `direct` | ಅವಮಾನಿಸು, ತೇಜೋವಧೆ, ಮರ್ಯಾದೆ ಕಳೆ |
| leaf | **ಅವಮರ್ಯಾದೆ** | *avamaryāde* | Disrespected | `direct` | ಅಗೌರವ, ಅವಮಾನ, ಉಪೇಕ್ಷೆ, ಅವಮರ್ಯಾದೆ |
| leaf | **ಗೇಲಿ** | *gēli* | Ridiculed | `direct` | ಅಪಹಾಸ್ಯ, ಗೇಲಿ, ಅವಹೇಳನ, ಅಣಕಿಸು |
| branch | **ಕಹಿ** | *kahi* | Bitter | `shaped` | ಹಾಗಲಕಾಯಿ ⟨bitter gourd⟩, ಕಹಿಗುಳಿಗೆ ⟨bitter pill⟩, ಕ್ರೂರ, ಕಠಿಣ |
| leaf | **ಆಕ್ರೋಶ** | *ākrōśa* | Indignant | `shaped` | ಕುಪಿತ, ಕೆರಳಿದ, ರೇಗಿದ |
| leaf | **ಭಂಗ** | *bhaṅga* | Violated | `gap` | ಉಲ್ಲಂಘಿಸು ⟨violate a rule⟩, ಮಾನಭಂಗ ⟨sexual assault⟩ |
| branch | **ಸಿಟ್ಟು** | *siṭṭu* | Mad | `direct` | ಸಿಟ್ಟು, ಹುಚ್ಚು ⟨insane⟩, ಮತಿಗೆಟ್ಟ |
| leaf | **ರೊಚ್ಚು** | *roccu* | Furious | `direct` | ರೋಷಾವೇಶದ, ಕ್ರೋಧಾವಿಷ್ಟ, ಉಗ್ರ, ಪ್ರಚಂಡ |
| leaf | **ಹೊಟ್ಟೆಕಿಚ್ಚು** | *hoṭṭe-kiccu* | Jealous | `shaped` | ಅಸೂಯೆಯ, ಮಾತ್ಸರ್ಯದ |
| branch | **ಜಗಳಗಂಟ** | *jagaḷagaṇṭa* | Aggressive | `direct` | ಆಕ್ರಮಣಶೀಲ, ಜಗಳಗಂಟ, ಮೇಲೆ ಬೀಳುವ |
| leaf | **ಕೆರಳಿಕೆ** | *keraḷike* | Provoked | `direct` | ಕೆರಳಿಸು, ಕೆಣಕು, ಪ್ರಚೋದಿಸು, ರೇಗಿಸು |
| leaf | **ಹಗೆತನ** | *hagetana* | Hostile | `direct` | ಹಗೆಯ, ವೈರದ, ಶತ್ರುತ್ವದ, ಪ್ರತಿಕೂಲ |
| branch | **ರೇಜಿಗೆ** | *rējige* | Frustrated | `shaped` | ಆಶಾಭಂಗ ಹೊಂದಿದ, ವಿಫಲವಾದ, ಭಗ್ನ, ನಿಷ್ಫಲಗೊಳಿಸು |
| leaf | **ಕೆಂಡಾಮಂಡಲ** | *keṇḍā-maṇḍala* | Infuriated | `shaped` | ರೇಗಿಸು, ಕೆರಳಿಸು |
| leaf | **ಕಿರಿಕಿರಿ** | *kirikiri* | Annoyed | `direct` | ಕಿರಿಕಿರಿಮಾಡು, ರೇಗಿಸು, ಕಾಡಿಸು |
| branch | **ಬಿಗುಮಾನ** | *bigumāna* | Distant | `direct` | ಬಿಗುಮಾನದ, ಸಲಿಗೆ ಇಲ್ಲದ, ದೂರದ |
| leaf | **ಮುದುಡು** | *muduḍu* | Withdrawn | `shaped` | ವಾಪಸ್ಸು ಪಡೆದ ⟨withdrawn application⟩, ಹಿಂದಕ್ಕೆ ಪಡೆದ |
| leaf | **ಮರಗಟ್ಟು** | *maragaṭṭu* | Numb | `direct` | ಮರಗಟ್ಟಿದ, ಜೋಮುಹಿಡಿದ, ಜಡವಾದ |
| branch | **ಟೀಕೆ** | *ṭīke* | Critical | `shaped` | ಕ್ರಾಂತಿಕೋನ ⟨critical angle⟩, ವಿಷಮ ಮೌಲ್ಯ ⟨critical value⟩, ವಿಮರ್ಶಾತ್ಮಕ |
| leaf | **ಅನುಮಾನ** | *anumāna* | Skeptical | `direct` | ಅನುಮಾನ, ಸಂಶಯ, ಸಂದೇಹ, ಶಂಕೆ |
| leaf | **ಉಡಾಫೆ** | *uḍāphe* | Dismissive | `shaped` | ತಳ್ಳಿಹಾಕು, ನಿರ್ಲಕ್ಷಿಸು, ವಜಾ ಮಾಡು ⟨dismiss from service⟩ |

<details><summary>Reading</summary>

- **ಕೋಪ** *(Angry)* — Kannada separates anger by heat and by intimacy: ಸಿಟ್ಟು is hot and quick, ಕೋಪ is the general word, ಕ್ರೋಧ is grand and destructive, ಸಿಡುಕು is chronic and worn on the face — and ಮುನಿಸು is the anger you only get to have with someone who loves you.  
  also said: **ಸಿಟ್ಟು** *siṭṭu*, hot, quick anger, **ಕ್ರೋಧ** *krōdha*, wrath, **ರೋಷ** *rōṣa*, fury, **ಸಿಡುಕು** *siḍuku*, worn-in irritability, **ಮುನಿಸು** *munisu*, the loving sulk, **ತಾಪ** *tāpa*, heat
- **ಕೈಕೊಟ್ಟರು** *(Let down)* — rala's single match for *let down* is the dairy term for milk ejection. Kannada has no noun here either — you say ಕೈಕೊಟ್ಟರು, 'they gave me the hand', meaning they withdrew it at the moment you leaned on it.
- **ದ್ರೋಹ** *(Betrayed)* — ದ್ರೋಹ is grave — the word used for treason and for betraying a guru. Kannada does not have a casual register for this.
- **ಅಸಮಾಧಾನ** *(Resentful)* — Literally 'un-settledness' — the negation of ಸಮಾಧಾನ, consolation. Resentment as a grievance that was never talked down.
- **ಅವಮಾನ** *(Humiliated)* — rala's ತೇಜೋವಧೆ is worth keeping: 'the murder of someone's lustre'. Humiliation as an assassination of light.
- **ಅವಮರ್ಯಾದೆ** *(Disrespected)* — ಮರ್ಯಾದೆ — the respect owed to you in public — is one of the most-used words in Kannada. This is its negation.  
  also said: **ಅಗೌರವ** *agaurava*, disrespect, **ಉಪೇಕ್ಷೆ** *upēkṣe*, being overlooked, **ತಿರಸ್ಕಾರ** *tiraskāra*, rejection, contempt
- **ಗೇಲಿ** *(Ridiculed)* — Laughter turned and pointed. The wound is that a good thing was aimed at you.  
  also said: **ಅಪಹಾಸ್ಯ** *apahāsya*, ridicule, **ಅಣಕ** *aṇaka*, mimicry, **ಅವಹೇಳನ** *avahēḷana*, belittling, **ಕುಚೋದ್ಯ** *kucōdya*, malicious teasing
- **ಕಹಿ** *(Bitter)* — rala gives mostly vegetables. But the metaphor is alive in Kannada too — ಮನಸ್ಸಿನಲ್ಲಿ ಕಹಿ, bitterness in the mind — so the taste-word earns its place here on its own terms, not as a calque.
- **ಆಕ್ರೋಶ** *(Indignant)* — rala's words are plain anger. ಆಕ್ರೋಶ is anger with a case to argue — literally an outcry, the anger of protest.
- **ಭಂಗ** *(Violated)* — A real hole. rala's options are either legal (breaking a rule) or the specific term for sexual assault. There is no neutral Kannada for 'I feel violated' — the therapeutic middle register simply hasn't been built yet.
- **ಸಿಟ್ಟು** *(Mad)* — Hot and quick, and the most-used of the anger words.  
  also said: **ಕೋಪ** *kōpa*, anger, composed, **ಕ್ರೋಧ** *krōdha*, wrath, **ಮುನಿಸು** *munisu*, the loving sulk, **ಸೆಡವು** *seḍavu*, a huff
- **ರೊಚ್ಚು** *(Furious)* — ರೊಚ್ಚಿಗೇಳು — to rise into ರೊಚ್ಚು. Native and physical, where ರೋಷ and ಕ್ರೋಧ are the grander registers of the same heat.  
  also said: **ರೋಷ** *rōṣa*, fury, **ಕ್ರೋಧ** *krōdha*, wrath, **ಆವೇಶ** *āvēśa*, frenzy, possession, **ಉಗ್ರ** *ugra*, ferocious
- **ಹೊಟ್ಟೆಕಿಚ್ಚು** *(Jealous)* — Belly-fire, and everyone knows exactly which organ is burning. ಅಸೂಯೆ and ಮಾತ್ಸರ್ಯ cover the same ground in a cooler register.  
  also said: **ಅಸೂಯೆ** *asūye*, envy, **ಮಾತ್ಸರ್ಯ** *mātsarya*, envious rivalry, **ಕರುಬು** *karubu*, to begrudge, to smoulder, **ಹೊಟ್ಟೆಯುರಿ** *hoṭṭeyuri*, the burn of being wronged
- **ಜಗಳಗಂಟ** *(Aggressive)* — 'Quarrel-knot' — a person who ties fights. rala offered this one itself.  
  also said: **ಆಕ್ರಮಣಶೀಲ** *ākramaṇaśīla*, aggressive, **ಕಾದಾಟ** *kādāṭa*, fighting, **ಹಟಮಾರಿ** *haṭamāri*, obstinate and combative
- **ಕೆರಳಿಕೆ** *(Provoked)* — ಕೆಣಕು is the good one: to poke a thing that was sitting quietly.
- **ಹಗೆತನ** *(Hostile)* — ಹಗೆ is the old native word for enemy, and it is heavy — the enmity of feuds and epics, not of office politics.
- **ರೇಜಿಗೆ** *(Frustrated)* — rala reads *frustrate* as 'to thwart' — an outcome. Frustration as an ongoing state is ರೇಜಿಗೆ: exasperation at something that keeps not working.
- **ಕೆಂಡಾಮಂಡಲ** *(Infuriated)* — 'A whole mandala of live coals.' One of the finest anger words in the language, and unfindable from English.
- **ಕಿರಿಕಿರಿ** *(Annoyed)* — Onomatopoeia again — the sound of a small grating thing. Kannada builds its minor irritations out of noise.
- **ಬಿಗುಮಾನ** *(Distant)* — rala found it exactly. ಬಿಗುಮಾನ is stiffness held on purpose — reserve that is also a kind of self-regard. And note its opposite in rala's own list: ಸಲಿಗೆ ಇಲ್ಲದ, 'without ಸಲಿಗೆ'.
- **ಮುದುಡು** *(Withdrawn)* — rala only knows withdrawn tenders. ಮುದುಡು is what a leaf or a touched mimosa does — to fold inward. Exactly right for a person.
- **ಮರಗಟ್ಟು** *(Numb)* — ಮರ + ಕಟ್ಟು: to turn to wood. Used for a foot that has gone to sleep and for a grief that has stopped registering.
- **ಟೀಕೆ** *(Critical)* — Physics and statistics, mostly. ಟೀಕೆ is fault-finding; ವಿಮರ್ಶೆ, also in the list, is the honourable kind — literary criticism. Kannada distinguishes the two, English does not.
- **ಅನುಮಾನ** *(Skeptical)* — Four graded words for doubt. ಶಂಕೆ leans toward fear, ಸಂಶಯ toward suspicion of a person, ಸಂದೇಹ toward uncertainty about a fact.
- **ಉಡಾಫೆ** *(Dismissive)* — ಉಡಾಫೆ is dismissiveness worn as a style — breezy, unbothered, faintly insulting. ಅಸಡ್ಡೆ and ತಾತ್ಸಾರ are the colder cousins.

</details>

### ಅಸಹ್ಯ · Disgusted — *asahya*

| ring | ಕನ್ನಡ | roman | English slot | status | rala's hits |
|---|---|---|---|---|---|
| core | **ಅಸಹ್ಯ** | *asahya* | Disgusted | `direct` | ಅಸಹ್ಯ, ಜಿಗುಪ್ಸೆ, ಹೇಸಿಕೆ, ರೋಸು, ವಾಕರಿಕೆ |
| branch | **ಒಪ್ಪದಿರು** | *oppadiru* | Disapproving | `direct` | ಅಸಮ್ಮತಿ, ಮೆಚ್ಚದಿರು, ಒಪ್ಪದಿರು |
| leaf | **ಕೊಂಕು** | *koṅku* | Judgmental | `shaped` | ನ್ಯಾಯಾಧೀಶ ⟨judge⟩, ಜಿಲ್ಲಾ ನ್ಯಾಯಾಧೀಶ ⟨district judge⟩, ಖಂಡನೆ |
| leaf | **ಮುಜುಗರ** | *mujugara* | Embarrassed | `direct` | ಮುಜುಗರ ಉಂಟಾದ |
| branch | **ನಿರಾಸೆ** | *nirāse* | Disappointed | `direct` | ನಿರಾಶೆಗೊಂಡ, ಆಶಾಭಂಗ, ಹತಾಶೆ |
| leaf | **ಹೌಹಾರು** | *hauhāru* | Appalled | `direct` | ದಿಗ್ಭ್ರಮೆಗೊಂಡ, ಭೀತ, ಗಾಬರಿಗೊಂಡ |
| leaf | **ರೋಸು** | *rōsu* | Revolted | `shaped` | ದಂಗೆ ⟨rebellion⟩, ಬಂಡಾಯ, ವಿದ್ರೋಹ |
| branch | **ಘೋರ** | *ghōra* | Awful | `shaped` | ಭಯಾನಕವಾದ, ಭೀಕರ |
| leaf | **ವಾಕರಿಕೆ** | *vākarike* | Nauseated | `direct` | ವಾಕರಿಕೆ, ಓಕರಿಕೆ, ಹೊಟ್ಟೆ ತೊಳಸು |
| leaf | **ಹೇಸಿಗೆ** | *hēsige* | Detestable | `direct` | ಹೇಸು, ಅಸಹ್ಯಪಡು, ಹೇಸಿಗೆ ಪಡು |
| branch | **ಜಿಗುಪ್ಸೆ** | *jigupse* | Repelled | `direct` | ಜಿಗುಪ್ಸೆಗೊಳಿಸು, ಹಿಮ್ಮೆಟ್ಟಿಸು, ವಿಕರ್ಷಿಸು |
| leaf | **ದಿಗಿಲು** | *digilu* | Horrified | `direct` | ದಿಗಿಲುಗೊಳಿಸು, ಭಯಹುಟ್ಟಿಸು, ದಿಕ್ಕುಗೆಡಿಸು |
| leaf | **ಹಿಂಜರಿಕೆ** | *hiñjarike* | Hesitant | `direct` | ಹಿಂಜರಿಯುವ, ಹಿಮ್ಮೆಟ್ಟುವ, ಶಂಕೆಯುಳ್ಳ |

<details><summary>Reading</summary>

- **ಅಸಹ್ಯ** *(Disgusted)* — ಅಸಹ್ಯ literally means 'unbearable' — what cannot be borne. Kannada files disgust under endurance rather than under taste.  
  also said: **ಜಿಗುಪ್ಸೆ** *jigupse*, world-weary revulsion, **ಜುಗುಪ್ಸೆ** *jugupse*, the same, other spelling, **ಹೇಸಿಗೆ** *hēsige*, filth, loathing, **ರೋಸು** *rōsu*, fed up to nausea, **ವಾಕರಿಕೆ** *vākarike*, nausea
- **ಒಪ್ಪದಿರು** *(Disapproving)* — Kannada's ordinary form here is the plain negative verb: they did not agree.  
  also said: **ಅಸಮ್ಮತಿ** *asammati*, dissent, **ಮೆಚ್ಚದಿರು** *meccadiru*, to not approve, **ಆಕ್ಷೇಪ** *ākṣēpa*, objection
- **ಕೊಂಕು** *(Judgmental)* — rala went straight to the judiciary. ಕೊಂಕು is the crooked remark — fault-finding delivered sideways, which is how it usually arrives.
- **ಮುಜುಗರ** *(Embarrassed)* — ಮುಜುಗರ is social awkwardness — the wince at a scene, often on someone else's behalf.  
  also said: **ಸಂಕೋಚ** *saṅkōca*, shrinking, **ಇರುಸುಮುರುಸು** *irusumurusu*, squirming discomfort, **ಕಸಿವಿಸಿ** *kasivisi*, small unease
- **ನಿರಾಸೆ** *(Disappointed)* — ನಿರಾಸೆ = ನಿರ್ + ಆಸೆ, de-hoped. ಆಶಾಭಂಗ, also offered, is stronger: hope actually broken.
- **ಹೌಹಾರು** *(Appalled)* — Onomatopoeic — to recoil bodily on hearing something.  
  also said: **ದಿಗ್ಭ್ರಮೆ** *digbhrame*, stupefaction, **ಬೆಚ್ಚಿಬೀಳು** *beccibīḷu*, to be startled and drop, **ಗಾಬರಿ** *gābari*, panic
- **ರೋಸು** *(Revolted)* — rala took *revolt* politically — every hit is an uprising. ರೋಸಿಹೋಗಿದೆ is the feeling: fed up to the point of nausea.
- **ಘೋರ** *(Awful)* — Used for an accident and for a cricket collapse alike.  
  also said: **ಅಸಹನೀಯ** *asahanīya*, unbearable, **ಭೀಕರ** *bhīkara*, dire, **ಕೆಟ್ಟ** *keṭṭa*, bad, of quality or morals
- **ವಾಕರಿಕೆ** *(Nauseated)* — ಹೊಟ್ಟೆ ತೊಳಸು — 'the stomach stirs'. Kannada has a full vocabulary for the gut, and uses it for feelings without apology.
- **ಹೇಸಿಗೆ** *(Detestable)* — ಹೇಸಿಗೆ is also literally filth. The moral and the physical are the same word — no metaphor required.  
  also said: **ಅಸಹ್ಯ** *asahya*, disgust, **ಕೊಳಕು** *koḷaku*, dirt, **ಜುಗುಪ್ಸೆ** *jugupse*, revulsion
- **ಜಿಗುಪ್ಸೆ** *(Repelled)* — ಜಿಗುಪ್ಸೆ is world-weary revulsion — the disgust that makes people renounce things, not just push a plate away.
- **ಹಿಂಜರಿಕೆ** *(Hesitant)* — ಹಿಂಜರಿ — to slide backwards. The foot that starts to move and then doesn't.

</details>

### ದುಃಖ · Sad — *duḥkha*

| ring | ಕನ್ನಡ | roman | English slot | status | rala's hits |
|---|---|---|---|---|---|
| core | **ದುಃಖ** | *duḥkha* | Sad | `direct` | ದುಃಖಕರ, ವಿಷಾದಕರ, ಶೋಚನೀಯ, ಕುಗ್ಗಿದ, ಸೊರಗಿದ, ಅಮಂಗಳ ⟨inauspicious⟩ |
| branch | **ಒಂಟಿತನ** | *oṇṭitana* | Lonely | `direct` | ಒಂಟಿ, ಏಕಾಂಗಿ, ಒಬ್ಬನೇ |
| leaf | **ಏಕಾಂಗಿ** | *ēkāṅgi* | Isolated | `shaped` | ಪ್ರತ್ಯೇಕಿಸಿದ, ಬೇರ್ಪಡಿಸಿದ, ಪ್ರತ್ಯೇಕ ಸ್ಥಳ |
| leaf | **ತಬ್ಬಲಿ** | *tabbali* | Abandoned | `shaped` | ತೊರೆದ ಪ್ರದೇಶ ⟨abandoned area⟩, ತಬ್ಬಲಿ |
| branch | **ದುರ್ಬಲತೆ** | *durbalate* | Vulnerable | `gap` | ಸುಭೇದ್ಯ, ಭೇದ್ಯ, ದುರ್ಬಲ ಸ್ಥಿತಿ ⟨vulnerable stage⟩ |
| leaf | **ಬಲಿಪಶು** | *balipaśu* | Victimised | `direct` | ಬಲಿಪಶುಮಾಡು, ಪೀಡಿಸು, ಸತಾಯಿಸು |
| leaf | **ನಾಜೂಕು** | *nājūku* | Fragile | `direct` | ನಾಜೂಕಾದ, ಭಂಗುರ, ಶಿಥಿಲ |
| branch | **ಹತಾಶೆ** | *hatāśe* | Despair | `direct` | ಹತಾಶೆ, ನಿರಾಶೆ, ಎದೆಗುಂದು, ಆಸೆಗೆಡು |
| leaf | **ಅಳಲು** | *aḷalu* | Grief | `direct` | ಅಳಲು, ಶೋಕ, ಸಂಕಟ, ಕೊರಗು, ವ್ಯಥೆ |
| leaf | **ಕೈಲಾಗದು** | *kailāgadu* | Powerless | `shaped` | ಶಕ್ತಿಹೀನ, ಬಲಹೀನ, ದುರ್ಬಲ |
| branch | **ಪಾಪಪ್ರಜ್ಞೆ** | *pāpa-prajñe* | Guilty | `shaped` | ಅಪರಾಧಿ, ತಪ್ಪಿತಸ್ಥ, ದೋಷಿ, ಅಪರಾಧಿ ಮನೋಭಾವ ⟨guilty mind⟩ |
| leaf | **ನಾಚಿಕೆ** | *nāchike* | Ashamed | `shaped` | ಅವಮಾನಗೊಂಡ, ಮಾನಗೆಟ್ಟ |
| leaf | **ಪಶ್ಚಾತ್ತಾಪ** | *paścāttāpa* | Remorseful | `direct` | ಪಶ್ಚಾತ್ತಾಪ, ಅನುತಾಪ, ಮರುಕ |
| branch | **ಖಿನ್ನತೆ** | *khinnate* | Depressed | `shaped` | ದಲಿತ ವರ್ಗ ⟨depressed classes⟩, ಶೋಷಿತ, ಕುಗ್ಗಿದ, ನಿರುತ್ಸಾಹದ |
| leaf | **ಕುಗ್ಗು** | *kuggu* | Inferior | `shaped` | ಕುಗ್ಗಿದ, ಇಳಿದ, ತಗ್ಗಿದ |
| leaf | **ಬರಿದು** | *baridu* | Empty | `shaped` | ಬರಿದು, ಖಾಲಿ, ಪೊಳ್ಳು, ಶೂನ್ಯ |
| branch | **ನೋವು** | *nōvu* | Hurt | `direct` | ನೋವು, ನೋಯಿಸು, ಗಾಯ, ಸಾಧಾರಣ ಗಾಯ ⟨simple hurt, IPC⟩ |
| leaf | **ಆಶಾಭಂಗ** | *āśābhaṅga* | Disappointed | `direct` | ಆಶಾಭಂಗ, ನಿರಾಶೆಗೊಂಡ |
| leaf | **ಸಂಕೋಚ** | *saṅkōca* | Embarrassed | `shaped` | ಮುಜುಗರ ಉಂಟಾದ |

<details><summary>Reading</summary>

- **ದುಃಖ** *(Sad)* — Note ಅಶುಭ / ಅಮಂಗಳ in rala's list — 'inauspicious'. For a large part of Kannada usage, sadness and bad omen are adjacent ideas; a sad event is an unlucky one.  
  also said: **ಶೋಕ** *śōka*, formal mourning, **ವ್ಯಥೆ** *vyathe*, affliction, **ಸಂಕಟ** *saṅkaṭa*, the chest closing, **ಕೊರಗು** *koragu*, the grief that thins you, **ವಿಷಾದ** *viṣāda*, melancholy, **ಅಳಲು** *aḷalu*, the wail
- **ಒಂಟಿತನ** *(Lonely)* — Kannada draws a line English blurs: ಒಂಟಿತನ is loneliness and it hurts; ಏಕಾಂತ is solitude, chosen, and is good for you. Same 'alone', opposite verdicts.  
  also said: **ಏಕಾಂತ** *ēkānta*, solitude, chosen and good, **ಒಬ್ಬಂಟಿ** *obbaṇṭi*, all by oneself, **ನಿರ್ಜನ** *nirjana*, deserted
- **ಏಕಾಂಗಿ** *(Isolated)* — 'Single-bodied' — cut off with no one on your side.  
  also said: **ಒಂಟಿ** *oṇṭi*, alone, **ದಿಕ್ಕಿಲ್ಲದ** *dikkillada*, without a direction to turn, **ಅನಾಥ** *anātha*, without protector
- **ತಬ್ಬಲಿ** *(Abandoned)* — ತಬ್ಬಲಿ means orphan, and it is used far past its literal sense — for anyone left without their people. One of the saddest words in the language. Orphan — used far past its literal sense, for anyone left without their people. One of the saddest words in the language.
- **ದುರ್ಬಲತೆ** *(Vulnerable)* — The clearest gap on the wheel. Every Kannada option means weak, breachable, at risk — all pejorative. The warm English sense of 'vulnerable', where opening up is a strength, has no Kannada word yet; people say ಮನಸ್ಸು ತೆರೆದಿಡುವುದು, 'to keep the mind open', as a description rather than a name.
- **ಬಲಿಪಶು** *(Victimised)* — 'Sacrificial animal'. Kannada's word for victim comes straight off the altar.
- **ನಾಜೂಕು** *(Fragile)* — ನಾಜೂಕು is fragile-and-fine, a compliment about a person's delicacy. ಭಂಗುರ is the philosophical one: that which is destined to break.
- **ಹತಾಶೆ** *(Despair)* — ಹತ + ಆಶೆ: hope, killed. The word contains the murder.
- **ಅಳಲು** *(Grief)* — rala's whole list is worth reading: ಶೋಕ is formal mourning, ಸಂಕಟ is the chest-squeeze, ಕೊರಗು is the grief that thins you over years, ಅಳಲು is the wail itself.  
  also said: **ಶೋಕ** *śōka*, mourning, **ಗೋಳು** *gōḷu*, wretched crying, **ರೋದನ** *rōdana*, lamentation
- **ಕೈಲಾಗದು** *(Powerless)* — rala offers strength-less. ಕೈಲಾಗದತನ is the spoken form: 'the state of the hands not managing it'.
- **ಪಾಪಪ್ರಜ್ಞೆ** *(Guilty)* — rala's hits for *guilty* are all courtroom Kannada — the accused, the convicted. ಪಾಪಪ್ರಜ್ಞೆ, sin-consciousness, comes from the other direction: Kannada's guilt is borrowed either from law or from the temple.
- **ನಾಚಿಕೆ** *(Ashamed)* — ನಾಚಿಕೆ is one word for shyness, modesty and shame — a bride's ನಾಚಿಕೆ and a thief's are the same noun. English needs three words and grades them differently; Kannada trusts context completely.  
  also said: **ಸಂಕೋಚ** *saṅkōca*, shrinking, reticence, **ಮುಜುಗರ** *mujugara*, awkwardness, **ಲಜ್ಜೆ** *lajje*, modesty, shame
- **ಪಶ್ಚಾತ್ತಾಪ** *(Remorseful)* — 'After-heat' — the burn that arrives once the act is over.
- **ಖಿನ್ನತೆ** *(Depressed)* — rala's first hits for *depressed* are ದಲಿತ and ಶೋಷಿತ — from the colonial administrative phrase 'depressed classes'. ಖಿನ್ನತೆ is the clinical word; ಮನಸ್ಸು ಕುಗ್ಗಿದೆ, the mind has shrunk, is the older way of saying it.
- **ಕುಗ್ಗು** *(Inferior)* — The English wheel repeats *inferior* in two branches. Kannada usefully does not: under fear it is ಕೀಳರಿಮೆ, a belief about your rank; here under sadness it is simply shrinking.
- **ಬರಿದು** *(Empty)* — rala's ಪೊಳ್ಳು is the good one — hollow, like a grain with nothing inside it. Used of people who look intact.
- **ನೋವು** *(Hurt)* — ನೋವು is bodily pain and emotional pain with no distinction at all. 'ಮನಸ್ಸಿಗೆ ನೋವಾಯಿತು' — it hurt my mind — is the ordinary way to say you were wounded.  
  also said: **ಬೇನೆ** *bēne*, ache, ailment, **ಯಾತನೆ** *yātane*, torment, **ಬಾಧೆ** *bādhe*, affliction
- **ಆಶಾಭಂಗ** *(Disappointed)* — The second 'disappointed' on the wheel. ನಿರಾಸೆ over in ಅಸಹ್ಯ is hope that faded; ಆಶಾಭಂಗ is hope that snapped.
- **ಸಂಕೋಚ** *(Embarrassed)* — The other 'embarrassed'. ಮುಜುಗರ is the wince at a social scene; ಸಂಕೋಚ is the shrinking-in-on-yourself, the hesitation to ask, to take, to take up room.

</details>

## ಒಡಲ ಚಕ್ರ — the part of the body Kannada sites each feeling in

### ಎದೆ · chest — *ede*

| ring | ಕನ್ನಡ | roman | meaning |
|---|---|---|---|
| core | **ಎದೆ** | *ede* | chest |
| branch | **ಧೈರ್ಯ** | *dhairya* | courage |
| leaf | **ಕೆಚ್ಚೆದೆ** | *keccede* | fierce courage — literally, a chest of embers |
| leaf | **ಎದೆಗಾರಿಕೆ** | *edegārike* | nerve — literally, chest-having |
| branch | **ಕುಗ್ಗು** | *kuggu* | losing heart |
| leaf | **ಎದೆಗುಂದು** | *edegundu* | dismay — literally, the chest sinks |
| leaf | **ಎದೆ ಒಡೆ** | *ede oḍe* | devastation — literally, the chest breaks |
| branch | **ದಿಗಿಲು** | *digilu* | dread |
| leaf | **ಎದೆ ಡವಡವ** | *ede ḍavaḍava* | thudding fear — literally, the chest goes thud-thud |
| leaf | **ಎದೆ ಝಲ್** | *ede jhal* | the jolt of alarm — literally, the chest goes cold, once |
| branch | **ಹೆಮ್ಮೆ** | *hemme* | pride |
| leaf | **ಎದೆ ತುಂಬು** | *ede tumbu* | pride on someone's behalf — literally, the chest fills |
| leaf | **ಎದೆಯುಬ್ಬು** | *edeyubbu* | swelling pride — literally, the chest swells |
| branch | **ಸಂಕಟ** | *saṅkaṭa* | anguish |
| leaf | **ಎದೆ ಭಾರ** | *ede bhāra* | the weight before weeping — literally, the chest is heavy |
| leaf | **ಉಸಿರುಗಟ್ಟು** | *usirugaṭṭu* | suffocation — literally, the breath is blocked |

<details><summary>Reading</summary>

- **ಎದೆ** *(chest)* — Nerve and collapse. Kannada puts courage here rather than in the heart — ಕೆಚ್ಚೆದೆ, a chest of embers — and puts the loss of it here too.
- **ಧೈರ್ಯ** *(courage)* — The chest holding.  
  also said: **ಕೆಚ್ಚು** *keccu*, embers-courage, **ಎದೆಗಾರಿಕೆ** *edegārike*, nerve, **ದಿಟ್ಟತನ** *diṭṭatana*, boldness, **ಛಲ** *chala*, resolve
- **ಕೆಚ್ಚೆದೆ** *(fierce courage)* — ಕೆಚ್ಚು is heat held in the body. The bravery word is thermal, not moral.
- **ಎದೆಗಾರಿಕೆ** *(nerve)* — The willingness to stand up and say it — closer to 'having the guts', one organ higher.
- **ಕುಗ್ಗು** *(losing heart)* — The English wheel repeats *inferior* in two branches. Kannada usefully does not: under fear it is ಕೀಳರಿಮೆ, a belief about your rank; here under sadness it is simply shrinking.
- **ಎದೆಗುಂದು** *(dismay)* — The standard word. Kannada names the physical drop and leaves the feeling to be inferred.
- **ಎದೆ ಒಡೆ** *(devastation)* — Reserved for news that arrives all at once. English 'heartbreak' drifted toward romance; this did not.
- **ದಿಗಿಲು** *(dread)* — The chest reacting before you do.  
  also said: **ಆತಂಕ** *ātaṅka*, anxiety, **ತಳಮಳ** *taḷamaḷa*, churn, **ಭೀತಿ** *bhīti*, terror
- **ಎದೆ ಡವಡವ** *(thudding fear)* — Anticipatory — the fear of a thing you can see coming.
- **ಎದೆ ಝಲ್** *(the jolt of alarm)* — A single event, not a state. There is no English noun for the one jolt.
- **ಹೆಮ್ಮೆ** *(pride)* — The chest filling.  
  also said: **ಅಭಿಮಾನ** *abhimāna*, pride as loyalty, **ಗರ್ವ** *garva*, pride, tipping toward vanity, **ಅಹಂಕಾರ** *ahaṅkāra*, the pride that has gone bad, **ಗತ್ತು** *gattu*, swagger
- **ಎದೆ ತುಂಬು** *(pride on someone's behalf)* — Said watching someone you raised do well. Not self-pride — English needs a whole clause.
- **ಎದೆಯುಬ್ಬು** *(swelling pride)* — One degree louder, and faintly comic if you use it about yourself.
- **ಸಂಕಟ** *(anguish)* — The chest closing.  
  also said: **ತಳಮಳ** *taḷamaḷa*, churn, **ಒದ್ದಾಟ** *oddāṭa*, thrashing about, **ಪರದಾಟ** *paradāṭa*, floundering
- **ಎದೆ ಭಾರ** *(the weight before weeping)* — The state just before tears, named as a load rather than a mood.
- **ಉಸಿರುಗಟ್ಟು** *(suffocation)* — Used for a room, a marriage and a job. Nobody hears it as metaphor.

</details>

### ಹೊಟ್ಟೆ · belly — *hoṭṭe*

| ring | ಕನ್ನಡ | roman | meaning |
|---|---|---|---|
| core | **ಹೊಟ್ಟೆ** | *hoṭṭe* | belly |
| branch | **ಹೊಟ್ಟೆಕಿಚ್ಚು** | *hoṭṭe-kiccu* | envy |
| leaf | **ಅಸೂಯೆ** | *asūye* | envy, formally |
| leaf | **ಕರುಬು** | *karubu* | to begrudge — literally, to smoulder |
| branch | **ಹೊಟ್ಟೆಯುರಿ** | *hoṭṭeyuri* | burning resentment |
| leaf | **ಅಸಮಾಧಾನ** | *asamādhāna* | discontent |
| leaf | **ಸೇಡು** | *sēḍu* | revenge |
| branch | **ತೃಪ್ತಿ** | *tṛpti* | satiety |
| leaf | **ಹೊಟ್ಟೆ ತುಂಬು** | *hoṭṭe tumbu* | enough — literally, the belly is full |
| leaf | **ತಣಿವು** | *taṇivu* | slaked — literally, cooling |
| branch | **ದುರಾಸೆ** | *durāse* | greed |
| leaf | **ಹೊಟ್ಟೆಬಾಕ** | *hoṭṭe-bāka* | glutton — literally, belly-eater |
| leaf | **ಆಸೆಬುರುಕ** | *āseburuka* | grasping — literally, full of wanting |
| branch | **ವಾಕರಿಕೆ** | *vākarike* | revulsion |
| leaf | **ಹೊಟ್ಟೆ ತೊಳಸು** | *hoṭṭe toḷasu* | the stomach stirs — literally, the stomach is stirred |
| leaf | **ಹೇಸಿಗೆ** | *hēsige* | loathing — literally, filth |

<details><summary>Reading</summary>

- **ಹೊಟ್ಟೆ** *(belly)* — Appetite and envy. Kannada is unembarrassed about siting the ugly feelings in the stomach, and says them out loud.
- **ಹೊಟ್ಟೆಕಿಚ್ಚು** *(envy)* — Belly-fire, and everyone knows exactly which organ is burning. ಅಸೂಯೆ and ಮಾತ್ಸರ್ಯ cover the same ground in a cooler register.  
  also said: **ಅಸೂಯೆ** *asūye*, envy, **ಮಾತ್ಸರ್ಯ** *mātsarya*, envious rivalry, **ಕರುಬು** *karubu*, to begrudge, to smoulder, **ಹೊಟ್ಟೆಯುರಿ** *hoṭṭeyuri*, the burn of being wronged
- **ಅಸೂಯೆ** *(envy, formally)* — Correct, literary, and not what anyone says at home.
- **ಕರುಬು** *(to begrudge)* — Native verb. The low-grade continuous version of the same fire.
- **ಹೊಟ್ಟೆಯುರಿ** *(burning resentment)* — Distinct from envy: the heat of having been wronged, not of wanting what another has.
- **ಅಸಮಾಧಾನ** *(discontent)* — 'Un-settledness' — a grievance nobody talked down.
- **ಸೇಡು** *(revenge)* — ಸೇಡು ತೀರಿಸಿಕೊಳ್ಳು — to settle it — treats revenge as a debt.
- **ತೃಪ್ತಿ** *(satiety)* — The belly at rest.  
  also said: **ಸಂತೃಪ್ತಿ** *santṛpti*, full satisfaction, **ತಣಿವು** *taṇivu*, slaked, **ಸಮಾಧಾನ** *samādhāna*, settledness
- **ಹೊಟ್ಟೆ ತುಂಬು** *(enough)* — Used far past food: a full belly is the standard image for having had sufficient of anything.
- **ತಣಿವು** *(slaked)* — Satisfaction as cooling rather than filling — the other half of how Kannada thinks about want.
- **ದುರಾಸೆ** *(greed)* — ಆಸೆ is desire and is morally neutral; the prefix does all the work.
- **ಹೊಟ್ಟೆಬಾಕ** *(glutton)* — An insult about appetite that transfers cleanly to money and power.
- **ಆಸೆಬುರುಕ** *(grasping)* — The -ಬುರುಕ suffix makes any noun into a person overfull of it.
- **ವಾಕರಿಕೆ** *(revulsion)* — The belly rejecting.
- **ಹೊಟ್ಟೆ ತೊಳಸು** *(the stomach stirs)* — Moral disgust and physical nausea in one phrase, with no marker between them.
- **ಹೇಸಿಗೆ** *(loathing)* — The moral and the physical are the same word.  
  also said: **ಅಸಹ್ಯ** *asahya*, disgust, **ಕೊಳಕು** *koḷaku*, dirt, **ಜುಗುಪ್ಸೆ** *jugupse*, revulsion

</details>

### ಕರುಳು · gut — *karuḷu*

| ring | ಕನ್ನಡ | roman | meaning |
|---|---|---|---|
| core | **ಕರುಳು** | *karuḷu* | gut |
| branch | **ಕನಿಕರ** | *kanikara* | compassion |
| leaf | **ಕರುಳು ಚುರುಕ್** | *karuḷu curuk* | the pang of pity — literally, the gut stings |
| leaf | **ಮರುಕ** | *maruka* | pity, ruth — literally, turning back toward |
| branch | **ಮರುಗು** | *maragu* | grieving for another |
| leaf | **ಕರುಳು ಹಿಂಡು** | *karuḷu hiṇḍu* | wrung with pity — literally, the gut is wrung |
| leaf | **ತಳಮಳ** | *taḷamaḷa* | churn |
| branch | **ಅಗಲಿಕೆ** | *agalike* | loss, parting |
| leaf | **ಕರುಳು ಕಿತ್ತು ಬರು** | *karuḷu kittu baru* | losing your own — literally, the gut tears loose |
| leaf | **ಉಮ್ಮಳ** | *ummaḷa* | grief welling up — literally, a swelling from below |
| branch | **ಮಮತೆ** | *mamate* | attachment-love |
| leaf | **ಕರುಳ ಬಳ್ಳಿ** | *karuḷa baḷḷi* | one's own child — literally, the gut-vine |
| leaf | **ವಾತ್ಸಲ್ಯ** | *vātsalya* | downward tenderness — literally, the feeling toward a calf |

<details><summary>Reading</summary>

- **ಕರುಳು** *(gut)* — The most untranslatable seat. In Kannada the gut is the organ of kinship — your child is your ಕರುಳ ಬಳ್ಳಿ, your gut-vine — so every feeling sited here is about your own people.
- **ಕನಿಕರ** *(compassion)* — What the gut does when it sees suffering.  
  also said: **ಅನುಕಂಪ** *anukampa*, fellow-feeling, **ಮರುಕ** *maruka*, pity, ruth, **ಕರುಣೆ** *karuṇe*, mercy, **ದಯೆ** *daye*, kindness
- **ಕರುಳು ಚುರುಕ್** *(the pang of pity)* — Involuntary, on seeing a child or an animal in distress. Pity is a judgement; this is a reflex.
- **ಮರುಕ** *(pity, ruth)* — Older and softer than ಕನಿಕರ, and slightly literary now.
- **ಮರುಗು** *(grieving for another)* — ಮರುಗು is a native verb with no exact English partner: to ache on someone else's account. The gut under strain.
- **ಕರುಳು ಹಿಂಡು** *(wrung with pity)* — The image is wringing a wet cloth. Used for watching suffering you cannot stop.
- **ತಳಮಳ** *(churn)* — The word for boiling liquid and for a mind that will not settle.
- **ಅಗಲಿಕೆ** *(loss, parting)* — The gut torn.
- **ಕರುಳು ಕಿತ್ತು ಬರು** *(losing your own)* — Kept for the death of a child or parent. Using it lightly would be shocking.
- **ಉಮ್ಮಳ** *(grief welling up)* — Names the swell, not the weeping.
- **ಮಮತೆ** *(attachment-love)* — The gut as a tie.
- **ಕರುಳ ಬಳ್ಳಿ** *(one's own child)* — The umbilical cord as a creeper. English has no everyday phrase saying kinship is physical.
- **ವಾತ್ಸಲ್ಯ** *(downward tenderness)* — Flows one way only: elder to younger. English 'love' has no direction; this word is nothing but direction.  
  also said: **ಮಮತೆ** *mamate*, attachment-love, **ಅಕ್ಕರೆ** *akkare*, fondness, **ಕಕ್ಕುಲತೆ** *kakkulate*, anxious tenderness

</details>

### ಮನಸ್ಸು · mind — *manassu*

| ring | ಕನ್ನಡ | roman | meaning |
|---|---|---|---|
| core | **ಮನಸ್ಸು** | *manassu* | mind |
| branch | **ನೋವು** | *nōvu* | hurt |
| leaf | **ಮನಸ್ಸಿಗೆ ನೋವು** | *manassige nōvu* | being wounded — literally, pain to the mind |
| leaf | **ಮನಸ್ತಾಪ** | *manastāpa* | a falling-out — literally, mind-heat |
| branch | **ಖಿನ್ನತೆ** | *khinnate* | lowness |
| leaf | **ಮನಸ್ಸು ಕುಗ್ಗು** | *manassu kuggu* | the mind shrinks — literally, the mind shrinks down |
| leaf | **ಬೇಸರ** | *bēsara* | weary discontent |
| branch | **ತೆರೆದುಕೊಳ್ಳು** | *teredukoḷḷu* | opening up |
| leaf | **ಮನಸ್ಸು ಬಿಚ್ಚು** | *manassu biccu* | to unfold the mind — literally, to untie the mind |
| leaf | **ಸಲಿಗೆ** | *salige* | earned informality |
| branch | **ಕರಗು** | *karagu* | being moved |
| leaf | **ಮನ ಮುಟ್ಟು** | *mana muṭṭu* | it touched me — literally, it touched the mind |
| leaf | **ಮೆಚ್ಚುಗೆ** | *meccuge* | admiration |
| branch | **ನೆಮ್ಮದಿ** | *nemmadi* | peace of mind |
| leaf | **ಮನಸ್ಸು ಹಗುರ** | *manassu hagura* | relief — literally, the mind is light |
| leaf | **ಸಮಾಧಾನ** | *samādhāna* | being consoled — literally, a settling |
| branch | **ಒಪ್ಪಿಗೆ** | *oppige* | assent |
| leaf | **ಮನಸ್ಸು ಒಪ್ಪು** | *manassu oppu* | felt consent — literally, the mind agrees |
| leaf | **ಮನಃಪೂರ್ವಕ** | *manaḥpūrvaka* | wholeheartedly — literally, mind-first |

<details><summary>Reading</summary>

- **ಮನಸ್ಸು** *(mind)* — The general seat, and the only one that is not an organ you could point to. Everything a body does, the ಮನಸ್ಸು does — it fills, shrinks, lightens, opens.
- **ನೋವು** *(hurt)* — ನೋವು is bodily and emotional pain with no distinction at all.  
  also said: **ಬೇನೆ** *bēne*, ache, ailment, **ಯಾತನೆ** *yātane*, torment, **ಬಾಧೆ** *bādhe*, affliction
- **ಮನಸ್ಸಿಗೆ ನೋವು** *(being wounded)* — The ordinary way to say someone hurt you.
- **ಮನಸ್ತಾಪ** *(a falling-out)* — Between two people who were close. Not anger, not grief — the cooled residue that keeps them apart.
- **ಖಿನ್ನತೆ** *(lowness)* — rala's first hits for *depressed* are ದಲಿತ and ಶೋಷಿತ — from the colonial administrative phrase 'depressed classes'. ಖಿನ್ನತೆ is the clinical word; ಮನಸ್ಸು ಕುಗ್ಗಿದೆ, the mind has shrunk, is the older way of saying it.
- **ಮನಸ್ಸು ಕುಗ್ಗು** *(the mind shrinks)* — What Kannada said before ಖಿನ್ನತೆ was coined. A description, where the new word is a diagnosis.
- **ಬೇಸರ** *(weary discontent)* — One word for bored, mildly sad and fed up. 'ಬೇಸರಾಗಿದೆ' could be any of the three.  
  also said: **ಬೇಜಾರು** *bējāru*, fed up, the same word one register down, **ಸಪ್ಪೆ** *sappe*, flat, unsalted, **ಜಡ** *jaḍa*, inert
- **ತೆರೆದುಕೊಳ್ಳು** *(opening up)* — The nearest Kannada gets to the therapeutic sense of vulnerable — and it is an act, not a state.
- **ಮನಸ್ಸು ಬಿಚ್ಚು** *(to unfold the mind)* — The same verb as untying a knot or opening a parcel.
- **ಸಲಿಗೆ** *(earned informality)* — The licence to tease someone, eat off their plate, drop the honorific. Intimacy defined as permission.  
  also said: **ಆತ್ಮೀಯತೆ** *ātmīyate*, closeness, **ಅನ್ಯೋನ್ಯ** *anyōnya*, mutual, easy with each other, **ನಿಕಟ** *nikaṭa*, near
- **ಕರಗು** *(being moved)* — The mind melting — Kannada's standard image for being touched.
- **ಮನ ಮುಟ್ಟು** *(it touched me)* — The agent is the thing, not you. A song ಮನ ಮುಟ್ಟುತ್ತದೆ.
- **ಮೆಚ್ಚುಗೆ** *(admiration)* — Both the feeling and its expression — to ಮೆಚ್ಚು silently is incomplete.  
  also said: **ಪ್ರಶಂಸೆ** *praśaṁse*, praise, **ಒಲವು** *olavu*, leaning toward, **ಇಷ್ಟ** *iṣṭa*, liking
- **ನೆಮ್ಮದಿ** *(peace of mind)* — Sharply distinct from ಶಾಂತಿ, peace as the absence of conflict.  
  also said: **ಶಾಂತಿ** *śānti*, peace, as the absence of conflict, **ಸಮಾಧಾನ** *samādhāna*, being consoled, **ನಿರಾಳ** *nirāḷa*, unclenched
- **ಮನಸ್ಸು ಹಗುರ** *(relief)* — Specifically after confessing or weeping. Relief as a change in weight.
- **ಸಮಾಧಾನ** *(being consoled)* — Both the comfort someone gives you and the state it produces.  
  also said: **ಸಂತೈಕೆ** *santaike*, consoling, **ನೆಮ್ಮದಿ** *nemmadi*, peace of mind, **ತಣ್ಣಗಾಗು** *taṇṇagāgu*, to cool down
- **ಒಪ್ಪಿಗೆ** *(assent)* — Kannada distinguishes agreeing out loud from your ಮನಸ್ಸು having agreed, and gives you the phrase to say so.
- **ಮನಸ್ಸು ಒಪ್ಪು** *(felt consent)* — You can say yes without this having happened, and everyone knows it.
- **ಮನಃಪೂರ್ವಕ** *(wholeheartedly)* — The adverb you attach to a thank-you to mean you meant it.

</details>

### ತಲೆ · head — *tale*

| ring | ಕನ್ನಡ | roman | meaning |
|---|---|---|---|
| core | **ತಲೆ** | *tale* | head |
| branch | **ಚಿಂತೆ** | *cinte* | worry |
| leaf | **ತಲೆಬಿಸಿ** | *talebisi* | worry as overheating — literally, head-heat |
| leaf | **ಯೋಚನೆ** | *yōcane* | thinking it over |
| branch | **ಗೊಂದಲ** | *gondala* | confusion |
| leaf | **ತಲೆಕೆಡು** | *talekeḍu* | driven out of your mind — literally, the head spoils |
| leaf | **ಕಕ್ಕಾಬಿಕ್ಕಿ** | *kakkābikki* | flustered |
| branch | **ಹೈರಾಣ** | *hairāṇa* | worn out |
| leaf | **ತಲೆ ಸುತ್ತು** | *tale suttu* | can't take any more — literally, the head spins |
| leaf | **ದಣಿವು** | *daṇivu* | tiredness |
| branch | **ಮರ್ಯಾದೆ** | *maryāde* | standing, face |
| leaf | **ತಲೆ ಎತ್ತು** | *tale ettu* | dignity — literally, to raise the head |
| leaf | **ತಲೆತಗ್ಗಿಸು** | *taletaggisu* | shame — literally, to lower the head |

<details><summary>Reading</summary>

- **ತಲೆ** *(head)* — Worry and standing. The head overheats, spoils and spins — and it is also the thing you raise or lower in front of other people.
- **ಚಿಂತೆ** *(worry)* — ಚಿಂತೆ is also simply 'thought'. To worry and to think are the same word.  
  also said: **ಯೋಚನೆ** *yōcane*, thinking it over, **ಕಾಳಜಿ** *kāḷaji*, care, concern, **ತಲೆಬಿಸಿ** *talebisi*, head-heat
- **ತಲೆಬಿಸಿ** *(worry as overheating)* — You can tell someone not to take ತಲೆಬಿಸಿ the way you would tell them to cool down.
- **ಯೋಚನೆ** *(thinking it over)* — Neutral by itself; 'ಯೋಚನೆ ಮಾಡಬೇಡ' means stop worrying.
- **ಗೊಂದಲ** *(confusion)* — Also the word for a noisy crowd — confusion as too many voices at once.  
  also said: **ಕಕ್ಕಾಬಿಕ್ಕಿ** *kakkābikki*, flustered, **ತಬ್ಬಿಬ್ಬು** *tabbibbu*, thrown, at a loss, **ಗಲಿಬಿಲಿ** *galibili*, muddle
- **ತಲೆಕೆಡು** *(driven out of your mind)* — Same verb as milk going off. Covers exam season and genuine breakdown, with tone doing the work.
- **ಕಕ್ಕಾಬಿಕ್ಕಿ** *(flustered)* — A sound-word with no parts that mean anything alone — the flap of not knowing what to do with your hands.
- **ಹೈರಾಣ** *(worn out)* — Overwhelm as depletion rather than dread.
- **ತಲೆ ಸುತ್ತು** *(can't take any more)* — Physical dizziness and being overwhelmed share the phrase entirely.
- **ದಣಿವು** *(tiredness)* — The only match rala had for *tired* was agronomy — ದಣಿದ ಮಣ್ಣು, exhausted soil. ದಣಿವು is used of a body and of a day alike.  
  also said: **ಆಯಾಸ** *āyāsa*, fatigue, **ಬಳಲಿಕೆ** *baḷalike*, exhaustion, **ಸುಸ್ತು** *sustu*, done in
- **ಮರ್ಯಾದೆ** *(standing, face)* — One of the most-used words in Kannada. Self-respect described entirely as a posture held in public.
- **ತಲೆ ಎತ್ತು** *(dignity)* — ಘನತೆ is the abstract noun; this is what people actually say.
- **ತಲೆತಗ್ಗಿಸು** *(shame)* — The same axis in the other direction. Kannada's shame is visible before it is internal.

</details>

### ಮೈ · body — *mai*

| ring | ಕನ್ನಡ | roman | meaning |
|---|---|---|---|
| core | **ಮೈ** | *mai* | body |
| branch | **ಪುಳಕ** | *puḷaka* | thrill |
| leaf | **ಮೈ ಝುಮ್** | *mai jhum* | the thrill of music — literally, the body tingles |
| leaf | **ರೋಮಾಂಚ** | *rōmāñca* | horripilation — literally, hair-motion |
| branch | **ನಡುಕ** | *naḍuka* | the body's alarm |
| leaf | **ಮೈ ನವಿರೇಳು** | *mai navirēḷu* | awe or dread — literally, the fine hair stands |
| leaf | **ಬೆವರು** | *bevaru* | sweat |
| branch | **ಉರಿ** | *uri* | burning |
| leaf | **ಮೈ ಉರಿ** | *mai uri* | rage gone physical — literally, the body burns |
| leaf | **ಸಿಡುಕು** | *siḍuku* | worn-in irritability |
| branch | **ಮೈಮರೆವು** | *maimarevu* | absorption |
| leaf | **ಮೈ ಮರೆ** | *mai mare* | lost in it — literally, to forget the body |
| leaf | **ಭಾವಪರವಶ** | *bhāva-paravaśa* | carried away — literally, subject to the feeling |

<details><summary>Reading</summary>

- **ಮೈ** *(body)* — The surface. Everything here is involuntary and visible — the hair standing up, the burn, the forgetting of the body altogether.
- **ಪುಳಕ** *(thrill)* — Classical poetics counts it as visible evidence of an inner state, which is why it has its own noun.
- **ಮೈ ಝುಮ್** *(the thrill of music)* — Specifically aesthetic. You would say it about a raga, rarely about good news.
- **ರೋಮಾಂಚ** *(horripilation)* — The Sanskrit register of exactly the same event.
- **ನಡುಕ** *(the body's alarm)* — The skin knowing before the mind does. Kannada names the tremble and lets the fear be inferred.
- **ಮೈ ನವಿರೇಳು** *(awe or dread)* — Which of the two it is comes from context alone. Kannada declines to separate the physiology.
- **ಬೆವರು** *(sweat)* — 'ಬೆವರಿಬಿಟ್ಟೆ' — I broke into a sweat — is a complete statement about fear.
- **ಉರಿ** *(burning)* — The point at which anger stops being an opinion.
- **ಮೈ ಉರಿ** *(rage gone physical)* — Also literally a fever or a rash — the phrase does not choose.
- **ಸಿಡುಕು** *(worn-in irritability)* — Not an episode but a temperament, and one you wear on your face.
- **ಮೈಮರೆವು** *(absorption)* — The body forgotten — the highest praise available for listening to music.
- **ಮೈ ಮರೆ** *(lost in it)* — Also what you say about someone who missed their stop.
- **ಭಾವಪರವಶ** *(carried away)* — ಪರವಶ means under another's control. The grammar says the feeling is driving.

</details>

### ಮುಖ · face — *mukha*

| ring | ಕನ್ನಡ | roman | meaning |
|---|---|---|---|
| core | **ಮುಖ** | *mukha* | face |
| branch | **ಮುನಿಸು** | *munisu* | the loving sulk |
| leaf | **ಮುಖ ಊದಿಸು** | *mukha ūdisu* | sulking — literally, to puff the face |
| leaf | **ಸೆಡವು** | *seḍavu* | a huff |
| branch | **ಸಪ್ಪೆ** | *sappe* | flatness |
| leaf | **ಮುಖ ಕಪ್ಪಿಡು** | *mukha kappiḍu* | crestfallen — literally, the face darkens |
| leaf | **ಸಪ್ಪೆ ಮೋರೆ** | *sappe mōre* | a long face — literally, an insipid face |
| branch | **ಅಳು** | *aḷu* | weeping |
| leaf | **ಕಣ್ಣು ತುಂಬು** | *kaṇṇu tumbu* | moved to tears — literally, the eyes fill |
| leaf | **ಕಣ್ಣೀರು** | *kaṇṇīru* | tears — literally, eye-water |
| branch | **ಸಿಟ್ಟು** | *siṭṭu* | visible anger |
| leaf | **ಕಣ್ಣು ಕೆಂಪು** | *kaṇṇu kempu* | about to break — literally, red eyes |
| leaf | **ಹುಬ್ಬು ಗಂಟು** | *hubbu gaṇṭu* | a knitted brow — literally, the eyebrows knot |
| branch | **ನಾಚಿಕೆ** | *nāchike* | shyness and shame at once |
| leaf | **ಕಣ್ಣು ತಗ್ಗಿಸು** | *kaṇṇu taggisu* | averting the eyes — literally, to lower the eyes |
| leaf | **ಮುಜುಗರ** | *mujugara* | awkwardness |

<details><summary>Reading</summary>

- **ಮುಖ** *(face)* — The public instrument. These are the feelings other people read off you whether or not you meant them to — which is why the sulk lives here and not in ಕೋಪ.
- **ಮುನಿಸು** *(the loving sulk)* — The anger you are only entitled to with someone who loves you. It wants soothing, not resolution, and would be insulted by an apology that was merely correct.  
  also said: **ಸೆಡವು** *seḍavu*, a huff, **ಕೋಪ** *kōpa*, anger, **ಬಿಗುಮಾನ** *bigumāna*, held stiffness
- **ಮುಖ ಊದಿಸು** *(sulking)* — Described as something you actively do to your own face. The performance is the point.
- **ಸೆಡವು** *(a huff)* — Native, and shorter-lived than ಮುನಿಸು — an afternoon rather than a week.
- **ಸಪ್ಪೆ** *(flatness)* — ಸಪ್ಪೆ is what you call unsalted food. A dejected face is described as under-seasoned.
- **ಮುಖ ಕಪ್ಪಿಡು** *(crestfallen)* — The visible fall when someone hears they were left out.
- **ಸಪ್ಪೆ ಮೋರೆ** *(a long face)* — ಮೋರೆ is the blunt, slightly rude word for a face.
- **ಅಳು** *(weeping)* — The plainest native verb. The eye as the place the mind overflows.
- **ಕಣ್ಣು ತುಂಬು** *(moved to tears)* — Reversible in a way English is not: a sight can also ಕಣ್ಣು ತುಂಬು you, by being beautiful.
- **ಕಣ್ಣೀರು** *(tears)* — Plain compound, no ceremony. Kannada saves its ceremony for the phrases around it.
- **ಸಿಟ್ಟು** *(visible anger)* — Hot and quick, and the most-used of the anger words.  
  also said: **ಕೋಪ** *kōpa*, anger, composed, **ಕ್ರೋಧ** *krōdha*, wrath, **ಮುನಿಸು** *munisu*, the loving sulk, **ಸೆಡವು** *seḍavu*, a huff
- **ಕಣ್ಣು ಕೆಂಪು** *(about to break)* — A warning read by everyone present. The threat is in the description, not in any word for anger.
- **ಹುಬ್ಬು ಗಂಟು** *(a knitted brow)* — The smallest visible unit of displeasure, and often the only one you get.
- **ನಾಚಿಕೆ** *(shyness and shame at once)* — A bride's ನಾಚಿಕೆ and a thief's are the same noun. English needs three words and grades them differently; Kannada trusts context completely.  
  also said: **ಸಂಕೋಚ** *saṅkōca*, shrinking, reticence, **ಮುಜುಗರ** *mujugara*, awkwardness, **ಲಜ್ಜೆ** *lajje*, modesty, shame
- **ಕಣ್ಣು ತಗ್ಗಿಸು** *(averting the eyes)* — The gesture that covers modesty, shyness and guilt without distinguishing them.
- **ಮುಜುಗರ** *(awkwardness)* — The wince at a social scene, often on someone else's behalf.  
  also said: **ಸಂಕೋಚ** *saṅkōca*, shrinking, **ಇರುಸುಮುರುಸು** *irusumurusu*, squirming discomfort, **ಕಸಿವಿಸಿ** *kasivisi*, small unease

</details>

## ರಸಚಕ್ರ — the nine rasas of the Nāṭyaśāstra, opened out into daily Kannada

### ಶೃಂಗಾರ · love, the erotic — *śṛṅgāra*  
ಸ್ಥಾಯಿಭಾವ · ರತಿ · rati, desire

| ring | ಕನ್ನಡ | roman | meaning |
|---|---|---|---|
| core | **ಶೃಂಗಾರ** | *śṛṅgāra* | love, the erotic |
| branch | **ಒಲವು** | *olavu* | fondness, leaning-toward |
| leaf | **ಪ್ರೀತಿ** | *prīti* | love |
| leaf | **ಮೆಚ್ಚುಗೆ** | *meccuge* | liking, approval |
| branch | **ಸರಸ** | *sarasa* | playful flirtation |
| leaf | **ಚೆಲ್ಲಾಟ** | *cellāṭa* | dalliance |
| leaf | **ನಾಚಿಕೆ** | *nāchike* | bashfulness |
| branch | **ವಿರಹ** | *viraha* | the pain of separation |
| leaf | **ಹಂಬಲ** | *hambala* | yearning |
| leaf | **ಕಾತರ** | *kātara* | aching eagerness |
| branch | **ಮೋಹ** | *mōha* | infatuation |
| leaf | **ಸೆಳೆತ** | *seḷeta* | pull, attraction |
| leaf | **ವ್ಯಾಮೋಹ** | *vyāmōha* | obsessive attachment |

<details><summary>Reading</summary>

- **ಶೃಂಗಾರ** *(love, the erotic)* — The first and most argued-over rasa. It is not romance in the modern sense — ಶೃಂಗಾರ covers the whole apparatus of attraction, adornment and separation, and half of it is about being apart.
- **ಒಲವು** *(fondness, leaning-toward)* — Native, and the gentlest of the love words. You have ಒಲವು for a person, a place, or an idea.
- **ಪ್ರೀತಿ** *(love)* — The general word, used for parents, friends and lovers without embarrassment.  
  also said: **ಮಮತೆ** *mamate*, attachment-love, **ವಾತ್ಸಲ್ಯ** *vātsalya*, tenderness flowing downward, **ಅಕ್ಕರೆ** *akkare*, fondness, **ಒಲವು** *olavu*, leaning toward
- **ಮೆಚ್ಚುಗೆ** *(liking, approval)* — Both the feeling and its expression — to ಮೆಚ್ಚು silently is incomplete.  
  also said: **ಪ್ರಶಂಸೆ** *praśaṁse*, praise, **ಒಲವು** *olavu*, leaning toward, **ಇಷ್ಟ** *iṣṭa*, liking
- **ಸರಸ** *(playful flirtation)* — Literally 'with rasa'. The word for banter between people who like each other, and it is not coy about it.
- **ಚೆಲ್ಲಾಟ** *(dalliance)* — Play with a loose edge to it — used affectionately and as a mild accusation.
- **ನಾಚಿಕೆ** *(bashfulness)* — Shyness, modesty and shame in one noun. A bride's ನಾಚಿಕೆ and a thief's are the same word.  
  also said: **ಸಂಕೋಚ** *saṅkōca*, shrinking, reticence, **ಮುಜುಗರ** *mujugara*, awkwardness, **ಲಜ್ಜೆ** *lajje*, modesty, shame
- **ವಿರಹ** *(the pain of separation)* — A whole genre of Kannada poetry sits here. English has no single word, which is why so much of it gets translated as 'longing' and loses the ache.
- **ಹಂಬಲ** *(yearning)* — The pull toward something absent — a place, a person, a life not lived.  
  also said: **ಕಾತರ** *kātara*, aching eagerness, **ತವಕ** *tavaka*, eagerness, **ಹಪಹಪಿ** *hapahapi*, craving
- **ಕಾತರ** *(aching eagerness)* — Waiting that has begun to hurt slightly.
- **ಮೋಹ** *(infatuation)* — In philosophy ಮೋಹ is delusion, one of the six enemies. In daily speech it is simply being besotted — the moral warning is still audible underneath.
- **ಸೆಳೆತ** *(pull, attraction)* — Native and physical: the same word for an undertow and for a muscle cramp.
- **ವ್ಯಾಮೋಹ** *(obsessive attachment)* — ಮೋಹ with the brakes off. Said of parents about children as often as of lovers.

</details>

### ಹಾಸ್ಯ · mirth, the comic — *hāsya*  
ಸ್ಥಾಯಿಭಾವ · ಹಾಸ · hāsa, laughter

| ring | ಕನ್ನಡ | roman | meaning |
|---|---|---|---|
| core | **ಹಾಸ್ಯ** | *hāsya* | mirth, the comic |
| branch | **ನಗು** | *nagu* | laughter |
| leaf | **ನಗೆ** | *nage* | a laugh |
| leaf | **ಕಿಸಿಕಿಸಿ** | *kisikisi* | giggling |
| branch | **ತಮಾಷೆ** | *tamāṣe* | fun |
| leaf | **ತುಂಟತನ** | *ṭuṇṭatana* | mischief |
| leaf | **ಕೀಟಲೆ** | *kīṭale* | teasing |
| branch | **ಗೇಲಿ** | *gēli* | mockery |
| leaf | **ಅಣಕ** | *aṇaka* | mimicry |
| leaf | **ವ್ಯಂಗ್ಯ** | *vyaṅgya* | sarcasm |
| branch | **ಮುಗುಳ್ನಗೆ** | *muguḷnage* | a smile |
| leaf | **ಸಂತಸ** | *santasa* | gladness |
| leaf | **ಹಗುರ** | *hagura* | lightness |

<details><summary>Reading</summary>

- **ಹಾಸ್ಯ** *(mirth, the comic)* — The rasa the English feeling wheel has no room for at all. Kannada grades laughter finely, and most of the grades are about who is being laughed at.
- **ನಗು** *(laughter)* — The plain native verb-noun. Everything else in this sector is a shade of it.
- **ನಗೆ** *(a laugh)* — The countable one — you can have a ನಗೆ, you cannot have a ನಗು.
- **ಕಿಸಿಕಿಸಿ** *(giggling)* — Sound-word. The laughter you are trying and failing to suppress.
- **ತಮಾಷೆ** *(fun)* — Borrowed from Urdu and now completely at home. 'ತಮಾಷೆಗೆ ಹೇಳಿದೆ' — I said it for fun — is the standard retreat.
- **ತುಂಟತನ** *(mischief)* — The naughtiness of a child you are not actually angry with.
- **ಕೀಟಲೆ** *(teasing)* — Teasing you are allowed to do, which means it is a claim about the relationship.
- **ಗೇಲಿ** *(mockery)* — Laughter turned and pointed. The wound is that a good thing was aimed at you.  
  also said: **ಅಪಹಾಸ್ಯ** *apahāsya*, ridicule, **ಅಣಕ** *aṇaka*, mimicry, **ಅವಹೇಳನ** *avahēḷana*, belittling, **ಕುಚೋದ್ಯ** *kucōdya*, malicious teasing
- **ಅಣಕ** *(mimicry)* — Doing an impression of someone to their disadvantage.
- **ವ್ಯಂಗ್ಯ** *(sarcasm)* — In poetics ವ್ಯಂಗ್ಯ is suggested meaning — the good kind. In an argument it is the knife.
- **ಮುಗುಳ್ನಗೆ** *(a smile)* — 'Bud-laugh' — the laugh that has not opened. A compound of exactly the kind Kannada makes best.
- **ಸಂತಸ** *(gladness)* — Softer and more native-feeling than ಸಂತೋಷ, and slightly more literary now.
- **ಹಗುರ** *(lightness)* — The change in weight after something is resolved.

</details>

### ಕರುಣ · compassion, pathos — *karuṇa*  
ಸ್ಥಾಯಿಭಾವ · ಶೋಕ · śōka, grief

| ring | ಕನ್ನಡ | roman | meaning |
|---|---|---|---|
| core | **ಕರುಣ** | *karuṇa* | compassion, pathos |
| branch | **ಅಳಲು** | *aḷalu* | the wail |
| leaf | **ದುಃಖ** | *duḥkha* | sorrow |
| leaf | **ಕಣ್ಣೀರು** | *kaṇṇīru* | tears |
| branch | **ಕನಿಕರ** | *kanikara* | compassion |
| leaf | **ಮರುಕ** | *maruka* | pity, ruth |
| leaf | **ಕರುಳು ಚುರುಕ್** | *karuḷu curuk* | the gut-pang |
| branch | **ಸಂಕಟ** | *saṅkaṭa* | anguish |
| leaf | **ಉಮ್ಮಳ** | *ummaḷa* | grief welling up |
| leaf | **ಕೊರಗು** | *koragu* | pining |
| branch | **ಹಳಹಳಿಕೆ** | *haḷahaḷike* | regret braided with longing |
| leaf | **ಪಶ್ಚಾತ್ತಾಪ** | *paścāttāpa* | remorse |
| leaf | **ವಿಷಾದ** | *viṣāda* | melancholy |

<details><summary>Reading</summary>

- **ಕರುಣ** *(compassion, pathos)* — The rasa Kannada literature is most at home in. Note that it names not grief itself but grief-made-shareable — the feeling an audience has, not the one the character has.
- **ಅಳಲು** *(the wail)* — Native, and it is the sound before it is the feeling.  
  also said: **ಶೋಕ** *śōka*, mourning, **ಗೋಳು** *gōḷu*, wretched crying, **ರೋದನ** *rōdana*, lamentation
- **ದುಃಖ** *(sorrow)* — The general word, and also the technical Buddhist one. Kannada uses it for a bad afternoon.  
  also said: **ಶೋಕ** *śōka*, formal mourning, **ವ್ಯಥೆ** *vyathe*, affliction, **ಸಂಕಟ** *saṅkaṭa*, the chest closing, **ಕೊರಗು** *koragu*, the grief that thins you, **ವಿಷಾದ** *viṣāda*, melancholy, **ಅಳಲು** *aḷalu*, the wail
- **ಕಣ್ಣೀರು** *(tears)* — Eye-water. Plain compound, no ceremony — Kannada saves the ceremony for the phrases around it.
- **ಕನಿಕರ** *(compassion)* — What you feel toward someone whose situation you can see clearly. Not quite pity — there is less height in it.  
  also said: **ಅನುಕಂಪ** *anukampa*, fellow-feeling, **ಮರುಕ** *maruka*, pity, ruth, **ಕರುಣೆ** *karuṇe*, mercy, **ದಯೆ** *daye*, kindness
- **ಮರುಕ** *(pity, ruth)* — 'Turning back toward.' Older and softer, and now slightly literary.
- **ಕರುಳು ಚುರುಕ್** *(the gut-pang)* — The involuntary sting on seeing a child or an animal in distress. Pity is a judgement; this is a reflex.
- **ಸಂಕಟ** *(anguish)* — Felt as constriction — the chest closing. Used equally for a dying person's distress and for an impossible choice.  
  also said: **ತಳಮಳ** *taḷamaḷa*, churn, **ಒದ್ದಾಟ** *oddāṭa*, thrashing about, **ಪರದಾಟ** *paradāṭa*, floundering
- **ಉಮ್ಮಳ** *(grief welling up)* — Names the swell, not the weeping — the moment before it breaks.
- **ಕೊರಗು** *(pining)* — The grief that thins you over years rather than days.
- **ಹಳಹಳಿಕೆ** *(regret braided with longing)* — Remorse for something you would, honestly, do again. English has to use a whole sentence.
- **ಪಶ್ಚಾತ್ತಾಪ** *(remorse)* — 'After-heat' — the burn that arrives once the act is over.
- **ವಿಷಾದ** *(melancholy)* — Sadness with the edges worn off. The word Kannada writers reach for when nothing in particular is wrong.

</details>

### ರೌದ್ರ · fury — *raudra*  
ಸ್ಥಾಯಿಭಾವ · ಕ್ರೋಧ · krōdha, wrath

| ring | ಕನ್ನಡ | roman | meaning |
|---|---|---|---|
| core | **ರೌದ್ರ** | *raudra* | fury |
| branch | **ಸಿಟ್ಟು** | *siṭṭu* | anger |
| leaf | **ಕೋಪ** | *kōpa* | anger, the general word |
| leaf | **ಸಿಡುಕು** | *siḍuku* | irritability |
| branch | **ರೊಚ್ಚು** | *roccu* | rage |
| leaf | **ಕೆಂಡಾಮಂಡಲ** | *keṇḍā-maṇḍala* | incandescent |
| leaf | **ಆವೇಶ** | *āvēśa* | frenzy |
| branch | **ಹಗೆ** | *hage* | enmity |
| leaf | **ದ್ವೇಷ** | *dvēṣa* | hatred |
| leaf | **ಸೇಡು** | *sēḍu* | revenge |
| branch | **ಆಕ್ರೋಶ** | *ākrōśa* | outcry |
| leaf | **ಅಸಮಾಧಾನ** | *asamādhāna* | discontent |
| leaf | **ಬಂಡಾಯ** | *baṇḍāya* | revolt |

<details><summary>Reading</summary>

- **ರೌದ್ರ** *(fury)* — Named for Rudra. The rasa is deliberately grand — a god's anger, not a bad mood — which is why the daily words underneath it feel so much smaller and so much more used.
- **ಸಿಟ್ಟು** *(anger)* — Hot and quick, and the most-used of the anger words.  
  also said: **ಕೋಪ** *kōpa*, anger, composed, **ಕ್ರೋಧ** *krōdha*, wrath, **ಮುನಿಸು** *munisu*, the loving sulk, **ಸೆಡವು** *seḍavu*, a huff
- **ಕೋಪ** *(anger, the general word)* — Slightly more composed than ಸಿಟ್ಟು — you can have ಕೋಪ quietly.  
  also said: **ಸಿಟ್ಟು** *siṭṭu*, hot, quick anger, **ಕ್ರೋಧ** *krōdha*, wrath, **ರೋಷ** *rōṣa*, fury, **ಸಿಡುಕು** *siḍuku*, worn-in irritability, **ಮುನಿಸು** *munisu*, the loving sulk, **ತಾಪ** *tāpa*, heat
- **ಸಿಡುಕು** *(irritability)* — Not an episode but a temperament, and one you wear on your face.
- **ರೊಚ್ಚು** *(rage)* — ರೊಚ್ಚಿಗೇಳು — to rise into ರೊಚ್ಚು. Native and physical, where ರೋಷ and ಕ್ರೋಧ are the grander registers of the same heat.  
  also said: **ರೋಷ** *rōṣa*, fury, **ಕ್ರೋಧ** *krōdha*, wrath, **ಆವೇಶ** *āvēśa*, frenzy, possession, **ಉಗ್ರ** *ugra*, ferocious
- **ಕೆಂಡಾಮಂಡಲ** *(incandescent)* — 'A whole mandala of live coals.' One of the finest anger words in the language.
- **ಆವೇಶ** *(frenzy)* — Also the word for being possessed by a deity. The grammar says the feeling is driving, not you.
- **ಹಗೆ** *(enmity)* — The old native word for an enemy, and heavy — the enmity of feuds, not of office politics.
- **ದ್ವೇಷ** *(hatred)* — Settled and directed. One of the six enemies in the moral vocabulary.
- **ಸೇಡು** *(revenge)* — Native. ಸೇಡು ತೀರಿಸಿಕೊಳ್ಳು — to settle the revenge — treats it as a debt.
- **ಆಕ್ರೋಶ** *(outcry)* — Anger with a case to argue. The word every Kannada news bulletin uses for public anger.
- **ಅಸಮಾಧಾನ** *(discontent)* — 'Un-settledness' — the negation of consolation. A grievance nobody talked down.
- **ಬಂಡಾಯ** *(revolt)* — Also the name of a Kannada literary movement, which is the right amount of baggage.

</details>

### ವೀರ · the heroic — *vīra*  
ಸ್ಥಾಯಿಭಾವ · ಉತ್ಸಾಹ · utsāha, vigour

| ring | ಕನ್ನಡ | roman | meaning |
|---|---|---|---|
| core | **ವೀರ** | *vīra* | the heroic |
| branch | **ಧೈರ್ಯ** | *dhairya* | courage |
| leaf | **ಕೆಚ್ಚು** | *keccu* | fierce courage |
| leaf | **ಎದೆಗಾರಿಕೆ** | *edegārike* | nerve |
| branch | **ಛಲ** | *chala* | resolve |
| leaf | **ಹಠ** | *haṭha* | insistence |
| leaf | **ಪಟ್ಟು** | *paṭṭu* | a hold, a grip |
| branch | **ಹೆಮ್ಮೆ** | *hemme* | pride |
| leaf | **ಅಭಿಮಾನ** | *abhimāna* | pride-as-loyalty |
| leaf | **ಗತ್ತು** | *gattu* | swagger |
| branch | **ಹುರುಪು** | *hurupu* | vigour |
| leaf | **ಉಮೇದು** | *umēdu* | zest |
| leaf | **ಸಂಭ್ರಮ** | *sambhrama* | festive elation |

<details><summary>Reading</summary>

- **ವೀರ** *(the heroic)* — The rasa with no home on the English wheel at all. Its ಸ್ಥಾಯಿಭಾವ is not courage but ಉತ್ಸಾಹ — energy — which quietly claims that heroism is a kind of enthusiasm.
- **ಧೈರ್ಯ** *(courage)* — Steadiness under fear. The everyday word, and the one you tell someone to have.  
  also said: **ಕೆಚ್ಚು** *keccu*, embers-courage, **ಎದೆಗಾರಿಕೆ** *edegārike*, nerve, **ದಿಟ್ಟತನ** *diṭṭatana*, boldness, **ಛಲ** *chala*, resolve
- **ಕೆಚ್ಚು** *(fierce courage)* — Heat held in the body. Kannada's bravery word is thermal, not moral.
- **ಎದೆಗಾರಿಕೆ** *(nerve)* — 'Chest-having' — the willingness to stand up and say it.
- **ಛಲ** *(resolve)* — One of the most-used words in Kannada self-description. Not stubbornness — the refusal to be finished with something.
- **ಹಠ** *(insistence)* — ಛಲ's difficult sibling. A child throwing ಹಠ and a satyagrahi holding it are the same noun.
- **ಪಟ್ಟು** *(a hold, a grip)* — From wrestling. ಪಟ್ಟು ಬಿಡದೆ — without letting go of the hold — is how persistence is described.
- **ಹೆಮ್ಮೆ** *(pride)* — Warm pride, usually in someone else. Distinct from ಅಹಂಕಾರ, which is the pride that has gone bad.  
  also said: **ಅಭಿಮಾನ** *abhimāna*, pride as loyalty, **ಗರ್ವ** *garva*, pride, tipping toward vanity, **ಅಹಂಕಾರ** *ahaṅkāra*, the pride that has gone bad, **ಗತ್ತು** *gattu*, swagger
- **ಅಭಿಮಾನ** *(pride-as-loyalty)* — For your language, your team, your people. Its second sense is the wound when that loyalty is slighted.
- **ಗತ್ತು** *(swagger)* — Native, and affectionately used — the carriage of someone who knows they are good.
- **ಹುರುಪು** *(vigour)* — Native. The energy you start a thing with, before ಛಲ has to take over.
- **ಉಮೇದು** *(zest)* — Borrowed and thoroughly domesticated. 'ಉಮೇದು ಇಲ್ಲ' is a complete diagnosis.
- **ಸಂಭ್ರಮ** *(festive elation)* — Busy, shared, slightly frantic joy — a wedding house at six in the morning. Nobody has ಸಂಭ್ರಮ alone.

</details>

### ಭಯಾನಕ · terror — *bhayānaka*  
ಸ್ಥಾಯಿಭಾವ · ಭಯ · bhaya, fear

| ring | ಕನ್ನಡ | roman | meaning |
|---|---|---|---|
| core | **ಭಯಾನಕ** | *bhayānaka* | terror |
| branch | **ಹೆದರಿಕೆ** | *hedarike* | being scared |
| leaf | **ಅಂಜಿಕೆ** | *añjike* | timidity |
| leaf | **ಬೆದರಿಕೆ** | *bedarike* | a threat |
| branch | **ದಿಗಿಲು** | *digilu* | dread |
| leaf | **ಆತಂಕ** | *ātaṅka* | anxiety |
| leaf | **ತಳಮಳ** | *taḷamaḷa* | churn |
| branch | **ಗಾಬರಿ** | *gābari* | panic |
| leaf | **ಬೆಚ್ಚು** | *beccu* | a startle |
| leaf | **ನಡುಕ** | *naḍuka* | the tremble |
| branch | **ಅಳುಕು** | *aḷuku* | misgiving |
| leaf | **ಹಿಂಜರಿಕೆ** | *hiñjarike* | hesitation |
| leaf | **ಅನುಮಾನ** | *anumāna* | doubt |

<details><summary>Reading</summary>

- **ಭಯಾನಕ** *(terror)* — Kannada's richest sector by count. Fear is graded by intensity and by whether you can see it coming.
- **ಹೆದರಿಕೆ** *(being scared)* — The plain daily word, and the one children are told not to have.
- **ಅಂಜಿಕೆ** *(timidity)* — Fear as a disposition. ಅಂಜುಬುರುಕ, one who is full of it, is a mild insult.
- **ಬೆದರಿಕೆ** *(a threat)* — The threat itself. Kannada places it outside you — 'ಬೆದರಿಕೆ ಇದೆ', there is a threat.  
  also said: **ಹೆದರಿಕೆ** *hedarike*, being scared, **ಬೆಚ್ಚು** *beccu*, a startle, **ಅಪಾಯ** *apāya*, danger
- **ದಿಗಿಲು** *(dread)* — Heavier and more still than ಹೆದರಿಕೆ. The fear that has settled in and is waiting.  
  also said: **ಆತಂಕ** *ātaṅka*, anxiety, **ತಳಮಳ** *taḷamaḷa*, churn, **ಭೀತಿ** *bhīti*, terror
- **ಆತಂಕ** *(anxiety)* — Now the standard clinical word too. Its older sense is closer to 'impediment' — anxiety as the thing in your way.  
  also said: **ಕಳವಳ** *kaḷavaḷa*, agitation, **ಚಿಂತೆ** *cinte*, worry, thought, **ತಳಮಳ** *taḷamaḷa*, churn, **ವ್ಯಾಕುಲ** *vyākula*, distress
- **ತಳಮಳ** *(churn)* — The word for boiling liquid and for a mind that will not settle.
- **ಗಾಬರಿ** *(panic)* — Sudden, visible, and slightly undignified — the fear other people can see you having.
- **ಬೆಚ್ಚು** *(a startle)* — ಬೆಚ್ಚಿಬೀಳು — to be startled and drop. Kannada builds the flinch out of a fall.
- **ನಡುಕ** *(the tremble)* — The body named, the feeling left to be inferred.
- **ಅಳುಕು** *(misgiving)* — The small inward flinch before you do the thing anyway. ಅಭದ್ರತೆ carries the other sense of *insecure* — physically unguarded, a word for buildings and borders.  
  also said: **ಅಭದ್ರತೆ** *abhadrate*, insecurity, of a thing unguarded, **ಹಿಂಜರಿಕೆ** *hiñjarike*, hesitation, **ಶಂಕೆ** *śaṅke*, misgiving with fear in it
- **ಹಿಂಜರಿಕೆ** *(hesitation)* — To slide backwards — the foot that starts to move and then does not.
- **ಅನುಮಾನ** *(doubt)* — One of four graded doubt words. ಶಂಕೆ leans to fear, ಸಂಶಯ to suspicion of a person, ಸಂದೇಹ to uncertainty about a fact.

</details>

### ಬೀಭತ್ಸ · disgust, the odious — *bībhatsa*  
ಸ್ಥಾಯಿಭಾವ · ಜುಗುಪ್ಸೆ · jugupse, revulsion

| ring | ಕನ್ನಡ | roman | meaning |
|---|---|---|---|
| core | **ಬೀಭತ್ಸ** | *bībhatsa* | disgust, the odious |
| branch | **ಅಸಹ್ಯ** | *asahya* | disgust |
| leaf | **ಹೇಸಿಗೆ** | *hēsige* | filth, loathing |
| leaf | **ಕೊಳಕು** | *koḷaku* | dirt |
| branch | **ವಾಕರಿಕೆ** | *vākarike* | nausea |
| leaf | **ಓಕರಿಕೆ** | *ōkarike* | retching |
| leaf | **ಹೊಟ್ಟೆ ತೊಳಸು** | *hoṭṭe toḷasu* | the stomach stirs |
| branch | **ರೋಸು** | *rōsu* | being fed up |
| leaf | **ಬೇಸರ** | *bēsara* | weary discontent |
| leaf | **ರೇಜಿಗೆ** | *rējige* | exasperation |
| branch | **ತಾತ್ಸಾರ** | *tātsāra* | disdain |
| leaf | **ಅಸಡ್ಡೆ** | *asaḍḍe* | not caring, coldly |
| leaf | **ಕೊಂಕು** | *koṅku* | the crooked remark |

<details><summary>Reading</summary>

- **ಬೀಭತ್ಸ** *(disgust, the odious)* — The rasa nobody wants and every tradition keeps. Kannada files disgust under endurance — ಅಸಹ್ಯ literally means what cannot be borne.
- **ಅಸಹ್ಯ** *(disgust)* — 'Unbearable.' The daily word, used for a smell and for a politician with equal ease.  
  also said: **ಜಿಗುಪ್ಸೆ** *jigupse*, world-weary revulsion, **ಜುಗುಪ್ಸೆ** *jugupse*, the same, other spelling, **ಹೇಸಿಗೆ** *hēsige*, filth, loathing, **ರೋಸು** *rōsu*, fed up to nausea, **ವಾಕರಿಕೆ** *vākarike*, nausea
- **ಹೇಸಿಗೆ** *(filth, loathing)* — Also literally filth. The moral and the physical are one word — no metaphor required.  
  also said: **ಅಸಹ್ಯ** *asahya*, disgust, **ಕೊಳಕು** *koḷaku*, dirt, **ಜುಗುಪ್ಸೆ** *jugupse*, revulsion
- **ಕೊಳಕು** *(dirt)* — Native and blunt. Calling a person ಕೊಳಕು is not a comment on hygiene.
- **ವಾಕರಿಕೆ** *(nausea)* — The bodily end of the sector, and Kannada moves between it and the moral end without a signal.
- **ಓಕರಿಕೆ** *(retching)* — Onomatopoeic and unglamorous.
- **ಹೊಟ್ಟೆ ತೊಳಸು** *(the stomach stirs)* — Used for moral revulsion and actual nausea with nothing between the two senses.
- **ರೋಸು** *(being fed up)* — ರೋಸಿಹೋಗಿದೆ — fed up to the point of nausea. The most useful word in this sector.
- **ಬೇಸರ** *(weary discontent)* — One word for bored, mildly sad, and fed up. The listener reads your face for which.  
  also said: **ಬೇಜಾರು** *bējāru*, fed up, the same word one register down, **ಸಪ್ಪೆ** *sappe*, flat, unsalted, **ಜಡ** *jaḍa*, inert
- **ರೇಜಿಗೆ** *(exasperation)* — Disgust at something that keeps not working, rather than at something foul.
- **ತಾತ್ಸಾರ** *(disdain)* — Disgust cooled into a social posture — the version you can hold at a wedding.
- **ಅಸಡ್ಡೆ** *(not caring, coldly)* — Not caring, and not quite bothering to hide that you are not caring.  
  also said: **ನಿರಾಸಕ್ತಿ** *nirāsakti*, disinterest, **ಉದಾಸೀನ** *udāsīna*, indifference, or the cold shoulder, **ತಾತ್ಸಾರ** *tātsāra*, disdain
- **ಕೊಂಕು** *(the crooked remark)* — Fault-finding delivered sideways, which is how it usually arrives.

</details>

### ಅದ್ಭುತ · wonder — *adbhuta*  
ಸ್ಥಾಯಿಭಾವ · ವಿಸ್ಮಯ · vismaya, astonishment

| ring | ಕನ್ನಡ | roman | meaning |
|---|---|---|---|
| core | **ಅದ್ಭುತ** | *adbhuta* | wonder |
| branch | **ಬೆರಗು** | *beragu* | amazement |
| leaf | **ಅಚ್ಚರಿ** | *accari* | surprise |
| leaf | **ದಂಗು** | *daṅgu* | dumbfounded |
| branch | **ಕುತೂಹಲ** | *kutūhala* | curiosity |
| leaf | **ಆಸಕ್ತಿ** | *āsakti* | interest |
| leaf | **ತವಕ** | *tavaka* | eagerness |
| branch | **ಪುಳಕ** | *puḷaka* | the thrill |
| leaf | **ರೋಮಾಂಚ** | *rōmāñca* | horripilation |
| leaf | **ಮೈ ಝುಮ್** | *mai jhum* | the body tingles |
| branch | **ಭಯಭಕ್ತಿ** | *bhaya-bhakti* | awe |
| leaf | **ಗೌರವ** | *gaurava* | respect |
| leaf | **ದಿಗ್ಭ್ರಮೆ** | *digbhrame* | stupefaction |

<details><summary>Reading</summary>

- **ಅದ್ಭುತ** *(wonder)* — The rasa that most resembles a modern emotion. Kannada keeps a native word for it — ಬೆರಗು — which is rarer than it should be.
- **ಬೆರಗು** *(amazement)* — Native. Wonder that stops you where you are.  
  also said: **ವಿಸ್ಮಯ** *vismaya*, astonishment, **ಅಚ್ಚರಿ** *accari*, surprise, **ಸೋಜಿಗ** *sōjiga*, marvel
- **ಅಚ್ಚರಿ** *(surprise)* — ಅಚ್ಚರಿ is the native word and ಆಶ್ಚರ್ಯ the Sanskrit one; both are in daily use, and this wheel uses the shorter.  
  also said: **ಆಶ್ಚರ್ಯ** *āścarya*, surprise, the Sanskrit form, **ವಿಸ್ಮಯ** *vismaya*, astonishment, **ಬೆರಗು** *beragu*, wonder that stops you
- **ದಂಗು** *(dumbfounded)* — ದಂಗಾದೆ — I was floored. The version of astonishment with your mouth open.  
  also said: **ವಿಸ್ಮಯ** *vismaya*, astonishment, **ಆಶ್ಚರ್ಯ** *āścarya*, surprise, **ಬೆರಗು** *beragu*, wonder, **ದಿಗ್ಭ್ರಮೆ** *digbhrame*, stupefaction
- **ಕುತೂಹಲ** *(curiosity)* — Wonder that has turned into a question. Kannada treats it as a virtue.
- **ಆಸಕ್ತಿ** *(interest)* — Literally attachment — interest as a mild binding to a thing.
- **ತವಕ** *(eagerness)* — Eagerness with an edge of ache in it.
- **ಪುಳಕ** *(the thrill)* — Classical poetics counts it as visible evidence of an inner state, which is why it has its own noun.
- **ರೋಮಾಂಚ** *(horripilation)* — 'Hair-motion.' The Sanskrit register of the same event.
- **ಮೈ ಝುಮ್** *(the body tingles)* — The spoken version, and specifically aesthetic — you say it about a raga.
- **ಭಯಭಕ್ತಿ** *(awe)* — Fear-and-devotion, in one compound. Awe as a social posture — how one stands before a deity or a formidable elder.
- **ಗೌರವ** *(respect)* — Something you give, actively, not something you passively have.
- **ದಿಗ್ಭ್ರಮೆ** *(stupefaction)* — 'Directions-confusion' — the compass spins and you cannot tell which way is which.

</details>

### ಶಾಂತ · repose — *śānta*  
ಸ್ಥಾಯಿಭಾವ · ಶಮ · śama, quiet

| ring | ಕನ್ನಡ | roman | meaning |
|---|---|---|---|
| core | **ಶಾಂತ** | *śānta* | repose |
| branch | **ನೆಮ್ಮದಿ** | *nemmadi* | peace of mind |
| leaf | **ನಿರಾಳ** | *nirāḷa* | unclenched |
| leaf | **ಸಮಾಧಾನ** | *samādhāna* | being consoled |
| branch | **ತೃಪ್ತಿ** | *tṛpti* | satiety |
| leaf | **ತಣಿವು** | *taṇivu* | slaked |
| leaf | **ಸಾರ್ಥಕ** | *sārthaka* | it was worth it |
| branch | **ವೈರಾಗ್ಯ** | *vairāgya* | detachment |
| leaf | **ಉದಾಸೀನ** | *udāsīna* | equanimity, or the cold shoulder |
| leaf | **ನಿರ್ಲಿಪ್ತ** | *nirlipta* | unsmeared |
| branch | **ಮೌನ** | *mauna* | silence |
| leaf | **ಏಕಾಂತ** | *ēkānta* | solitude, chosen |
| leaf | **ತಂಪು** | *tampu* | coolness |

<details><summary>Reading</summary>

- **ಶಾಂತ** *(repose)* — The ninth rasa, added late and argued over for centuries — can the absence of agitation be a flavour? The English wheel files peace under happiness; the rasa tradition insists it is a state of its own.
- **ನೆಮ್ಮದಿ** *(peace of mind)* — Sharply distinct from ಶಾಂತಿ, which is peace as the absence of conflict. You can have ಶಾಂತಿ in a house with no ನೆಮ್ಮದಿ in it.  
  also said: **ಶಾಂತಿ** *śānti*, peace, as the absence of conflict, **ಸಮಾಧಾನ** *samādhāna*, being consoled, **ನಿರಾಳ** *nirāḷa*, unclenched
- **ನಿರಾಳ** *(unclenched)* — The breath after the weight comes off. Freedom as a bodily state, not a political one.
- **ಸಮಾಧಾನ** *(being consoled)* — Both the comfort someone gives and the state it produces.  
  also said: **ಸಂತೈಕೆ** *santaike*, consoling, **ನೆಮ್ಮದಿ** *nemmadi*, peace of mind, **ತಣ್ಣಗಾಗು** *taṇṇagāgu*, to cool down
- **ತೃಪ್ತಿ** *(satiety)* — The feeling after a meal, and after a life. Kannada uses the same word without irony.  
  also said: **ಸಂತೃಪ್ತಿ** *santṛpti*, full satisfaction, **ತಣಿವು** *taṇivu*, slaked, **ಸಮಾಧಾನ** *samādhāna*, settledness
- **ತಣಿವು** *(slaked)* — Satisfaction as cooling rather than filling — the other half of how Kannada thinks about want.
- **ಸಾರ್ಥಕ** *(it was worth it)* — 'Having meaning.' The feeling, where ಯಶಸ್ವಿ is only the outcome.
- **ವೈರಾಗ್ಯ** *(detachment)* — Ordinary speech in Kannada, not only monastic — said of anyone who has stopped wanting a thing they used to want.
- **ಉದಾಸೀನ** *(equanimity, or the cold shoulder)* — In philosophy the sage's evenness. In an argument, the coldest insult available. Same word.
- **ನಿರ್ಲಿಪ್ತ** *(unsmeared)* — Literally not stuck to anything — the lotus-leaf image, worn down into an ordinary adjective.
- **ಮೌನ** *(silence)* — Treated as an action, not an absence. ಮೌನ ವಹಿಸು — to take up silence — is something you do to someone.
- **ಏಕಾಂತ** *(solitude, chosen)* — The good kind of alone. Kannada draws the line English blurs: ಒಂಟಿತನ hurts, ಏಕಾಂತ is sought.
- **ತಂಪು** *(coolness)* — Native, and the whole thermal vocabulary in one word — the opposite pole from ಸಿಟ್ಟು, ಕಿಚ್ಚು, ಬಿಸಿ and ಉರಿ.

</details>

## Appendix — words with nowhere to sit

Feelings Kannada names precisely and English can only paraphrase. Most of these now live inside ಒಡಲ ಚಕ್ರ or ರಸಚಕ್ರ; they are listed together here because the list is the argument for redrawing a wheel rather than translating one.

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

## Files

| path | what's in it |
|---|---|
| [`index.html`](index.html) | the whole site — one file, three wheels, no runtime dependencies |
| [`data/wheels/bhava.json`](data/wheels/bhava.json) | wheel one. Every node has `kn`, `tr`, `en`, `status`, `rala[]` and usually `note` |
| [`data/wheels/odalu.json`](data/wheels/odalu.json) | wheel two, the body. Adds `lit`, the literal reading of each phrase |
| [`data/wheels/rasa.json`](data/wheels/rasa.json) | wheel three. Cores carry `sthayi`, the durable feeling under each rasa |
| | Any node may carry `also[]` — synonyms in the same sense that did not fit on the wheel, each with `kn`, `tr`, `en` |
| [`data/words.csv`](data/words.csv) | all three wheels flattened into one table |
| [`data/native.json`](data/native.json) | the untranslatables appendix — `kn`, `tr`, `gloss` |
| [`data/rala-responses.json`](data/rala-responses.json) | raw API responses keyed by query — provenance for every claim above |
| [`scripts/rala.py`](scripts/rala.py) | rala client and the morphological expander |
| [`scripts/build.py`](scripts/build.py) | regenerates `index.html`, this README and `words.csv` |
| [`src/wheel.js`](src/wheel.js) | the sunburst renderer, shared by all three wheels |

```bash
python3 scripts/build.py                    # rebuild site + README
python3 scripts/rala.py loneliness annoyed  # try the expander
```

### One rendering note

Do not use SVG `<textPath>` for Kannada. It positions each glyph separately along the path, which shatters an akshara into base, vowel sign and ottakshara, each rotated on its own — ಅಸಹ್ಯ came out as three unrelated pieces. Core labels here are horizontal and never rotated; the outer rings rotate the whole string as one unit, which is safe.

## Attribution

- Word data checked against [**rala**](https://github.com/pvnkmrksk/rala), a reversal of [**Alar**](https://alar.ink) by V. Krishna, licensed [ODC-ODbL](https://opendatacommons.org/licenses/odbl/), combined with [Padakanaja](https://padakanaja.karnataka.gov.in/dictionary), Government of Karnataka.
- ಭಾವಚಕ್ರ's structure follows Gloria Willcox's Feeling Wheel (1982) and its widely circulated three-ring descendant. ಒಡಲ ಚಕ್ರ and ರಸಚಕ್ರ are not translations of anything.
- Derived data in `data/` is offered under ODbL, matching Alar. Code and page are MIT.

