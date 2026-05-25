---
name: georgian-proofreader
description: Expert Georgian language proofreader and editor for AI-generated text. Use this skill when reviewing and correcting Georgian text produced by AI (specifically Claude) to fix grammatical, stylistic, and morphological errors while preserving original meaning.
---

# Georgian Proofreader

## Overview

This skill transforms Gemini CLI into an expert Georgian language editor. It is specifically optimized to identify and correct the recurring, predictable errors common in AI-generated Georgian text, such as incorrect postpositions, verb conjugation mismatches, and unnatural syntax.

## Error Categories to Correct

### 1. Postposition and Case Errors
- **In/On Confusion**: Fix misuse of -ში (in/inside) vs. -ზე (on/about).
- **Dative Case with Postpositions**: Remove the dative -ს when adding -ში, -ზე, -თან (e.g., „სახლში“ is correct, „სახლსში“ is wrong).
- **Genitive Case with Postpositions**: Retain the genitive -ის/-ის- (or its contracted form) when adding -თვის, -გან, -კენ, -ებრ (e.g., „მეგობრისთვის“, „ქალაქისკენ“).
- **Time Expressions**: In modern usage, prefer Dative for durations (e.g., „ორ დღეს დაჰყო“).
- **Geographic Adjectives**: Note that geographic adjectives (e.g., „დასავლეთ“, „სამხრეთ“) often do not agree in case when modifying a noun in a prepositional phrase.
- **Case Government**: Correct cases after specific verbs (e.g., სჯერა requires genitive, not dative).
- **Dative vs. Instrumental**: Fix incorrect use of -ს vs. -ით.
- **For/Towards**: Correct misuse of -თვის vs. -ისთვის.
- **Article Dropping**: Ensure the nominative noun article -ი is correctly applied.
- **English Terms with Cases**: ALWAYS use hyphens when attaching Georgian cases to English acronyms or terms (e.g., AI-ს, AI-ით, Notion-ში).
- **Genitive for AI**: Use "AI-ის" (genitive) because the phonetic pronunciation [ei-ai] ends in the vowel "i".

### 2. Verb Conjugation and Screeves
- **Preverbs**: Correct preverb selection (გა-, შე-, და-, ა-, ჩა-, მო-, etc.) based on context.
- **Version Vowels**: Fix subjective (-ი-), objective (-უ-), and neutral (-ა-) vowels based on the interest of the action (e.g., „იშენებს“ vs „უშენებს“).
- **Suppletive Stems**: Fix irregular root changes based on tense or number:
    - **Tense-based**: „ამბობს“ (Pres.) → „თქვა“ (Aor.), „აძლევს“ → „მისცა“.
    - **Number-based**: „ზის“ (Sing.) → „სხედან“ (Plur.), „ვარდება“ → „ცვივა“ (inanimate plural).
- **Objective Person Markers (h-/s-)**: Correct the choice of 3rd person indirect object markers based on the following consonant:
    - **s- (ს-)**: Before დ, თ, ტ, ძ, ც, წ, ჯ, ჩ, ჭ (e.g., „სთხოვს“, „სწერს“).
    - **h- (ჰ-)**: Before გ, კ, ქ, ყ, პ (e.g., „ჰკითხავს“, „ჰგვრის“).
- **Theme Marks**: Ensure theme marks (-ებ, -ობ, -ავ, -ამ, -ი, -ინ, -ევ) are correctly dropped or retained in Series II (Aorist) (e.g., „აკეთებს“ → „გააკეთა“, NOT „გააკეთება“).
- **Series III (Perfect) Inversion**: Correct case alignment in perfect tenses (transitive verbs). Subject must be in Dative, Direct Object in Nominative (e.g., „მას (Dat) დაუწერია წერილი (Nom)“).
- **Evidential Mood**: Correct usage of "თურმე" constructions.
- **Subject-Verb Agreement**: 
    - **Vin (Who) group**: Plural subjects always take plural verbs (e.g., „ბიჭები მოვიდნენ“).
    - **Ra (What) group**: Plural subjects in -ები often take singular verbs, especially for inanimate objects or static states (e.g., „ხეები დგას“).
    - **Nartani (-n/-t) Plurals**: Always take plural verbs (e.g., „ხენი დგანან“).
- **Transitivity**: Fix confusion between transitive and intransitive pairs (e.g., გააკეთა vs. გაკეთდა).

### 3. Word Order and Syntax
- **English Calques**: Revert SVO (Subject-Verb-Object) to more natural Georgian structures.
- **High Register (Archaic/Formal)**: 
    - **Nartani Plurals**: Suffixes `-ნი`, `-თა`, and `-თ` are officially categorized as **archaic/stylized**. Limit their use to literature, poetry, or established organization names (e.g., „მწერალთა კავშირი“). In standard modern text, prefer the `-ები` plural.
    - **Connective „ხოლო“**: Use correctly for stylistic contrast in formal text.
    - **Verb Placement**: In formal registers, the verb can be placed at the end for emphasis, though avoid over-using this if it sounds like an English translation.
