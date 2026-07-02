# Problem

- Year/Venue: 2024 / RA-L
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Robotics, 3D Vision, Gaussian Splatting, semantic
- Paper link: ./2024/RA-L/2024_RA-L_GaussianGrasper-3D-Language-Gaussian-Splatting-for-Open-vo/paper.pdf
- Code/Project: https://github.com/MrSecant/GaussianGrasper
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- To tackle this challenge, some research efforts have been dedicated to the development of language-embedded implicit fields.
- NeRF) encounter limitations due to the necessity of processing a large number of input views for reconstruction, coupled with their inherent inefficiencies in inference.

## 해결하려는 문제
- Thus, we present the GaussianGrasper, which utilizes 3D Gaussian Splatting to explicitly represent the scene as a collection of Gaussian primitives.
- Through comprehensive real-world experiments, we demonstrate that GaussianGrasper enables robots to accurately query and grasp objects with language instructions, providing a new solution for language-guided manipulation tasks.
- With the reconstructed geometry of the Gaussian field, our method enables the pre-trained grasping model to generate collision-free grasp pose candidates.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
