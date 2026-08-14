# Evaluation — π0: A Vision-Language-Action Flow Model for General Robot Control

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2025 / RSS
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, VLA, Flow Matching, generalist policy, cross-embodiment, dexterous manipulation
- Official paper: https://www.roboticsproceedings.org/rss21/p010.html
- Official PDF: https://www.roboticsproceedings.org/rss21/p010.pdf
- Code/Project: https://www.pi.website/research/pi0
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Verified Evaluation Scope

- 공식 RSS abstract는 laundry folding, table cleaning, box assembly 등 다양한 dexterous task와 여러 robot platform을 보고한다.
- Direct prompting, language following과 new-skill fine-tuning을 구분해 비교해야 한다.

## Required Comparison Fields

- Embodiment/task와 simulation/real-robot 여부
- Observation, action representation, action horizon과 control rate
- Data source, demonstration quality와 train/test generalization split
- Success뿐 아니라 latency, intervention, failure severity와 reproducibility cost

## Reproducible Minimum

공개 checkpoint를 이용해 한 개 LIBERO suite 또는 단일 real-robot task에서 chunk length와 inference latency를 측정한다.

## Manual Review Needed

- Exact trial count, uncertainty interval, baseline configuration와 ablation은 full text에서 확인한다.
