# Problem

- Year/Venue: 2025 / CVPR
- Category: 3D Generative Modeling and Diffusion
- Tags: 3D reconstruction, Diffusion, Generation, 3D Vision
- Paper link: ./2025/CVPR/2025_CVPR_Light-Transport-aware-Diffusion-Posterior-Sampling-for-Sin/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- However, this problem is ill-posed and, in general, requires additional views to constrain the object parameters and infer plausible reconstructions of unseen parts.
- In such scenarios, the problem becomes so ill-posed that it requires dozens, if not hundreds, of different views to adequately constrain the object parameters .
- The challenge increases significantly when these parameters describe complex distributions of volumetric materials, such as clouds, smoke, or fire.

## 해결하려는 문제
- We model the unknown distribution of volumetric fields using an unconditional diffusion model trained on a novel benchmark dataset comprising 1,000 synthetically simulated volumetric density fields.
- Through various experiments, we demonstrate single-view reconstruction of volumetric clouds at a previously unattainable quality.
- We introduce a single-view reconstruction technique of volumetric fields in which multiple light scattering effects are omnipresent, such as in clouds.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
