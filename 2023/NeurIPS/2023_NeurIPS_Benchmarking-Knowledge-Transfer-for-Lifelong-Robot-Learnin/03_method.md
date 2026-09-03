# Method - Benchmarking Knowledge Transfer for Lifelong Robot Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (44 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2306.03310; PDF retrieval source: https://arxiv.org/pdf/2306.03310. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (Abstract), p. 6 (2 Background), p. 6 (2 Background), p. 3 (2 Background), p. 1 (Abstract), p. 2 (1 Introduction)): Specifically, LIBERO highlights five key research topics in LLDM: 1) how to efficiently transfer declarative knowledge, procedural knowledge, or the mixture of both; 2) how to design effective policy architectures ...

## Method Body Digest

- **p. 1 / Abstract - extractive body cue:** Specifically, LIBERO highlights five key research topics in LLDM: 1) how to efficiently transfer declarative knowledge, procedural knowledge, or the mixture of both; 2) how ...
- **p. 6 / 2 Background - extractive body cue:** architecture [75] uses a similar ResNet-based visual backbone, but a transformer decoder [66] as the temporal backbone to process outputs from ResNet, which are a ...
- **p. 6 / 2 Background - extractive body cue:** For all the lifelong learning algorithms and neural architectures, we use behavioral cloning (BC) [4] to train policies for individual tasks (See (2)).
- **p. 3 / 2 Background - extractive body cue:** But during training, we perform behavioral cloning [4] with the following surrogate objective function: min π JBC(π) = 1 k k X p=1 E ot,at∼Dp ...
- **p. 1 / Abstract - extractive body cue:** Our extensive experiments present several insightful or even unexpected discoveries: sequential finetuning outperforms existing lifelong learning methods in forward transfer, no single visual encoder architecture ...
- **p. 2 / 1 Introduction - extractive body cue:** Policy architecture design is as crucial as lifelong learning algorithms.
- **p. 2 / 1 Introduction - extractive body cue:** The transformer architecture is better at abstracting temporal information than a recurrent neural network.
- **p. 3 / 2 Background - extractive body cue:** The robot's objective is to learn a policy π that maximizes the expected return: maxπ J(π) = Est,at∼π,µ0[PH t=1 g(st)].

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** We present an initial study using LIBERO to investigate five major research topics in LLDM (Figure 1): 1) knowledge transfer with different types of distribution ...
- **p. 1 / Abstract - extractive body cue:** To advance research in LLDM, we introduce LIBERO, a novel benchmark of lifelong learning for robot manipulation.
- **p. 3 / 2 Background - extractive body cue:** We present four task suites in Section 4.2: three task suites for studying the transfer of knowledge about spatial relationships, object concepts, and task goals ...

## Source Evidence Cues

