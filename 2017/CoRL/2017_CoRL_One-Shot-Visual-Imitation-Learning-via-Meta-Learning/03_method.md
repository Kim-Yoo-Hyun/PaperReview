# Method - One-Shot Visual Imitation Learning via Meta-Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1703.07326; PDF retrieval source: https://arxiv.org/pdf/1703.07326. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1 Introduction), p. 6 (B C), p. 1 (Abstract), p. 2 (1 Introduction), p. 6 (B C), p. 3 (1 Introduction)): (a) Traditional Imitation Learning Task A e.g. stack blocks into towers of height 3 Many demonstrations Imitation Learning Algorithm Policy for task A action Environment obs Task B e.g. stack ...

## Method Body Digest

- **p. 2 / 1 Introduction - extractive body cue:** (a) Traditional Imitation Learning Task A e.g. stack blocks into towers of height 3 Many demonstrations Imitation Learning Algorithm Policy for task A action Environment ...
- **p. 6 / B C - extractive body cue:** We then apply standard soft attention over the current state to produce fixed-dimensional vectors, where the memory content only consists of positions of each block, ...
- **p. 1 / Abstract - extractive body cue:** A neural net is trained such that when it takes as input the first demonstration demonstration and a state sampled from the second demonstration, it ...
- **p. 2 / 1 Introduction - extractive body cue:** When conditioned on both the first demonstration and this observation, the network is trained to output the corresponding action. systems are not yet at a ...
- **p. 6 / B C - extractive body cue:** Attention over demonstration: The context network starts by computing a query vector as a function of the current state, which is then used to attend ...
- **p. 3 / 1 Introduction - extractive body cue:** To make this model work, we made essential use of soft attention [6] for processing both the (potentially long) sequence of states and action that ...
- **p. 5 / B C - extractive body cue:** D E F G H I J Attention over Current State Context Network Demonstration Network Manipulation Network Context Embedding Figure 2: Illustration of the network ...
- **p. 2 / 1 Introduction - extractive body cue:** 1, where the objective is to maximize the expected performance of the learned policy when faced with a new, previously unseen, task, and having received ...

## Design Rationale

- **p. 1 / Abstract - extractive body cue:** In this paper, we propose a meta-learning framework for achieving such capability, which we call one-shot imitation learning.
- **p. 5 / B C - extractive body cue:** The memory content to be extracted consists of the coordinates of each block, concatenated with the input embedding.
- **p. 3 / 1 Introduction - extractive body cue:** In particular, on a family of block stacking tasks, our neural network policy was able to perform well on novel block configurations which were not ...

## Source Evidence Cues

