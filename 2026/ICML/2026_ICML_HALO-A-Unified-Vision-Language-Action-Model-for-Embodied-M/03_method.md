# Method

- Year/Venue: 2026 / ICML
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model
- Paper link: ./2026/ICML/2026_ICML_HALO-A-Unified-Vision-Language-Action-Model-for-Embodied-M/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To enable H ALO learning at scale, we introduce an automated pipeline to synthesize EM-CoT training data along with a carefully crafted training recipe.
- To this end, we propose H ALO, a unified VLA model that enables embodied multimodal chain-of-thought (EM-CoT) reasoning through textual reasoning, fine-grained visual subgoal prediction, and EM-CoT-augmented action ...
- We instantiate H ALO with a Mixture-ofTransformers (MoT) architecture that decouples semantic reasoning, visual foresight, and action prediction into specialized experts with seamless cross-expert collaboration.

## 원리적 동기
- However, most existing VLAs map perceptual inputs directly to motor commands, lacking explicit mechanisms for reasoning about task structure or anticipating how the environment will evolve under motion ...
- This limitation becomes particularly pronounced in long-horizon or out-of-distribution scenarios—such as novel layouts, unfamiliar objects, or contact-rich interactions—where successful execution depends more on deliberation and foresight than on ...
- To enable H ALO learning at scale, we introduce an automated pipeline to synthesize EM-CoT training data along with a carefully crafted training recipe.

## 핵심 방법론
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
