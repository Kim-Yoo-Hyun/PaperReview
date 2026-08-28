# Problem — MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2024 / ACM Transactions on Graphics
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, whole-body control, motion imitation, NVIDIA
- Official paper: https://research.nvidia.com/labs/par/maskedmimic/
- Code/Project: https://research.nvidia.com/labs/par/maskedmimic/
- Source audit: official NVIDIA project/publication page checked; architecture and benchmark details remain UNVERIFIED.

## Target Problem and Assumptions

full motion tracking, sparse keypoints, text/object goals 등 서로 다른 control tasks를 별도 specialist 없이 처리한다.

## Closed-Loop Position

partial motion/task constraints와 humanoid state를 joint-level whole-body actions로 매핑한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
