# Evaluation - Ctrl-World: A Controllable Generative World Model for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10011332; PDF retrieval source: https://arxiv.org/pdf/2510.10125. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 17 (Figure/Table caption), p. 5 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS)): Spatial Shape Towel-Dir Novel-Obj Average 0.0 0.2 0.4 0.6 0.8 1.0 Success rate 0.29 0.44 0.57 0.25 0.39 0.88 0.91 0.80 0.75 0.83 Base Policy Finetuned Policy Figure 9: Policy ...

## Evaluation Body Digest

- **p. 5 / 5 EXPERIMENTS - extractive body cue:** The DROID dataset (Khazatsky et al., 2024) contains 95,599 diverse trajectories collected from 564 scenes, providing dense coverage of the workspace.
- **p. 5 / 5 EXPERIMENTS - extractive body cue:** (2) Can Ctrl-World reliably evaluate different generalist robot policies in imagination space, faithfully reproducing their real-world performance rankings?
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** Consistent with observations from prior work (Quevedo et al., 2025; Zhu et al., 2024), we also find that these baselines struggle to capture robot-object interactions ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** In contrast, Ctrl-World precisely models the robot-object interactions through joint prediction of the wrist-camera view, which provides critical, fine-grained information about contact events and object ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Similar to how prior works have seen DROID policies generalize to new setups (Pertsch et al., 2025), we find that Ctrl-World, pretrained solely on the ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** 0.0 0.2 0.4 0.6 0.8 1.0 Instruction Following in Real World 0.0 0.2 0.4 0.6 0.8 1.0 in World Model y = 0.87x-0.04 0.0 0.2 ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Finally, we fine-tune the policy on the curated synthetic dataset for 2k steps, improving base model's capability in unfamiliar instructions and objects.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** As described in Section 4.2, we encourage rollout diversity by either (1) rephrasing task instructions or (2) resetting the robot arm to a new initial ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** 5 EXPERIMENTS (p. 5); B MORE DETAILS FOR POLICY EVALUATION (p. 16).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Spatial Shape Towel-Dir Novel-Obj Average 0.0 0.2 0.4 0.6 0.8 1.0 Success rate 0.29 0.44 0.57 0.25 0.39 0.88 0.91 0.80 0.75 0.83 Base ... | p. 9 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | While the pretrained π0.5 policy achieves low success rates on unfamiliar objects and novel instructions, post-training aligns the model with new instructions and boosts ... | p. 9 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 1, Ctrl-World-third-view outperforms these prior models, and multi-view joint prediction further improves generation quality. | p. 6 (5 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 3: Comparison of instruction-following and success rate across methods and tasks. Breakdown for policy evaluation. We present the instruction-following and low-level execution success ... | p. 17 (Figure/Table caption) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | (3) Can Ctrl-World improve a policy's instruction following by discovering and synthesizing successful trajectories entirely within its imagination? | p. 5 (5 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 5 / 5 EXPERIMENTS - extractive body cue:** The DROID dataset (Khazatsky et al., 2024) contains 95,599 diverse trajectories collected from 564 scenes, providing dense coverage of the workspace.
- **p. 5 / 5 EXPERIMENTS - extractive body cue:** (2) Can Ctrl-World reliably evaluate different generalist robot policies in imagination space, faithfully reproducing their real-world performance rankings?
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** Consistent with observations from prior work (Quevedo et al., 2025; Zhu et al., 2024), we also find that these baselines struggle to capture robot-object interactions ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** In contrast, Ctrl-World precisely models the robot-object interactions through joint prediction of the wrist-camera view, which provides critical, fine-grained information about contact events and object ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Similar to how prior works have seen DROID policies generalize to new setups (Pertsch et al., 2025), we find that Ctrl-World, pretrained solely on the ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** 0.0 0.2 0.4 0.6 0.8 1.0 Instruction Following in Real World 0.0 0.2 0.4 0.6 0.8 1.0 in World Model y = 0.87x-0.04 0.0 0.2 ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Finally, we fine-tune the policy on the curated synthetic dataset for 2k steps, improving base model's capability in unfamiliar instructions and objects.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** As described in Section 4.2, we encourage rollout diversity by either (1) rephrasing task instructions or (2) resetting the robot arm to a new initial ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Ctrl-World is designed for policy-in-the-loop rollouts with generalist robot policies. It generates joint multi-view predictions (including wrist views), enforces fine-grained action control via ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Ctrl-World is initialized from a pretrained video diffusion model and adapted into a controllable, temporally consistent world model with: (1) Multi-view input and ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Quantitative results for interactive long-trajectory generation on the validation set. We evaluate our world model's quality by generating 10-second trajectories. Given a randomly ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Qualitative results on long-horizon rollouts from the validation set. Prior models rely on single-view prediction, suffering from partial observability and hallucinations (e.g., failing ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2: Ablations on key components in Ctrl-World. Removing memory mechanisms, frame-level action conditioning or multi-view joint predictions all lead to a performance drop. 2025) ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Controllability of Ctrl-World and ablations. Different action sequences can produce distinct rollouts in Ctrl-World with centimeter-level precision. Removing memory leads to blurry predictions ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Consistency of Ctrl-World. Since the wrist camera's field of view changes dramatically within a single trajectory, leveraging multi-view information and memory retrieval is ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Comparisons between π0.5 rollouts in the real-world and world model. Each trajectory contains 20 interactions between π0.5 and Ctrl-World. Remarkably, both the generalist ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The DROID dataset (Khazatsky et al., 2024) contains 95,599 diverse trajectories collected from 564 scenes, providing dense coverage of the workspace. | embodiment, simulator version and control stack | p. 5 (5 EXPERIMENTS), p. 5 (5 EXPERIMENTS) |
| Task/environment | (2) Can Ctrl-World reliably evaluate different generalist robot policies in imagination space, faithfully reproducing their real-world performance rankings? | reset, timeout, object/scene variation | p. 5 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 5 (1 INTRODUCTION), p. 4 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 3: Comparison of instruction-following and success rate across methods and tasks. Breakdown for policy evaluation. We present the instruction-following and low-level execution success ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| The world model reliably captures instruction-following behavior but tends to underestimate the execution success rate. | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| We report instruction following rates and success rates in Figure 7 and visualize qualitative comparisons between real and imagined rollouts in Figure 6. | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| Spatial Shape Towel-Dir Novel-Obj Average 0.0 0.2 0.4 0.6 0.8 1.0 Success rate 0.29 0.44 0.57 0.25 0.39 0.88 0.91 0.80 0.75 0.83 Base ... | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| While the pretrained π0.5 policy achieves low success rates on unfamiliar objects and novel instructions, post-training aligns the model with new instructions and boosts ... | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| This includes about 76k successful and about 19k failed trajectories. | definition/direction/unit from same section | p. 5 (5 EXPERIMENTS) |
| (3) Can Ctrl-World improve a policy's instruction following by discovering and synthesizing successful trajectories entirely within its imagination? | definition/direction/unit from same section | p. 5 (5 EXPERIMENTS) |
| Removing memory mechanisms, frame-level action conditioning or multi-view joint predictions all lead to a performance drop. | definition/direction/unit from same section | p. 6 (5 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Consistent with observations from prior work (Quevedo et al., 2025; Zhu et al., 2024), we also find that these baselines struggle to capture robot-object ... | comparison identity and matched condition | p. 6 (5 EXPERIMENTS) |
| 5.2 WORLD MODEL QUALITY ANALYSIS Baselines and Evaluation Matrices. | comparison identity and matched condition | p. 5 (5 EXPERIMENTS) |
| As shown in Table 1, Ctrl-World-third-view outperforms these prior models, and multi-view joint prediction further improves generation quality. | comparison identity and matched condition | p. 6 (5 EXPERIMENTS) |
| 0.0 0.2 0.4 0.6 0.8 1.0 Instruction Following in Real World 0.0 0.2 0.4 0.6 0.8 1.0 in World Model y = 0.87x-0.04 0.0 ... | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |
| Published as a conference paper at ICLR 2026 Z axis -6 cm Z axis -6 cm Close Gripper Z axis +6 cm X axis ... | comparison identity and matched condition | p. 7 (5 EXPERIMENTS) |
| Similar to how prior works have seen DROID policies generalize to new setups (Pertsch et al., 2025), we find that Ctrl-World, pretrained solely on ... | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Published as a conference paper at ICLR 2026 Z axis -6 cm Z axis -6 cm Close Gripper Z axis +6 cm X axis ... | component/input/data sensitivity | p. 7 (5 EXPERIMENTS) |
| Figure 4: Controllability of Ctrl-World and ablations. Different action sequences can produce distinct rollouts in Ctrl-World with centimeter-level precision. Removing memory leads to blurry ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Evaluated Camera Method Computation-based Model-based PSNR ↑ SSIM ↑ LPIPS ↓ FID ↓ FVD ↓ Third-view Camera Ctrl-World 23.56 0.828 0.091 25.00 97.4 Ctrl-World ... | component/input/data sensitivity | p. 6 (5 EXPERIMENTS) |
| Ablations on memory components and frame-level conditions are in Table 2, which confirm the importance of each component. | component/input/data sensitivity | p. 8 (5 EXPERIMENTS) |
| Table 2: Ablations on key components in Ctrl-World. Removing memory mechanisms, frame-level action conditioning or multi-view joint predictions all lead to a performance drop. ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| We now evaluate whether Ctrl-World can be used to generate synthetic post-training data for improving VLA models without real-world data. | component/input/data sensitivity | p. 9 (5 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we introduce Ctrl-World, a Controllable, multi-view generative world model designed for policy-in-the-loop interaction, enabling multi-step rollouts entirely within imagination space, as ... | Spatial Shape Towel-Dir Novel-Obj Average 0.0 0.2 0.4 0.6 0.8 1.0 Success rate 0.29 0.44 0.57 0.25 0.39 0.88 0.91 0.80 0.75 0.83 Base ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 17 (Figure/Table caption), p. 5 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Primary metric/result | While the pretrained π0.5 policy achieves low success rates on unfamiliar objects and novel instructions, post-training aligns the model with new instructions and boosts ... | numeric claim only at cited anchor | p. 9 (5 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 5 / 5 EXPERIMENTS - extractive body cue:** The DROID dataset (Khazatsky et al., 2024) contains 95,599 diverse trajectories collected from 564 scenes, providing dense coverage of the workspace.
- **p. 5 / 5 EXPERIMENTS - extractive body cue:** The model is conditioned on a history of 7 frames, with an interval of 1-2 seconds between frames.
- **p. 5 / 5 EXPERIMENTS - extractive body cue:** During interaction, if a policy's output is less than 15 steps, we pad the action chunk with dummy actions and only use the predictions for ...
- **p. 5 / 5 EXPERIMENTS - extractive body cue:** We train the model on 2×8 H100 GPUs, with a total batch size of 64.
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** For evaluation, we hold out 2% of the trajectories as a validation set and randomly sample 256 video clips, each 10 s in length.
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** During rollouts, the world model receives 15-step action chunks (corresponding to 1 s) and autoregressively predicts the next frames for 10 steps, producing 10 s-long ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Published as a conference paper at ICLR 2026 These limitations may diminish as video backbones become more physically accurate and coherent over time (Ball ... | p. 10 (6 CONCLUSION) |
| body limitation/failure cue | The inclusion of diverse actions and failure data is crucial, as it allows us to train a controllable world model that can simulate a ... | p. 5 (5 EXPERIMENTS) |
| body limitation/failure cue | Although some failure trajectories are included in the DROID dataset, there are still many failure modes outside the data distribution. | p. 9 (5 EXPERIMENTS) |
| body limitation/failure cue | Table 3: Comparison of instruction-following and success rate across methods and tasks. Breakdown for policy evaluation. We present the instruction-following and low-level execution success ... | p. 17 (Figure/Table caption) |
| body limitation/failure cue | Published as a conference paper at ICLR 2026 precise modeling of complex physics dynamics such as collisions, objects sliding away, rotations, etc. | p. 9 (5 EXPERIMENTS) |
| body limitation/failure cue | This includes about 76k successful and about 19k failed trajectories. | p. 5 (5 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We train the model on 2×8 H100 GPUs, with a total batch size of 64. | p. 5 (5 EXPERIMENTS) |
| During interaction, if a policy's output is less than 15 steps, we pad the action chunk with dummy actions and only use the predictions ... | p. 5 (5 EXPERIMENTS) |
| During rollouts, the world model receives 15-step action chunks (corresponding to 1 s) and autoregressively predicts the next frames for 10 steps, producing 10 ... | p. 6 (5 EXPERIMENTS) |
| Finally, we fine-tune the policy on the curated synthetic dataset for 2k steps, improving base model's capability in unfamiliar instructions and objects. | p. 9 (5 EXPERIMENTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 6 CONCLUSION - extractive body cue:** Published as a conference paper at ICLR 2026 These limitations may diminish as video backbones become more physically accurate and coherent over time (Ball et ...
- **p. 5 / 5 EXPERIMENTS - extractive body cue:** The inclusion of diverse actions and failure data is crucial, as it allows us to train a controllable world model that can simulate a wide ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Although some failure trajectories are included in the DROID dataset, there are still many failure modes outside the data distribution.
- **p. 17 / Figure/Table caption - extractive body cue:** Table 3: Comparison of instruction-following and success rate across methods and tasks. Breakdown for policy evaluation. We present the instruction-following and low-level execution success rates ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Published as a conference paper at ICLR 2026 precise modeling of complex physics dynamics such as collisions, objects sliding away, rotations, etc.
- **p. 5 / 5 EXPERIMENTS - extractive body cue:** This includes about 76k successful and about 19k failed trajectories.

- **PDF anchors reviewed:** datasets p. 5 (5 EXPERIMENTS), p. 5 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), metrics p. 17 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 5 (5 EXPERIMENTS), baselines p. 6 (5 EXPERIMENTS), p. 5 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), results p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 17 (Figure/Table caption), p. 5 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
