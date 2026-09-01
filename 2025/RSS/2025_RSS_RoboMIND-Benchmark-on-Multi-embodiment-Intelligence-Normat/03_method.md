# Method - RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (21 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p152.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p152.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 12 (C. Vision-Language-Action Large Models), p. 10 (B. Single-task Imitation Learning Models), p. 10 (B. Single-task Imitation Learning Models), p. 12 (C. Vision-Language-Action Large Models), p. 11 (B. Single-task Imitation Learning Models), p. 11 (B. Single-task Imitation Learning Models)): The first category consists of tasks similar to those performed by the single-arm Franka robot, which are intended to evaluate the model's performance across different robot types.

## Method Body Digest

- **p. 12 / C. Vision-Language-Action Large Models - extractive body cue:** The first category consists of tasks similar to those performed by the single-arm Franka robot, which are intended to evaluate the model's performance across different ...
- **p. 10 / B. Single-task Imitation Learning Models - extractive body cue:** In terms of the im tation learning algorithms, we used three well-known and commonly used methods: ACT [116], Diffusion Policy {17}, and BAKU [39].
- **p. 10 / B. Single-task Imitation Learning Models - extractive body cue:** Using the three algorithms, we trained the singletask model from scratch for each dataset.
- **p. 12 / C. Vision-Language-Action Large Models - extractive body cue:** It is noting that RoboMIND contains valuable data from diverse robots including the Tien Kung humanoid robots with dexterous hands, and we applied this dataset ...
- **p. 11 / B. Single-task Imitation Learning Models - extractive body cue:** 12: Success rates of ACT, Diffusion Policy, and BAKU on RoboMIND.
- **p. 11 / B. Single-task Imitation Learning Models - extractive body cue:** Each model was tested ten times, and the testers recorded the success or failure of each test and the reasons if there were any failures.
- **p. 11 / B. Single-task Imitation Learning Models - extractive body cue:** This discrepancy could be attributed to the hyper-parameter settings from the original BAKU paper, which is primarily optimized for simulation environments rather than real-world robotic ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** In contrast, recent works [73, 27, 28] incorporate visual observations as input to predict action poses.

## Design Rationale

- **p. 3 / I. INTRODUCTION - extractive body cue:** demonstrate that RoboMIND can be effectively utilized by various single-task imitation learning algorithms and suecessfully adapted t0 VLA large models. ‘The high-quality information provided by ...
- **p. 12 / C. Vision-Language-Action Large Models - extractive body cue:** The first category consists of tasks similar to those performed by the single-arm Franka robot, which are intended to evaluate the model's performance across different ...
- **p. 4 / I. INTRODUCTION - extractive body cue:** To support the development of such a large-scale dataset, we develop an intelligent data platform designed to collect, filter, and process the dataset efficiently. ‘This ...

## Source Evidence Cues

- **p. 12 / C. Vision-Language-Action Large Models - extractive body cue:** The first category consists of tasks similar to those performed by the single-arm Franka robot, which are intended to evaluate the model's performance across different ...
- **p. 10 / B. Single-task Imitation Learning Models - extractive body cue:** In terms of the im tation learning algorithms, we used three well-known and commonly used methods: ACT [116], Diffusion Policy {17}, and BAKU [39].
- **p. 10 / B. Single-task Imitation Learning Models - extractive body cue:** Using the three algorithms, we trained the singletask model from scratch for each dataset.
- **p. 12 / C. Vision-Language-Action Large Models - extractive body cue:** It is noting that RoboMIND contains valuable data from diverse robots including the Tien Kung humanoid robots with dexterous hands, and we applied this dataset ...
- **p. 11 / B. Single-task Imitation Learning Models - extractive body cue:** 12: Success rates of ACT, Diffusion Policy, and BAKU on RoboMIND.
- **p. 11 / B. Single-task Imitation Learning Models - extractive body cue:** Each model was tested ten times, and the testers recorded the success or failure of each test and the reasons if there were any failures.
- **Detected method headings:** B. Single-task Imitation Learning Models (p. 10); C. Vision-Language-Action Large Models (p. 12)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | The first category consists of tasks similar to those performed by the single-arm Franka robot, which are intended to evaluate the model's ... | p. 12 (C. Vision-Language-Action Large Models), p. 10 (B. Single-task Imitation Learning Models) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | In terms of the im tation learning algorithms, we used three well-known and commonly used methods: ACT [116], Diffusion Policy {17}, and ... | p. 10 (B. Single-task Imitation Learning Models), p. 10 (B. Single-task Imitation Learning Models) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | Using the three algorithms, we trained the singletask model from scratch for each dataset. | p. 10 (B. Single-task Imitation Learning Models), p. 12 (C. Vision-Language-Action Large Models) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 11 / B. Single-task Imitation Learning Models - extractive body cue:** This discrepancy could be attributed to the hyper-parameter settings from the original BAKU paper, which is primarily optimized for simulation environments rather than real-world robotic ...
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | contrast, recent, works, incorporate, visual, observations, input, predict, action, poses, Driven, advancements, diffusion-based, generative | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | contrast, recent, works, incorporate, visual, observations, input, predict, action, poses | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | demonstrate, RoboMIND, effectively, utilized, various, single-task, imitation, learning, algorithms, suecessfully | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | discrepancy, could, attributed, hyper-parameter, settings, original, BAKU, primarily, optimized, simulation | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / I. INTRODUCTION - extractive body cue:** In contrast, recent works [73, 27, 28] incorporate visual observations as input to predict action poses.
- **p. 3 / I. INTRODUCTION - extractive body cue:** Driven by advancements in diffusion-based generative models [41, 95, 89], diffusion policy [17] and subsequent works [82, 86, 105] focus on transforming random Gaussian noise ...
- **p. 4 / I. INTRODUCTION - extractive body cue:** Another prominent approach, VLA models, leverages multimodal instruction datasets (71, 62, 42] and robot data [9, 72, 91, 103] for co-training or pretraining, ‘enhancing the ...
- **p. 4 / I. INTRODUCTION - extractive body cue:** One series of works leverages egocentric human videos [36, 20, 21, 37] to assist in robot action leaming.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our dataset, called RoboMIND (Multi-embodiment Intelligence Normative Data for Robot manipulation), is aan extensive dataset that encompasses a broad range of robotic interactions and experiences.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Such diversity ensures that models learn to perform reliably under different conditions and environments [70, 77, 92, 14, 29, 97] Therefore, in this work, we ...
- **p. 10 / B. Single-task Imitation Learning Models - extractive body cue:** For Diffusion Policy, we followed the implementation in DROID [50].
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | We calculate the average task horizon (the number of time steps in one trajectory) for each embodiment, as shown in Figure 1(b). | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | In contrast, tasks from Tien Kung and AgileX have longer trajectories (over 500 time steps), better suited for longhorizon task training and ... | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | RoboMIND includes over 96 object categories from five usage scenarios, as shown in Figure 1(d), covering most daily life settings: domestic, industrial, ... | hardware, batch and throughput |

