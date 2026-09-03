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

- **Paper-specific interface:** The system is defined by states xt, actions ut, and observations ot. (p. 5, 3.1 Definitions and Problem Formulation).
- **Paper-specific mechanism:** In our method, the full state of the system is observable at training time, but not at test time. (p. 2, 1. Introduction).
- **Evidence boundary:** the reported outcome is The results in Table 3 indicate that using the softmax and expectation operators improves pose estimation accuracy substantially. (p. 21, 6.3 Spatial Softmax CNN Architecture Evaluation); the relevant task/metric cue is To evaluate their robustness to errors in the specified target position, we conducted experiments on the lego block and ring tasks where the target object (the lower block and the ... (p. 20, 6.2 Learning Linear-Gaussian Controllers on a PR2 Robot). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** The graph shows the average distance travelled on rollouts that did not fall, and shows that only our method was able to learn walking policies that succeeded consistently. (p. 19, 6.1 Simulated Comparisons to Prior Policy Search Methods).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `RL, IL, offline learning, and robot data`; tags: `Robotics, guided policy search, policy learning, manipulation`.
- **Reading predecessor in the generated track queue:** A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Generative Adversarial Imitation Learning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In many cases, this limitation is minor, and the only "instrumentation" required at training is to position the objects in the scene at consistent positions.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: The system is defined by states xt, actions ut, and observations ot. (p. 5, 3.1 Definitions and Problem Formulation); preserve the objective/update rule: This constrained optimization is performed in the "inner loop" of the optimization described in the previous section, and the KL-divergence constraint DKL(p(τ)∥ˆp(τ)) ≤ϵ imposes a step size on the trajectory ... (p. 11, 4.2 Trajectory Optimization under Unknown Dynamics).
2. Use the paper-reported task/data/environment cue: Does our trajectory optimization algorithm work on a real robotic platform with unknown dynamics, for a range of different tasks? (p. 16, 6. Experimental Evaluation).
3. Compare against the reported or matched baseline: On 3D insertion, it outperformed the iLQG baseline, which used a known model. (p. 18, 6.1 Simulated Comparisons to Prior Policy Search Methods).
4. Report the body metric with its denominator and aggregation: To evaluate their robustness to errors in the specified target position, we conducted experiments on the lego block and ring tasks where the target object (the lower block and the ... (p. 20, 6.2 Learning Linear-Gaussian Controllers on a PR2 Robot).
5. Re-run the reported ablation or stress/failure condition: Our method used 5 rollouts with the Gaussian mixture model prior, and 20 without. (p. 17, 6.1 Simulated Comparisons to Prior Policy Search Methods); if none is reported, design one around: The graph shows the average distance travelled on rollouts that did not fall, and shows that only our method was able to learn walking policies that succeeded consistently. (p. 19, 6.1 Simulated Comparisons to Prior Policy Search Methods).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1. Introduction), p. 5 (3.2 Approach Summary), match the reported outcome at p. 21 (6.3 Spatial Softmax CNN Architecture Evaluation), p. 21 (6.2 Learning Linear-Gaussian Controllers on a PR2 Robot), p. 21 (6.3 Spatial Softmax CNN Architecture Evaluation), and measure the boundary at p. 19 (6.1 Simulated Comparisons to Prior Policy Search Methods), p. 23 (6.4 Deep Visuomotor Policy Evaluation).

## Falsifiable research question

Under the paper's stated interface (The system is defined by states xt, actions ut, and observations ot.), does the paper-specific mechanism (In our method, the full state of the system is observable at training time, but not at test time.) retain the reported evaluation outcome (To evaluate their robustness to errors in the specified target position, we conducted experiments on the lego block ...) when tested against the paper's strongest explicit boundary (The graph shows the average distance travelled on rollouts that did not fall, and shows that only our ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (To evaluate their robustness to errors in the specified target position, we conducted experiments on the lego block ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (40 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In our method, the full state of the system is observable at training time, but not at test time. (p. 2, 1. Introduction).
- **Paper-supported outcome:** The results in Table 3 indicate that using the softmax and expectation operators improves pose estimation accuracy substantially. (p. 21, 6.3 Spatial Softmax CNN Architecture Evaluation).
- **Strongest explicit boundary:** The graph shows the average distance travelled on rollouts that did not fall, and shows that only our method was able to learn walking policies that succeeded consistently. (p. 19, 6.1 Simulated Comparisons to Prior Policy Search Methods).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
