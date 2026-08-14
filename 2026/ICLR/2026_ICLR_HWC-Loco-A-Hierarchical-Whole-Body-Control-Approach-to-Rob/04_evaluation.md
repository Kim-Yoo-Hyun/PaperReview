# Evaluation

- Year/Venue: 2026 / ICLR Poster
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, whole-body control, robust locomotion, safety recovery
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://simonlinsx.github.io/HWC_Loco/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- success rate

## Evaluation Protocol and Results
- To demonstrate the robustness of HWC-Loco, we conduct extensive disturbance tests in simulation.
- To evaluate the effectiveness of different components in HWC-Loco, we design a comparison method using an ablation approach as follows: 1) HWC-Loco-l sets α to a lower value, ...
- We evaluate the policies on challenging terrains, specifically slopes and stairs.
- After regaining stability, it smoothly transitions back to goal tracking, showcasing its adaptive control in dynamic and uncertain environments.
- To evaluate the performance of HWC-Loco, we conduct extensive comparisons against state-of-the-art humanoid control models, demonstrating HWC-Loco’s superior performance across diverse terrains, robot structures, and locomotion tasks under ...
- To demonstrate the robustness of HWC-Loco, we conduct extensive disturbance tests in simulation.

## Baselines
- 4) To highlight the benefits of our hierarchical policy, we compare a recent advancement of DreamWaQ, called AHL , which employs two-phase training for updating the locomotion policy.
- To evaluate the effectiveness of different components in HWC-Loco, we design a comparison method using an ablation approach as follows: 1) HWC-Loco-l sets α to a lower value, ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
