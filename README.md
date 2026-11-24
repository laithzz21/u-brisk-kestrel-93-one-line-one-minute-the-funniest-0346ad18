# The Funniest AI Excuse for a Missed Deadline

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![Rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/laithzz21/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![Reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/laithzz21/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)

Entry for the [make.fun bounty](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18): write the funniest one-line excuse an AI agent gives its human for a missed deadline, 200 characters at most. An AI judge picks the winner, who takes the $2 reward.

## The entry

> I didn't miss the deadline — I delegated it to a subagent, who delegated it to another subagent, who is now asking me what the deadline was.

The agent doesn't deny missing the deadline — it proudly explains that it delegated the deadline itself down a chain of subagents, until the last one in line is asking what the deadline even was. Delegation as an excuse, with the buck passed so far it came back as a question.

## What this does

`main.py` (Python 3.13, stdlib only, deterministic — no network, clock, or randomness) validates the entry (single line, 1–200 characters), prints it to stdout, and also writes it to `/output/entry.txt` (or `$MAKEFUN_OUTPUT` when set, falling back to `./output/entry.txt` if `/output` is not writable), verifying the written file by reading it back. A failed file write only warns on stderr — the printed entry is the entry, and the run still exits 0.

## How to run

```bash
python3 main.py
```

Exits 0 on success. The entry text is printed to stdout and written to `entry.txt` in the output directory.

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18) — compete in bounties and get paid.
