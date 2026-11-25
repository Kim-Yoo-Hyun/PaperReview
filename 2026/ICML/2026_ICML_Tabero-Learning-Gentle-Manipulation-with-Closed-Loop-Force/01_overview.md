# Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2605.27886.
> PDF retrieval source: https://arxiv.org/pdf/2605.27886. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: Qiwei Wu, Rui Zhang, Xin Xiang, Tao Li, Weihua Zhang, Junjie Lai, Renjing Xu
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: VLA, tactile, force feedback, contact-rich manipulation, Benchmark, dexterity, language-conditioned manipulation
- Official paper: https://arxiv.org/abs/2605.27886
- Full-text retrieval: https://arxiv.org/pdf/2605.27886
- Code/Project: https://github.com/NathanWu7/Tabero
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Tabero는 촉각과 언어 지시로 조작 힘을 조절하는 정책을 평가하기 위해 작업 성공과 접촉 품질을 함께 측정한다. [PDF 1쪽](https://arxiv.org/pdf/2605.27886v1#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Tactile sensing is essential for robots to achieve human-like gentle manipulation.
- **p. 1 / Abstract - extractive body cue:** However, existing Vision-Language-Action (VLA) models struggle to exploit tactile feedback for gentle manipulation due to scarce aligned vision-tactile-language data and the lack of effective closed-loop ...
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we introduce Tabero, a benchmark and model suite for gentle, language-conditioned robotic manipulation that demands fine-grained contact force perception.
- **p. 1 / Abstract - extractive body cue:** First, the Tabero benchmark addresses the scarcity of tactile data by presenting a data-efficient pipeline that repurposes open-source robot manipulation trajectories to generate diverse vision-tactile-language ...
- **p. 1 / Abstract - extractive body cue:** Second, we propose Tabero-VTLA, an architecture with a decoupled force-position command interface; the resulting force-position commands are executed by a fixed hybrid controller to enable ...
- **p. 1 / 1. Introduction - extractive body cue:** Training such models, however, faces two major challenges.
- **p. 1 / 1. Introduction - extractive body cue:** Simulation offers a scalable alternative, yet existing pipelines focus on visual diversity and lack efficient mechanisms to generate and integrate high-fidelity tactile signals.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our work makes the following contributions: The Tabero benchmark, which enables scalable visiontactile-language data generation by replaying open-source trajectories in a high-fidelity tactile ...
- **p. 4 / 3.4. Tabero-VTLA - extractive body cue:** Building on the Pi0 infrastructure and leveraging flow matching, our approach enables continuous prediction of both pose and force.
- **p. 1 / 1. Introduction - extractive body cue:** To enable language-conditioned gentle manipulation, we introduce Tabero (Fig.
- **p. 2 / 1. Introduction - extractive body cue:** Tabero: We present a high-fidelity multimodal simulation platform integrating Isaac Lab with advanced tactile simulation.
- **p. 4 / 3.4. Tabero-VTLA - extractive body cue:** To integrate this tactile signal into the VLA foundation model, we introduce a tactile tokenizer that maps tactile inputs into conditional tokens.
- **p. 4 / 3.4. Tabero-VTLA - extractive body cue:** Although these fingertip forces can be decomposed to recover the full 6D interaction wrench on the object, we find it more effective to directly feed ...
- **p. 4 / 3.4. Tabero-VTLA - extractive body cue:** Its features then interact with visual features via cross-attention in the transformer, enabling joint reasoning over contact history and scene geometry.
- **p. 6 / 3.6. Metrics Beyond Success Rate - extractive body cue:** To address this limitation, we introduce a set of processaware metrics that quantify the quality of physical interaction during task execution: Maximum Transient Grip Force ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Real-Time Force Feedback System VTLA System VIT Paligemma Action Expert Robot States Force-aware Instruction Marker Motion Field? | standardized observation, action, task state와 evaluation split | p. 5 (3.5. Decoupled Force-Position Hybrid Controller), p. 4 (3.2. Cross-Modal Data Acquisition) |
| State/latent | Real-Time, Force, Feedback, System, VTLA, VIT, Paligemma, Action, Expert, Robot, States, Force-aware | benchmark state/goal와 method decision | p. 5 (3.5. Decoupled Force-Position Hybrid Controller), p. 4 (3.2. Cross-Modal Data Acquisition), p. 5 (3.5. Decoupled Force-Position Hybrid Controller) |
| Output/action | All cameras are rendered in parallel using tiled rendering, and all modalities, including visual, tactile, force, language instructions, and executed actions, are sampled synchronously at 20 Hz to produce temporally aligned multimodal ... | policy/controller trajectory 또는 measured result | p. 4 (3.2. Cross-Modal Data Acquisition), p. 5 (3.5. Decoupled Force-Position Hybrid Controller), p. 2 (1. Introduction) |
| Objective/outcome | To address this issue, we align the tool center point (TCP) of the end-effector by adjusting the base pose of the robot arm and use a high-gain PD joint controller during trajectory ... | success metric, robustness, generalization과 reproducibility | p. 3 (3.1. Cross-Platform Data Reutilization), p. 4 (3.4. Tabero-VTLA), p. 5 (3.4. Tabero-VTLA) |

## Main Claims and Actual Contribution

- 기존 조작 궤적을 재활용해 시각·촉각·언어 자료를 만들고, 정책의 힘·위치 명령을 고정된 하이브리드 제어기로 실행한다. [PDF 3쪽](https://arxiv.org/pdf/2605.27886v1#page=3) · [PDF 5쪽](https://arxiv.org/pdf/2605.27886v1#page=5)
- 부드럽게 잡으라는 지시에서 평균 파지력을 낮추면서 작업을 수행하는지 평가하고 촉각 입력의 영향을 비교했다. [PDF 7쪽](https://arxiv.org/pdf/2605.27886v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2605.27886v1#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 8 (4.4. Ablation and Comparison of VTLA), p. 8 (4.4. Ablation and Comparison of VTLA) |
| Embodiment/environment | Specifically, we select four subtasks from the LIBERO benchmark suite and compare the success rates of the original MuJoCo-based dataset with those of our replayed version in Isaac Lab. | hardware/simulator version and reset protocol | p. 6 (4.1. Cross-Platform Data Validation), p. 6 (4.1. Cross-Platform Data Validation) |
| Dataset/benchmark | This subset includes 9 tasks from the Object dataset, each executed under two force conditions specified by linguistic adverbs. | role, split, size and leakage | p. 6 (4.1. Cross-Platform Data Validation), p. 6 (4.1. Cross-Platform Data Validation), p. 7 (4.2. Tactile Data Diversity Analysis), p. 7 (4.2. Tactile Data Diversity Analysis) |
| Metric | Cross-platform data validation: Task success rates across four LIBERO subtasks. | definition, denominator, direction and uncertainty | p. 6 (4.1. Cross-Platform Data Validation), p. 6 (4.1. Cross-Platform Data Validation), p. 7 (4.2. Tactile Data Diversity Analysis) |
| Baseline/ablation | We compare a baseline using binary gripper control against our approach, which explicitly sets different force parameters during execution, the results are shown in fig. | fair input/data/compute/action matching | p. 6 (4.2. Tactile Data Diversity Analysis), p. 6 (4.1. Cross-Platform Data Validation), p. 7 (4.3. Effectiveness of Hybrid Controller) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.2. Tactile Data Diversity Analysis - extractive body cue:** 2, removing tactile feedback leads to complete failure in force modulation, highlighting its critical role in gentle manipulation.
- **p. 8 / 5. Conclusions - extractive body cue:** Future work could explore reinforcement learning to balance these objectives.
- **p. 8 / 5. Conclusions - extractive body cue:** Nevertheless, Our current framework does not jointly optimize for both task success and minimal interaction force.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Tabero Simulation Platform. Tabero replicates the LIBERO task environments, enables data reuse, enhances the visual fidelity of simulated data, and makes it possible ...
- **p. 7 / 4.2. Tactile Data Diversity Analysis - extractive body cue:** Dataset B also employs continuous control but reduces the force to 10%, representing an extreme low-force regime where slippage is likely.
- **p. 6 / 4.1. Cross-Platform Data Validation - extractive body cue:** This degradation is especially pronounced in tasks requiring delicate manipulation, where lower grip forces strongly correlate with reduced success.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.4. Tabero-VTLA), p. 6 (3.6. Metrics Beyond Success Rate)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Training such models, however, faces two major challenges. (p. 1, 1. Introduction).
- **Actual contribution:** In summary, our work makes the following contributions: The Tabero benchmark, which enables scalable visiontactile-language data generation by replaying open-source trajectories in a high-fidelity tactile simulator and establishes the f ... (p. 2, 1. Introduction).
- **Evaluation boundary:** When using the same robot kinematics and control policy as in the original dataset, our baseline configuration yields a success rate distribution that closely matches that reported in OpenVLA (Kim ... (p. 6, 4.1. Cross-Platform Data Validation).
- **Explicit failure boundary:** 2, removing tactile feedback leads to complete failure in force modulation, highlighting its critical role in gentle manipulation. (p. 7, 4.2. Tactile Data Diversity Analysis).

## 원문과 공개 자료

- 코드 · 환경 및 폐루프 추론 클라이언트 구현으로 학습 코드는 저자가 별도 저장소에서 제공한다 · benchmarks/common/closedloop_policy_inference.py [배포 파일](https://raw.githubusercontent.com/NathanWu7/Tabero/07e01d15369399a09f9898957d4a59e953be97ca/benchmarks/common/closedloop_policy_inference.py)
- 가중치 · Tabero의 힘·촉각 미세조정 정책 파라미터 · checkpoints/pi0_lora_tacfield_tabero/pi0_lora_tacfield_tabero/49999/params/ocdbt.process_0/d/03217ea9a027e1e4e2ba8c1cd897539a [배포 파일](https://huggingface.co/NathanWu7/pi0_lora_tacfield_tabero/blob/1ce3438ce5f290da65aff286935ecf97e9ea4046/checkpoints/pi0_lora_tacfield_tabero/pi0_lora_tacfield_tabero/49999/params/ocdbt.process_0/d/03217ea9a027e1e4e2ba8c1cd897539a)
- 데이터 · Isaac Lab으로 옮긴 LIBERO 단일 과제 시연 HDF5 · assembled_hdf5/libero_10_task0_LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket_demo.hdf5 [배포 파일](https://huggingface.co/datasets/NathanWu7/Isaaclab_Libero/blob/fe6263d3ff1f600f123522e298d6d755bc827d33/assembled_hdf5/libero_10_task0_LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket_demo.hdf5)
