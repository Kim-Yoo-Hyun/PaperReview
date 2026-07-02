# Method

- Year/Venue: 2023 / NeurIPS
- Category: Foundations: Vision-Language Models
- Tags: Vision-Language Model, LLM, instruction tuning
- Paper link: ./2023/NeurIPS/2023_NeurIPS_Visual-Instruction-Tuning/paper.pdf
- Code/Project: https://github.com/haotian-liu/LLaVA
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- By instruction tuning on such generated data, we introduce LLaVA: Large Language and Vision Assistant, an end-to-end trained large multimodal model that connects a vision encoder and an ...
- We present the instruction-following data.
- Best variant 90.92 89.96 (-0.96) We tried using the last layer feature from CLIP 89.77 (-1.15) Predict answer first vision encoder, which yields 89.96% and is Training from ...

## 원리적 동기
- One key challenge is the lack of vision-language instruction-following data.
- By instruction tuning on such generated data, we introduce LLaVA: Large Language and Vision Assistant, an end-to-end trained large multimodal model that connects a vision encoder and an ...

## 핵심 방법론
- Best variant 90.92 89.96 (-0.96) We tried using the last layer feature from CLIP 89.77 (-1.15) Predict answer first vision encoder, which yields 89.96% and is Training from ...
- We skip pre-training and directly train on Science QA from scratch – performance drops to 85.81% accuracy.
- The 5.11% absolute degradation indicates the importance of our pre-training stage, in aligning multimodal features while preserving the vast pre-trained knowledge. (iv) Model size.
