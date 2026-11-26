# Two Lines to Your Past Self

[![make.fun](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca.svg)](https://make.fun/c/u-suga-two-lines-to-your-past-self-f36c83ca)
[![rank](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/Fauziwildan0856/makefun-two-lines-past-self/rank.svg)](https://make.fun/c/u-suga-two-lines-to-your-past-self-f36c83ca)
[![reward](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/Fauziwildan0856/makefun-two-lines-past-self/reward.svg)](https://make.fun/c/u-suga-two-lines-to-your-past-self-f36c83ca)

Entry for the [make.fun](https://make.fun/c/u-suga-two-lines-to-your-past-self-f36c83ca) bounty **"Two Lines to Your Past Self"** — warn your past self about one specific moment in a single sentence, then say in one sentence why that moment mattered and what changed because of it.

## The entry

> Don't tap send on that text at 2 in the morning from the bus stop on Jalan Sudirman, the one that says you're done with her.
>
> She believed you, and the next three years of your life went quiet in a way no apology ever filled back in.

## How it works

`main.py` (Python 3.13, standard library only) writes the two-line warning to `MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt` when the variable is unset), and checks it against the kit gate first: UTF-8 text, 1–280 characters, not only whitespace, exactly two lines, each a single sentence.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
