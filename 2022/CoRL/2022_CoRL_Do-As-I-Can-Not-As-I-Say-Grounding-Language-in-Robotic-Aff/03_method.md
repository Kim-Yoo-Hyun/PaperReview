# Method - Do As I Can, Not As I Say: Grounding Language in Robotic Affordances

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (34 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2204.01691; PDF retrieval source: https://arxiv.org/pdf/2204.01691. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 1 (Abstract), p. 2 (2 Preliminaries), p. 5 (2 Preliminaries), p. 6 (2 Preliminaries), p. 2 (2 Preliminaries), p. 4 (2 Preliminaries)): We propose to provide real-world grounding by means of pretrained skills, which are used to constrain the model to propose natural language actions that are both feasible and contextually appropriate.

## Method Body Digest

- **p. 1 / Abstract - extractive PDF cue:** We propose to provide real-world grounding by means of pretrained skills, which are used to constrain the model to propose natural language actions that are ...
- **p. 2 / 2 Preliminaries - extractive PDF cue:** Recent breakthroughs initiated by neural network-based Attention architectures [2] have enabled efficient scaling of so-called Large Language Models (LLMs).
- **p. 5 / 2 Preliminaries - extractive PDF cue:** To learn a language-conditioned RL policy, we use MT-Opt [14] in the Everyday Robots simulator using RetinaGAN sim-to-real transfer [16].
- **p. 6 / 2 Preliminaries - extractive PDF cue:** We use a network architecture similar to MT-Opt (shown in Fig.
- **p. 2 / 2 Preliminaries - extractive PDF cue:** We use temporal-difference-based (TD) reinforcement learning to accomplish this goal.
- **p. 4 / 2 Preliminaries - extractive PDF cue:** With this approach, we are able to effectively extract knowledge from the language model, but it leaves a major issue: while the decoding of the ...
- **p. 5 / 2 Preliminaries - extractive PDF cue:** As mentioned previously, for skill specification we use a set of short, natural language descriptions that are represented as language model embeddings.
- **p. 3 / 2 Preliminaries - extractive PDF cue:** We leverage that intuition in our setup and express affordances via value functions of sparse reward tasks.

## Design Rationale

- **p. 1 / Abstract - extractive PDF cue:** We evaluate our method on a number of real-world robotic tasks, where we show the need for real-world grounding and that this approach is capable ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Our method, SayCan, extracts and leverages the knowledge within LLMs in physically-grounded tasks.
- **p. 1 / Abstract - extractive PDF cue:** We propose to provide real-world grounding by means of pretrained skills, which are used to constrain the model to propose natural language actions that are ...

## Source Evidence Cues

- **p. 1 / Abstract - extractive PDF cue:** We propose to provide real-world grounding by means of pretrained skills, which are used to constrain the model to propose natural language actions that are ...
- **p. 2 / 2 Preliminaries - extractive PDF cue:** Recent breakthroughs initiated by neural network-based Attention architectures [2] have enabled efficient scaling of so-called Large Language Models (LLMs).
- **p. 5 / 2 Preliminaries - extractive PDF cue:** To learn a language-conditioned RL policy, we use MT-Opt [14] in the Everyday Robots simulator using RetinaGAN sim-to-real transfer [16].
- **p. 6 / 2 Preliminaries - extractive PDF cue:** We use a network architecture similar to MT-Opt (shown in Fig.
- **p. 2 / 2 Preliminaries - extractive PDF cue:** We use temporal-difference-based (TD) reinforcement learning to accomplish this goal.
- **p. 4 / 2 Preliminaries - extractive PDF cue:** With this approach, we are able to effectively extract knowledge from the language model, but it leaves a major issue: while the decoding of the ...
- **p. 5 / 2 Preliminaries - extractive PDF cue:** As mentioned previously, for skill specification we use a set of short, natural language descriptions that are represented as language model embeddings.
- **Detected method headings:** C.1 RL and BC Policy Architecture (p. 19); C.2 RL and BC Policy Training (p. 20); C.3 RL and BC Policy Evaluations (p. 21)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | We propose to provide real-world grounding by means of pretrained skills, which are used to constrain the model to propose natural language ... | p. 1 (Abstract), p. 2 (2 Preliminaries) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Recent breakthroughs initiated by neural network-based Attention architectures [2] have enabled efficient scaling of so-called Large Language Models (LLMs). | p. 2 (2 Preliminaries), p. 5 (2 Preliminaries) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | To learn a language-conditioned RL policy, we use MT-Opt [14] in the Everyday Robots simulator using RetinaGAN sim-to-real transfer [16]. | p. 5 (2 Preliminaries), p. 6 (2 Preliminaries) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 2 Preliminaries - extractive PDF cue:** We leverage that intuition in our setup and express affordances via value functions of sparse reward tasks.
- **p. 3 / 2 Preliminaries - extractive PDF cue:** In RL terminology, p(cπ/s, ℓπ) is the value function for the skill if we take the reward to be 1 for successful completion and 0 ...
- **p. 4 / 2 Preliminaries - extractive PDF cue:** In order to amortize the cost of training many skills, we utilize multi-task BC and multitask RL, respectively, where instead of training a separate policy ...
- **p. 5 / 2 Preliminaries - extractive PDF cue:** To complete the description of the underlying MDP that we consider, we provide the reward function as well as the skill specification that is used ...
- **p. 2 / 2 Preliminaries - extractive PDF cue:** In particular, we define a Markov decision process (MDP) M = (S, A, P, R, γ), where S and A are state and action spaces, ...
- **p. 5 / 2 Preliminaries - extractive PDF cue:** Algorithm 1 SayCan Given: A high level instruction i, state s0, and a set of skills Π and their language descriptions ℓΠ 1: n = ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 3 (2 Preliminaries).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | goal, methods, learn, state, state-action, value, functions, Q-function, represents, discounted, rewards, when, starting, action | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | goal, methods, learn, state, state-action, value, functions, Q-function, represents, discounted | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | evaluate, number, real-world, robotic, tasks, where, need, grounding, capable, completing | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | leverage, intuition, setup, express, affordances, value, functions, sparse, reward, tasks | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 2 Preliminaries - extractive PDF cue:** The goal of TD methods is to learn state or state-action value functions (Q-function) Qπ(s, a), which represents the discounted sum of rewards when starting ...
- **p. 3 / 2 Preliminaries - extractive PDF cue:** Therefore, to adapt language models to our problem statement, we must somehow inform them that we specifically want the high-level instruction to be broken down ...
- **p. 5 / 2 Preliminaries - extractive PDF cue:** Algorithm 1 SayCan Given: A high level instruction i, state s0, and a set of skills Π and their language descriptions ℓΠ 1: n = ...
- **p. 6 / 2 Preliminaries - extractive PDF cue:** The instructions span multiple axes of variation: time-horizon (from single primitives to 10+ in a row), language complexity (from structured language to fully crowd-sourced requests), ...
- **p. 2 / 2 Preliminaries - extractive PDF cue:** Our goal is to be able to accurately predict whether a skill (given by a language command) is feasible at a current state.
- **p. 5 / 2 Preliminaries - extractive PDF cue:** The success of language command execution is rated by humans where the raters are given a video of the robot performing the skill, together with ...
- **p. 2 / 2 Preliminaries - extractive PDF cue:** In particular, we define a Markov decision process (MDP) M = (S, A, P, R, γ), where S and A are state and action spaces, ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Furthermore, this combination results in a fully explainable sequence of steps that the robot will execute to accomplish an instruction - an ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | (starting from different completion stages) Crowd-Sourced 15 Queries in unstructured formats My favorite drink is redbull, bring one Long-Horizon 15 Long-horizon queries ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / Abstract - extractive PDF cue:** We propose to provide real-world grounding by means of pretrained skills, which are used to constrain the model to propose natural language actions that are ...
- **p. 3 / 2 Preliminaries - extractive PDF cue:** However, this is not enough to fully constrain the output to admissible primitive skills for an embodied agent, and indeed at times it can produce ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** provide, real-world, grounding, means, pretrained, skills, constrain, model, natural, language, actions, feasible, contextually, appropriate, Recent, breakthroughs, initiated, neural, network-based, Attention.
- **Relevant PDF headings:** C.1 RL and BC Policy Architecture (p. 19); C.2 RL and BC Policy Training (p. 20); C.3 RL and BC Policy Evaluations (p. 21).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | The robot interacts with a large portion of the kitchen environment and successfully performs sequences of manipulation and navigation skills. | p. 7 (5.1 Results), p. 7 (5.1 Results) |
| Action / skill decoding | We also find that PaLM outperforms FLAN. | p. 9 (5.1 Results), p. 9 (5.1 Results) |
| Receding execution / feedback | Table 2: Success rates of instructions by family. PaLM-SayCan achieves a planning success rate of 84% and execution success rate of 74% ... | p. 9 (Figure/Table caption), p. 9 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / 5.1 Results - extractive PDF cue:** These tasks require PaLMSayCan to plan many steps without error and for the robot to navigate and interact with a significant portion of the kitchen.
- **p. 8 / 5.1 Results - extractive PDF cue:** To study the importance of the LLM, we conduct two ablation experiments using the language-conditioned policy (see Sections 4-4).
- **p. 8 / 5.1 Results - extractive PDF cue:** We compare PaLM-SayCan to (1) No VF, which removes the value function grounding (i.e., choosing the maximum language score skill) and to (2) Generative, which ...
- **p. 9 / 5.1 Results - extractive PDF cue:** Finally we show the system can work with multilingual queries, without explicitly being designed to.
- **p. 10 / 5.1 Results - extractive PDF cue:** Human: Can you bring a fruit-flavored drink without caffeine?
- **p. 29 / Figure/Table caption - extractive PDF cue:** Table 6: Ablations over the size of the LLM. Compared only with the generative outputs (no value function) with USE embeddings [15]. Listing 2: Prompt ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: LLMs have not interacted with their environment and observed the outcome of their responses, and thus are not grounded in the world. SayCan ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 1 (Abstract), p. 2 (2 Preliminaries), p. 5 (2 Preliminaries), p. 6 (2 Preliminaries), p. 2 (2 Preliminaries), p. 4 (2 Preliminaries), objective p. 3 (2 Preliminaries), p. 3 (2 Preliminaries), p. 4 (2 Preliminaries), p. 5 (2 Preliminaries), p. 2 (2 Preliminaries), p. 5 (2 Preliminaries), temporal p. 2 (1 Introduction), p. 6 (2 Preliminaries), p. 7 (5.1 Results), p. 7 (5.1 Results), p. 1 (Abstract), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
