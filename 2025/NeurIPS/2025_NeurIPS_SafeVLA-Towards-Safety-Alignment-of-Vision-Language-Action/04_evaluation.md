# Evaluation - SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (39 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=dt940loCBT; PDF retrieval source: https://openreview.net/pdf/050ee02bf65d6e2e7aa5ba14d172add1b64f86fa.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 9 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 36 (C.4 Experimental Environment and Costs), p. 7 (5 Experiments)): Figure 5: Comparative performance of VLA models on multiple benchmarks. Left: SR of each model per benchmark. Right: CC incurred by each model on these benchmarks. demonstrates substantial safety improvements, ...

## Evaluation Body Digest

- **p. 7 / 5 Experiments - extractive PDF cue:** 0.0 0.2 0.4 0.6 0.8 1.0 +0.031 -0.038 +0.067 -0.011 Safety-CHORES - SR 0 10 20 30 40 =-23.95 =-36.06 =-26.50 =-29.97 Safety-CHORES - CC ...
- **p. 10 / 5 Experiments - extractive PDF cue:** 5.3 Empirical Study: Sim-to-Real Transfer To validate the real-world applicability of our framework, we constructed the physical robot platform shown in Figure 8.
- **p. 39 / C.4 Experimental Environment and Costs - extractive PDF cue:** The most immediate goal is to bridge the sim-to-real gap by validating and adapting the ISA framework on complex, real-world robotic platforms.
- **p. 34 / C.4 Experimental Environment and Costs - extractive PDF cue:** For a trajectory τ, the constituent events Ei(sti, ati) establish that: (i) an object was perceived at an earlier time tj within the history window ...
- **p. 36 / C.4 Experimental Environment and Costs - extractive PDF cue:** For each task, if the robot exceeds the maximum number of steps, the episode is terminated and marked as a failure.
- **p. 39 / C.4 Experimental Environment and Costs - extractive PDF cue:** While prior work supports the feasibility of sim-to-real transfer for VLAs [32, 28], and simulation is indispensable for affordably collecting diverse safety-critical data, extensive validation ...
- **p. 7 / 5 Experiments - extractive PDF cue:** Borrowing from safety considerations in robotics [78, 79], our evaluation focuses on two metrics: the task success rate (SR) and the cumulative cost (CC).
- **p. 8 / 5 Experiments - extractive PDF cue:** Right: CC incurred by each model on these benchmarks. demonstrates substantial safety improvements, achieving an average reduction in CC of 83.58% compared to the strongest ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 5 Experiments (p. 6); A Additional Empirical Results (p. 25); C Implementation Details and Hyperparameters (p. 31); C.4 Experimental Environment and Costs (p. 33).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5: Comparative performance of VLA models on multiple benchmarks. Left: SR of each model per benchmark. Right: CC incurred by each model on ... | p. 8 (Figure/Table caption) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results demonstrate that our approach with dynamic Lagrangian multipliers achieves a superior trade-off, adhering to the cost limit while attaining a higher success ... | p. 9 (5 Experiments) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 0.00 0.25 0.50 0.75 1.00 Success Rate EmbCLIP 0.00 0.25 0.50 0.75 1.00 Success Rate Embodied-Codebook 0.00 0.25 0.50 0.75 1.00 Success Rate EmbCLIP-DINOv2 ... | p. 8 (5 Experiments) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | The average changes reported at the bottom of Table 2 indicate that, the safety benefits and reasonable task performance achieved by ISA are largely ... | p. 9 (5 Experiments) |
| C.4 Experimental Environment and Costs | EMPIRICAL / REAL-ROBOT OR HARDWARE | Following extensive evaluation and analysis, our method achieved state-of-the-art performance in both safety and task performance. | p. 36 (C.4 Experimental Environment and Costs) |

## Dataset / Benchmark Role

