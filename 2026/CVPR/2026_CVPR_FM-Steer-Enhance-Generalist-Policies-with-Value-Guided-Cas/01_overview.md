# FM-Steer: Enhance Generalist Policies with Value-Guided Cascaded Denoising

- Year/Venue: 2026 / CVPR
- Category: World Models, Safety, and Recovery
- Tags: Robotics, VLA, test-time computation, value guidance, dexterous manipulation, real-time control
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://hume-vla.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- To satisfy the stringent frequency demands of robot control, FM-Steer further introduces cascaded action denoising, decoupling expensive value-guided sampling from fast action refinement.

## Core Idea
- To address this issue, we propose a cascaded action denoising mechanism that distributes the denoising computation across the original VLA and a separate Lite-Flow denoiser, a lightweight transformer ...
- In this work, we propose FM-Steer, a test-time computing framework that augments flow-based Vision-Language-Action (VLA) generalist policies with value-guided sampling and cascaded action denoising, enabling stronger control performance ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Simply applying repeated sampling at test time results in a low control frequency, which is impractical for dexterous robot control.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To address this issue, we propose a cascaded action denoising mechanism that distributes the denoising computation across the original VLA and a separate Lite-Flow denoiser, a lightweight transformer ...
- In this work, we propose FM-Steer, a test-time computing framework that augments flow-based Vision-Language-Action (VLA) generalist policies with value-guided sampling and cascaded action denoising, enabling stronger control performance ...
- At test time, the policy iteratively samples multiple noisy action proposals and retains the one with the highest predicted value, yielding value-aligned, high-quality actions without retraining.

## Abstract Cue
- Humans naturally allocate more time before acting when handling complex tasks in the physical world.
