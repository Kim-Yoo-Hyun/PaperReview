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

- **Closed-loop position:** `multi-view observation, language/task label과 action trajectory → shared representation, embodiment/task identity와 data distribution → dataset sample 또는 learned policy action`.
- 이 논문의 재사용 가능한 지점은 A sim-to-real algorithm Algo for reward design and domain randomization takes M and task specification ltask as inputs, and outputs a reward function R and a distribution over transition functions, T : ...를 In Eureka, the LLM first takes the task description ltask and a summary of the environment state and action spaces (provided by environment code M) as input, and then samples several reward ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 shared representation, embodiment/task identity와 data distribution가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 While DrEureka demonstrates the potential of leveraging LLMs for automating the sim-to-real transfer process in robotics, there are several areas of improvement to the current implementation: • Lack of visual inputs: The ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this work, we propose DrEureka (Domain Randomization Eureka), a novel algorithm that leverages LLMs to automate reward design and domain randomization parameter configuration simultaneously for sim-to-real transfer.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, sim-to-real, Reinforcement Learning, Large Language Model, NVIDIA`.
- **Reading predecessor in the generated track queue:** Eureka: Human-Level Reward Design via Coding Large Language Models (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Continuous Control with Deep Reinforcement Learning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** While DrEureka demonstrates the potential of leveraging LLMs for automating the sim-to-real transfer process in robotics, there are several areas of improvement to the current implementation: • Lack of visual inputs: The ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We use the simulation environment as well as the real-world controller from Margolis et al..
3. Compare against the body-reported baseline or a matched simpler baseline: Forward locomotion specifically uses a teacher-student variant of PPO in which the teacher Sim-to-real Configuration Forward Velocity (m/s) Meters Traveled (m) Human-Designed [25] 1.32 ± 0.44 4.17 ± 1.57 Eureka [9] 0.0 ....
4. Report the body metric and its denominator/aggregation: Fig. 8: Forward locomotion training curves for 16 DR configurations. All runs are trained with the same reward function. B3. LLM Reward Reflection The following is an example of reward reflection on ....
5. Re-run the body-reported ablation/failure condition: Forward locomotion specifically uses a teacher-student variant of PPO in which the teacher Sim-to-real Configuration Forward Velocity (m/s) Meters Traveled (m) Human-Designed [25] 1.32 ± 0.44 4.17 ± 1.57 Eureka [9] 0.0 ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (IV. METHOD), p. 3 (IV. METHOD), p. 3 (IV. METHOD); the primary result is directionally consistent at p. 5 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 DrEureka, Domain, Randomization mechanism이 Forward locomotion specifically uses a teacher-student variant of PPO in which the teacher Sim-to-real Configuration Forward ... 대비 Fig. 8: Forward locomotion training curves for 16 DR configurations. All runs are trained with the same reward ...을 개선하고, While DrEureka demonstrates the potential of leveraging LLMs for automating the sim-to-real transfer process in robotics, ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
