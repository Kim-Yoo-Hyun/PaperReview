# Method - Habitat: A Platform for Embodied AI Research

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1904.01201; PDF retrieval source: https://arxiv.org/pdf/1904.01201. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1. Introduction), p. 5 (4. PointGoal Navigation at Scale), p. 4 (3. Habitat Platform), p. 6 (4. PointGoal Navigation at Scale), p. 6 (4. PointGoal Navigation at Scale), p. 1 (Abstract)): We propose a unified embodied agent stack with the Habitat platform, including generic dataset support, a highly performant simulator (Habitat-Sim), and a flexible API (Habitat-API) allowing the definition and evaluation ...

## Method Body Digest

- **p. 2 / 1. Introduction - extractive body cue:** We propose a unified embodied agent stack with the Habitat platform, including generic dataset support, a highly performant simulator (Habitat-Sim), and a flexible API (Habitat-API) ...
- **p. 5 / 4. PointGoal Navigation at Scale - extractive body cue:** In Habitat and our experiments, we use a more realistic collision model - the agent navigates in a continuous state space4 and motion can produce ...
- **p. 4 / 3. Habitat Platform - extractive body cue:** RGB, depth, contact, GPS, compass sensors) attached to each agent. - Scenario and task API: allows portable definition of tasks and their evaluation protocols. - ...
- **p. 6 / 4. PointGoal Navigation at Scale - extractive body cue:** The agent calls the stop action when within 0.2m of the goal. - RL (PPO) is an agent trained with reinforcement learning, specifically proximal policy ...
- **p. 6 / 4. PointGoal Navigation at Scale - extractive body cue:** When training learning-based agents, we first divide the scenes in the training set equally among 8 (Gibson), 6 (Matterport3D) concurrently running simulator worker threads.
- **p. 1 / Abstract - extractive body cue:** Specifically, Habitat consists of: (i) Habitat-Sim: a flexible, high-performance 3D simulator with configurable agents, sensors, and generic 3D dataset handling.
- **p. 2 / 1. Introduction - extractive body cue:** Habitat-API: a modular high-level library for endto-end development of embodied AI algorithms - defining embodied AI tasks (e.g. navigation, instruction following, question answering), configuring and ...
- **p. 6 / 4. PointGoal Navigation at Scale - extractive body cue:** Let rt denote the reward at timestep t, dt be the geodesic distance to goal at timestep t, s a success reward and λ a ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Specifically, Habitat consists of the following: 1.
- **p. 2 / 1. Introduction - extractive body cue:** We propose a unified embodied agent stack with the Habitat platform, including generic dataset support, a highly performant simulator (Habitat-Sim), and a flexible API (Habitat-API) ...
- **p. 1 / Abstract - extractive body cue:** We present Habitat, a platform for research in embodied artificial intelligence (AI).

## Source Evidence Cues

