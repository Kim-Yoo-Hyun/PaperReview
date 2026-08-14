# Evaluation

- Year/Venue: 2025 / Nature
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, generalist reinforcement learning, latent imagination
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://danijar.com/project/dreamerv3/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Evaluation Protocol and Results
- Crucially, Dreamer substantially outperforms PPO across all domains. • Atari This established benchmark contains 57 Atari 2600 games with a budget of 200M frames, posing a diverse range ...
- Dreamer also outperforms the widely-used expert algorithms Rainbow 40 and IQN 41 . • ProcGen This benchmark of 16 games features randomized levels and visual distractions to test ...
- We designed the experiments to compare Dreamer to the best methods in the literature, which are often specifically designed and tuned for the benchmark at hand.
- Dreamer outperforms the powerful MuZero algorithm 8 while using only a fraction of the computational resources.
- Minecraft Diamond Max Mean 100K 1M 10M 100M Env steps Unified configuration Figure 1: Benchmark summary. a, Using fixed hyperparameters across all domains, Dreamer outperforms tuned expert algorithms ...
- Crucially, Dreamer substantially outperforms PPO across all domains. • Atari This established benchmark contains 57 Atari 2600 games with a budget of 200M frames, posing a diverse range ...

## Baselines
- We note that these baselines were not designed for data-efficiency but serve as a valuable comparison point for the performance previously achievable at scale.
- We designed the experiments to compare Dreamer to the best methods in the literature, which are often specifically designed and tuned for the benchmark at hand.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
