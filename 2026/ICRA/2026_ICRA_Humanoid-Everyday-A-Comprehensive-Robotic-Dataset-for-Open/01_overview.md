# Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> Source audit: 2025년 arXiv 공개 후 ICRA 2026에 게재됐다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다. [IEEE DOI 서지](https://doi.org/10.1109/ICRA57385.2026.11696267)

- Year/Venue: 2026 / ICRA
- Authors: Zhenyu Zhao, Hongyi Jing, Xiawei Liu, Jiageng Mao, Abha Jha, Hanwen Yang, Rong Xue, Sergey Zakharov, Vitor Guizilini, Yue Wang
- Primary track: RL, IL, offline learning, and robot data
- Tags: robot-data, humanoid, loco-manipulation, multimodal, Benchmark
- Official paper: https://arxiv.org/abs/2510.08807
- Venue verification: https://api.crossref.org/works/10.1109/icra57385.2026.11696267
- Project: https://humanoideveryday.github.io/
- Code: https://github.com/physical-superintelligence-lab/Humanoid-Everyday
- Public identifiers: {"arxiv": "2510.08807", "doi": "10.1109/icra57385.2026.11696267"}
- 방법·평가 확인 (2026-11-25): [원문 4, 5, 6쪽](https://arxiv.org/pdf/2510.08807v3#page=4) · [다축 분류와 공개 범위](../../../work/sources/batches/core_next_10.yaml)

## Problem and Importance

Humanoid Everyday는 전신 이동을 동반한 조작과 사람과의 상호작용을 포함한 휴머노이드 시연 데이터셋과 정책 평가 절차를 제시한다. [PDF 1쪽](https://arxiv.org/pdf/2510.08807v3#page=1)

## Core Idea and Contribution

- G1과 H1 원격조작으로 260개 과제의 궤적 약 1만 300개를 수집하고, 로봇별 센서 관측·행동 기록에 언어 주석을 연결했다. [PDF 4쪽](https://arxiv.org/pdf/2510.08807v3#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2510.08807v3#page=5)
- 데이터셋에서 고른 일곱 과제에 대해 정책별·과제별 열 번씩 실행해 모방 정책들의 성공률을 비교하고, 이동 조작과 정밀 삽입의 실패를 수량화했다. [PDF 6쪽](https://arxiv.org/pdf/2510.08807v3#page=6)

## Scope and Limits

260개 과제는 시연 수집 범위다. 논문의 정책 평가는 일곱 과제에 한정된다. Ψ₀에서 사용한 31시간은 별도 하위 집합이다. [자료 수집](https://arxiv.org/pdf/2510.08807v3#page=5) · [정책 평가, 표 II](https://arxiv.org/pdf/2510.08807v3#page=6) · [Ψ₀ 원문](https://www.roboticsproceedings.org/rss22/p021.html)

## Why This Paper Is Here — Researcher Interpretation

Ψ₀의 휴머노이드 사전학습 자료 가운데 실제 G1·H1의 관측과 행동이 어떤 형태로 기록됐는지 비교할 때 읽는다.

## 공개 자료의 확인 범위

- 휴머노이드 평가 서버와 관측·명령을 교환하는 클라이언트 · humanoid_everyday/core.py [배포 파일](https://raw.githubusercontent.com/physical-superintelligence-lab/Humanoid-Everyday/7c427fdb01a919dfd1b0697353e41b689a0f7e26/humanoid_everyday/core.py)
- Humanoid Everyday의 LeRobot 형식 궤적 · data/chunk-000/episode_000000.parquet [배포 파일](https://huggingface.co/datasets/USC-GVL/humanoid-everyday/resolve/71f6210e91c2a7e8b8e4d47db0147444a1a0640e/data/chunk-000/episode_000000.parquet)
