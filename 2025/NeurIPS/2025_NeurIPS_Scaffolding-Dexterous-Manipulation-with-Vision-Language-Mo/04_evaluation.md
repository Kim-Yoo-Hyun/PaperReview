# Evaluation - Scaffolding Dexterous Manipulation with Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (29 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=PdRf0O7baQ; PDF retrieval source: https://arxiv.org/pdf/2506.19212.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 23 (Figure/Table caption), p. 9 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 7 (4 Experiments)): Figure 5: (Left) The performance of our method as we iteratively refine the high-level policy πh by providing successful plans τ in-context. (Right) The projected 3D plans on the evaluation ...

## Evaluation Body Digest

- **p. 9 / 4 Experiments - extractive body cue:** The low-level policy is trained entirely in simulation using a digital twin of the real-world environment, and then executed in the real-world, conditioned on the ...
- **p. 9 / 4 Experiments - extractive body cue:** To evaluate sim-to-real transfer, we deploy our system on a real robot using the same inference pipeline as in simulation.
- **p. 7 / 4 Experiments - extractive body cue:** 4.1 Experimental Setup Task Suite We construct an evaluation suite using the ManiSkill simulator [45, 62] and Allegro Hand model designed to evaluate four core ...
- **p. 7 / 4 Experiments - extractive body cue:** We run 20 trials for each configuration for a total of 2000 evaluation episodes and average results across three seeds.
- **p. 8 / 4 Experiments - extractive body cue:** 4 shows the success rates for the different simulation tasks.
- **p. 8 / 4 Experiments - extractive body cue:** Pre-recorded IKER (Zero-Shot) Ours (Zero-Shot) Ours (Few-Shot) Oracle Success Rate (%) 13 45 84 87 95 Apple 25 63 88 86 96 Bottle 49 23 ...
- **p. 6 / 4 Experiments - extractive body cue:** We conduct a comprehensive suite of experiments to assess the effectiveness, generality, and robustness of our method across a diverse range of dexterous manipulation tasks.
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 9: Results on the simulation task suite. Success rate (in %) is averaged across three seeds; uncertainty reflects the standard error. Our method performs ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 Experiments (p. 6); C Hardware Experiment Details (p. 18).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5: (Left) The performance of our method as we iteratively refine the high-level policy πh by providing successful plans τ in-context. (Right) The ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 11: Effect of Gaussian noise on VLM predictions in the simulation task suite. Success rate (in %) is averaged across three seeds; uncertainty ... | p. 23 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | The resulting improvements vary across tasks: in the drawer task, the Traj. oracle achieves near perfect performance indicating planning was the bottleneck, however, in ... | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | After iterative refinement, the overall success rate improves to 81%. | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our system achieves a 90% success rate on Place Bottle onto Plate, 85% on Slide Box to Bottle, and 65% on Hammer Three Times. | p. 9 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 9 / 4 Experiments - extractive body cue:** The low-level policy is trained entirely in simulation using a digital twin of the real-world environment, and then executed in the real-world, conditioned on the ...
- **p. 9 / 4 Experiments - extractive body cue:** To evaluate sim-to-real transfer, we deploy our system on a real robot using the same inference pipeline as in simulation.
- **p. 7 / 4 Experiments - extractive body cue:** 4.1 Experimental Setup Task Suite We construct an evaluation suite using the ManiSkill simulator [45, 62] and Allegro Hand model designed to evaluate four core ...
- **p. 7 / 4 Experiments - extractive body cue:** We run 20 trials for each configuration for a total of 2000 evaluation episodes and average results across three seeds.
- **p. 8 / 4 Experiments - extractive body cue:** 4 shows the success rates for the different simulation tasks.
- **p. 8 / 4 Experiments - extractive body cue:** Pre-recorded IKER (Zero-Shot) Ours (Zero-Shot) Ours (Few-Shot) Oracle Success Rate (%) 13 45 84 87 95 Apple 25 63 88 86 96 Bottle 49 23 ...
- **p. 6 / 4 Experiments - extractive body cue:** We conduct a comprehensive suite of experiments to assess the effectiveness, generality, and robustness of our method across a diverse range of dexterous manipulation tasks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Overview of our method: a VLM generates hand and object keypoint trajectories from a language command and scene image. A low-level residual RL ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: a) Training: a high-level VLM predicts 3D keypoint plans, which a low-level policy learns to track via RL. b) Inference: new plans are ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: A depiction of the eight tasks used for evaluation. Each task belongs to one of four overarching categories. Methods Given the novelty of ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Results on the simulation task suite. Success rate (in %) is averaged across 3 seeds and uncertainty is given by the standard error. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: (Left) The performance of our method as we iteratively refine the high-level policy πh by providing successful plans τ in-context. (Right) The projected ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 5. All tasks show an increase in the success rate after the first iteration, with diminishing returns after the second iteration. This is likely ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Error decomposition across failure cases. Most errors stem from incomplete trajectory tracking, followed by keypoint detection issues. Failure Modes. To comprehensively evaluate the ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 7: (Left) Task success vs. number of waypoints in VLM plans. Most tasks saturate by 10 waypoints; only the hammer task benefits from denser ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The low-level policy is trained entirely in simulation using a digital twin of the real-world environment, and then executed in the real-world, conditioned on ... | embodiment, simulator version and control stack | p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Task/environment | To evaluate sim-to-real transfer, we deploy our system on a real robot using the same inference pipeline as in simulation. | reset, timeout, object/scene variation | p. 9 (4 Experiments), p. 7 (4 Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 5 (2. Plan Generation 𝜏), p. 5 (2. Plan Generation 𝜏) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (1 Introduction), p. 6 (2. Plan Generation 𝜏) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 9: Results on the simulation task suite. Success rate (in %) is averaged across three seeds; uncertainty reflects the standard error. Our method ... | definition/direction/unit from same section | p. 22 (Figure/Table caption) |
| Figure 11: Effect of Gaussian noise on VLM predictions in the simulation task suite. Success rate (in %) is averaged across three seeds; uncertainty ... | definition/direction/unit from same section | p. 23 (Figure/Table caption) |
| Fig. 5. All tasks show an increase in the success rate after the first iteration, with diminishing returns after the second iteration. This is ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Our method with few-shot adaptation achieves consistently high success rates, with an average success rate of 72%, often approaching the performance of the oracle ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Our system achieves a 90% success rate on Place Bottle onto Plate, 85% on Slide Box to Bottle, and 65% on Hammer Three Times. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Oracle Keypoint Oracle Success Rate (%) 84 91 90 Apple 87 99 82 Drawer 87 91 96 Sponge 80 90 85 Pliers Figure 7: ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Thus, we mainly focus our experiments on comparison with a variety of oracles and ablations: • Iterative Keypoint Rewards (IKER): We implement Iterative Keypoint ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Crucially, the capabilities evaluated by our task set are difficult to design reward functions for (articulated object manipulation or requiring complex and unstructured motion) ... | definition/direction/unit from same section | p. 7 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 3: A depiction of the eight tasks used for evaluation. Each task belongs to one of four overarching categories. Methods Given the novelty ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Since IKER assumes a fixed set of keypoints, we adopt the same VLM-identified keypoints used by our system to ensure parity. • Pre-recorded Trajectories: ... | comparison identity and matched condition | p. 7 (4 Experiments) |
| Figure 9: Results on the simulation task suite. Success rate (in %) is averaged across three seeds; uncertainty reflects the standard error. Our method ... | comparison identity and matched condition | p. 22 (Figure/Table caption) |
| Our method with few-shot adaptation achieves consistently high success rates, with an average success rate of 72%, often approaching the performance of the oracle ... | comparison identity and matched condition | p. 8 (4 Experiments) |
| Performance of the pre-recorded baseline remains poor for all tasks, except in the drawer task, where the novel plans are likely less important at ... | comparison identity and matched condition | p. 8 (4 Experiments) |
| For the Traj. oracle, we use VLM keypoints but script plans for τ. | comparison identity and matched condition | p. 9 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 11: Effect of Gaussian noise on VLM predictions in the simulation task suite. Success rate (in %) is averaged across three seeds; uncertainty ... | component/input/data sensitivity | p. 23 (Figure/Table caption) |
| (Right) Ablation of VLM components. | component/input/data sensitivity | p. 9 (4 Experiments) |
| Thus, we mainly focus our experiments on comparison with a variety of oracles and ablations: • Iterative Keypoint Rewards (IKER): We implement Iterative Keypoint ... | component/input/data sensitivity | p. 7 (4 Experiments) |
| We compare against additional reinforcement learning and imitation learning baselines and additionally ablate adding systematic noise into VLM predictions in Section E We evaluate ... | component/input/data sensitivity | p. 7 (4 Experiments) |
| To ablate the impact of using a VLM for keypoint detection and plan generation, we replace each component with an oracle in Fig. | component/input/data sensitivity | p. 9 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Moreover, we showcase that our method transfers to realworld robotic hands without any human demonstrations or handcrafted rewards. | Figure 5: (Left) The performance of our method as we iteratively refine the high-level policy πh by providing successful plans τ in-context. (Right) The ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 23 (Figure/Table caption), p. 9 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 7 (4 Experiments) |
| Primary metric/result | Figure 11: Effect of Gaussian noise on VLM predictions in the simulation task suite. Success rate (in %) is averaged across three seeds; uncertainty ... | numeric claim only at cited anchor | p. 23 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Experiments - extractive body cue:** Since IKER assumes a fixed set of keypoints, we adopt the same VLM-identified keypoints used by our system to ensure parity. • Pre-recorded Trajectories: This ...
- **p. 7 / 4 Experiments - extractive body cue:** We use Gemini 2.5 Flash Thinking [63] as the high-level policy with a thinking budget of 1000 tokens for plan generation.
- **p. 7 / 4 Experiments - extractive body cue:** We run 20 trials for each configuration for a total of 2000 evaluation episodes and average results across three seeds.
- **p. 8 / 4 Experiments - extractive body cue:** Success rate (in %) is averaged across 3 seeds and uncertainty is given by the standard error.
- **p. 9 / 4 Experiments - extractive body cue:** In 3 of 4 tasks, performance saturates with 10 waypoints.
- **p. 9 / 4 Experiments - extractive body cue:** Each task is executed for 20 rollouts.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | To comprehensively evaluate the failure modes of our pipeline across all tasks, we present a Sankey diagram in Fig. | p. 8 (4 Experiments) |
| body limitation/failure cue | Our analysis reveals that the most significant failure mode is incomplete trajectory tracking, occurring in 26% of the rollouts. | p. 8 (4 Experiments) |
| body limitation/failure cue | Figure 9: Results on the simulation task suite. Success rate (in %) is averaged across three seeds; uncertainty reflects the standard error. Our method ... | p. 22 (Figure/Table caption) |
| body limitation/failure cue | We conduct a comprehensive suite of experiments to assess the effectiveness, generality, and robustness of our method across a diverse range of dexterous manipulation ... | p. 6 (4 Experiments) |
| body limitation/failure cue | 3) What causes VLM scaffolds to fail? | p. 7 (4 Experiments) |
| body limitation/failure cue | We compare against additional reinforcement learning and imitation learning baselines and additionally ablate adding systematic noise into VLM predictions in Section E We evaluate ... | p. 7 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We run 20 trials for each configuration for a total of 2000 evaluation episodes and average results across three seeds. | p. 7 (4 Experiments) |
| Additional implementation and hardware details are provided in Section C. | p. 9 (4 Experiments) |
| Thus, we mainly focus our experiments on comparison with a variety of oracles and ablations: • Iterative Keypoint Rewards (IKER): We implement Iterative Keypoint ... | p. 7 (4 Experiments) |
| Success rate (in %) is averaged across 3 seeds and uncertainty is given by the standard error. | p. 8 (4 Experiments) |
| Our key insight is that modern vision-language models (VLMs) already encode the commonsense spatial and semantic knowledge needed to specify tasks and guide exploration ... | p. 1 (Abstract) |
| The prevailing approach for training generalist policies - imitation learning from demonstrations [5, 49] - has achieved limited success with robot hands, primarily due ... | p. 1 (1 Introduction) |
| Further training details and hyperparameters are in Section A. | p. 6 (2. Plan Generation 𝜏) |
| Practically, πl is implemented as a multi-layer perceptron where keypoints are provided in a fixed order and future planning steps τt:T are down-sampled to ... | p. 6 (2. Plan Generation 𝜏) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4 Experiments - extractive body cue:** To comprehensively evaluate the failure modes of our pipeline across all tasks, we present a Sankey diagram in Fig.
- **p. 8 / 4 Experiments - extractive body cue:** Our analysis reveals that the most significant failure mode is incomplete trajectory tracking, occurring in 26% of the rollouts.
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 9: Results on the simulation task suite. Success rate (in %) is averaged across three seeds; uncertainty reflects the standard error. Our method performs ...
- **p. 6 / 4 Experiments - extractive body cue:** We conduct a comprehensive suite of experiments to assess the effectiveness, generality, and robustness of our method across a diverse range of dexterous manipulation tasks.
- **p. 7 / 4 Experiments - extractive body cue:** 3) What causes VLM scaffolds to fail?
- **p. 7 / 4 Experiments - extractive body cue:** We compare against additional reinforcement learning and imitation learning baselines and additionally ablate adding systematic noise into VLM predictions in Section E We evaluate two ...

- **Evidence anchors reviewed:** datasets p. 9 (4 Experiments), p. 9 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), metrics p. 22 (Figure/Table caption), p. 23 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), baselines p. 7 (Figure/Table caption), p. 7 (4 Experiments), p. 22 (Figure/Table caption), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), results p. 8 (Figure/Table caption), p. 23 (Figure/Table caption), p. 9 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 7 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
