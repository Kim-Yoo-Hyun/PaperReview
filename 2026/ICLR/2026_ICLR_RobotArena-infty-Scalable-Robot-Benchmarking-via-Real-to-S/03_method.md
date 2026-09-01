# Method - RobotArena $\infty$: Scalable Robot Benchmarking via Real-to-Sim Translation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=OutljIofvS; PDF retrieval source: https://openreview.net/pdf/4355de50de1431de9a4ef52786c9b5f7f9f124fe.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (ABSTRACT)): First, vision-language-action (VLA) models are highly sensitive to dataset differences: performance drops when they are tested in environments outside their training distribution, indicating that current models are not true generalists ...

## Method Body Digest

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** First, vision-language-action (VLA) models are highly sensitive to dataset differences: performance drops when they are tested in environments outside their training distribution, indicating that current ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** We introduce a fully automated reality-to-simulation translation pipeline built upon VLMs, 2D-to-3D generative models and differentiable rendering.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** We first automatically translate real videos into corresponding simulation environments, building upon recent advances in vision-language models for scene understanding, 2D-to-3D generative models for asset ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Such manual oversight also raises concerns about consistency and fairness, particularly when baselines and new models are compared under slightly different conditions.
- **p. 1 / ABSTRACT - extractive PDF cue:** To measure robustness, we systematically perturb simulated environments along multiple axes, including textures and object placements, stress-testing policy generalization under controlled variation.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** However, the high cost for both organizers and participants means such events occur infrequently, often no more than once a year.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** BEHAVIOR boasts an impressive manual effort of asset and environment creation, while SIMPLER reconstructs four real-world Bridge scenes and includes hand-designed reward functions.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** While recent years have witnessed substantial progress in developing more capable and general robot policies, their evaluation remains a persistent challenge and lacks standardization.

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** RobotArena ∞: We introduce RobotArena ∞, a new benchmarking framework that scales robot evaluation by deploying policies in automatically constructed simulated environments and assessing them ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** We present key evaluation results that reveal how current robot policies generalize-or fail to-under distribution shifts.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** We introduce a fully automated reality-to-simulation translation pipeline built upon VLMs, 2D-to-3D generative models and differentiable rendering.

