# Evaluation - Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://roboticsproceedings.org/rss14/p49.html; PDF retrieval source: https://arxiv.org/pdf/1709.10087. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 6 (2) Do the resulting policies exhibit desirable properties like), p. 6 (2) Do the resulting policies exhibit desirable properties like), p. 7 (2) Do the resulting policies exhibit desirable properties like), p. 7 (2) Do the resulting policies exhibit desirable properties like), p. 1 (Figure/Table caption)): Figure 10: Performance of RL with demonstrations methods - DAPG(ours) and DDPGfD. DAPG significantly outperforms DDPGfD. For DAPG, we plot the performance of the stochastic policy used for exploration. At ...

## Evaluation Body Digest

- **p. 6 / 2) Do the resulting policies exhibit desirable properties like - extractive body cue:** In order to benchmark the capabilities of DRL with regard to the dexterous manipulation tasks outlined in Section III, we evaluate the NPG algorithm described ...
- **p. 7 / 2) Do the resulting policies exhibit desirable properties like - extractive body cue:** 0 20 40 60 80 100 Robot Hours 0 20 40 60 80 100 Success Percentage Object Relocation 0 5 10 15 20 Robot Hours ...
- **p. 6 / 2) Do the resulting policies exhibit desirable properties like - extractive body cue:** 3) Are the resulting movements safe for execution on physical hardware, and are elegant/nimble/human-like?
- **p. 7 / 2) Do the resulting policies exhibit desirable properties like - extractive body cue:** (b/c) unnatural grasp for hammer (d) unnatural use of wrist for unlatching the door. be useful for training on the physical hardware.
- **p. 6 / V. RESULTS AND DISCUSSION - extractive body cue:** Subsequently, we demonstrate the benefits of incorporating human demonstrations with regard to faster learning, increased robustness of trained policies, and ability to cope with sparse ...
- **p. 6 / 2) Do the resulting policies exhibit desirable properties like - extractive body cue:** We score the different methods based on the percentage of successful trajectories the trained policies can generate, using a sample size of 100 trajectories.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7: Performance of pure RL methods - NPG and DDPG, with sparse task completion reward and shaped reward. Sparse reward setting is primarily ineffective ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: We demonstrate a wide range of dexterous manipulation skills such as object relocation, in-hand manipulation, tool use, and opening doors using DRL methods. ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** V. RESULTS AND DISCUSSION (p. 6); 2) Do the resulting policies exhibit desirable properties like (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 10: Performance of RL with demonstrations methods - DAPG(ours) and DDPGfD. DAPG significantly outperforms DDPGfD. For DAPG, we plot the performance of the ... | p. 8 (Figure/Table caption) |
| 2) Do the resulting policies exhibit desirable properties like | EMPIRICAL / REAL-ROBOT OR HARDWARE | With the shaped rewards, we find that NPG is indeed able to achieve high success percentage on these tasks (Figure 7), while DDPG was ... | p. 6 (2) Do the resulting policies exhibit desirable properties like) |
| 2) Do the resulting policies exhibit desirable properties like | EMPIRICAL / REAL-ROBOT OR HARDWARE | We score the different methods based on the percentage of successful trajectories the trained policies can generate, using a sample size of 100 trajectories. | p. 6 (2) Do the resulting policies exhibit desirable properties like) |
| 2) Do the resulting policies exhibit desirable properties like | EMPIRICAL / REAL-ROBOT OR HARDWARE | 0 20 40 60 80 100 Robot Hours 0 20 40 60 80 100 Success Percentage Object Relocation 0 5 10 15 20 Robot ... | p. 7 (2) Do the resulting policies exhibit desirable properties like) |
| 2) Do the resulting policies exhibit desirable properties like | EMPIRICAL / REAL-ROBOT OR HARDWARE | Such unnatural behaviors are indeed quite prevalent in the recent DRL results [15]. | p. 7 (2) Do the resulting policies exhibit desirable properties like) |

## Dataset / Benchmark Role

