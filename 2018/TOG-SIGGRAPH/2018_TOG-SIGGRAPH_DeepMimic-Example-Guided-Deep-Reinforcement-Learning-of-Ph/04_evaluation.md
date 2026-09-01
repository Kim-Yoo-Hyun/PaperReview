# Evaluation - DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1804.02717; PDF retrieval source: https://arxiv.org/pdf/1804.02717. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 12 (10 RESULTS), p. 11 (10 RESULTS), p. 11 (10 RESULTS), p. 12 (10 RESULTS), p. 10 (10 RESULTS), p. 10 (10 RESULTS)): The performance achieved by the Atlas policies are comparable to those achieved by the humanoid.

## Evaluation Body Digest

- **p. 10 / 10 RESULTS - extractive body cue:** Each environment is denoted by "Character: Skill - Task".
- **p. 10 / 10 RESULTS - extractive body cue:** The weights for the imitation and task objectives are set to ωI = 0.7 and ωG = 0.3 for all tasks.
- **p. 11 / 10 RESULTS - extractive body cue:** Success rate of policies trained with the imitation or task objectives disabled.
- **p. 11 / 10 RESULTS - extractive body cue:** Simply imitating the reference motions proves insufficient for fulfilling the task objectives.
- **p. 12 / 10 RESULTS - extractive body cue:** 10.3 Retargeting Due to modeling discrepancies between simulation and the real world, the dynamics under which a motion capture clip was recorded can differ dramatically ...
- **p. 12 / 10 RESULTS - extractive body cue:** Examples of the environments are available in Figure 4.
- **p. 11 / 10 RESULTS - extractive body cue:** Similarly, for the strike task, the policy trained with both objectives successfully hits 99% of the targets, while the policy trained only to imitate the ...
- **p. 10 / 10 RESULTS - extractive body cue:** Performance is measured by the average return normalized by the minimum and maximum possible return per episode.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** 10 RESULTS (p. 10).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 10 RESULTS | EMPIRICAL / SIMULATION | The performance achieved by the Atlas policies are comparable to those achieved by the humanoid. | p. 12 (10 RESULTS) |
| 10 RESULTS | EMPIRICAL / SIMULATION | Success rate of policies trained with the imitation or task objectives disabled. | p. 11 (10 RESULTS) |
| 10 RESULTS | EMPIRICAL / SIMULATION | Similarly, for the strike task, the policy trained with both objectives successfully hits 99% of the targets, while the policy trained only to imitate ... | p. 11 (10 RESULTS) |
| 10 RESULTS | EMPIRICAL / SIMULATION | Skill RSI + ET ET RSI Backflip 0.791 0.730 0.379 Sideflip 0.823 0.717 0.355 Spinkick 0.848 0.858 0.358 Walk 0.980 0.981 0.974 and 0.630 ... | p. 12 (10 RESULTS) |
| 10 RESULTS | EMPIRICAL / SIMULATION | A comprehensive list of the learned skills and performance statistics is available in Table 2. | p. 10 (10 RESULTS) |

## Dataset / Benchmark Role

