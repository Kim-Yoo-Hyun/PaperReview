# Method - Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v100/yu20a.html; PDF retrieval source: https://proceedings.mlr.press/v100/yu20a.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction)): In this paper, we propose an open-source simulated benchmark for meta-reinforcement learning and multitask learning consisting of 50 distinct robotic manipulation tasks.

## Method Body Digest

- **p. 1 / Abstract - extractive body cue:** In this paper, we propose an open-source simulated benchmark for meta-reinforcement learning and multitask learning consisting of 50 distinct robotic manipulation tasks.
- **p. 1 / Abstract - extractive body cue:** We evaluate 6 state-of-the-art meta-reinforcement learning and multi-task learning algorithms on these tasks.
- **p. 2 / 1 Introduction - extractive body cue:** This opens the door for future developments in multi-task and meta reinforcement learning: instead of focusing on further increasing performance on current narrow task suites, ...
- **p. 2 / 1 Introduction - extractive body cue:** In order to study the capabilities of current multi-task and meta-reinforcement learning methods and make it feasible to design new algorithms that actually generalize and ...
- **p. 2 / 1 Introduction - extractive body cue:** While these methods have made progress, the development of both classes of approaches has been limited by the lack of established benchmarks and evaluation protocols ...
- **p. 2 / 1 Introduction - extractive body cue:** In the most difficult evaluation, the method must use experience from 45 training tasks (left) to quickly learn distinctly new test tasks (right). tasks, and ...
- **p. 1 / 1 Introduction - extractive body cue:** While reinforcement learning (RL) has achieved some success in domains such as assembly [1], ping pong [2], in-hand manipulation [3], and hockey [4], state-of-the-art methods ...
- **p. 2 / 1 Introduction - extractive body cue:** We contend that multi-task and meta reinforcement learning methods that aim to efficiently learn many tasks and quickly generalize to new tasks should be evaluated ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** To this end, we present a benchmark of simulated manipulation tasks with everyday objects, all of which are contained in a shared, table-top environment with ...
- **p. 2 / 1 Introduction - extractive body cue:** For example, one popular evaluation of metalearning involves choosing different running directions for simulated legged robots [10], which then enables fast adaptation to new directions.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose an open-source simulated benchmark for meta-reinforcement learning and multitask learning consisting of 50 distinct robotic manipulation tasks.

## Source Evidence Cues

