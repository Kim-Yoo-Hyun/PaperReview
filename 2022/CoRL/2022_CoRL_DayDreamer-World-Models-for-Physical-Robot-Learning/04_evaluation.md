# Evaluation

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2022 / CoRL
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, real robot, model-based reinforcement learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://danijar.com/project/daydreamer/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- UNVERIFIED — full text의 해당 section을 정독한 뒤 근거와 위치를 기록한다.

## Metrics
- UNVERIFIED — full text의 해당 section을 정독한 뒤 근거와 위치를 기록한다.

## Evaluation Protocol and Results
- The goal of the experiments is to evaluate whether the recent successes of learned world models enables sample-efficient robot learning directly in the real world.
- The experiments are representative of common robotic tasks, such as locomotion, manipulation, and navigation.
- We evaluate Dreamer on 4 robots, each with a different task, and compare its performance to appropriate algorithmic and human baselines.
- The Dreamer algorithm has recently shown great promise for learning from small amounts of interaction by planning within a learned world model, outperforming pure reinforcement learning in video ...
- The goal of the experiments is to evaluate whether the recent successes of learned world models enables sample-efficient robot learning directly in the real world.

## Baselines
- We evaluate Dreamer on 4 robots, each with a different task, and compare its performance to appropriate algorithmic and human baselines.
- Specifically, we aim to answer the following research questions: • Does Dreamer enable robot learning directly in the real world, without simulators? • Does Dreamer succeed across various ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
