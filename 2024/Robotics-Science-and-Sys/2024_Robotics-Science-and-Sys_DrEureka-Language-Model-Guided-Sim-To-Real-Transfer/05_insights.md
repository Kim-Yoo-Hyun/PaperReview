# Insights — DrEureka: Language Model Guided Sim-To-Real Transfer

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p094.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p094.html. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose DrEureka (Domain Randomization Eureka), a novel algorithm that leverages LLMs to automate reward design and domain randomization parameter configuration simultaneously ...
- **p. 4 / IV. METHOD - extractive body cue:** Instead, we propose to directly exploit the strong instructionfollowing capability of instruction-tuned LLMs [62] and prompt the LLM to explicitly consider including safety terms for ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** We evaluate DrEureka on quadruped and dexterous manipulator platforms, demonstrating that our method is general
- **p. 3 / IV. METHOD - extractive body cue:** In this section, we introduce DrEureka, which uses LLMs to automate two important bottlenecks in sim-to-real design: reward design and domain randomization.
- **p. 4 / IV. METHOD - extractive body cue:** We introduce a simple reward aware physics prior (RAPP) mechanism to restrict the base ranges for the LLM.
- **p. 4 / IV. METHOD - extractive body cue:** Algorithm 2 Reward Aware Physics Prior (RAPP) 1: Require: Reinforcement learning policy πinitial, simulator S, success criteria F, domain randomization parameters P and their respective ...
- **p. 3 / IV. METHOD - extractive body cue:** In Eureka, the LLM first takes the task description ltask and a summary of the environment state and action spaces (provided by environment code M) ...
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 4 (IV. METHOD), p. 1 (I. INTRODUCTION), p. 3 (IV. METHOD), p. 4 (IV. METHOD), p. 4 (IV. METHOD)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** Directly synthesizing robot policies from LLMs is difficult because it does not explicitly reason through the physics of the environment, however, when a simulator is ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** These characteristics of designing DR parameters make it an ideal problem for LLMs to tackle because of their strong grasp of physical knowledge [1, 18] ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Walking globe is a novel task to show DrEureka's capability for guiding the sim-to-real transfer of a challenging new task without pre-existing sim-to-real configurations.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Then, it tests the policy under different simulation conditions to build a reward-aware physics prior, which is provided to the LLM to generate a set ...
- **p. 3 / III. PROBLEM SETTING - extractive body cue:** We formalize the sim-to-real design problem setting.
- **p. 9 / VIII. LIMITATIONS - extractive body cue:** While DrEureka demonstrates the potential of leveraging LLMs for automating the sim-to-real transfer process in robotics, there are several areas of improvement to the current ...
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** Sim-to-real Configuration Rotation (rad) Time-to-Fall (s) Human-Designed [25] 3.24 ± 1.66 20.00 ± 0.00 Our Method (Best) 9.39 ± 4.15 20.00 ± 0.00 Our Method ...
- **Boundary to test:** While DrEureka demonstrates the potential of leveraging LLMs for automating the sim-to-real transfer process in robotics, there are several areas of improvement to the current implementation: • Lack of visual inputs: The ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this work, we propose DrEureka (Domain Randomization Eureka), a novel algorithm that leverages LLMs to automate reward design and domain randomization parameter configuration simultaneously for sim-to-real transfer. | p. 1 (I. INTRODUCTION), p. 4 (IV. METHOD) |
| Reported outcome | The task of forward locomotion is to walk forward at 2 meters-per-second on flat terrains; while it is possible for the robot to walk forward at a higher speed, we find 2 ... | p. 5 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP) |
| Failure/limitation | While DrEureka demonstrates the potential of leveraging LLMs for automating the sim-to-real transfer process in robotics, there are several areas of improvement to the current implementation: • Lack of visual inputs: The ... | p. 9 (VIII. LIMITATIONS), p. 6 (V. EXPERIMENTAL SETUP) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Instead, we propose to directly exploit the strong instructionfollowing capability of instruction-tuned LLMs [62] and prompt the LLM to explicitly consider including safety terms for stability, smoothness, and desirable task-specific ... (p. 4, IV. METHOD).
- **Paper-specific mechanism:** In this work, we propose DrEureka (Domain Randomization Eureka), a novel algorithm that leverages LLMs to automate reward design and domain randomization parameter configuration simultaneously for sim-to-real transfer. (p. 1, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is Note that while CEM and BayRn tackle the same problem, their iterative procedure is conceptually different from DrEureka, which trains all policies in parallel; thus, this comparison favors the baselines ... (p. 6, V. EXPERIMENTAL SETUP); the relevant task/metric cue is Therefore, the differences in performance between DrEureka and Human-Designed can be attributed to the different DR parameters as well as reward functions DrEureka produces. (p. 6, V. EXPERIMENTAL SETUP). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** While DrEureka demonstrates the potential of leveraging LLMs for automating the sim-to-real transfer process in robotics, there are several areas of improvement to the current implementation: • Lack of visual ... (p. 9, VIII. LIMITATIONS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, sim-to-real, Reinforcement Learning, Large Language Model, NVIDIA`.
- **Reading predecessor in the generated track queue:** Eureka: Human-Level Reward Design via Coding Large Language Models (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Continuous Control with Deep Reinforcement Learning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** While DrEureka demonstrates the potential of leveraging LLMs for automating the sim-to-real transfer process in robotics, there are several areas of improvement to the current implementation: • Lack of visual inputs: The ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Instead, we propose to directly exploit the strong instructionfollowing capability of instruction-tuned LLMs [62] and prompt the LLM to explicitly consider including safety terms for stability, smoothness, and desirable task-specific ... (p. 4, IV. METHOD); preserve the objective/update rule: Algorithm 2 Reward Aware Physics Prior (RAPP) 1: Require: Reinforcement learning policy πinitial, simulator S, success criteria F, domain randomization parameters P and their respective search values R, 2: for ... (p. 4, IV. METHOD).
2. Use the paper-reported task/data/environment cue: We use the simulation environment as well as the real-world controller from Margolis et al. (p. 5, V. EXPERIMENTAL SETUP).
3. Compare against the reported or matched baseline: Forward locomotion specifically uses a teacher-student variant of PPO in which the teacher Sim-to-real Configuration Forward Velocity (m/s) Meters Traveled (m) Human-Designed [25] 1.32 ± 0.44 4.17 ± 1.57 Eureka ... (p. 6, V. EXPERIMENTAL SETUP).
4. Report the body metric with its denominator and aggregation: Therefore, the differences in performance between DrEureka and Human-Designed can be attributed to the different DR parameters as well as reward functions DrEureka produces. (p. 6, V. EXPERIMENTAL SETUP).
5. Re-run the reported ablation or stress/failure condition: Forward locomotion specifically uses a teacher-student variant of PPO in which the teacher Sim-to-real Configuration Forward Velocity (m/s) Meters Traveled (m) Human-Designed [25] 1.32 ± 0.44 4.17 ± 1.57 Eureka ... (p. 6, V. EXPERIMENTAL SETUP); if none is reported, design one around: While DrEureka demonstrates the potential of leveraging LLMs for automating the sim-to-real transfer process in robotics, there are several areas of improvement to the current implementation: • Lack of visual ... (p. 9, VIII. LIMITATIONS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), match the reported outcome at p. 6 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP), p. 26 (Figure/Table caption), and measure the boundary at p. 9 (VIII. LIMITATIONS), p. 4 (IV. METHOD).

## Falsifiable research question

Under the paper's stated interface (Instead, we propose to directly exploit the strong instructionfollowing capability of instruction-tuned LLMs [62] and prompt the LLM to explicitly consider including ...), does the paper-specific mechanism (In this work, we propose DrEureka (Domain Randomization Eureka), a novel algorithm that leverages LLMs to automate reward design and domain randomization ...) retain the reported evaluation outcome (Therefore, the differences in performance between DrEureka and Human-Designed can be attributed to the different DR parameters as ...) when tested against the paper's strongest explicit boundary (While DrEureka demonstrates the potential of leveraging LLMs for automating the sim-to-real transfer process in robotics, there are ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Therefore, the differences in performance between DrEureka and Human-Designed can be attributed to the different DR parameters as ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (28 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In this work, we propose DrEureka (Domain Randomization Eureka), a novel algorithm that leverages LLMs to automate reward design and domain randomization parameter configuration simultaneously for sim-to-real transfer. (p. 1, I. INTRODUCTION).
- **Paper-supported outcome:** Note that while CEM and BayRn tackle the same problem, their iterative procedure is conceptually different from DrEureka, which trains all policies in parallel; thus, this comparison favors the baselines ... (p. 6, V. EXPERIMENTAL SETUP).
- **Strongest explicit boundary:** While DrEureka demonstrates the potential of leveraging LLMs for automating the sim-to-real transfer process in robotics, there are several areas of improvement to the current implementation: • Lack of visual ... (p. 9, VIII. LIMITATIONS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
