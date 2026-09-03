# Insights — Learning Vision-Based Bipedal Locomotion for Challenging Terrain

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2309.14594; PDF retrieval source: https://arxiv.org/pdf/2309.14594. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** The relative encoding means that the heights vary as the robot moves up and down during its gait, but enables us to avoid using global ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The key contribution of our work is the sim-to-real pipeline and the system integration for these components, which allows the overall locomotion controller to transfer ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The proposed approach enables bipedal robot Cassie traversing over challenging terrains, including random high blocks, stairs, 0.5m step up (∼60% leg length), with speed up ...
- **p. 3 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** 3: Policy consists of a blind policy and a vision-based modulator. cos (2π(ϕt + γi t)).
- **p. 3 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** This allows the policy to gain some experience on easier terrains, which is useful early in learning, but focuses most of the learning effort on ...
- **p. 3 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** We use a neural network to represent the policy for mapping observation sequences to actions.
- **p. 2 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** Below, we describe the observation space, action space, architecture of the policy, and training methods.
- **Contribution anchor:** p. 2 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** Robustly achieving such an integration of vision and locomotion remains an open problem for bipedal robots.
- **p. 1 / I. INTRODUCTION - extractive body cue:** For this purpose, bipedal robots have the potential to match human locomotion capabilities, but currently are far inferior.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 7: A. Ablation study on policy with simulation heightmap. B. Ablation study on policy with different heightmap predictor architectures. Each ablation study uses data ...
- **p. 5 / VI. SIMULATION RESULTS - extractive body cue:** These random foot collisions with the terrain could lead to failures.
- **p. 5 / VI. SIMULATION RESULTS - extractive body cue:** Indeed, Terminations due to foot collision indicates that collisions account for most failure cases overall.
- **p. 6 / VI. SIMULATION RESULTS - extractive body cue:** In Termination due to foot collision, compared to LSTM, other models fails with higher chances from unfavorable foot collisions.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: Types of terrain used in training. a real robot. In particular, we use a three component reward function where all components are weighted ...
- **Boundary to test:** Fig. 7: A. Ablation study on policy with simulation heightmap. B. Ablation study on policy with different heightmap predictor architectures. Each ablation study uses data collected from a range of terrains defined ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The relative encoding means that the heights vary as the robot moves up and down during its gait, but enables us to avoid using global mapping and odometry estimation techniques, 3) user ... | p. 2 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 1 (I. INTRODUCTION) |
| Reported outcome | Fig. 6: Depth image from simulation and real world, with corre- sponding real predicted heightmap and simulation heightmap. mode of terrains. For more difficult terrain modes, however, policies w/o Learned Clock and ... | p. 5 (Figure/Table caption), p. 5 (VI. SIMULATION RESULTS) |
| Failure/limitation | Fig. 7: A. Ablation study on policy with simulation heightmap. B. Ablation study on policy with different heightmap predictor architectures. Each ablation study uses data collected from a range of terrains defined ... | p. 6 (Figure/Table caption), p. 5 (VI. SIMULATION RESULTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, terrain/perception observation과 velocity command → body/contact state, foothold 또는 behavior mode → joint target, torque, footstep 또는 locomotion action`.
- 이 논문의 재사용 가능한 지점은 The input to the vision-based modulator includes all of the available observations, including the heightmap, in addition to the action produced by the blind policy.를 In particular, our architecture is composed of two primary learned components: 1) a control policy whose input is proprioceptive information and a heightmap of a local region in front of the robot ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 body/contact state, foothold 또는 behavior mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Fig. 7: A. Ablation study on policy with simulation heightmap. B. Ablation study on policy with different heightmap predictor architectures. Each ablation study uses data collected from a range of terrains defined ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: The relative encoding means that the heights vary as the robot moves up and down during its gait, but enables us to avoid using global mapping and odometry estimation techniques, 3) user ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, bipedal locomotion, sim-to-real, Reinforcement Learning`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 7: A. Ablation study on policy with simulation heightmap. B. Ablation study on policy with different heightmap predictor architectures. Each ablation study uses data collected from a range of terrains defined ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Episodes with foot collision indicates the number of episodes that have one or more foot collision events occurred during rollouts, and such random collision events are unfavorable towards hardware deployment..
3. Compare against the body-reported baseline or a matched simpler baseline: Episodes with foot collision shows that, compared to Ours, other policies have significantly more foot collisions events..
4. Report the body metric and its denominator/aggregation: Although foot collisions lead to frequent failures, policy w/o Foot Collision Reward has a similar success rate as Ours..
5. Re-run the body-reported ablation/failure condition: Policy Performance We use the trained policy, along with a number of different policy setups, to evaluate the performance in simulation for the ablation study..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 2 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY); the primary result is directionally consistent at p. 5 (Figure/Table caption), p. 5 (VI. SIMULATION RESULTS), p. 6 (VI. SIMULATION RESULTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 relative, encoding, means mechanism이 Episodes with foot collision shows that, compared to Ours, other policies have significantly more foot collisions ... 대비 Although foot collisions lead to frequent failures, policy w/o Foot Collision Reward has a similar success rate as ...을 개선하고, Fig. 7: A. Ablation study on policy with simulation heightmap. B. Ablation study on policy with ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
