# Method — MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2024 / ACM Transactions on Graphics
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, whole-body control, motion imitation, NVIDIA
- Official paper: https://research.nvidia.com/labs/par/maskedmimic/
- Code/Project: https://research.nvidia.com/labs/par/maskedmimic/
- Source audit: official NVIDIA project/publication page checked; architecture and benchmark details remain UNVERIFIED.

## Pipeline

motion state의 임의 부분을 mask하고 conditioned physics policy가 missing motion을 생성·추종하도록 학습한다.

## Interface

partial motion/task constraints와 humanoid state를 joint-level whole-body actions로 매핑한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
