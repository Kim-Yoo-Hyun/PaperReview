# Insights — Learning Neural Network Policies with Guided Policy Search under Unknown Dynamics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (40 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://jmlr.org/papers/v17/15-522.html; PDF retrieval source: https://jmlr.org/papers/volume17/15-522/15-522.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 5 / 3.2 Approach Summary - extractive body cue:** Our methods consists of two main components, which are illustrated in Figure 3.
- **p. 2 / 1. Introduction - extractive body cue:** In our method, the full state of the system is observable at training time, but not at test time.
- **p. 2 / 1. Introduction - extractive body cue:** Levine, Finn, Darrell, and Abbeel hanger cube hammer bottle Figure 1: Our method learns visuomotor policies that directly use camera image observations (left) to set ...
- **p. 5 / 3. Background and Overview - extractive body cue:** We also discuss a policy architecture suitable for end-to-end learning of vision and control, and a training setup that allows our method to be applied ...
- **p. 9 / 4.1 Algorithm Derivation - extractive body cue:** Minimization of the Lagrangian with respect to p(τ) and θ is done in alternating fashion: minimizing with respect to θ corresponds to supervised learning (making ...
- **p. 12 / 4.3 Supervised Policy Optimization - extractive body cue:** Since training complex neural networks requires a substantial number of samples, we found it beneficial to include sampled observations from previous iterations into the policy ...
- **p. 7 / 3.2 Approach Summary - extractive body cue:** We also initially train the guiding trajectory distributions pi(ut/xt) independently of the convolutional network until the trajectories achieve a basic level of competence at the ...
- **Contribution anchor:** p. 5 (3.2 Approach Summary), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3. Background and Overview), p. 9 (4.1 Algorithm Derivation), p. 12 (4.3 Supervised Policy Optimization)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** However, designing the perception and control software for autonomous operation remains a major challenge, even for basic tasks.
- **p. 2 / 1. Introduction - extractive body cue:** However, using deep neural networks for real-world sensorimotor policies, such as robotic controllers that map image pixels and joint angles to motor torques, presents a ...
- **p. 2 / 1. Introduction - extractive body cue:** We address these challenges by developing a guided policy search algorithm for sensorimotor deep learning, as well as a novel CNN architecture designed for robotic ...
- **p. 7 / 3.2 Approach Summary - extractive body cue:** Our network has 7 layers and around 92,000 parameters, which presents a major challenge for standard policy search methods (Deisenroth et al., 2013). initial controllers ...
- **p. 3 / 1. Introduction - extractive body cue:** End-to-End Training of Deep Visuomotor Policies number of prior methods when training high-dimensional neural network policies.
- **p. 27 / 7. Discussion and Future Work - extractive body cue:** In many cases, this limitation is minor, and the only "instrumentation" required at training is to position the objects in the scene at consistent positions.
- **p. 27 / 7. Discussion and Future Work - extractive body cue:** A promising direction for addressing this limitation is to combine our method with unsupervised state-space learning, as proposed in several recent works, including our own ...
- **Boundary to test:** In many cases, this limitation is minor, and the only "instrumentation" required at training is to position the objects in the scene at consistent positions.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our methods consists of two main components, which are illustrated in Figure 3. | p. 5 (3.2 Approach Summary), p. 2 (1. Introduction) |
| Reported outcome | When provided with pose estimation features, the policy has more freedom in how it uses the visual information, and achieves somewhat higher success rates. | p. 23 (6.4 Deep Visuomotor Policy Evaluation), p. 21 (6.3 Spatial Softmax CNN Architecture Evaluation) |
| Failure/limitation | In many cases, this limitation is minor, and the only "instrumentation" required at training is to position the objects in the scene at consistent positions. | p. 27 (7. Discussion and Future Work), p. 27 (7. Discussion and Future Work) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `state 또는 observation, action, reward와 transition history → policy/value state와 action-selection variable → action policy와 induced trajectory`.
- 이 논문의 재사용 가능한 지점은 The policy is trained to predict the actions along each trajectory from the observations ot, rather than the full state xt.를 Since the input to µπ(ot) and Σπ(ot) is not the state xt, but only an observation ot, we can train the policy to directly use raw observations.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 policy/value state와 action-selection variable가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 In many cases, this limitation is minor, and the only "instrumentation" required at training is to position the objects in the scene at consistent positions.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our methods consists of two main components, which are illustrated in Figure 3.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `RL, IL, offline learning, and robot data`; tags: `Robotics, guided policy search, policy learning, manipulation`.
- **Reading predecessor in the generated track queue:** A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Generative Adversarial Imitation Learning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In many cases, this limitation is minor, and the only "instrumentation" required at training is to position the objects in the scene at consistent positions.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Does our trajectory optimization algorithm work on a real robotic platform with unknown dynamics, for a range of different tasks?.
3. Compare against the body-reported baseline or a matched simpler baseline: On 3D insertion, it outperformed the iLQG baseline, which used a known model..
4. Report the body metric and its denominator/aggregation: We also did not extensively optimize the parameters of this network, such as filter size and number of channels, and investigating these design decisions further would be valuable to investigate in future ....
5. Re-run the body-reported ablation/failure condition: Our method used 5 rollouts with the Gaussian mixture model prior, and 20 without..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 12 (4.3 Supervised Policy Optimization), p. 7 (3.2 Approach Summary), p. 6 (3.2 Approach Summary); the primary result is directionally consistent at p. 23 (6.4 Deep Visuomotor Policy Evaluation), p. 21 (6.3 Spatial Softmax CNN Architecture Evaluation), p. 19 (6.1 Simulated Comparisons to Prior Policy Search Methods); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 methods, consists, main mechanism이 On 3D insertion, it outperformed the iLQG baseline, which used a known model. 대비 We also did not extensively optimize the parameters of this network, such as filter size and number of ...을 개선하고, In many cases, this limitation is minor, and the only "instrumentation" required at training is to ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
