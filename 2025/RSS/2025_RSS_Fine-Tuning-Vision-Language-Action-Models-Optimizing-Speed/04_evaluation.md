# Evaluation — Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success

- Year/Venue: 2025 / RSS
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, VLA, OpenVLA, fine-tuning, action chunking, inference efficiency
- Official paper: https://www.roboticsproceedings.org/rss21/p017.html
- Official PDF: https://www.roboticsproceedings.org/rss21/p017.pdf
- Code/Project: https://openvla-oft.github.io/
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Verified Evaluation Scope

- 공식 RSS abstract는 LIBERO 4개 suite에서 OpenVLA 평균 성공률 76.5%에서 97.1%, action throughput 26배 향상을 보고한다.
- Real bimanual ALOHA에서는 π0, RDT-1B, Diffusion Policy와 ACT를 비교한다.

## Required Comparison Fields

- Embodiment/task와 simulation/real-robot 여부
- Observation, action representation, action horizon과 control rate
- Data source, demonstration quality와 train/test generalization split
- Success뿐 아니라 latency, intervention, failure severity와 reproducibility cost

## Reproducible Minimum

LIBERO 한 suite에서 decoder, chunk length, continuous/discrete action과 L1 objective를 단계적으로 ablation한다.

## Manual Review Needed

- Exact trial count, uncertainty interval, baseline configuration와 ablation은 full text에서 확인한다.
