# Insights — Learning to Walk from Three Minutes of Real-World Data with Semi-structured Dynamics Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=evCXwlCMIi; PDF retrieval source: https://arxiv.org/pdf/2410.09163. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 6 / 1 Introduction - extractive body cue:** This, when combined with the accuracy of our predictions over long-horizons (Section 4.2) provides insight into why our approach enables such effective policy optimization [38].
- **p. 3 / 1 Introduction - extractive body cue:** The space of observations Ωconsists of the states that can be measured, and the observation distribution O(·/st, at, et) provides (noisy) estimates of the states ...
- **p. 4 / 1 Introduction - extractive body cue:** 3 Semi-structured Reinforcement Learning A high-level overview of our method is presented in Fig.
- **p. 5 / 1 Introduction - extractive body cue:** 3.4 Policy Optimization Finally, we introduce the Semi-Structured Reinforcement Learning (SSRL) in Algorithm 2.
- **p. 7 / 1 Introduction - extractive body cue:** Right-Prediction error for 20-step synthetic rollouts in an unseen environment showcases our method's superior ability to generalize.
- **p. 14 / A.3 Control Architecture - extractive body cue:** The desired joint angles are sent to the joint level PD controllers, where the desired torque outputs are: τt = Kp(qdes -qj) -Kp ˙qj, (11) ...
- **p. 14 / A.3 Control Architecture - extractive body cue:** Referring to the action space definition Table 2, the policy takes in the current observation and a history of observations and outputs offsets to foot ...
- **Contribution anchor:** p. 6 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 7 (1 Introduction), p. 14 (A.3 Control Architecture)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** However, in practice, the black-box neural network models favored in the ∗These ...
- **p. 6 / 1 Introduction - extractive body cue:** Predictions from semi-structured dynamics models demonstrate greater accuracy and improved generalization beyond training data compared to black-box models.
- **p. 7 / 1 Introduction - extractive body cue:** To assess generalization (Hypothesis 3), we train our semi-structured models and the black-box models from scratch over 3 minutes of saved simulated data using 1- ...
- **p. 1 / 1 Introduction - extractive body cue:** Effective robotic agents must leverage complex interactions between the robot and its environment, which are difficult to model using first principles.
- **p. 2 / 1 Introduction - extractive body cue:** Currently, both paradigms are too inefficient and unreliable to make learning new behaviors in the real world practical for many applications.
- **p. 8 / 5 Related Work - extractive body cue:** However there are several key limitations.
- **p. 8 / 5 Related Work - extractive body cue:** 6 Limitations This paper presents a novel framework for model-based reinforcement learning, which leverages physics-informed, semi-structured dynamics models to enable highly sample-efficient policy learning in ...
- **Boundary to test:** However there are several key limitations.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | This, when combined with the accuracy of our predictions over long-horizons (Section 4.2) provides insight into why our approach enables such effective policy optimization [38]. | p. 6 (1 Introduction), p. 3 (1 Introduction) |
| Reported outcome | Figure 12: Simulated benchmark results. Better performance is achieved when using our semi- structured dynamics models and a multi-step loss. Plots show the mean and standard deviation for episodic rewards. 18 | p. 18 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Failure/limitation | However there are several key limitations. | p. 8 (5 Related Work), p. 8 (5 Related Work) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, terrain/perception observation과 velocity command → body/contact state, foothold 또는 behavior mode → joint target, torque, footstep 또는 locomotion action`.
- 이 논문의 재사용 가능한 지점은 Algorithm 1 Auto-Regressive State Predictions 1: Inputs hallucination buffer Dmodel, models {ˆpi ψi}, policy πθ, start state s0, start history h0 2: for t = 0 . . . k -1 do ...를 Referring to the action space definition Table 2, the policy takes in the current observation and a history of observations and outputs offsets to foot positions and a nominal height for the ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 body/contact state, foothold 또는 behavior mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 However there are several key limitations.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: This, when combined with the accuracy of our predictions over long-horizons (Section 4.2) provides insight into why our approach enables such effective policy optimization [38].
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, locomotion, model-based reinforcement learning, real-world learning`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** However there are several key limitations.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: dataset/benchmark role not recovered.
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 5: Left-SSRL achieves better policy performance compared to a baseline using black-box models. Right-Prediction error for 20-step synthetic rollouts in an unseen environment showcases our method's supe- rior ability to generalize ....
4. Report the body metric and its denominator/aggregation: Figure 7: Prediction error for 20-step synthetic rollouts using our semi-structured dynamics models and the black-box models where the best results from the 1- or 4- step losses are presented. Pre- diction ....
5. Re-run the body-reported ablation/failure condition: Figure 9: Training performance when removing the noise estimators and removing both the noise estimators and ensemble. B.5 Additional Simulated Terrain Experiments To further demonstrate the versatility of our approach on varying ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 14 (A.3 Control Architecture), p. 14 (A.3 Control Architecture), p. 13 (A.1 Observation and Action Spaces); the primary result is directionally consistent at p. 18 (Figure/Table caption), p. 7 (Figure/Table caption), p. 2 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 when, combined, accuracy mechanism이 Figure 5: Left-SSRL achieves better policy performance compared to a baseline using black-box models. Right-Prediction error ... 대비 Figure 7: Prediction error for 20-step synthetic rollouts using our semi-structured dynamics models and the black-box models where ...을 개선하고, However there are several key limitations. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
