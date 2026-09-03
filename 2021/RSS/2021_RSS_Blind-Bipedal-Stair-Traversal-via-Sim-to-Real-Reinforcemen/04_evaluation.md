# Evaluation - Blind Bipedal Stair Traversal via Sim-to-Real Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss17/p061.html; PDF retrieval source: https://www.roboticsproceedings.org/rss17/p061.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 4 (Figure/Table caption), p. 5 (Figure/Table caption), p. 7 (Figure/Table caption)): Fig. 3: The learned policies exhibit a high degree of blind robustness to a variety of stair-like terrain, and can reliably ascend and descend stairs of typical dimensions found in ...

## Evaluation Body Digest

- **p. 4 / IV. RESULTS - extractive body cue:** Each policy was trained until 300 million timesteps were sampled from the virtual environment, simulated with MuJoCo [22].
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: The learned policies exhibit a high degree of blind robustness to a variety of stair-like terrain, and can reliably ascend and descend stairs ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: We evaluate the probability of successfully climbing and descending stairs without falling as a function of commanded speed between 0.25 m/s and 1.5 ...
- **p. 4 / IV. RESULTS - extractive body cue:** We use the Adam [23] optimizer with a learning rate of 0.0005 for both the actor and critic, which are learned separately and do not ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: In order to ensure robustness over a variety of possible stair- like terrain, we randomize a number of parameters when generating stairs at ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: A comparison of the swing foot motion of the Stair LSTM policy and the Flat Ground LSTM policy while locomoting at 1.0 m/s. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: The ground reaction forces and cumulative impulses of a Stair LSTM policy when it encounters varying ground height. The peak vertical force (A) ...
- **p. 7 / V. CONCLUSION - extractive body cue:** In future work, it will be interesting to investigate how vision can be most effectively used to improve the efficiency and/or performance of a blind ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** legged robot, terrain과 contact dynamics.
- **Input boundary:** proprioception, terrain/perception observation과 velocity command.
- **Output/decision under evaluation:** joint target, torque, footstep 또는 locomotion action.
- **Primary target:** velocity/progress, stability, energy와 terrain generalization.
- **Detected evaluation headings:** IV. RESULTS (p. 4).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SIMULATION | Fig. 3: The learned policies exhibit a high degree of blind robustness to a variety of stair-like terrain, and can reliably ascend and descend ... | p. 4 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Fig. 4: We evaluate the probability of successfully climbing and descending stairs without falling as a function of commanded speed between 0.25 m/s and ... | p. 5 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Fig. 6: The ground reaction forces and cumulative impulses of a Stair LSTM policy when it encounters varying ground height. The peak vertical force ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 4 / IV. RESULTS - extractive body cue:** Each policy was trained until 300 million timesteps were sampled from the virtual environment, simulated with MuJoCo [22].

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: In this work, we investigate the limits of blind bipedal locomo- tion. We present a training pipeline which produces policies capable of blindly ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: In order to ensure robustness over a variety of possible stair- like terrain, we randomize a number of parameters when generating stairs at ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: The learned policies exhibit a high degree of blind robustness to a variety of stair-like terrain, and can reliably ascend and descend stairs ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: We evaluate the probability of successfully climbing and descending stairs without falling as a function of commanded speed between 0.25 m/s and 1.5 ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: A comparison of the swing foot motion of the Stair LSTM policy and the Flat Ground LSTM policy while locomoting at 1.0 m/s. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: The ground reaction forces and cumulative impulses of a Stair LSTM policy when it encounters varying ground height. The peak vertical force (A) ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: By alternatingly punishing foot forces during a ‘stance' phase to teach the policy to lift the foot, and punishing foot velocities during a ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Each policy was trained until 300 million timesteps were sampled from the virtual environment, simulated with MuJoCo [22]. | embodiment, simulator version and control stack | p. 4 (IV. RESULTS) |
| Task/environment | not recovered | reset, timeout, object/scene variation | 본문 anchor 없음 |
| Observation/sensor | proprioception, terrain/perception observation과 velocity command | calibration, preprocessing, privileged input | p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 2 (II. REINFORCEMENT LEARNING FORMULATION) |
| Output/decision | joint target, torque, footstep 또는 locomotion action | action frame, controller and termination | p. 3 (II. REINFORCEMENT LEARNING FORMULATION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 3: The learned policies exhibit a high degree of blind robustness to a variety of stair-like terrain, and can reliably ascend and descend ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Fig. 4: We evaluate the probability of successfully climbing and descending stairs without falling as a function of commanded speed between 0.25 m/s and ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| We use the Adam [23] optimizer with a learning rate of 0.0005 for both the actor and critic, which are learned separately and do ... | definition/direction/unit from same section | p. 4 (IV. RESULTS) |
| Fig. 2: In order to ensure robustness over a variety of possible stair- like terrain, we randomize a number of parameters when generating stairs ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Fig. 5: A comparison of the swing foot motion of the Stair LSTM policy and the Flat Ground LSTM policy while locomoting at 1.0 ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Fig. 6: The ground reaction forces and cumulative impulses of a Stair LSTM policy when it encounters varying ground height. The peak vertical force ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We also trained a group of policies without stair terrain randomization, and denote these Flat Ground LSTM, to investigate the importance of the terrain ... | comparison identity and matched condition | p. 4 (IV. RESULTS) |
| Fig. 4: We evaluate the probability of successfully climbing and descending stairs without falling as a function of commanded speed between 0.25 m/s and ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| Fig. 5: A comparison of the swing foot motion of the Stair LSTM policy and the Flat Ground LSTM policy while locomoting at 1.0 ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 4: We evaluate the probability of successfully climbing and descending stairs without falling as a function of commanded speed between 0.25 m/s and ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| We also trained a group of policies without stair terrain randomization, and denote these Flat Ground LSTM, to investigate the importance of the terrain ... | component/input/data sensitivity | p. 4 (IV. RESULTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We present a training pipeline which produces policies capable of blindly ascending and descending stairs in the real world. | Fig. 3: The learned policies exhibit a high degree of blind robustness to a variety of stair-like terrain, and can reliably ascend and descend ... | PDF body cue; verify exact table/figure and matched conditions | p. 4 (Figure/Table caption), p. 5 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Primary metric/result | Fig. 4: We evaluate the probability of successfully climbing and descending stairs without falling as a function of commanded speed between 0.25 m/s and ... | numeric claim only at cited anchor | p. 5 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 4 / IV. RESULTS - extractive body cue:** Our selection of hyperparameters for the PPO algorithm includes a replay buffer size of 50,000 timesteps, a batch size of 64 trajectories for recurrent policies, ...
- **p. 2 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** Action Space The output action at of the control policy at each time step (running at 40Hz) is an 11 dimensional vector with the first ...
- **p. 3 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** (2) This delta is bounded in a way such that the policy can choose to regulate the gait cycle between 0.5x and 1.5x the nominal ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In future work, it will be interesting to investigate how vision can be most effectively used to improve the efficiency and/or performance of a ... | p. 7 (V. CONCLUSION) |
| body limitation/failure cue | Fig. 4: We evaluate the probability of successfully climbing and descending stairs without falling as a function of commanded speed between 0.25 m/s and ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | Fig. 1: In this work, we investigate the limits of blind bipedal locomo- tion. We present a training pipeline which produces policies capable of ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | In this work, we have motivated the desirability of a highly robust but blind walking controller, and demonstrated that such a blind bipedal walking ... | p. 7 (V. CONCLUSION) |
| body limitation/failure cue | Fig. 2: In order to ensure robustness over a variety of possible stair- like terrain, we randomize a number of parameters when generating stairs ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | Fig. 3: The learned policies exhibit a high degree of blind robustness to a variety of stair-like terrain, and can reliably ascend and descend ... | p. 4 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Our selection of hyperparameters for the PPO algorithm includes a replay buffer size of 50,000 timesteps, a batch size of 64 trajectories for recurrent ... | p. 4 (IV. RESULTS) |
| We use the Adam [23] optimizer with a learning rate of 0.0005 for both the actor and critic, which are learned separately and do ... | p. 4 (IV. RESULTS) |
| Given that maximum episode length is 300 discrete timesteps, this means each command will change at least once on average per episode. | p. 2 (II. REINFORCEMENT LEARNING FORMULATION) |
| Each episode is limited to be 300 timesteps, which corresponds to about 7.5 seconds of simulation time. | p. 3 (II. REINFORCEMENT LEARNING FORMULATION) |
| For recurrent policies, we sample batches of episodes from a replay buffer as in [19], while for feedforward policies we sample batches of timesteps. | p. 3 (II. REINFORCEMENT LEARNING FORMULATION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / V. CONCLUSION - extractive body cue:** In future work, it will be interesting to investigate how vision can be most effectively used to improve the efficiency and/or performance of a blind ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: We evaluate the probability of successfully climbing and descending stairs without falling as a function of commanded speed between 0.25 m/s and 1.5 ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: In this work, we investigate the limits of blind bipedal locomo- tion. We present a training pipeline which produces policies capable of blindly ...
- **p. 7 / V. CONCLUSION - extractive body cue:** In this work, we have motivated the desirability of a highly robust but blind walking controller, and demonstrated that such a blind bipedal walking controller ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: In order to ensure robustness over a variety of possible stair- like terrain, we randomize a number of parameters when generating stairs at ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: The learned policies exhibit a high degree of blind robustness to a variety of stair-like terrain, and can reliably ascend and descend stairs ...

- **Evidence anchors reviewed:** datasets p. 4 (IV. RESULTS), metrics p. 4 (Figure/Table caption), p. 5 (Figure/Table caption), p. 4 (IV. RESULTS), p. 3 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), baselines p. 4 (IV. RESULTS), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), results p. 4 (Figure/Table caption), p. 5 (Figure/Table caption), p. 7 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