- **p. 1 / Abstract - extractive body cue:** In this paper, we propose an open-source simulated benchmark for meta-reinforcement learning and multitask learning consisting of 50 distinct robotic manipulation tasks.
- **p. 1 / Abstract - extractive body cue:** We evaluate 6 state-of-the-art meta-reinforcement learning and multi-task learning algorithms on these tasks.
- **p. 2 / 1 Introduction - extractive body cue:** This opens the door for future developments in multi-task and meta reinforcement learning: instead of focusing on further increasing performance on current narrow task suites, ...
- **p. 2 / 1 Introduction - extractive body cue:** In order to study the capabilities of current multi-task and meta-reinforcement learning methods and make it feasible to design new algorithms that actually generalize and ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | In this paper, we propose an open-source simulated benchmark for meta-reinforcement learning and multitask learning consisting of 50 distinct robotic manipulation tasks. | p. 1 (Abstract), p. 1 (Abstract) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | We evaluate 6 state-of-the-art meta-reinforcement learning and multi-task learning algorithms on these tasks. | p. 1 (Abstract), p. 2 (1 Introduction) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | This opens the door for future developments in multi-task and meta reinforcement learning: instead of focusing on further increasing performance on current ... | p. 2 (1 Introduction), p. 2 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1 Introduction - extractive body cue:** While these methods have made progress, the development of both classes of approaches has been limited by the lack of established benchmarks and evaluation protocols ...
- **p. 2 / 1 Introduction - extractive body cue:** In the most difficult evaluation, the method must use experience from 45 training tasks (left) to quickly learn distinctly new test tasks (right). tasks, and ...
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | evaluate, state-of-the-art, meta-reinforcement, learning, multi-task, algorithms, tasks, While, reinforcement, achieved, some, success, domains, assembly | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | evaluate, state-of-the-art, meta-reinforcement, learning, multi-task, algorithms, tasks, While, reinforcement, achieved | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | present, benchmark, simulated, manipulation, tasks, everyday, objects, contained, shared, table-top | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | While, methods, have, made, progress, development, classes, approaches, been, limited | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Abstract - extractive body cue:** We evaluate 6 state-of-the-art meta-reinforcement learning and multi-task learning algorithms on these tasks.
- **p. 1 / 1 Introduction - extractive body cue:** While reinforcement learning (RL) has achieved some success in domains such as assembly [1], ping pong [2], in-hand manipulation [3], and hockey [4], state-of-the-art methods ...
- **p. 2 / 1 Introduction - extractive body cue:** We contend that multi-task and meta reinforcement learning methods that aim to efficiently learn many tasks and quickly generalize to new tasks should be evaluated ...
- **p. 2 / 1 Introduction - extractive body cue:** Our empirical evaluation of existing methods on this benchmark reveals that, despite some impressive progress in multi-task and meta-reinforcement learning over the past few years, ...
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | For the meta-RL evaluation, we study three algorithms: RL2 [18, 19]: an on-policy metaRL algorithm that corresponds to training a LSTM network ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | There is a long history of robotics benchmarks [28], datasets [29, 30, 31, 32, 33, 34, 35], competitions [36] and standardized object ... | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | There is a long history of robotics benchmarks [28], datasets [29, 30, 31, 32, 33, 34, 35], competitions [36] and standardized object ... | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** open-source, simulated, benchmark, meta-reinforcement, learning, multitask, consisting, distinct, robotic, manipulation, tasks, evaluate, state-of-the-art, multi-task, algorithms, opens, door, future, developments, meta.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | For example, a commonly used meta-reinforcement learning benchmark uses different running velocities for a simulated robot as different tasks. | p. 1 (Abstract), p. 1 (Abstract) |
| Baseline harness | We evaluate 6 state-of-the-art meta-reinforcement learning and multi-task learning algorithms on these tasks. | p. 1 (Abstract), p. 1 (1 Introduction) |
| Metric / failure reporting | Figure 5: Quantitative results on MT10, MT50, ML10, and ML45. Note that, even on the challenging ML10 and ML45 benchmarks, current methods ... | p. 8 (Figure/Table caption), p. 1 (1 Introduction) |

## Failure and Ablation Link

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Introducing this parametric variability not only creates a substantially larger (infinite) variety of tasks, but also makes it substantially more practical to expect ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 1: A list of all of the Meta-World tasks and a description of each task. B Task Rewards and Success Metrics The form of ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Quantitative results on MT10, MT50, ML10, and ML45. Note that, even on the challenging ML10 and ML45 benchmarks, current methods already exhibit some ...
- **p. 1 / Abstract - extractive body cue:** When policies are meta-trained on such narrow task distributions, they cannot possibly generalize to more quickly acquire entirely new tasks.
- **p. 7 / 2 Related Work - extractive body cue:** Our experiments show that current meta-RL methods in fact cannot yet generalize effectively to entirely new tasks and do not even learn the meta-training tasks ...
- **p. 2 / 1 Introduction - extractive body cue:** This opens the door for future developments in multi-task and meta reinforcement learning: instead of focusing on further increasing performance on current narrow task suites, ...
- **p. 7 / 2 Related Work - extractive body cue:** This suggests a number of directions for future work, which we describe below.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), objective p. 2 (1 Introduction), p. 2 (1 Introduction), temporal p. 6 (2 Related Work), p. 3 (2 Related Work), p. 3 (2 Related Work), p. 6 (2 Related Work), p. 8 (2 Related Work), p. 8 (2 Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
