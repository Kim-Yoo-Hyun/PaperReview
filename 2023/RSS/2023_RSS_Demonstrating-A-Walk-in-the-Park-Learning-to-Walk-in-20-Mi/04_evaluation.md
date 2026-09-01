# Evaluation - Demonstrating A Walk in the Park: Learning to Walk in 20 Minutes With Model-Free Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://roboticsproceedings.org/rss19/p056.html; PDF retrieval source: https://arxiv.org/pdf/2208.07860. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (V. SIMULATION ANALYSIS), p. 5 (V. SIMULATION ANALYSIS), p. 5 (V. SIMULATION ANALYSIS), p. 6 (V. SIMULATION ANALYSIS)): From these results, we can conclude that a variety of regularization or normalization methods, if implemented and applied carefully, can all achieve a similar level of improvement in performance over ...

## Evaluation Body Digest

- **p. 5 / V. SIMULATION ANALYSIS - extractive PDF cue:** 3: Experimental evaluation of (a) performance for different value of the damping parameter for the position PD controller; (b) ablations of various task setup choices; ...
- **p. 6 / V. SIMULATION ANALYSIS - extractive PDF cue:** We also compare updating the agent between episodes and after every environment step and notice that getting immediate feedback leads to more stable training and ...
- **p. 5 / V. SIMULATION ANALYSIS - extractive PDF cue:** Since our goal is to run training on a real robot, we aim for design decisions and algorithms that lead to improved stability and sample ...
- **p. 6 / V. SIMULATION ANALYSIS - extractive PDF cue:** 4: Examples of learned gaits acquired on a variety of real-world terrains.
- **p. 5 / V. SIMULATION ANALYSIS - extractive PDF cue:** To match the real-world setup, we simulate the official A1 model in MuJoCo, and used the same position controller and rewards as discussed in Section ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 5: Learning curves for all the real-world experiments showing the average velocity of the stochastic policy with respect to real-world, wall- clock time. Note ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: We demonstrate that deep reinforcement learning can be used to efficiently train a quadruped robot directly on various real world terrains, e.g., flat ...
- **p. 6 / V. SIMULATION ANALYSIS - extractive PDF cue:** From these results, we can conclude that a variety of regularization or normalization methods, if implemented and applied carefully, can all achieve a similar level ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** legged robot, terrain과 contact dynamics.
- **Input boundary:** proprioception, terrain/perception observation과 velocity command.
- **Output/decision under evaluation:** joint target, torque, footstep 또는 locomotion action.
- **Primary target:** velocity/progress, stability, energy와 terrain generalization.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| V. SIMULATION ANALYSIS | EMPIRICAL / REAL-ROBOT OR HARDWARE | From these results, we can conclude that a variety of regularization or normalization methods, if implemented and applied carefully, can all achieve a similar ... | p. 6 (V. SIMULATION ANALYSIS) |
| V. SIMULATION ANALYSIS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Since our goal is to run training on a real robot, we aim for design decisions and algorithms that lead to improved stability and ... | p. 5 (V. SIMULATION ANALYSIS) |
| V. SIMULATION ANALYSIS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We see that na¨ıvely increasing the number of critic updates made per time-step improves sample efficiency, but still requires roughly 30k samples, which would ... | p. 5 (V. SIMULATION ANALYSIS) |
| V. SIMULATION ANALYSIS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Left to right: flat, solid ground covered in dense foam mats; a 5cm memory foam mattress; loose ground comprised of eucalyptus bark; a grassy ... | p. 6 (V. SIMULATION ANALYSIS) |

## Dataset / Benchmark Role