## Training vs Inference

- **p. 10 / B. Single-task Imitation Learning Models - extractive body cue:** Using the three algorithms, we trained the singletask model from scratch for each dataset.
- **p. 12 / C. Vision-Language-Action Large Models - extractive body cue:** It is noting that RoboMIND contains valuable data from diverse robots including the Tien Kung humanoid robots with dexterous hands, and we applied this dataset ...
- **p. 7 / A. Quantitative Analysis - extractive body cue:** In contrast, tasks from Tien Kung and AgileX have longer trajectories (over 500 time steps), better suited for longhorizon task training and skill composition, Since ...
- **p. 12 / C. Vision-Language-Action Large Models - extractive body cue:** Specifically, we took the official pre-trained VLA models and fine-tuned them on the multitask datasets for each type of robot, and evaluated their performance on ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** first, category, consists, tasks, similar, performed, single-arm, Franka, robot, intended, evaluate, model, performance, across, different, types, terms, tation, learning, algorithms.
- **Relevant PDF headings:** B. Single-task Imitation Learning Models (p. 10); C. Vision-Language-Action Large Models (p. 12).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | In addition to the diversity across robot, the varied task horizons in the dataset directly impact the temporal generalization capabilities of policies ... | p. 7 (A. Quantitative Analysis), p. 8 (B. Qualitative Analysis) |
| Baseline harness | 8: Comparison between Open X-Embodiment and RoboMIND. | p. 9 (B. Qualitative Analysis), p. 7 (A. Quantitative Analysis) |
| Metric / failure reporting | Fig. 12: Success rates of ACT, Diffusion Policy, and BAKU on RoboMIND. | p. 11 (Figure/Table caption), p. 15 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / A. Quantitative Analysis - extractive body cue:** The heterogeneous set of embodiment data collected under a unified standard can provide pretraining data for policy models with different action spaces (65, 51], as ...
- **p. 9 / B. Qualitative Analysis - extractive body cue:** In the failure ‘case, the arm fails to locate the correct slot position, causing the plate to slip out of the rack, likely due to ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 9: Visualization of failed data collection cases. We present two examples of failure from Franka and AgileX. In the FR-PlacePlateInP lateRack task (the second ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: We define 8 quality assurance criteria in the data collection process. Touch Excess: Unnecessary contact with objects by the robotic arm; Movement not ...
- **p. 8 / B. Qualitative Analysis - extractive body cue:** We also release Sk trajectories of the robot task failure cases.
- **p. 8 / B. Qualitative Analysis - extractive body cue:** The failure cases documented include scenarios where different types of humane operators filed to complete their assigned tasks, as well as in
- **p. 11 / B. Single-task Imitation Learning Models - extractive body cue:** Each model was tested ten times, and the testers recorded the success or failure of each test and the reasons if there were any failures.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 12 (C. Vision-Language-Action Large Models), p. 10 (B. Single-task Imitation Learning Models), p. 10 (B. Single-task Imitation Learning Models), p. 12 (C. Vision-Language-Action Large Models), p. 11 (B. Single-task Imitation Learning Models), p. 11 (B. Single-task Imitation Learning Models), objective p. 11 (B. Single-task Imitation Learning Models), temporal p. 7 (A. Quantitative Analysis), p. 7 (A. Quantitative Analysis), p. 1 (Front matter), p. 3 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 4 (I. INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
