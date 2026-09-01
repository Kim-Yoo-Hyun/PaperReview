# Method - BEHAVIOR-1K: A Benchmark for Embodied AI with 1,000 Everyday Activities and Realistic Simulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (43 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v205/li23s.html; PDF retrieval source: https://arxiv.org/pdf/2403.09227. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 7 (Method), p. 7 (Method), p. 8 (Method), p. 8 (Method)): We evaluate three different baselines based on state-of-the-art reinforcement learning algorithms (RL) [60]: • RL-VMC, a visuomotor control (from image to low-level joint commands) RL solution based on Soft Actor-Critic ...

## Method Body Digest

- **p. 7 / Method - extractive PDF cue:** We evaluate three different baselines based on state-of-the-art reinforcement learning algorithms (RL) [60]: • RL-VMC, a visuomotor control (from image to low-level joint commands) RL ...
- **p. 7 / Method - extractive PDF cue:** The policy outputs a discrete selection of a primitive applied on an object; • RL-Prim.Hist., a variant of RL-Prim. that takes in the history observations ...
- **p. 8 / Method - extractive PDF cue:** We also evaluate to what extent the simplifications we introduce in physics and actuation (grasping, motion execution) during training impact the performance of RL-Prim. during ...
- **p. 8 / Method - extractive PDF cue:** 6.1), policy failures (i.e., selecting the wrong action primitive) dominate.
- **p. 7 / Method - extractive PDF cue:** All agents are trained with a sparse task success reward without any reward engineering.
- **p. 7 / Method - extractive PDF cue:** The extreme long-horizon in our activities causes the visuomotor control (RL-VMC) policy to fail in all three activities, potentially due to problems such as credit ...
- **p. 8 / Method - extractive PDF cue:** We evaluate two strategies for selecting action primitives in the real world: an optimal policy based on human input, and a vision-based policy (RL-Prim.) trained ...
- **p. 2 / 1 Introduction - extractive PDF cue:** We evaluate state-of-the-art reinforcement learning algorithms [47, 48] in several activities of BEHAVIOR-1K, both with visuomotor control in the original action space, and with action ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** In this work, we present BEHAVIOR-1K, a Benchmark of 1,000 Everyday Household Activities in Virtual, Interactive, and Ecological Environments-the next generation of BEHAVIOR-100 [27].
- **p. 8 / Method - extractive PDF cue:** We also evaluate to what extent the simplifications we introduce in physics and actuation (grasping, motion execution) during training impact the performance of RL-Prim. during ...
- **p. 2 / 1 Introduction - extractive PDF cue:** We hope that the BEHAVIOR-1K benchmark, our survey, and our analysis will serve to support and guide the development of future embodied AI agents and ...

## Source Evidence Cues