- **p. 6 / 2) Do the resulting policies exhibit desirable properties like - extractive body cue:** In order to benchmark the capabilities of DRL with regard to the dexterous manipulation tasks outlined in Section III, we evaluate the NPG algorithm described ...
- **p. 7 / 2) Do the resulting policies exhibit desirable properties like - extractive body cue:** 0 20 40 60 80 100 Robot Hours 0 20 40 60 80 100 Success Percentage Object Relocation 0 5 10 15 20 Robot Hours ...
- **p. 6 / 2) Do the resulting policies exhibit desirable properties like - extractive body cue:** 3) Are the resulting movements safe for execution on physical hardware, and are elegant/nimble/human-like?
- **p. 7 / 2) Do the resulting policies exhibit desirable properties like - extractive body cue:** (b/c) unnatural grasp for hammer (d) unnatural use of wrist for unlatching the door. be useful for training on the physical hardware.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: We demonstrate a wide range of dexterous manipulation skills such as object relocation, in-hand manipulation, tool use, and opening doors using DRL methods. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Object relocation - move the blue ball to the green target. Positions of the ball and target are randomized over the entire workspace. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3: In-hand manipulation - reposition the blue pen to match the orientation of the green target. The base of the hand is fixed. The ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 4: Door opening - undo the latch and swing the door open. The latch has significant dry friction and a bias torque that forces ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 5: Tool use - pick up and hammer with significant force to drive the nail into the board. Nail position is randomized and has ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 6: 24 degree of freedom ADROIT hand. The blue arrows mark the position of the joints and corresponding position actuator.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7: Performance of pure RL methods - NPG and DDPG, with sparse task completion reward and shaped reward. Sparse reward setting is primarily ineffective ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 8: Unnatural movements observed in the execution trace of behavior trained with pure reinforcement leaning. From left to right: (a) unnatural, socially unacceptable, finger ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In order to benchmark the capabilities of DRL with regard to the dexterous manipulation tasks outlined in Section III, we evaluate the NPG algorithm ... | embodiment, simulator version and control stack | p. 6 (2) Do the resulting policies exhibit desirable properties like), p. 7 (2) Do the resulting policies exhibit desirable properties like) |
| Task/environment | 0 20 40 60 80 100 Robot Hours 0 20 40 60 80 100 Success Percentage Object Relocation 0 5 10 15 20 Robot ... | reset, timeout, object/scene variation | p. 7 (2) Do the resulting policies exhibit desirable properties like), p. 6 (2) Do the resulting policies exhibit desirable properties like) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 1 (I. INTRODUCTION), p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG)) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 2 (I. INTRODUCTION), p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG)) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Subsequently, we demonstrate the benefits of incorporating human demonstrations with regard to faster learning, increased robustness of trained policies, and ability to cope with ... | definition/direction/unit from same section | p. 6 (V. RESULTS AND DISCUSSION) |
| 0 20 40 60 80 100 Robot Hours 0 20 40 60 80 100 Success Percentage Object Relocation 0 5 10 15 20 Robot ... | definition/direction/unit from same section | p. 7 (2) Do the resulting policies exhibit desirable properties like) |
| We score the different methods based on the percentage of successful trajectories the trained policies can generate, using a sample size of 100 trajectories. | definition/direction/unit from same section | p. 6 (2) Do the resulting policies exhibit desirable properties like) |
| Figure 7: Performance of pure RL methods - NPG and DDPG, with sparse task completion reward and shaped reward. Sparse reward setting is primarily ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 1: We demonstrate a wide range of dexterous manipulation skills such as object relocation, in-hand manipulation, tool use, and opening doors using DRL ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2: Object relocation - move the blue ball to the green target. Positions of the ball and target are randomized over the entire ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 3: In-hand manipulation - reposition the blue pen to match the orientation of the green target. The base of the hand is fixed. ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 10: Performance of RL with demonstrations methods - DAPG(ours) and DDPGfD. DAPG significantly outperforms DDPGfD. For DAPG, we plot the performance of the ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 10: Performance of RL with demonstrations methods - DAPG(ours) and DDPGfD. DAPG significantly outperforms DDPGfD. For DAPG, we plot the performance of the ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 9: Robustness of trained policies to variations in the envi- ronment. The top two figures are trained on a single instance of the ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To overcome this challenge, we propose to augment the policy search process with a small number of human demonstrations collected in virtual reality (VR). | Figure 10: Performance of RL with demonstrations methods - DAPG(ours) and DDPGfD. DAPG significantly outperforms DDPGfD. For DAPG, we plot the performance of the ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 6 (2) Do the resulting policies exhibit desirable properties like), p. 6 (2) Do the resulting policies exhibit desirable properties like), p. 7 (2) Do the resulting policies exhibit desirable properties like), p. 7 (2) Do the resulting policies exhibit desirable properties like), p. 1 (Figure/Table caption) |
| Primary metric/result | With the shaped rewards, we find that NPG is indeed able to achieve high success percentage on these tasks (Figure 7), while DDPG was ... | numeric claim only at cited anchor | p. 6 (2) Do the resulting policies exhibit desirable properties like) |

