# NavBench: Probing Multimodal Large Language Models for Embodied Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://neurips.cc/virtual/2025/poster/116120.
> PDF retrieval source: https://arxiv.org/pdf/2506.01031. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: Yanyuan Qiao, Haodong Hong, Wenqi Lyu, Dong An, Siqi Zhang, Yutong Xie, Xinyu Wang, Qi Wu
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Navigation
- Official paper: https://neurips.cc/virtual/2025/poster/116120
- Published PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/8932bbe603280f51d425e2781cd6ea6e-Paper-Conference.pdf
- Full-text retrieval at original review: https://arxiv.org/pdf/2506.01031
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

NavBench는 모델이 이동 지시와 장면을 이해하는 능력과 실제로 다음 이동을 선택해 목적지에 도달하는 능력을 나누어 평가한다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/8932bbe603280f51d425e2781cd6ea6e-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Multimodal Large Language Models (MLLMs) have demonstrated strong generalization in vision-language tasks, yet their ability to understand and act within embodied environments remains underexplored.
- **p. 1 / Abstract - extractive body cue:** We present NavBench, a benchmark to evaluate the embodied navigation capabilities of MLLMs under zero-shot settings.
- **p. 1 / Abstract - extractive body cue:** NavBench consists of two components: (1) navigation comprehension, assessed through three cognitively grounded tasks including global instruction alignment, temporal progress estimation, and local observation-action reasoning, ...
- **p. 1 / Abstract - extractive body cue:** To support real-world deployment, we introduce a pipeline that converts MLLMs' outputs into robotic actions.
- **p. 1 / Abstract - extractive body cue:** We evaluate both proprietary and open-source models, finding that GPT-4o performs well across tasks, while lighter open-source models succeed in simpler cases.
- **p. 2 / 1 Introduction - extractive body cue:** However, most existing benchmarks treat all navigation episodes equally difficult, failing to capture this essential variation.
- **p. 2 / 1 Introduction - extractive body cue:** This allows detailed analysis of models' generalization and decision-making performance across varying levels of difficulty.

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** In summary, our main contributions are as follows: (1) We introduce NavBench, a benchmark for evaluating MLLMs in embodied navigation under zero-shot settings.
- **p. 2 / 1 Introduction - extractive body cue:** To fill these gaps, we introduce NavBench, a benchmark designed to systematically evaluate MLLMs in embodied navigation under zero-shot settings.
- **p. 3 / 1 Introduction - extractive body cue:** pipeline includes a waypoint selection module, an MLLM-based navigator, and a low-level controller, demonstrating the deployability of our framework in physical environments.
- **p. 1 / Abstract - extractive body cue:** To support real-world deployment, we introduce a pipeline that converts MLLMs' outputs into robotic actions.
- **p. 1 / Abstract - extractive body cue:** NavBench consists of two components: (1) navigation comprehension, assessed through three cognitively grounded tasks including global instruction alignment, temporal progress estimation, and local observation-action reasoning, ...
- **p. 2 / 1 Introduction - extractive body cue:** Local Observation-Action Inference evaluates the model's ability to reason about the spatial consequences of individual actions by either predicting the future observation given an action ...
- **p. 7 / C Progress Level - extractive body cue:** It consists of three modules: (1) a Waypoint Predictor that extracts RGB and depth inputs to generate candidate waypoints, (2) an MLLM Decision Module that ...
- **p. 6 / C Progress Level - extractive body cue:** Local Observation-Action Reasoning We design two multiple-choice reasoning tasks to evaluate a model's capacity for local spatial and action reasoning inference.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | NavBench consists of two components: (1) navigation comprehension, assessed through three cognitively grounded tasks including global instruction alignment, temporal progress estimation, and local observation-action reasoning, covering ... | camera/depth stream, pose, map와 language goal | p. 1 (Abstract), p. 4 (C Progress Level) |
| State/latent | NavBench, consists, components, navigation, comprehension, assessed, through, three, cognitively, grounded, tasks, including | robot pose, free-space/semantic map와 local goal | p. 1 (Abstract), p. 4 (C Progress Level), p. 5 (C Progress Level) |
| Output/action | This evaluates the model's capacity to monitor task progress and comprehend the temporal structure of instructions. • Local Level - Local Observation-Action Reasoning: To evaluate the model's ability to reason about the ... | collision-free trajectory 또는 velocity command | p. 4 (C Progress Level), p. 5 (C Progress Level), p. 8 (C Progress Level) |
| Objective/outcome | To ensure data quality and minimize ambiguity, we filter the examples using a curated list of valid instruction-path pairs. | goal reach, safety, localization error와 replanning latency | p. 6 (C Progress Level), p. 4 (C Progress Level), p. 4 (C Progress Level) |

## Main Claims and Actual Contribution

- 지시와 전체 경로의 대응, 이동 진행도, 현재 관측과 행동의 관계를 묻는 질의응답을 만들고 장면과 경로 난이도에 따라 실행 에피소드를 구성했다. [PDF 4쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/8932bbe603280f51d425e2781cd6ea6e-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/8932bbe603280f51d425e2781cd6ea6e-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/8932bbe603280f51d425e2781cd6ea6e-Paper-Conference.pdf#page=6)
- 공개·비공개 모델의 이해 점수와 이동 수행을 비교하고, 지도 정보를 추가할 때의 성능 변화와 진행도 추정에서의 실패를 분석했다. [PDF 8쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/8932bbe603280f51d425e2781cd6ea6e-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/8932bbe603280f51d425e2781cd6ea6e-Paper-Conference.pdf#page=9) · [PDF 10쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/8932bbe603280f51d425e2781cd6ea6e-Paper-Conference.pdf#page=10)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (5.3 Discussion), p. 9 (5.3 Discussion) |
| Embodiment/environment | Navigation Comprehension Source Raw Datasets R2R / RxR … Step A1 Extract Multimodal Navigation Data Step A2 Navigation Execution Sample Navigation Episodes MatterPort3D Simulator Step B1 Compute Difficulty Sores Step B2 Spatial/Cognitiv ... | hardware/simulator version and reset protocol | p. 5 (C Progress Level), p. 5 (C Progress Level) |
| Dataset/benchmark | 3.2.2 Navigation Episodes Collection We sample 432 navigation cases from 72 unique scenes in the Matterport3D simulator [55]. | role, split, size and leakage | p. 5 (C Progress Level), p. 5 (C Progress Level), p. 6 (C Progress Level), p. 8 (C Progress Level) |
| Metric | Their responses were automatically scored using the same metrics applied to model evaluation, including accuracy for comprehension tasks and SR/SPL for execution. | definition, denominator, direction and uncertainty | p. 8 (C Progress Level), p. 9 (5.3 Discussion), p. 9 (C Progress Level) |
| Baseline/ablation | As shown in Figure 7, models show consistent performance across both, with GPT-4o clearly outperforming all others, consistent with its strong results in Navigation Execution. | fair input/data/compute/action matching | p. 9 (5.3 Discussion), p. 8 (Figure/Table caption), p. 9 (5.3 Discussion) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 5.3 Discussion - extractive body cue:** Error Analysis We manually analyze 100 failed cases to understand model failures.
- **p. 9 / 5.3 Discussion - extractive body cue:** The models' failure in this setting highlights their limited ability to reason about temporal order within complex instructions.
- **p. 7 / C Progress Level - extractive body cue:** All physical experiments are conducted in a controlled indoor lab to assess robustness and feasibility.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (Abstract)이다.
