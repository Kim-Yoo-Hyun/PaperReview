# Method - Benchmarking Safe Exploration in Deep Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openai.com/index/benchmarking-safe-exploration-in-deep-reinforcement-learning/; PDF retrieval source: https://cdn.openai.com/safexp-short.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (Abstract), p. 3 (1 Introduction)): First, building on a wide range of prior work on safe reinforcement learning, we propose to standardize constrained RL as the main formalism for safe exploration.

## Method Body Digest

- **p. 1 / Abstract - extractive PDF cue:** First, building on a wide range of prior work on safe reinforcement learning, we propose to standardize constrained RL as the main formalism for safe ...
- **p. 2 / 1 Introduction - extractive PDF cue:** While "sim-to-real" transfer learning algorithms may mitigate this issue, we expect that in problems centered on AI-human interaction or very complex systems, challenges in building ...
- **p. 2 / 1 Introduction - extractive PDF cue:** We recommend a protocol for evaluating constrained RL algorithms on Safety Gym environments based on three metrics: task performance of the final policy, constraint satisfaction ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Our baseline algorithms include Trust Region Policy Optimization (TRPO) [Schulman et al., 2015] and Proximal Policy Optimization (PPO) [Schulman et al., 2017] in their original ...
- **p. 1 / Abstract - extractive PDF cue:** While it is currently typical to train RL agents mostly or entirely in simulation, where safety concerns are minimal, we anticipate that challenges in simulating ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Additionally, we include Constrained Policy Optimization (CPO) [Achiam et al., 2017], a constrained form of TRPO that calculates a penalty coefficient from scratch at each ...
- **p. 2 / 1 Introduction - extractive PDF cue:** These are expressed via a reward function and a set of auxiliary cost functions respectively.
- **p. 1 / 1 Introduction - extractive PDF cue:** The fundamental principle of RL is that an agent, the AI system, tries to maximize a reward signal by trial and error.

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** To address the gap, we present Safety Gym: a set of tools for accelerating safe exploration research.
- **p. 2 / 1 Introduction - extractive PDF cue:** Towards standardizing safety specifications: Based on a range of prior work, we propose to standardize constrained RL [Altman, 1999] as the main formalism for incorporating ...
- **p. 1 / 1 Introduction - extractive PDF cue:** However, for many problems simulators will either not be available or high-enough fidelity for RL to learn behaviors that succeed in the real environment. ∗equal ...

## Source Evidence Cues