## Source Evidence Cues

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** First, vision-language-action (VLA) models are highly sensitive to dataset differences: performance drops when they are tested in environments outside their training distribution, indicating that current ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** We introduce a fully automated reality-to-simulation translation pipeline built upon VLMs, 2D-to-3D generative models and differentiable rendering.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** We first automatically translate real videos into corresponding simulation environments, building upon recent advances in vision-language models for scene understanding, 2D-to-3D generative models for asset ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Such manual oversight also raises concerns about consistency and fairness, particularly when baselines and new models are compared under slightly different conditions.
- **p. 1 / ABSTRACT - extractive PDF cue:** To measure robustness, we systematically perturb simulated environments along multiple axes, including textures and object placements, stress-testing policy generalization under controlled variation.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | First, vision-language-action (VLA) models are highly sensitive to dataset differences: performance drops when they are tested in environments outside their training distribution, ... | p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | We introduce a fully automated reality-to-simulation translation pipeline built upon VLMs, 2D-to-3D generative models and differentiable rendering. | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | We first automatically translate real videos into corresponding simulation environments, building upon recent advances in vision-language models for scene understanding, 2D-to-3D generative ... | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** However, the high cost for both organizers and participants means such events occur infrequently, often no more than once a year.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** BEHAVIOR boasts an impressive manual effort of asset and environment creation, while SIMPLER reconstructs four real-world Bridge scenes and includes hand-designed reward functions.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** While recent years have witnessed substantial progress in developing more capable and general robot policies, their evaluation remains a persistent challenge and lacks standardization.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** We then deploy VLAs in these environments and evaluate their execution trajectories using two complementary strategies: (1) absolute evaluation, in which prompted VLMs or crowdsourced ...
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | First, vision-language-action, VLA, models, highly, sensitive, dataset, differences, performance, drops, when, they, tested, environments | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | First, vision-language-action, VLA, models, highly, sensitive, dataset, differences, performance, drops | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | RobotArena, introduce, benchmarking, framework, scales, robot, evaluation, deploying, policies, automatically | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | However, high, cost, organizers, participants, means, events, occur, infrequently, often | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** First, vision-language-action (VLA) models are highly sensitive to dataset differences: performance drops when they are tested in environments outside their training distribution, indicating that current ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Published as a conference paper at ICLR 2026 Robotic Datasets Bridge V2 Make the cup lie down " Put the tomato in the pot " ...
- **p. 1 / ABSTRACT - extractive PDF cue:** We introduce RobotArena ∞, a new benchmarking framework that overcomes these challenges by shifting VLA evaluation into large-scale simulated environments augmented with online human feedback.
- **p. 1 / ABSTRACT - extractive PDF cue:** To measure robustness, we systematically perturb simulated environments along multiple axes, including textures and object placements, stress-testing policy generalization under controlled variation.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** We present a scalable and extensible benchmarking protocol for robotics, by coupling physics engines, real-to-sim translation and human preference feedback.
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | We introduce RobotArena ∞, a new benchmarking framework that overcomes these challenges by shifting VLA evaluation into large-scale simulated environments augmented with ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | RobotArena ∞: We introduce RobotArena ∞, a new benchmarking framework that scales robot evaluation by deploying policies in automatically constructed simulated environments ... | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | (2024), and (iii) a feature loss aligning DINOv2 embeddings between rendered and observed frames, shown in Figure 3 Step 2. | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** First, vision-language-action (VLA) models are highly sensitive to dataset differences: performance drops when they are tested in environments outside their training distribution, indicating that current ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** We measure both in-distribution performance by testing on simulation environments seeded from training videos in established datasets such as Bridge Walke et al.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** First, vision-language-action, VLA, models, highly, sensitive, dataset, differences, performance, drops, when, they, tested, environments, outside, training, distribution, indicating, current, true.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | Published as a conference paper at ICLR 2026 Robotic Datasets Bridge V2 Make the cup lie down " Put the tomato in ... | p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT) |
| Baseline harness | Such manual oversight also raises concerns about consistency and fairness, particularly when baselines and new models are compared under slightly different conditions. | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Metric / failure reporting | Figure 9: Policy evaluation results in RobotArena ∞ versus SIMPLER of Li et al. (2024c). 5.3 ROBOTARENA ∞VERSUS SIMPLER OF LI ET ... | p. 9 (Figure/Table caption), p. 6 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** Our benchmark is not without limitations.
- **p. 21 / Figure/Table caption - extractive PDF cue:** Figure 14: Background Change Example. The top-left image shows the original image without background perturbations.
- **p. 21 / Figure/Table caption - extractive PDF cue:** Figure 15: Color Shift Example. The leftmost image shows the original image without color perturbations. color vector [R, G , B ], we compute: C'( ...
- **p. 22 / Figure/Table caption - extractive PDF cue:** Figure 16: Object Position Perturbation Example. The top-left image shows the original setup without perturbation.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 7: Policy evaluation results obtained from VLMs (a) in all RobotArena ∞environments and (b) in perturbations of BridgeSim environments. 5. X-VLA Zheng et al. ...
- **p. 6 / 2 RELATED WORK - extractive PDF cue:** Intuitively, this focuses evaluation on the terminal phase of execution, where task completion (or failure) is most evident.
- **p. 24 / Figure/Table caption - extractive PDF cue:** Figure 19: Example VLM-generated task evaluation curves on perturbed environments. Top: A successful pick-and-place execution-after the object lift the VLM score climbs steadily and correctly ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (ABSTRACT), objective p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), temporal p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 5 (2 RELATED WORK), p. 6 (2 RELATED WORK), p. 6 (2 RELATED WORK), p. 1 (1 INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
