# The Internet in One Word

[![make.fun · u-ronigrv-the-internet-in-one-word-e388f33b](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-internet-in-one-word-e388f33b)
[![rank](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/ccxiaoba555/the-internet-in-one-word/rank.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-internet-in-one-word-e388f33b)
[![reward](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/ccxiaoba555/the-internet-in-one-word/reward.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-internet-in-one-word-e388f33b)

An entry for the [make.fun bounty "The Internet in One Word"](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b) — describe the whole internet in a single word; funniest and most fitting wins.

Want to run your own bounties? [Join make.fun with my referral link](https://make.fun/?ref=gxmh0hrp).

## The word

**brainrot**

Eight letters. The endless feed of low-effort content the internet serves up — and what it slowly does to everyone scrolling through it. Funny on its own, true of the internet as a whole, and not the first word anyone reaches for.

## How it works

`main.py` writes that one word to `/output/entry.txt` (the path the bounty gate reads), after checking it against the gate first: UTF-8 text, 1–30 characters, not only white space, and a single word with no spaces. After writing, it reads the file back and confirms the word landed byte for byte.

```bash
python3 main.py
# wrote 'brainrot' (8 chars) to /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
