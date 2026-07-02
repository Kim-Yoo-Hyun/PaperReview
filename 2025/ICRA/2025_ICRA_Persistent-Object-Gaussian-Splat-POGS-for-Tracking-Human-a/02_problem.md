# Problem

- Year/Venue: 2025 / ICRA
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Robotics, Gaussian Splatting, Reinforcement Learning
- Paper link: ./2025/ICRA/2025_ICRA_Persistent-Object-Gaussian-Splat-POGS-for-Tracking-Human-a/paper.pdf
- Code/Project: not identified from venue audit
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- The challenge is greater when dealing with irregularly shaped objects for which obtaining an accurate Computer-Aided Design (CAD) model is impractical.
- Recently introduced Gaussian Splats efficiently model object geometry, but lack persistent state estimation for taskoriented manipulation.
- However, many of these approaches fail to effectively integrate geometric information across multiple object viewpoints or timesteps, and do not address the estimation or reconstruction of occluded object ...

## 해결하려는 문제
- We present Persistent Object Gaussian Splat (POGS), a system that embeds semantics, self-supervised visual features, and object grouping features into a compact representation that can be continuously updated ...
- After an initial multi-view scene capture and training phase, POGS uses a single stereo camera to integrate depth estimates along with self-supervised vision encoder features for object pose ...
- Recently introduced Gaussian Splats efficiently model object geometry, but lack persistent state estimation for taskoriented manipulation.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
