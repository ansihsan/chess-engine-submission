# chess-engine-submission

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/ansihsan/chess-engine-submission/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/ansihsan/chess-engine-submission/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in under 4 KB of Python: alpha-beta search with quiescence, material and piece-square evaluation, move ordering and a fixed node budget. Fully deterministic. Entered for make.fun's tiny-chess-01 bounty, $500 in USDC.

## Run it

```sh
python3 main.py
```

The engine talks to the contest env at `MAKEFUN_ENV_URL`, playing each game of the gauntlet through `/game` and `/move`.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