- **p. 1 / Abstract - extractive body cue:** Specifically, LIBERO highlights five key research topics in LLDM: 1) how to efficiently transfer declarative knowledge, procedural knowledge, or the mixture of both; 2) how ...
- **p. 6 / 2 Background - extractive body cue:** architecture [75] uses a similar ResNet-based visual backbone, but a transformer decoder [66] as the temporal backbone to process outputs from ResNet, which are a ...
- **p. 6 / 2 Background - extractive body cue:** For all the lifelong learning algorithms and neural architectures, we use behavioral cloning (BC) [4] to train policies for individual tasks (See (2)).
- **p. 3 / 2 Background - extractive body cue:** But during training, we perform behavioral cloning [4] with the following surrogate objective function: min π JBC(π) = 1 k k X p=1 E ot,at∼Dp ...
- **p. 1 / Abstract - extractive body cue:** Our extensive experiments present several insightful or even unexpected discoveries: sequential finetuning outperforms existing lifelong learning methods in forward transfer, no single visual encoder architecture ...
- **p. 2 / 1 Introduction - extractive body cue:** Policy architecture design is as crucial as lifelong learning algorithms.
- **p. 2 / 1 Introduction - extractive body cue:** The transformer architecture is better at abstracting temporal information than a recurrent neural network.
- **Detected method headings:** A Implemented Neural Architectures and Lifelong Learning Algorithms (p. 17); A.1 Neural Architectures (p. 17); B.1 Lifelong Learning Algorithms (p. 19)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | Specifically, LIBERO highlights five key research topics in LLDM: 1) how to efficiently transfer declarative knowledge, procedural knowledge, or the mixture of ... | p. 1 (Abstract), p. 6 (2 Background) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | architecture [75] uses a similar ResNet-based visual backbone, but a transformer decoder [66] as the temporal backbone to process outputs from ResNet, ... | p. 6 (2 Background), p. 6 (2 Background) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | For all the lifelong learning algorithms and neural architectures, we use behavioral cloning (BC) [4] to train policies for individual tasks (See ... | p. 6 (2 Background), p. 3 (2 Background) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 2 Background - extractive body cue:** The robot's objective is to learn a policy π that maximizes the expected return: maxπ J(π) = Est,at∼π,µ0[PH t=1 g(st)].
- **p. 3 / 2 Background - extractive body cue:** But during training, we perform behavioral cloning [4] with the following surrogate objective function: min π JBC(π) = 1 k k X p=1 E ot,at∼Dp ...
- **p. 5 / 2 Background - extractive body cue:** We pick ER, EWC, and PACKNET because they correspond to the memory-based, regularization-based, and dynamic-architecture-based methods for lifelong learning.
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 3 (2 Background), p. 3 (2 Background).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | robot, executes, policy, sampling, continuous, value, end-effector, action, output, distribution, Neural, Architecture, Design, important | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | robot, executes, policy, sampling, continuous, value, end-effector, action, output, distribution | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | present, initial, study, LIBERO, investigate, five, major, research, topics, LLDM | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | robot, objective, learn, policy, maximizes, expected, return, Est, But, during | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 2 Background - extractive body cue:** In the end, a robot executes a policy by sampling a continuous value for end-effector action from the output distribution.
- **p. 4 / 2 Background - extractive body cue:** (T2) Neural Architecture Design An important research question in LLDM is how to design effective neural architectures to abstract the multi-modal observations (images, language descriptions, ...
- **p. 3 / 2 Background - extractive body cue:** Here, ot is the robot's sensory input, including the perceptual observation and the information about the robot's joints and gripper.
- **p. 5 / 2 Background - extractive body cue:** The language instruction is incorporated into the ResNet features using the FiLM method [50] and added to the LSTM inputs, respectively.
- **p. 3 / 2 Background - extractive body cue:** Here, S and A are the state and action spaces of the robot. µ0 is the initial state distribution, R : S × A →R ...
- **p. 5 / 2 Background - extractive body cue:** Initial State Distribution (µ0) To specify µ0, we first sample a scene layout that matches the objects/behaviors in a provided instruction.
- **p. 6 / 2 Background - extractive body cue:** We compute the multi-modal distribution over manipulation actions using a Gaussian-Mixture-Model (GMM) based output head [8, 42, 68].
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | The RESNET-RNN [42] uses a ResNet as the visual backbone that encodes per-step visual observations and an LSTM as the temporal backbone ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | 3Throughout the paper, a superscript/subscript is used to index the task/time step. | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | We save a checkpoint every 5 epochs of training and then pick the checkpoint for each architecture that has the best performance ... | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / Abstract - extractive body cue:** Specifically, LIBERO highlights five key research topics in LLDM: 1) how to efficiently transfer declarative knowledge, procedural knowledge, or the mixture of both; 2) how ...
- **p. 6 / 2 Background - extractive body cue:** For all the lifelong learning algorithms and neural architectures, we use behavioral cloning (BC) [4] to train policies for individual tasks (See (2)).
- **p. 3 / 2 Background - extractive body cue:** But during training, we perform behavioral cloning [4] with the following surrogate objective function: min π JBC(π) = 1 k k X p=1 E ot,at∼Dp ...
- **p. 1 / Abstract - extractive body cue:** Our extensive experiments present several insightful or even unexpected discoveries: sequential finetuning outperforms existing lifelong learning methods in forward transfer, no single visual encoder architecture ...
- **p. 9 / 5 Experiments - extractive body cue:** We save a checkpoint every 5 epochs of training and then pick the checkpoint for each architecture that has the best performance as the pretrained ...
- **p. 9 / 5 Experiments - extractive body cue:** For pretraining, we apply behavioral cloning on the 90 tasks using the three policy architectures for 50 epochs.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Specifically, LIBERO, highlights, five, research, topics, LLDM, efficiently, transfer, declarative, knowledge, procedural, mixture, design, effective, policy, architectures, algorithms, robustness, lifelong.
- **Relevant PDF headings:** A Implemented Neural Architectures and Lifelong Learning Algorithms (p. 17); A.1 Neural Architectures (p. 17); B.1 Lifelong Learning Algorithms (p. 19).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | But since PACKNET splits the network into different sub-networks, the essential capacity of the network for learning any individual task is smaller. | p. 8 (5 Experiments), p. 8 (5 Experiments) |
| Baseline harness | Study on Lifelong Learning Algorithms (Q1, Q3) Table 2 reports the lifelong learning performance of the three lifelong learning algorithms, together with ... | p. 8 (5 Experiments), p. 8 (5 Experiments) |
| Metric / failure reporting | This is surprising since it indicates all lifelong learning algorithms we consider actually hurt forward transfer; 2) PACKNET outperforms other lifelong learning ... | p. 8 (5 Experiments), p. 6 (5 Experiments) |

