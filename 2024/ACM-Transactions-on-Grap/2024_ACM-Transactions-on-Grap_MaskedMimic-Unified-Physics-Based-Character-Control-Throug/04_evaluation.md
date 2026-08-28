# Evaluation — MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2024 / ACM Transactions on Graphics
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, whole-body control, motion imitation, NVIDIA
- Official paper: https://research.nvidia.com/labs/par/maskedmimic/
- Code/Project: https://research.nvidia.com/labs/par/maskedmimic/
- Source audit: official NVIDIA project/publication page checked; architecture and benchmark details remain UNVERIFIED.

## Protocol

여러 conditioning modality와 large motion corpus의 physics-based control을 평가한다.

## Limitations and Reproducibility

simulation-to-real humanoid transfer, contact-rich manipulation과 actuator constraints는 추가 검증이 필요하다.

정독 시 embodiment, simulator/real robot, split, metric, baseline, trial count, code/checkpoint와 compute dependency를 표로 확정한다.
