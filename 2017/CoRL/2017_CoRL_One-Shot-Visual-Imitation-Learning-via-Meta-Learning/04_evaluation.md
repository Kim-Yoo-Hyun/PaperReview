# Evaluation

- Year/Venue: 2017 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, Imitation Learning, meta-learning, visual manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://arxiv.org/abs/1703.07326
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- mAP
- success rate

## Evaluation Protocol and Results
- 2 Additional experiment results are available in the Appendix, including a simple illustrative example of particle reaching tasks and further analysis of block stacking 6 • Can our ...
- We conduct experiments with the block stacking tasks described in Section 3.2.2 These experiments are designed to answer the following questions: • How does training with behavioral cloning ...
- We evaluate the policy on tasks seen during training, as well as tasks unseen during training.
- Note that generalization is evaluated at multiple levels: the learned policy not only needs to generalize to new configurations and new demonstrations of tasks seen already, but also ...
- Our experiments show that the use of soft attention allows the model to generalize to conditions and tasks unseen in the training data.
- 2 Additional experiment results are available in the Appendix, including a simple illustrative example of particle reaching tasks and further analysis of block stacking 6 • Can our ...

## Baselines
- To answer these questions, we compare the performance of the following architectures: • BC: We use the same architecture as previous, but and the policy using behavioral cloning. ...
- We conduct experiments with the block stacking tasks described in Section 3.2.2 These experiments are designed to answer the following questions: • How does training with behavioral cloning ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
