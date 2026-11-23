# Can VLMs Diagnose and Recover from VLA Manipulation Faults?

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://icml.cc/virtual/2026/poster/64203.
> PDF retrieval source: https://kakigo.github.io/VLA-FixBench/. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: Bowen Yan, Jiahao Xiao, Kehui Liu, Jianbo Zhang, Zicheng Zhang, Qi Jia, Zhongjie Jia, Haoming Song, Chunyi Li, Bin Zhao, Guangtao Zhai
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, VLA, failure diagnosis, recovery, Benchmark, LIBERO, real robot
- Official paper: https://icml.cc/virtual/2026/poster/64203
- Full-text retrieval: https://kakigo.github.io/VLA-FixBench/
- Code/Project: https://kakigo.github.io/VLA-FixBench/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA-FixBench와 FaultEval은 조작 실패를 말로 진단하는 능력부터 실제 로봇을 복구하는 능력까지 단계별로 측정한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/yan26r/yan26r.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Existing VLA models frequently fail in robotic manipulation tasks, with poorly structured fault types that often require expert diagnosis.
- **p. 1 / Abstract - extractive body cue:** While VLMs offer strong explanatory capabilities, their effectiveness in assisting VLAs is limited by their unclear role in diagnostics and inadequate collaboration mechanisms.
- **p. 1 / Abstract - extractive body cue:** To address this, we introduce VLA-FixBench, a fault evaluation dataset that spans perception, planning, and control failures, and provides annotations for task stages, fault types, ...
- **p. 1 / Abstract - extractive body cue:** We further propose FaultEval, a static-to-dynamicto-real evaluation framework that benchmarks
- **p. 1 / 1. Introduction - extractive body cue:** With the rapid advancement of embodied intelligence, Vision-Language-Action (VLA) models have demonstrated increasing advantages in scenarios such as industrial assembly, logistics sorting, and household services.
- **p. 1 / 1. Introduction - 원문 대조 요지:** 기존 VLA는 로봇 조작 중 자주 실패하며 원인 진단에는 전문가 지식과 수작업이 필요하다.
- **p. 1 / 1. Introduction - extractive body cue:** As a result, existing methods face key limitations: insufficient focus on VLM-VLA collaboration with no standardized interfaces (Yang et al., 2025b; Chen et al., 2024), ...

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we introduce VLA-FixBench, a benchmark for VLM-assisted VLA fault diagnosis and recovery, with over 6,000 annotated failure cases across perception, planning, ...
- **p. 1 / 1. Introduction - extractive body cue:** Based on VLA-FixBench, we propose FaultEval, a unified static-to-dynamic-to-real evaluation framework that assesses VLM performance in fault identification, severity estimation, temporal localization, spatial correction, and ...
- **p. 2 / 1. Introduction - extractive body cue:** We further construct a VLM-VLA collaboration mechanism that enables fault detection, rollback, and action repair during VLA execution.
- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as follows: • VLA-FixBench, a robotic manipulation fault evaluation dataset comprising 6k failure cases covering perception, control, and cognition errors, ...
- **p. 4 / 3. Construction of VLA-FixBench - extractive body cue:** Multi-dimensional Annotation We develop a fine-grained annotation framework to construct a high-resolution failure map across three integrated dimensions: temporal, spatial, and semantic.
- **p. 3 / Approach - extractive body cue:** Reinforcement learning has been explored for failure recovery by learning corrective behaviors through interaction, including recent efforts that guide agents back to in-distribution states after ...
- **p. 3 / Approach - extractive body cue:** The bottom axis indicates the trade-off between evaluation convenience and physical accuracy. proaches employ supervised classifiers or temporal models to predict failure states from sensory ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The bottom axis indicates the trade-off between evaluation convenience and physical accuracy. proaches employ supervised classifiers or temporal models to predict failure states from sensory inputs. | standardized observation, action, task state와 evaluation split | p. 3 (Approach), p. 3 (Approach) |
| State/latent | bottom, axis, indicates, trade-off, between, evaluation, convenience, physical, accuracy, proaches, employ, supervised | benchmark state/goal와 method decision | p. 3 (Approach), p. 3 (Approach), p. 1 (1. Introduction) |
| Output/action | Reinforcement learning has been explored for failure recovery by learning corrective behaviors through interaction, including recent efforts that guide agents back to in-distribution states after Out-Of-Distribution (OOD) failures (Kim ... | policy/controller trajectory 또는 measured result | p. 3 (Approach), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Objective/outcome | While effective in specific domains (Li et al., 2026), such methods typically rely on task rewards or policy-level supervision, embedding recovery implicitly in learned behaviors. | success metric, robustness, generalization과 reproducibility | p. 3 (Approach) |

## Main Claims and Actual Contribution

- 실패 사례에 작업 단계·오류 유형·시간 및 공간상 수정 정보를 붙여 진단과 복구를 같은 사례에서 평가한다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/yan26r/yan26r.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/yan26r/yan26r.pdf#page=4)
- 실행을 되돌려 수정하는 방식의 시뮬레이션·실물 결과를 비교하고, 사람 전문가가 개입했을 때의 성공률을 상한으로 구별했다. [PDF 2쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/yan26r/yan26r.pdf#page=2) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/yan26r/yan26r.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 5 (4.2. Dynamic Evaluation), p. 9 (5.6. Ablation Study) |
| Embodiment/environment | To evaluate the practical performance of multimodal models in real-world robotic manipulation, we conduct on-robot experiments. | hardware/simulator version and reset protocol | p. 6 (4.3. Real-Time Evaluation), p. 9 (5.4. Real-Time Evaluation Results) |
| Dataset/benchmark | While existing benchmarks like LIBERO (Liu et al., 2023)provide rigorous environments to assess task success rates , they largely overlook the underlying failure behaviors. | role, split, size and leakage | p. 6 (4.3. Real-Time Evaluation), p. 9 (5.4. Real-Time Evaluation Results), p. 3 (2.2. Benchmark and Failure Evaluation of VLM), p. 4 (4.2. Dynamic Evaluation) |
| Metric | The performance is measured across diagnostic metrics (Recall, Precision, F2-Score, and FPR) and the manipulation Success Rate (SR). | definition, denominator, direction and uncertainty | p. 8 (5.2. Static Evaluation Results), p. 16 (Figure/Table caption), p. 4 (4.2. Dynamic Evaluation) |
| Baseline/ablation | Experimental results validate this choice: even with this minimal interface, human-in-theloop corrections yield 13% improvement in simulation and 35% on real robots, and precise rollback outperforms coarse task restarts, demonstrating t ... | fair input/data/compute/action matching | p. 5 (4.2. Dynamic Evaluation), p. 8 (5.4. Real-Time Evaluation Results), p. 8 (5.3. Dynamic Evaluation Results) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 5.4. Real-Time Evaluation Results - extractive body cue:** The real-robot setup is therefore a sparse diagnostic-and-recovery loop that trades limited inspection latency for recovery from failures that the VLA alone cannot escape.
- **p. 3 / 2.2. Benchmark and Failure Evaluation of VLM - extractive body cue:** We introduce a unified benchmark and evaluation framework that systematically characterizes failure types, severity, and spatiotemporal repair behaviors, and explicitly measures how VLMs contribute to ...
- **p. 2 / 2.1. Robotic Failure Diagnosis and Recovery - extractive body cue:** To bridge low-level signals and task execution, some works analyze failures in specific manipulation tasks.
- **p. 2 / 2.1. Robotic Failure Diagnosis and Recovery - extractive body cue:** As a result, existing failure analyses remain fragmented and lack a unified framework for systematic evaluation across tasks and models (Lin et al., 2025).Classical learning-based ...
- **p. 3 / 2.1. Robotic Failure Diagnosis and Recovery - extractive body cue:** Error severity level 7s Roll back time Accuracy Failure onset timestamp Convenience
- **p. 4 / 4.2. Dynamic Evaluation - extractive body cue:** For each failure scenario i, the model generates a dynamic recovery tuple ˆdi = ⟨ˆtstop, ˆtrb, vi⟩, consisting of the Stop Time ˆtstop ∈R≥0 representing ...
- **p. 8 / 5.2. Static Evaluation Results - extractive body cue:** Failure recovery in the real-robot make-tea task.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (Approach)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** 기존 VLA는 로봇 조작 중 자주 실패하며 원인 진단에는 전문가 지식과 수작업이 필요하다. (p. 1, 1. Introduction).
- **Actual contribution:** Our main contributions are summarized as follows: • VLA-FixBench, a robotic manipulation fault evaluation dataset comprising 6k failure cases covering perception, control, and cognition errors, with fine-grained annotations of sub-task ... (p. 2, 1. Introduction).
- **Evaluation boundary:** Experimental results validate this choice: even with this minimal interface, human-in-theloop corrections yield 13% improvement in simulation and 35% on real robots, and precise rollback outperforms coarse task restarts, demonstrating ... (p. 5, 4.2. Dynamic Evaluation).
- **Explicit failure boundary:** GPT-5-2 achieves the highest sensitivity (Recall: 0.8571, F2-Score: 0.7143), but its high FPR (0.7568) causes task failure (SR: 0), indicating that oversensitive diagnosis can disrupt nominal executions. (p. 8, 5.4. Real-Time Evaluation Results).
