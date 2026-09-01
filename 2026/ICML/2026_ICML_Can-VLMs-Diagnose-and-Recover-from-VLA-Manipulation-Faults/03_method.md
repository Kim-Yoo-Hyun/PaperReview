# Method - Can VLMs Diagnose and Recover from VLA Manipulation Faults?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`.
> Analysis basis: official ICML proceedings page (abstract only; public PDF unavailable) checked on 2026-09-02 (1 source page(s); official ICML proceedings page (abstract only; public PDF unavailable); extraction quality: medium); canonical paper source: https://kakigo.github.io/VLA-FixBench/; body source: https://icml.cc/virtual/2026/poster/64203. The note is an evidence-anchored abstract/source-page analysis; exact tables/equations or section details remain at the cited source anchors. Evidence boundary: abstract/source-page only; method details, exact metrics, limitations and failure cases require full-text review. Reading tracker status/evidence was not changed.

## Method in One Sentence

abstract/source-page method statement (p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?)): Existing VLA models frequently fail in robotic manipulation tasks, with poorly structured fault types that often require expert diagnosis.

## Method Body Digest

- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** Existing VLA models frequently fail in robotic manipulation tasks, with poorly structured fault types that often require expert diagnosis.
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** Based on these findings, we design a robot recovery mechanism that can stop execution, roll back to an earlier safe step, and apply a corrective ...
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** Our results show that current AI models are still limited in reliable robot recovery, but accurate human-level feedback can substantially improve task success.

## Design Rationale

- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** We introduce VLA-FixBench, a dataset of robot manipulation failures covering problems in perception, planning, and control.
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** To address this, we introduce VLA-FixBench, a fault evaluation dataset that spans perception, planning, and control failures, and provides annotations for task stages, fault types, ...

## Source Evidence Cues

- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** Existing VLA models frequently fail in robotic manipulation tasks, with poorly structured fault types that often require expert diagnosis.
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** Based on these findings, we design a robot recovery mechanism that can stop execution, roll back to an earlier safe step, and apply a corrective ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | abstract/source-page cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | Existing VLA models frequently fail in robotic manipulation tasks, with poorly structured fault types that often require expert diagnosis. | p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | Based on these findings, we design a robot recovery mechanism that can stop execution, roll back to an earlier safe step, and ... | p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | Existing VLA models frequently fail in robotic manipulation tasks, with poorly structured fault types that often require expert diagnosis. | p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | findings, design, robot, recovery, mechanism, stop, execution, roll, back, earlier, safe, step, apply, corrective | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | findings, design, robot, recovery, mechanism, stop, execution, roll, back, earlier | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | introduce, VLA-FixBench, dataset, robot, manipulation, failures, covering, problems, perception, planning | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | not recovered | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** Based on these findings, we design a robot recovery mechanism that can stop execution, roll back to an earlier safe step, and apply a corrective ...
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** Our results show that current AI models are still limited in reliable robot recovery, but accurate human-level feedback can substantially improve task success.
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | abstract/source-page cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | We further propose FaultEval, a static-to-dynamic-to-real evaluation framework that benchmarks 20 VLMs across multiple fault-related dimensions. | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | Based on these findings, we design a robot recovery mechanism that can stop execution, roll back to an earlier safe step, and ... | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Existing, VLA, models, frequently, fail, robotic, manipulation, tasks, poorly, structured, fault, types, often, require, expert, diagnosis, findings, design, robot, recovery.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | The upper-bound analysis using human expert intervention shows that an idealized feedback loop can improve task success rates by 13\% on LIBERO ... | p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?) |
| Baseline harness | no linked comparison cue | 본문 anchor 없음 |
| Metric / failure reporting | The upper-bound analysis using human expert intervention shows that an idealized feedback loop can improve task success rates by 13\% on LIBERO ... | p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?) |

## Failure and Ablation Link

- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** This suggests that better failure diagnosis and recovery could make future robotic systems safer and more reliable.
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** We also build an evaluation framework to test how well different vision-language models can detect failures, locate when and where they happen, and provide useful ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), objective 본문 anchor 없음, temporal p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
