# Evaluation - Perpetual Humanoid Control for Real-time Simulated Avatars

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2023/html/Luo_Perpetual_Humanoid_Control_for_Real-time_Simulated_Avatars_ICCV_2023_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2023/html/Luo_Perpetual_Humanoid_Control_for_Real-time_Simulated_Avatars_ICCV_2023_paper.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.1. Motion Imitation), p. 7 (4.1. Motion Imitation), p. 7 (4.1. Motion Imitation), p. 8 (4.2. Fail-state Recovery)): H36M-Test-Video* RET MCP PNN Rotation Fail-Recover Succ ↑ Eg-mpjpe ↓ Empjpe ↓ ✗ ✗ ✗ ✓ ✗ 51.2% 56.2 34.4 ✓ ✗ ✗ ✓ ✗ 59.4% 60.2 37.2 ✓ ✓ ...

## Evaluation Body Digest

- **p. 7 / 4. Experiments - extractive body cue:** PHC is trained on the training split of the AMASS [23] dataset.
- **p. 7 / 4.1. Motion Imitation - extractive body cue:** On the training dataset, PHC has a better success rate while achieving better or similar MPJPE, showcasing its ability to better imitate sequences from the ...
- **p. 8 / 4.1. Motion Imitation - extractive body cue:** Fig.4 shows a qualitative result on a live demonstration of using poses estimated from an office environment.
- **p. 8 / 4.1. Motion Imitation - extractive body cue:** Similarly, we see that keypoint-based controller (ours-kp) outperforms rotation-based, which can be explained by 1) estimating 3D keypoint directly from images is an easier task ...
- **p. 7 / 4.1. Motion Imitation - extractive body cue:** On testing, PHC shows a high success rate on unseen MoCap sequences from both the AMASS and H36M data.
- **p. 8 / 4.2. Fail-state Recovery - extractive body cue:** From Tab.4 we can see that both of our keypoint-based and rotation-based controllers can recover from fall state with high success rate (> 90%) even ...
- **p. 8 / 4.1. Motion Imitation - extractive body cue:** H36M-Test-Video* RET MCP PNN Rotation Fail-Recover Succ ↑ Eg-mpjpe ↓ Empjpe ↓ ✗ ✗ ✗ ✓ ✗ 51.2% 56.2 34.4 ✓ ✗ ✗ ✓ ✗ ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: (a) Imitating high-quality MoCap - spin and kick. (b) Recover from fallen state and go back to reference motion (indicated by red dots). ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** 4. Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Motion Imitation | SYSTEM / EVALUATION SCOPE UNRESOLVED | H36M-Test-Video* RET MCP PNN Rotation Fail-Recover Succ ↑ Eg-mpjpe ↓ Empjpe ↓ ✗ ✗ ✗ ✓ ✗ 51.2% 56.2 34.4 ✓ ✗ ✗ ✓ ... | p. 8 (4.1. Motion Imitation) |
| 4.1. Motion Imitation | SYSTEM / EVALUATION SCOPE UNRESOLVED | Similar to results on MoCap Imitation, PHC outperforms the baselines 10901 | p. 7 (4.1. Motion Imitation) |
| 4.1. Motion Imitation | SYSTEM / EVALUATION SCOPE UNRESOLVED | On testing, PHC shows a high success rate on unseen MoCap sequences from both the AMASS and H36M data. | p. 7 (4.1. Motion Imitation) |
| 4.2. Fail-state Recovery | SYSTEM / EVALUATION SCOPE UNRESOLVED | From Tab.4 we can see that both of our keypoint-based and rotation-based controllers can recover from fall state with high success rate (> 90%) ... | p. 8 (4.2. Fail-state Recovery) |

## Dataset / Benchmark Role