- **p. 7 / 5 Experiments - extractive PDF cue:** 0.0 0.2 0.4 0.6 0.8 1.0 +0.031 -0.038 +0.067 -0.011 Safety-CHORES - SR 0 10 20 30 40 =-23.95 =-36.06 =-26.50 =-29.97 Safety-CHORES - CC ...
- **p. 10 / 5 Experiments - extractive PDF cue:** 5.3 Empirical Study: Sim-to-Real Transfer To validate the real-world applicability of our framework, we constructed the physical robot platform shown in Figure 8.
- **p. 39 / C.4 Experimental Environment and Costs - extractive PDF cue:** The most immediate goal is to bridge the sim-to-real gap by validating and adapting the ISA framework on complex, real-world robotic platforms.
- **p. 34 / C.4 Experimental Environment and Costs - extractive PDF cue:** For a trajectory τ, the constituent events Ei(sti, ati) establish that: (i) an object was perceived at an earlier time tj within the history window ...
- **p. 36 / C.4 Experimental Environment and Costs - extractive PDF cue:** For each task, if the robot exceeds the maximum number of steps, the episode is terminated and marked as a failure.
- **p. 39 / C.4 Experimental Environment and Costs - extractive PDF cue:** While prior work supports the feasibility of sim-to-real transfer for VLAs [32, 28], and simulation is indispensable for affordably collecting diverse safety-critical data, extensive validation ...
- **p. 7 / 5 Experiments - extractive PDF cue:** Borrowing from safety considerations in robotics [78, 79], our evaluation focuses on two metrics: the task success rate (SR) and the cumulative cost (CC).
- **p. 8 / 5 Experiments - extractive PDF cue:** Right: CC incurred by each model on these benchmarks. demonstrates substantial safety improvements, achieving an average reduction in CC of 83.58% compared to the strongest ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: The Integrated Safety Approach (ISA) pipeline. Our proposed pipeline employs multi- faceted framework for the systematic safety alignment of vision-language-action (VLA) models. challenges ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 2: Upper: Conceptual diagrams of each safety critical component. Lower: Corresponding photorealistic examples from our simulation environment. we utilize a large-scale dataset of 150K ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1: Performance comparison across methods. The orange background of the rows indicates the methods using privileged information and the bold text indicates the best ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3: Cumulative cost distribution analysis. Left: Distribution of cumulative cost across robot trajectories in the test set after fine-tuning with ISA and FLaRe. Middle: ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4: Effectiveness of ISA across diverse VLA models and benchmarks. (§ 5.2.2); (III) Which components within ISA critically impact its safety-performance balance? (§ 5.2.3) ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5: Comparative performance of VLA models on multiple benchmarks. Left: SR of each model per benchmark. Right: CC incurred by each model on these ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6: ISA with fixed penalty coefficients. Importance of Risk Elicitation. The impor- tance of risk elicitation is demonstrated by an ablation study in Figure ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 7: Left: Ablation of the risk elicitation component. Middle: Ablation on cost thresholds bi. Right: Safety in extreme failure scenarios. ISA Generalizability to Different ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 0.0 0.2 0.4 0.6 0.8 1.0 +0.031 -0.038 +0.067 -0.011 Safety-CHORES - SR 0 10 20 30 40 =-23.95 =-36.06 =-26.50 =-29.97 Safety-CHORES - ... | embodiment, simulator version and control stack | p. 7 (5 Experiments), p. 10 (5 Experiments) |
| Task/environment | 5.3 Empirical Study: Sim-to-Real Transfer To validate the real-world applicability of our framework, we constructed the physical robot platform shown in Figure 8. | reset, timeout, object/scene variation | p. 10 (5 Experiments), p. 39 (C.4 Experimental Environment and Costs) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 31 (C.1 Details of SafeRL Training), p. 32 (C.1 Details of SafeRL Training) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (1 Introduction), p. 1 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 0.00 0.25 0.50 0.75 1.00 Success Rate EmbCLIP 0.00 0.25 0.50 0.75 1.00 Success Rate Embodied-Codebook 0.00 0.25 0.50 0.75 1.00 Success Rate EmbCLIP-DINOv2 ... | definition/direction/unit from same section | p. 8 (5 Experiments) |
| Borrowing from safety considerations in robotics [78, 79], our evaluation focuses on two metrics: the task success rate (SR) and the cumulative cost (CC). | definition/direction/unit from same section | p. 7 (5 Experiments) |
| 5.2.3 Ablation Studies: Impact of Key ISA Design Choices To understand the contribution of specific design choices in ISA, we conduct several ablation studies. ... | definition/direction/unit from same section | p. 8 (5 Experiments) |
| The results demonstrate that our approach with dynamic Lagrangian multipliers achieves a superior trade-off, adhering to the cost limit while attaining a higher success ... | definition/direction/unit from same section | p. 9 (5 Experiments) |
| Table 8: Zero-shot Generalization on DivScene. Performance is measured by Success Rate (SR ↑) / Cumulative Cost (CC ↓). | definition/direction/unit from same section | p. 30 (Figure/Table caption) |
| Table 11: Evaluating ISA with Alternative SafeRL Algorithms. Performance is measured by Success Rate (SR ↑) / Cumulative Cost (CC ↓). | definition/direction/unit from same section | p. 31 (Figure/Table caption) |
| Table 10: Safety under Semantic and Perceptual Perturbations. Performance is measured by Success Rate (SR ↑) / Cumulative Cost (CC ↓). Method / Perturbation ... | definition/direction/unit from same section | p. 31 (Figure/Table caption) |
| Left: Task success rate over training steps. | definition/direction/unit from same section | p. 32 (C.1 Details of SafeRL Training) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| ISA achieves an average SR increase of 3.85% compared to FLaRe, outperforming IL-only baselines and matching or exceeding other RL-based methods. | comparison identity and matched condition | p. 8 (5 Experiments) |
| Right: CC incurred by each model on these benchmarks. demonstrates substantial safety improvements, achieving an average reduction in CC of 83.58% compared to the ... | comparison identity and matched condition | p. 8 (5 Experiments) |
| In this section, we aim to answer the following questions: (I) Can ISA outperform standard VLA fine-tuning methods? | comparison identity and matched condition | p. 6 (5 Experiments) |
| First, SPOC is a state-of-the-art VLA trained solely on simulated data. | comparison identity and matched condition | p. 7 (5 Experiments) |
| IL-only: SPOC [32], which is a state-of-the-art imitation learning method. | comparison identity and matched condition | p. 7 (5 Experiments) |
| We compare this against baselines using fixed penalty coefficients for safety costs, as shown in Figure 6. | comparison identity and matched condition | p. 9 (5 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 0.86 0.64 0.75 1.85 5.01 4.75 0.00 0.25 0.50 0.75 1.00 0 1 2 3 4 5 ISA ISA without eliciting FLaRe-RS SR 0.82 ... | component/input/data sensitivity | p. 9 (5 Experiments) |
| Figure 6: ISA with fixed penalty coefficients. Importance of Risk Elicitation. The impor- tance of risk elicitation is demonstrated by an ablation study in ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| We also evaluate ISA on other VLA models (i.e., EmbCLIP [76], Embodied-Codebook [77] and their variants with different vision encoders). | component/input/data sensitivity | p. 7 (5 Experiments) |
| IL+RL (Reward Shaping): FLaRe-RS, a variant of FLaRe where safety costs are directly used as penalties on reward, representing a common heuristic for addressing ... | component/input/data sensitivity | p. 7 (5 Experiments) |
| 5.2.3 Ablation Studies: Impact of Key ISA Design Choices To understand the contribution of specific design choices in ISA, we conduct several ablation studies. ... | component/input/data sensitivity | p. 8 (5 Experiments) |
| Middle: Ablation on cost thresholds bi. | component/input/data sensitivity | p. 9 (5 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our study details how these interconnected aspects contribute to a more holistic safety alignment. • Environment: Addressing the gap in comprehensive VLA safety assessment, ... | Figure 5: Comparative performance of VLA models on multiple benchmarks. Left: SR of each model per benchmark. Right: CC incurred by each model on ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 9 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 36 (C.4 Experimental Environment and Costs), p. 7 (5 Experiments) |
| Primary metric/result | The results demonstrate that our approach with dynamic Lagrangian multipliers achieves a superior trade-off, adhering to the cost limit while attaining a higher success ... | numeric claim only at cited anchor | p. 9 (5 Experiments) |

- Numeric sentences retained from the body:
- **p. 36 / C.4 Experimental Environment and Costs - extractive PDF cue:** Observation Space: The observation space of the task consists of two 384×224 RGB cameras centered around the robot, pointing in orthogonal directions.
- **p. 36 / C.4 Experimental Environment and Costs - extractive PDF cue:** As shown in Table 13, each task is limited to a maximum of 600 steps.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 11: Qualitative comparison of ISA-aligned VLA and unaligned VLA behaviors. Left: Trajectory comparison for a representative task. The ISA-aligned VLA exhibits a smoother, ... | p. 26 (Figure/Table caption) |
| body limitation/failure cue | Crucially, aligned policies showed robust safety assurance, mitigating long-tail risks and generalizing to out-of-distribution perturbations and extreme failures, marking a first systematic integration of ... | p. 10 (6 Conclusion) |
| body limitation/failure cue | Figure 8: Setup for sim-to-real validation. The physical platform consists of dual Realman RM75- 6F arms equipped with PsiBot G0-R hands, perceived through an ... | p. 10 (Figure/Table caption) |
| body limitation/failure cue | Table 5: GPT-4 Response. Blind Spots The robot, while executing the action move-ahead in the LivingRoom, collided with scooter. This collision with an object ... | p. 28 (Figure/Table caption) |
| body limitation/failure cue | Algorithm 1 Corner Safety Component Require: Agent Position p, Detection Radius r, Corner Threshold ϵ, Map Points Set S 1: Integer N ←0 2: ... | p. 34 (C.4 Experimental Environment and Costs) |
| body limitation/failure cue | For FLaRe, higher safety costs are more prevalent in task failures, suggesting that unsafe behaviors often contribute to or coincide with failure. | p. 8 (5 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Additionally, we present the corresponding pseudocode for their algorithmic implementation. | p. 33 (C.4 Experimental Environment and Costs) |
| At iteration k, the policy parameter θk is adjusted by a gradient step on the combined objective LR -λkLC, scaled by a learning rate ... | p. 32 (C.1 Details of SafeRL Training) |
| We observe that using a larger batch size benefits the learning process. | p. 33 (C.4 Experimental Environment and Costs) |
| For simpler tasks like Safety-ObjNav and Safety-PickUp, we train for 15 million steps. | p. 7 (5 Experiments) |
| For more complex tasks that require integrated capabilities, such as Safety-Fetch, we train for 25 million steps. | p. 7 (5 Experiments) |
| 0.00 0.25 0.50 0.75 1.00 Success Rate EmbCLIP 0.00 0.25 0.50 0.75 1.00 Success Rate Embodied-Codebook 0.00 0.25 0.50 0.75 1.00 Success Rate EmbCLIP-DINOv2 ... | p. 8 (5 Experiments) |
| Left: Task success rate over training steps. | p. 32 (C.1 Details of SafeRL Training) |
| Algorithm 4 Critical Points Safety via Perturbation Require: Status Change Objects S, Movement Threshold δ 1: U ←∅ ▷Initialize set of unstable objects 2: ... | p. 35 (C.4 Experimental Environment and Costs) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 26 / Figure/Table caption - extractive PDF cue:** Figure 11: Qualitative comparison of ISA-aligned VLA and unaligned VLA behaviors. Left: Trajectory comparison for a representative task. The ISA-aligned VLA exhibits a smoother, more ...
- **p. 10 / 6 Conclusion - extractive PDF cue:** Crucially, aligned policies showed robust safety assurance, mitigating long-tail risks and generalizing to out-of-distribution perturbations and extreme failures, marking a first systematic integration of explicit ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Figure 8: Setup for sim-to-real validation. The physical platform consists of dual Realman RM75- 6F arms equipped with PsiBot G0-R hands, perceived through an egocentric ...
- **p. 28 / Figure/Table caption - extractive PDF cue:** Table 5: GPT-4 Response. Blind Spots The robot, while executing the action move-ahead in the LivingRoom, collided with scooter. This collision with an object previously ...
- **p. 34 / C.4 Experimental Environment and Costs - extractive PDF cue:** Algorithm 1 Corner Safety Component Require: Agent Position p, Detection Radius r, Corner Threshold ϵ, Map Points Set S 1: Integer N ←0 2: Integer ...
- **p. 8 / 5 Experiments - extractive PDF cue:** For FLaRe, higher safety costs are more prevalent in task failures, suggesting that unsafe behaviors often contribute to or coincide with failure.

- **PDF anchors reviewed:** datasets p. 7 (5 Experiments), p. 10 (5 Experiments), p. 39 (C.4 Experimental Environment and Costs), p. 34 (C.4 Experimental Environment and Costs), p. 36 (C.4 Experimental Environment and Costs), p. 39 (C.4 Experimental Environment and Costs), metrics p. 8 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 30 (Figure/Table caption), p. 31 (Figure/Table caption), baselines p. 8 (5 Experiments), p. 8 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments), p. 7 (5 Experiments), p. 9 (5 Experiments), results p. 8 (Figure/Table caption), p. 9 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 36 (C.4 Experimental Environment and Costs), p. 7 (5 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
