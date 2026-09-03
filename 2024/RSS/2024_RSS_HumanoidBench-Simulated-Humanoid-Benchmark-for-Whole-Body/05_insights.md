# Insights — HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p061.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p061.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** To accelerate the progress of research for humanoid robots, We present the first-of-its-kind humanoid robot benchmark, HumanoidBench, with a diverse set of locomotion and manipulation ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present extensive benchmarking results of the state-of-the-art reinforcement leaning (RL) algorithms, which do not require extensive domain knowledge, and a hierarchical ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** 4, 42, 29, 17, 30, 48] In the context of humanoids, we propose an HRL paradigm
- **p. 3 / I. INTRODUCTION - extractive body cue:** While this is not currently a realistic model, we anticipate the trend in the industry towards developing slimmer, human-like hhands (e-g., Tesla Optimus, Figure 01) ...
- **p. 4 / I. INTRODUCTION - extractive body cue:** Torque-based control is also supported but we found that position control is generally more stable and allows for lower control frequency than torque control.
- **p. 1 / Abstract - extractive body cue:** To aecelerate algorithmic research in humanoid robots, we present a high-dimensional, simulated robot learning henchmark, HumanoidBench, featuring a humanoid robot equipped with dexterous hands and ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** The benchmarking results on this task suite show how the state-ofthe-art RL algorithms struggle with controlling the complex humanoid robot dynamics and solving the most ...
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 4 (I. INTRODUCTION), p. 1 (Abstract)

### Strongest assumption and failure boundary