- **p. 7 / 4. Experiments - extractive body cue:** PHC is trained on the training split of the AMASS [23] dataset.
- **p. 7 / 4.1. Motion Imitation - extractive body cue:** On the training dataset, PHC has a better success rate while achieving better or similar MPJPE, showcasing its ability to better imitate sequences from the ...
- **p. 8 / 4.1. Motion Imitation - extractive body cue:** Fig.4 shows a qualitative result on a live demonstration of using poses estimated from an office environment.
- **p. 8 / 4.1. Motion Imitation - extractive body cue:** Similarly, we see that keypoint-based controller (ours-kp) outperforms rotation-based, which can be explained by 1) estimating 3D keypoint directly from images is an easier task ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: We propose a motion imitator that can naturally recover from falls and walk to far-away reference motion, perpetually controlling simulated avatars without requiring ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Our progressive training procedure to train primitives P(1), P(2), · · · , P(K) by gradually learning harder and harder sequences. Fail recovery ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Goal-conditioned RL framework with Adversarial Mo- tion Prior. Each primitive P(k) and composer C is trained using the same procedure, and here we ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: (a) Imitating high-quality MoCap - spin and kick. (b) Recover from fallen state and go back to reference motion (indicated by red dots). ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Quantitative results on imitating MoCap motion sequences (* indicates removing sequences containing human-object interaction). AMASS-Train*, AMASS-Test*, and H36M-Motion* contains 11313, 140, and 140 ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Motion imitation on noisy motion. We use HybrIK[17] to estimate the joint rotations ˜θt and uses MeTRAbs [39] for global 3D keypoints ˜pt. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Ablation on components of our pipeline, performed using noisy pose estimate from HybrIK + Metrabs (root) on the H36M-Test-Video* data. RET: relaxed early ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4: We measure whether our controller can recover from the fail-states by generating these scenarios (dropping the humanoid on the ground & far from ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | PHC is trained on the training split of the AMASS [23] dataset. | embodiment, simulator version and control stack | p. 7 (4. Experiments), p. 7 (4.1. Motion Imitation) |
| Task/environment | On the training dataset, PHC has a better success rate while achieving better or similar MPJPE, showcasing its ability to better imitate sequences from ... | reset, timeout, object/scene variation | p. 7 (4.1. Motion Imitation), p. 8 (4.1. Motion Imitation) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 3 (3.1. Goal Conditioned Motion Imitation with Ad), p. 5 (3.2. Progressive Multiplicative Control Policy) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 2 (1. Introduction), p. 6 (3.2. Progressive Multiplicative Control Policy) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| On testing, PHC shows a high success rate on unseen MoCap sequences from both the AMASS and H36M data. | definition/direction/unit from same section | p. 7 (4.1. Motion Imitation) |
| On the training dataset, PHC has a better success rate while achieving better or similar MPJPE, showcasing its ability to better imitate sequences from ... | definition/direction/unit from same section | p. 7 (4.1. Motion Imitation) |
| From Tab.4 we can see that both of our keypoint-based and rotation-based controllers can recover from fall state with high success rate (> 90%) ... | definition/direction/unit from same section | p. 8 (4.2. Fail-state Recovery) |
| H36M-Test-Video* RET MCP PNN Rotation Fail-Recover Succ ↑ Eg-mpjpe ↓ Empjpe ↓ ✗ ✗ ✗ ✓ ✗ 51.2% 56.2 34.4 ✓ ✗ ✗ ✓ ... | definition/direction/unit from same section | p. 8 (4.1. Motion Imitation) |
| Figure 4: (a) Imitating high-quality MoCap - spin and kick. (b) Recover from fallen state and go back to reference motion (indicated by red ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Figure 3: Goal-conditioned RL framework with Adversarial Mo- tion Prior. Each primitive P(k) and composer C is trained using the same procedure, and here ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 1: We propose a motion imitator that can naturally recover from falls and walk to far-away reference motion, perpetually controlling simulated avatars without ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Similar to results on MoCap Imitation, PHC outperforms the baselines 10901 | comparison identity and matched condition | p. 7 (4.1. Motion Imitation) |
| Comparing with the baseline with RFC, our method outperforms it on almost all metrics across training and test datasets. | comparison identity and matched condition | p. 7 (4.1. Motion Imitation) |
| Similarly, we see that keypoint-based controller (ours-kp) outperforms rotation-based, which can be explained by 1) estimating 3D keypoint directly from images is an easier ... | comparison identity and matched condition | p. 8 (4.1. Motion Imitation) |
| We perform ablation on the noisy input from H36M-Test-Image* to better showcase the controller's ability to imitate noisy data. | comparison identity and matched condition | p. 8 (4.1. Motion Imitation) |
| Figure 1: We propose a motion imitator that can naturally recover from falls and walk to far-away reference motion, perpetually controlling simulated avatars without ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Comparing R4 and R5 shows that PMCP is effective in adding fail-state recovery capability without compromising motion imitation. | component/input/data sensitivity | p. 8 (4.1. Motion Imitation) |
| We compare against UHC both with and without residual force control. | component/input/data sensitivity | p. 7 (4. Experiments) |
| Succ measures whether the humanoid can track the reference motion without losing balance or significantly lags behind. | component/input/data sensitivity | p. 7 (4. Experiments) |
| We perform ablation on the noisy input from H36M-Test-Image* to better showcase the controller's ability to imitate noisy data. | component/input/data sensitivity | p. 8 (4.1. Motion Imitation) |
| Figure 1: We propose a motion imitator that can naturally recover from falls and walk to far-away reference motion, perpetually controlling simulated avatars without ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To summarize, our contributions are as follows: (1) we propose a Perpetual Humanoid Controller that can successfully imitate 98.9% of the AMASS dataset without ... | H36M-Test-Video* RET MCP PNN Rotation Fail-Recover Succ ↑ Eg-mpjpe ↓ Empjpe ↓ ✗ ✗ ✗ ✓ ✗ 51.2% 56.2 34.4 ✓ ✗ ✗ ✓ ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.1. Motion Imitation), p. 7 (4.1. Motion Imitation), p. 7 (4.1. Motion Imitation), p. 8 (4.2. Fail-state Recovery) |
| Primary metric/result | Similar to results on MoCap Imitation, PHC outperforms the baselines 10901 | numeric claim only at cited anchor | p. 7 (4.1. Motion Imitation) |

