# Method - Goal-VLA: Image-Generative VLMs As Object-Centric World Models Empowering Zero-Shot Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html; PDF retrieval source: https://arxiv.org/pdf/2506.23919. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD)): Algorithm 1 Goal-VLA Execution Framework Require: Initial observation O = (I, D), Language instruction L, Initial End-effector pose Pinit Ensure: Action sequence {a}i 1: procedure GOAL-VLA(O, L) Stage 1: Goal ...

## Method Body Digest

- **p. 3 / III. METHOD - extractive PDF cue:** Algorithm 1 Goal-VLA Execution Framework Require: Initial observation O = (I, D), Language instruction L, Initial End-effector pose Pinit Ensure: Action sequence {a}i 1: procedure ...
- **p. 4 / III. METHOD - extractive PDF cue:** The Low-level Policy takes the current observation O = (I, D) and the mask M as input, then outputs a sequence of actions {a}i to ...
- **p. 4 / III. METHOD - extractive PDF cue:** "Place tomato in pan" Task Description Initial Image (a) Goal State Reasoning World Model Goal Image Goal Depth Synthesized Image Reflector Failure Success Depth-Anything Initial ...
- **p. 3 / III. METHOD - extractive PDF cue:** We then detail the core components, starting with the Goal State Reasoning module, which interprets the user's instruction to generate a visual goal state (Sec.
- **p. 3 / III. METHOD - extractive PDF cue:** Problem Formulation Given a single-view RGBD image observation O = (I ∈ RH×W ×3, D ∈RH×W ×1), and a natural language task description L , ...
- **p. 4 / III. METHOD - extractive PDF cue:** The objective of this module is to compute the rotation R ∈SO(3) and translation t ∈R3 that maps the object from its initial pose to ...
- **p. 4 / III. METHOD - extractive PDF cue:** 2: Overview of the Goal-VLA framework, which decouples the manipulation pipeline into three stages: (a) Goal State Reasoning: A VLM generates a goal image from ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** To summarize, our key contributions are: • We introduce Goal-VLA, a decoupled hierarchical framework that leverages an Image-Generative VLM as a world model to generate ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** To summarize, our key contributions are: • We introduce Goal-VLA, a decoupled hierarchical framework that leverages an Image-Generative VLM as a world model to generate ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** To this end, we propose a decoupled architecture that leverages the VLM as an objectcentric world model.
- **p. 3 / III. METHOD - extractive PDF cue:** The overall workflow of our framework is illustrated conceptually in Figure 2 and detailed procedurally in Algorithm 1.

## Source Evidence Cues

