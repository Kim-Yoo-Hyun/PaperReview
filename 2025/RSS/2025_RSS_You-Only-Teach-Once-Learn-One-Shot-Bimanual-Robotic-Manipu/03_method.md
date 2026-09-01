# Method - You Only Teach Once: Learn One-Shot Bimanual Robotic Manipulation from Video Demonstrations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (22 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p149.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p149.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 17 (A. Implementation Details of Our BiDP), p. 17 (A. Implementation Details of Our BiDP), p. 4 (B. Hand Motion Extraction and Injection), p. 4 (B. Hand Motion Extraction and Injection), p. 5 (B. Hand Motion Extraction and Injection), p. 5 (B. Hand Motion Extraction and Injection)): 2) Network architecture: In all tasks, we use a SIM(3)- equivariant PointNet++ (96, 95] with 4 layers and hidden dimensionality 128 as the ‘feature encoder.

## Method Body Digest

- **p. 17 / A. Implementation Details of Our BiDP - extractive body cue:** 2) Network architecture: In all tasks, we use a SIM(3)- equivariant PointNet++ (96, 95] with 4 layers and hidden dimensionality 128 as the ‘feature encoder.
- **p. 17 / A. Implementation Details of Our BiDP - extractive body cue:** For the noise prediction network, we inherits hyperparameters from the ‘original Diffusion Policy [15], Specifically, to optimize for inference speed in all experiments, we use ...
- **p. 4 / B. Hand Motion Extraction and Injection - extractive body cue:** As an altemative, we propose to project all 3D points {f!"°}/_, onto the 2D image, nd then lft these points to 3D by applying the ...
- **p. 4 / B. Hand Motion Extraction and Injection - extractive body cue:** Then, we leverage favourable vision techniques to extract rich manipulation features from recorded videos by a single binocular ‘camera, Extracted features will be post-processed to ...
- **p. 5 / B. Hand Motion Extraction and Injection - extractive body cue:** Additionally, we adopt cutting-edge vision algorithms (in- ‘cluding the vision-language model Florence-2 [90] and SAM2.
- **p. 5 / B. Hand Motion Extraction and Injection - extractive body cue:** Accordingly, we can just learn to predict the next best keyframe, and use a sampling-based motion planner to reach it during inference We thus simplify ...
- **p. 4 / A. Problem Formulation - extractive body cue:** The learning objective can be simply ‘concluded as maximum likelihood observation-conditioned, imitation objective to learn the policy =:
- **p. 17 / A. Implementation Details of Our BiDP - extractive body cue:** In particular, wwe have tried increasing the number of point clouds to 2088 or ‘more, but the evaluation improvement in each task is minimal, and ...

## Design Rationale

- **p. 4 / B. Hand Motion Extraction and Injection - extractive body cue:** As an altemative, we propose to project all 3D points {f!"°}/_, onto the 2D image, nd then lft these points to 3D by applying the ...
- **p. 4 / A. Problem Formulation - extractive body cue:** Next, we present how to obtain sufficient training demonstrations proliferated from only a single-shot human teaching and how to improve existing diffusion-based imitation policies for ...
- **p. 17 / A. Implementation Details of Our BiDP - extractive body cue:** 1) Spaces of observation and action: We adopt a 13 ‘dimensional proprioception vector and a 7-dimensional action, space for each robot arm, respectively. ‘The proprioception ...

## Source Evidence Cues

- **p. 17 / A. Implementation Details of Our BiDP - extractive body cue:** 2) Network architecture: In all tasks, we use a SIM(3)- equivariant PointNet++ (96, 95] with 4 layers and hidden dimensionality 128 as the ‘feature encoder.
- **p. 17 / A. Implementation Details of Our BiDP - extractive body cue:** For the noise prediction network, we inherits hyperparameters from the ‘original Diffusion Policy [15], Specifically, to optimize for inference speed in all experiments, we use ...
- **p. 4 / B. Hand Motion Extraction and Injection - extractive body cue:** As an altemative, we propose to project all 3D points {f!"°}/_, onto the 2D image, nd then lft these points to 3D by applying the ...
- **p. 4 / B. Hand Motion Extraction and Injection - extractive body cue:** Then, we leverage favourable vision techniques to extract rich manipulation features from recorded videos by a single binocular ‘camera, Extracted features will be post-processed to ...
- **p. 5 / B. Hand Motion Extraction and Injection - extractive body cue:** Additionally, we adopt cutting-edge vision algorithms (in- ‘cluding the vision-language model Florence-2 [90] and SAM2.
- **p. 5 / B. Hand Motion Extraction and Injection - extractive body cue:** Accordingly, we can just learn to predict the next best keyframe, and use a sampling-based motion planner to reach it during inference We thus simplify ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Demonstration representation | expert trajectory를 training pair/context로 정렬한다 | observation history, goal, expert action | temporal alignment, relabeling 또는 latent context construction을 수행 | training sample/context | 2) Network architecture: In all tasks, we use a SIM(3)- equivariant PointNet++ (96, 95] with 4 layers and hidden dimensionality 128 as ... | p. 17 (A. Implementation Details of Our BiDP), p. 17 (A. Implementation Details of Our BiDP) |
| Policy fitting | expert action distribution을 학습한다 | context와 action target | behavior cloning, adversarial, sequence, diffusion 또는 flow objective를 최적화 | policy/action distribution | For the noise prediction network, we inherits hyperparameters from the ‘original Diffusion Policy [15], Specifically, to optimize for inference speed in all ... | p. 17 (A. Implementation Details of Our BiDP), p. 4 (B. Hand Motion Extraction and Injection) |
| Closed-loop rollout | distribution shift와 recovery를 확인한다 | current observation/history | action/chunk을 실행하고 feedback으로 다음 prediction을 갱신 | trajectory/failure signal | As an altemative, we propose to project all 3D points {f!"°}/_, onto the 2D image, nd then lft these points to 3D ... | p. 4 (B. Hand Motion Extraction and Injection), p. 4 (B. Hand Motion Extraction and Injection) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / A. Problem Formulation - extractive body cue:** The learning objective can be simply ‘concluded as maximum likelihood observation-conditioned, imitation objective to learn the policy =:
- **p. 17 / A. Implementation Details of Our BiDP - extractive body cue:** In particular, wwe have tried increasing the number of point clouds to 2088 or ‘more, but the evaluation improvement in each task is minimal, and ...
- **p. 17 / A. Implementation Details of Our BiDP - extractive body cue:** In addition, we have explained and demonstrated the importance and advantages of object-centric point cloud input in our main paper.
- **Formal bridge:** observation history o_{t−H:t} -> expert-like action/chunk a_{t:t+H} -> imitation or action-distribution loss -> closed-loop task success and robustness.
- **Equation/algorithm anchors:** p. 4 (A. Problem Formulation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | bimanual, tasks, observation, horizon, only, initial, state, left, network, inputs, action, space, includes, target | observation history와 expert trajectory/action | body cue; exact tensor/frame verify |
| State/latent | bimanual, tasks, observation, horizon, only, initial, state, left, network, inputs | behavior policy와 temporal action context | body cue; notation verify |
| Action/output | altemative, project, points, onto, image, then, applying, stereo, matching, algorithm | predicted action 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | learning, objective, simply, concluded, maximum, likelihood, observation-conditioned, imitation, learn, policy | imitation or action-distribution loss | equation anchor required |

## Observation–State–Action Interface

- **p. 17 / A. Implementation Details of Our BiDP - extractive body cue:** For all our bimanual tasks, the observation horizon is set to 1, so we only use the initial state observation of the left arm as ...
- **p. 4 / A. Problem Formulation - extractive body cue:** As for the action space A= {a? & R¥,a" © SO(3),a & {0,1}}. it includes the target 6-DoF pose of each robot arm and the ...
- **p. 4 / A. Problem Formulation - extractive body cue:** In this paper, we mainly consider bimanual robot manipula tion tasks, where the agent (e.g., dual manipulators equipped with parallel-jaw grippers) does not have access ...
- **p. 17 / A. Implementation Details of Our BiDP - extractive body cue:** 1) Spaces of observation and action: We adopt a 13 ‘dimensional proprioception vector and a 7-dimensional action, space for each robot arm, respectively. ‘The proprioception ...
- **p. 5 / B. Hand Motion Extraction and Injection - extractive body cue:** (73}) to extract segmented manipulated objects from the left initial image as our disturbance-free visual observations O, which will be further lifted to 3D point ...
- **p. 5 / B. Hand Motion Extraction and Injection - extractive body cue:** Specifically, we inherit the abstraction of a consequent demonstration into discrete keyframes (a.k.a. keyposes) as in C2FARM [38] and PerAct (80).
- **Normalized interface:** observation=observation history와 expert trajectory/action; state=behavior policy와 temporal action context; output/action=predicted action 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single-step 또는 action chunk/trajectory horizon; exact chunk length는 exact value not recovered from the selected body cues. | For a more detailed comparison, we report the average length (following CLAVIN [59]) in each substep for a sequenced long-horizon task, where ... | episode/sequence/action-chunk boundary |
| Rate / latency | training inference와 deployed control tick을 분리; action chunk면 receding execution 여부 확인. | For the number of the action steps, which is also the length of the predicted horizon, we simplify it and set the ... | Hz/fps, inference time and control rate |
| Memory | current observation, temporal history 또는 recurrent/sequence context. | not recovered | window and reset |
| Compute | backbone/decoder inference, sampling steps와 action horizon이 latency를 결정한다. | 4) Metries: We train all methods for 500 or 1,000 epochs and only save the last checkpoint for testing. | hardware, batch and throughput |

## Training vs Inference

- **p. 17 / A. Implementation Details of Our BiDP - extractive body cue:** For the noise prediction network, we inherits hyperparameters from the ‘original Diffusion Policy [15], Specifically, to optimize for inference speed in all experiments, we use ...
- **p. 5 / B. Hand Motion Extraction and Injection - extractive body cue:** Accordingly, we can just learn to predict the next best keyframe, and use a sampling-based motion planner to reach it during inference We thus simplify ...
- **p. 8 / A. Experiment Setups - extractive body cue:** 4) Metries: We train all methods for 500 or 1,000 epochs and only save the last checkpoint for testing.
- **p. 17 / A. Implementation Details of Our BiDP - extractive body cue:** For the noise prediction network, we inherits hyperparameters from the ‘original Diffusion Policy [15], Specifically, to optimize for inference speed in all experiments, we use ...
- **p. 17 / A. Implementation Details of Our BiDP - extractive body cue:** At inference time, we also need to preprocess the binocular RGB observations to obtain the point cloud of manipulated objects.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Network, architecture, tasks, SIM, equivariant, PointNet, layers, hidden, dimensionality, feature, encoder, noise, prediction, inherits, hyperparameters, original, Diffusion, Policy, Specifically, optimize.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Demonstration representation | We then processed these data into the form suitable for BiDP, including extracting 3D point clouds of manipulated objects and saving the ... | p. 8 (A. Experiment Setups), p. 7 (A. Experiment Setups) |
| Policy fitting | also makes our model more robust compared to all baselines The core idea here is to rely on the still rapidly developing ... | p. 11 (B. Results Comparison), p. 8 (A. Experiment Setups) |
| Closed-loop rollout | ong-horizon bimanual manipulation tasks, the existing stateof-the-art methods still have a lot of room for improvement, such as the gradually decaying effect ... | p. 10 (B. Results Comparison), p. 9 (B. Results Comparison) |

## Failure and Ablation Link

- **p. 9 / B. Results Comparison - extractive body cue:** Il, ‘we quantitatively illustrate the effectiveness of each strategy cone by one through many ablation studies.
- **p. 9 / B. Results Comparison - extractive body cue:** First, the method (id-1) without any proposed strategy can be regarded as the vanilla EquiBot [95], which takes the entire point cloud scene as observation, ...
- **p. 8 / A. Experiment Setups - extractive body cue:** It is a variant of diffusion policy with a simpler point cloud encoder.
- **p. 8 / A. Experiment Setups - extractive body cue:** 6: Ablation studies on expanded training data at different scales using geometric transformations.
- **p. 10 / B. Results Comparison - extractive body cue:** Comparing to EquiBot, our BiDP still has a clear advantage, thanks to the fact that we use explicit 3D geometric transformations for expanding the training ...
- **p. 17 / A. Implementation Details of Our BiDP - extractive body cue:** Therefore, reducing the number of points to 1024 ‘can make training faster without hurting performance.
- **p. 17 / A. Implementation Details of Our BiDP - extractive body cue:** 2) Network architecture: In all tasks, we use a SIM(3)- equivariant PointNet++ (96, 95] with 4 layers and hidden dimensionality 128 as the ‘feature encoder.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 17 (A. Implementation Details of Our BiDP), p. 17 (A. Implementation Details of Our BiDP), p. 4 (B. Hand Motion Extraction and Injection), p. 4 (B. Hand Motion Extraction and Injection), p. 5 (B. Hand Motion Extraction and Injection), p. 5 (B. Hand Motion Extraction and Injection), objective p. 4 (A. Problem Formulation), p. 17 (A. Implementation Details of Our BiDP), p. 17 (A. Implementation Details of Our BiDP), temporal p. 8 (A. Experiment Setups), p. 17 (A. Implementation Details of Our BiDP), p. 7 (A. Experiment Setups), p. 7 (A. Experiment Setups), p. 8 (A. Experiment Setups), p. 17 (A. Implementation Details of Our BiDP).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
