# FlashSAC: Fast and Stable Off-Policy Reinforcement Learning for High-Dimensional Robot Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 표시한 평가 항목을 확인했다.
> Source audit: 2026-11-24 원문 대조.

## Evaluation in One Sentence

Unitree G1의 실물 계단 오르기에서 인용하는 4시간은 FlashSAC의 시뮬레이션 학습 시간이다. 그림 6은 비슷한 계단 등반 능력에 도달한 PPO의 약 20시간과 비교한다. [PDF 5쪽](https://roboticsproceedings.org/rss22/p099.pdf#page=5) · [PDF 7쪽](https://roboticsproceedings.org/rss22/p099.pdf#page=7)

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT AND SIMULATION`.

## Dataset / Benchmark Role

29자유도 G1의 비시각 보행을 위해 계단·격자·파형·구덩이 지형에서 학습했다. [PDF 7쪽](https://roboticsproceedings.org/rss22/p099.pdf#page=7)

## Baselines and Fairness

계단 등반의 실물 전이 비교 대상은 PPO다. [PDF 7쪽](https://roboticsproceedings.org/rss22/p099.pdf#page=7)

## Proposed Evaluation — Researcher Interpretation

하나의 조작 환경에서 replay coverage와 norm 제한을 분리하고 sample·wall-clock 비용을 함께 비교한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p099.html) · [저자 project/code](https://github.com/Holiday-Robot/FlashSAC).
