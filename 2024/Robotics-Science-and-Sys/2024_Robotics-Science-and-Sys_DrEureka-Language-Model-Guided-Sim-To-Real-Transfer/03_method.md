# Method - DrEureka: Language Model Guided Sim-To-Real Transfer

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p094.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p094.html. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (IV. METHOD), p. 3 (IV. METHOD), p. 3 (IV. METHOD), p. 4 (IV. METHOD), p. 5 (IV. METHOD), p. 5 (IV. METHOD)): Algorithm 2 Reward Aware Physics Prior (RAPP) 1: Require: Reinforcement learning policy πinitial, simulator S, success criteria F, domain randomization parameters P and their respective search values R, 2: for ...

## Method Body Digest

- **p. 4 / IV. METHOD - extractive body cue:** Algorithm 2 Reward Aware Physics Prior (RAPP) 1: Require: Reinforcement learning policy πinitial, simulator S, success criteria F, domain randomization parameters P and their respective ...
- **p. 3 / IV. METHOD - extractive body cue:** In Eureka, the LLM first takes the task description ltask and a summary of the environment state and action spaces (provided by environment code M) ...
- **p. 3 / IV. METHOD - extractive body cue:** At a high level, DrEureka first uses the LLM to generate a reward function that is both effective at the task and safe (Section IV-A ...
- **p. 4 / IV. METHOD - extractive body cue:** Instead, we propose to directly exploit the strong instructionfollowing capability of instruction-tuned LLMs [62] and prompt the LLM to explicitly consider including safety terms for ...
- **p. 5 / IV. METHOD - extractive body cue:** Finally, we use RL to train policies for each reward and DR combination, resulting in a set of policies where πfinal,i = A(M, Ti, RDrEureka), ...
- **p. 5 / IV. METHOD - extractive body cue:** Finally, note that some prior works prescribe continuously tuning the DR configuration to adapt to improving policy capabilities over the course of training [27, 28, ...
- **p. 4 / IV. METHOD - extractive body cue:** These scores as well as other training statistics (e.g., values of the reward components during training) are provided as feedback to the LLM to iteratively ...
- **p. 4 / IV. METHOD - extractive body cue:** Algorithm 1 DrEureka Reward Design 1: Require: Task description ltask, safety instruction lsafety, RL algorithm A, environment code M, coding LLM LLM, fitness function F, ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose DrEureka (Domain Randomization Eureka), a novel algorithm that leverages LLMs to automate reward design and domain randomization parameter configuration simultaneously ...
- **p. 4 / IV. METHOD - extractive body cue:** Instead, we propose to directly exploit the strong instructionfollowing capability of instruction-tuned LLMs [62] and prompt the LLM to explicitly consider including safety terms for ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** We evaluate DrEureka on quadruped and dexterous manipulator platforms, demonstrating that our method is general

## Source Evidence Cues

- **p. 4 / IV. METHOD - extractive body cue:** Algorithm 2 Reward Aware Physics Prior (RAPP) 1: Require: Reinforcement learning policy πinitial, simulator S, success criteria F, domain randomization parameters P and their respective ...
- **p. 3 / IV. METHOD - extractive body cue:** In Eureka, the LLM first takes the task description ltask and a summary of the environment state and action spaces (provided by environment code M) ...
- **p. 3 / IV. METHOD - extractive body cue:** At a high level, DrEureka first uses the LLM to generate a reward function that is both effective at the task and safe (Section IV-A ...
- **p. 4 / IV. METHOD - extractive body cue:** Instead, we propose to directly exploit the strong instructionfollowing capability of instruction-tuned LLMs [62] and prompt the LLM to explicitly consider including safety terms for ...
- **p. 5 / IV. METHOD - extractive body cue:** Finally, we use RL to train policies for each reward and DR combination, resulting in a set of policies where πfinal,i = A(M, Ti, RDrEureka), ...
- **p. 5 / IV. METHOD - extractive body cue:** Finally, note that some prior works prescribe continuously tuning the DR configuration to adapt to improving policy capabilities over the course of training [27, 28, ...
- **Detected method headings:** IV. METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data schema / normalization | heterogeneous robot trajectory를 공통 sample로 만든다 | observation, action, task와 embodiment metadata | sensor/action schema alignment, filtering, normalization을 수행 | shared dataset representation | Algorithm 2 Reward Aware Physics Prior (RAPP) 1: Require: Reinforcement learning policy πinitial, simulator S, success criteria F, domain randomization parameters P ... | p. 4 (IV. METHOD), p. 3 (IV. METHOD) |
| Coverage / augmentation | task·embodiment·failure variation을 확장한다 | dataset과 metadata | retargeting, relabeling, synthetic/teleoperation augmentation 또는 sampling을 적용 | expanded data support | In Eureka, the LLM first takes the task description ltask and a summary of the environment state and action spaces (provided by ... | p. 3 (IV. METHOD), p. 3 (IV. METHOD) |
| Downstream learning interface | 정규화된 data를 policy/representation이 사용한다 | shared observations/actions | pretraining, BC, action-token 또는 representation learning을 수행 | checkpoint/policy action | At a high level, DrEureka first uses the LLM to generate a reward function that is both effective at the task and ... | p. 3 (IV. METHOD), p. 4 (IV. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / IV. METHOD - extractive body cue:** These scores as well as other training statistics (e.g., values of the reward components during training) are provided as feedback to the LLM to iteratively ...
- **p. 4 / IV. METHOD - extractive body cue:** Algorithm 1 DrEureka Reward Design 1: Require: Task description ltask, safety instruction lsafety, RL algorithm A, environment code M, coding LLM LLM, fitness function F, ...
- **p. 3 / IV. METHOD - extractive body cue:** In this section, we introduce DrEureka, which uses LLMs to automate two important bottlenecks in sim-to-real design: reward design and domain randomization.
- **p. 3 / IV. METHOD - extractive body cue:** In Eureka, the LLM first takes the task description ltask and a summary of the environment state and action spaces (provided by environment code M) ...
- **p. 5 / IV. METHOD - extractive body cue:** Finally, we use RL to train policies for each reward and DR combination, resulting in a set of policies where πfinal,i = A(M, Ti, RDrEureka), ...
- **Formal bridge:** trajectory D with task/embodiment metadata -> normalized sample or downstream action -> coverage/data efficiency/transfer objective -> cross-domain transfer and task performance.
- **Equation/algorithm anchors:** p. 4 (IV. METHOD), p. 4 (IV. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | sim-to-real, algorithm, Algo, reward, design, domain, randomization, takes, task, specification, ltask, inputs, outputs, function | multi-view observation, language/task label과 action trajectory | body cue; exact tensor/frame verify |
| State/latent | sim-to-real, algorithm, Algo, reward, design, domain, randomization, takes, task, specification | shared representation, embodiment/task identity와 data distribution | body cue; notation verify |
| Action/output | DrEureka, Domain, Randomization, Eureka, novel, algorithm, leverages, LLMs, automate, reward | dataset sample 또는 learned policy action | body cue; unit/decoder verify |
| Objective/constraint | scores, well, other, training, statistics, values, reward, components, during, provided | coverage/data efficiency/transfer objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. PROBLEM SETTING - extractive body cue:** A sim-to-real algorithm Algo for reward design and domain randomization takes M and task specification ltask as inputs, and outputs a reward function R and ...
- **p. 3 / IV. METHOD - extractive body cue:** In Eureka, the LLM first takes the task description ltask and a summary of the environment state and action spaces (provided by environment code M) ...
- **p. 4 / IV. METHOD - extractive body cue:** Algorithm 1 DrEureka Reward Design 1: Require: Task description ltask, safety instruction lsafety, RL algorithm A, environment code M, coding LLM LLM, fitness function F, ...
- **p. 4 / IV. METHOD - extractive body cue:** Instead, we propose to directly exploit the strong instructionfollowing capability of instruction-tuned LLMs [62] and prompt the LLM to explicitly consider including safety terms for ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** 1: DrEureka takes the task and safety instruction, along with environment source code, and runs Eureka to generate a regularized reward function and policy.
- **p. 1 / I. INTRODUCTION - extractive body cue:** To make Eureka reward functions more amenable for real-world transfer, we propose to include safety instructions in the prompt to automatically generate reward functions that ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Instead, DrEureka decomposes the optimization into three stages: an LLM first synthesizes reward functions, then an initial policy is rolled out in perturbed simulations to ...
- **Normalized interface:** observation=multi-view observation, language/task label과 action trajectory; state=shared representation, embodiment/task identity와 data distribution; output/action=dataset sample 또는 learned policy action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | trajectory demonstration horizon; training sample window와 deployment task horizon을 분리한다. | Its observations include joint positions, joint velocities, and a gravity vector in the robot's local frame, as well as a history of ... | episode/sequence/action-chunk boundary |
| Rate / latency | data recording/action sampling rate와 policy inference/control rate를 분리한다. | LLM for Domain Randomization Given the RAPP ranges for each DR parameter, the final step of DrEureka instructs the LLM to generate ... | Hz/fps, inference time and control rate |
| Memory | trajectory, embodiment/task metadata와 dataset index. | Its observations include joint positions, joint velocities, and a gravity vector in the robot's local frame, as well as a history of ... | window and reset |
| Compute | data decoding, normalization/augmentation과 downstream training budget이 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / IV. METHOD - extractive body cue:** Finally, we use RL to train policies for each reward and DR combination, resulting in a set of policies where πfinal,i = A(M, Ti, RDrEureka), ...
- **p. 5 / IV. METHOD - extractive body cue:** Finally, note that some prior works prescribe continuously tuning the DR configuration to adapt to improving policy capabilities over the course of training [27, 28, ...
- **p. 4 / IV. METHOD - extractive body cue:** Algorithm 1 DrEureka Reward Design 1: Require: Task description ltask, safety instruction lsafety, RL algorithm A, environment code M, coding LLM LLM, fitness function F, ...
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** For every DR configuration, we train policies using 3 random seeds and report average as well as standard deviation across trials and seeds.
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** Second, we consider a baseline that trains with the human-designed DR (Human-Designed DR) in the original implementation.
- **p. 4 / IV. METHOD - extractive body cue:** This is a challenging problem because we do not have access to the real-world environment M ∗at training time.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Algorithm, Reward, Aware, Physics, Prior, RAPP, Require, Reinforcement, learning, policy, initial, simulator, success, criteria, domain, randomization, parameters, respective, search, values.
- **Relevant PDF headings:** IV. METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data schema / normalization | We use the simulation environment as well as the real-world controller from Margolis et al. | p. 5 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP) |
| Coverage / augmentation | Forward locomotion specifically uses a teacher-student variant of PPO in which the teacher Sim-to-real Configuration Forward Velocity (m/s) Meters Traveled (m) Human-Designed ... | p. 6 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP) |
| Downstream learning interface | The task of forward locomotion is to walk forward at 2 meters-per-second on flat terrains; while it is possible for the robot ... | p. 5 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP) |

## Failure and Ablation Link

- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** Forward locomotion specifically uses a teacher-student variant of PPO in which the teacher Sim-to-real Configuration Forward Velocity (m/s) Meters Traveled (m) Human-Designed [25] 1.32 ± ...
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** In the second category of ablations, we consider an ablation that only has access to the set of physics parameters but without the reward-aware priors ...
- **p. 26 / Figure/Table caption - extractive body cue:** Fig. 9: Policies trained on DrEureka DR configurations exert less torque in the real world. E. Additional Ablation Results Sampling from DrEureka priors enables stable ...
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** 1In both Without Prior and Uninformative Prior experiments, 15 out of the 16 policies resulted in jerky and dangerous behavior, many times immediately triggering the ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: Our quadruped locomotion, dexterous cube rotation, and walk- ing globe tasks. Walking globe is a novel task to show DrEureka's capability for guiding ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: DrEureka takes the task and safety instruction, along with environment source code, and runs Eureka to generate a regularized reward function and policy. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Walking Globe sim and real environments. In lab settings, we loosely strap the robot horizontally to a center point to prevent robot from ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (IV. METHOD), p. 3 (IV. METHOD), p. 3 (IV. METHOD), p. 4 (IV. METHOD), p. 5 (IV. METHOD), p. 5 (IV. METHOD), objective p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 3 (IV. METHOD), p. 3 (IV. METHOD), p. 5 (IV. METHOD), temporal p. 5 (V. EXPERIMENTAL SETUP), p. 5 (IV. METHOD), p. 6 (V. EXPERIMENTAL SETUP), p. 1 (I. INTRODUCTION), p. 3 (III. PROBLEM SETTING), p. 8 (2) How important is each component of DrEureka?).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
