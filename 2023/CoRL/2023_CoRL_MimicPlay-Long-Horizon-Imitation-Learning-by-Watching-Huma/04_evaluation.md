# Evaluation

- Year/Venue: 2023 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, Imitation Learning, human video, cross-embodiment, hierarchical policy, long-horizon manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://mimic-play.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- success rate

## Evaluation Protocol and Results
- Our method outperforms Ours (0% human) by more than 23% in long-horizon task settings over all trained tasks, as shown in both Tab.
- Ours (0% human) trained with our two-stage framework outperform prior end-to-end learning methods in the long-horizon task settings by more than 15%, as is shown in Tab.
- 2, our full with GMM model largely outperforms Ours (w/o GMM).
- These results showcase the difficulty of learning multiple tasks with a single model.
- With systematic evaluations of 14 longhorizon manipulation tasks in the real world, we show that MIMICPLAY outperforms state-of-the-art imitation learning methods in task success rate, generalization ability, and ...
- Our method outperforms Ours (0% human) by more than 23% in long-horizon task settings over all trained tasks, as shown in both Tab.

## Baselines
- 2, although Ours (w/o KL) baseline outperforms most baselines in trained tasks, its success rate is 17% lower than Ours.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
