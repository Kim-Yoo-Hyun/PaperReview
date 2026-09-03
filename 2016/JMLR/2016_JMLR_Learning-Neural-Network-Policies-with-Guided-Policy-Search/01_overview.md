# Learning Neural Network Policies with Guided Policy Search under Unknown Dynamics

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (40 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://jmlr.org/papers/v17/15-522.html.
> PDF retrieval source: https://jmlr.org/papers/volume17/15-522/15-522.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2016 / JMLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: Robotics, guided policy search, policy learning, manipulation
- Official paper: https://jmlr.org/papers/v17/15-522.html
- Full-text retrieval: https://jmlr.org/papers/volume17/15-522/15-522.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (40 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 rl 문제를 이해하기 위해 읽는다. 본문은 However, designing the perception and control software for autonomous operation remains a major challenge, even for basic tasks.를 문제로 두고, Our methods consists of two main components, which are illustrated in Figure 3.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Policy search methods can allow robots to learn control policies for a wide range of tasks, but practical applications of policy search often require hand-engineered ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we aim to answer the following question: does training the perception and control systems jointly end-toend provide better performance than training each ...
- **p. 1 / Abstract - extractive body cue:** To this end, we develop a method that can be used to learn policies that map raw image observations directly to torques at the robot's ...
- **p. 1 / Abstract - extractive body cue:** The policies are represented by deep convolutional neural networks (CNNs) with 92,000 parameters, and are trained using a guided policy search method, which transforms policy ...
- **p. 1 / Abstract - extractive body cue:** We evaluate our method on a range of real-world manipulation tasks that require close coordination between vision and control, such as screwing a cap onto ...
- **p. 1 / 1. Introduction - extractive body cue:** However, designing the perception and control software for autonomous operation remains a major challenge, even for basic tasks.
- **p. 2 / 1. Introduction - extractive body cue:** However, using deep neural networks for real-world sensorimotor policies, such as robotic controllers that map image pixels and joint angles to motor torques, presents a ...

## Core Idea

- **p. 5 / 3.2 Approach Summary - extractive body cue:** Our methods consists of two main components, which are illustrated in Figure 3.
- **p. 2 / 1. Introduction - extractive body cue:** In our method, the full state of the system is observable at training time, but not at test time.
- **p. 2 / 1. Introduction - extractive body cue:** Levine, Finn, Darrell, and Abbeel hanger cube hammer bottle Figure 1: Our method learns visuomotor policies that directly use camera image observations (left) to set ...
- **p. 5 / 3. Background and Overview - extractive body cue:** We also discuss a policy architecture suitable for end-to-end learning of vision and control, and a training setup that allows our method to be applied ...
- **p. 9 / 4.1 Algorithm Derivation - extractive body cue:** Minimization of the Lagrangian with respect to p(τ) and θ is done in alternating fashion: minimizing with respect to θ corresponds to supervised learning (making ...
- **p. 12 / 4.3 Supervised Policy Optimization - extractive body cue:** Since training complex neural networks requires a substantial number of samples, we found it beneficial to include sampled observations from previous iterations into the policy ...
- **p. 7 / 3.2 Approach Summary - extractive body cue:** We also initially train the guiding trajectory distributions pi(ut/xt) independently of the convolutional network until the trajectories achieve a basic level of competence at the ...
- **p. 6 / 3.2 Approach Summary - extractive body cue:** The guiding distributions are substantially easier to optimize than learning the policy parameters directly (e.g., using model-free reinforcement learning), because they use the full state ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The policy is trained to predict the actions along each trajectory from the observations ot, rather than the full state xt. | state 또는 observation, action, reward와 transition history | p. 8 (4. Guided Policy Search with BADMM), p. 12 (4.3 Supervised Policy Optimization) |
| State/latent | policy, trained, predict, actions, along, trajectory, observations, rather, full, state, Since, input | policy/value state와 action-selection variable | p. 8 (4. Guided Policy Search with BADMM), p. 12 (4.3 Supervised Policy Optimization), p. 12 (4.3 Supervised Policy Optimization) |
| Output/action | Since the input to µπ(ot) and Σπ(ot) is not the state xt, but only an observation ot, we can train the policy to directly use raw observations. | action policy와 induced trajectory | p. 12 (4.3 Supervised Policy Optimization), p. 12 (4.3 Supervised Policy Optimization), p. 5 (3.1 Definitions and Problem Formulation) |
| Objective/outcome | The goal of a task is given by a cost function ℓ(xt, ut), and the objective in policy search is to minimize the expectation Eπθ(τ)[PT t=1 ℓ(xt, ut)], which we will abbreviate ... | expected return, task success, stability와 sample efficiency | p. 5 (3.1 Definitions and Problem Formulation), p. 12 (4.3 Supervised Policy Optimization), p. 12 (4.3 Supervised Policy Optimization) |

## Main Claims and Actual Contribution

- **p. 5 / 3.2 Approach Summary - extractive body cue:** Our methods consists of two main components, which are illustrated in Figure 3.
- **p. 2 / 1. Introduction - extractive body cue:** In our method, the full state of the system is observable at training time, but not at test time.
- **p. 2 / 1. Introduction - extractive body cue:** Levine, Finn, Darrell, and Abbeel hanger cube hammer bottle Figure 1: Our method learns visuomotor policies that directly use camera image observations (left) to set ...
- **p. 5 / 3. Background and Overview - extractive body cue:** We also discuss a policy architecture suitable for end-to-end learning of vision and control, and a training setup that allows our method to be applied ...
- **p. 9 / 4.1 Algorithm Derivation - extractive body cue:** Minimization of the Lagrangian with respect to p(τ) and θ is done in alternating fashion: minimizing with respect to θ corresponds to supervised learning (making ...
- **p. 23 / 6.4 Deep Visuomotor Policy Evaluation - extractive body cue:** When provided with pose estimation features, the policy has more freedom in how it uses the visual information, and achieves somewhat higher success rates.
- **p. 21 / 6.3 Spatial Softmax CNN Architecture Evaluation - extractive body cue:** The results in Table 3 indicate that using the softmax and expectation operators improves pose estimation accuracy substantially.
- **p. 19 / 6.1 Simulated Comparisons to Prior Policy Search Methods - extractive body cue:** On swimming, our method achieved similar performance to the linear-Gaussian case, but since the neural network policy was stationary, the resulting gait was much smoother.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 23 (6.4 Deep Visuomotor Policy Evaluation), p. 21 (6.3 Spatial Softmax CNN Architecture Evaluation) |
| Embodiment/environment | Does our trajectory optimization algorithm work on a real robotic platform with unknown dynamics, for a range of different tasks? | hardware/simulator version and reset protocol | p. 16 (6. Experimental Evaluation), p. 19 (6.2 Learning Linear-Gaussian Controllers on a PR2 Robot) |
| Dataset/benchmark | Since performing trajectory optimization is a prerequisite for guided policy search to learn effective visuomotor policies, it is important to evaluate that our trajectory optimization can learn a wide variety of robotic ... | role, split, size and leakage | p. 16 (6. Experimental Evaluation), p. 19 (6.2 Learning Linear-Gaussian Controllers on a PR2 Robot), p. 19 (6.2 Learning Linear-Gaussian Controllers on a PR2 Robot), p. 16 (6.1 Simulated Comparisons to Prior Policy Search Methods) |
| Metric | We also did not extensively optimize the parameters of this network, such as filter size and number of channels, and investigating these design decisions further would be valuable to investigate in future ... | definition, denominator, direction and uncertainty | p. 21 (6.3 Spatial Softmax CNN Architecture Evaluation), p. 21 (6.2 Learning Linear-Gaussian Controllers on a PR2 Robot), p. 23 (6.4 Deep Visuomotor Policy Evaluation) |
| Baseline/ablation | On 3D insertion, it outperformed the iLQG baseline, which used a known model. | fair input/data/compute/action matching | p. 18 (6.1 Simulated Comparisons to Prior Policy Search Methods), p. 20 (6.2 Learning Linear-Gaussian Controllers on a PR2 Robot), p. 23 (6.4 Deep Visuomotor Policy Evaluation) |

## Explicit Limitations and Failure Boundary

- **p. 27 / 7. Discussion and Future Work - extractive body cue:** In many cases, this limitation is minor, and the only "instrumentation" required at training is to position the objects in the scene at consistent positions.
- **p. 27 / 7. Discussion and Future Work - extractive body cue:** A promising direction for addressing this limitation is to combine our method with unsupervised state-space learning, as proposed in several recent works, including our own ...
- **p. 23 / 6.4 Deep Visuomotor Policy Evaluation - extractive body cue:** This suggests that the failure of this baseline is not atypical, and that our visuomotor policies are learning visual features and control strategies that improve ...
- **p. 26 / 7. Discussion and Future Work - extractive body cue:** Although we demonstrate moderate generalization over variations in the scene, our current method does not generalize to dramatically different settings, especially when visual distractors occlude ...
- **p. 26 / 7. Discussion and Future Work - extractive body cue:** More practical alternatives that could be explored in future work include simultaneously training the policy on multiple robots, each of which is located in a ...
- **p. 18 / 6.1 Simulated Comparisons to Prior Policy Search Methods - extractive body cue:** Since the peg is 0.5 units long, distances above this amount correspond to controllers that cannot perform an insertion.
- **p. 19 / 6.2 Learning Linear-Gaussian Controllers on a PR2 Robot - extractive body cue:** PILCO cannot optimize neural network policies, and we could not obtain reasonable results with REPS.

## Why Read It

RL, IL, offline learning, and robot data의 rl 문제를 이해하기 위해 읽는다. 본문은 However, designing the perception and control software for autonomous operation remains a major challenge, even for basic tasks.를 문제로 두고, Our methods consists of two main components, which are illustrated in Figure 3.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 7 (3.2 Approach Summary), p. 3 (1. Introduction), p. 12 (4.3 Supervised Policy Optimization) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (40 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, designing the perception and control software for autonomous operation remains a major challenge, even for basic tasks. (p. 1, 1. Introduction).
- **Actual contribution:** In our method, the full state of the system is observable at training time, but not at test time. (p. 2, 1. Introduction).
- **Evaluation boundary:** The results in Table 3 indicate that using the softmax and expectation operators improves pose estimation accuracy substantially. (p. 21, 6.3 Spatial Softmax CNN Architecture Evaluation).
- **Explicit failure boundary:** The graph shows the average distance travelled on rollouts that did not fall, and shows that only our method was able to learn walking policies that succeeded consistently. (p. 19, 6.1 Simulated Comparisons to Prior Policy Search Methods).
