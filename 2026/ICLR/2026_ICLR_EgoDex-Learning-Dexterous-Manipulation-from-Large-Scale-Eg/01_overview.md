# EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> Source audit: ICLR 2026 게재본 표제면에서 저자 표기를 확인했다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

- Year/Venue: 2026 / ICLR
- Authors: Ryan Hoque, Peide Huang, David J. Yoon, Mouli Sivapurapu, Jian Zhang
- Primary track: RL, IL, offline learning, and robot data
- Tags: robot-data, human-video, dexterous-manipulation, Benchmark
- Official paper: https://arxiv.org/abs/2505.11709
- Project: https://github.com/apple-aiml-research/ml-egodex
- Code: https://github.com/apple-aiml-research/ml-egodex
- Public identifiers: {"arxiv": "2505.11709", "openreview": "FFxkFMU89E"}
- 방법·평가 확인 (2026-11-25): [원문 3, 4, 6, 7, 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/07fcc6e2b89439d3ee5ab60939aaa6a0-Paper-Conference.pdf#page=3) · [다축 분류와 공개 범위](../../../work/sources/batches/core_next_10.yaml)

## Problem and Importance

EgoDex는 사람이 조작할 때의 1인칭 영상과 양손 손가락의 3차원 궤적을 동기화해 손재주가 필요한 동작을 학습하고 평가할 자료를 제공한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/07fcc6e2b89439d3ee5ab60939aaa6a0-Paper-Conference.pdf#page=1)

## Core Idea and Contribution

- Apple Vision Pro로 탁상 조작 194개 과제에서 829시간을 기록하고 영상 프레임을 손 관절 추적과 연결했다. [PDF 3쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/07fcc6e2b89439d3ee5ab60939aaa6a0-Paper-Conference.pdf#page=3) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/07fcc6e2b89439d3ee5ab60939aaa6a0-Paper-Conference.pdf#page=4)
- 영상과 과거 손 자세에서 미래 사람 손 궤적을 예측하는 과제와 오차 지표를 정의하고 여러 모방학습 모델을 같은 조건에서 비교했다. [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/07fcc6e2b89439d3ee5ab60939aaa6a0-Paper-Conference.pdf#page=6) · [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/07fcc6e2b89439d3ee5ab60939aaa6a0-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/07fcc6e2b89439d3ee5ab60939aaa6a0-Paper-Conference.pdf#page=8)

## Scope and Limits

평가 대상은 사람의 손 궤적 예측이다. 로봇의 폐루프 작업 성공률과 로봇 손으로 옮길 때의 오차는 후속 검증 항목이다. 최초 공개는 2025년, 학회 게재는 2026년이다. [저자판](https://arxiv.org/abs/2505.11709) · [ICLR 게재본](https://proceedings.iclr.cc/paper_files/paper/2026/file/07fcc6e2b89439d3ee5ab60939aaa6a0-Paper-Conference.pdf)

## Why This Paper Is Here — Researcher Interpretation

Ψ₀가 사용한 인간 시연의 출처다. 사람 손 궤적을 로봇 사전학습에 활용하는 방법을 비교할 때 읽는다.

## 공개 자료의 확인 범위

- EgoDex 손 궤적의 오프라인 평가 지표 · compute_metrics.py [배포 파일](https://raw.githubusercontent.com/apple-aiml-research/ml-egodex/718d9ebd8ec17187f72a74a08c66deea80178cb6/compute_metrics.py)
- EgoDex 궤적 배포 첫 번째 압축 묶음 · part1.zip [배포 파일](https://ml-site.cdn-apple.com/datasets/egodex/part1.zip)
