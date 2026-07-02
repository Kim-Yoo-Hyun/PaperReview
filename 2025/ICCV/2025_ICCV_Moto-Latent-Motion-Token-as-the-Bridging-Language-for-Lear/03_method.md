# Method

- Year/Venue: 2025 / ICCV
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics
- Paper link: ./2025/ICCV/2025_ICCV_Moto-Latent-Motion-Token-as-the-Bridging-Language-for-Lear/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Inspired by the way humans learn new skills through observing dynamic environments, we propose that effective robotic learning should emphasize motion-related knowledge, which is closely tied to low-level ...
- To this end, we introduce Moto, which converts video content into latent Motion Token sequences by a Latent Motion Tokenizer, learning a bridging “language” of motion from videos ...
- We ask: given the abundant video data containing interaction-related knowledge available as a rich “corpus”, can a similar generative pretraining approach be effectively applied to enhance robot learning?

## 원리적 동기
- The key challenge is to identify an effective representation for autoregressive pre-training that benefits robot manipulation tasks.
- This success offers new promise for robotics, which has long been constrained by the high cost of action-labeled data.
- Inspired by the way humans learn new skills through observing dynamic environments, we propose that effective robotic learning should emphasize motion-related knowledge, which is closely tied to low-level ...

## 핵심 방법론
- Comparison of models adopting different pre-training techniques on CALVIN (ABC−→D).
