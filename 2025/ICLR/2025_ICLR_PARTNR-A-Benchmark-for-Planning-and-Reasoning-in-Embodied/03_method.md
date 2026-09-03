# Method - PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (64 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=T5QLRRHyL1; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/114714. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 34 (A.9.2 IMPLEMENTATION DETAILS), p. 31 (A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS), p. 31 (A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS), p. 34 (A.9.2 IMPLEMENTATION DETAILS)): We train the model to predict, for every example, the action taken by the agent, which corresponds to the text after the </reserved_special_token_0>/ token.

## Method Body Digest

- **p. 34 / A.9.2 IMPLEMENTATION DETAILS - extractive body cue:** We train the model to predict, for every example, the action taken by the agent, which corresponds to the text after the </reserved_special_token_0>/ token.
- **p. 31 / A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS - extractive body cue:** The finetuned model based on Llama-3.1-8B required an average of 0.53s per planning step.
- **p. 31 / A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS - extractive body cue:** For all experiments, LLM inferrence is performed on two Nvidia A100 GPUs using the gpt-fast inference engine PyTorch (2023).
- **p. 34 / A.9.2 IMPLEMENTATION DETAILS - extractive body cue:** We train all models on 4 A100 GPUs, with a batch size of 2 per GPU.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** PARTNR consists of 100,000 natural language instructions paired with tailored evaluation functions, focusing on four task types: (1) constraint-free, where sub-tasks can be completed in ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Beyond the conventional challenges of long-horizon planning, partially observed environments, and large state and action spaces, PARTNR emphasizes the need for effective collaboration.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Subsequently, a set of 1,000 verified instructions and evaluation functions are utilized to guide an LLM through in-context prompting to create 100,000 tasks.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Moreover, in decentralized multi-agent settings, task completion takes 1.3x more steps than singleagent, due to poor tracking of partner actions, resulting in extraneous actions.

## Design Rationale

- **p. 1 / 1 INTRODUCTION - extractive body cue:** To bridge this gap, we introduce Planning And Reasoning Tasks in humaN-Robot collaboration (PARTNR), a novel benchmark that evaluates the ability of embodied AI agents ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Instead, we propose a semi-automated approach using 1
- **p. 2 / 1 INTRODUCTION - extractive body cue:** LLM-based helper agents LLM Planner We propose modular LLM-based agent baselines to collaborate in our benchmark.

## Source Evidence Cues

