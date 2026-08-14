# Evaluation

- Year/Venue: 2024 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, embodiment, graph neural network, policy learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sferrazza.cc/bot_site/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- mAP

## Evaluation Protocol and Results
- We report results in the table shown in Figure 3a, where BoT consistently outperforms the MLP and transformer baselines.
- While the multi-clip policy is competitive with the vanilla transformer baseline, it is strongly outperformed by our architecture.
- 5.1 Imitation Learning Experiments We evaluate the imitation learning performance of the BoT architecture in a body-tracking task defined through the MoCapAct dataset , which comprises action-labeled humanoid ...
- Particularly, across the various experiments listed in this section, we present the following baselines and variations: (i) an MLP that stacks all embedding vectors as its input, (ii) ...
- We report results in the table shown in Figure 3a, where BoT consistently outperforms the MLP and transformer baselines.
- While the multi-clip policy is competitive with the vanilla transformer baseline, it is strongly outperformed by our architecture.

## Baselines
- As shown in Figure 3b, we also find that BoT-Hard exhibits strong scaling capabilities, as its performance keeps improving with the number of trainable parameters compared to the ...
- This is a particularly remarkable result, as the comparison presents conditions more favorable to the baseline, which features a more flexible stochastic policy, was optimized in a recurrent ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
