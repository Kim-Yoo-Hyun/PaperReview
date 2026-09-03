# Evaluation - Strengthening Generative Robot Policies through Predictive World Modeling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://computationalrobotics.seas.harvard.edu/GPC/; PDF retrieval source: https://arxiv.org/pdf/2502.00622. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 8 (Figure/Table caption)): The results show that (a) GPC-RANK improves performance by ∼10% over the behavior cloning baseline; (b) GPC-OPT yields a ∼15% gain; and (c) GPC-RANK+OPT achieves up to ∼25%. • Importance ...

## Evaluation Body Digest

- **p. 4 / V. EXPERIMENTS - extractive body cue:** We evaluate GPC on (1) a state-based planar pushing task, (2) four vision-based simulation tasks, and (3) two real-world manipulation tasks.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** QI et al.: INFERENCE-TIME ENHANCEMENT OF GENERATIVE ROBOT POLICIES VIA PREDICTIVE WORLD MODELING 5 Behavior Cloning GPC-RANK GPC-OPT GPC-RANK+OPT With GT Simulator (K=1, M=0) (K=100, ...
- **p. 4 / V. EXPERIMENTS - extractive body cue:** We study the planar pushing task with the goal of pushing an object from an initial pose to a specified target pose, where the groundtruth ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** 6 IEEE ROBOTICS AND AUTOMATION LETTERS.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Besides, we compare the world model against two baselines: deep visual foresight [40], which uses CNNs and LSTMs for prediction,1 and AVDC [26], a video ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** 3: WORLD MODEL PREDICTIONS IN GPC FOR VISIONBASED SIMULATION TASKS.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Planning-only methods without a generative policy prior, including model predictive path integral (MPPI), cross-entropy method (CEM), and pure gradient ascent [35], achieve substantially lower performance ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** We adopt two strategies: (1) when a numerical reward can be defined (e.g., registration loss in Push-T or cube distance in Block Stacking), we train ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** V. EXPERIMENTS (p. 4).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results show that (a) GPC-RANK improves performance by ∼10% over the behavior cloning baseline; (b) GPC-OPT yields a ∼15% gain; and (c) GPC-RANK+OPT ... | p. 6 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Planning-only methods without a generative policy prior, including model predictive path integral (MPPI), cross-entropy method (CEM), and pure gradient ascent [35], achieve substantially lower ... | p. 6 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | In all cases, GPC consistently outperforms the behavior cloning baseline, highlighting its effectiveness as an inference-time enhancement. | p. 4 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Clearly, all GPCRANK, GPC-OPT, and GPC-RANK+OPT variants outperform pure behavior cloning. | p. 5 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | This table presents an ablation over sampling (i.e., number of action proposals K from P(·)) and optimization (i.e., number of gradient steps M), illustrating ... | p. 5 (V. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 4 / V. EXPERIMENTS - extractive body cue:** We evaluate GPC on (1) a state-based planar pushing task, (2) four vision-based simulation tasks, and (3) two real-world manipulation tasks.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** QI et al.: INFERENCE-TIME ENHANCEMENT OF GENERATIVE ROBOT POLICIES VIA PREDICTIVE WORLD MODELING 5 Behavior Cloning GPC-RANK GPC-OPT GPC-RANK+OPT With GT Simulator (K=1, M=0) (K=100, ...
- **p. 4 / V. EXPERIMENTS - extractive body cue:** We study the planar pushing task with the goal of pushing an object from an initial pose to a specified target pose, where the groundtruth ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** 6 IEEE ROBOTICS AND AUTOMATION LETTERS.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Besides, we compare the world model against two baselines: deep visual foresight [40], which uses CNNs and LSTMs for prediction,1 and AVDC [26], a video ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** 3: WORLD MODEL PREDICTIONS IN GPC FOR VISIONBASED SIMULATION TASKS.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: GENERATIVE PREDICTIVE CONTROL (GPC). (a) GPC-RANK: The generative policy proposes multiple action sequences that are evaluated in imagination using the predictive world model; ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: DIFFUSION-BASED VISUAL WORLD MODELING. [Left] Recursive single-step prediction produces multi- step futures. [Right] Each single-step predictor is a condi- tioned diffusion model, where ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: WORLD MODEL PREDICTIONS IN GPC FOR VISION- BASED SIMULATION TASKS. All images shown are model- predicted future observations, sampled from intermediate steps along ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: COMPARISON OF DIFFERENT VISUAL WORLD MODELS. We report the average SSIM between each method's prediction and ground-truth frames over 10 uniformly sampled prediction ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: IMPORTANCE OF RANDOM EXPLORATION IN WORLD MODEL LEARNING (VISION-BASED PUSH-T). highest overall results. Ablations in planar pushing. Using the Push-T task, we analyze ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: REAL-WORLD TESTS FOR PUSH-T. Top row shows trajectories of baseline model (K = 1, M = 0), middle row shows trajectories of GPC-RANK ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: REAL-WORLD TESTS FOR CLOTHES FOLDING. Top row shows trajectories of baseline model (K = 1, M = 0), second row shows trajectories of ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: REAL-WORLD SUCCESS RATES [29] H. Bharadhwaj, D. Dwibedi, A. Gupta, S. Tulsiani, C. Doersch, T. Xiao, D. Shah, F. Xia, D. Sadigh, and ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate GPC on (1) a state-based planar pushing task, (2) four vision-based simulation tasks, and (3) two real-world manipulation tasks. | embodiment, simulator version and control stack | p. 4 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Task/environment | QI et al.: INFERENCE-TIME ENHANCEMENT OF GENERATIVE ROBOT POLICIES VIA PREDICTIVE WORLD MODELING 5 Behavior Cloning GPC-RANK GPC-OPT GPC-RANK+OPT With GT Simulator (K=1, M=0) ... | reset, timeout, object/scene variation | p. 5 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 1 (B EHAVIOR cloning (BC) with generative models has), p. 3 (III. OVERVIEW OF GENERATIVE PREDICTIVE CONTROL) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 3 (III. OVERVIEW OF GENERATIVE PREDICTIVE CONTROL), p. 4 (IV. WORLD MODEL LEARNING) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Planning-only methods without a generative policy prior, including model predictive path integral (MPPI), cross-entropy method (CEM), and pure gradient ascent [35], achieve substantially lower ... | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| We adopt two strategies: (1) when a numerical reward can be defined (e.g., registration loss in Push-T or cube distance in Block Stacking), we ... | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| Scores report IoU averaged over 100 evaluation seeds. | definition/direction/unit from same section | p. 5 (V. EXPERIMENTS) |
| Fig. 8: REAL-WORLD SUCCESS RATES [29] H. Bharadhwaj, D. Dwibedi, A. Gupta, S. Tulsiani, C. Doersch, T. Xiao, D. Shah, F. Xia, D. Sadigh, ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Two representative sets of predicted frames are shown, with regions of interest highlighted in blue for comparison. define the reward with a registration loss ... | definition/direction/unit from same section | p. 5 (V. EXPERIMENTS) |
| Fig. 1: GENERATIVE PREDICTIVE CONTROL (GPC). (a) GPC-RANK: The generative policy proposes multiple action sequences that are evaluated in imagination using the predictive world ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| We further provide ablations and comparisons to illustrate: (i) the influence of K and M on performance, and (ii) how GPC compares with other ... | definition/direction/unit from same section | p. 4 (V. EXPERIMENTS) |
| Fig. 2: DIFFUSION-BASED VISUAL WORLD MODELING. [Left] Recursive single-step prediction produces multi- step futures. [Right] Each single-step predictor is a condi- tioned diffusion model, ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In all cases, GPC consistently outperforms the behavior cloning baseline, highlighting its effectiveness as an inference-time enhancement. | comparison identity and matched condition | p. 4 (V. EXPERIMENTS) |
| We further provide ablations and comparisons to illustrate: (i) the influence of K and M on performance, and (ii) how GPC compares with other ... | comparison identity and matched condition | p. 4 (V. EXPERIMENTS) |
| This table presents an ablation over sampling (i.e., number of action proposals K from P(·)) and optimization (i.e., number of gradient steps M), illustrating ... | comparison identity and matched condition | p. 5 (V. EXPERIMENTS) |
| Using the Push-T task, we analyze the impact of K and M, compare against additional MPC-style baselines without diffusion-policy warm-start, and study the role ... | comparison identity and matched condition | p. 6 (V. EXPERIMENTS) |
| Clearly, all GPCRANK, GPC-OPT, and GPC-RANK+OPT variants outperform pure behavior cloning. | comparison identity and matched condition | p. 5 (V. EXPERIMENTS) |
| During evaluation, we use 100 action candidates for all baselines. | comparison identity and matched condition | p. 6 (V. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| This table presents an ablation over sampling (i.e., number of action proposals K from P(·)) and optimization (i.e., number of gradient steps M), illustrating ... | component/input/data sensitivity | p. 5 (V. EXPERIMENTS) |
| Fig. 5: IMPORTANCE OF RANDOM EXPLORATION IN WORLD MODEL LEARNING (VISION-BASED PUSH-T). highest overall results. Ablations in planar pushing. Using the Push-T task, we ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Notably, the best-performing GPC variant in Table I approaches the performance of planning based on a pretrained behavior cloning policy with a groundtruth simulator ... | component/input/data sensitivity | p. 5 (V. EXPERIMENTS) |
| We further provide ablations and comparisons to illustrate: (i) the influence of K and M on performance, and (ii) how GPC compares with other ... | component/input/data sensitivity | p. 4 (V. EXPERIMENTS) |
| 5 compares GPCRANK and GPC-OPT using world models trained with and without random exploration. | component/input/data sensitivity | p. 6 (V. EXPERIMENTS) |
| Fig. 1: GENERATIVE PREDICTIVE CONTROL (GPC). (a) GPC-RANK: The generative policy proposes multiple action sequences that are evaluated in imagination using the predictive world ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| GPC consists of three components: • Generative policy training. | The results show that (a) GPC-RANK improves performance by ∼10% over the behavior cloning baseline; (b) GPC-OPT yields a ∼15% gain; and (c) GPC-RANK+OPT ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 8 (Figure/Table caption) |
| Primary metric/result | Planning-only methods without a generative policy prior, including model predictive path integral (MPPI), cross-entropy method (CEM), and pure gradient ascent [35], achieve substantially lower ... | numeric claim only at cited anchor | p. 6 (V. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 5 / V. EXPERIMENTS - extractive body cue:** We report the average structural similarity index (SSIM) between predicted and ground-truth frames over the full evaluation horizon (≈250 frames), averaged across 5 evaluation seeds.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** We report the average SSIM between each method's prediction and ground-truth frames over 10 uniformly sampled prediction from the full evaluation, averaged across 100 samples ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Without freezing the noise, GPC-OPT fails, as stochastic gradients destabilize the reward optimization in (4). | p. 4 (IV. WORLD MODEL LEARNING) |
| body limitation/failure cue | Dϕ is trained by adding random noises to the clean images and then predicting the noise. | p. 4 (IV. WORLD MODEL LEARNING) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We further provide ablations and comparisons to illustrate: (i) the influence of K and M on performance, and (ii) how GPC compares with other ... | p. 4 (V. EXPERIMENTS) |
| Scores report IoU averaged over 100 evaluation seeds. | p. 5 (V. EXPERIMENTS) |
| All images shown are modelpredicted future observations, sampled from intermediate steps along the rollout horizon. | p. 5 (V. EXPERIMENTS) |
| Score is measured by the IoU metric averaged over 100 evaluation seeds. | p. 6 (V. EXPERIMENTS) |
| K is the number of action proposals; M is the number of gradient steps. using the structural similarity index (SSIM) between predicted and ground-truth ... | p. 6 (V. EXPERIMENTS) |
| At inference time, GPC enhances the frozen policy using lightweight planning strategies. | p. 1 (B EHAVIOR cloning (BC) with generative models has) |
| We propose generative predictive control (GPC), a framework that strengthens pretrained diffusion-based BC policies at inference time by coupling them with an action-conditioned predictive ... | p. 1 (B EHAVIOR cloning (BC) with generative models has) |
| We therefore fix oNd t+1 = 0 at inference time, making the world model deterministic and producing the most likely future prediction. | p. 4 (IV. WORLD MODEL LEARNING) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / IV. WORLD MODEL LEARNING - extractive body cue:** Without freezing the noise, GPC-OPT fails, as stochastic gradients destabilize the reward optimization in (4).
- **p. 4 / IV. WORLD MODEL LEARNING - extractive body cue:** Dϕ is trained by adding random noises to the clean images and then predicting the noise.

- **Evidence anchors reviewed:** datasets p. 4 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), metrics p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 8 (Figure/Table caption), p. 5 (V. EXPERIMENTS), p. 2 (Figure/Table caption), baselines p. 4 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), results p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