- Numeric sentences retained from the body:
- **p. 6 / 2) Do the resulting policies exhibit desirable properties like - extractive body cue:** We score the different methods based on the percentage of successful trajectories the trained policies can generate, using a sample size of 100 trajectories.
- **p. 7 / 2) Do the resulting policies exhibit desirable properties like - extractive body cue:** 0 20 40 60 80 100 Robot Hours 0 20 40 60 80 100 Success Percentage Object Relocation 0 5 10 15 20 Robot Hours ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Subsequently, we demonstrate the benefits of incorporating human demonstrations with regard to faster learning, increased robustness of trained policies, and ability to cope with ... | p. 6 (V. RESULTS AND DISCUSSION) |
| body limitation/failure cue | robustness to variations in the environment? | p. 6 (2) Do the resulting policies exhibit desirable properties like) |
| body limitation/failure cue | The mental models of solution strategies that humans have for these tasks are indeed quite robust. | p. 7 (2) Do the resulting policies exhibit desirable properties like) |
| body limitation/failure cue | Furthermore, we take the additional step of analyzing the robustness of these policies to variations in environments that were not experienced during training. | p. 7 (2) Do the resulting policies exhibit desirable properties like) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| DDPG can be very sample efficient, but is known to be very sensitive to hyperparameters and random seeds [16], which may explain the difficulty ... | p. 6 (2) Do the resulting policies exhibit desirable properties like) |
| Our implementation of NPG for the experiments is based on Rajeswaran et al. | p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG)) |
| First, NPG computes the vanilla policy gradient, or REINFORCE [54] gradient: g = 1 NT N X i=1 T X t=1 ∇θ log πθ(ai ... | p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG)) |
| 3) Are the resulting movements safe for execution on physical hardware, and are elegant/nimble/human-like? | p. 6 (2) Do the resulting policies exhibit desirable properties like) |
| (b/c) unnatural grasp for hammer (d) unnatural use of wrist for unlatching the door. be useful for training on the physical hardware. | p. 7 (2) Do the resulting policies exhibit desirable properties like) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / V. RESULTS AND DISCUSSION - extractive body cue:** Subsequently, we demonstrate the benefits of incorporating human demonstrations with regard to faster learning, increased robustness of trained policies, and ability to cope with sparse ...
- **p. 6 / 2) Do the resulting policies exhibit desirable properties like - extractive body cue:** robustness to variations in the environment?
- **p. 7 / 2) Do the resulting policies exhibit desirable properties like - extractive body cue:** The mental models of solution strategies that humans have for these tasks are indeed quite robust.
- **p. 7 / 2) Do the resulting policies exhibit desirable properties like - extractive body cue:** Furthermore, we take the additional step of analyzing the robustness of these policies to variations in environments that were not experienced during training.

- **PDF anchors reviewed:** datasets p. 6 (2) Do the resulting policies exhibit desirable properties like), p. 7 (2) Do the resulting policies exhibit desirable properties like), p. 6 (2) Do the resulting policies exhibit desirable properties like), p. 7 (2) Do the resulting policies exhibit desirable properties like), metrics p. 6 (V. RESULTS AND DISCUSSION), p. 7 (2) Do the resulting policies exhibit desirable properties like), p. 6 (2) Do the resulting policies exhibit desirable properties like), p. 7 (Figure/Table caption), p. 1 (Figure/Table caption), p. 3 (Figure/Table caption), baselines p. 8 (Figure/Table caption), results p. 8 (Figure/Table caption), p. 6 (2) Do the resulting policies exhibit desirable properties like), p. 6 (2) Do the resulting policies exhibit desirable properties like), p. 7 (2) Do the resulting policies exhibit desirable properties like), p. 7 (2) Do the resulting policies exhibit desirable properties like), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
