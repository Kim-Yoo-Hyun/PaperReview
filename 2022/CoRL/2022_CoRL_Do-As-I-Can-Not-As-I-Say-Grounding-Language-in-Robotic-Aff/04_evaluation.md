# Evaluation

- Year/Venue: 2022 / CoRL
- Category: Foundations: Vision-Language-Action and Robotics
- Tags: LLM, affordance, Planning, Robotics
- Paper link: ./2022/CoRL/2022_CoRL_Do-As-I-Can-Not-As-I-Say-Grounding-Language-in-Robotic-Aff/paper.pdf
- Code/Project: https://say-can.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- success rate

## Evaluation Protocol and Results
- The results in Table 2 illustrate the necessity of the language grounding where BC NL achieves 0% in all tasks and BC USE achieves 60% for single primitives, ...
- In the mock kitchen, PaLMSayCan achieved a planning success rate of 84% and an execution rate of 74%.
- To study the importance of the LLM, we conduct two ablation experiments using the language-conditioned policy (see Sections 4-4).
- The full task list and results can be found in the Appendix Table 5, and videos of experiment rollouts and the decision making process can be found on ...
- The results in Table 2 illustrate the necessity of the language grounding where BC NL achieves 0% in all tasks and BC USE achieves 60% for single primitives, ...
- In the mock kitchen, PaLMSayCan achieved a planning success rate of 84% and an execution rate of 74%.

## Baselines
- We compare PaLM-SayCan to (1) No VF, which removes the value function grounding (i.e., choosing the maximum language score skill) and to (2) Generative, which uses the generative ...
- The latter in effect compares to , which loses the explicit option probabilities, and thus is less interpretable and cannot be combined with affordance probabilities.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
