# Set up Shakespeare

Shakespeare writes and revises prose so it reads like a skilled person wrote it. It keeps facts, evidence and the author's voice, and it avoids the recurring habits of LLM text. The name doesn't mean Elizabethan language. The rules come from 31 AI-text-detection papers and 17 newer studies of LLM writing style (see [research-basis.md](../skills/shakespeare/references/research-basis.md)). They don't guarantee any AI-detector score.

## Claude: upload the skill

1. Open **Customize → Skills → + → Create skill → Upload a skill**.
2. Upload `shakespeare.zip` from the [latest release](../../../releases/latest), or zip the `skills/shakespeare` folder yourself so the archive holds a single `shakespeare/` folder.
3. Enable Shakespeare and ask: "Use Shakespeare to revise this text while keeping my voice and facts."

Skills require **Code execution and file creation** to be on, and organization settings may control availability. With code execution, Claude can also run the optional checker in `scripts/pattern_check.py`. See [Claude's setup guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

The ZIP holds a single top-level folder, `shakespeare`, as Claude's packaging guide requires ([custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)).

## ChatGPT: use a Project

1. Create a ChatGPT Project named **Shakespeare**.
2. Open the project's instructions.
3. Copy all of [`chatgpt/Shakespeare-ChatGPT-Instructions.md`](../chatgpt/Shakespeare-ChatGPT-Instructions.md) into the project instructions and save. It is a condensed version of the skill, about 6,300 characters.
4. Start a chat inside that project and ask for a draft or paste text to revise.

For a single conversation, paste the instructions into your first message, followed by your request.

## ChatGPT desktop and Codex: native skill

The `skills/shakespeare` folder is a standard skill package, with optional OpenAI display metadata in `agents/openai.yaml`. Where standalone skills are available, pick it from the skill picker: `@` in ChatGPT, `$shakespeare` in Codex.

## The checker

`scripts/pattern_check.py` uses only the Python standard library. It counts surface patterns: overused vocabulary, stock phrases, "not X but Y" constructions, trailing -ing clauses, transition openers, uniform sentence and paragraph lengths, em dashes, markdown habits, announced counts and recap endings.

```
python3 skills/shakespeare/scripts/pattern_check.py draft.txt
python3 skills/shakespeare/scripts/pattern_check.py draft.txt --json
```

It points at things to look at. It isn't a detector and it doesn't score text: human writing triggers some of its flags too.

## Check the behavior

Try a short revision that contains a date, a direct quotation and an uncertain estimate. The output should keep all three, cut empty wording, and follow the tone and format you asked for. Try a terse set of notes with a requested length: the result should reach roughly that length by working through the facts, and it should put bracketed prompts where it would otherwise have to invent memories.