- **p. 2 / 1 Introduction - extractive body cue:** (a) Traditional Imitation Learning Task A e.g. stack blocks into towers of height 3 Many demonstrations Imitation Learning Algorithm Policy for task A action Environment ...
- **p. 6 / B C - extractive body cue:** We then apply standard soft attention over the current state to produce fixed-dimensional vectors, where the memory content only consists of positions of each block, ...
- **p. 1 / Abstract - extractive body cue:** A neural net is trained such that when it takes as input the first demonstration demonstration and a state sampled from the second demonstration, it ...
- **p. 2 / 1 Introduction - extractive body cue:** When conditioned on both the first demonstration and this observation, the network is trained to output the corresponding action. systems are not yet at a ...
- **p. 6 / B C - extractive body cue:** Attention over demonstration: The context network starts by computing a query vector as a function of the current state, which is then used to attend ...
- **p. 3 / 1 Introduction - extractive body cue:** To make this model work, we made essential use of soft attention [6] for processing both the (potentially long) sequence of states and action that ...
- **p. 5 / B C - extractive body cue:** D E F G H I J Attention over Current State Context Network Demonstration Network Manipulation Network Context Embedding Figure 2: Illustration of the network ...
- **Detected method headings:** B.1 Full Description of Architecture (p. 14)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Demonstration representation | expert trajectory를 training pair/context로 정렬한다 | observation history, goal, expert action | temporal alignment, relabeling 또는 latent context construction을 수행 | training sample/context | (a) Traditional Imitation Learning Task A e.g. stack blocks into towers of height 3 Many demonstrations Imitation Learning Algorithm Policy for task ... | p. 2 (1 Introduction), p. 6 (B C) |
| Policy fitting | expert action distribution을 학습한다 | context와 action target | behavior cloning, adversarial, sequence, diffusion 또는 flow objective를 최적화 | policy/action distribution | We then apply standard soft attention over the current state to produce fixed-dimensional vectors, where the memory content only consists of positions ... | p. 6 (B C), p. 1 (Abstract) |
| Closed-loop rollout | distribution shift와 recovery를 확인한다 | current observation/history | action/chunk을 실행하고 feedback으로 다음 prediction을 갱신 | trajectory/failure signal | A neural net is trained such that when it takes as input the first demonstration demonstration and a state sampled from the ... | p. 1 (Abstract), p. 2 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1 Introduction - extractive body cue:** 1, where the objective is to maximize the expected performance of the learned policy when faced with a new, previously unseen, task, and having received ...
- **p. 2 / 1 Introduction - extractive body cue:** (a) Traditional Imitation Learning Task A e.g. stack blocks into towers of height 3 Many demonstrations Imitation Learning Algorithm Policy for task A action Environment ...
- **Formal bridge:** observation history o_{t−H:t} -> expert-like action/chunk a_{t:t+H} -> imitation or action-distribution loss -> closed-loop task success and robustness.
- **Equation/algorithm anchors:** p. 2 (1 Introduction), p. 2 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | When, conditioned, first, demonstration, observation, network, trained, output, corresponding, action, systems, level, where, could | observation history와 expert trajectory/action | body cue; exact tensor/frame verify |
| State/latent | When, conditioned, first, demonstration, observation, network, trained, output, corresponding, action | behavior policy와 temporal action context | body cue; notation verify |
| Action/output | meta-learning, framework, achieving, capability, call, one-shot, imitation, learning, memory, content | predicted action 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | where, objective, maximize, expected, performance, learned, policy, when, faced, previously | imitation or action-distribution loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive body cue:** When conditioned on both the first demonstration and this observation, the network is trained to output the corresponding action. systems are not yet at a ...
- **p. 1 / Abstract - extractive body cue:** A neural net is trained such that when it takes as input the first demonstration demonstration and a state sampled from the second demonstration, it ...
- **p. 2 / 1 Introduction - extractive body cue:** We note that any pair of demonstrations for the same task provides a supervised training example for the neural net policy, where one demonstration is ...
- **p. 5 / B C - extractive body cue:** Therefore, we need an operation that can map variable-dimensional inputs to outputs with comparable dimensions.
- **p. 3 / 1 Introduction - extractive body cue:** To make this model work, we made essential use of soft attention [6] for processing both the (potentially long) sequence of states and action that ...
- **p. 5 / B C - extractive body cue:** Soft attention is a natural operation which maps variable-dimensional inputs to fixed-dimensional outputs.
- **p. 6 / B C - extractive body cue:** It processes both the current state and the embedding produced by the demonstration network, and outputs a context embedding, whose dimension does not depend on ...
- **Normalized interface:** observation=observation history와 expert trajectory/action; state=behavior policy와 temporal action context; output/action=predicted action 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single-step 또는 action chunk/trajectory horizon; exact chunk length는 exact value not recovered from the selected body cues. | Temporal Dropout: For block stacking, the demonstrations can span hundreds to thousands of time steps, and training with such long sequences can ... | episode/sequence/action-chunk boundary |
| Rate / latency | training inference와 deployed control tick을 분리; action chunk면 receding execution 여부 확인. | We measure success rate per task by executing the greedy policy (taking the most confident action at every time step) in 100 ... | Hz/fps, inference time and control rate |
| Memory | current observation, temporal history 또는 recurrent/sequence context. | Temporal Dropout: For block stacking, the demonstrations can span hundreds to thousands of time steps, and training with such long sequences can ... | window and reset |
| Compute | backbone/decoder inference, sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 Introduction - extractive body cue:** (a) Traditional Imitation Learning Task A e.g. stack blocks into towers of height 3 Many demonstrations Imitation Learning Algorithm Policy for task A action Environment ...
- **p. 1 / Abstract - extractive body cue:** A neural net is trained such that when it takes as input the first demonstration demonstration and a state sampled from the second demonstration, it ...
- **p. 2 / 1 Introduction - extractive body cue:** When conditioned on both the first demonstration and this observation, the network is trained to output the corresponding action. systems are not yet at a ...
- **p. 1 / Abstract - extractive body cue:** At training time, our algorithm is presented with pairs of demonstrations for a subset of all tasks.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Traditional, Imitation, Learning, Task, stack, blocks, towers, height, Many, demonstrations, Algorithm, Policy, action, Environment, Meta, more, tasks, One-Shot, Imitator, Neural.
- **Relevant PDF headings:** B.1 Full Description of Architecture (p. 14).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Demonstration representation | We conduct experiments with the block stacking tasks described in Section 3.2.2 These experiments are designed to answer the following questions: • ... | p. 6 (5 Experiments), p. 7 (5 Experiments) |
| Policy fitting | This assumes that a segmentation of the demonstration into multiple stages is available at test time, which gives it an unfair advantage ... | p. 7 (5 Experiments), p. 8 (5 Experiments) |
| Closed-loop rollout | Figure 2: Success rates of different architectures for particle reaching. The "Train" curves show the success rates when conditioned on demonstrations seen ... | p. 14 (Figure/Table caption), p. 7 (5 Experiments) |

## Failure and Ablation Link

- **p. 7 / 5 Experiments - extractive body cue:** However, a full trajectory, one which contains information about intermediate stages of the task's solution, can make it easier to train the optimal policy, because ...
- **p. 8 / 5 Experiments - extractive body cue:** We plan to extend the framework to demonstrations in the form of image data, which will allow more end-to-end learning without requiring a separate perception ...
- **p. 8 / 5 Experiments - extractive body cue:** Another interesting finding was that training with behavioral cloning has the same level of performance as training with DAGGER, which suggests that the entire training ...
- **p. 6 / 5 Experiments - extractive body cue:** 1In principle, one can replace this module with an RNN module.
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 6: Breakdown of the success and failure scenarios. The area that each color occupies represent the ratio of the corresponding scenario. B.5 Learning Curves ...
- **p. 22 / Figure/Table caption - extractive body cue:** Table 8: Breakdown of success and failure scenarios for DAGGER policy. 10
- **p. 22 / Figure/Table caption - extractive body cue:** Table 6: Success rates of a set of tasks that are equivalent up to permutations, using the DAGGER policy conditioned on full trajectories. #Stages Success ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1 Introduction), p. 6 (B C), p. 1 (Abstract), p. 2 (1 Introduction), p. 6 (B C), p. 3 (1 Introduction), objective p. 2 (1 Introduction), p. 2 (1 Introduction), temporal p. 4 (2 Related Work), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 8 (5 Experiments), p. 4 (2 Related Work), p. 6 (B C).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
