# Evaluation — Flow Matching for Generative Modeling

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2023 / ICLR
- Category: Foundations: Generative Models
- Tags: Flow Matching, generative modeling, continuous normalizing flow, action generation
- Official paper: https://iclr.cc/virtual/2023/poster/11309
- Official PDF: https://openreview.net/pdf?id=PqvMRDCJT9t
- Code/Project: https://openreview.net/forum?id=PqvMRDCJT9t
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Verified Evaluation Scope

- 원 논문은 ImageNet generative modeling에서 likelihood와 sample quality를 평가한다.
- Robotics prerequisite로 읽되 robot success나 latency는 원 논문의 직접 평가 범위가 아니다.

## Required Comparison Fields

- Embodiment/task와 simulation/real-robot 여부
- Observation, action representation, action horizon과 control rate
- Data source, demonstration quality와 train/test generalization split
- Success뿐 아니라 latency, intervention, failure severity와 reproducibility cost

## Reproducible Minimum

2D toy mixture에서 diffusion path와 OT path의 vector-field regression 및 sampling step 수를 비교한다.

## Manual Review Needed

- Exact trial count, uncertainty interval, baseline configuration와 ablation은 full text에서 확인한다.
