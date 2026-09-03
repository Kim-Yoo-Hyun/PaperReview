# Evaluation - PolicyTrim: Boosting Intrinsic Policy Efficiency of Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2606.22540; PDF retrieval source: https://arxiv.org/pdf/2606.22540. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (4 Experiment), p. 12 (Figure/Table caption), p. 12 (Figure/Table caption), p. 25 (Figure/Table caption), p. 11 (Figure/Table caption), p. 2 (Figure/Table caption)): Reported metrics include average success rate, average physical steps, average action chunk execution length, end-to-end execution speedup, and wall-clock execution time for real-world deployment. • LIBERO is a tabletop manipulation ...

## Evaluation Body Digest

- **p. 9 / 4 Experiment - extractive body cue:** We evaluate on three diverse benchmarks including LIBERO [25], ManiSkill [41], Meta-World [30] and further validate its sim-to-real transfer on a physical robot platform.
- **p. 9 / 4 Experiment - extractive body cue:** Reported metrics include average success rate, average physical steps, average action chunk execution length, end-to-end execution speedup, and wall-clock execution time for real-world deployment. • ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: Intrinsic policy inefficiency in deployed VLA models manifests along two di- mensions. (a) Repeated rollouts on identical tasks reveal substantial variance in step ...
- **p. 25 / Figure/Table caption - extractive body cue:** Table 10: Simulation robustness results on LIBERO-Spatial under visual perturba- tions. We report SR / Step, where SR is success rate in % and Step ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 1: Evaluation of π0.5, OpenVLA-OFT, and GR00T on the four subsets of the LIBERO benchmark. We report average success rate (SR), average physical steps ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 3: Cross-architecture results. We report success rate (SR), average physical steps, action horizon h, and end-to-end speedup.
- **p. 12 / Figure/Table caption - extractive body cue:** Table 4: Real-world deployment results. Standard uses a fixed target pose, while Dynamic perturbs the target during grasping. Values under Standard and Dynamic are success ...
- **p. 26 / Figure/Table caption - extractive body cue:** Table 11: Horizon-sweep baseline for π0.5. Fixed larger horizons degrade success rate, while PolicyTrim learns to extend the reliable horizon through RL post-training.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 Experiment (p. 9); B Implementation Details (p. 21); C Additional Results (p. 22); C.1 Qualitative Results (p. 22).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | Reported metrics include average success rate, average physical steps, average action chunk execution length, end-to-end execution speedup, and wall-clock execution time for real-world deployment. ... | p. 9 (4 Experiment) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 3: Cross-architecture results. We report success rate (SR), average physical steps, action horizon h, and end-to-end speedup. | p. 12 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 4: Real-world deployment results. Standard uses a fixed target pose, while Dynamic perturbs the target during grasping. Values under Standard and Dynamic are ... | p. 12 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 10: Simulation robustness results on LIBERO-Spatial under visual perturba- tions. We report SR / Step, where SR is success rate in % and ... | p. 25 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 3: Qualitative comparison on randomly sampled LIBERO tasks. Under identi- cal configurations, the baseline incurs redundant physical actions, whereas PolicyTrim achieves task completion ... | p. 11 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 9 / 4 Experiment - extractive body cue:** We evaluate on three diverse benchmarks including LIBERO [25], ManiSkill [41], Meta-World [30] and further validate its sim-to-real transfer on a physical robot platform.
- **p. 9 / 4 Experiment - extractive body cue:** Reported metrics include average success rate, average physical steps, average action chunk execution length, end-to-end execution speedup, and wall-clock execution time for real-world deployment. • ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: Intrinsic policy inefficiency in deployed VLA models manifests along two di- mensions. (a) Repeated rollouts on identical tasks reveal substantial variance in step ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 2: Overview of PolicyTrim. PolicyTrim is a two-stage RL post-training frame- work that enhances intrinsic policy efficiency of VLA models. The first stage progres- ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 1: Evaluation of π0.5, OpenVLA-OFT, and GR00T on the four subsets of the LIBERO benchmark. We report average success rate (SR), average physical steps ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 2: Evaluation on ManiSkill and Meta-World. We report average success rate (SR), average physical steps (Stotal), average action chunk execution length (hchunk), and end-to-end ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 3: Qualitative comparison on randomly sampled LIBERO tasks. Under identi- cal configurations, the baseline incurs redundant physical actions, whereas PolicyTrim achieves task completion in ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 3: Cross-architecture results. We report success rate (SR), average physical steps, action horizon h, and end-to-end speedup.
- **p. 12 / Figure/Table caption - extractive body cue:** Table 4: Real-world deployment results. Standard uses a fixed target pose, while Dynamic perturbs the target during grasping. Values under Standard and Dynamic are success ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 5: Ablation study of different components on LIBERO-Spatial benchmarks. Reliable Chunk Step-Saving Group-Anchored SR Stotal hchunk Spd↑

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate on three diverse benchmarks including LIBERO [25], ManiSkill [41], Meta-World [30] and further validate its sim-to-real transfer on a physical robot platform. | embodiment, simulator version and control stack | p. 9 (4 Experiment), p. 9 (4 Experiment) |
| Task/environment | Reported metrics include average success rate, average physical steps, average action chunk execution length, end-to-end execution speedup, and wall-clock execution time for real-world deployment. ... | reset, timeout, object/scene variation | p. 9 (4 Experiment) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 5 (3 Method), p. 4 (X. Wang et al) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (Body text (section not recovered)), p. 15 (2.48 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 1: Intrinsic policy inefficiency in deployed VLA models manifests along two di- mensions. (a) Repeated rollouts on identical tasks reveal substantial variance in ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Reported metrics include average success rate, average physical steps, average action chunk execution length, end-to-end execution speedup, and wall-clock execution time for real-world deployment. ... | definition/direction/unit from same section | p. 9 (4 Experiment) |
| Table 10: Simulation robustness results on LIBERO-Spatial under visual perturba- tions. We report SR / Step, where SR is success rate in % and ... | definition/direction/unit from same section | p. 25 (Figure/Table caption) |
| Table 1: Evaluation of π0.5, OpenVLA-OFT, and GR00T on the four subsets of the LIBERO benchmark. We report average success rate (SR), average physical ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| Table 3: Cross-architecture results. We report success rate (SR), average physical steps, action horizon h, and end-to-end speedup. | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| Table 4: Real-world deployment results. Standard uses a fixed target pose, while Dynamic perturbs the target during grasping. Values under Standard and Dynamic are ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| Table 11: Horizon-sweep baseline for π0.5. Fixed larger horizons degrade success rate, while PolicyTrim learns to extend the reliable horizon through RL post-training. | definition/direction/unit from same section | p. 26 (Figure/Table caption) |
| Fig. 2: Overview of PolicyTrim. PolicyTrim is a two-stage RL post-training frame- work that enhances intrinsic policy efficiency of VLA models. The first stage ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 3: Qualitative comparison on randomly sampled LIBERO tasks. Under identi- cal configurations, the baseline incurs redundant physical actions, whereas PolicyTrim achieves task completion ... | comparison identity and matched condition | p. 11 (Figure/Table caption) |
| Fig. 5: Qualitative comparisons on GR00T and OpenVLA-OFT. For each instruction, we compare execution snapshots of the baseline policy and PolicyTrim. Across both backbones, ... | comparison identity and matched condition | p. 23 (Figure/Table caption) |
| Table 11: Horizon-sweep baseline for π0.5. Fixed larger horizons degrade success rate, while PolicyTrim learns to extend the reliable horizon through RL post-training. | comparison identity and matched condition | p. 26 (Figure/Table caption) |
| Table 5: Ablation study of different components on LIBERO-Spatial benchmarks. Reliable Chunk Step-Saving Group-Anchored SR Stotal hchunk Spd↑ | comparison identity and matched condition | p. 13 (Figure/Table caption) |
| Table 6: Ablation of Dynamic Execution Horizon Exploration on LIBERO-Object using π0.5 with H = 20. Fixed-γ variants replace diverse ratio sampling with a ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |
| We applied group-relative reward normalization and updated the policy directly from rollout returns, without a critic | comparison identity and matched condition | p. 21 (B Implementation Details) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 6: Ablation of Dynamic Execution Horizon Exploration on LIBERO-Object using π0.5 with H = 20. Fixed-γ variants replace diverse ratio sampling with a ... | component/input/data sensitivity | p. 13 (Figure/Table caption) |
| Fig. 7: Failure case without group-anchored stability regularization. The pol- icy approaches the bowl with insufficient clearance, causing a collision and task failure. In ... | component/input/data sensitivity | p. 27 (Figure/Table caption) |
| Table 5: Ablation study of different components on LIBERO-Spatial benchmarks. Reliable Chunk Step-Saving Group-Anchored SR Stotal hchunk Spd↑ | component/input/data sensitivity | p. 13 (Figure/Table caption) |
| Fig. 4: Training reward curves with- out (Left) and with (Right) Group- Anchored Regularization on LIBERO- Spatial (π0.5). Effect of Group-Anchored Regularization. When Group-Anchored ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| We applied group-relative reward normalization and updated the policy directly from rollout returns, without a critic | component/input/data sensitivity | p. 21 (B Implementation Details) |
| Table 8: Ablation on group size G for π0.5 on the four LIBERO subsets. We report success rate (SR), average physical steps (Stotal), average ... | component/input/data sensitivity | p. 24 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The main contributions of this work are summarized as follows: - We identify policy efficiency as a critical yet overlooked deployment bottleneck for VLA ... | Reported metrics include average success rate, average physical steps, average action chunk execution length, end-to-end execution speedup, and wall-clock execution time for real-world deployment. ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (4 Experiment), p. 12 (Figure/Table caption), p. 12 (Figure/Table caption), p. 25 (Figure/Table caption), p. 11 (Figure/Table caption), p. 2 (Figure/Table caption) |
| Primary metric/result | Table 3: Cross-architecture results. We report success rate (SR), average physical steps, action horizon h, and end-to-end speedup. | numeric claim only at cited anchor | p. 12 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 9 / 4 Experiment - extractive body cue:** We use a group size of G = 8 trajectories for each task in every iteration.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 7: Failure case without group-anchored stability regularization. The pol- icy approaches the bowl with insufficient clearance, causing a collision and task failure. In ... | p. 27 (Figure/Table caption) |
| body limitation/failure cue | Fig. 1: Intrinsic policy inefficiency in deployed VLA models manifests along two di- mensions. (a) Repeated rollouts on identical tasks reveal substantial variance in ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Fig. 6: Real-world execution visualization on the FlipMug task. C.5 Robustness under Visual Perturbations We further evaluate PolicyTrim under visual distribution shifts in simulation. ... | p. 25 (Figure/Table caption) |
| body limitation/failure cue | Table 10: Simulation robustness results on LIBERO-Spatial under visual perturba- tions. We report SR / Step, where SR is success rate in % and ... | p. 25 (Figure/Table caption) |
| body limitation/failure cue | Table 11: Horizon-sweep baseline for π0.5. Fixed larger horizons degrade success rate, while PolicyTrim learns to extend the reliable horizon through RL post-training. | p. 26 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For all VLA models, the maximum chunk capacity H predicted at each step is initialized to match or exceed the original settings of the ... | p. 9 (4 Experiment) |
| Reported metrics include average success rate, average physical steps, average action chunk execution length, end-to-end execution speedup, and wall-clock execution time for real-world deployment. ... | p. 9 (4 Experiment) |
| We propose a two-stage posttraining framework that extends the executable action horizon per inference and reduces the number of steps required to complete a ... | p. 5 (3 Method) |
| Orthogonality with Compute-centric Methods. | p. 15 (2.48 Method) |
| Moreover, prediction errors accumulate along action chunks due to distribution shift, causing the policy to take redundant corrective actions that further inflate the total ... | p. 15 (2.48 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 27 / Figure/Table caption - extractive body cue:** Fig. 7: Failure case without group-anchored stability regularization. The pol- icy approaches the bowl with insufficient clearance, causing a collision and task failure. In this ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: Intrinsic policy inefficiency in deployed VLA models manifests along two di- mensions. (a) Repeated rollouts on identical tasks reveal substantial variance in step ...
- **p. 25 / Figure/Table caption - extractive body cue:** Fig. 6: Real-world execution visualization on the FlipMug task. C.5 Robustness under Visual Perturbations We further evaluate PolicyTrim under visual distribution shifts in simulation. Specifically, ...
- **p. 25 / Figure/Table caption - extractive body cue:** Table 10: Simulation robustness results on LIBERO-Spatial under visual perturba- tions. We report SR / Step, where SR is success rate in % and Step ...
- **p. 26 / Figure/Table caption - extractive body cue:** Table 11: Horizon-sweep baseline for π0.5. Fixed larger horizons degrade success rate, while PolicyTrim learns to extend the reliable horizon through RL post-training.

- **Evidence anchors reviewed:** datasets p. 9 (4 Experiment), p. 9 (4 Experiment), metrics p. 2 (Figure/Table caption), p. 9 (4 Experiment), p. 25 (Figure/Table caption), p. 10 (Figure/Table caption), p. 12 (Figure/Table caption), p. 12 (Figure/Table caption), baselines p. 11 (Figure/Table caption), p. 23 (Figure/Table caption), p. 26 (Figure/Table caption), p. 13 (Figure/Table caption), p. 13 (Figure/Table caption), p. 21 (B Implementation Details), results p. 9 (4 Experiment), p. 12 (Figure/Table caption), p. 12 (Figure/Table caption), p. 25 (Figure/Table caption), p. 11 (Figure/Table caption), p. 2 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
