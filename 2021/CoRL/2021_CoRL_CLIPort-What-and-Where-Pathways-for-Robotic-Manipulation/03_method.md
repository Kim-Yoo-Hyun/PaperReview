# Method

- Year/Venue: 2021 / CoRL
- Category: Foundations: Vision-Language-Action and Robotics
- Tags: Robotics, Vision-Language Action, CLIP, manipulation
- Paper link: ./2021/CoRL/2021_CoRL_CLIPort-What-and-Where-Pathways-for-Robotic-Manipulation/paper.pdf
- Code/Project: https://cliport.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To this end, we propose a framework that combines the best of both worlds: a two-stream architecture with semantic and spatial pathways for vision-based manipulation.
- Specifically, we present CLIP ORT, a language-conditioned imitationlearning agent that combines the broad semantic understanding (what) of CLIP with the spatial precision (where) of Transporter .
- 5 Conclusion We introduced CLIP ORT, an end-to-end framework for language-conditioned fine-grained manipulation.

## 원리적 동기
- To address this problem, we bake in a strong semantic prior while learning policies.
- A natural solution to both these problems is to condition policies with natural language.
- To this end, we propose a framework that combines the best of both worlds: a two-stream architecture with semantic and spatial pathways for vision-based manipulation.

## 핵심 방법론
- 5 Conclusion We introduced CLIP ORT, an end-to-end framework for language-conditioned fine-grained manipulation.
- We estimate that for more robust real-world performance at least 50 to 100 training demonstrations are necessary, as evident in Figure 3.
- Interestingly, we observed that the model sometimes exploits biases in the training data instead of learning to ground instructions.
- Task success scores (mean %) from 100 evaluation instances vs. # of training demonstrations (1, 10, 100, or 1000).
- It also validates a trait of data-driven approaches where training on lots of diverse data leads to more robust and generalizable representations .
