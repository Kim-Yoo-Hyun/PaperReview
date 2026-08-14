# Evaluation

- Year/Venue: 2023 / CoRL
- Category: Planning and Long-Horizon Reasoning
- Tags: Robotics, 3D Vision, LLM planning, 3D Scene Graph, replanning, mobile manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sayplan.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- mAP
- success rate

## Evaluation Protocol and Results
- SayPlan (GPT-4) in contrast achieved 86.7% and 73.3% success in identifying the desired subgraph across both the simple and complex search tasks respectively, demonstrating significantly better graph-based reasoning ...
- Semantic Search Office Home Subtask Human SayPlan (GPT-3.5) SayPlan (GPT-4) Human SayPlan (GPT-3.5) SayPlan (GPT-4) Simple Search Complex Search 100% 100% 6.6% 0.0% 86.7% 73.3% 100% 100% 0.0% ...
- The table shows the semantic search success rate failed to reason over the input graph in finding a suitable subgraph for planning. representation, hallucinating nodes to explore or ...
- : Large language models (LLMs) have demonstrated impressive results in developing generalist planning agents for diverse tasks.
- SayPlan (GPT-4) in contrast achieved 86.7% and 73.3% success in identifying the desired subgraph across both the simple and complex search tasks respectively, demonstrating significantly better graph-based reasoning ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
