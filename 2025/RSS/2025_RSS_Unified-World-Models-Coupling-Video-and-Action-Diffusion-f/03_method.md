# Method

- Year/Venue: 2025 / RSS
- Category: World Models, Safety, and Recovery
- Tags: Robotics, VLA, world model, video diffusion, action diffusion, robot data
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://weirdlabuw.github.io/uwm/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- Specifically, a UWM integrates an action diffusion process and a video diffusion process within a unified transformer architecture, where independent diffusion timesteps govern each modality.
- In this work, we present Unified World Models (UWM), a framework that allows for leveraging both video and action data for policy learning.
- By controlling each diffusion timestep, UWM can flexibly represent a policy, a forward dynamics, an inverse dynamics, and a video generator.

## 원리적 동기
- Leveraging this data directly for imitation learning, however, has proven difficult due to the lack of action annotation.
- Specifically, a UWM integrates an action diffusion process and a video diffusion process within a unified transformer architecture, where independent diffusion timesteps govern each modality.

## 핵심 방법론
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
