# Evaluation

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics, Reinforcement Learning
- Paper link: ./2025/NeurIPS/2025_NeurIPS_DreamVLA-A-Vision-Language-Action-Model-Dreamed-with-Compr/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- CALVIN
- LIBERO

## Metrics
- accuracy
- mAP
- SR
- success rate
- collision

## Evaluation Protocol and Results
- 4.2 Simulation Benchmark Experiments Simulation setup.
- We evaluate DreamVLA on CALVIN and LIBERO benchmark.
- For the LIBERO benchmark, we first pretrain DreamVLA on LIBERO-90 and then finetune on each track.
- CALVIN is a simulated benchmark designed for learning long-horizon, language-conditioned robot manipulation policies.
- Extensive experiments on both real-world and simulation environments demonstrate that DreamVLA achieves 76.7% success rate on real robot tasks and 4.44 average length on the CALVIN ABC-D benchmarks.
- Recent advances in vision-language-action (VLA) models have shown promise in integrating image generation with action prediction to improve generalization and reasoning in robot manipulation.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
