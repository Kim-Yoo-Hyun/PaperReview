# Problem

- Year/Venue: 2026 / CVPR
- Category: World Models, Safety, and Recovery
- Tags: Robotics, VLA, test-time computation, value guidance, dexterous manipulation, real-time control
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://hume-vla.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- To satisfy the stringent frequency demands of robot control, FM-Steer further introduces cascaded action denoising, decoupling expensive value-guided sampling from fast action refinement.

## 해결하려는 문제
- To address this issue, we propose a cascaded action denoising mechanism that distributes the denoising computation across the original VLA and a separate Lite-Flow denoiser, a lightweight transformer ...
- In this work, we propose FM-Steer, a test-time computing framework that augments flow-based Vision-Language-Action (VLA) generalist policies with value-guided sampling and cascaded action denoising, enabling stronger control performance ...
- At test time, the policy iteratively samples multiple noisy action proposals and retains the one with the highest predicted value, yielding value-aligned, high-quality actions without retraining.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
