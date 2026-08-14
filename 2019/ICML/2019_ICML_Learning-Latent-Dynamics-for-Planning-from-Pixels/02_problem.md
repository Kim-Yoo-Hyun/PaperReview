# Problem

- Year/Venue: 2019 / ICML
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, Planning, latent dynamics
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://planetrl.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- Introduction Planning is a natural and powerful approach to decision making problems with known dynamics, such as game playing and simulated robot control (Tassa et al., 2012; Silver ...
- Key difficulties include model inaccuracies, accumulating errors of multi-step predictions, failure to capture multiple possible futures, and overconfident predictions outside of the training distribution.
- However, learning dynamics models that are accurate enough for planning has been a long-standing challenge, especially in image-based domains.

## 해결하려는 문제
- Key difficulties include model inaccuracies, accumulating errors of multi-step predictions, failure to capture multiple possible futures, and overconfident predictions outside of the training distribution.
- We propose the Deep Planning Network (PlaNet), a purely model-based agent that learns the environment dynamics from images and chooses actions through fast online planning in latent space.
- Moreover, we propose a multi-step variational inference objective that we name latent overshooting.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
