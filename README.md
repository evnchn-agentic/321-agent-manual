# James Clear's 3-2-1, read as an AI-agent operating manual ⛏️

> **James Clear has spent 7 years writing an agent operating manual without knowing it.**

James Clear's [3-2-1 newsletter](https://jamesclear.com/3-2-1) is written for humans trying to
live and work better. This project mined **all 361 issues** and read them back as something their
author never intended: a coherent, battle-tested **operating manual for autonomous AI agents**.

The advice a self-improvement writer gives a person — keep your actions reversible, prefer autonomy
to permission-seeking, treat failure as information, verify against reality instead of your own
model of it, seek dissent, curate ruthlessly — turns out to be almost exactly the advice you'd
write for an agent you're about to let run unsupervised. Read `index.html` and see how little
translation the lines actually need.

## What's here

- **`index.html`** — a single self-contained page. `★ The 15 best single lines`, then **12 themes**
  distilled from ~350 relevant hits across the archive, each backed by direct quotes from the
  newsletter with their issue dates.

## Method

- **Coverage:** every one of the 361 issues was read (batched; each batch reported full 361/361
  coverage with none missed). ~350 relevant lines were deduped into the 12 themes; only the
  strongest few per theme are shown.
- **Fact-checking:** the **40 quotes** shown were **individually fact-checked against primary
  sources**. Most trace to a documented primary work (McEwan's *Amsterdam*, PKD's *Flow My Tears*,
  Naval's *Almanack*, Meyer's 2010 TED talk, Quine & Ullian's *Web of Belief*, Jobs at WWDC 1997,
  Meadows' *Thinking in Systems*, Rubin's *Better Than Before*, and others). **Honest exceptions are
  flagged inline where they appear** — e.g. "Don't explain your philosophy. Embody it." is a modern
  distillation of Epictetus (*Enchiridion* 46), not a verbatim quote; "Simplify, then add lightness"
  and "ask forgiveness than permission" are folklore their named figures popularized rather than
  coined. See the footer of `index.html` for the full exceptions list.
- **Quote text vs. the cited issue (2026-10-31):** a second pass checked every quoted line against
  the text of the issue it cites. 22 lines were reworded or carried the wrong date (one cited an
  issue that does not exist), and now use the issue's own words. Re-run with
  `python3 check_quotes.py` (fetches the cited issues; exits 1 on any miss).
- **Sources:** the full text of any issue lives at its dated URL, e.g.
  <https://jamesclear.com/3-2-1/february-1-2024>.

## From reading to shipping — the loop closed

This wasn't just an essay. Mining the archive against how autonomous AI agents *actually* operate
fed concrete changes back into open Claude Code skills:

- **A review's default closing move** is now a question built on Adam Grant's *"I ask for a 0-10
  score. … Then I ask how I can get closer to a 10."* (from the 2021-03-25 issue) — merged into the **calibrated-critique**
  skill: <https://github.com/evnchn-agentic/calibrated-critique/pull/1>
- **A two-word verification pre-flight**, *"Is that assumed or confirmed?"* (Jeanne Torre, via the
  2024-03-28 issue), was added to the **seeing-is-believing** skill:
  <https://github.com/evnchn-agentic/chengyu-skills/pull/16>
- **A process lesson from building this page:** the ~40 quotes here were fact-checked against
  primary sources by a dedicated adversarial pass, and **~20% were provably wrong as first
  extracted** (apocryphal, mis-credited, or paraphrase-as-verbatim) — and **none** were caught by
  the model that pulled them. That's now a standing rule: **never publish LLM-extracted quotes
  without a fresh fact-check pass.** (It's why the caveat fold on the page lists its exceptions
  honestly.)

## Viewing

`index.html` is self-contained — clone and open it locally, or once this repo is public, view it
rendered without cloning via htmlpreview:

```
https://htmlpreview.github.io/?https://github.com/evnchn-agentic/321-agent-manual/blob/main/index.html
```

> Note: htmlpreview only works on **public** repos. While this repo is private, open `index.html`
> from a local clone instead.

---

*3-2-1 newsletter content © James Clear. This project is an independent analytical reading, not
affiliated with or endorsed by James Clear.*
