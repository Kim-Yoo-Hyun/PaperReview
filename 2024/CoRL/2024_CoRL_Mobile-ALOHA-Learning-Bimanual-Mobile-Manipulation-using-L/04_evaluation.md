# Evaluation - Mobile ALOHA: Learning Bimanual Mobile Manipulation using Low-Cost Whole-Body Teleoperation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2401.02117; PDF retrieval source: https://arxiv.org/pdf/2401.02117. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (6.1. Co-training Improves Performance), p. 7 (Figure/Table caption), p. 9 (Figure/Table caption), p. 9 (6.1. Co-training Improves Performance), p. 8 (6.1. Co-training Improves Performance)): Co-training improves the whole-task success rate in 5 out of the 7 tasks, with a boost of 45%, 20%, 80%, 95% and 80% respectively.

## Evaluation Body Digest

- **p. 8 / 6.1. Co-training Improves Performance - extractive body cue:** We then evaluate each policy in the real-world, with randomization of robot and objects configurations as described in Figure 3.
- **p. 8 / 6.1. Co-training Improves Performance - extractive body cue:** For example in the case of Lift Glass and Wipe sub-task, the #Attempts equals the number of success from the previous subtask Grasp Towel, as ...
- **p. 9 / 6.1. Co-training Improves Performance - extractive body cue:** In Table 2, we report co-training and no cotraining success rates on 2 real-world tasks: Wipe Wine and Push Chairs.
- **p. 9 / 6.1. Co-training Improves Performance - extractive body cue:** VINN trains a visual representation model, BYOL [37] and uses it to retrieve actions from the demonstration dataset with nearest neighbors.
- **p. 10 / 6.1. Co-training Improves Performance - extractive body cue:** New users can quickly approach expert speed on an unseen tasks teleoperating Mobile ALOHA .
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Co-training improves ACT performance. Across 7 challenging mobile manipulation tasks, co-training with static ALOHA dataset consistently improve the success rate (%) of ACT. ...
- **p. 8 / 6.1. Co-training Improves Performance - extractive body cue:** To calculate the success rate for a sub-task, we divide #Success by #Attempts.
- **p. 9 / 6.1. Co-training Improves Performance - extractive body cue:** For VINN + Chunking, the policy performs worse than ACT or Diffusion across the board, while still reaching reasonable success rates with 60% on Push ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mobile base와 one/two-arm manipulation environment.
- **Input boundary:** egocentric RGB-D, language/task goal, base-arm proprioception.
- **Output/decision under evaluation:** base motion plus arm/gripper action.
- **Primary target:** long-horizon task success, reachability, collision과 recovery.
- **Detected evaluation headings:** 6. Experiments (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 6.1. Co-training Improves Performance | EMPIRICAL / REAL-ROBOT OR HARDWARE | Co-training improves the whole-task success rate in 5 out of the 7 tasks, with a boost of 45%, 20%, 80%, 95% and 80% respectively. | p. 8 (6.1. Co-training Improves Performance) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1: Co-training improves ACT performance. Across 7 challenging mobile manipulation tasks, co-training with static ALOHA dataset consistently improve the success rate (%) of ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 4: Co-train vs. Pre-train. Co-train outperforms pre-train on the Wipe Wine task. For pre-train, we first train ACT on the static ALOHA data ... | p. 9 (Figure/Table caption) |
| 6.1. Co-training Improves Performance | EMPIRICAL / REAL-ROBOT OR HARDWARE | We find co-training to improve Diffusion Policy's performance, by 30% and 20% for on Wipe Wine and Push Chairs respectively. | p. 9 (6.1. Co-training Improves Performance) |
| 6.1. Co-training Improves Performance | EMPIRICAL / REAL-ROBOT OR HARDWARE | To calculate the success rate for a sub-task, we divide #Success by #Attempts. | p. 8 (6.1. Co-training Improves Performance) |

## Dataset / Benchmark Role

- **p. 8 / 6.1. Co-training Improves Performance - extractive body cue:** We then evaluate each policy in the real-world, with randomization of robot and objects configurations as described in Figure 3.
- **p. 8 / 6.1. Co-training Improves Performance - extractive body cue:** For example in the case of Lift Glass and Wipe sub-task, the #Attempts equals the number of success from the previous subtask Grasp Towel, as ...
- **p. 9 / 6.1. Co-training Improves Performance - extractive body cue:** In Table 2, we report co-training and no cotraining success rates on 2 real-world tasks: Wipe Wine and Push Chairs.
- **p. 9 / 6.1. Co-training Improves Performance - extractive body cue:** VINN trains a visual representation model, BYOL [37] and uses it to retrieve actions from the demonstration dataset with nearest neighbors.
- **p. 10 / 6.1. Co-training Improves Performance - extractive body cue:** New users can quickly approach expert speed on an unseen tasks teleoperating Mobile ALOHA .

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Mobile ALOHA . We introduce a low-cost mobile manipulation system that is bimanual and supports whole-body teleoperation. The system costs $32k including onboard ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Hardware Details. Left: Mobile ALOHA has two wrist cameras and one top camera, with onboard power and compute. Middle: The teleoperation setup can ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Task Definitions. We illustrate 6 real-world tasks that Mobile ALOHA can perform autonomously. The 7th task High Five is illustrated in the Appendix ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Co-training improves ACT performance. Across 7 challenging mobile manipulation tasks, co-training with static ALOHA dataset consistently improve the success rate (%) of ACT. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Mobile ALOHA is compatible with recent imitation learning methods. VINN with chunking, Diffusion Policy, and ACT all achieves good performance on Mobile ALOHA, ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Data efficiency. Co-training with static ALOHA data leads to better data efficiency and consistent improvements over training with Mobile ALOHA data only. Figure ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Co-training is robust to different data mix- tures. Result uses ACT training on the Wipe Wine task. Co-train Pre-train No Co-train No Pre-train ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: Co-train vs. Pre-train. Co-train outperforms pre-train on the Wipe Wine task. For pre-train, we first train ACT on the static ALOHA data and ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We then evaluate each policy in the real-world, with randomization of robot and objects configurations as described in Figure 3. | embodiment, simulator version and control stack | p. 8 (6.1. Co-training Improves Performance), p. 8 (6.1. Co-training Improves Performance) |
| Task/environment | For example in the case of Lift Glass and Wipe sub-task, the #Attempts equals the number of success from the previous subtask Grasp Towel, ... | reset, timeout, object/scene variation | p. 8 (6.1. Co-training Improves Performance), p. 9 (6.1. Co-training Improves Performance) |
| Observation/sensor | egocentric RGB-D, language/task goal, base-arm proprioception | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 4 (3. Mobile ALOHA Hardware) |
| Output/decision | base motion plus arm/gripper action | action frame, controller and termination | p. 2 (1. Introduction), p. 4 (3. Mobile ALOHA Hardware) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 1: Co-training improves ACT performance. Across 7 challenging mobile manipulation tasks, co-training with static ALOHA dataset consistently improve the success rate (%) of ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| We report all success rates in Table 1. | definition/direction/unit from same section | p. 8 (6.1. Co-training Improves Performance) |
| To calculate the success rate for a sub-task, we divide #Success by #Attempts. | definition/direction/unit from same section | p. 8 (6.1. Co-training Improves Performance) |
| For VINN + Chunking, the policy performs worse than ACT or Diffusion across the board, while still reaching reasonable success rates with 60% on ... | definition/direction/unit from same section | p. 9 (6.1. Co-training Improves Performance) |
| Figure 2: Hardware Details. Left: Mobile ALOHA has two wrist cameras and one top camera, with onboard power and compute. Middle: The teleoperation setup ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 8: Open-lopp Replay Errors. We mark the right arm end-effector position on a piece of paper for the original episode (red cross), and ... | definition/direction/unit from same section | p. 20 (Figure/Table caption) |
| Co-train Pre-train No Co-train No Pre-train Success (%) 95 40 50 Table 4: Co-train vs. | definition/direction/unit from same section | p. 9 (6.1. Co-training Improves Performance) |
| Figure 1: Mobile ALOHA . We introduce a low-cost mobile manipulation system that is bimanual and supports whole-body teleoperation. The system costs $32k including ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Co-train outperforms pre-train on the Wipe Wine task. | comparison identity and matched condition | p. 9 (6.1. Co-training Improves Performance) |
| We start with ACT [104], the method introduced with ALOHA, and train it on all 7 tasks with and without co-training. | comparison identity and matched condition | p. 8 (6.1. Co-training Improves Performance) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We start with ACT [104], the method introduced with ALOHA, and train it on all 7 tasks with and without co-training. | component/input/data sensitivity | p. 8 (6.1. Co-training Improves Performance) |
| Figure 2: Hardware Details. Left: Mobile ALOHA has two wrist cameras and one top camera, with onboard power and compute. Middle: The teleoperation setup ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| For pre-train, we first train ACT on the static ALOHA data and then fine-tune it with the Mobile ALOHA data. co-training, we simply co-train ... | component/input/data sensitivity | p. 9 (6.1. Co-training Improves Performance) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| On the hardware front, we present Mobile ALOHA, a low-cost and whole-body teleoperation system for collecting bimanual mobile manipulation data. | Co-training improves the whole-task success rate in 5 out of the 7 tasks, with a boost of 45%, 20%, 80%, 95% and 80% respectively. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (6.1. Co-training Improves Performance), p. 7 (Figure/Table caption), p. 9 (Figure/Table caption), p. 9 (6.1. Co-training Improves Performance), p. 8 (6.1. Co-training Improves Performance) |
| Primary metric/result | Table 1: Co-training improves ACT performance. Across 7 challenging mobile manipulation tasks, co-training with static ALOHA dataset consistently improve the success rate (%) of ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 8 / 6.1. Co-training Improves Performance - extractive body cue:** We start with ACT [104], the method introduced with ALOHA, and train it on all 7 tasks with and without co-training.
- **p. 8 / 6.1. Co-training Improves Performance - extractive body cue:** Each success rate is computed from 20 trials of evaluation, except Cook Shrimp which has 5.
- **p. 8 / 6.1. Co-training Improves Performance - extractive body cue:** Co-training improves the whole-task success rate in 5 out of the 7 tasks, with a boost of 45%, 20%, 80%, 95% and 80% respectively.
- **p. 10 / 6.1. Co-training Improves Performance - extractive body cue:** 20 40 60 80 Duration (s) Wipe Wine 1 2 3 4 5 Trial Num.
- **p. 2 / 1. Introduction - extractive body cue:** It contains 825 episodes with tasks disjoint from the Mobile ALOHA tasks, and has different mounting positions of the two arms.
- **p. 4 / 3. Mobile ALOHA Hardware - extractive body cue:** We found Tracer to possess sufficient traversability in accessible buildings: it can traverse obstacles as tall as 10mm and slopes as steep as 8 degrees ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Despite Mobile ALOHA's simplicity and performance, there are still limitations that we hope to address in future works. | p. 10 (8. User Studies) |
| body limitation/failure cue | Figure 2: Hardware Details. Left: Mobile ALOHA has two wrist cameras and one top camera, with onboard power and compute. Middle: The teleoperation setup ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | In all of these cases, compounding errors appear to be the main source of failure, either from the stochasticity of robot base velocity control ... | p. 8 (6.1. Co-training Improves Performance) |
| body limitation/failure cue | The main failure modes are imprecise grasping on Lift Glass and Wipe as well as jerky motion when switching between chunks. | p. 9 (6.1. Co-training Improves Performance) |
| body limitation/failure cue | The only task that falls below 80% success is Cook Shrimp (40%), which is a 75-second long-horizon task for which we only collected 20 ... | p. 8 (6.1. Co-training Improves Performance) |
| body limitation/failure cue | Conclusion, Limitations and Future Directions In summary, our paper tackles both the hardware and the software aspects of bimanual mobile manipulation. | p. 10 (8. User Studies) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Each success rate is computed from 20 trials of evaluation, except Cook Shrimp which has 5. | p. 8 (6.1. Co-training Improves Performance) |
| Action chunking also provides a unique advantage for Mobile ALOHA: handling the delay of different parts of the hardware more flexibly. | p. 8 (6. Experiments) |
| For pre-train, we first train ACT on the static ALOHA data and then fine-tune it with the Mobile ALOHA data. co-training, we simply co-train ... | p. 9 (6.1. Co-training Improves Performance) |
| 20 40 60 80 Duration (s) Wipe Wine 1 2 3 4 5 Trial Num. | p. 10 (6.1. Co-training Improves Performance) |
| All compute during data collection and inference is conducted on a consumer-grade laptop with Nvidia 3070 Ti GPU (8GB VRAM) and Intel i7-12800H. | p. 4 (3. Mobile ALOHA Hardware) |
| (1) We lack accessible, plug-and-play hardware for whole-body teleoperation. | p. 2 (1. Introduction) |
| Additional hardware and calibration are also necessary to enable teleoperation on these platforms. | p. 2 (1. Introduction) |
| Untethered: Onboard power and compute. | p. 4 (3. Mobile ALOHA Hardware) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 8. User Studies - extractive body cue:** Despite Mobile ALOHA's simplicity and performance, there are still limitations that we hope to address in future works.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Hardware Details. Left: Mobile ALOHA has two wrist cameras and one top camera, with onboard power and compute. Middle: The teleoperation setup can ...
- **p. 8 / 6.1. Co-training Improves Performance - extractive body cue:** In all of these cases, compounding errors appear to be the main source of failure, either from the stochasticity of robot base velocity control or ...
- **p. 9 / 6.1. Co-training Improves Performance - extractive body cue:** The main failure modes are imprecise grasping on Lift Glass and Wipe as well as jerky motion when switching between chunks.
- **p. 8 / 6.1. Co-training Improves Performance - extractive body cue:** The only task that falls below 80% success is Cook Shrimp (40%), which is a 75-second long-horizon task for which we only collected 20 demonstrations.
- **p. 10 / 8. User Studies - extractive body cue:** Conclusion, Limitations and Future Directions In summary, our paper tackles both the hardware and the software aspects of bimanual mobile manipulation.

- **PDF anchors reviewed:** datasets p. 8 (6.1. Co-training Improves Performance), p. 8 (6.1. Co-training Improves Performance), p. 9 (6.1. Co-training Improves Performance), p. 9 (6.1. Co-training Improves Performance), p. 10 (6.1. Co-training Improves Performance), metrics p. 7 (Figure/Table caption), p. 8 (6.1. Co-training Improves Performance), p. 8 (6.1. Co-training Improves Performance), p. 9 (6.1. Co-training Improves Performance), p. 3 (Figure/Table caption), p. 20 (Figure/Table caption), baselines p. 9 (6.1. Co-training Improves Performance), p. 8 (6.1. Co-training Improves Performance), results p. 8 (6.1. Co-training Improves Performance), p. 7 (Figure/Table caption), p. 9 (Figure/Table caption), p. 9 (6.1. Co-training Improves Performance), p. 8 (6.1. Co-training Improves Performance).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