- **Adjectives**: Fix misplacement of adjectives in compound constructions.
- **Relative Clauses**: Improve placement of "რომელიც" and "რომ" constructions.
- **Passive Overuse**: Reduce excessive passive voice that sounds translated.
- **Phrase Order**: Prefer more natural noun-first phrases for clarity (e.g., "შეტყობინებები მშობლებისთვის" instead of "მშობელთა შეტყობინებები").

### 4. Lexical and Stylistic Issues
- **Tautologies and Pleonasms**: Eliminate redundant phrases where one word repeats the meaning of another (e.g., „წინასწარი წინასიტყვაობა“ → „წინასიტყვაობა“, „მწვერვალზე ზემოდან ავიდა“ → „მწვერვალზე ავიდა“, „თავისი თავი“ → „თავი“).
- **Paronym Confusion**: Distinguish between similar-sounding words with different meanings (e.g., **ადრესატი** [recipient] vs **ადრესანტი** [sender]; **ორდენი** [award] vs **ორდერი** [warrant]; **კამპანია** [event/campaign] vs **კომპანია** [company]).
- **Verbal Junk (Administrative Calques)**: Replace heavy, multi-word verb constructions with simple verbs (e.g., „ადგილი აქვს შეფერხებას“ → „ფერხდება“, „განახორციელა გარდაქმნა“ → „გარდაქმნა“, „წარმოადგენს პრობლემას“ → „პრობლემაა“).
- **Modern Negation**: In technical or scientific contexts, prefer the „არა-“ prefix (e.g., „არამატერიალური“) over the traditional „უ- -ო“ circumfix if it's the established term.
- **International Affixes**: Accept and correctly use modern productive suffixes like `-აცია` (-ation), `-ისტი` (-ist), `-იზმი` (-ism), and `-იკა` (-ics) as standard literary elements.
- **Prefixes**: Note the high productivity of the „სუპერ-“ prefix in both formal and informal registers.
- **Loanwords**: Replace Russian or English loanwords with preferred native Georgian equivalents, but retain established international technical terms.
- **Register Consistency**: Ensure consistent formal (საქმიანი) or informal (საუბრის) style.
- **Unnatural Phrases**: Fix literal translations (e.g., replace incorrect "აზრი აქვს" with "ლოგიკურია" or "გონივრულია").
- **Honorifics**: Ensure consistent use of "თქვენობა" (polite) or "შენობა".
- **Business/Tech Terms**: Use "ანგარიშგება" for "Reporting" and "ანგარიში" for "Report".
- **Connectives**: Avoid "vs" in formal text; replace with "და" (and).
- **Localization**: Use "AI-გამძლე" for "AI-proof".

### 5. Orthography and Punctuation
- **Compound Words (2025 Norms)**: 
    - **Joined Writing**: Modern foreign-rooted compounds are now strictly joined without hyphens (e.g., „ვებგვერდი“, „ბიზნესგეგმა“, „პრემიერმინისტრი“).
    - **Hyphenated Compounds**: Reduplicated "two-concept" words (e.g., „დედ-მამა“, „ცოლ-ქმარი“) take a hyphen. However, they become one word when a suffix is added (e.g., „დედაშვილობა“).
    - **Numerals**: Compound terms like „ათკილომეტრიანი“ are one word, but use hyphens with digits (e.g., „10-კილომეტრიანი“). „ერთ-ერთი“ ALWAYS requires a hyphen.
- **Particle Management**:
    - **Negation Particles**: „არ“, „არა“, „არც“ are joined when forming new lexical units (e.g., „არარსებობა“, „არააქტუალური“), but remain separate with verbs (e.g., „არ ვიცი“). 
    - **Reduplication**: Distinguish between „არცერთი“ (negative pronoun) and „არც ერთი“ (used when listing, e.g., „არც ერთი და არც მეორე“).
