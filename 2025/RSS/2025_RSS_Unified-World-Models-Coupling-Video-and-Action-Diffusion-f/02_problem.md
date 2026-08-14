# Problem

- Year/Venue: 2025 / RSS
- Category: World Models, Safety, and Recovery
- Tags: Robotics, VLA, world model, video diffusion, action diffusion, robot data
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://weirdlabuw.github.io/uwm/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- Leveraging this data directly for imitation learning, however, has proven difficult due to the lack of action annotation.

## 해결하려는 문제
- Through simulated and real-world experiments, we show that: (1) UWM enables effective pretraining on largescale multitask robot datasets with both dynamics and action predictions, resulting in more generalizable ...
- Specifically, a UWM integrates an action diffusion process and a video diffusion process within a unified transformer architecture, where independent diffusion timesteps govern each modality.
- However, despite showing robust and reliable behavior within the training distribution, these methods can be brittle w

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
