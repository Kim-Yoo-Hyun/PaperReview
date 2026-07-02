# Problem

- Year/Venue: 2026 / ICML
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model
- Paper link: ./2026/ICML/2026_ICML_HALO-A-Unified-Vision-Language-Action-Model-for-Embodied-M/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- However, most existing VLAs map perceptual inputs directly to motor commands, lacking explicit mechanisms for reasoning about task structure or anticipating how the environment will evolve under motion ...
- This limitation becomes particularly pronounced in long-horizon or out-of-distribution scenarios—such as novel layouts, unfamiliar objects, or contact-rich interactions—where successful execution depends more on deliberation and foresight than on ...
- Recent work has sought to address this limitation by introducing intermediate reasoning processes like human.

## 해결하려는 문제
- Extensive experiments demonstrate that: (1) H ALO achieves superior performance in both simulated and real world, surpassing baseline policy π0 by 25.9% on the RoboTwin benchmark; (2) all ...
- To enable H ALO learning at scale, we introduce an automated pipeline to synthesize EM-CoT training data along with a carefully crafted training recipe.
- We instantiate H ALO with a Mixture-ofTransformers (MoT) architecture that decouples semantic reasoning, visual foresight, and action prediction into specialized experts with seamless cross-expert collaboration.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