- **p. 1 / Abstract - extractive PDF cue:** First, building on a wide range of prior work on safe reinforcement learning, we propose to standardize constrained RL as the main formalism for safe ...
- **p. 2 / 1 Introduction - extractive PDF cue:** While "sim-to-real" transfer learning algorithms may mitigate this issue, we expect that in problems centered on AI-human interaction or very complex systems, challenges in building ...
- **p. 2 / 1 Introduction - extractive PDF cue:** We recommend a protocol for evaluating constrained RL algorithms on Safety Gym environments based on three metrics: task performance of the final policy, constraint satisfaction ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Our baseline algorithms include Trust Region Policy Optimization (TRPO) [Schulman et al., 2015] and Proximal Policy Optimization (PPO) [Schulman et al., 2017] in their original ...
- **p. 1 / Abstract - extractive PDF cue:** While it is currently typical to train RL agents mostly or entirely in simulation, where safety concerns are minimal, we anticipate that challenges in simulating ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Additionally, we include Constrained Policy Optimization (CPO) [Achiam et al., 2017], a constrained form of TRPO that calculates a penalty coefficient from scratch at each ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | First, building on a wide range of prior work on safe reinforcement learning, we propose to standardize constrained RL as the main ... | p. 1 (Abstract), p. 2 (1 Introduction) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | While "sim-to-real" transfer learning algorithms may mitigate this issue, we expect that in problems centered on AI-human interaction or very complex systems, ... | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | We recommend a protocol for evaluating constrained RL algorithms on Safety Gym environments based on three metrics: task performance of the final ... | p. 2 (1 Introduction), p. 3 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1 Introduction - extractive PDF cue:** These are expressed via a reward function and a set of auxiliary cost functions respectively.
- **p. 1 / 1 Introduction - extractive PDF cue:** The fundamental principle of RL is that an agent, the AI system, tries to maximize a reward signal by trial and error.
- **p. 2 / 1 Introduction - extractive PDF cue:** We recommend a protocol for evaluating constrained RL algorithms on Safety Gym environments based on three metrics: task performance of the final policy, constraint satisfaction ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Our baseline algorithms include Trust Region Policy Optimization (TRPO) [Schulman et al., 2015] and Proximal Policy Optimization (PPO) [Schulman et al., 2017] in their original ...
- **p. 1 / 1 Introduction - extractive PDF cue:** RL is suitable for any problem where it is easier to evaluate behaviors (by computing a reward function) than it is to generate optimal behaviors ...
- **p. 3 / 1 Introduction - extractive PDF cue:** The tools used to build Safety Gym allow the easy creation of new environments with different layout distributions, including combinations of constraints not present in ...
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | recommend, protocol, evaluating, constrained, algorithms, Safety, Gym, environments, three, metrics, task, performance, final, policy | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | recommend, protocol, evaluating, constrained, algorithms, Safety, Gym, environments, three, metrics | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | address, present, Safety, Gym, tools, accelerating, safe, exploration, research, Towards | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | expressed, reward, function, auxiliary, cost, functions, respectively, fundamental, principle, agent | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive PDF cue:** We recommend a protocol for evaluating constrained RL algorithms on Safety Gym environments based on three metrics: task performance of the final policy, constraint satisfaction ...
- **p. 1 / Abstract - extractive PDF cue:** While it is currently typical to train RL agents mostly or entirely in simulation, where safety concerns are minimal, we anticipate that challenges in simulating ...
- **p. 2 / 1 Introduction - extractive PDF cue:** While "sim-to-real" transfer learning algorithms may mitigate this issue, we expect that in problems centered on AI-human interaction or very complex systems, challenges in building ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Additionally, we include Constrained Policy Optimization (CPO) [Achiam et al., 2017], a constrained form of TRPO that calculates a penalty coefficient from scratch at each ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Towards providing useful baselines: To make Safety Gym relevant out-of-the-box and to partially clarify state-of-the-art in safe exploration, we benchmark several existing constrained and unconstrained ...
- **p. 1 / Abstract - extractive PDF cue:** First, building on a wide range of prior work on safe reinforcement learning, we propose to standardize constrained RL as the main formalism for safe ...
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | The quantity we aim to constrain. • The average cost over the entirety of training, ρc (the sum of all costs divided ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | That is, in our experiments, we use the finite horizon undiscounted return and cumulative cost formulations, and furthermore, we fold all safety ... | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | As a result, we consider memory-based and model-based RL approaches to be particularly interesting here. | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | Point and Car agents were trained for 107 steps, and Doggo agents were trained for 108 steps. | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / Abstract - extractive PDF cue:** First, building on a wide range of prior work on safe reinforcement learning, we propose to standardize constrained RL as the main formalism for safe ...
- **p. 2 / 1 Introduction - extractive PDF cue:** While "sim-to-real" transfer learning algorithms may mitigate this issue, we expect that in problems centered on AI-human interaction or very complex systems, challenges in building ...
- **p. 2 / 1 Introduction - extractive PDF cue:** We recommend a protocol for evaluating constrained RL algorithms on Safety Gym environments based on three metrics: task performance of the final policy, constraint satisfaction ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Our baseline algorithms include Trust Region Policy Optimization (TRPO) [Schulman et al., 2015] and Proximal Policy Optimization (PPO) [Schulman et al., 2017] in their original ...
- **p. 1 / Abstract - extractive PDF cue:** While it is currently typical to train RL agents mostly or entirely in simulation, where safety concerns are minimal, we anticipate that challenges in simulating ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Additionally, we include Constrained Policy Optimization (CPO) [Achiam et al., 2017], a constrained form of TRPO that calculates a penalty coefficient from scratch at each ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** First, building, wide, range, prior, safe, reinforcement, learning, standardize, constrained, main, formalism, exploration, While, sim-to-real, transfer, algorithms, mitigate, issue, expect.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | SG6 has at least one environment for each task, robot, and level. | p. 15 (5 Experiments), p. 21 (5.3 Results) |
| Baseline harness | Advancing SOTA on Safety Gym: Our baseline results for constrained RL indicate a need for stronger and/or better-tuned algorithms to succeed on ... | p. 21 (5.3 Results), p. 14 (5 Experiments) |
| Metric / failure reporting | By success, we mean attaining improvements simultaneously along both the episodic return axis and the constraint regret axis, while still producing a ... | p. 21 (5.3 Results), p. 14 (5 Experiments) |

## Failure and Ablation Link

- **p. 16 / 5.3 Results - extractive PDF cue:** These learning curves depict the metrics Jr(θ), Jc(θ), and ρc(θ) without normalization, and show the absolute performance of each algorithm.
- **p. 16 / 5.3 Results - extractive PDF cue:** [2017]. • Lagrangian methods are able to find constraint-satisfying policies that attain nontrivial returns in several of the Point environments, demonstrating that when controlling for ...
- **p. 21 / 5.3 Results - extractive PDF cue:** We note that standard model-free RL approaches without replay buffers are fundamentally limited in their ability to minimize constraint regret: they must continually experience unsafe ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Figure 3: Constraint elements used in our environments. currently-highlighted button, which is the goal button. After the agent presses the correct button, the environment will ...
- **p. 16 / 5 Experiments - extractive PDF cue:** [2017], we omit the learned failure predictor they used for cost shaping.
- **p. 21 / 5.3 Results - extractive PDF cue:** There are a number of avenues we consider promising for future work.
- **p. 12 / Figure/Table caption - extractive PDF cue:** Figure 6: Diversity of generated layouts for the Safexp-PointPush2-v0 env. 4.2 Safety Gym Benchmark Suite Safety Gym ships with a suite of pre-configured benchmark environments, ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (Abstract), p. 3 (1 Introduction), objective p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction), temporal p. 14 (5 Experiments), p. 14 (5 Experiments), p. 16 (5 Experiments), p. 16 (5 Experiments), p. 21 (5.3 Results), p. 21 (5.3 Results).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