- **p. 5 / V. SIMULATION ANALYSIS - extractive PDF cue:** 3: Experimental evaluation of (a) performance for different value of the damping parameter for the position PD controller; (b) ablations of various task setup choices; ...
- **p. 6 / V. SIMULATION ANALYSIS - extractive PDF cue:** We also compare updating the agent between episodes and after every environment step and notice that getting immediate feedback leads to more stable training and ...
- **p. 5 / V. SIMULATION ANALYSIS - extractive PDF cue:** Since our goal is to run training on a real robot, we aim for design decisions and algorithms that lead to improved stability and sample ...
- **p. 6 / V. SIMULATION ANALYSIS - extractive PDF cue:** 4: Examples of learned gaits acquired on a variety of real-world terrains.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: We demonstrate that deep reinforcement learning can be used to efficiently train a quadruped robot directly on various real world terrains, e.g., flat ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 3: Experimental evaluation of (a) performance for different value of the damping parameter for the position PD controller; (b) ablations of various task setup ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 4: Examples of learned gaits acquired on a variety of real-world terrains. Left to right: flat, solid ground covered in dense foam mats; a ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 5: Learning curves for all the real-world experiments showing the average velocity of the stochastic policy with respect to real-world, wall- clock time. Note ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 3: Experimental evaluation of (a) performance for different value of the damping parameter for the position PD controller; (b) ablations of various task setup ... | embodiment, simulator version and control stack | p. 5 (V. SIMULATION ANALYSIS), p. 6 (V. SIMULATION ANALYSIS) |
| Task/environment | We also compare updating the agent between episodes and after every environment step and notice that getting immediate feedback leads to more stable training ... | reset, timeout, object/scene variation | p. 6 (V. SIMULATION ANALYSIS), p. 5 (V. SIMULATION ANALYSIS) |
| Observation/sensor | proprioception, terrain/perception observation과 velocity command | calibration, preprocessing, privileged input | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Output/decision | joint target, torque, footstep 또는 locomotion action | action frame, controller and termination | p. 2 (I. INTRODUCTION), p. 4 (B. Efficient Model-Free RL) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| To match the real-world setup, we simulate the official A1 model in MuJoCo, and used the same position controller and rewards as discussed in ... | definition/direction/unit from same section | p. 5 (V. SIMULATION ANALYSIS) |
| Fig. 3: Experimental evaluation of (a) performance for different value of the damping parameter for the position PD controller; (b) ablations of various task ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Fig. 5: Learning curves for all the real-world experiments showing the average velocity of the stochastic policy with respect to real-world, wall- clock time. ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Fig. 1: We demonstrate that deep reinforcement learning can be used to efficiently train a quadruped robot directly on various real world terrains, e.g., ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| From these results, we can conclude that a variety of regularization or normalization methods, if implemented and applied carefully, can all achieve a similar ... | definition/direction/unit from same section | p. 6 (V. SIMULATION ANALYSIS) |
| Left to right: flat, solid ground covered in dense foam mats; a 5cm memory foam mattress; loose ground comprised of eucalyptus bark; a grassy ... | definition/direction/unit from same section | p. 6 (V. SIMULATION ANALYSIS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Therefore, for the remaining ablations, we used the value of damping set to 10. | comparison identity and matched condition | p. 5 (V. SIMULATION ANALYSIS) |
| This section presents simulated comparisons of design decisions and SAC variants we considered in this work. | comparison identity and matched condition | p. 5 (V. SIMULATION ANALYSIS) |
| Left to right: flat, solid ground covered in dense foam mats; a 5cm memory foam mattress; loose ground comprised of eucalyptus bark; a grassy ... | comparison identity and matched condition | p. 6 (V. SIMULATION ANALYSIS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 3: Experimental evaluation of (a) performance for different value of the damping parameter for the position PD controller; (b) ablations of various task setup ... | component/input/data sensitivity | p. 5 (V. SIMULATION ANALYSIS) |
| In particular, we confirm the efficacy of constraining the action space: we observe that the simulated agent cannot make any progress in the unconstrained ... | component/input/data sensitivity | p. 5 (V. SIMULATION ANALYSIS) |
| As such, we favor using the less computationally expensive DroQ variants over others in the real world. | component/input/data sensitivity | p. 6 (V. SIMULATION ANALYSIS) |
| Left to right: flat, solid ground covered in dense foam mats; a 5cm memory foam mattress; loose ground comprised of eucalyptus bark; a grassy ... | component/input/data sensitivity | p. 6 (V. SIMULATION ANALYSIS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contribution is an empirical demonstration that current deep RL methods can effectively learn quadrupedal locomotion directly in the real world in under ... | From these results, we can conclude that a variety of regularization or normalization methods, if implemented and applied carefully, can all achieve a similar ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (V. SIMULATION ANALYSIS), p. 5 (V. SIMULATION ANALYSIS), p. 5 (V. SIMULATION ANALYSIS), p. 6 (V. SIMULATION ANALYSIS) |
| Primary metric/result | Since our goal is to run training on a real robot, we aim for design decisions and algorithms that lead to improved stability and ... | numeric claim only at cited anchor | p. 5 (V. SIMULATION ANALYSIS) |

- Numeric sentences retained from the body:
- **p. 5 / V. SIMULATION ANALYSIS - extractive PDF cue:** In particular, we confirm the efficacy of constraining the action space: we observe that the simulated agent cannot make any progress in the unconstrained action ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In the simulator, we used p = [0.05, 0.7, -1.4]; however, during the early experiments in the real world, we found that p = ... | p. 4 (IV. SYSTEM DESIGN) |
| body limitation/failure cue | As such, such policies cannot trivially be further trained in the real world. | p. 4 (IV. SYSTEM DESIGN) |
| body limitation/failure cue | During early experiments with the real robot, we found that using the forward velocity in the robot's local frame caused it to dive forward ... | p. 5 (IV. SYSTEM DESIGN) |
| body limitation/failure cue | In particular, we confirm the efficacy of constraining the action space: we observe that the simulated agent cannot make any progress in the unconstrained ... | p. 5 (V. SIMULATION ANALYSIS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Because of this, a na¨ıve implementation cannot train as fast as the samples are collected. | p. 4 (B. Efficient Model-Free RL) |
| Prior work has addressed this either by performing asynchronous training [23], [28] or training in-between trials [24]. | p. 4 (B. Efficient Model-Free RL) |
| Efficiency can be increased by taking more gradient steps, and we show standard SAC with a larger UTD ratio of 20 (dark blue) as ... | p. 5 (V. SIMULATION ANALYSIS) |
| Since our goal is to run training on a real robot, we aim for design decisions and algorithms that lead to improved stability and ... | p. 5 (V. SIMULATION ANALYSIS) |
| In order to facilitate this kind of training synchronously, the updates must be inexpensive enough to be able to perform them between time-steps (of ... | p. 6 (V. SIMULATION ANALYSIS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / IV. SYSTEM DESIGN - extractive PDF cue:** In the simulator, we used p = [0.05, 0.7, -1.4]; however, during the early experiments in the real world, we found that p = [0.05, ...
- **p. 4 / IV. SYSTEM DESIGN - extractive PDF cue:** As such, such policies cannot trivially be further trained in the real world.
- **p. 5 / IV. SYSTEM DESIGN - extractive PDF cue:** During early experiments with the real robot, we found that using the forward velocity in the robot's local frame caused it to dive forward as ...
- **p. 5 / V. SIMULATION ANALYSIS - extractive PDF cue:** In particular, we confirm the efficacy of constraining the action space: we observe that the simulated agent cannot make any progress in the unconstrained action ...

- **PDF anchors reviewed:** datasets p. 5 (V. SIMULATION ANALYSIS), p. 6 (V. SIMULATION ANALYSIS), p. 5 (V. SIMULATION ANALYSIS), p. 6 (V. SIMULATION ANALYSIS), metrics p. 5 (V. SIMULATION ANALYSIS), p. 5 (Figure/Table caption), p. 7 (Figure/Table caption), p. 1 (Figure/Table caption), p. 6 (V. SIMULATION ANALYSIS), p. 6 (V. SIMULATION ANALYSIS), baselines p. 5 (V. SIMULATION ANALYSIS), p. 5 (V. SIMULATION ANALYSIS), p. 6 (V. SIMULATION ANALYSIS), results p. 6 (V. SIMULATION ANALYSIS), p. 5 (V. SIMULATION ANALYSIS), p. 5 (V. SIMULATION ANALYSIS), p. 6 (V. SIMULATION ANALYSIS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
