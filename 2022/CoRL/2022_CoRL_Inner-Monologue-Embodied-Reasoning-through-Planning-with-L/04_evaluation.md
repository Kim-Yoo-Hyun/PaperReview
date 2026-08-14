# Evaluation

- Year/Venue: 2022 / CoRL
- Category: Planning and Long-Horizon Reasoning
- Tags: Robotics, LLM planning, feedback, replanning, long-horizon manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://innermonologue.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- mAP
- success rate

## Evaluation Protocol and Results
- Below, we show results for a tabletop manipulation environment in sim (Sec 4.1) and real (Sec 4.2) as well as a mobile manipulation environment in real (Sec 4.3).
- For more details about the experiment setup and results, please refer to the Appendix.
- 4.1 Simulated Tabletop Rearrangement We experiment with vision-based block manipulation tasks in a Ravens-based simulation environment to evaluate our method against several baselines and ablate across varying amounts ...
- Below, we show results for a tabletop manipulation environment in sim (Sec 4.1) and real (Sec 4.2) as well as a mobile manipulation environment in real (Sec 4.3).
- We find that closed-loop language feedback significantly improves high-level instruction completion on three domains, including simulated and real table top rearrangement tasks and long-horizon mobile manipulation tasks in ...

## Baselines
- 4.1 Simulated Tabletop Rearrangement We experiment with vision-based block manipulation tasks in a Ravens-based simulation environment to evaluate our method against several baselines and ablate across varying amounts ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
