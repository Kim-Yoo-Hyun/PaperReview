# DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1804.02717.
> PDF retrieval source: https://arxiv.org/pdf/1804.02717. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2018 / TOG / SIGGRAPH
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, humanoid, motion imitation, Reinforcement Learning, physics-based control
- Official paper: https://arxiv.org/abs/1804.02717
- Full-text retrieval: https://arxiv.org/pdf/1804.02717
- Code/Project: https://github.com/xbpeng/DeepMimic
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 Authoring motions for simulated characters remains notoriously difficult, and current interfaces still cannot provide users with an effective means of eliciting the desired behaviours from simulated characters.를 문제로 두고, Although our framework consists of individual components that have been known for some time, the particular combination of these components in the context of data-driven and physics-based character animation is novel and, ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 INTRODUCTION - extractive body cue:** Physics-based simulation of passive phenomena, such as cloth and fluids, has become nearly ubiquitous in industry.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, the adoption of physically simulated characters has been more modest.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Modeling the motion of humans and animals remains a challenging problem, and currently, few methods exist that can simulate the diversity of behaviors exhibited in ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Among the enduring challenges in this domain are generalization and directability.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Methods that rely on manually designed controllers have produced compelling results, but their ability to generalize to new skills and new situations is limited by ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Authoring motions for simulated characters remains notoriously difficult, and current interfaces still cannot provide users with an effective means of eliciting the desired behaviours from ...
- **p. 5 / 4 BACKGROUND - extractive body cue:** One of the persistent challenges in RL is the problem of exploration.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Although our framework consists of individual components that have been known for some time, the particular combination of these components in the context of data-driven ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In our ablation studies, we identify two specific components of our method, reference state initialization and early termination, that are critical for achieving highly dynamic ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Our method handles keyframed motions, highly-dynamic actions such as motion-captured flips and spins, and retargeted motions.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Highly dynamic skills learned by imitating reference motion capture clips using our method, executed by physically simulated characters.
- **p. 4 / 4 BACKGROUND - extractive body cue:** The value function is modeled by a similar network, with exception of the output layer, which consists of a single linear unit.
- **p. 6 / 4 BACKGROUND - extractive body cue:** Property Humanoid Atlas T-Rex Dragon Links 13 12 20 32 Total Mass (kg) 45 169.8 54.5 72.5 Height (m) 1.62 1.82 1.66 1.83 Degrees of ...
- **p. 4 / 4 BACKGROUND - extractive body cue:** The action distribution is modeled as a Gaussian, with a state dependent mean µ(s) specified by the network, and a fixed diagonal covariance matrix Σ ...
- **p. 4 / 4 BACKGROUND - extractive body cue:** The resulting features are then concatenated with the input state s and goal д, and processed by a similar fully-connected network as the one used ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 5.2 Network Each policy π is represented by a neural network that maps a given state s and goal д to a distribution over action π(a/s,д). | proprioception, reference pose/motion, visual or language command | p. 4 (4 BACKGROUND), p. 5 (4 BACKGROUND) |
| State/latent | Network, policy, represented, neural, maps, given, state, goal, distribution, over, action, Training | whole-body pose, balance/contact state와 skill/mode | p. 4 (4 BACKGROUND), p. 5 (4 BACKGROUND), p. 3 (4 BACKGROUND) |
| Output/action | Training proceeds episodically, where at the start of each episode, an initial state s0 is sampled uniformly from the reference motion (section 6.1), and rollouts are generated by sampling actions from the ... | joint/whole-body action, motion target 또는 task trajectory | p. 5 (4 BACKGROUND), p. 3 (4 BACKGROUND), p. 4 (4 BACKGROUND) |
| Objective/outcome | The policy is updated using gradients computed from the surrogate objective, with advantages At computed using GAE(λ) [Schulman et al. | tracking, balance, skill/task success와 recovery | p. 5 (4 BACKGROUND), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Although our framework consists of individual components that have been known for some time, the particular combination of these components in the context of data-driven ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In our ablation studies, we identify two specific components of our method, reference state initialization and early termination, that are critical for achieving highly dynamic ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Our method handles keyframed motions, highly-dynamic actions such as motion-captured flips and spins, and retargeted motions.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Highly dynamic skills learned by imitating reference motion capture clips using our method, executed by physically simulated characters.
- **p. 4 / 4 BACKGROUND - extractive body cue:** The value function is modeled by a similar network, with exception of the output layer, which consists of a single linear unit.
- **p. 12 / 10 RESULTS - extractive body cue:** The performance achieved by the Atlas policies are comparable to those achieved by the humanoid.
- **p. 11 / 10 RESULTS - extractive body cue:** Success rate of policies trained with the imitation or task objectives disabled.
- **p. 11 / 10 RESULTS - extractive body cue:** Similarly, for the strike task, the policy trained with both objectives successfully hits 99% of the targets, while the policy trained only to imitate the ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 12 (10 RESULTS), p. 11 (10 RESULTS) |
| Embodiment/environment | Each environment is denoted by "Character: Skill - Task". | hardware/simulator version and reset protocol | p. 10 (10 RESULTS), p. 10 (10 RESULTS) |
| Dataset/benchmark | Success rate of policies trained with the imitation or task objectives disabled. | role, split, size and leakage | p. 10 (10 RESULTS), p. 10 (10 RESULTS), p. 11 (10 RESULTS), p. 11 (10 RESULTS) |
| Metric | Success rate of policies trained with the imitation or task objectives disabled. | definition, denominator, direction and uncertainty | p. 11 (10 RESULTS), p. 11 (10 RESULTS), p. 10 (10 RESULTS) |
| Baseline/ablation | To investigate the extent to which the motions are adapted for a particular task, we compared the performance of policies trained to optimize both the imitation objective rI and the task objective ... | fair input/data/compute/action matching | p. 11 (10 RESULTS), p. 12 (10 RESULTS), p. 10 (10 RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 12 / 10 RESULTS - extractive body cue:** When the character falls, the composite policy activates the appropriate getup policy without requiring any manual scripting, as shown in the supplemental video.
- **p. 13 / Figure/Table caption - extractive body cue:** Table 6. Maximum forwards and sideways push each policy can tolerate before falling. Each push is applied to the character's pelvis for 0.2s. Skill Forward ...
- **p. 10 / 10 RESULTS - extractive body cue:** The learned policies are robust to significant external perturbation and generate plausible recovery behaviors.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Highly dynamic skills learned by imitating reference motion capture clips using our method, executed by physically simulated characters. Left: Humanoid character performing a ...
- **p. 12 / 10 RESULTS - extractive body cue:** To evaluate our framework's robustness to these discrepancies, we trained policies to perform similar skills with different character models, environments, and physics.

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 Authoring motions for simulated characters remains notoriously difficult, and current interfaces still cannot provide users with an effective means of eliciting the desired behaviours from simulated characters.를 문제로 두고, Although our framework consists of individual components that have been known for some time, the particular combination of these components in the context of data-driven and physics-based character animation is novel and, ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 5 (4 BACKGROUND), p. 5 (4 BACKGROUND), p. 6 (4 BACKGROUND), p. 6 (4 BACKGROUND) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Authoring motions for simulated characters remains notoriously difficult, and current interfaces still cannot provide users with an effective means of eliciting the desired behaviours from simulated characters. (p. 1, 1 INTRODUCTION).
- **Actual contribution:** Although our framework consists of individual components that have been known for some time, the particular combination of these components in the context of data-driven and physics-based character animation is ... (p. 2, 1 INTRODUCTION).
- **Evaluation boundary:** Similarly, for the strike task, the policy trained with both objectives successfully hits 99% of the targets, while the policy trained only to imitate the reference motion has a success ... (p. 11, 10 RESULTS).
- **Explicit failure boundary:** Since the motion is highly sensitive to the initial conditions at takeoff, many strategies will result in failure. (p. 6, 4 BACKGROUND).
