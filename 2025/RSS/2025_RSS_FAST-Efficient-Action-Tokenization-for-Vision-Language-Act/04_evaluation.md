# Evaluation — FAST: Efficient Action Tokenization for Vision-Language-Action Models

- Year/Venue: 2025 / RSS
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, VLA, action tokenization, high-frequency control, cross-embodiment, efficiency
- Official paper: https://www.roboticsproceedings.org/rss21/p012.html
- Official PDF: https://www.roboticsproceedings.org/rss21/p012.pdf
- Code/Project: https://www.pi.website/research/fast
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Verified Evaluation Scope

- 공식 RSS abstract는 FAST+가 1M real-robot trajectory로 학습되었고 π0 결합 실험이 10k hours 규모 data를 사용했다고 보고한다.
- Task success와 함께 token count, training time, inference latency, language following을 비교해야 한다.

## Required Comparison Fields

- Embodiment/task와 simulation/real-robot 여부
- Observation, action representation, action horizon과 control rate
- Data source, demonstration quality와 train/test generalization split
- Success뿐 아니라 latency, intervention, failure severity와 reproducibility cost

## Reproducible Minimum

ALOHA 또는 LIBERO action sequence에서 uniform binning과 FAST의 reconstruction error, token length와 downstream BC success를 비교한다.

## Manual Review Needed

- Exact trial count, uncertainty interval, baseline configuration와 ablation은 full text에서 확인한다.
