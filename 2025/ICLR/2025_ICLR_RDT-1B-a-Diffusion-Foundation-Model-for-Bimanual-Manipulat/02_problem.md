# Problem

- Year/Venue: 2025 / ICLR Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, Diffusion
- Paper link: ./2025/ICLR/2025_ICLR_RDT-1B-a-Diffusion-Foundation-Model-for-Bimanual-Manipulat/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- We choose Transformer as the scalable backbone network (Bao et al., 2023; Peebles & Xie, 2023) and make the following three key modifications from Diffusion Transfomer (DiT) by ...
- To solve this problem, we add (a) Loss w/o QKN & RMSN QKNorm (Henry et al., 2020) to avoid numerical instability when calculating attention.
- Besides, we also note that our problem can 5 ' 7 Z R 0 / 3 be considered as a time series forecasting task, and the centering Z ...

## 해결하려는 문제
- To improve the approximation capability for nonlinear robot actions, we replace the final linear decoder with Figure 4: (a) Unstable loss curve a nonlinear MLP decoder as a ...
- 4a shows that large-scale pre-training tends to be 7 D V N very unstable or even explode without this modification. (b) Task w/o MLP or ACI • MLP ...
- We choose Transformer as the scalable backbone network (Bao et al., 2023; Peebles & Xie, 2023) and make the following three key modifications from Diffusion Transfomer (DiT) by ...

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
