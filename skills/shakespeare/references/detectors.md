# What AI detectors measure

Read this when the user asks about AI-detector scores, says a detector flagged their text, or wants text that "won't be flagged." Source codes refer to [research-basis.md](research-basis.md); D-codes are the detector studies.

## The short version

The leading commercial detectors no longer rely on word lists or sentence-length variation. Pangram, GPTZero, Turnitin and Originality all use trained transformer classifiers (D11, D14, D15, D18). They are trained on human documents paired with AI "mirror" texts on the same topic, length and style, so they learn how a text was produced rather than what it says (D14). They are now also trained on the output of humanizer tools (D07, D11, D15, D18), and several report how much of a document was AI-written, sentence by sentence, instead of a single yes or no (D03, D11, D15).

So a detector score mostly reflects provenance: how much of the final text a model generated. Style editing changes it only a little. In one controlled study, people who hand-edited an LLM draft to sound like themselves lowered detector scores, but their text stayed much closer to LLM style than to their own writing (D05). Their edits were mostly removing em dashes and adding contractions.

This skill improves writing. It does not promise any detector result, and text that a model drafted or substantially rewrote is AI-assisted whatever its score.

## What changes a score, legitimately

These are all things that also make the writing better or more honest:

- **The author's own material.** Facts, experiences, judgments and sentences that come from the user. The more of the final text that originated with them, the more human it is, by any definition. Ask for it.
- **The author's own edits.** Substantive human editing of AI drafts lowered AI scores in about 89% of documents in one benchmark (D03), and expert editing that fixed facts, repetition, flow and formatting cut detector separability by up to 22 AUROC points, while LLM "make it human" edits did not (D04).
- **Editing in place instead of regenerating.** Grammar and spelling fixes leave almost no trace (D03, D18). Summarizing, expanding and rewriting leave a large one (D03). Even a light AI polish of human text can tip some detectors (D02), so when the user's draft is human, change only what needs changing.
- **The author's real voice.** When models imitated a specific author from a few real samples, detectors missed noticeably more of the output than with plain prompts (D16). For honest work this just means: if the user wants their voice, ask for two or three samples of their own writing and match them. Don't present this as a bypass; most such text was still caught.

## What doesn't work

- **Humanizer tools.** An audit of 19 commercial humanizers found every one made the text less coherent; humanized text beat the original on quality only 3–26% of the time, depending on the tool's tier, and the strongest detectors caught 92–99% of it (D07, D11).
- **Synonym swaps, removing stock phrases or em dashes, typos, look-alike characters.** These are now in detectors' training data (D11, D15). Plain LLM paraphrasing raised detection on some detectors (D06).
- **Iterative or detector-guided rewriting.** It can defeat current detectors (D06, D17), but it's adversarial optimization, not writing, and it degrades the text. It's out of scope for this skill.

## Where detectors are unreliable

Tell users this when a score surprises them:

- **Short text.** Turnitin needs at least 300 words; Pangram and GPTZero about 50. Under those lengths, scores are noisy both ways (D01, D11, D18).
- **Formulaic genres.** Recipes, poetry, reviews, product blurbs, landing pages, Wikipedia-style entries and manuals produce the most false positives on human text (D01, D11; RAID P20: up to 52% false positives for one detector on recipes).
- **Dense academic wording and ESL prose.** Human abstracts full of long academic words scored higher; theology abstracts were flagged far more than chemistry ones (D08). Vendors name academic and ESL writing as their known false-positive risk (D11).
- **Sentence highlights.** Word- and sentence-level attribution in mixed documents is still unreliable (D12), and Turnitin's falsely flagged sentences cluster next to real AI text (D18).
- **Weak tools.** ZeroGPT publishes no method and performed worst in independent tests (P20). One run on one tool says little; vendors' claims of 0.01% false positives are self-reported.

## How to answer the user

1. Say plainly what the score measures: how much of the text a model produced, judged against millions of known AI texts. Clean style doesn't change that much.
2. If a model wrote it, the detector is probably right, and that's not a writing flaw.
3. Offer the honest levers: their own facts and stories, their own edits, minimal-edit revision of their own drafts, writing in their voice from their samples.
4. If they wrote it themselves and it was flagged, explain the false-positive zones above. Suggest keeping drafts and version history as evidence of process.
5. Decline to add evasion tricks. They damage the text and mostly don't work against current detectors.
