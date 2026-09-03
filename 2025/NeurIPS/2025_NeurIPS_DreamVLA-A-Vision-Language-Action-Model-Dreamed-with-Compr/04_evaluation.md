# Evaluation - DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (30 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=PK07eretkF; PDF retrieval source: https://arxiv.org/pdf/2507.04447. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments), p. 9 (4 Experiments)): Table 2: The extended LIBERO experiments. DreamVLA achieves the best or competitive performance across all tracks compared to previous approaches. The best results are bolded. Methods Scores (%) Average Spatial ...

## Evaluation Body Digest

- **p. 24 / A.2 Feature Extraction - extractive body cue:** In cases where depth annotations are not provided-such as in certain real-world robot datasets-we use monocular depth estimators, specifically Depth-Anything v2 [64], to generate pseudo-ground-truth ...
- **p. 7 / 4 Experiments - extractive body cue:** CALVIN is a simulated benchmark designed for learning long-horizon, language-conditioned robot manipulation policies.
- **p. 8 / 4 Experiments - extractive body cue:** Follow [56], we pretrain DreamVLA on the DROID [82] contains large-scale trajectories of Franka robots in varied scenes.
- **p. 8 / 4 Experiments - extractive body cue:** For fair comparison, we fine-tune Diffusion Policy [90], Octo-Base [13], OpenVLA [1] and DreamVLA on collected demonstration datasets containing 100 trajectories for each task.
- **p. 7 / 4 Experiments - extractive body cue:** We first pre-train DreamVLA on the language-free split of the CALVIN [117] and on the full DROID dataset [82].
- **p. 9 / 4 Experiments - extractive body cue:** In our ablation, every prediction strategy is individually replaced by its reconstruction counterpart, yet each substitution consistently lowers performance: VLA trained only to redraw the ...
- **p. 22 / A.1 DreamVLA Architecture - extractive body cue:** We tokenize the robot state using an MLP.
- **p. 22 / A.1 DreamVLA Architecture - extractive body cue:** The robot state consists of the arm and gripper state.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 Experiments (p. 7); A Implementation Details (p. 22); B Experiments (p. 24); B.1 Simulation Benchmark and Settings (p. 24); B.2 Simulation Results (p. 25).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2: The extended LIBERO experiments. DreamVLA achieves the best or competitive performance across all tracks compared to previous approaches. The best results are ... | p. 8 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 1(b) in manuscripts, our model significantly achieves more accurate control. | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | All models are trained for 20 epochs, and we select the checkpoint with the highest validation success rate (SR) for final evaluation. | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | This extra burden manifests in markedly lower multi-step success rates. | p. 10 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | With K = 9, each modality has sufficient bandwidth without overloading the backbone, yielding the best success rate and the longest uninterrupted task execution. | p. 10 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 24 / A.2 Feature Extraction - extractive body cue:** In cases where depth annotations are not provided-such as in certain real-world robot datasets-we use monocular depth estimators, specifically Depth-Anything v2 [64], to generate pseudo-ground-truth ...
- **p. 7 / 4 Experiments - extractive body cue:** CALVIN is a simulated benchmark designed for learning long-horizon, language-conditioned robot manipulation policies.
- **p. 8 / 4 Experiments - extractive body cue:** Follow [56], we pretrain DreamVLA on the DROID [82] contains large-scale trajectories of Franka robots in varied scenes.
- **p. 8 / 4 Experiments - extractive body cue:** For fair comparison, we fine-tune Diffusion Policy [90], Octo-Base [13], OpenVLA [1] and DreamVLA on collected demonstration datasets containing 100 trajectories for each task.
- **p. 7 / 4 Experiments - extractive body cue:** We first pre-train DreamVLA on the language-free split of the CALVIN [117] and on the full DROID dataset [82].
- **p. 9 / 4 Experiments - extractive body cue:** In our ablation, every prediction strategy is individually replaced by its reconstruction counterpart, yet each substitution consistently lowers performance: VLA trained only to redraw the ...
- **p. 22 / A.1 DreamVLA Architecture - extractive body cue:** We tokenize the robot state using an MLP.
- **p. 22 / A.1 DreamVLA Architecture - extractive body cue:** The robot state consists of the arm and gripper state.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: (a) Vanilla VLA directly maps visual observations and language instructions to actions. (b) Models leveraging separate image/video generation or copilot models to generate ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Framework Overview. Given the current robot state st, observation ot, and language instruction, DreamVLA encodes multimodal inputs via frozen text, visual encoders and ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Visualization of dynamic regions over time. We show the static camera (left) and wrist-mounted camera (right) observations alongside the corresponding dynamic masks generated ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Block-wise structured attention. Structured attention for cross-type knowledge dis- entanglement. To preserve clear cross-type knowl- edge boundaries, <dream> is decomposed into three sub-queries ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: CALVIN ABC-D results. We present the average success computed over 1000 rollouts for each task and the average number of completed tasks to ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: The extended LIBERO experiments. DreamVLA achieves the best or competitive performance across all tracks compared to previous approaches. The best results are bolded. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Real-world experiment setup. To evaluate the effectiveness of our method in the real-world, we use the Franka Panda arm to conduct real-world experiments ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Real-world evaluation with the Franka Robot across three tasks.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In cases where depth annotations are not provided-such as in certain real-world robot datasets-we use monocular depth estimators, specifically Depth-Anything v2 [64], to generate ... | embodiment, simulator version and control stack | p. 24 (A.2 Feature Extraction), p. 7 (4 Experiments) |
| Task/environment | CALVIN is a simulated benchmark designed for learning long-horizon, language-conditioned robot manipulation policies. | reset, timeout, object/scene variation | p. 7 (4 Experiments), p. 8 (4 Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 4 (3 Methodology) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (3 Methodology), p. 3 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In our ablation, every prediction strategy is individually replaced by its reconstruction counterpart, yet each substitution consistently lowers performance: VLA trained only to redraw ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| All models are trained for 20 epochs, and we select the checkpoint with the highest validation success rate (SR) for final evaluation. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| We report the success rate of every track and the average length of 5 tasks. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| This extra burden manifests in markedly lower multi-step success rates. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| With K = 9, each modality has sufficient bandwidth without overloading the backbone, yielding the best success rate and the longest uninterrupted task execution. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| Methods Scores (%) Average Spatial Object Goal Long Diffusion Policy [90] 78.3 92.5 68.3 50.5 72.4 Octo [13] 78.9 85.7 84.6 51.1 75.1 OpenVLA ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Parameter Value Model type DiT-B Token size 1024 Action prediction window 2 future steps (3-frame chunk) Past context steps 0 Number of Transformer layers ... | definition/direction/unit from same section | p. 23 (A.1 DreamVLA Architecture) |
| By contrast, supervising the network with depth map, DINO or SAM features alone not only fails to help but often degrades performance. | definition/direction/unit from same section | p. 9 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| DreamVLA outperforms approaches like UP-VLA [57], Seer [56], and VPP [49] as shown in Fig. | comparison identity and matched condition | p. 8 (4 Experiments) |
| DreamVLA achieves the best or competitive performance across all tracks compared to previous approaches. | comparison identity and matched condition | p. 8 (4 Experiments) |
| The green dashed line denotes the performance of the Vanilla VLA baseline, which uses no knowledge prediction. | comparison identity and matched condition | p. 9 (4 Experiments) |
| With the limited model attention budget, these competing gradients dilute the task-relevant features and push the backbone toward suboptimal optima, producing the observed drop ... | comparison identity and matched condition | p. 9 (4 Experiments) |
| Figure 3: Visualization of dynamic regions over time. We show the static camera (left) and wrist-mounted camera (right) observations alongside the corresponding dynamic masks ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| Table 1: CALVIN ABC-D results. We present the average success computed over 1000 rollouts for each task and the average number of completed tasks ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Next, we train the model with all five knowledge heads simultaneously (All) and perform an ablation study (All-X), where we remove one knowledge signal ... | component/input/data sensitivity | p. 9 (4 Experiments) |
| Interestingly, removing DINO results in similar or even better performance, suggesting that not all semantic signals are equally helpful or stable in predicting outcomes, ... | component/input/data sensitivity | p. 9 (4 Experiments) |
| Q6: Effect of the query count per modality inside <dream> queries. | component/input/data sensitivity | p. 10 (4 Experiments) |
| Our mask removes all query-to-query edges, so <action> query consults only past language, state and multimodal predictions, never their siblings. | component/input/data sensitivity | p. 10 (4 Experiments) |
| Figure 10: Qualitative results of real world language-grounded manipulation. D Additional Discussions and Future Work i. Scaling Laws. A promising direction for future exploration ... | component/input/data sensitivity | p. 29 (Figure/Table caption) |
| Figure 1: (a) Vanilla VLA directly maps visual observations and language instructions to actions. (b) Models leveraging separate image/video generation or copilot models to ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The key contributions of our work are summarized as follows: • We recast the vision-language-action model as a perception-prediction-action model and make the model ... | Table 2: The extended LIBERO experiments. DreamVLA achieves the best or competitive performance across all tracks compared to previous approaches. The best results are ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments), p. 9 (4 Experiments) |
| Primary metric/result | 1(b) in manuscripts, our model significantly achieves more accurate control. | numeric claim only at cited anchor | p. 8 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Experiments - extractive body cue:** All models are trained for 20 epochs, and we select the checkpoint with the highest validation success rate (SR) for final evaluation.
- **p. 8 / 4 Experiments - extractive body cue:** We report the success rate of every track and the average length of 5 tasks.
- **p. 8 / 4 Experiments - extractive body cue:** Each suite contains 10 tasks supported by 50 human-teleoperated demonstrations, targeting spatial reasoning, object-centric manipulation, and goal completion.
- **p. 8 / 4 Experiments - extractive body cue:** For fair comparison, we fine-tune Diffusion Policy [90], Octo-Base [13], OpenVLA [1] and DreamVLA on collected demonstration datasets containing 100 trajectories for each task.
- **p. 8 / 4 Experiments - extractive body cue:** The experiment is considered successful if the drawer displacement exceeds 10 centimeters, indicating effective interaction.
- **p. 22 / A.1 DreamVLA Architecture - extractive body cue:** Directly inputting all 197 tokens into the transformer backbone would create a significant computational burden, particularly when processing long histories.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | By contrast, supervising the network with depth map, DINO or SAM features alone not only fails to help but often degrades performance. | p. 9 (4 Experiments) |
| body limitation/failure cue | In our ablation, every prediction strategy is individually replaced by its reconstruction counterpart, yet each substitution consistently lowers performance: VLA trained only to redraw ... | p. 9 (4 Experiments) |
| body limitation/failure cue | In this setting, every <dream> query, including the one meant to capture semantics, can also read the flow and depth tokens produced in the ... | p. 10 (4 Experiments) |
| body limitation/failure cue | The model does not utilize past action context during generation (i.e., past window size is 0), focusing solely on predictive synthesis. | p. 23 (A.1 DreamVLA Architecture) |
| body limitation/failure cue | Figure 10: Qualitative results of real world language-grounded manipulation. D Additional Discussions and Future Work i. Scaling Laws. A promising direction for future exploration ... | p. 29 (Figure/Table caption) |
| body limitation/failure cue | Figure 2: Framework Overview. Given the current robot state st, observation ot, and language instruction, DreamVLA encodes multimodal inputs via frozen text, visual encoders ... | p. 4 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Batch size is set to 64, we set the query length of each modality 9 and diffusion steps in DiT to 10. | p. 7 (4 Experiments) |
| This approach requires extra storage space to save all the features extracted from the above foundation models, but significantly saves on training time and ... | p. 24 (A.3 Training Detail) |
| All models are trained for 20 epochs, and we select the checkpoint with the highest validation success rate (SR) for final evaluation. | p. 7 (4 Experiments) |
| The resulting mask is flattened and reshaped into the form (B, 1, L), where L = ⌊H/8⌋· ⌊W/8⌋and B is the batch size. | p. 24 (A.2 Feature Extraction) |
| In the experimental setup, each trial permits a maximum of 20 consecutive attempts. | p. 8 (4 Experiments) |
| A trial is deemed successful if the robotic arm successfully grasps the target object within the predefined attempt limit. | p. 8 (4 Experiments) |
| Increasing to K = 16 introduces redundant tokens that compete for attention and raise GPU memory, bringing no extra gain and slightly lower generalization. | p. 10 (4 Experiments) |
| We employ an MAE-pretrained ViT-B [104] as the vision encoder. | p. 22 (A.1 DreamVLA Architecture) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 4 Experiments - extractive body cue:** By contrast, supervising the network with depth map, DINO or SAM features alone not only fails to help but often degrades performance.
- **p. 9 / 4 Experiments - extractive body cue:** In our ablation, every prediction strategy is individually replaced by its reconstruction counterpart, yet each substitution consistently lowers performance: VLA trained only to redraw the ...
- **p. 10 / 4 Experiments - extractive body cue:** In this setting, every <dream> query, including the one meant to capture semantics, can also read the flow and depth tokens produced in the same ...
- **p. 23 / A.1 DreamVLA Architecture - extractive body cue:** The model does not utilize past action context during generation (i.e., past window size is 0), focusing solely on predictive synthesis.
- **p. 29 / Figure/Table caption - extractive body cue:** Figure 10: Qualitative results of real world language-grounded manipulation. D Additional Discussions and Future Work i. Scaling Laws. A promising direction for future exploration involves ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Framework Overview. Given the current robot state st, observation ot, and language instruction, DreamVLA encodes multimodal inputs via frozen text, visual encoders and ...

- **Evidence anchors reviewed:** datasets p. 24 (A.2 Feature Extraction), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), metrics p. 9 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments), p. 8 (4 Experiments), baselines p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 5 (Figure/Table caption), p. 7 (Figure/Table caption), results p. 8 (Figure/Table caption), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments), p. 9 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