- **p. 2 / 1. Introduction - extractive body cue:** We propose a unified embodied agent stack with the Habitat platform, including generic dataset support, a highly performant simulator (Habitat-Sim), and a flexible API (Habitat-API) ...
- **p. 5 / 4. PointGoal Navigation at Scale - extractive body cue:** In Habitat and our experiments, we use a more realistic collision model - the agent navigates in a continuous state space4 and motion can produce ...
- **p. 4 / 3. Habitat Platform - extractive body cue:** RGB, depth, contact, GPS, compass sensors) attached to each agent. - Scenario and task API: allows portable definition of tasks and their evaluation protocols. - ...
- **p. 6 / 4. PointGoal Navigation at Scale - extractive body cue:** The agent calls the stop action when within 0.2m of the goal. - RL (PPO) is an agent trained with reinforcement learning, specifically proximal policy ...
- **p. 6 / 4. PointGoal Navigation at Scale - extractive body cue:** When training learning-based agents, we first divide the scenes in the training set equally among 8 (Gibson), 6 (Matterport3D) concurrently running simulator worker threads.
- **p. 1 / Abstract - extractive body cue:** Specifically, Habitat consists of: (i) Habitat-Sim: a flexible, high-performance 3D simulator with configurable agents, sensors, and generic 3D dataset handling.
- **p. 2 / 1. Introduction - extractive body cue:** Habitat-API: a modular high-level library for endto-end development of embodied AI algorithms - defining embodied AI tasks (e.g. navigation, instruction following, question answering), configuring and ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | We propose a unified embodied agent stack with the Habitat platform, including generic dataset support, a highly performant simulator (Habitat-Sim), and a ... | p. 2 (1. Introduction), p. 5 (4. PointGoal Navigation at Scale) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | In Habitat and our experiments, we use a more realistic collision model - the agent navigates in a continuous state space4 and ... | p. 5 (4. PointGoal Navigation at Scale), p. 4 (3. Habitat Platform) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | RGB, depth, contact, GPS, compass sensors) attached to each agent. - Scenario and task API: allows portable definition of tasks and their ... | p. 4 (3. Habitat Platform), p. 6 (4. PointGoal Navigation at Scale) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3. Habitat Platform - extractive body cue:** RGB, depth, contact, GPS, compass sensors) attached to each agent. - Scenario and task API: allows portable definition of tasks and their evaluation protocols. - ...
- **p. 6 / 4. PointGoal Navigation at Scale - extractive body cue:** Let rt denote the reward at timestep t, dt be the geodesic distance to goal at timestep t, s a success reward and λ a ...
- **p. 6 / 4. PointGoal Navigation at Scale - extractive body cue:** All models were trained with the following reward function: rt = ( s + dt-1 -dt + λ if goal is reached dt-1 -dt + ...
- **p. 1 / 1. Introduction - extractive body cue:** While there has been significant progress in the vision and language communities thanks to recent advances in deep representations [14, 11], much of this progress ...
- **p. 2 / 1. Introduction - extractive body cue:** Datasets have been a key driver of progress in computer vision, NLP, and other areas of AI [10, 18, 4, 1].
- **p. 2 / 1. Introduction - extractive body cue:** In the context of embodied AI, simulators help overcome the aforementioned challenges - they can run orders of magnitude faster than real-time and can be ...
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 6 (4. PointGoal Navigation at Scale).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | RGB, depth, contact, GPS, compass, sensors, attached, agent, Scenario, task, API, allows, portable, definition | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | RGB, depth, contact, GPS, compass, sensors, attached, agent, Scenario, task | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | Specifically, Habitat, consists, following, unified, embodied, agent, stack, platform, including | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | RGB, depth, contact, GPS, compass, sensors, attached, agent, Scenario, task | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3. Habitat Platform - extractive body cue:** RGB, depth, contact, GPS, compass sensors) attached to each agent. - Scenario and task API: allows portable definition of tasks and their evaluation protocols. - ...
- **p. 6 / 4. PointGoal Navigation at Scale - extractive body cue:** The agent calls the stop action when within 0.2m of the goal. - RL (PPO) is an agent trained with reinforcement learning, specifically proximal policy ...
- **p. 1 / 1. Introduction - extractive body cue:** And if so, bring it to me.' In order to be successful, such a robot would need a range of skills - visual perception (to ...
- **p. 4 / 3. Habitat Platform - extractive body cue:** Setting up an embodied task involves specifying observations that may be used by the agent(s), using environment information provided by the simulator, and connecting the ...
- **p. 6 / 4. PointGoal Navigation at Scale - extractive body cue:** We do not hardcode the stop action to retain generality and allow for comparison with future work that does not assume GPS inputs.
- **p. 5 / 4. PointGoal Navigation at Scale - extractive body cue:** This task is ostensibly simple to define - an agent is initialized at a random starting position and orientation in an environment and asked to ...
- **p. 1 / 1. Introduction - extractive body cue:** The embodiment hypothesis is the idea that intelligence emerges in the interaction of an agent with an environment and as a result of sensorimotor activity.
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | One conspicuous underspecification in the PointGoal task [2] is whether the goal coordinates are static (i.e. provided once at the start of ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | Habitat-Sim is fast - when rendering a scene from Matterport3D, it achieves several thousand frames per second (fps) running single-threaded, and can ... | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | Currently, frames rendered by Habitat-Sim are exposed as Python tensors through shared memory. | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | Habitat-Sim is fast - when rendering a scene from Matterport3D, it achieves several thousand frames per second (fps) running single-threaded, and can ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1. Introduction - extractive body cue:** We propose a unified embodied agent stack with the Habitat platform, including generic dataset support, a highly performant simulator (Habitat-Sim), and a flexible API (Habitat-API) ...
- **p. 4 / 3. Habitat Platform - extractive body cue:** RGB, depth, contact, GPS, compass sensors) attached to each agent. - Scenario and task API: allows portable definition of tasks and their evaluation protocols. - ...
- **p. 6 / 4. PointGoal Navigation at Scale - extractive body cue:** The agent calls the stop action when within 0.2m of the goal. - RL (PPO) is an agent trained with reinforcement learning, specifically proximal policy ...
- **p. 6 / 4. PointGoal Navigation at Scale - extractive body cue:** When training learning-based agents, we first divide the scenes in the training set equally among 8 (Gibson), 6 (Matterport3D) concurrently running simulator worker threads.
- **p. 2 / 1. Introduction - extractive body cue:** Habitat-API: a modular high-level library for endto-end development of embodied AI algorithms - defining embodied AI tasks (e.g. navigation, instruction following, question answering), configuring and ...
- **p. 4 / 3. Habitat Platform - extractive body cue:** RGB, depth, contact, GPS, compass sensors) attached to each agent. - Scenario and task API: allows portable definition of tasks and their evaluation protocols. - ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** unified, embodied, agent, stack, Habitat, platform, including, generic, dataset, support, highly, performant, simulator, Habitat-Sim, flexible, API, Habitat-API, allowing, definition, evaluation.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | In contrast, RGB sensors provide a high-dimensional complex signal that may be prone to overfitting to train environments due to the variety ... | p. 7 (5. Results and Findings), p. 7 (5. Results and Findings) |
| Baseline harness | Figure 3: Average SPL of agents on the val set over the course of training. Previous work [20, 16] has analyzed performance ... | p. 7 (Figure/Table caption), p. 7 (5. Results and Findings) |
| Metric / failure reporting | Interestingly, RGB agents do not significantly outperform Blind agents; we hypothesize because both are equipped with GPS sensors. | p. 7 (5. Results and Findings), p. 8 (5. Results and Findings) |

