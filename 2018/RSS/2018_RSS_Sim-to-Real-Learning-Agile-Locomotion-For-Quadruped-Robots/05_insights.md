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

- **Paper-specific interface:** For this reason, we decouple the locomotion controller into two parts, an open loop component that allows a user to provide reference trajectories and a feedback component that adjusts the ... (p. 4, IV. LEARNING LOCOMOTION CONTROLLERS).
- **Paper-specific mechanism:** The main contributions of this paper are: 1) We propose a complete learning system for agile locomotion. (p. 2, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is Fig. 6: Controller performance in simulation (blue) and on the robot (red). From left to right, the controllers are trained using baseline simulation, using baseline simulation with random perturbations, and ... (p. 7, Figure/Table caption); the relevant task/metric cue is While it is unclear how to use reward shaping to learn such a gait, we can directly control the learned gait by providing an open loop signal (¯a(t) in eq. (p. 6, VI. EVALUATION AND DISCUSSION). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** However, the binary outcome of success or failure does not capture the key characteristics of locomotion, such as running speed and energy consumption. (p. 7, B. Narrowing the Reality Gap).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, quadruped locomotion, Reinforcement Learning, sim-to-real`.
- **Reading predecessor in the generated track queue:** DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Learning Quadrupedal Locomotion over Challenging Terrain (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** However, when the policies were deployed on the robot, we had mixed results due to the reality gap: Some policies can transfer while others cannot.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: For this reason, we decouple the locomotion controller into two parts, an open loop component that allows a user to provide reference trajectories and a feedback component that adjusts the ... (p. 4, IV. LEARNING LOCOMOTION CONTROLLERS); preserve the objective/update rule: Reinforcement learning optimizes a policy π : O 7→A that maximizes the expected return (accumulated rewards) R. π∗= arg maxπEs0∼D[Rπ(s0)] (1) B. (p. 3, IV. LEARNING LOCOMOTION CONTROLLERS).
2. Use the paper-reported task/data/environment cue: This time, we observed stable, comparable movements in both simulation and on the real robot. (p. 6, VI. EVALUATION AND DISCUSSION).
3. Compare against the reported or matched baseline: We compared the learned gaits with the handcrafted ones from Ghost Robotics [3]. (p. 6, VI. EVALUATION AND DISCUSSION).
4. Report the body metric with its denominator and aggregation: While it is unclear how to use reward shaping to learn such a gait, we can directly control the learned gait by providing an open loop signal (¯a(t) in eq. (p. 6, VI. EVALUATION AND DISCUSSION).
5. Re-run the reported ablation or stress/failure condition: The controllers worked directly in the real world without additional fine tuning on the physical system. (p. 6, VI. EVALUATION AND DISCUSSION); if none is reported, design one around: However, the binary outcome of success or failure does not capture the key characteristics of locomotion, such as running speed and energy consumption. (p. 7, B. Narrowing the Reality Gap).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), match the reported outcome at p. 7 (Figure/Table caption), p. 6 (VI. EVALUATION AND DISCUSSION), p. 6 (VI. EVALUATION AND DISCUSSION), and measure the boundary at p. 7 (B. Narrowing the Reality Gap), p. 6 (VI. EVALUATION AND DISCUSSION).

## Falsifiable research question

Under the paper's stated interface (For this reason, we decouple the locomotion controller into two parts, an open loop component that allows a user to provide reference ...), does the paper-specific mechanism (The main contributions of this paper are: 1) We propose a complete learning system for agile locomotion.) retain the reported evaluation outcome (While it is unclear how to use reward shaping to learn such a gait, we can directly control ...) when tested against the paper's strongest explicit boundary (However, the binary outcome of success or failure does not capture the key characteristics of locomotion, such as ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (While it is unclear how to use reward shaping to learn such a gait, we can directly control ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (11 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** The main contributions of this paper are: 1) We propose a complete learning system for agile locomotion. (p. 2, I. INTRODUCTION).
- **Paper-supported outcome:** Fig. 6: Controller performance in simulation (blue) and on the robot (red). From left to right, the controllers are trained using baseline simulation, using baseline simulation with random perturbations, and ... (p. 7, Figure/Table caption).
- **Strongest explicit boundary:** However, the binary outcome of success or failure does not capture the key characteristics of locomotion, such as running speed and energy consumption. (p. 7, B. Narrowing the Reality Gap).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
