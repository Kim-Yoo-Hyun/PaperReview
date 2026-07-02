# Evaluation

- Year/Venue: 2025 / NeurIPS Spotlight
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model
- Paper link: ./2025/NeurIPS/2025_NeurIPS_SafeVLA-Towards-Safety-Alignment-of-Vision-Language-Action/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- Objaverse

## Metrics
- mAP
- SR
- success rate

## Evaluation Protocol and Results
- The results demonstrate that our approach with dynamic Lagrangian multipliers achieves a superior trade-off, adhering to the cost limit while attaining a higher success rate than any fixed-penalty ...
- The results consistently show that ISA alignment leads to substantial improvements across these models, evidenced by significant reductions in CC alongside stable SR when evaluated on Safety-CHORES and ...
- ISA achieves an average SR increase of 3.85% compared to FLaRe, outperforming IL-only baselines and matching or exceeding other RL-based methods.
- Right: CC incurred by each model on these benchmarks. demonstrates substantial safety improvements, achieving an average reduction in CC of 83.58% compared to the strongest task-focused RL baseline, ...
- The results demonstrate that our approach with dynamic Lagrangian multipliers achieves a superior trade-off, adhering to the cost limit while attaining a higher success rate than any fixed-penalty ...
- The results consistently show that ISA alignment leads to substantial improvements across these models, evidenced by significant reductions in CC alongside stable SR when evaluated on Safety-CHORES and ...

## Baselines
- We compare ISA against a comprehensive set of baselines that represent various paradigms for VLA training and fine-tuning.
- We compare this against baselines using fixed penalty coefficients for safety costs, as shown in Figure 6.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