## Failure and Ablation Link

- **p. 9 / 7. Future Work - extractive body cue:** Another planned avenue of future work involves procedural generation of 3D environments by leveraging a combination of 3D reconstruction and virtual object datasets.
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 10: Average number of collisions during successful navi- gation episodes for the different sensory configurations of the RL (PPO) baseline agent on test set ...
- **p. 7 / 5. Results and Findings - extractive body cue:** SLAM [20] does not require training and thus has a constant performance (0.59 on Gibson, 0.42 on Matterport3D).
- **p. 8 / 5. Results and Findings - extractive body cue:** RGB and RGBD agents suffer a significant performance degradation, while the Blind agent is least affected (as we would expect).
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 7: Performance of Habitat-Sim under different sensor frame memory transfer strategies for increasing image resolution. We see that ‘GPU->GPU' is unaffected by image resolution ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1. Introduction), p. 5 (4. PointGoal Navigation at Scale), p. 4 (3. Habitat Platform), p. 6 (4. PointGoal Navigation at Scale), p. 6 (4. PointGoal Navigation at Scale), p. 1 (Abstract), objective p. 4 (3. Habitat Platform), p. 6 (4. PointGoal Navigation at Scale), p. 6 (4. PointGoal Navigation at Scale), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), temporal p. 5 (4. PointGoal Navigation at Scale), p. 1 (Abstract), p. 3 (2. Related Work), p. 3 (2. Related Work), p. 4 (3. Habitat Platform), p. 6 (4. PointGoal Navigation at Scale).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
