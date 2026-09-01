# Insights — ANYmal Parkour: Learning Agile Navigation for Quadrupedal Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2306.14874; PDF retrieval source: https://arxiv.org/pdf/2306.14874. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 5 / 3) We develop a neural terrain reconstruction method that - extractive body cue:** Despite the promising results and the close similarity to our method, this work requires human-designed path and skill selection and is limited to a single ...
- **p. 5 / 3) We develop a neural terrain reconstruction method that - extractive body cue:** To the best of our knowledge, we propose the first system that can perform agile navigation with a quadrupedal robot in such challenging scenarios without ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** We can summarize our contributions as follows:
- **p. 3 / I. INTRODUCTION - extractive body cue:** Contributions In our experimental validation, we demonstrate the system's ability to solve the problem autonomously, resulting in behaviors not shown before with such platforms.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This discipline requires years of practice to develop the necessary competencies, intuitions, and reflexes and is considered particularly dangerous.
- **p. 5 / 3) We develop a neural terrain reconstruction method that - extractive body cue:** Pre-training low-level skills with imitation learning and then controlling them through latent actions has been proposed for both character animation [33] and robotics [18].
- **p. 3 / 3) We develop a neural terrain reconstruction method that - extractive body cue:** We also modify the network architecture to allow for efficient inference with large batch sizes during RL training.
- **Contribution anchor:** p. 5 (3) We develop a neural terrain reconstruction method that), p. 5 (3) We develop a neural terrain reconstruction method that), p. 3 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 5 (3) We develop a neural terrain reconstruction method that)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** The complexity of the task exacerbates many of the challenges commonly faced by mobile robots: • The locomotion controller cannot rely on a stable and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Method overview This work aims to solve the above-mentioned challenges and proposes a method to perform agile navigation with a quadrupedal robot in parkour-like settings ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** The robot can cross difficult terrains with speeds of up to 2 m/s and make the right navigation decisions to reach the target in time.
- **p. 3 / I. INTRODUCTION - extractive body cue:** Contributions In our experimental validation, we demonstrate the system's ability to solve the problem autonomously, resulting in behaviors not shown before with such platforms.
- **p. 12 / A. Current Limitations - extractive body cue:** Finally, since the navigation module must make a series of correct decisions to reach the goal with many possibilities leading to failure, the algorithm requires ...
- **p. 12 / A. Current Limitations - extractive body cue:** We develop a specific curriculum to overcome this limitation.
- **p. 5 / II. RESULTS - extractive body cue:** 3 (A2)), which is necessary for the leg to reach the other side of the gap and catch the fall of the robot during the ...
- **Boundary to test:** Finally, since the navigation module must make a series of correct decisions to reach the goal with many possibilities leading to failure, the algorithm requires many iterations to converge.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Despite the promising results and the close similarity to our method, this work requires human-designed path and skill selection and is limited to a single pre-mapped environment with a motion capture system. | p. 5 (3) We develop a neural terrain reconstruction method that), p. 5 (3) We develop a neural terrain reconstruction method that) |
| Reported outcome | Fig. 4: Training scenarios of the locomotion skills with the resulting behaviors. (A) Jumping. (B) Climbing down. (C) Climbing up. (D) Crouching. (E) Walking. (F) Success rate of each skill for obstacles ... | p. 8 (Figure/Table caption), p. 4 (Figure/Table caption) |
| Failure/limitation | Finally, since the navigation module must make a series of correct decisions to reach the goal with many possibilities leading to failure, the algorithm requires many iterations to converge. | p. 12 (A. Current Limitations), p. 12 (A. Current Limitations) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, terrain/perception observation과 velocity command → body/contact state, foothold 또는 behavior mode → joint target, torque, footstep 또는 locomotion action`.
- 이 논문의 재사용 가능한 지점은 As input, the policies receive the current proprioceptive state, a local map of the surrounding terrain, an intermediate command, and output position commands to the motors.를 While these approaches produce a separate representation, the exteroceptive measurements can also be directly provided as input to the policy [8], [40].로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 body/contact state, foothold 또는 behavior mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Finally, since the navigation module must make a series of correct decisions to reach the goal with many possibilities leading to failure, the algorithm requires many iterations to converge.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Despite the promising results and the close similarity to our method, this work requires human-designed path and skill selection and is limited to a single pre-mapped environment with a motion capture system.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, quadruped locomotion, parkour, Navigation`.
- **Reading predecessor in the generated track queue:** Learning Robust Perceptive Locomotion for Quadrupedal Robots in the Wild (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Finally, since the navigation module must make a series of correct decisions to reach the goal with many possibilities leading to failure, the algorithm requires many iterations to converge.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The three learning-based modules operate together without expert demonstration, offline computation, or a priori knowledge of the environment and enable the robot to reliably reach a target across different arrangements of randomized ....
3. Compare against the body-reported baseline or a matched simpler baseline: The skill learns to turn on the spot in tight spaces and is more capable in such scenarios compared to other skills..
4. Report the body metric and its denominator/aggregation: Fig. 4: Training scenarios of the locomotion skills with the resulting behaviors. (A) Jumping. (B) Climbing down. (C) Climbing up. (D) Crouching. (E) Walking. (F) Success rate of each skill for obstacles ....
5. Re-run the body-reported ablation/failure condition: The three learning-based modules operate together without expert demonstration, offline computation, or a priori knowledge of the environment and enable the robot to reliably reach a target across different arrangements of randomized ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (3) We develop a neural terrain reconstruction method that), p. 3 (3) We develop a neural terrain reconstruction method that), p. 14 (IV. MATERIALS AND METHODS); the primary result is directionally consistent at p. 8 (Figure/Table caption), p. 4 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Despite, promising, close mechanism이 The skill learns to turn on the spot in tight spaces and is more capable in ... 대비 Fig. 4: Training scenarios of the locomotion skills with the resulting behaviors. (A) Jumping. (B) Climbing down. (C) ...을 개선하고, Finally, since the navigation module must make a series of correct decisions to reach the goal ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
