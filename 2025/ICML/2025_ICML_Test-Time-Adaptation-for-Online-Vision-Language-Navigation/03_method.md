# Method

- Year/Venue: 2025 / ICML Poster
- Category: Navigation and Embodied AI
- Tags: Vision-Language Model, Navigation, Reinforcement Learning
- Paper link: ./2025/ICML/2025_ICML_Test-Time-Adaptation-for-Online-Vision-Language-Navigation/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Additionally, we propose a gradient regularization technique that leverages the binary structure of F EED TTA to achieve a balance between plasticity and stability during adaptation.
- Experiments In this section, we present experimental results of our study.
- To address this, we introduce F EED TTA, a novel TTA framework for online VLN utilizing feedback-based reinforcement learning.

## 원리적 동기
- One existing approach (Gao et al., 2024a) relies on the widely adopted TTA paradigm of entropy minimization (Wang et al., 2020a; Zhang et al., 2022), where we identify ...
- Navigating in an unfamiliar environment during deployment poses a critical challenge for a vision-language navigation (VLN) agent.
- Additionally, we propose a gradient regularization technique that leverages the binary structure of F EED TTA to achieve a balance between plasticity and stability during adaptation.

## 핵심 방법론
- Experiments In this section, we present experimental results of our study.
- For a comparable evaluation with our approach, Tent is applied on a per-episode basis. • RQ2: How sensitive is the performance to the quality and the quantity of ...
- We use a batch size of 1 to properly simulate the online environment.
- For R2R and R2R-CE, we use p = 0.05 and α = 0.1 for both splits.
