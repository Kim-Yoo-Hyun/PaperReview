# Method - ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (30 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v270/huang25g.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v270/main/assets/huang25g/huang25g.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3 Method), p. 24 (A.8 Implementation Details of Sub-Goal Solver), p. 22 (A.6 Querying Vision-Language Model), p. 4 (3 Method), p. 5 (3 Method), p. 22 (A.6 Querying Vision-Language Model)): 3.4 Keypoint Proposal and ReKep Generation To enable the system to perform tasks in-the-wild given a free-form task instruction, we devise a pipeline using large vision models and vision-language models ...

## Method Body Digest

- **p. 5 / 3 Method - extractive body cue:** 3.4 Keypoint Proposal and ReKep Generation To enable the system to perform tasks in-the-wild given a free-form task instruction, we devise a pipeline using large ...
- **p. 24 / A.8 Implementation Details of Sub-Goal Solver - extractive body cue:** We use sampling-based global optimization Dual Annealing [129] in the first iteration to quickly search the full space, which is followed by a gradient-based local ...
- **p. 22 / A.6 Querying Vision-Language Model - extractive body cue:** For the experiments conducted in this work, we use GPT-4o [6] as it is one of the latest available models at the time of the ...
- **p. 4 / 3 Method - extractive body cue:** Constrained Optimization Solver RGB-D Observation Optimized Actions def subgoal_stage1_f1(k): dist = norm(k[0]-k[1]) return dist def path_stage2_f1(k): z_diff = k[1][2]-k[2][2] return abs(z_diff) def subgoal_stage2_f1(k): k[3][2] += ...
- **p. 5 / 3 Method - extractive body cue:** Then we perform bilinear interpolation to upsample the features to the original image size, Finterp ∈Rh×w×d.
- **p. 22 / A.6 Querying Vision-Language Model - extractive body cue:** Then the image and the task instruction are fed into a vision-language model with the prompt described below.
- **p. 3 / 3 Method - extractive body cue:** (3) What is our algorithmic instantiation that can efficiently solve the optimization in real-time (Sec.
- **p. 4 / 3 Method - extractive body cue:** Namely, for each stage i, the optimization shall find an end-effector pose as next sub-goal, along with its timing, and a sequence of poses egi-1:gi ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are summarized as follows: 1) We formulate manipulation tasks as a hierarchical optimization problem with Relational Keypoint Constraints; 2) We devise a pipeline ...
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we propose Relational Keypoint Constraints (ReKep).
- **p. 4 / 3 Method - extractive body cue:** 2, which consists of three stages: grasp, align, and pour.

## Source Evidence Cues