## Failure and Ablation Link

- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Performance of different combinations of algorithms and architectures without pretraining or with pretraining. The multi-task learning performance is also included for reference. Findings: ...
- **p. 43 / Figure/Table caption - extractive body cue:** Figure 26: Attention map comparison between models without/with pretrained models using RESNET- T and different lifelong learning algorithms on three selected tasks from LIBERO-LONG. 43
- **p. 19 / Figure/Table caption - extractive body cue:** Table 7: Hyper parameters of VIT-T. B.1 Lifelong Learning Algorithms Lifelong learning (LL) is a field of study that aims to understand how an agent ...
- **p. 8 / 5 Experiments - extractive body cue:** Task-ID embeddings are produced by feeding a string such as "Task 5" into a pretrained BERT model.
- **p. 8 / 5 Experiments - extractive body cue:** Study on Language Embeddings as the Task Identifier (Q4) To investigate to what extent language embedding play a role in LLDM, we compare the performance ...
- **p. 9 / 5 Experiments - extractive body cue:** For pretraining, we apply behavioral cloning on the 90 tasks using the three policy architectures for 50 epochs.
- **p. 6 / 5 Experiments - extractive body cue:** Q5: How robust are different LL algorithms to task ordering in LLDM?

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (Abstract), p. 6 (2 Background), p. 6 (2 Background), p. 3 (2 Background), p. 1 (Abstract), p. 2 (1 Introduction), objective p. 3 (2 Background), p. 3 (2 Background), p. 5 (2 Background), temporal p. 5 (2 Background), p. 3 (2 Background), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 6 (2 Background), p. 6 (2 Background).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (44 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Specifically, LIBERO highlights five key research topics in LLDM: 1) how to efficiently transfer declarative knowledge, procedural knowledge, or the mixture of both; 2) how to design effective policy architectures ... (p. 1, Abstract).
- **Objective/update evidence:** But during training, we perform behavioral cloning [4] with the following surrogate objective function: min π JBC(π) = 1 k k X p=1 E ot,at∼Dp  lp X t=0 L ... (p. 3, 2 Background).
- **Temporal/runtime evidence:** The RESNET-RNN [42] uses a ResNet as the visual backbone that encodes per-step visual observations and an LSTM as the temporal backbone to process a sequence of encoded visual information. (p. 5, 2 Background).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
