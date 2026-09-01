# Insights — Sim-to-Real: Learning Agile Locomotion For Quadruped Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://roboticsproceedings.org/rss14/p10.html; PDF retrieval source: https://arxiv.org/pdf/1804.10332. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** The main contributions of this paper are: 1) We propose a complete learning system for agile locomotion.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present a complete learning system for agile locomotion, in which control policies are learned in simulation and deployed on real robots.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We show that with deep RL, highly agile locomotion gaits can emerge automatically.
- **p. 4 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** For this reason, we decouple the locomotion controller into two parts, an open loop component that allows a user to provide reference trajectories and a ...
- **p. 3 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** Our problem is partially observable because certain states such as the position of the Minitaur's base and the foot contact forces are not accessible due ...
- **p. 4 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** We represent the feedback component π with a neural network and solve the above POMDP using Proximal Policy Optimization [5].
- **p. 3 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** More importantly, a compact observation space helps to transfer the policy to the real robot.
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** Overcoming the reality gap is challenging.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Even worse, this gap is greatly amplified in locomotion tasks.
- **p. 2 / I. INTRODUCTION - extractive body cue:** 2) We show that the reality gap can be narrowed by a variety of approaches and conduct comprehensive evaluations on their effectiveness.
- **p. 6 / VI. EVALUATION AND DISCUSSION - extractive body cue:** However, when the policies were deployed on the robot, we had mixed results due to the reality gap: Some policies can transfer while others cannot.
- **p. 6 / VI. EVALUATION AND DISCUSSION - extractive body cue:** Note that while this open loop controller expresses the user's preference of the locomotion style, by itself, it cannot produce any forward movement in the ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: The simulated and the real Minitaurs learned to gallop using deep reinforcement learning. to locomotion tasks due to the difficulties of automatically resetting ...
- **p. 8 / VII. CONCLUSION - extractive body cue:** This points us to two interesting avenues for future work.
- **Boundary to test:** However, when the policies were deployed on the robot, we had mixed results due to the reality gap: Some policies can transfer while others cannot.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The main contributions of this paper are: 1) We propose a complete learning system for agile locomotion. | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Reported outcome | After we improved the simulation (Section V-A), an agile galloping gait emerged automatically. | p. 6 (VI. EVALUATION AND DISCUSSION), p. 6 (VI. EVALUATION AND DISCUSSION) |
| Failure/limitation | However, when the policies were deployed on the robot, we had mixed results due to the reality gap: Some policies can transfer while others cannot. | p. 6 (VI. EVALUATION AND DISCUSSION), p. 6 (VI. EVALUATION AND DISCUSSION) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, terrain/perception observation과 velocity command → body/contact state, foothold 또는 behavior mode → joint target, torque, footstep 또는 locomotion action`.
- 이 논문의 재사용 가능한 지점은 If we want a policy that is learned from scratch, we can set ¯a(t) = 0 and give the feedback component π(o) a wide output range.를 For this reason, we decouple the locomotion controller into two parts, an open loop component that allows a user to provide reference trajectories and a feedback component that adjusts the leg poses ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 body/contact state, foothold 또는 behavior mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 However, when the policies were deployed on the robot, we had mixed results due to the reality gap: Some policies can transfer while others cannot.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: The main contributions of this paper are: 1) We propose a complete learning system for agile locomotion.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, quadruped locomotion, Reinforcement Learning, sim-to-real`.
- **Reading predecessor in the generated track queue:** DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Learning Quadrupedal Locomotion over Challenging Terrain (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** However, when the policies were deployed on the robot, we had mixed results due to the reality gap: Some policies can transfer while others cannot.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: This time, we observed stable, comparable movements in both simulation and on the real robot..
3. Compare against the body-reported baseline or a matched simpler baseline: We compared the learned gaits with the handcrafted ones from Ghost Robotics [3]..
4. Report the body metric and its denominator/aggregation: Fig. 8: Performance of controllers when they are tested in different simulation environments. Error bars indicate one standard deviation. 0 2 4 6 small.
5. Re-run the body-reported ablation/failure condition: The controllers worked directly in the real world without additional fine tuning on the physical system..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS); the primary result is directionally consistent at p. 6 (VI. EVALUATION AND DISCUSSION), p. 6 (VI. EVALUATION AND DISCUSSION), p. 7 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 main, contributions, complete mechanism이 We compared the learned gaits with the handcrafted ones from Ghost Robotics [3]. 대비 Fig. 8: Performance of controllers when they are tested in different simulation environments. Error bars indicate one standard ...을 개선하고, However, when the policies were deployed on the robot, we had mixed results due to the ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
