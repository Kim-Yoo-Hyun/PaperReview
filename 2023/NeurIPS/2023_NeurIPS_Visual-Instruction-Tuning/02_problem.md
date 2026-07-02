# Problem

- Year/Venue: 2023 / NeurIPS
- Category: Foundations: Vision-Language Models
- Tags: Vision-Language Model, LLM, instruction tuning
- Paper link: ./2023/NeurIPS/2023_NeurIPS_Visual-Instruction-Tuning/paper.pdf
- Code/Project: https://github.com/haotian-liu/LLaVA
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- One key challenge is the lack of vision-language instruction-following data.

## 해결하려는 문제
- By instruction tuning on such generated data, we introduce LLaVA: Large Language and Vision Assistant, an end-to-end trained large multimodal model that connects a vision encoder and an ...
- Our experiments show that LLaVA demonstrates impressive multimodal chat abilities, sometimes exhibiting the behaviors of multimodal GPT-4 on unseen images/instructions, and yields a 85.1% relative score compared with ...
- When fine-tuned on Science QA, the synergy of LLaVA and GPT-4 achieves a new state-of-the-art accuracy of 92.53%.

## 선행 연구 / 배경 단서
- One key challenge is the lack of vision-language instruction-following data.
- We develop a large multimodal model (LMM), by connecting the open-set visual encoder of CLIP with the language decoder Vicuna , and fine-tuning end-to-end on our generated instructional ...
- In this paper, we present visual instruction-tuning, the first attempt to extend instruction-tuning to the language-image multimodal space, to pave the way towards building a general-purpose visual assistant.