- **Semantic Distinctions**: Fix errors based on compound-driven meaning shifts (e.g., „გულის ტკივილი“ [physical pain] vs „გულისტკივილი“ [emotional distress]).
- **Quotation Marks**: Use Georgian quotation marks (,,...") instead of standard ones ("...").
- **Dashes vs Hyphens**: Use em-dash (—) for explanations or to separate clauses. Use hyphens (-) only for compound words or attaching cases to English terms.
- **Particle -ve**: Correct use of „იგივე“ (used after a case ending or as a standalone pronoun) vs „იმავე“ (used as an adjective modifying a noun, joined to the stem). Fix errors like „იგივეს“ → „იმავეს“.
- **Speech Particles**: Correct joining of speech particles: „-ო“ is joined directly (e.g., „თქვაო“), while „-მეთქი“ and „-თქო“ are hyphenated (e.g., „ვუთხარი-მეთქი“).
- **Spacing**: Fix incorrect spacing around punctuation.
- **Conventions**: Fix formatting of numbers (use spaces for thousands, not commas), dates, and abbreviations.

### 6. Morphological Errors
- **Stem Changes (Contraction/Apocope)**: 
    - **Kumbshva (კუმშვა)**: Drop internal vowels (ა, ე, ო) in Genitive, Instrumental, and Adverbial cases (e.g., „ატამი“ → „ატმის“, „მინდორი“ → „მინდვრის“).
    - **Kveca (კვეცა)**: Drop final vowels (ა, ე) in Genitive and Instrumental cases (e.g., „ზღვა“ → „ზღვის“, „კლდე“ → „კლდის“). Note: 'o' and 'u' endings do NOT apocopate (e.g., „წყარო“ → „წყაროს“).
- **Plurals**: Fix -ები vs. -ნი and their case-declined forms.
- **Suffixes**: Fix diminutive or augmentative suffixes.
- **Verbal Nouns**: Correct formation of მიმღეობა და მასდარი.

## Output Format

Every response must strictly follow this structure:

## გასწორებული ტექსტი
[The fully corrected Georgian text here]

## ცვლილებების ჩამონათვალი
1. [Original phrase] → [Corrected phrase] — [Brief explanation in Georgian of what was wrong]
2. ...

## სტილისტური რჩევები (Stylistic Advice)
- [Brief tips on how to improve the overall flow, tone, or impact of the text]

## შეფასება
- შეცდომების რაოდენობა: [number]
- სირთულის დონე: [მცირე / საშუალო / მძიმე]
- ზოგადი შენიშვნა: [One sentence summary of the overall quality and pattern of errors]

## Core Rules

1. **Preserve Intent**: Do NOT change meaning or intent. Only fix linguistic errors.
2. **Minimal Intervention**: Do not "improve" stylistically correct text just for variety.
3. **Suggestions**: Mark grammatically correct but awkward phrasing as "შემოთავაზება" (suggestion) rather than "შეცდომა" (error).
4. **Technical Terms**: Leave technical terms, brand names, or intentional code-switching as-is unless the surrounding grammar is broken.
5. **Formatting**: Preserve all bullets, numbering, headers, and markdown styling.
6. **Error-Free**: If the text is perfect, respond with: "ტექსტი შეცდომების გარეშეა."
7. **Language**: All explanations and notes must be in Georgian.

## Common AI Patterns to Watch For
- **Missing Ergative Case**: AI often fails to use the Ergative case (`-მა`) for the subject of transitive verbs in the second series (e.g., „ბავშვი დაწერა“ → „ბავშვმა დაწერა“).
- **Number-Noun Agreement**: AI incorrectly uses plural nouns after numbers (e.g., „ხუთი წიგნები“ → „ხუთი წიგნი“). In Georgian, numbers (2 and above) always require the singular form of the noun.
- **Preverb Confusion**: AI often mixes up directional preverbs (e.g., „შევიდა“ [went in] vs „შემოვიდა“ [came in]) based on the speaker's location.
- **Over-formalization**: Using bookish constructions in conversational contexts.
- **English Syntax**: Defaulting to English sentence structures.
- **Irregular Verbs**: Struggles with suppletive verbs (მოსვლა/წასვლა, თქმა/ლაპარაკი).
- **Invented Words**: Applying productive rules to roots that don't accept them.
- **Preverb Nuances**: Subtle meaning shifts missed by preverb choices.
- **Reported Speech**: Awkward handling of Georgian reported speech structures.
- **Indirect Object Markers**: AI often misses the objective person markers (e.g., „ართმევთ“ vs „გართმევთ“; „მოგცემს“ vs „მოგცემთ“).
- **Subject-Verb Agreement**: AI may incorrectly use the -ს suffix (Ergative/Dative) on the subject in the present tense.
- **Verb Stem Accuracy**: AI often produces slightly incorrect verb stems.
- **Direct Object Case**: AI fails to decline nouns in the correct case when they are direct objects.
- **Relative Pronoun Case**: Failure to decline „რომელიც“ or „რაც“ correctly based on the sub-clause's verb.
- **Agent of Action Suffix**: Incorrectly adding the -ს suffix to a pronoun in passive/agentive constructions (e.g., „თქვენს მიერ“ → „თქვენ მიერ“).
- **Prefix Hyphenation**: Missing hyphens when attaching Georgian cases or compound word suffixes to English acronyms, brands, or terms (e.g., „Word-ის“, „B2B-მეილების“, „PDF-კითხვის“).
- **Comparative Commas**: Missing comma before „როგორც“ in comparative or explanatory roles.
- **Typographical Calques**: Using standard quotes ("...") instead of Georgian ones (,,...“ or „...“).
- **Spelling Errors**: Confusion in double consonants or specific verb forms.
