# Evaluation

- Year/Venue: 2020 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, Imitation Learning, Reinforcement Learning, long-horizon manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://relay-policy-learning.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- success rate

## Evaluation Protocol and Results
- When we analyze the proportion of compound goals that are actually fully achieved (see Table 1, bottom row), RIL shows significant improvement over other methods.
- Our experiments aim to answer the following questions: (1) Does RIL improve imitation learning with unstructured and unlabelled demonstrations? (2) Is RIL more amenable to RL fine-tuning than ...
- Lastly, we compare RPL with a baseline (7) (Nearest Neighbor) which uses a nearest neighbor strategy to choose the demonstration which has the achieved goal closest to the ...
- We find that, while none of the variants are able to achieve near-perfect completion scores via just imitation, the average stepwise completion score is higher for RIL as ...
- When we analyze the proportion of compound goals that are actually fully achieved (see Table 1, bottom row), RIL shows significant improvement over other methods.
- Videos are available at https://relay-policy-learning.github.io/ Our experiments aim to answer the following questions: (1) Does RIL improve imitation learning with unstructured and unlabelled demonstrations? (2) Is RIL more ...

## Baselines
- For comparisons with methods that learn from scratch we compare with (6) an on-policy variant of HIRO trained from scratch with natural policy gradient instead of Q-learning and ...
- Each goal has different elements manipulated, requiring multiple stages to solve: (a) microwave, kettle, light, slider, (b) kettle, burner, slider, cabinet, (c) burner, top burner, slide hinge, (d) ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
