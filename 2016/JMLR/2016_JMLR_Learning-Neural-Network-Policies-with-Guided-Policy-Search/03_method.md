# Method - Learning Neural Network Policies with Guided Policy Search under Unknown Dynamics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (40 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://jmlr.org/papers/v17/15-522.html; PDF retrieval source: https://jmlr.org/papers/volume17/15-522/15-522.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 12 (4.3 Supervised Policy Optimization), p. 7 (3.2 Approach Summary), p. 6 (3.2 Approach Summary), p. 15 (5.2 Visuomotor Policy Training), p. 9 (4.1 Algorithm Derivation), p. 5 (3.2 Approach Summary)): Since training complex neural networks requires a substantial number of samples, we found it beneficial to include sampled observations from previous iterations into the policy optimization, evaluating the action µp ...

## Method Body Digest

- **p. 12 / 4.3 Supervised Policy Optimization - extractive body cue:** Since training complex neural networks requires a substantial number of samples, we found it beneficial to include sampled observations from previous iterations into the policy ...
- **p. 7 / 3.2 Approach Summary - extractive body cue:** We also initially train the guiding trajectory distributions pi(ut/xt) independently of the convolutional network until the trajectories achieve a basic level of competence at the ...
- **p. 6 / 3.2 Approach Summary - extractive body cue:** The guiding distributions are substantially easier to optimize than learning the policy parameters directly (e.g., using model-free reinforcement learning), because they use the full state ...
- **p. 15 / 5.2 Visuomotor Policy Training - extractive body cue:** Since the training set is still small (we use 1000 images collected from random arm motions), we initialize the filters in the first layer with ...
- **p. 9 / 4.1 Algorithm Derivation - extractive body cue:** Minimization of the Lagrangian with respect to p(τ) and θ is done in alternating fashion: minimizing with respect to θ corresponds to supervised learning (making ...
- **p. 5 / 3.2 Approach Summary - extractive body cue:** The second component is a trajectory-centric reinforcement learning (RL) algorithm that generates guiding distributions pi(ut/xt) that provide the supervision used to train the policy.
- **p. 7 / 3.2 Approach Summary - extractive body cue:** End-to-End Training of Deep Visuomotor Policies 3 channels 64 filters 5x5 conv ReLU conv1 conv2 5x5 conv ReLU 32 filters conv3 32 distributions spatial softmax ...
- **p. 5 / 3.1 Definitions and Problem Formulation - extractive body cue:** The goal of a task is given by a cost function ℓ(xt, ut), and the objective in policy search is to minimize the expectation Eπθ(τ)[PT ...

## Design Rationale

- **p. 5 / 3.2 Approach Summary - extractive body cue:** Our methods consists of two main components, which are illustrated in Figure 3.
- **p. 2 / 1. Introduction - extractive body cue:** In our method, the full state of the system is observable at training time, but not at test time.
- **p. 2 / 1. Introduction - extractive body cue:** Levine, Finn, Darrell, and Abbeel hanger cube hammer bottle Figure 1: Our method learns visuomotor policies that directly use camera image observations (left) to set ...

## Source Evidence Cues

- **p. 12 / 4.3 Supervised Policy Optimization - extractive body cue:** Since training complex neural networks requires a substantial number of samples, we found it beneficial to include sampled observations from previous iterations into the policy ...
- **p. 7 / 3.2 Approach Summary - extractive body cue:** We also initially train the guiding trajectory distributions pi(ut/xt) independently of the convolutional network until the trajectories achieve a basic level of competence at the ...
- **p. 6 / 3.2 Approach Summary - extractive body cue:** The guiding distributions are substantially easier to optimize than learning the policy parameters directly (e.g., using model-free reinforcement learning), because they use the full state ...
- **p. 15 / 5.2 Visuomotor Policy Training - extractive body cue:** Since the training set is still small (we use 1000 images collected from random arm motions), we initialize the filters in the first layer with ...
- **p. 9 / 4.1 Algorithm Derivation - extractive body cue:** Minimization of the Lagrangian with respect to p(τ) and θ is done in alternating fashion: minimizing with respect to θ corresponds to supervised learning (making ...
- **p. 5 / 3.2 Approach Summary - extractive body cue:** The second component is a trajectory-centric reinforcement learning (RL) algorithm that generates guiding distributions pi(ut/xt) that provide the supervision used to train the policy.
- **p. 7 / 3.2 Approach Summary - extractive body cue:** End-to-End Training of Deep Visuomotor Policies 3 channels 64 filters 5x5 conv ReLU conv1 conv2 5x5 conv ReLU 32 filters conv3 32 distributions spatial softmax ...
- **Detected method headings:** 3.2 Approach Summary (p. 5); 4. Guided Policy Search with BADMM (p. 7); 4.1 Algorithm Derivation (p. 8); 4.3 Supervised Policy Optimization (p. 12); 4.4 Comparison with Prior Guided Policy Search Methods (p. 12); 5.1 Visuomotor Policy Architecture (p. 13); 5.2 Visuomotor Policy Training (p. 14); 6.1 Simulated Comparisons to Prior Policy Search Methods (p. 16); 6.2 Learning Linear-Gaussian Controllers on a PR2 Robot (p. 19); 6.3 Spatial Softmax CNN Architecture Evaluation (p. 21); 6.4 Deep Visuomotor Policy Evaluation (p. 22)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Policy / value representation | state에서 action과 return estimate를 표현한다 | state/observation과 task context | actor, critic, value, Q 또는 sequence policy를 계산 | policy/value estimate | Since training complex neural networks requires a substantial number of samples, we found it beneficial to include sampled observations from previous iterations ... | p. 12 (4.3 Supervised Policy Optimization), p. 7 (3.2 Approach Summary) |
| Rollout / target construction | interaction에서 update target을 만든다 | state, action, reward, next state | return, advantage, TD target 또는 trajectory statistics를 구성 | training target | We also initially train the guiding trajectory distributions pi(ut/xt) independently of the convolutional network until the trajectories achieve a basic level of ... | p. 7 (3.2 Approach Summary), p. 6 (3.2 Approach Summary) |
| Policy / value update | 목표를 최적화해 다음 policy를 만든다 | target, replay/data와 parameters | gradient, trust region, entropy, replay 또는 constraint update를 수행 | updated policy/controller | The guiding distributions are substantially easier to optimize than learning the policy parameters directly (e.g., using model-free reinforcement learning), because they use ... | p. 6 (3.2 Approach Summary), p. 15 (5.2 Visuomotor Policy Training) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.1 Definitions and Problem Formulation - extractive body cue:** The goal of a task is given by a cost function ℓ(xt, ut), and the objective in policy search is to minimize the expectation Eπθ(τ)[PT ...
- **p. 12 / 4.3 Supervised Policy Optimization - extractive body cue:** Since the policy parameters θ participate only in the constraints of the optimization problem in Equation (1), optimizing the policy corresponds to minimizing the KL-divergence ...
- **p. 12 / 4.3 Supervised Policy Optimization - extractive body cue:** At convergence, when the policy πθ(ut/ot) takes the same actions as pi(ut/xt), their Q-functions are equal, and the supervised policy objective becomes equivalent to the ...
- **p. 8 / 4.1 Algorithm Derivation - extractive body cue:** Policy search methods minimize the expected cost Eπθ[ℓ(τ)], where τ = {x1, u1, . . . , xT , uT } is a trajectory, and ...
- **p. 8 / 4.1 Algorithm Derivation - extractive body cue:** We begin by rewriting the expected cost minimization as a constrained problem: min p,πθ Ep[ℓ(τ)] s.t. p(ut/xt) = πθ(ut/xt) ∀xt, ut, t, (1) where we ...
- **p. 11 / 4.2 Trajectory Optimization under Unknown Dynamics - extractive body cue:** Note that the trajectory optimization cost function Lp(p, θ) also depends on the policy πθ(ut/xt), while we only have access to πθ(ut/ot).
- **Formal bridge:** s_t/o_t -> a_t sampled or selected by πθ -> expected return / constrained return -> task return, success and safe execution.
- **Equation/algorithm anchors:** p. 12 (4.3 Supervised Policy Optimization), p. 12 (4.3 Supervised Policy Optimization), p. 11 (4.2 Trajectory Optimization under Unknown Dynamics), p. 5 (3.1 Definitions and Problem Formulation), p. 8 (4.1 Algorithm Derivation), p. 9 (4.1 Algorithm Derivation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | policy, trained, predict, actions, along, trajectory, observations, rather, full, state, Since, input, only, observation | state 또는 observation, action, reward와 transition history | body cue; exact tensor/frame verify |
| State/latent | policy, trained, predict, actions, along, trajectory, observations, rather, full, state | policy/value state와 action-selection variable | body cue; notation verify |
| Action/output | methods, consists, main, components, illustrated, Figure, full, state, system, observable | action policy와 induced trajectory | body cue; unit/decoder verify |
| Objective/constraint | goal, task, given, cost, function, objective, policy, search, minimize, expectation | expected return / constrained return | equation anchor required |

## Observation–State–Action Interface

- **p. 8 / 4. Guided Policy Search with BADMM - extractive body cue:** The policy is trained to predict the actions along each trajectory from the observations ot, rather than the full state xt.
- **p. 12 / 4.3 Supervised Policy Optimization - extractive body cue:** Since the input to µπ(ot) and Σπ(ot) is not the state xt, but only an observation ot, we can train the policy to directly use ...
- **p. 12 / 4.3 Supervised Policy Optimization - extractive body cue:** Since training complex neural networks requires a substantial number of samples, we found it beneficial to include sampled observations from previous iterations into the policy ...
- **p. 5 / 3.1 Definitions and Problem Formulation - extractive body cue:** In policy search, the goal is to learn a policy πθ(ut/ot) that allows an agent to choose actions ut in response to observations ot to ...
- **p. 6 / 3.2 Approach Summary - extractive body cue:** The guiding distributions are substantially easier to optimize than learning the policy parameters directly (e.g., using model-free reinforcement learning), because they use the full state ...
- **p. 5 / 3.1 Definitions and Problem Formulation - extractive body cue:** The system is defined by states xt, actions ut, and observations ot.
- **p. 1 / 1. Introduction - extractive body cue:** However, policies learned using such methods often rely on a number of hand-engineered components for perception and control, so as to present the policy with ...
- **Normalized interface:** observation=state 또는 observation, action, reward와 transition history; state=policy/value state와 action-selection variable; output/action=action policy와 induced trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | rollout/return horizon과 episode termination; exact n-step/discount는 exact value was not selected from the PDF body. | Images in the lowerright show the last time step for each system at several iterations of our method, with red lines indicating ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 environment step이 분리되며 deployment control rate는 별도 contract다. | The neural network policies used one hidden layer and soft rectifier nonlinearities of the form a = log(1+exp(z)). | Hz/fps, inference time and control rate |
| Memory | replay/rollout buffer와 actor/critic parameters; recurrent history 여부 확인 필요. | CNNs have a long history in computer vision and deep learning (Fukushima, 1980; LeCun et al., 1989; Schmidhuber, 2015), and have recently ... | window and reset |
| Compute | environment interaction, value/policy update와 batch size가 비용을 결정한다. | Our method used 5 rollouts with the Gaussian mixture model prior, and 20 without. | hardware, batch and throughput |

## Training vs Inference

- **p. 12 / 4.3 Supervised Policy Optimization - extractive body cue:** Since training complex neural networks requires a substantial number of samples, we found it beneficial to include sampled observations from previous iterations into the policy ...
- **p. 7 / 3.2 Approach Summary - extractive body cue:** We also initially train the guiding trajectory distributions pi(ut/xt) independently of the convolutional network until the trajectories achieve a basic level of competence at the ...
- **p. 15 / 5.2 Visuomotor Policy Training - extractive body cue:** Since the training set is still small (we use 1000 images collected from random arm motions), we initialize the filters in the first layer with ...
- **p. 5 / 3.2 Approach Summary - extractive body cue:** The second component is a trajectory-centric reinforcement learning (RL) algorithm that generates guiding distributions pi(ut/xt) that provide the supervision used to train the policy.
- **p. 7 / 3.2 Approach Summary - extractive body cue:** End-to-End Training of Deep Visuomotor Policies 3 channels 64 filters 5x5 conv ReLU conv1 conv2 5x5 conv ReLU 32 filters conv3 32 distributions spatial softmax ...
- **p. 26 / 6.6 Computational Performance and Sample Efficiency - extractive body cue:** Only about 15 minutes of the training time consisted of executing trials on the robot.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Since, training, complex, neural, networks, requires, substantial, number, samples, found, beneficial, include, sampled, observations, previous, iterations, policy, optimization, evaluating, action.
- **Relevant PDF headings:** 3.2 Approach Summary (p. 5); 4. Guided Policy Search with BADMM (p. 7); 4.1 Algorithm Derivation (p. 8); 4.3 Supervised Policy Optimization (p. 12); 4.4 Comparison with Prior Guided Policy Search Methods (p. 12); 5.1 Visuomotor Policy Architecture (p. 13); 5.2 Visuomotor Policy Training (p. 14); 6.1 Simulated Comparisons to Prior Policy Search Methods (p. 16); 6.2 Learning Linear-Gaussian Controllers on a PR2 Robot (p. 19); 6.3 Spatial Softmax CNN Architecture Evaluation (p. 21); 6.4 Deep Visuomotor Policy Evaluation (p. 22).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Policy / value representation | Does our trajectory optimization algorithm work on a real robotic platform with unknown dynamics, for a range of different tasks? | p. 16 (6. Experimental Evaluation), p. 19 (6.2 Learning Linear-Gaussian Controllers on a PR2 Robot) |
| Rollout / target construction | On 3D insertion, it outperformed the iLQG baseline, which used a known model. | p. 18 (6.1 Simulated Comparisons to Prior Policy Search Methods), p. 20 (6.2 Learning Linear-Gaussian Controllers on a PR2 Robot) |
| Policy / value update | When provided with pose estimation features, the policy has more freedom in how it uses the visual information, and achieves somewhat higher ... | p. 23 (6.4 Deep Visuomotor Policy Evaluation), p. 21 (6.3 Spatial Softmax CNN Architecture Evaluation) |

## Failure and Ablation Link

- **p. 17 / 6.1 Simulated Comparisons to Prior Policy Search Methods - extractive body cue:** Our method used 5 rollouts with the Gaussian mixture model prior, and 20 without.
- **p. 17 / 6.1 Simulated Comparisons to Prior Policy Search Methods - extractive body cue:** We compare to a variant of REPS that also fits linear dynamics to generate 500 pseudo-samples (Lioutikov et al., 2014), which we label "REPS (20 ...
- **p. 19 / 6.1 Simulated Comparisons to Prior Policy Search Methods - extractive body cue:** In practice, we found the performance of these methods to be very similar, though the BADMM variant was substantially faster and easier to implement.
- **p. 19 / 6.1 Simulated Comparisons to Prior Policy Search Methods - extractive body cue:** On peg insertion, the neural network was trained to insert the peg without precise knowledge of the position of the hole, resulting in a partially ...
- **p. 20 / 6.2 Learning Linear-Gaussian Controllers on a PR2 Robot - extractive body cue:** Robustness increased slightly when more noise was injected during training, but even controllers trained without noise exhibited considerable robustness, since the linear-Gaussian controllers themselves add ...
- **p. 21 / 6.3 Spatial Softmax CNN Architecture Evaluation - extractive body cue:** This is a reasonable proxy for evaluating how well the network can overcome two major challenges in visuomotor learning: the ability to handle relatively small ...
- **p. 23 / 6.4 Deep Visuomotor Policy Evaluation - extractive body cue:** This variant achieves poor performance.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 12 (4.3 Supervised Policy Optimization), p. 7 (3.2 Approach Summary), p. 6 (3.2 Approach Summary), p. 15 (5.2 Visuomotor Policy Training), p. 9 (4.1 Algorithm Derivation), p. 5 (3.2 Approach Summary), objective p. 5 (3.1 Definitions and Problem Formulation), p. 12 (4.3 Supervised Policy Optimization), p. 12 (4.3 Supervised Policy Optimization), p. 8 (4.1 Algorithm Derivation), p. 8 (4.1 Algorithm Derivation), p. 11 (4.2 Trajectory Optimization under Unknown Dynamics), temporal p. 17 (6.1 Simulated Comparisons to Prior Policy Search Methods), p. 16 (6.1 Simulated Comparisons to Prior Policy Search Methods), p. 17 (6.1 Simulated Comparisons to Prior Policy Search Methods), p. 18 (6.1 Simulated Comparisons to Prior Policy Search Methods), p. 19 (6.1 Simulated Comparisons to Prior Policy Search Methods), p. 3 (2. Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (40 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Since training complex neural networks requires a substantial number of samples, we found it beneficial to include sampled observations from previous iterations into the policy optimization, evaluating the action µp ... (p. 12, 4.3 Supervised Policy Optimization).
- **Objective/update evidence:** This constrained optimization is performed in the "inner loop" of the optimization described in the previous section, and the KL-divergence constraint DKL(p(τ)∥ˆp(τ)) ≤ϵ imposes a step size on the trajectory ... (p. 11, 4.2 Trajectory Optimization under Unknown Dynamics).
- **Temporal/runtime evidence:** Images in the lowerright show the last time step for each system at several iterations of our method, with red lines indicating end effector trajectories. (p. 17, 6.1 Simulated Comparisons to Prior Policy Search Methods).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