- **p. 2 / I. INTRODUCTION - extractive body cue:** However, all these works focus fon demonstrating their approaches on specific humanoid tasks and lack a diversity of tasks.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, most of these benchmarks use a singlearm manipulation setup with either a parallel gripper or a dexterous hand [9, 49], limiting the types of ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our simulated humanoid benchmark demonstrates a variety of challenges in addressing learning for autonomous humanoid robots, such as the intricate control of robots with, complex ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** Although other sensory inputs are available from the environment, to investigate challenges in whole-body control of humanoid robots, we first focus on the state-based environment ...
- **p. 4 / I. INTRODUCTION - extractive body cue:** We devise 15 benchmarking whole-body manipulation tasks that cover a wide variety of interactions and difficulties.
- **p. 9 / B. Results - extractive body cue:** In this subsection, we remark on notable challenges and com- ‘mon failures for some representative tasks in our benchmark, which denote the challenge in learning ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 10: Failure Scenarios. This figure presents a selection of common failures that occur while training our benchmark tasks.
- **Boundary to test:** In this subsection, we remark on notable challenges and com- ‘mon failures for some representative tasks in our benchmark, which denote the challenge in learning with high-dimensional action spaces and limited planning ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To accelerate the progress of research for humanoid robots, We present the first-of-its-kind humanoid robot benchmark, HumanoidBench, with a diverse set of locomotion and manipulation tasks. | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Reported outcome | In Figure 9, our hierarchical architecture significantly outperforms the flat, end-to-end baselines on the push task, achieving very high success rates ‘with DreamerV3. | p. 9 (B. Results), p. 9 (B. Results) |
| Failure/limitation | In this subsection, we remark on notable challenges and com- ‘mon failures for some representative tasks in our benchmark, which denote the challenge in learning with high-dimensional action spaces and limited planning ... | p. 9 (B. Results), p. 10 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** ACM Transactions on policy optimisation. (p. 1, V. B ENCHMARKING R ESULTS).
- **Paper-specific mechanism:** [3] Firas Al-Hafez, Guoping Zhao, Jan Peters, and Davide We presented HumanoidBench, a high-dimensional hu- Tateo. (p. 1, V. B ENCHMARKING R ESULTS).
- **Evidence boundary:** the reported outcome is The results in combination of dense rewards and sparse subtask completion Figure 7 show that the presence of hands, with their additional rewards, and for each of these we provide ... (p. 1, V. B ENCHMARKING R ESULTS); the relevant task/metric cue is The results in combination of dense rewards and sparse subtask completion Figure 7 show that the presence of hands, with their additional rewards, and for each of these we provide ... (p. 1, V. B ENCHMARKING R ESULTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Mobility Fellowship 211086, ONR MURI N00014-22-1-2773, Common Failure on door. (p. 1, V. B ENCHMARKING R ESULTS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, humanoid, Benchmark, whole-body control, loco-manipulation`.
- **Reading predecessor in the generated track queue:** ANYmal Parkour: Learning Agile Navigation for Quadrupedal Robots (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In this subsection, we remark on notable challenges and com- ‘mon failures for some representative tasks in our benchmark, which denote the challenge in learning with high-dimensional action spaces and limited planning ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: ACM Transactions on policy optimisation. (p. 1, V. B ENCHMARKING R ESULTS); preserve the objective/update rule: All the policies barely learn to stabilize using the dense reward, but struggle to learn any complex no constraints on how to obtain both low-level and high-level manipulation skills. policies. (p. 1, V. B ENCHMARKING R ESULTS).
2. Use the paper-reported task/data/environment cue: This motivates us are limited to quasi-static, short-horizon skills, having focused to implement a comprehensive simulated humanoid benchmark on tasks like picking and placing [7, 24, 70, 64, 37], in-hand ... (p. 1, II. R ELATED W ORK).
3. Compare against the reported or matched baseline: In Figure 9, our hierarchical MJX8 , which enables training PPO on thousands of parallel architecture significantly outperforms the flat, end-to-end environments. baselines on the push task, achieving very high ... (p. 1, V. B ENCHMARKING R ESULTS).
4. Report the body metric with its denominator and aggregation: The results in combination of dense rewards and sparse subtask completion Figure 7 show that the presence of hands, with their additional rewards, and for each of these we provide ... (p. 1, V. B ENCHMARKING R ESULTS).
5. Re-run the reported ablation or stress/failure condition: 7: Performance with and without dexterous hands. (p. 1, V. B ENCHMARKING R ESULTS); if none is reported, design one around: Mobility Fellowship 211086, ONR MURI N00014-22-1-2773, Common Failure on door. (p. 1, V. B ENCHMARKING R ESULTS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (V. B ENCHMARKING R ESULTS), p. 1 (Abstract), match the reported outcome at p. 1 (V. B ENCHMARKING R ESULTS), p. 1 (V. B ENCHMARKING R ESULTS), p. 1 (Abstract), and measure the boundary at p. 1 (V. B ENCHMARKING R ESULTS), p. 1 (V. B ENCHMARKING R ESULTS).

## Falsifiable research question

Under the paper's stated interface (ACM Transactions on policy optimisation.), does the paper-specific mechanism ([3] Firas Al-Hafez, Guoping Zhao, Jan Peters, and Davide We presented HumanoidBench, a high-dimensional hu- Tateo.) retain the reported evaluation outcome (The results in combination of dense rewards and sparse subtask completion Figure 7 show that the presence of ...) when tested against the paper's strongest explicit boundary (Mobility Fellowship 211086, ONR MURI N00014-22-1-2773, Common Failure on door.)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (The results in combination of dense rewards and sparse subtask completion Figure 7 show that the presence of ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (1 pages; pdftotext fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** [3] Firas Al-Hafez, Guoping Zhao, Jan Peters, and Davide We presented HumanoidBench, a high-dimensional hu- Tateo. (p. 1, V. B ENCHMARKING R ESULTS).
- **Paper-supported outcome:** The results in combination of dense rewards and sparse subtask completion Figure 7 show that the presence of hands, with their additional rewards, and for each of these we provide ... (p. 1, V. B ENCHMARKING R ESULTS).
- **Strongest explicit boundary:** Mobility Fellowship 211086, ONR MURI N00014-22-1-2773, Common Failure on door. (p. 1, V. B ENCHMARKING R ESULTS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
