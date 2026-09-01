# Evaluation - Learning Memory-Based Control for Human-Scale Bipedal Locomotion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss16/p031.html; PDF retrieval source: https://www.roboticsproceedings.org/rss16/p031.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (IV. RESULTS), p. 5 (IV. RESULTS), p. 1 (Figure/Table caption)): As can be seen, dynamics randomization improves performance of both policy types and LSTM with dynamics randomization performs the best.

## Evaluation Body Digest

- **p. 5 / IV. RESULTS - extractive PDF cue:** The LSTM achieves a much higher reward with remarkably little variance, but both networks perform roughly the same on hardware.
- **p. 5 / IV. RESULTS - extractive PDF cue:** All networks were trained for fifty million simulation timesteps, and each iteration we sampled about fifty thousand timesteps from the simulated environment.
- **p. 4 / IV. RESULTS - extractive PDF cue:** Simulation We trained ten LSTM networks and ten FF networks with dynamics randomization, and ten LSTM networks and ten FF networks without dynamics randomization, each ...
- **p. 5 / IV. RESULTS - extractive PDF cue:** Feedforward networks obtain a notably lower reward, with high variance.
- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: We use recurrent neural networks and dynamics randomization to greatly improve the sim-to-real transfer rate and demonstrate learned, memory-based control on the bipedal ...
- **p. 5 / IV. RESULTS - extractive PDF cue:** As can be seen, dynamics randomization improves performance of both policy types and LSTM with dynamics randomization performs the best.
- **p. 6 / V. CONCLUSION - extractive PDF cue:** The policies were learned and tested first in simulation, then transferred to the robot, demonstrating the robustness and promise of this approach.
- **p. 5 / IV. RESULTS - extractive PDF cue:** We conducted a robustness test in simulation across ten chosen sets of dynamics, taken from the range in Table I.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** legged robot, terrain과 contact dynamics.
- **Input boundary:** proprioception, terrain/perception observation과 velocity command.
- **Output/decision under evaluation:** joint target, torque, footstep 또는 locomotion action.
- **Primary target:** velocity/progress, stability, energy와 terrain generalization.
- **Detected evaluation headings:** IV. RESULTS (p. 4).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | As can be seen, dynamics randomization improves performance of both policy types and LSTM with dynamics randomization performs the best. | p. 5 (IV. RESULTS) |
| IV. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The LSTM achieves a much higher reward with remarkably little variance, but both networks perform roughly the same on hardware. | p. 5 (IV. RESULTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 1: We use recurrent neural networks and dynamics randomization to greatly improve the sim-to-real transfer rate and demonstrate learned, memory-based control on the ... | p. 1 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / IV. RESULTS - extractive PDF cue:** The LSTM achieves a much higher reward with remarkably little variance, but both networks perform roughly the same on hardware.
- **p. 5 / IV. RESULTS - extractive PDF cue:** All networks were trained for fifty million simulation timesteps, and each iteration we sampled about fifty thousand timesteps from the simulated environment.
- **p. 4 / IV. RESULTS - extractive PDF cue:** Simulation We trained ten LSTM networks and ten FF networks with dynamics randomization, and ten LSTM networks and ten FF networks without dynamics randomization, each ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: We use recurrent neural networks and dynamics randomization to greatly improve the sim-to-real transfer rate and demonstrate learned, memory-based control on the bipedal ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2: We provide an RNN with a clock input, a velocity command, and information about the robot's state. The RNN produces joint position commands ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 3: A diagram of the RNN structure (left) and conventional NN structure (right) we use in our experiments. The recurrent policy has connections which ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 4: A PCA projection of the hidden layer activations of a feedforward policy (top) and of an LSTM policy (bottom) could imply that using ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 5: Reward curve of LSTM and FF networks during training without dynamics randomization. The LSTM achieves a much higher reward with remarkably little variance, ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The LSTM achieves a much higher reward with remarkably little variance, but both networks perform roughly the same on hardware. | embodiment, simulator version and control stack | p. 5 (IV. RESULTS), p. 5 (IV. RESULTS) |
| Task/environment | All networks were trained for fifty million simulation timesteps, and each iteration we sampled about fifty thousand timesteps from the simulated environment. | reset, timeout, object/scene variation | p. 5 (IV. RESULTS), p. 4 (IV. RESULTS) |
| Observation/sensor | proprioception, terrain/perception observation과 velocity command | calibration, preprocessing, privileged input | p. 3 (III. METHOD), p. 2 (II. BACKGROUND) |
| Output/decision | joint target, torque, footstep 또는 locomotion action | action frame, controller and termination | p. 3 (III. METHOD), p. 4 (III. METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Feedforward networks obtain a notably lower reward, with high variance. | definition/direction/unit from same section | p. 5 (IV. RESULTS) |
| The LSTM achieves a much higher reward with remarkably little variance, but both networks perform roughly the same on hardware. | definition/direction/unit from same section | p. 5 (IV. RESULTS) |
| Simulation We trained ten LSTM networks and ten FF networks with dynamics randomization, and ten LSTM networks and ten FF networks without dynamics randomization, ... | definition/direction/unit from same section | p. 4 (IV. RESULTS) |
| Fig. 1: We use recurrent neural networks and dynamics randomization to greatly improve the sim-to-real transfer rate and demonstrate learned, memory-based control on the ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Simulation We trained ten LSTM networks and ten FF networks with dynamics randomization, and ten LSTM networks and ten FF networks without dynamics randomization, ... | comparison identity and matched condition | p. 4 (IV. RESULTS) |
| 5: Reward curve of LSTM and FF networks during training without dynamics randomization. | comparison identity and matched condition | p. 5 (IV. RESULTS) |
| As can be seen in Figure 5, when trained without dynamics randomization, LSTM networks attain a significantly higher reward than feedforward networks, with surprisingly ... | comparison identity and matched condition | p. 5 (IV. RESULTS) |
| Fig. 1: We use recurrent neural networks and dynamics randomization to greatly improve the sim-to-real transfer rate and demonstrate learned, memory-based control on the ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 1: We use recurrent neural networks and dynamics randomization to greatly improve the sim-to-real transfer rate and demonstrate learned, memory-based control on the ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Simulation We trained ten LSTM networks and ten FF networks with dynamics randomization, and ten LSTM networks and ten FF networks without dynamics randomization, ... | component/input/data sensitivity | p. 4 (IV. RESULTS) |
| 5: Reward curve of LSTM and FF networks during training without dynamics randomization. | component/input/data sensitivity | p. 5 (IV. RESULTS) |
| As can be seen in Figure 5, when trained without dynamics randomization, LSTM networks attain a significantly higher reward than feedforward networks, with surprisingly ... | component/input/data sensitivity | p. 5 (IV. RESULTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| State Space and Action Space The policy's input consists of: Xt =          fvel desired forward ... | As can be seen, dynamics randomization improves performance of both policy types and LSTM with dynamics randomization performs the best. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (IV. RESULTS), p. 5 (IV. RESULTS), p. 1 (Figure/Table caption) |
| Primary metric/result | The LSTM achieves a much higher reward with remarkably little variance, but both networks perform roughly the same on hardware. | numeric claim only at cited anchor | p. 5 (IV. RESULTS) |

- Numeric sentences retained from the body:
- **p. 5 / IV. RESULTS - extractive PDF cue:** Dots become lighter as a function of time. batch size of 64 trajectories and a maximum trajectory length of 300 timesteps, equal to 9 seconds ...
- **p. 5 / IV. RESULTS - extractive PDF cue:** Parameter Set LSTM LSTM DR FF FF DR µ1 1.3s > 40.0s 1.6s 17.1s µ2 > 40.0s > 40.0s > 40s > 40.0s µ3 1.9s ...
- **p. 5 / IV. RESULTS - extractive PDF cue:** 23.5s 40.0s 14.8s 22.1s TABLE II: Average time (in seconds) that ten randomly seeded policies were able to walk in simulation subject to the conditions ...
- **p. 3 / III. METHOD - extractive PDF cue:** The policy is evaluated every 30 milliseconds, or roughly 33Hz, while the PD controller operates at 2kHz, as can be seen in Figure 2.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 1: We use recurrent neural networks and dynamics randomization to greatly improve the sim-to-real transfer rate and demonstrate learned, memory-based control on the ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | The policies were learned and tested first in simulation, then transferred to the robot, demonstrating the robustness and promise of this approach. | p. 6 (V. CONCLUSION) |
| body limitation/failure cue | We conducted a robustness test in simulation across ten chosen sets of dynamics, taken from the range in Table I. | p. 5 (IV. RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| When training the feedforward policies, we used a batch size of 1024 timesteps. | p. 5 (IV. RESULTS) |
| Dots become lighter as a function of time. batch size of 64 trajectories and a maximum trajectory length of 300 timesteps, equal to 9 ... | p. 5 (IV. RESULTS) |
| Though we believe that the recurrent policies do not have any theoretical reason for needing a clock input, we were not able to train ... | p. 3 (III. METHOD) |
| We aggressively randomize the pelvis center of mass because we believe the robot's center of mass in simulation differs significantly from the center of ... | p. 3 (III. METHOD) |
| Compute advantage estimates ˆAbuff. for epoch=1,2, ... | p. 4 (III. METHOD) |
| Pseudocode of the recurrent version of the algorithm that we used can be seen in Algorithm 1. | p. 4 (III. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: We use recurrent neural networks and dynamics randomization to greatly improve the sim-to-real transfer rate and demonstrate learned, memory-based control on the bipedal ...
- **p. 6 / V. CONCLUSION - extractive PDF cue:** The policies were learned and tested first in simulation, then transferred to the robot, demonstrating the robustness and promise of this approach.
- **p. 5 / IV. RESULTS - extractive PDF cue:** We conducted a robustness test in simulation across ten chosen sets of dynamics, taken from the range in Table I.

- **PDF anchors reviewed:** datasets p. 5 (IV. RESULTS), p. 5 (IV. RESULTS), p. 4 (IV. RESULTS), metrics p. 5 (IV. RESULTS), p. 5 (IV. RESULTS), p. 4 (IV. RESULTS), p. 1 (Figure/Table caption), baselines p. 4 (IV. RESULTS), p. 5 (IV. RESULTS), p. 5 (IV. RESULTS), p. 1 (Figure/Table caption), results p. 5 (IV. RESULTS), p. 5 (IV. RESULTS), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