- Numeric sentences retained from the body:
- **p. 7 / 4. Experiments - extractive body cue:** Once trained, the composite policy runs at > 30 FPS.
- **p. 7 / 4. Experiments - extractive body cue:** The control policy is run at 30 Hz, while simulation runs at 60 Hz.
- **p. 8 / 4.2. Fail-state Recovery - extractive body cue:** Fallen-State Far-State Fallen + Far-State Method Succ-5s ↑ Succ-10s ↑ Succ-5s ↑ Succ-10s ↑ Succ-5s ↑ Succ-10s ↑ Ours 95.0% 98.8% 83.7% 99.5% 93.4% 98.8% ...
- **p. 8 / 4.2. Fail-state Recovery - extractive body cue:** We create the far-state by initializing the humanoid 3 meters from the reference motion.
- **p. 8 / 4.2. Fail-state Recovery - extractive body cue:** Experiments are run randomly 1000 trials.
- **p. 4 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** For early termination, we follow UHC [20] and terminate the episode when the joints are more than 0.5 meters globally on average from the reference ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Although we can train single-clip controller to overfit on these sequences (see the supplement), our full controller often fails to learn these sequences. | p. 8 (5. Discussions) |
| body limitation/failure cue | Figure 4: (a) Imitating high-quality MoCap - spin and kick. (b) Recover from fallen state and go back to reference motion (indicated by red ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | We uses four primitives (including failstate recovery) for all our evaluations. | p. 7 (4. Experiments) |
| body limitation/failure cue | Table 4: We measure whether our controller can recover from the fail-states by generating these scenarios (dropping the humanoid on the ground & far ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Figure 1: We propose a motion imitator that can naturally recover from falls and walk to far-away reference motion, perpetually controlling simulated avatars without ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Figure 2: Our progressive training procedure to train primitives P(1), P(2), · · · , P(K) by gradually learning harder and harder sequences. Fail ... | p. 4 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Experiments are run randomly 1000 trials. | p. 8 (4.2. Fail-state Recovery) |
| All experiments are run three times and averaged. | p. 7 (4. Experiments) |
| The control policy is run at 30 Hz, while simulation runs at 60 Hz. | p. 7 (4. Experiments) |
| We generate fallen-states by dropping the humanoid on the ground and applying random joint torques for 150 time steps. | p. 8 (4.2. Fail-state Recovery) |
| The physics simulation determines state st ∈S and transition dynamics T while our policy πPHC computes per-step action at ∈A. | p. 3 (3.1. Goal Conditioned Motion Imitation with Ad) |
| Based on the simulation state st and reference motion ˆqt, the reward function R computes a reward rt = R(st, ˆqt) as the learning ... | p. 3 (3.1. Goal Conditioned Motion Imitation with Ad) |
| The AMP discriminator D(sp t-10:t) computes a real and fake value based on the current prioproception of the humanoid. | p. 4 (3.1. Goal Conditioned Motion Imitation with Ad) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Discussions - extractive body cue:** Although we can train single-clip controller to overfit on these sequences (see the supplement), our full controller often fails to learn these sequences.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: (a) Imitating high-quality MoCap - spin and kick. (b) Recover from fallen state and go back to reference motion (indicated by red dots). ...
- **p. 7 / 4. Experiments - extractive body cue:** We uses four primitives (including failstate recovery) for all our evaluations.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4: We measure whether our controller can recover from the fail-states by generating these scenarios (dropping the humanoid on the ground & far from ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: We propose a motion imitator that can naturally recover from falls and walk to far-away reference motion, perpetually controlling simulated avatars without requiring ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Our progressive training procedure to train primitives P(1), P(2), · · · , P(K) by gradually learning harder and harder sequences. Fail recovery ...

- **Evidence anchors reviewed:** datasets p. 7 (4. Experiments), p. 7 (4.1. Motion Imitation), p. 8 (4.1. Motion Imitation), p. 8 (4.1. Motion Imitation), metrics p. 7 (4.1. Motion Imitation), p. 7 (4.1. Motion Imitation), p. 8 (4.2. Fail-state Recovery), p. 8 (4.1. Motion Imitation), p. 6 (Figure/Table caption), p. 4 (Figure/Table caption), baselines p. 7 (4.1. Motion Imitation), p. 7 (4.1. Motion Imitation), p. 8 (4.1. Motion Imitation), p. 8 (4.1. Motion Imitation), p. 1 (Figure/Table caption), results p. 8 (4.1. Motion Imitation), p. 7 (4.1. Motion Imitation), p. 7 (4.1. Motion Imitation), p. 8 (4.2. Fail-state Recovery).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (10 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Similar to results on MoCap Imitation, PHC outperforms the baselines 10901 (p. 7, 4.1. Motion Imitation).
- **Metric evidence:** From Tab.4 we can see that both of our keypoint-based and rotation-based controllers can recover from fall state with high success rate (> 90%) even in the challenging scenario when ... (p. 8, 4.2. Fail-state Recovery).
- **Baseline/ablation evidence:** Similar to results on MoCap Imitation, PHC outperforms the baselines 10901 (p. 7, 4.1. Motion Imitation).
- **Failure/negative evidence:** Thus, it is important to have a controller that can gracefully handle unexpected falls and noisy input, naturally recover from failstate, and resume imitation. (p. 2, 1. Introduction).
