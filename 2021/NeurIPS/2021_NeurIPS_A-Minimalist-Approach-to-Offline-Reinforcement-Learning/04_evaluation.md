# Evaluation

- Year/Venue: 2021 / NeurIPS
- Category: Robot Learning and Data
- Tags: Robotics, offline reinforcement learning, behavior cloning, continuous control
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://github.com/sfujim/TD3_BC
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Evaluation Protocol and Results
- Our offline RL baselines include two state-of-the-art algorithms, CQL [Kumar et al., 2020] and Fisher-BRC [Kostrikov et al., 2021], as well as BRAC [Wu et al., 2019] and ...
- We evaluate our proposed approach on the D4RL benchmark of OpenAI gym MuJoCo tasks [Todorov et al., 2012, Brockman et al., 2016, Fu et al., 2020], which encompasses ...
- We train each algorithm for 1 million time steps and evaluate every 5000 time steps.
- We find that we can match the performance of state-of-the-art offline RL algorithms by simply adding a behavior cloning term to the policy update of an online RL ...
- Our offline RL baselines include two state-of-the-art algorithms, CQL [Kumar et al., 2020] and Fisher-BRC [Kostrikov et al., 2021], as well as BRAC [Wu et al., 2019] and ...

## Baselines
- Our offline RL baselines include two state-of-the-art algorithms, CQL [Kumar et al., 2020] and Fisher-BRC [Kostrikov et al., 2021], as well as BRAC [Wu et al., 2019] and ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
