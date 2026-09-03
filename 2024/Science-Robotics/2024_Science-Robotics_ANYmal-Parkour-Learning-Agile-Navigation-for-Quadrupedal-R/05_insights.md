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

- **Paper-specific interface:** Pre-training low-level skills with imitation learning and then controlling them through latent actions has been proposed for both character animation [33] and robotics [18]. (p. 5, 3) We develop a neural terrain reconstruction method that).
- **Paper-specific mechanism:** We can summarize our contributions as follows: (p. 3, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is Fig. 4: Training scenarios of the locomotion skills with the resulting behaviors. (A) Jumping. (B) Climbing down. (C) Climbing up. (D) Crouching. (E) Walking. (F) Success rate of each skill ... (p. 8, Figure/Table caption); the relevant task/metric cue is The locomotion and navigation modules operate synchronously in a single node on the onboard computer. (p. 5, II. RESULTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** The complexity of the task exacerbates many of the challenges commonly faced by mobile robots: • The locomotion controller cannot rely on a stable and periodic gait but must use ... (p. 1, I. INTRODUCTION).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, quadruped locomotion, parkour, Navigation`.
- **Reading predecessor in the generated track queue:** Learning Robust Perceptive Locomotion for Quadrupedal Robots in the Wild (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Finally, since the navigation module must make a series of correct decisions to reach the goal with many possibilities leading to failure, the algorithm requires many iterations to converge.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Pre-training low-level skills with imitation learning and then controlling them through latent actions has been proposed for both character animation [33] and robotics [18]. (p. 5, 3) We develop a neural terrain reconstruction method that); preserve the objective/update rule: While the navigation module receives a full 3D representation of the map, it is impractical for the locomotion policies due to their high update rate and the corresponding computational cost ... (p. 14, IV. MATERIALS AND METHODS).
2. Use the paper-reported task/data/environment cue: In trajectory B, the policy saturates the motor during the climb to propel the robot onto the 0.9 m high platform (Fig. (p. 5, II. RESULTS).
3. Compare against the reported or matched baseline: The skill learns to turn on the spot in tight spaces and is more capable in such scenarios compared to other skills. (p. 5, II. RESULTS).
4. Report the body metric with its denominator and aggregation: The locomotion and navigation modules operate synchronously in a single node on the onboard computer. (p. 5, II. RESULTS).
5. Re-run the reported ablation or stress/failure condition: The three learning-based modules operate together without expert demonstration, offline computation, or a priori knowledge of the environment and enable the robot to reliably reach a target across different arrangements ... (p. 5, II. RESULTS); if none is reported, design one around: The complexity of the task exacerbates many of the challenges commonly faced by mobile robots: • The locomotion controller cannot rely on a stable and periodic gait but must use ... (p. 1, I. INTRODUCTION).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 3 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), match the reported outcome at p. 8 (Figure/Table caption), p. 5 (II. RESULTS), p. 5 (II. RESULTS), and measure the boundary at p. 1 (I. INTRODUCTION), p. 12 (A. Current Limitations).

## Falsifiable research question

Under the paper's stated interface (Pre-training low-level skills with imitation learning and then controlling them through latent actions has been proposed for both character animation [33] and ...), does the paper-specific mechanism (We can summarize our contributions as follows:) retain the reported evaluation outcome (The locomotion and navigation modules operate synchronously in a single node on the onboard computer.) when tested against the paper's strongest explicit boundary (The complexity of the task exacerbates many of the challenges commonly faced by mobile robots: • The locomotion ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (The locomotion and navigation modules operate synchronously in a single node on the onboard computer.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (19 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** We can summarize our contributions as follows: (p. 3, I. INTRODUCTION).
- **Paper-supported outcome:** Fig. 4: Training scenarios of the locomotion skills with the resulting behaviors. (A) Jumping. (B) Climbing down. (C) Climbing up. (D) Crouching. (E) Walking. (F) Success rate of each skill ... (p. 8, Figure/Table caption).
- **Strongest explicit boundary:** The complexity of the task exacerbates many of the challenges commonly faced by mobile robots: • The locomotion controller cannot rely on a stable and periodic gait but must use ... (p. 1, I. INTRODUCTION).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
