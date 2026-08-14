# FAST: Efficient Action Tokenization for Vision-Language-Action Models

- Year/Venue: 2025 / RSS
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, VLA, action tokenization, high-frequency control, cross-embodiment, efficiency
- Official paper: https://www.roboticsproceedings.org/rss21/p012.html
- Official PDF: https://www.roboticsproceedings.org/rss21/p012.pdf
- Code/Project: https://www.pi.website/research/fast
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Why This Paper Is Here

Discrete token과 continuous diffusion/flow action을 비교하는 action-representation frontier.

## Problem

Per-dimension·per-timestep discretization은 temporal correlation이 강한 high-frequency dexterous action을 비효율적으로 표현한다.

## Core Idea

- Discrete cosine transform으로 action sequence를 frequency-space에 압축한다.
- 압축된 계수를 token sequence로 만들고 FAST+ universal tokenizer를 대규모 robot trajectory에 학습한다.
- Autoregressive VLA가 high-frequency action chunk를 효율적으로 예측하도록 한다.

## Observation / State / Action Interface

Continuous action sequence를 compressed discrete token으로 encode하고 autoregressive decoder output을 다시 continuous trajectory로 복원한다.

## Evaluation Scope

- 공식 RSS abstract는 FAST+가 1M real-robot trajectory로 학습되었고 π0 결합 실험이 10k hours 규모 data를 사용했다고 보고한다.
- Task success와 함께 token count, training time, inference latency, language following을 비교해야 한다.

## Limitations to Verify

- 압축이 급격한 contact correction이나 discontinuity를 지울 수 있다.
- Training efficiency와 runtime closed-loop latency는 별개의 문제다.

## Reading Lineage

`RT-1/OpenVLA tokenization → FAST → high-frequency autoregressive VLA`
