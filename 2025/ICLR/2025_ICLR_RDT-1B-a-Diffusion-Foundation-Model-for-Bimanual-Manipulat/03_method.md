# Method

- Year/Venue: 2025 / ICLR Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, Diffusion
- Paper link: ./2025/ICLR/2025_ICLR_RDT-1B-a-Diffusion-Foundation-Model-for-Bimanual-Manipulat/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To encode them, we use a pre-trained Transformer-based language model, T5-XXL (Raffel et al., 2020).
- To improve the approximation capability for nonlinear robot actions, we replace the final linear decoder with Figure 4: (a) Unstable loss curve a nonlinear MLP decoder as a ...
- We choose Transformer as the scalable backbone network (Bao et al., 2023; Peebles & Xie, 2023) and make the following three key modifications from Diffusion Transfomer (DiT) by ...

## 원리적 동기
- We choose Transformer as the scalable backbone network (Bao et al., 2023; Peebles & Xie, 2023) and make the following three key modifications from Diffusion Transfomer (DiT) by ...
- To solve this problem, we add (a) Loss w/o QKN & RMSN QKNorm (Henry et al., 2020) to avoid numerical instability when calculating attention.
- To encode them, we use a pre-trained Transformer-based language model, T5-XXL (Raffel et al., 2020).

## 핵심 방법론
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
