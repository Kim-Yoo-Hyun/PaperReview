# Method

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model
- Paper link: ./2025/NeurIPS/2025_NeurIPS_4D-VLA-Spatiotemporal-Vision-Language-Action-Pretraining-w/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Vision-language model backbone We leverage a pretrained large vision-language model (VLM) as the backbone, specifically InternVL-4B , which consists of a text tokenizer T , a vision encoder ...
- To address this, we propose 4D-VLA, a novel approach that effectively integrates 4D information into the input to mitigate these sources of chaos.
- This inconsistency significantly hampers pretraining efficiency.

## 원리적 동기
- However, existing pretraining paradigms t often suffer from incomplete or under-informative input, lacking critical contextual cues required for reliable action reasoning.
- However, efficiently extracting useful information from these datasets remains a challenge for improving generalization across diverse scenarios.
- Vision-language model backbone We leverage a pretrained large vision-language model (VLM) as the backbone, specifically InternVL-4B , which consists of a text tokenizer T , a vision encoder ...

## 핵심 방법론
- Vision-language model backbone We leverage a pretrained large vision-language model (VLM) as the backbone, specifically InternVL-4B , which consists of a text tokenizer T , a vision encoder ...
- These tokens, together with task-specific text tokens, serve as feature inputs for the subsequent Transformer.
- After decoding through the VLM Transformer and action head, it ultimately generates the action output.
- The vision encoder processes visual observations, which are subsequently compressed by an MLP projector P to generate vision embeddings, while text inputs are tokenized and embedded to form ...
- These multimodal tokens are then fed into the decoder D for next-token prediction.