- **p. 3 / III. METHOD - extractive PDF cue:** Algorithm 1 Goal-VLA Execution Framework Require: Initial observation O = (I, D), Language instruction L, Initial End-effector pose Pinit Ensure: Action sequence {a}i 1: procedure ...
- **p. 4 / III. METHOD - extractive PDF cue:** The Low-level Policy takes the current observation O = (I, D) and the mask M as input, then outputs a sequence of actions {a}i to ...
- **p. 4 / III. METHOD - extractive PDF cue:** "Place tomato in pan" Task Description Initial Image (a) Goal State Reasoning World Model Goal Image Goal Depth Synthesized Image Reflector Failure Success Depth-Anything Initial ...
- **p. 3 / III. METHOD - extractive PDF cue:** We then detail the core components, starting with the Goal State Reasoning module, which interprets the user's instruction to generate a visual goal state (Sec.
- **Detected method headings:** III. METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Algorithm 1 Goal-VLA Execution Framework Require: Initial observation O = (I, D), Language instruction L, Initial End-effector pose Pinit Ensure: Action sequence ... | p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | The Low-level Policy takes the current observation O = (I, D) and the mask M as input, then outputs a sequence of ... | p. 4 (III. METHOD), p. 4 (III. METHOD) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | "Place tomato in pan" Task Description Initial Image (a) Goal State Reasoning World Model Goal Image Goal Depth Synthesized Image Reflector Failure ... | p. 4 (III. METHOD), p. 3 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. METHOD - extractive PDF cue:** Problem Formulation Given a single-view RGBD image observation O = (I ∈ RH×W ×3, D ∈RH×W ×1), and a natural language task description L , ...
- **p. 4 / III. METHOD - extractive PDF cue:** The objective of this module is to compute the rotation R ∈SO(3) and translation t ∈R3 that maps the object from its initial pose to ...
- **p. 3 / III. METHOD - extractive PDF cue:** Algorithm 1 Goal-VLA Execution Framework Require: Initial observation O = (I, D), Language instruction L, Initial End-effector pose Pinit Ensure: Action sequence {a}i 1: procedure ...
- **p. 4 / III. METHOD - extractive PDF cue:** 2: Overview of the Goal-VLA framework, which decouples the manipulation pipeline into three stages: (a) Goal State Reasoning: A VLM generates a goal image from ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Algorithm, Goal-VLA, Execution, Framework, Require, Initial, observation, Language, instruction, End-effector, pose, Pinit, Ensure, Action | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Algorithm, Goal-VLA, Execution, Framework, Require, Initial, observation, Language, instruction, End-effector | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | summarize, contributions, introduce, Goal-VLA, decoupled, hierarchical, framework, leverages, Image-Generative, VLM | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Problem, Formulation, Given, single-view, RGBD, image, observation, natural, language, task | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. METHOD - extractive PDF cue:** Algorithm 1 Goal-VLA Execution Framework Require: Initial observation O = (I, D), Language instruction L, Initial End-effector pose Pinit Ensure: Action sequence {a}i 1: procedure ...
- **p. 4 / III. METHOD - extractive PDF cue:** "Place tomato in pan" Task Description Initial Image (a) Goal State Reasoning World Model Goal Image Goal Depth Synthesized Image Reflector Failure Success Depth-Anything Initial ...
- **p. 4 / III. METHOD - extractive PDF cue:** The Low-level Policy takes the current observation O = (I, D) and the mask M as input, then outputs a sequence of actions {a}i to ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** To summarize, our key contributions are: • We introduce Goal-VLA, a decoupled hierarchical framework that leverages an Image-Generative VLM as a world model to generate ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** The end-to-end VLA approach is to train a single, largescale policy to map visual and language inputs to low-level robot actions directly.
- **p. 3 / III. METHOD - extractive PDF cue:** Problem Formulation Given a single-view RGBD image observation O = (I ∈ RH×W ×3, D ∈RH×W ×1), and a natural language task description L , ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** In contrast, while dense visual representations like goal images provide rich information [20]-[23], they typically require the low-level policy to be explicitly trained on paired ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Algorithm 1 Goal-VLA Execution Framework Require: Initial observation O = (I, D), Language instruction L, Initial End-effector pose Pinit Ensure: Action sequence ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | The overall workflow of our framework is illustrated conceptually in Figure 2 and detailed procedurally in Algorithm 1. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | We conduct 10 trials for each task, with detailed results presented in Table III and Figure 5. | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Algorithm, Goal-VLA, Execution, Framework, Require, Initial, observation, Language, instruction, End-effector, pose, Pinit, Ensure, Action, sequence, procedure, Stage, Goal, State, Reasoning.
- **Relevant PDF headings:** III. METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Q3: Can our framework generalize across diverse environments, tasks, object categories, and robot embodiments? | p. 5 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT) |
| Action / skill decoding | In this section, we conduct comprehensive experiments and analyses to answer the following key questions: Q1: How well does our proposed method ... | p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT) |
| Receding execution / feedback | Our method, Goal-VLA, achieves a remarkable average success rate of 59.9%, significantly outperforming all baselines across a diverse set of eight manipulation ... | p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 4: Ablation Study. The performance of our full model ("World Model w/ Instruction & max 3 Reflection"), shown by the purple line, surpasses all ...
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** Ablation Study (Q2) We perform an ablation study to validate the contributions of our two key components: Input Enhancement and the Reflection-through-Synthesis process.
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** In all experiments, the robot starts without holding any object at the beginning of each trial.
- **p. 7 / IV. EXPERIMENT - extractive PDF cue:** These results demonstrate that both components are critical and complementary, confirming their effectiveness and answering our second research question (Q2).
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** Reflection's Necessary: Figure 3 highlights a typical failure mode of image generation.
- **p. 7 / IV. EXPERIMENT - extractive PDF cue:** Failures originating from the Spatial Grounding module are the primary obstacle in several precision-demanding tasks.
- **p. 7 / IV. EXPERIMENT - extractive PDF cue:** Failure Cases Analysis In our real-world experiments, we observe several typical failure modes as different tasks place varying demands on each module of our framework.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), objective p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), temporal p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
