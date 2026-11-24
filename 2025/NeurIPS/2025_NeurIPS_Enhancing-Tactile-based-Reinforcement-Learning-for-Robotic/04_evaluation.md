# Enhancing Tactile-based Reinforcement Learning for Robotic Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 표시한 평가 항목을 확인했다.
> Source audit: 2026-11-24 원문 대조.

## Evaluation in One Sentence

RoTO 실험은 Isaac Lab의 세 과제로 구성된다. 10초 동안 공을 88번 튀긴 수치와 보정구를 25번 회전시킨 수치는 시뮬레이션 에이전트의 최고 기록이다. [PDF 6쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf#page=6) · [PDF 9쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf#page=9)

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / SIMULATION`.

## Dataset / Benchmark Role

희소 이진 접촉과 고유수용감각을 입력으로 사용하는 시뮬레이션 조작을 평가했다. [PDF 6쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf#page=6) · [PDF 7쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf#page=7)

## Metrics and Success Definition

학습 보상과 물리적 과제 지표를 별도로 측정했다. [PDF 7쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf#page=7) · [PDF 9쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf#page=9)

## Ablations and Sensitivity

촉각 입력과 자기지도 목표, 기억 공유 여부의 영향을 비교했다. [PDF 7쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf#page=9)

## Statistics, Efficiency, and Reproducibility

최종 비교는 학습 시드 5개를 사용했다. [PDF 6쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf#page=6)

## Proposed Evaluation — Researcher Interpretation

동일 제어기에서 contact 유무와 SSL memory 공유/분리를 교차 비교한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/bc09efb501c801ed92e181e26a885c2d-Abstract-Conference.html) · [저자 project/code](https://elle-miller.github.io/tactile_rl/) · [공식 code](https://github.com/elle-miller/roto).