- **p. 5 / 3 Method - extractive body cue:** 3.4 Keypoint Proposal and ReKep Generation To enable the system to perform tasks in-the-wild given a free-form task instruction, we devise a pipeline using large ...
- **p. 24 / A.8 Implementation Details of Sub-Goal Solver - extractive body cue:** We use sampling-based global optimization Dual Annealing [129] in the first iteration to quickly search the full space, which is followed by a gradient-based local ...
- **p. 22 / A.6 Querying Vision-Language Model - extractive body cue:** For the experiments conducted in this work, we use GPT-4o [6] as it is one of the latest available models at the time of the ...
- **p. 4 / 3 Method - extractive body cue:** Constrained Optimization Solver RGB-D Observation Optimized Actions def subgoal_stage1_f1(k): dist = norm(k[0]-k[1]) return dist def path_stage2_f1(k): z_diff = k[1][2]-k[2][2] return abs(z_diff) def subgoal_stage2_f1(k): k[3][2] += ...
- **p. 5 / 3 Method - extractive body cue:** Then we perform bilinear interpolation to upsample the features to the original image size, Finterp ∈Rh×w×d.
- **p. 22 / A.6 Querying Vision-Language Model - extractive body cue:** Then the image and the task instruction are fed into a vision-language model with the prompt described below.
- **p. 3 / 3 Method - extractive body cue:** (3) What is our algorithmic instantiation that can efficiently solve the optimization in real-time (Sec.
- **Detected method headings:** 3 Method (p. 3); A.4.2 Details on Baseline Methods (p. 21); A.6 Querying Vision-Language Model (p. 22)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | 3.4 Keypoint Proposal and ReKep Generation To enable the system to perform tasks in-the-wild given a free-form task instruction, we devise a ... | p. 5 (3 Method), p. 24 (A.8 Implementation Details of Sub-Goal Solver) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | We use sampling-based global optimization Dual Annealing [129] in the first iteration to quickly search the full space, which is followed by ... | p. 24 (A.8 Implementation Details of Sub-Goal Solver), p. 22 (A.6 Querying Vision-Language Model) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | For the experiments conducted in this work, we use GPT-4o [6] as it is one of the latest available models at the ... | p. 22 (A.6 Querying Vision-Language Model), p. 4 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3 Method - extractive body cue:** Namely, for each stage i, the optimization shall find an end-effector pose as next sub-goal, along with its timing, and a sequence of poses egi-1:gi ...
- **p. 24 / A.8 Implementation Details of Sub-Goal Solver - extractive body cue:** Constraint Violation: We implement constraints as cost terms in the optimization problem, where the returned costs by the ReKep functions are multiplied with large weights.
- **p. 4 / 3 Method - extractive body cue:** We denote the end-effector pose as e ∈SE(3).To perform the manipulation task, we aim to obtain the overall discrete-time trajectory e1:T by formulating the control ...
- **p. 3 / 3 Method - extractive body cue:** A single instance of ReKep is a function f : RK×3 →R that maps an array of keypoints, denoted as k, to an unbounded cost, ...
- **p. 5 / 3 Method - extractive body cue:** 2 attempts to find a sub-goal that satisfies Ci sub-goal while minimizing the auxiliary costs.
- **p. 5 / 3 Method - extractive body cue:** The Sub-Goal Problem: We first solve the sub-goal problem to obtain egi for the current stage i: arg min egi λ(i) sub-goal(egi) s.t. f(kgi) ≤0, ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 3 (3 Method), p. 3 (3 Method), p. 4 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 6 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | contributions, summarized, follows, formulate, manipulation, tasks, hierarchical, optimization, problem, Relational, Keypoint, Constraints, devise, pipeline | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | contributions, summarized, follows, formulate, manipulation, tasks, hierarchical, optimization, problem, Relational | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | contributions, summarized, follows, formulate, manipulation, tasks, hierarchical, optimization, problem, Relational | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Namely, stage, optimization, shall, find, end-effector, pose, next, sub-goal, along | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are summarized as follows: 1) We formulate manipulation tasks as a hierarchical optimization problem with Relational Keypoint Constraints; 2) We devise a pipeline ...
- **p. 3 / 3 Method - extractive body cue:** (4) How to automatically obtain ReKep from RGB-D observations and language instructions (Sec.
- **p. 4 / 3 Method - extractive body cue:** Constrained Optimization Solver RGB-D Observation Optimized Actions def subgoal_stage1_f1(k): dist = norm(k[0]-k[1]) return dist def path_stage2_f1(k): z_diff = k[1][2]-k[2][2] return abs(z_diff) def subgoal_stage2_f1(k): k[3][2] += ...
- **p. 22 / A.6 Querying Vision-Language Model - extractive body cue:** The prompt contains only generic instructions with no image-text in-context examples, although a few text-based examples are given to concretely explain the proposed method and ...
- **p. 2 / 1 Introduction - extractive body cue:** While constraints are typically defined manually per task [4], we demonstrate the specific form of ReKep possesses a unique advantage in that they can be ...
- **p. 4 / 3 Method - extractive body cue:** The image and an instruction are fed into GPT-4o [6] to generate a series of ReKep constraints as python programs that specify desired relations between ...
- **p. 5 / 3 Method - extractive body cue:** 3.4 Keypoint Proposal and ReKep Generation To enable the system to perform tasks in-the-wild given a free-form task instruction, we devise a pipeline using large ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Coupled with point trackers, we demonstrate that ReKep constraints can be repeatedly and efficiently solved in a hierarchical optimization framework to act ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | After initialization, at each time step, we similarly obtain the pixel-wise features from DINOv2 from all cameras with their 3D world coordinates. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Each setting has 10 trials, in which object poses are randomized. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3 Method - extractive body cue:** Constrained Optimization Solver RGB-D Observation Optimized Actions def subgoal_stage1_f1(k): dist = norm(k[0]-k[1]) return dist def path_stage2_f1(k): z_diff = k[1][2]-k[2][2] return abs(z_diff) def subgoal_stage2_f1(k): k[3][2] += ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Keypoint, Proposal, ReKep, Generation, enable, system, perform, tasks, in-the-wild, given, free-form, task, instruction, devise, pipeline, large, vision, models, vision-language, respectively.
- **Relevant PDF headings:** 3 Method (p. 3); A.4.2 Details on Baseline Methods (p. 21); A.6 Querying Vision-Language Model (p. 22).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | 5 Conclusion & Limitations In this work, we presented Relational Keypoint Constraints (ReKep), a structural task representation using constraints that operates on ... | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Action / skill decoding | Compared to baselines, ReKep can effectively handle core challenges of each task. | p. 7 (4 Experiments), p. 27 (A.12 Simulation Experiments) |
| Receding execution / feedback | Folding 0/10 4/10 7/10 Total (%) 10.0% 44.3% 68.6% Table 1: Success rate on wheeled singlearm and stationary bimanual platforms. | p. 7 (4 Experiments), p. 7 (4 Experiments) |

## Failure and Ablation Link

- **p. 7 / 4 Experiments - extractive body cue:** We evaluate two variants of the system: "Auto" uses foundation models to automatically generate ReKep, and "Annotated (Annot.)" uses human-annotated ReKep.
- **p. 8 / 4 Experiments - extractive body cue:** Results are shown on two robot platforms and on a variety of tasks featuring multi-stage, in-the-wild, bimanual, and reactive behaviors, all without task-specific data, additional ...
- **p. 27 / A.12 Simulation Experiments - extractive body cue:** Although the monolithic policy excels in training scenarios given its access to expert demonstrations, we observe that ReKep performs significantly stronger in unseen settings, and ...
- **p. 22 / A.5 Implementation Details of Keypoint Proposal - extractive body cue:** We find that applying PCA improves the clustering as it often removes details and artifacts related to texture that are not useful for our tasks.
- **p. 7 / 4 Experiments - extractive body cue:** (3) How do the individual components contribute to the failure cases of the system (Sec.
- **p. 8 / 4 Experiments - extractive body cue:** The optimization module, on the other hand, does not contribute as much to the failures despite given limited time budget, since there often exist many ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 7: Stationary Dual-Arm Platform. A.2 Wheeled Single-Arm Platform One of our investigated platform is a Franka arm mounted on a wheeled base built with ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3 Method), p. 24 (A.8 Implementation Details of Sub-Goal Solver), p. 22 (A.6 Querying Vision-Language Model), p. 4 (3 Method), p. 5 (3 Method), p. 22 (A.6 Querying Vision-Language Model), objective p. 4 (3 Method), p. 24 (A.8 Implementation Details of Sub-Goal Solver), p. 4 (3 Method), p. 3 (3 Method), p. 5 (3 Method), p. 5 (3 Method), temporal p. 8 (4 Experiments), p. 24 (A.7 Implementation Details of Point Tracker), p. 1 (Abstract), p. 2 (1 Introduction), p. 5 (3 Method), p. 8 (4 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (30 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Our contributions are summarized as follows: 1) We formulate manipulation tasks as a hierarchical optimization problem with Relational Keypoint Constraints; 2) We devise a pipeline to automatically specify keypoints and ... (p. 2, 1 Introduction).
- **Objective/update evidence:** Namely, for each stage i, the optimization shall find an end-effector pose as next sub-goal, along with its timing, and a sequence of poses egi-1:gi that achieves the sub-goal, subject ... (p. 4, 3 Method).
- **Temporal/runtime evidence:** Coupled with point trackers, we demonstrate that ReKep constraints can be repeatedly and efficiently solved in a hierarchical optimization framework to act as a closed-loop policy that runs at a ... (p. 8, 4 Experiments).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