- **p. 10 / 10 RESULTS - extractive body cue:** Each environment is denoted by "Character: Skill - Task".
- **p. 10 / 10 RESULTS - extractive body cue:** The weights for the imitation and task objectives are set to ωI = 0.7 and ωG = 0.3 for all tasks.
- **p. 11 / 10 RESULTS - extractive body cue:** Success rate of policies trained with the imitation or task objectives disabled.
- **p. 11 / 10 RESULTS - extractive body cue:** Simply imitating the reference motions proves insufficient for fulfilling the task objectives.
- **p. 12 / 10 RESULTS - extractive body cue:** 10.3 Retargeting Due to modeling discrepancies between simulation and the real world, the dynamics under which a motion capture clip was recorded can differ dramatically ...
- **p. 12 / 10 RESULTS - extractive body cue:** Examples of the environments are available in Figure 4.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Highly dynamic skills learned by imitating reference motion capture clips using our method, executed by physically simulated characters. Left: Humanoid character performing a ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2. Schematic illustration of the visuomotor policy network. The heightmap H is processed by 3 convolutional layers with 16 8x8 filters, 32 4x4 filters, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3. 3D simulated characters. Our framework is able to train policies for a wide range of character morphologies. states from the reference motion, the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Properties of the characters. Property Humanoid Atlas T-Rex Dragon Links 13
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4. Characters traversing randomly generated terrains. Top-to-bottom: mixed obstacles, dense gaps, winding balance beam, stairs. The blue line traces the trajectory of the character's ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. Performance statistics of imitating various skills. All skills are performed by the humanoid unless stated otherwise. Policies are trained only to imitate a ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 5. Snapshots of motions from the trained policies. Top-to-bottom: walk, run, cartwheel, dance A, backflip, frontflip, roll. and a binary variable h that indicates ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 6. Simulated characters performing various skills. Our framework is able to train policies for a broad range of characters, skills, and environments. ACM Trans. ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Each environment is denoted by "Character: Skill - Task". | embodiment, simulator version and control stack | p. 10 (10 RESULTS), p. 10 (10 RESULTS) |
| Task/environment | The weights for the imitation and task objectives are set to ωI = 0.7 and ωG = 0.3 for all tasks. | reset, timeout, object/scene variation | p. 10 (10 RESULTS), p. 11 (10 RESULTS) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 4 (4 BACKGROUND), p. 5 (4 BACKGROUND) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 3 (4 BACKGROUND), p. 4 (4 BACKGROUND) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Success rate of policies trained with the imitation or task objectives disabled. | definition/direction/unit from same section | p. 11 (10 RESULTS) |
| Similarly, for the strike task, the policy trained with both objectives successfully hits 99% of the targets, while the policy trained only to imitate ... | definition/direction/unit from same section | p. 11 (10 RESULTS) |
| Performance is measured by the average return normalized by the minimum and maximum possible return per episode. | definition/direction/unit from same section | p. 10 (10 RESULTS) |
| Note that the maximum return may not be achievable. | definition/direction/unit from same section | p. 10 (10 RESULTS) |
| Performance statistics of the Atlas policies are available in Table 2. | definition/direction/unit from same section | p. 12 (10 RESULTS) |
| Next, we explore vision-based locomotion in more complex procedurally generated environments. | definition/direction/unit from same section | p. 12 (10 RESULTS) |
| Fig. 3. 3D simulated characters. Our framework is able to train policies for a wide range of character morphologies. states from the reference motion, ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Fig. 4. Characters traversing randomly generated terrains. Top-to-bottom: mixed obstacles, dense gaps, winding balance beam, stairs. The blue line traces the trajectory of the ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| To investigate the extent to which the motions are adapted for a particular task, we compared the performance of policies trained to optimize both ... | comparison identity and matched condition | p. 11 (10 RESULTS) |
| The humanoid policies, when applied to the Atlas, fail to reproduce any of the skills, achieving a normalized return of 0.013 and 0.014 for ... | comparison identity and matched condition | p. 12 (10 RESULTS) |
| The task is left unspecified for policies that are trained solely to imitate a reference motion without additional task objectives. | comparison identity and matched condition | p. 10 (10 RESULTS) |
| Policy trained for the throw task without a reference motion. | comparison identity and matched condition | p. 11 (10 RESULTS) |
| Learning curves for policies trained with and without reference state initialization (RSI) and early termination (ET). | comparison identity and matched condition | p. 12 (10 RESULTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 2. Performance statistics of imitating various skills. All skills are performed by the humanoid unless stated otherwise. Policies are trained only to imitate ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| The task is left unspecified for policies that are trained solely to imitate a reference motion without additional task objectives. | component/input/data sensitivity | p. 10 (10 RESULTS) |
| Training without a reference motion produces policies that develop awkward, but functional, strategies for satisfying the task objectives. | component/input/data sensitivity | p. 11 (10 RESULTS) |
| Fig. 8. Policy trained for the throw task without a reference motion. Instead of throwing the ball, the character learns to run towards the ... | component/input/data sensitivity | p. 11 (Figure/Table caption) |
| Learning curves for policies trained with and without reference state initialization (RSI) and early termination (ET). | component/input/data sensitivity | p. 12 (10 RESULTS) |
| To retarget the motion clips, we simply copied the local joint rotations from the humanoid to the Atlas, without any further modification. | component/input/data sensitivity | p. 12 (10 RESULTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Although our framework consists of individual components that have been known for some time, the particular combination of these components in the context of ... | The performance achieved by the Atlas policies are comparable to those achieved by the humanoid. | PDF body cue; verify exact table/figure and matched conditions | p. 12 (10 RESULTS), p. 11 (10 RESULTS), p. 11 (10 RESULTS), p. 12 (10 RESULTS), p. 10 (10 RESULTS), p. 10 (10 RESULTS) |
| Primary metric/result | Success rate of policies trained with the imitation or task objectives disabled. | numeric claim only at cited anchor | p. 11 (10 RESULTS) |

- Numeric sentences retained from the body:
- **p. 10 / 10 RESULTS - extractive body cue:** 10.1 Tasks In addition to imitating reference motions, the policies can also adapt the motions as needed to satisfy additional task objectives, ACM Trans.
- **p. 11 / 10 RESULTS - extractive body cue:** Each policy is evaluated over 100 trials.
- **p. 4 / 4 BACKGROUND - extractive body cue:** The policy is queried at 30Hz, and target orientations for spherical joints are represented in axis-angle form, while targets for revolute joints are represented by ...
- **p. 6 / 4 BACKGROUND - extractive body cue:** Property Humanoid Atlas T-Rex Dragon Links 13 12 20 32 Total Mass (kg) 45 169.8 54.5 72.5 Height (m) 1.62 1.82 1.66 1.83 Degrees of ...
- **p. 7 / 4 BACKGROUND - extractive body cue:** All characters are modeled as articulated rigid bodies, with each link attached to its parent link via a 3 degree-of-freedom spherical joint, except for the ...
- **p. 7 / 4 BACKGROUND - extractive body cue:** 9 TASKS In addition to imitating a set of motion clips, the policies can be trained to perform a variety of tasks while preserving the ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | When the character falls, the composite policy activates the appropriate getup policy without requiring any manual scripting, as shown in the supplemental video. | p. 12 (10 RESULTS) |
| body limitation/failure cue | Table 6. Maximum forwards and sideways push each policy can tolerate before falling. Each push is applied to the character's pelvis for 0.2s. Skill ... | p. 13 (Figure/Table caption) |
| body limitation/failure cue | The learned policies are robust to significant external perturbation and generate plausible recovery behaviors. | p. 10 (10 RESULTS) |
| body limitation/failure cue | Fig. 1. Highly dynamic skills learned by imitating reference motion capture clips using our method, executed by physically simulated characters. Left: Humanoid character performing ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | To evaluate our framework's robustness to these discrepancies, we trained policies to perform similar skills with different character models, environments, and physics. | p. 12 (10 RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Reinforcement learning (RL) provides a promising approach for motion synthesis, whereby an agent learns to perform various skills through trial-and-error, thus reducing the need ... | p. 1 (1 INTRODUCTION) |
| Though humans are adept at performing a wide range of skills themselves, it can be difficult to articulate the internal strategies that underly such ... | p. 1 (1 INTRODUCTION) |
| 143:4 • Xue Bin Peng, Pieter Abbeel, Sergey Levine, and Michiel van de Panne of T steps. | p. 4 (4 BACKGROUND) |
| The advantages for the policy gradient will be computed using the generalized advantage estimator GAE(λ) [Schulman et al. | p. 4 (4 BACKGROUND) |
| The value function is updated using target values computed with TD(λ) [Sutton and Barto 1998]. | p. 5 (4 BACKGROUND) |
| The policy is updated using gradients computed from the surrogate objective, with advantages At computed using GAE(λ) [Schulman et al. | p. 5 (4 BACKGROUND) |
| In this setup, multiple policies are learned independently and, at runtime, their value functions are used to determine which policy should be activated. | p. 6 (4 BACKGROUND) |
| The task-specific behaviors are encoded into the task objective rG t . | p. 7 (4 BACKGROUND) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 12 / 10 RESULTS - extractive body cue:** When the character falls, the composite policy activates the appropriate getup policy without requiring any manual scripting, as shown in the supplemental video.
- **p. 13 / Figure/Table caption - extractive body cue:** Table 6. Maximum forwards and sideways push each policy can tolerate before falling. Each push is applied to the character's pelvis for 0.2s. Skill Forward ...
- **p. 10 / 10 RESULTS - extractive body cue:** The learned policies are robust to significant external perturbation and generate plausible recovery behaviors.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Highly dynamic skills learned by imitating reference motion capture clips using our method, executed by physically simulated characters. Left: Humanoid character performing a ...
- **p. 12 / 10 RESULTS - extractive body cue:** To evaluate our framework's robustness to these discrepancies, we trained policies to perform similar skills with different character models, environments, and physics.

- **PDF anchors reviewed:** datasets p. 10 (10 RESULTS), p. 10 (10 RESULTS), p. 11 (10 RESULTS), p. 11 (10 RESULTS), p. 12 (10 RESULTS), p. 12 (10 RESULTS), metrics p. 11 (10 RESULTS), p. 11 (10 RESULTS), p. 10 (10 RESULTS), p. 10 (10 RESULTS), p. 12 (10 RESULTS), p. 12 (10 RESULTS), baselines p. 11 (10 RESULTS), p. 12 (10 RESULTS), p. 10 (10 RESULTS), p. 11 (10 RESULTS), p. 12 (10 RESULTS), results p. 12 (10 RESULTS), p. 11 (10 RESULTS), p. 11 (10 RESULTS), p. 12 (10 RESULTS), p. 10 (10 RESULTS), p. 10 (10 RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