- **p. 34 / A.9.2 IMPLEMENTATION DETAILS - extractive body cue:** We train the model to predict, for every example, the action taken by the agent, which corresponds to the text after the </reserved_special_token_0>/ token.
- **p. 31 / A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS - extractive body cue:** The finetuned model based on Llama-3.1-8B required an average of 0.53s per planning step.
- **p. 31 / A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS - extractive body cue:** For all experiments, LLM inferrence is performed on two Nvidia A100 GPUs using the gpt-fast inference engine PyTorch (2023).
- **p. 34 / A.9.2 IMPLEMENTATION DETAILS - extractive body cue:** We train all models on 4 A100 GPUs, with a batch size of 2 per GPU.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | We train the model to predict, for every example, the action taken by the agent, which corresponds to the text after the ... | p. 34 (A.9.2 IMPLEMENTATION DETAILS), p. 31 (A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | The finetuned model based on Llama-3.1-8B required an average of 0.53s per planning step. | p. 31 (A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS), p. 31 (A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | For all experiments, LLM inferrence is performed on two Nvidia A100 GPUs using the gpt-fast inference engine PyTorch (2023). | p. 31 (A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS), p. 34 (A.9.2 IMPLEMENTATION DETAILS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | PARTNR, consists, natural, language, instructions, paired, tailored, evaluation, functions, focusing, four, task, types, constraint-free | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | PARTNR, consists, natural, language, instructions, paired, tailored, evaluation, functions, focusing | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | bridge, introduce, Planning, Reasoning, Tasks, humaN-Robot, collaboration, PARTNR, novel, benchmark | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | not recovered | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1 INTRODUCTION - extractive body cue:** PARTNR consists of 100,000 natural language instructions paired with tailored evaluation functions, focusing on four task types: (1) constraint-free, where sub-tasks can be completed in ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Beyond the conventional challenges of long-horizon planning, partially observed environments, and large state and action spaces, PARTNR emphasizes the need for effective collaboration.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Subsequently, a set of 1,000 verified instructions and evaluation functions are utilized to guide an LLM through in-context prompting to create 100,000 tasks.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Moreover, in decentralized multi-agent settings, task completion takes 1.3x more steps than singleagent, due to poor tracking of partner actions, resulting in extraneous actions.
- **p. 34 / A.9.2 IMPLEMENTATION DETAILS - extractive body cue:** We train the model to predict, for every example, the action taken by the agent, which corresponds to the text after the </reserved_special_token_0>/ token.
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

- **p. 34 / A.9.2 IMPLEMENTATION DETAILS - extractive body cue:** We train the model to predict, for every example, the action taken by the agent, which corresponds to the text after the </reserved_special_token_0>/ token.
- **p. 31 / A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS - extractive body cue:** For all experiments, LLM inferrence is performed on two Nvidia A100 GPUs using the gpt-fast inference engine PyTorch (2023).
- **p. 34 / A.9.2 IMPLEMENTATION DETAILS - extractive body cue:** We train all models on 4 A100 GPUs, with a batch size of 2 per GPU.
- **p. 34 / A.9.2 IMPLEMENTATION DETAILS - extractive body cue:** We train all models on 4 A100 GPUs, with a batch size of 2 per GPU.
- **p. 31 / A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS - extractive body cue:** For those experiments, simulation time and human agent inference time remained unchanged, giving a final wall time of 25.3 minutes per episode.
- **p. 34 / A.9.2 IMPLEMENTATION DETAILS - extractive body cue:** The models are trained for 40,000 steps, which takes around 24 hours.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** train, model, predict, every, example, action, taken, agent, corresponds, text, after, reserved_special_token_0, token, finetuned, Llama-3, required, average, planning, step, experiments.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | Released data includes extensions of the Habitat Synthetic Scenes Dataset (HSSD) (Khanna et al., 2024), generated benchmark task episodes, and model weights ... | p. 15 (A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE), p. 15 (A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE) |
| Baseline harness | Released code includes our PARTNR benchmark tasks, metrics, baseline oracle skills, large planning model framework, and dataset generation utilities. | p. 15 (A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE), p. 35 (Figure/Table caption) |
| Metric / failure reporting | Table 3: Human-in-the-Loop Evaluation. We evaluate the performance of a 2-person human team and human-LLM teams, comparing them to solo human performance ... | p. 10 (Figure/Table caption), p. 35 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: We present PARTNR, a benchmark for planning and reasoning in embodied multi-agent tasks, featuring 100,000 everyday tasks and evaluation functions generated semi-automatically, spanning ...
- **p. 23 / Figure/Table caption - extractive body cue:** Table 7: Manually-annotated generation accuracy of 100k-scale PARTNR tasks and evaluation functions. Altogether, we find that 83% of episodes are generated without any task or ...
- **p. 15 / A.1 OPEN-SOURCING PARTNR DATASET AND CODEBASE - extractive body cue:** Released data includes extensions of the Habitat Synthetic Scenes Dataset (HSSD) (Khanna et al., 2024), generated benchmark task episodes, and model weights for our trained ...
- **p. 26 / Figure/Table caption - extractive body cue:** Figure 9: PARTNR tasks visualized in PrediViz. The design distills the task and scene to only the components necessary for verification. In example task #2, ...
- **p. 37 / Figure/Table caption - extractive body cue:** Figure 13: HITL on Web-browser. Our HITL sys- tem can be deployed on web browsers enabling large-scale collection. We adapt the existing human-in-the-loop (HITL) infrastructure ...
- **p. 24 / Figure/Table caption - extractive body cue:** Table 8: Top three failure modes of 100k-scale task and evaluation generation reported for each task type. Failures of task generation are led by the ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Analysis of planner baselines in various settings. We compare performance using simula- tion steps, success rate and percent complete on the tasks, and ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 34 (A.9.2 IMPLEMENTATION DETAILS), p. 31 (A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS), p. 31 (A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS), p. 34 (A.9.2 IMPLEMENTATION DETAILS), objective 본문 anchor 없음, temporal p. 31 (A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS), p. 31 (A.8 IMPLEMENTATION DETAILS FOR REACT AGENTS), p. 34 (A.9.2 IMPLEMENTATION DETAILS), p. 4 (0 TemporalConstraint(), p. 5 (0 TemporalConstraint(), p. 7 (0 TemporalConstraint().
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
