# Evaluation

- Year/Venue: 2023 / NeurIPS
- Category: Foundations: Vision-Language Models
- Tags: Vision-Language Model, LLM, instruction tuning
- Paper link: ./2023/NeurIPS/2023_NeurIPS_Visual-Instruction-Tuning/paper.pdf
- Code/Project: https://github.com/haotian-liu/LLaVA
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- COCO
- Habitat

## Metrics
- accuracy

## Evaluation Protocol and Results
- 5.1 Multimodal Chatbot We developed a chatbot demo to show the image understanding and conversation abilities of LLaVA, and to study how well LLaVA is able to digest ...
- We first use the examples in the original GPT-4 paper , shown in Table 3 (more examples in Appendix), that require in-depth image understanding.
- When fine-tuned on Science QA, the synergy of LLaVA and GPT-4 achieves a new state-of-the-art accuracy of 92.53%.
- Our experiments show that LLaVA demonstrates impressive multimodal chat abilities, sometimes exhibiting the behaviors of multimodal GPT-4 on unseen images/instructions, and yields a 85.1% relative score compared with ...

## Baselines
- For comparisons, we quote the prompt and response of the multimodal GPT-4 from their paper, and query BLIP-2 and OpenFlamingo model checkpoints to get their response.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
