# Evaluation - Diffusion Policy: Visuomotor Policy Learning via Action Diffusion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2303.04137; PDF retrieval source: https://arxiv.org/pdf/2303.04137. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 9 (Figure/Table caption), p. 6 (5 Evaluation), p. 9 (5 Evaluation), p. 8 (5 Evaluation), p. 8 (5 Evaluation)): Table 1. Behavior Cloning Benchmark (State Policy) We present success rates with different checkpoint selection methods in the format of (max performance) / (average of last 10 checkpoints), with each ...

## Evaluation Body Digest

- **p. 6 / 5 Evaluation - extractive body cue:** The benchmark consists of 5 tasks with a proficient human (PH) teleoperated demonstration dataset for each and mixed proficient/non-proficient human (MH) demonstration datasets for 4 ...
- **p. 7 / 5 Evaluation - extractive body cue:** (2019), the Franka Kitchen environment contains 7 objects for interaction and comes with a human demonstration dataset of 566 demonstrations, each completing 4 tasks in ...
- **p. 6 / 5 Evaluation - extractive body cue:** This evaluation suite includes both simulated and real environments, single and multiple task benchmarks, fully actuated and under-actuated systems, and rigid and fluid objects.
- **p. 7 / 5 Evaluation - extractive body cue:** Tasks Summary. # Rob: number of robots, #Obj: number of objects, ActD: action dimension, PH: proficient-human demonstration, MH: multi-human demonstration, Steps: max number of rollout ...
- **p. 8 / 5 Evaluation - extractive body cue:** 5.3 Key Findings Diffusion Policy outperforms alternative methods on all tasks and variants, with both state and vision observations, in our simulation benchmark study (Tabs ...
- **p. 8 / 5 Evaluation - extractive body cue:** The results from these simulation benchmarks are summarized in Table 1 and Table 2.
- **p. 9 / 5 Evaluation - extractive body cue:** The real-world Push-T task is multi-stage.
- **p. 9 / 5 Evaluation - extractive body cue:** Realworld Push-T Experiment. a) Hardware setup. b) Illustration of the task.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** 5 Evaluation (p. 6); A Diffusion Policy Implementation Details (p. 16); B Additional Ablation Results (p. 16); C.2.2 Evaluation Both Diffusion Policy and LSTM-GMM (p. 17).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1. Behavior Cloning Benchmark (State Policy) We present success rates with different checkpoint selection methods in the format of (max performance) / (average ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Tab. 6. Diffusion Policy with R3M achieves an 80% success rate but predicts jittery actions and is more likely to get stuck compared to ... | p. 9 (Figure/Table caption) |
| 5 Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | We found Diffusion Policy to consistently outperform the prior state-of-the-art on all of the tested benchmarks, with an average success-rate improvement of 46.9%. | p. 6 (5 Evaluation) |
| 5 Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | We threshold success rate by the minimum achieved IoU metric from the human demonstration dataset. | p. 9 (5 Evaluation) |
| 5 Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | We find that Diffusion Policy copes well with this type of multimodality; it outperforms baselines on both tasks by a large margin: 32% improvement ... | p. 8 (5 Evaluation) |

## Dataset / Benchmark Role

- **p. 6 / 5 Evaluation - extractive body cue:** The benchmark consists of 5 tasks with a proficient human (PH) teleoperated demonstration dataset for each and mixed proficient/non-proficient human (MH) demonstration datasets for 4 ...
- **p. 7 / 5 Evaluation - extractive body cue:** (2019), the Franka Kitchen environment contains 7 objects for interaction and comes with a human demonstration dataset of 566 demonstrations, each completing 4 tasks in ...
- **p. 6 / 5 Evaluation - extractive body cue:** This evaluation suite includes both simulated and real environments, single and multiple task benchmarks, fully actuated and under-actuated systems, and rigid and fluid objects.
- **p. 7 / 5 Evaluation - extractive body cue:** Tasks Summary. # Rob: number of robots, #Obj: number of objects, ActD: action dimension, PH: proficient-human demonstration, MH: multi-human demonstration, Steps: max number of rollout ...
- **p. 8 / 5 Evaluation - extractive body cue:** 5.3 Key Findings Diffusion Policy outperforms alternative methods on all tasks and variants, with both state and vision observations, in our simulation benchmark study (Tabs ...
- **p. 8 / 5 Evaluation - extractive body cue:** The results from these simulation benchmarks are summarized in Table 1 and Table 2.
- **p. 9 / 5 Evaluation - extractive body cue:** The real-world Push-T task is multi-stage.
- **p. 9 / 5 Evaluation - extractive body cue:** Realworld Push-T Experiment. a) Hardware setup. b) Illustration of the task.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Policy Representations. a) Explicit policy with different types of action representations. b) Implicit policy learns an energy function conditioned on both action and ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Diffusion Policy Overview a) General formulation. At time step t, the policy takes the latest To steps of observation data Ot as input ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Multimodal behavior. At the given state, the end-effector (blue) can either go left or right to push the block. Diffusion Policy learns both ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Velocity v.s. Position Control. The performance difference when switching from velocity to position control. While both BCRNN and BET performance decrease, Diffusion Policy ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5. Diffusion Policy Ablation Study. Change (difference) in success rate relative to the maximum for each task is shown on the Y-axis. Left: trade-off ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6. Training Stability. Left: IBC fails to infer training actions with increasing accuracy despite smoothly decreasing training loss for energy function. Right: IBC's evaluation ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Behavior Cloning Benchmark (State Policy) We present success rates with different checkpoint selection methods in the format of (max performance) / (average of ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Behavior Cloning Benchmark (Visual Policy) Performance are reported in the same format as in Tab 1. LSTM-GMM numbers were reproduced to get a ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The benchmark consists of 5 tasks with a proficient human (PH) teleoperated demonstration dataset for each and mixed proficient/non-proficient human (MH) demonstration datasets for ... | embodiment, simulator version and control stack | p. 6 (5 Evaluation), p. 7 (5 Evaluation) |
| Task/environment | (2019), the Franka Kitchen environment contains 7 objects for interaction and comes with a human demonstration dataset of 566 demonstrations, each completing 4 tasks ... | reset, timeout, object/scene variation | p. 7 (5 Evaluation), p. 6 (5 Evaluation) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 1 (1 Introduction), p. 1 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We threshold success rate by the minimum achieved IoU metric from the human demonstration dataset. | definition/direction/unit from same section | p. 9 (5 Evaluation) |
| 0.84 average IoU, compared with the 0% and 20% success rate of best-performing IBC and LSTM-GMM variants. | definition/direction/unit from same section | p. 9 (5 Evaluation) |
| Figure 6. Training Stability. Left: IBC fails to infer training actions with increasing accuracy despite smoothly decreasing training loss for energy function. Right: IBC's ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Behavior Cloning Benchmark (State Policy) We present success rates with different checkpoint selection methods in the format of (max performance) / (average of last ... | definition/direction/unit from same section | p. 7 (5 Evaluation) |
| The metric for most tasks is success rate, except for the Push-T task, which uses target area coverage. | definition/direction/unit from same section | p. 7 (5 Evaluation) |
| This is especially true for the CLIP-trained ViT-B/16, which reaches 98% success rate with only 50 epochs of training. | definition/direction/unit from same section | p. 8 (5 Evaluation) |
| We found training ViT from scratch to be challenging (with only 22% success rate), likely due to the limited amount data. | definition/direction/unit from same section | p. 8 (5 Evaluation) |
| Figure 5. Diffusion Policy Ablation Study. Change (difference) in success rate relative to the maximum for each task is shown on the Y-axis. Left: ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We found Diffusion Policy to consistently outperform the prior state-of-the-art on all of the tested benchmarks, with an average success-rate improvement of 46.9%. | comparison identity and matched condition | p. 6 (5 Evaluation) |
| We find that Diffusion Policy copes well with this type of multimodality; it outperforms baselines on both tasks by a large margin: 32% improvement ... | comparison identity and matched condition | p. 8 (5 Evaluation) |
| On the realworld Push-T task, we perform ablations examining Diffusion Policy on 2 architecture options and 3 visual encoder options; we also benchmarked against ... | comparison identity and matched condition | p. 9 (5 Evaluation) |
| This does not change our conclusion since all baseline methods are evaluated in the same way. | comparison identity and matched condition | p. 7 (5 Evaluation) |
| The demonstration data is generated by a scripted oracle with access to groundtruth state info. | comparison identity and matched condition | p. 7 (5 Evaluation) |
| 4) shows that selecting position control as the diffusion-policy action space significantly outperformed velocity control. | comparison identity and matched condition | p. 8 (5 Evaluation) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| There are two variants: one with RGB image observations and another with 9 2D keypoints obtained from the groundtruth pose of the T block, ... | component/input/data sensitivity | p. 6 (5 Evaluation) |
| Each method is evaluated with its best-performing action space: position control for Diffusion Policy and velocity control for baselines (the effect of action space ... | component/input/data sensitivity | p. 8 (5 Evaluation) |
| For each variant, we report results for both stateand image-based observations. | component/input/data sensitivity | p. 6 (5 Evaluation) |
| 5.4 Ablation Study We explore alternative vision encoder design decisions on the simulated robomimic square task. | component/input/data sensitivity | p. 8 (5 Evaluation) |
| 0.84 average IoU, compared with the 0% and 20% success rate of best-performing IBC and LSTM-GMM variants. | component/input/data sensitivity | p. 9 (5 Evaluation) |
| On all tasks, Diffusion Policy variants with both CNN backbones and end-to-end-trained visual encoders yielded the best performance. | component/input/data sensitivity | p. 9 (5 Evaluation) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To successfully employ diffusion models for visuomotor policy learning, we present the following technical contributions that enhance the performance of Diffusion Policy and unlock ... | Table 1. Behavior Cloning Benchmark (State Policy) We present success rates with different checkpoint selection methods in the format of (max performance) / (average ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 9 (Figure/Table caption), p. 6 (5 Evaluation), p. 9 (5 Evaluation), p. 8 (5 Evaluation), p. 8 (5 Evaluation) |
| Primary metric/result | Tab. 6. Diffusion Policy with R3M achieves an 80% success rate but predicts jittery actions and is more likely to get stuck compared to ... | numeric claim only at cited anchor | p. 9 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 5 Evaluation - extractive body cue:** We systematically evaluate Diffusion Policy on 15 tasks from 4 benchmarks Florence et al.
- **p. 6 / 5 Evaluation - extractive body cue:** The benchmark consists of 5 tasks with a proficient human (PH) teleoperated demonstration dataset for each and mixed proficient/non-proficient human (MH) demonstration datasets for 4 ...
- **p. 7 / 5 Evaluation - extractive body cue:** BlockPush uses 1000 episodes of scripted demonstrations. into two squares in any order.
- **p. 7 / 5 Evaluation - extractive body cue:** (2019), the Franka Kitchen environment contains 7 objects for interaction and comes with a human demonstration dataset of 566 demonstrations, each completing 4 tasks in ...
- **p. 7 / 5 Evaluation - extractive body cue:** We report results from the average of the last 10 checkpoints (saved every 50 epochs) across 3 training seeds and 50 environment initializations * (an ...
- **p. 8 / 5 Evaluation - extractive body cue:** All state-based tasks are trained for 4500 epochs, and image-based tasks for 3000 epochs.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We observed that poor performance during the transition between stages is the most common failure case for the baseline method due to high multimodality ... | p. 9 (5 Evaluation) |
| body limitation/failure cue | Figure 7. Realworld Push-T Comparisons. Columns 1-4 show action trajectories based on key events. The last column shows averaged images of the end state. ... | p. 10 (Figure/Table caption) |
| body limitation/failure cue | The primary failure modes for these were out-of-domain initial positioning of the egg beater, or missing the egg beater crank handle or losing grasp ... | p. 11 (A C) |
| body limitation/failure cue | The primary failure modes for these were missed grasps for initial folding (the sleeves and the color), and the policy being unable to stop ... | p. 12 (A C) |
| body limitation/failure cue | The primary failure modes for these were missed grasps during initial grasp of the mat, where the policy struggled to correct itself and thus ... | p. 12 (A C) |
| body limitation/failure cue | Figure 3. Multimodal behavior. At the given state, the end-effector (blue) can either go left or right to push the block. Diffusion Policy learns ... | p. 5 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We report results from the average of the last 10 checkpoints (saved every 50 epochs) across 3 training seeds and 50 environment initializations * ... | p. 7 (5 Evaluation) |
| However, we found finetuning the pretrained vision encoder with a small learning rate (10x smaller vs diffusion policy network) gives the best performance overall. | p. 8 (5 Evaluation) |
| For each architecture, we evaluated 3 different training strategies: training end-to-end from scratch, using frozen pre-trained vision encoder, and finetuning pre-trained vision encoders (with ... | p. 8 (5 Evaluation) |
| Behavior Cloning Benchmark (State Policy) We present success rates with different checkpoint selection methods in the format of (max performance) / (average of last ... | p. 7 (5 Evaluation) |
| We used batch size of 256 for all state-based experiments and 64 for all image-based experiments. | p. 16 (A.4 Hyperparameters) |
| Realworld Push-T Experiment. a) Hardware setup. b) Illustration of the task. | p. 9 (5 Evaluation) |
| The IoU metric is measured at the last step instead of taking the maximum over all steps. | p. 9 (5 Evaluation) |
| We found that the optimal hyperparameters for CNNbased Diffusion Policy are consistent across tasks. | p. 16 (A.4 Hyperparameters) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 5 Evaluation - extractive body cue:** We observed that poor performance during the transition between stages is the most common failure case for the baseline method due to high multimodality during ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 7. Realworld Push-T Comparisons. Columns 1-4 show action trajectories based on key events. The last column shows averaged images of the end state. A: ...
- **p. 11 / A C - extractive body cue:** The primary failure modes for these were out-of-domain initial positioning of the egg beater, or missing the egg beater crank handle or losing grasp of ...
- **p. 12 / A C - extractive body cue:** The primary failure modes for these were missed grasps for initial folding (the sleeves and the color), and the policy being unable to stop adjusting ...
- **p. 12 / A C - extractive body cue:** The primary failure modes for these were missed grasps during initial grasp of the mat, where the policy struggled to correct itself and thus got ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Multimodal behavior. At the given state, the end-effector (blue) can either go left or right to push the block. Diffusion Policy learns both ...

- **Evidence anchors reviewed:** datasets p. 6 (5 Evaluation), p. 7 (5 Evaluation), p. 6 (5 Evaluation), p. 7 (5 Evaluation), p. 8 (5 Evaluation), p. 8 (5 Evaluation), metrics p. 9 (5 Evaluation), p. 9 (5 Evaluation), p. 6 (Figure/Table caption), p. 7 (5 Evaluation), p. 7 (5 Evaluation), p. 8 (5 Evaluation), baselines p. 6 (5 Evaluation), p. 8 (5 Evaluation), p. 9 (5 Evaluation), p. 7 (5 Evaluation), p. 7 (5 Evaluation), p. 8 (5 Evaluation), results p. 7 (Figure/Table caption), p. 9 (Figure/Table caption), p. 6 (5 Evaluation), p. 9 (5 Evaluation), p. 8 (5 Evaluation), p. 8 (5 Evaluation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (19 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Table 1. Behavior Cloning Benchmark (State Policy) We present success rates with different checkpoint selection methods in the format of (max performance) / (average of last 10 checkpoints), with each ... (p. 7, Figure/Table caption).
- **Metric evidence:** 0.84 average IoU, compared with the 0% and 20% success rate of best-performing IBC and LSTM-GMM variants. (p. 9, 5 Evaluation).
- **Baseline/ablation evidence:** We found Diffusion Policy to consistently outperform the prior state-of-the-art on all of the tested benchmarks, with an average success-rate improvement of 46.9%. (p. 6, 5 Evaluation).
- **Failure/negative evidence:** The primary failure modes for these were missed grasps for initial folding (the sleeves and the color), and the policy being unable to stop adjusting the shirt at the end. (p. 12, A C).
