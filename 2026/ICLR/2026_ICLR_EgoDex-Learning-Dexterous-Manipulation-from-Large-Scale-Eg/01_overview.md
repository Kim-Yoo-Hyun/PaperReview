# EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video

> Evidence maturity: `ABSTRACT_CHECKED`.
> Source audit: 2026-11-16: 공식 초록·ICLR 목록·repository 확인. abstract 기반 — 본문 수동 확인 필요. 사용자 상태 UNREAD 유지.

- Year/Venue: 2026 / ICLR
- Primary track: RL, IL, offline learning, and robot data
- Tags: robot-data, human-video, dexterous-manipulation, Benchmark
- Official paper: https://arxiv.org/abs/2505.11709
- Project: https://github.com/apple-aiml-research/ml-egodex
- Code: https://github.com/apple-aiml-research/ml-egodex
- Public identifiers: {"arxiv": "2505.11709", "openreview": "FFxkFMU89E"}

## Why This Paper Is Here

Ψ₀의 핵심 인간 데이터 출처이며 robot data 사전학습을 이해할 NEXT다. [ICLR 2026 공식 목록](https://iclr.cc/Downloads/2026)과 [OpenReview](https://openreview.net/forum?id=FFxkFMU89E)로 게재를 확인했다. 최초 preprint는2025년이지만 registry는 게재연도2026을 사용한다.

## Problem, Contribution, and Interface

대규모 1인칭 영상과 정밀3D 손 추적을 결합해 dexterous manipulation 학습 자료를 제공한다. 입력 영상/언어에서 인간 손 궤적을 다루며 robot joint command를 직접 제공하는 정책과 구분한다. [초록](https://arxiv.org/abs/2505.11709).

## Scope and Limits

829시간·194과제. Human trajectory benchmark와 로봇 closed-loop 성공은 서로 다른 증거다. 자동 언어 label과 retargeting의 신뢰도는 downstream 연구에서 별도로 점검한다.
