# Method - PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (63 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=T5QLRRHyL1; PDF retrieval source: https://openreview.net/pdf/4bb6ff694eaca45e88773722cf73178602665bfd.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 11 (Method), p. 11 (Method), p. 10 (Method), p. 10 (Method), p. 35 (A.10.2 Implementation Details), p. 32 (A.9 Implementation Details for ReAct Agents)): We also measure exploration efficiency in human-in-the-loop, by measuring the steps taken to pick the first object, and extraneous effort, indicating actions that were not useful for task completion.

## Method Body Digest

- **p. 11 / Method - extractive PDF cue:** We also measure exploration efficiency in human-in-the-loop, by measuring the steps taken to pick the first object, and extraneous effort, indicating actions that were not ...
- **p. 11 / Method - extractive PDF cue:** This reflects that smaller models with faster inference can improve human experience in real-world deployment.
- **p. 10 / Method - extractive PDF cue:** The goal of these experiments is to study multi-user dynamics at PARTNR tasks, and see if multiple humans collaborating are more efficient than single human.
- **p. 10 / Method - extractive PDF cue:** Finally, we run a human-AI experiment where a human participant collaborates with a robot controlled by an LLM (using the ReAct and Finetuned models from ...
- **p. 35 / A.10.2 Implementation Details - extractive PDF cue:** We train the model to predict, for every example, the action taken by the agent, which corresponds to the text after the </reserved_special_token_0>/ token.
- **p. 32 / A.9 Implementation Details for ReAct Agents - extractive PDF cue:** The finetuned model based on Llama-3.1-8B required an average of 0.53s per planning step.
- **p. 32 / A.9 Implementation Details for ReAct Agents - extractive PDF cue:** For all experiments, LLM inferrence is performed on two Nvidia A100 GPUs using the gpt-fast inference engine PyTorch (2023).
- **p. 10 / Method - extractive PDF cue:** This highlights the limitations of LLMs in reasoning about agent capabilities and following strict ordering constraints.

## Design Rationale

- **p. 1 / 1 Introduction - extractive PDF cue:** To bridge this gap, we introduce Planning And Reasoning Tasks in humaN-Robot collaboration (PARTNR), a novel benchmark that evaluates the ability of embodied AI agents ...
- **p. 1 / 1 Introduction - extractive PDF cue:** PARTNR consists of 100,000 natural language instructions paired with tailored evaluation functions, focusing on four task types: (1) constraint-free, where sub-tasks can be completed in ...
- **p. 2 / 1 Introduction - extractive PDF cue:** LLM-based helper agents LLM Planner We propose modular LLM-based agent baselines to collaborate in our benchmark.

## Source Evidence Cues

- **p. 11 / Method - extractive PDF cue:** We also measure exploration efficiency in human-in-the-loop, by measuring the steps taken to pick the first object, and extraneous effort, indicating actions that were not ...
- **p. 11 / Method - extractive PDF cue:** This reflects that smaller models with faster inference can improve human experience in real-world deployment.
- **p. 10 / Method - extractive PDF cue:** The goal of these experiments is to study multi-user dynamics at PARTNR tasks, and see if multiple humans collaborating are more efficient than single human.
- **p. 10 / Method - extractive PDF cue:** Finally, we run a human-AI experiment where a human participant collaborates with a robot controlled by an LLM (using the ReAct and Finetuned models from ...
- **p. 35 / A.10.2 Implementation Details - extractive PDF cue:** We train the model to predict, for every example, the action taken by the agent, which corresponds to the text after the </reserved_special_token_0>/ token.
- **p. 32 / A.9 Implementation Details for ReAct Agents - extractive PDF cue:** The finetuned model based on Llama-3.1-8B required an average of 0.53s per planning step.
- **p. 32 / A.9 Implementation Details for ReAct Agents - extractive PDF cue:** For all experiments, LLM inferrence is performed on two Nvidia A100 GPUs using the gpt-fast inference engine PyTorch (2023).
- **Detected method headings:** Method (p. 10); Method (p. 11); Method (p. 36); Method (p. 37); Method (p. 40)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | We also measure exploration efficiency in human-in-the-loop, by measuring the steps taken to pick the first object, and extraneous effort, indicating actions ... | p. 11 (Method), p. 11 (Method) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | This reflects that smaller models with faster inference can improve human experience in real-world deployment. | p. 11 (Method), p. 10 (Method) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | The goal of these experiments is to study multi-user dynamics at PARTNR tasks, and see if multiple humans collaborating are more efficient ... | p. 10 (Method), p. 10 (Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 10 / Method - extractive PDF cue:** This highlights the limitations of LLMs in reasoning about agent capabilities and following strict ordering constraints.
- **p. 10 / Method - extractive PDF cue:** Task success drops by 27% for temporal tasks and 20% for heterogeneous tasks compared to constraint-free tasks for ReAct (Table 13).
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 10 (Method), p. 10 (Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | PARTNR, consists, natural, language, instructions, paired, tailored, evaluation, functions, focusing, four, task, types, constraint-free | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | PARTNR, consists, natural, language, instructions, paired, tailored, evaluation, functions, focusing | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | bridge, introduce, Planning, Reasoning, Tasks, humaN-Robot, collaboration, PARTNR, novel, benchmark | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | highlights, limitations, LLMs, reasoning, about, agent, capabilities, following, strict, ordering | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1 Introduction - extractive PDF cue:** PARTNR consists of 100,000 natural language instructions paired with tailored evaluation functions, focusing on four task types: (1) constraint-free, where sub-tasks can be completed in ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Beyond the conventional challenges of long-horizon planning, novel partially observed environments, and large state and action spaces, PARTNR emphasizes the need for effective collaboration dynamics, ...
- **p. 10 / Method - extractive PDF cue:** To capture such extraneous agent effort, we measure the portion of agent actions that did not increase the percent complete metric i.e., did not contribute ...
- **p. 11 / Method - extractive PDF cue:** We also measure exploration efficiency in human-in-the-loop, by measuring the steps taken to pick the first object, and extraneous effort, indicating actions that were not ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Environment Multi-Agent Language Action Space Task Types Num tasks Overcooked (Carroll et al., 2019) 2D ✓ HL C 4 RoboGen (Wang et al., 2024) 3D ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Next, we employ simulation-in-the-loop to filter out hallucinations and infeasible instructions, complemented by human annotation to enhance diversity and accuracy.
- **p. 2 / 1 Introduction - extractive PDF cue:** Moreover, in decentralized multi-agent settings, task completion takes 1.3x more steps than single-agent, due to poor tracking of partner actions, resulting in extraneous actions.
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | Each planning step required an average of 52 tokens resulting in a latency of 4.55 seconds per planning step. | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | The average wall time to complete and entire episode (planning steps for both agents and simulation time) was 36.0 minutes. | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | Each planning step required an average of 52 tokens resulting in a latency of 4.55 seconds per planning step. | hardware, batch and throughput |

## Training vs Inference

- **p. 11 / Method - extractive PDF cue:** This reflects that smaller models with faster inference can improve human experience in real-world deployment.
- **p. 35 / A.10.2 Implementation Details - extractive PDF cue:** We train the model to predict, for every example, the action taken by the agent, which corresponds to the text after the </reserved_special_token_0>/ token.
- **p. 32 / A.9 Implementation Details for ReAct Agents - extractive PDF cue:** For all experiments, LLM inferrence is performed on two Nvidia A100 GPUs using the gpt-fast inference engine PyTorch (2023).
- **p. 35 / A.10.2 Implementation Details - extractive PDF cue:** We train all models on 4 A100 GPUs, with a batch size of 2 per GPU.
- **p. 32 / A.9 Implementation Details for ReAct Agents - extractive PDF cue:** For those experiments, simulation time and human agent inference time remained unchanged, giving a final wall time of 25.3 minutes per episode.
- **p. 35 / A.10.2 Implementation Details - extractive PDF cue:** The models are trained for 40,000 steps, which takes around 24 hours.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** measure, exploration, efficiency, human-in-the-loop, measuring, steps, taken, pick, first, object, extraneous, effort, indicating, actions, useful, task, completion, reflects, smaller, models.
- **Relevant PDF headings:** Method (p. 10); Method (p. 11); Method (p. 36); Method (p. 37); Method (p. 40).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | Released data includes extensions of the Habitat Synthetic Scenes Dataset (HSSD) (Khanna et al., 2024), generated benchmark task episodes, and model weights ... | p. 16 (A.1 Open-sourcing PARTNR Dataset and Codebase), p. 16 (A.1 Open-sourcing PARTNR Dataset and Codebase) |
| Baseline harness | Released code includes our PARTNR benchmark tasks, metrics, baseline oracle skills, large planning model framework, and dataset generation utilities. | p. 16 (A.1 Open-sourcing PARTNR Dataset and Codebase), p. 32 (A.9 Implementation Details for ReAct Agents) |
| Metric / failure reporting | PARTNR serves as a challenging benchmark that highlights the substantial limitations of current models. | p. 11 (5 Conclusion) |

## Failure and Ablation Link

- **p. 16 / A.1 Open-sourcing PARTNR Dataset and Codebase - extractive PDF cue:** Released data includes extensions of the Habitat Synthetic Scenes Dataset (HSSD) (Khanna et al., 2024), generated benchmark task episodes, and model weights for our trained ...
- **p. 11 / 5 Conclusion - extractive PDF cue:** PARTNR serves as a challenging benchmark that highlights the substantial limitations of current models.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 11 (Method), p. 11 (Method), p. 10 (Method), p. 10 (Method), p. 35 (A.10.2 Implementation Details), p. 32 (A.9 Implementation Details for ReAct Agents), objective p. 10 (Method), p. 10 (Method), temporal p. 32 (A.9 Implementation Details for ReAct Agents), p. 32 (A.9 Implementation Details for ReAct Agents), p. 6 (0 TemporalConstraint(), p. 10 (Method), p. 10 (Method), p. 11 (Method).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
