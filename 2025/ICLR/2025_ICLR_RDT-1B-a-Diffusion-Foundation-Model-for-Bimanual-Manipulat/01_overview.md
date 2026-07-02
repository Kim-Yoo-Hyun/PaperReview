# RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation

- Year/Venue: 2025 / ICLR Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, Diffusion
- Paper link: ./2025/ICLR/2025_ICLR_RDT-1B-a-Diffusion-Foundation-Model-for-Bimanual-Manipulat/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- We choose Transformer as the scalable backbone network (Bao et al., 2023; Peebles & Xie, 2023) and make the following three key modifications from Diffusion Transfomer (DiT) by ...
- To solve this problem, we add (a) Loss w/o QKN & RMSN QKNorm (Henry et al., 2020) to avoid numerical instability when calculating attention.
- Besides, we also note that our problem can 5 ' 7 Z R 0 / 3 be considered as a time series forecasting task, and the centering Z ...

## Core Idea
- To encode them, we use a pre-trained Transformer-based language model, T5-XXL (Raffel et al., 2020).
- To improve the approximation capability for nonlinear robot actions, we replace the final linear decoder with Figure 4: (a) Unstable loss curve a nonlinear MLP decoder as a ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- To improve the approximation capability for nonlinear robot actions, we replace the final linear decoder with Figure 4: (a) Unstable loss curve a nonlinear MLP decoder as a ...
- 4a shows that large-scale pre-training tends to be 7 D V N very unstable or even explode without this modification. (b) Task w/o MLP or ACI • MLP ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To improve the approximation capability for nonlinear robot actions, we replace the final linear decoder with Figure 4: (a) Unstable loss curve a nonlinear MLP decoder as a ...
- 4a shows that large-scale pre-training tends to be 7 D V N very unstable or even explode without this modification. (b) Task w/o MLP or ACI • MLP ...
- We choose Transformer as the scalable backbone network (Bao et al., 2023; Peebles & Xie, 2023) and make the following three key modifications from Diffusion Transfomer (DiT) by ...

## Abstract Cue
- , posing integration challenges due to their complexity and ambiguity.
