# Insights — Resilient Legged Local Navigation: Learning to Traverse with Compromised Perception End-to-End

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2310.03581; PDF retrieval source: https://arxiv.org/pdf/2310.03581. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose to incorporate locomotion-level observations into navigation, contrasting existing methods that typically decouple navigation from locomotion.
- **p. 2 / III. METHOD - extractive body cue:** Overview The objective of our method is to guide the robot to a local target within the given time.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, such manually-designed rules cannot scale well to diverse situations.
- **p. 3 / III. METHOD - extractive body cue:** Actor Critic Low-Level Exteroception Proprioception Previous Action Position Command Heading Command Corrupted Map Navigation Action Latent Features Feature Mixing LSTM Memory Values Observations with Privileged ...
- **p. 2 / III. METHOD - extractive body cue:** Given a preestablished low-level locomotion policy [6], we train a navigation policy that generates velocity commands to be tracked in a hierarchical RL structure.
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 2 (III. METHOD), p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 2 (III. METHOD)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** However, such manually-designed rules cannot scale well to diverse situations.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Generally, given an accurate map, it is not difficult for existing navigation planners to guide the robot towards the local goal safely.
- **p. 2 / I. INTRODUCTION - extractive body cue:** The learned navigation policy generates velocity commands to a pre-existing low-level locomotion policy, and takes low-level observations as part of its inputs.
- **p. 6 / VI. LIMITATIONS AND FUTURE WORKS - extractive body cue:** Despite our policy's generalization to different collision geometries, we find it cannot handle out-of-distribution mapping noises.
- **p. 5 / V. RESULTS AND ANALYSES - extractive body cue:** These results indicate that the navigation policy cannot learn to react to perception failures without being exposed to them, and the locomotion policy cannot overcome ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2. Besides reaching the target in time, the robot should also reduce base collisions and avoid falls. An overview of our system is in ...
- **p. 6 / VI. LIMITATIONS AND FUTURE WORKS - extractive body cue:** Hence, it is of great interest if we can train a policy to actively explore these areas and explicitly revise the map allowing it to ...
- **Boundary to test:** Despite our policy's generalization to different collision geometries, we find it cannot handle out-of-distribution mapping noises.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this work, we propose to incorporate locomotion-level observations into navigation, contrasting existing methods that typically decouple navigation from locomotion. | p. 1 (I. INTRODUCTION), p. 2 (III. METHOD) |
| Reported outcome | According to the results, all of the policies perform well when the visibility is 100 %, and the Planner achieves a perfect 100 % success rate. | p. 5 (V. RESULTS AND ANALYSES), p. 5 (V. RESULTS AND ANALYSES) |
| Failure/limitation | Despite our policy's generalization to different collision geometries, we find it cannot handle out-of-distribution mapping noises. | p. 6 (VI. LIMITATIONS AND FUTURE WORKS), p. 5 (V. RESULTS AND ANALYSES) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, terrain/perception observation과 velocity command → body/contact state, foothold 또는 behavior mode → joint target, torque, footstep 또는 locomotion action`.
- 이 논문의 재사용 가능한 지점은 Actor Critic Low-Level Exteroception Proprioception Previous Action Position Command Heading Command Corrupted Map Navigation Action Latent Features Feature Mixing LSTM Memory Values Observations with Privileged Information Observations ...를 The learned navigation policy generates velocity commands to a pre-existing low-level locomotion policy, and takes low-level observations as part of its inputs.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 body/contact state, foothold 또는 behavior mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Despite our policy's generalization to different collision geometries, we find it cannot handle out-of-distribution mapping noises.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this work, we propose to incorporate locomotion-level observations into navigation, contrasting existing methods that typically decouple navigation from locomotion.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, legged locomotion, Navigation, robust perception`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Despite our policy's generalization to different collision geometries, we find it cannot handle out-of-distribution mapping noises.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Environments We verify our methodology on the quadruped ANYmal robot both in simulation and in the real world..
3. Compare against the body-reported baseline or a matched simpler baseline: Comparison Results We compare the proposed Ours with the baselines Oracle and Planner in simulation..
4. Report the body metric and its denominator/aggregation: According to the results, all of the policies perform well when the visibility is 100 %, and the Planner achieves a perfect 100 % success rate..
5. Re-run the body-reported ablation/failure condition: Fig. 1. An illustration of what happens under perception failures, exem- plified by an invisible obstacle case. (A) Without perception failures, both classical planners and our navigation policy can function well. (B) ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (III. METHOD), p. 2 (III. METHOD), p. 2 (III. METHOD); the primary result is directionally consistent at p. 5 (V. RESULTS AND ANALYSES), p. 5 (V. RESULTS AND ANALYSES), p. 4 (IV. EXPERIMENTAL SETUP); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 incorporate, locomotion-level, observations mechanism이 Comparison Results We compare the proposed Ours with the baselines Oracle and Planner in simulation. 대비 According to the results, all of the policies perform well when the visibility is 100 %, and the ...을 개선하고, Despite our policy's generalization to different collision geometries, we find it cannot handle out-of-distribution mapping noises. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
