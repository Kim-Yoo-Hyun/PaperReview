# Evaluation - PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_PALM_Progress-Aware_Policy_Learning_via_Affordance_Reasoning_for_Long-Horizon_Robotic_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_PALM_Progress-Aware_Policy_Learning_via_Affordance_Reasoning_for_Long-Horizon_Robotic_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.1. Simulation Experiments), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (4.3. Real-World Experiments), p. 1 (Figure/Table caption), p. 7 (4.2. Ablation Studies)): Moreover, as shown in Table 2, across all four LIBERO suites, PALM achieves state-of-the-art performance with an average success rate of 94.5%.

## Evaluation Body Digest

- **p. 5 / 4. Experiments - extractive body cue:** For pre-training, we utilize a mixed dataset from the DROID [54] and BridgeData V2 [113] datasets, which together provide large-scale, in-the-wild robotic arm demonstrations to ...
- **p. 8 / 4.3. Real-World Experiments - extractive body cue:** We select a mixed pre-training dataset composed of DROID [54] and BridgeData V2 [113], while the fine-tuning dataset consists of 200 demonstrations collected on the ...
- **p. 6 / 4.1. Simulation Experiments - extractive body cue:** Additionally, we compare against Octo [111], which pre-trains robot policies on diverse datasets to enhance generalization.
- **p. 7 / 4.2. Ablation Studies - extractive body cue:** For each task suite (Spatial, Object, Goal, Long), we report the average success rate and standard error across 3 seeds with 500 episodes each.
- **p. 5 / 4.1. Simulation Experiments - extractive body cue:** We conduct evaluations across two simulation benchmarks: the LIBERO [77] benchmark compris28100
- **p. 6 / 4.1. Simulation Experiments - extractive body cue:** Prediction-based methods, represented by Susie [7], GR-1 [118], and Seer [112], merge visual foresight as a future representation to enhance performance in multitask robot manipulation.
- **p. 8 / 4.3. Real-World Experiments - extractive body cue:** We report the success rate (SR) and average length for each task over 20 real-world rollouts.
- **p. 7 / 4.2. Ablation Studies - extractive body cue:** Results on the CALVIN ABC→D benchmark demonstrate the effectiveness of each training module under both pre-training and fine-tuning.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Simulation Experiments (p. 5); 4.3. Real-World Experiments (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Simulation Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Moreover, as shown in Table 2, across all four LIBERO suites, PALM achieves state-of-the-art performance with an average success rate of 94.5%. | p. 6 (4.1. Simulation Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2. LIBERO experimental results. For each task suite (Spatial, Object, Goal, Long), we report the average success rate and standard error across 3 ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1. CALVIN ABC→D experimental results. We group the baselines into four types and report the average success rate of the top three checkpoints, ... | p. 6 (Figure/Table caption) |
| 4.3. Real-World Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | We report the success rate (SR) and average length for each task over 20 real-world rollouts. | p. 8 (4.3. Real-World Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1. In contrast to vanilla VLAs that directly map inputs to actions or to predictive methods that forecast dense future images, PALM introduces ... | p. 1 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / 4. Experiments - extractive body cue:** For pre-training, we utilize a mixed dataset from the DROID [54] and BridgeData V2 [113] datasets, which together provide large-scale, in-the-wild robotic arm demonstrations to ...
- **p. 8 / 4.3. Real-World Experiments - extractive body cue:** We select a mixed pre-training dataset composed of DROID [54] and BridgeData V2 [113], while the fine-tuning dataset consists of 200 demonstrations collected on the ...
- **p. 6 / 4.1. Simulation Experiments - extractive body cue:** Additionally, we compare against Octo [111], which pre-trains robot policies on diverse datasets to enhance generalization.
- **p. 7 / 4.2. Ablation Studies - extractive body cue:** For each task suite (Spatial, Object, Goal, Long), we report the average success rate and standard error across 3 seeds with 500 episodes each.
- **p. 5 / 4.1. Simulation Experiments - extractive body cue:** We conduct evaluations across two simulation benchmarks: the LIBERO [77] benchmark compris28100
- **p. 6 / 4.1. Simulation Experiments - extractive body cue:** Prediction-based methods, represented by Susie [7], GR-1 [118], and Seer [112], merge visual foresight as a future representation to enhance performance in multitask robot manipulation.
- **p. 8 / 4.3. Real-World Experiments - extractive body cue:** We report the success rate (SR) and average length for each task over 20 real-world rollouts.
- **p. 7 / 4.2. Ablation Studies - extractive body cue:** Results on the CALVIN ABC→D benchmark demonstrate the effectiveness of each training module under both pre-training and fine-tuning.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. In contrast to vanilla VLAs that directly map inputs to actions or to predictive methods that forecast dense future images, PALM introduces learnable ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. PALM Overview. (a) Model Architecture: Given a language instruction l, observation ot, and robot state st, PALM encodes each modality using frozen encoders ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. CALVIN ABC→D experimental results. We group the baselines into four types and report the average success rate of the top three checkpoints, computed ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Ablation studies of affordance components on CALVIN ABC→D and LIBERO-LONG benchmarks demonstrate the effectiveness of the four components of affordance prediction. increases (e.g., ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. LIBERO experimental results. For each task suite (Spatial, Object, Goal, Long), we report the average success rate and standard error across 3 seeds ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Ablation studies of PALM components. Results on the CALVIN ABC→D benchmark demonstrate the effectiveness of each training module under both pre-training and fine-tuning. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Ablation studies on training data composition. Re- sults on the CALVIN ABC→D and LIBERO-LONG benchmarks demonstrate the data efficiency of each source type. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Real-world experimental setup and task design. Left: We use a UFACTORY xArm6 robot with the matched Gripper G2 and two RealSense D455 cameras. ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For pre-training, we utilize a mixed dataset from the DROID [54] and BridgeData V2 [113] datasets, which together provide large-scale, in-the-wild robotic arm demonstrations ... | embodiment, simulator version and control stack | p. 5 (4. Experiments), p. 8 (4.3. Real-World Experiments) |
| Task/environment | We select a mixed pre-training dataset composed of DROID [54] and BridgeData V2 [113], while the fine-tuning dataset consists of 200 demonstrations collected on ... | reset, timeout, object/scene variation | p. 8 (4.3. Real-World Experiments), p. 6 (4.1. Simulation Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (3.2. PALM Architecture), p. 5 (3.4. Progress-aware Policy via Inverse Dynamics) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For each task suite (Spatial, Object, Goal, Long), we report the average success rate and standard error across 3 seeds with 500 episodes each. | definition/direction/unit from same section | p. 7 (4.2. Ablation Studies) |
| Moreover, as shown in Table 2, across all four LIBERO suites, PALM achieves state-of-the-art performance with an average success rate of 94.5%. | definition/direction/unit from same section | p. 6 (4.1. Simulation Experiments) |
| First, PALM (Prediction + Progress) reaches a 96.9% success rate on the first subtask and maintains strong performance as horizon length LIBERO-LONG 0 20 ... | definition/direction/unit from same section | p. 6 (4.1. Simulation Experiments) |
| We report the success rate (SR) and average length for each task over 20 real-world rollouts. | definition/direction/unit from same section | p. 8 (4.3. Real-World Experiments) |
| Figure 1. In contrast to vanilla VLAs that directly map inputs to actions or to predictive methods that forecast dense future images, PALM introduces ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| As shown in Table 5, results demonstrate PALM's superior generalization over baselines as the task sequence length increases, showing its robustness in longhorizon settings. | definition/direction/unit from same section | p. 8 (4.3. Real-World Experiments) |
| PALM achieves the best performance over previous methods. | definition/direction/unit from same section | p. 7 (4.2. Ablation Studies) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| PALM consistently and substantially outperforms all baselines. | comparison identity and matched condition | p. 6 (4.1. Simulation Experiments) |
| The largest gain is in LIBERO-LONG, where PALM reaches 91.8%, outperforming the strongest baseline (CoT-VLA at 69.0%) by 22.8%. | comparison identity and matched condition | p. 6 (4.1. Simulation Experiments) |
| We select OpenVLA [55] and Octo [111] as baselines. | comparison identity and matched condition | p. 8 (4.3. Real-World Experiments) |
| As shown in Table 5, results demonstrate PALM's superior generalization over baselines as the task sequence length increases, showing its robustness in longhorizon settings. | comparison identity and matched condition | p. 8 (4.3. Real-World Experiments) |
| Figure 1. In contrast to vanilla VLAs that directly map inputs to actions or to predictive methods that forecast dense future images, PALM introduces ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Ablation studies of PALM components. | comparison identity and matched condition | p. 7 (4.2. Ablation Studies) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation studies of affordance components on CALVIN ABC→D and LIBERO-LONG benchmarks demonstrate the effectiveness of the four components of affordance prediction. increases (e.g., 82.0% ... | component/input/data sensitivity | p. 6 (4.1. Simulation Experiments) |
| Table 3. Ablation studies of PALM components. Results on the CALVIN ABC→D benchmark demonstrate the effectiveness of each training module under both pre-training and ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Our training process consists of a pretraining and a fine-tuning stage. | component/input/data sensitivity | p. 5 (4. Experiments) |
| Figure 2. PALM Overview. (a) Model Architecture: Given a language instruction l, observation ot, and robot state st, PALM encodes each modality using frozen ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Table 4. Ablation studies on training data composition. Re- sults on the CALVIN ABC→D and LIBERO-LONG benchmarks demonstrate the data efficiency of each source ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| For fine-tuning, we select 942 trajectories from robot data and annotate them with affordance data and continuous progress labels using a semi-automated method. | component/input/data sensitivity | p. 5 (4. Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are as follows: • We introduce PALM, a unified VLA framework that integrates structured affordance reasoning and progress-aware policy generation to enable ... | Moreover, as shown in Table 2, across all four LIBERO suites, PALM achieves state-of-the-art performance with an average success rate of 94.5%. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.1. Simulation Experiments), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (4.3. Real-World Experiments), p. 1 (Figure/Table caption), p. 7 (4.2. Ablation Studies) |
| Primary metric/result | Table 2. LIBERO experimental results. For each task suite (Spatial, Object, Goal, Long), we report the average success rate and standard error across 3 ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 4. Experiments - extractive body cue:** For fine-tuning, we select 942 trajectories from robot data and annotate them with affordance data and continuous progress labels using a semi-automated method.
- **p. 6 / 4.1. Simulation Experiments - extractive body cue:** We group the baselines into four types and report the average success rate of the top three checkpoints, computed over 1,000 rollouts per task, as ...
- **p. 7 / 4.2. Ablation Studies - extractive body cue:** For each task suite (Spatial, Object, Goal, Long), we report the average success rate and standard error across 3 seeds with 500 episodes each.
- **p. 7 / 4.2. Ablation Studies - extractive body cue:** Average (↑) Spatial (↑) Object (↑) Goal (↑) Long (↑) OpenVLA [55] 76.5 ± 0.6% 84.7 ± 0.9% 88.4 ± 0.8% 79.2 ± 1.0% 53.7 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | PALM achieves stateof-the-art results on two benchmarks, with a 12.5% improvement on CALVIN ABC→D and 91.8% success on LIBEROLONG, and shows significant robustness in ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | As shown in Table 5, results demonstrate PALM's superior generalization over baselines as the task sequence length increases, showing its robustness in longhorizon settings. | p. 8 (4.3. Real-World Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We group the baselines into four types and report the average success rate of the top three checkpoints, computed over 1,000 rollouts per task, ... | p. 6 (4.1. Simulation Experiments) |
| For pre-training, we utilize a mixed dataset from the DROID [54] and BridgeData V2 [113] datasets, which together provide large-scale, in-the-wild robotic arm demonstrations ... | p. 5 (4. Experiments) |
| For each task suite (Spatial, Object, Goal, Long), we report the average success rate and standard error across 3 seeds with 500 episodes each. | p. 7 (4.2. Ablation Studies) |
| To ensure fairness, all models are fine-tuned on our training dataset, trained for an equal number of iterations, and evaluated with the final checkpoint. | p. 8 (4.3. Real-World Experiments) |
| Instructions are embedded using a CLIP text encoder [102], observations are encoded with a Masked Autoencoder [36] and downsampled by a Perceiver Resampler [46] ... | p. 3 (3.2. PALM Architecture) |
| At time t, given observations ot "O, and task specification ⌧"T , and conditioned on the predicted affordance latent, the policy jointly decodes an ... | p. 3 (3.1. Problem Formulation) |
| Affordance Queries Action-progress Queries Multi-Modal Encoders Affordance prediction Frozen Trainable Unidirectional Attention Action-progress <Global> <Local> <Spatial> <Dynamic> T S V G | p. 4 (3.2. PALM Architecture) |
| Training follows the standard diffusion objective: ˜yt⇥t+n-1,td = ‘ ¯↵td yt⇥t+n-1 + ‘ 1 -¯↵td ✏ (9) LDiT = Etd, ✏æ✏-✏✓(˜yt⇥t+n-1,td ∑l, ot, st, ... | p. 5 (3.4. Progress-aware Policy via Inverse Dynamics) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive body cue:** PALM achieves stateof-the-art results on two benchmarks, with a 12.5% improvement on CALVIN ABC→D and 91.8% success on LIBEROLONG, and shows significant robustness in real-world ...
- **p. 8 / 4.3. Real-World Experiments - extractive body cue:** As shown in Table 5, results demonstrate PALM's superior generalization over baselines as the task sequence length increases, showing its robustness in longhorizon settings.

- **PDF anchors reviewed:** datasets p. 5 (4. Experiments), p. 8 (4.3. Real-World Experiments), p. 6 (4.1. Simulation Experiments), p. 7 (4.2. Ablation Studies), p. 5 (4.1. Simulation Experiments), p. 6 (4.1. Simulation Experiments), metrics p. 7 (4.2. Ablation Studies), p. 6 (4.1. Simulation Experiments), p. 6 (4.1. Simulation Experiments), p. 8 (4.3. Real-World Experiments), p. 1 (Figure/Table caption), p. 8 (4.3. Real-World Experiments), baselines p. 6 (4.1. Simulation Experiments), p. 6 (4.1. Simulation Experiments), p. 8 (4.3. Real-World Experiments), p. 8 (4.3. Real-World Experiments), p. 1 (Figure/Table caption), p. 7 (4.2. Ablation Studies), results p. 6 (4.1. Simulation Experiments), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (4.3. Real-World Experiments), p. 1 (Figure/Table caption), p. 7 (4.2. Ablation Studies).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
