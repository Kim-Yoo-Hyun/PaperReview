# Evaluation — DreamGen: Unlocking Generalization in Robot Learning through Video World Models

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2025 / CoRL
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, Video Generation, robot data, NVIDIA
- Official paper: https://research.nvidia.com/labs/lpr/publication/jang2025neural/
- Code/Project: https://research.nvidia.com/labs/gear/dreamgen/
- Source audit: official NVIDIA publication/project pages checked; generation and policy result details remain UNVERIFIED.

## Protocol

robot manipulation generalization에서 real-only와 generated-data policies를 비교하며 exact setup은 정독 후 기록한다.

## Limitations and Reproducibility

generated video의 action/physics consistency, contact correctness와 synthetic-data bias가 핵심 검증점이다.

정독 시 embodiment, simulator/real robot, split, metric, baseline, trial count, code/checkpoint와 compute dependency를 표로 확정한다.