- **p. 7 / Method - extractive PDF cue:** We evaluate three different baselines based on state-of-the-art reinforcement learning algorithms (RL) [60]: • RL-VMC, a visuomotor control (from image to low-level joint commands) RL ...
- **p. 7 / Method - extractive PDF cue:** The policy outputs a discrete selection of a primitive applied on an object; • RL-Prim.Hist., a variant of RL-Prim. that takes in the history observations ...
- **p. 8 / Method - extractive PDF cue:** We also evaluate to what extent the simplifications we introduce in physics and actuation (grasping, motion execution) during training impact the performance of RL-Prim. during ...
- **p. 8 / Method - extractive PDF cue:** 6.1), policy failures (i.e., selecting the wrong action primitive) dominate.
- **Detected method headings:** Method (p. 7); Method (p. 8)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | We evaluate three different baselines based on state-of-the-art reinforcement learning algorithms (RL) [60]: • RL-VMC, a visuomotor control (from image to low-level ... | p. 7 (Method), p. 7 (Method) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | The policy outputs a discrete selection of a primitive applied on an object; • RL-Prim.Hist., a variant of RL-Prim. that takes in ... | p. 7 (Method), p. 8 (Method) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | We also evaluate to what extent the simplifications we introduce in physics and actuation (grasping, motion execution) during training impact the performance ... | p. 8 (Method), p. 8 (Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / Method - extractive PDF cue:** All agents are trained with a sparse task success reward without any reward engineering.
- **p. 7 / Method - extractive PDF cue:** The extreme long-horizon in our activities causes the visuomotor control (RL-VMC) policy to fail in all three activities, potentially due to problems such as credit ...
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 7 (Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | policy, outputs, discrete, selection, primitive, applied, object, RL-Prim, Hist, variant, takes, history, observations, steps | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | policy, outputs, discrete, selection, primitive, applied, object, RL-Prim, Hist, variant | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | present, BEHAVIOR-1K, Benchmark, Everyday, Household, Activities, Virtual, Interactive, Ecological, Environments-the | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | agents, trained, sparse, task, success, reward, without, engineering, extreme, long-horizon | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 7 / Method - extractive PDF cue:** The policy outputs a discrete selection of a primitive applied on an object; • RL-Prim.Hist., a variant of RL-Prim. that takes in the history observations ...
- **p. 7 / Method - extractive PDF cue:** We evaluate three different baselines based on state-of-the-art reinforcement learning algorithms (RL) [60]: • RL-VMC, a visuomotor control (from image to low-level joint commands) RL ...
- **p. 8 / Method - extractive PDF cue:** We evaluate two strategies for selecting action primitives in the real world: an optimal policy based on human input, and a vision-based policy (RL-Prim.) trained ...
- **p. 2 / 1 Introduction - extractive PDF cue:** We evaluate state-of-the-art reinforcement learning algorithms [47, 48] in several activities of BEHAVIOR-1K, both with visuomotor control in the original action space, and with action ...
- **p. 8 / Method - extractive PDF cue:** 6.1), policy failures (i.e., selecting the wrong action primitive) dominate.
- **p. 2 / 1 Introduction - extractive PDF cue:** The BEHAVIOR-1K DATASET is a large-scale dataset comprising 1) a commonsense knowledge base for 1,000 activities with definitions in predicate logic (initial and goal conditions), ...
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | We observe that longer-horizon activities are more challenging: while CleanTable can be accomplished by executing the optimal sequence of 6 primitive steps, ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | Memory of observations helps in longer horizon activities (e.g. | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | Memory of observations helps in longer horizon activities (e.g. | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | The policy outputs a discrete selection of a primitive applied on an object; • RL-Prim.Hist., a variant of RL-Prim. that takes in ... | hardware, batch and throughput |

## Training vs Inference

- **p. 8 / Method - extractive PDF cue:** We also evaluate to what extent the simplifications we introduce in physics and actuation (grasping, motion execution) during training impact the performance of RL-Prim. during ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** evaluate, three, different, baselines, state-of-the-art, reinforcement, learning, algorithms, RL-VMC, visuomotor, control, image, low-level, joint, commands, solution, Soft, Actor-Critic, SAC, RL-Prim.
- **Relevant PDF headings:** Method (p. 7); Method (p. 8).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | The survey reveals systematicity in what activities people want robots to do, but more importantly, highlights two key factors that we should ... | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Baseline harness | We evaluate three different baselines based on state-of-the-art reinforcement learning algorithms (RL) [60]: • RL-VMC, a visuomotor control (from image to low-level ... | p. 7 (Method), p. 1 (Abstract) |
| Metric / failure reporting | Table 2: Task success rates across three baseline methods. RL-VMC with end-to-end visuomotor control completely fails to solve any of the activities, ... | p. 7 (Figure/Table caption), p. 8 (Method) |

## Failure and Ablation Link

- **p. 7 / Method - extractive PDF cue:** We include an ablation analysis of the effect of these assumptions and simplifications in our evaluation (see Table 4).
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4: Ablation study of RL-Prim. on the impact of removing the simplifying assumptions of grasping and motion execution during evaluation. We observe a large ...
- **p. 8 / Method - extractive PDF cue:** Realism Task success rate Grasping Full Motion StoreDecoration CollectTrash CleanTable Ë Ë 0.0 ± 0.0 0.0 ± 0.0 0.0 ± 0.0 é Ë 0.46 ± ...
- **p. 5 / C C - extractive PDF cue:** Finally, annotators and researchers also create transition rules, e.g., turning tomatoes and salt into sauces, or requiring sandpaper to remove rust.
- **p. 6 / C C - extractive PDF cue:** Indeed, without these features, over half of BEHAVIOR-1K activities would not be simulatable, highlighting how crucial these features are for capturing everyday activities.
- **p. 7 / Method - extractive PDF cue:** All agents are trained with a sparse task success reward without any reward engineering.
- **p. 1 / Abstract - extractive PDF cue:** BEHAVIOR-1K includes two components, guided and motivated by the results of an extensive survey on ‘what do you want robots to do for you?'.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 7 (Method), p. 7 (Method), p. 8 (Method), p. 8 (Method), objective p. 7 (Method), p. 7 (Method), temporal p. 7 (Method), p. 7 (Method), p. 8 (Method), p. 1 (Abstract), p. 3 (6. Clean a shower).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
