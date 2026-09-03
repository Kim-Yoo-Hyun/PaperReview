# Method - What Matters in Learning from Offline Human Demonstrations for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v164/mandlekar22a.html; PDF retrieval source: https://proceedings.mlr.press/v164/mandlekar22a/mandlekar22a.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1 Introduction), p. 3 (Dataset), p. 4 (Dataset), p. 3 (Dataset), p. 1 (Abstract), p. 2 (1 Introduction)): We find that history-dependent models can be extremely effective in learning from single and multi-human datasets while state-of-the-art batch RL algorithms struggle to learn from such datasets, and that the ...

## Method Body Digest

- **p. 2 / 1 Introduction - extractive body cue:** We find that history-dependent models can be extremely effective in learning from single and multi-human datasets while state-of-the-art batch RL algorithms struggle to learn from ...
- **p. 3 / Dataset - extractive body cue:** Unlike traditional supervised learning, where model selection can be achieved by using the model with the lowest validation loss [21], offline policy learning often suffers ...
- **p. 4 / Dataset - extractive body cue:** We collected these datasets by first training a state-of-the-art RL algorithm [30] on the Lift and Can task, taking agent checkpoints that are saved regularly ...
- **p. 3 / Dataset - extractive body cue:** In our study, we explore how agent design decisions affect policy performances, including the choice of agent architecture, agent observation space, and hyperparameter choices per ...
- **p. 1 / Abstract - extractive body cue:** Based on the study, we derive a series of lessons including the sensitivity to different algorithmic design choices, the dependence on the quality of the ...
- **p. 2 / 1 Introduction - extractive body cue:** Differences from classic supervised learning, such as a mismatch between training and evaluation objectives (task success rate), can make selecting a final policy challenging [21, ...
- **p. 1 / Abstract - extractive body cue:** While recent advances have been made in imitation learning and batch (offline) reinforcement learning, a lack of open-source human datasets and reproducible learning methods make ...
- **p. 1 / 1 Introduction - extractive body cue:** Roboticists have also attempted to tackle robot manipulation through learning from human datasets, using the paradigms of Imitation Learning [8-10] and Batch (Offline) Reinforcement Learning ...

## Design Rationale

- **p. 3 / Dataset - extractive body cue:** We present success rates averaged over 3 seeds for each method across the low-dim Machine-Generated (MG), Proficient-Human (PH), and Multi-Human (MH) datasets.

## Source Evidence Cues

- **p. 2 / 1 Introduction - extractive body cue:** We find that history-dependent models can be extremely effective in learning from single and multi-human datasets while state-of-the-art batch RL algorithms struggle to learn from ...
- **p. 3 / Dataset - extractive body cue:** Unlike traditional supervised learning, where model selection can be achieved by using the model with the lowest validation loss [21], offline policy learning often suffers ...
- **p. 4 / Dataset - extractive body cue:** We collected these datasets by first training a state-of-the-art RL algorithm [30] on the Lift and Can task, taking agent checkpoints that are saved regularly ...
- **p. 3 / Dataset - extractive body cue:** In our study, we explore how agent design decisions affect policy performances, including the choice of agent architecture, agent observation space, and hyperparameter choices per ...
- **p. 1 / Abstract - extractive body cue:** Based on the study, we derive a series of lessons including the sensitivity to different algorithmic design choices, the dependence on the quality of the ...
- **p. 2 / 1 Introduction - extractive body cue:** Differences from classic supervised learning, such as a mismatch between training and evaluation objectives (task success rate), can make selecting a final policy challenging [21, ...
- **p. 1 / Abstract - extractive body cue:** While recent advances have been made in imitation learning and batch (offline) reinforcement learning, a lack of open-source human datasets and reproducible learning methods make ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | We find that history-dependent models can be extremely effective in learning from single and multi-human datasets while state-of-the-art batch RL algorithms struggle ... | p. 2 (1 Introduction), p. 3 (Dataset) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | Unlike traditional supervised learning, where model selection can be achieved by using the model with the lowest validation loss [21], offline policy ... | p. 3 (Dataset), p. 4 (Dataset) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | We collected these datasets by first training a state-of-the-art RL algorithm [30] on the Lift and Can task, taking agent checkpoints that ... | p. 4 (Dataset), p. 3 (Dataset) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / Dataset - extractive body cue:** Unlike traditional supervised learning, where model selection can be achieved by using the model with the lowest validation loss [21], offline policy learning often suffers ...
- **p. 1 / Abstract - extractive body cue:** Based on the study, we derive a series of lessons including the sensitivity to different algorithmic design choices, the dependence on the quality of the ...
- **p. 1 / 1 Introduction - extractive body cue:** Roboticists have also attempted to tackle robot manipulation through learning from human datasets, using the paradigms of Imitation Learning [8-10] and Batch (Offline) Reinforcement Learning ...
- **p. 2 / 1 Introduction - extractive body cue:** Differences from classic supervised learning, such as a mismatch between training and evaluation objectives (task success rate), can make selecting a final policy challenging [21, ...
- **p. 3 / Dataset - extractive body cue:** This analysis is useful to understand the value of adding more data - an important consideration since collecting human demonstrations can be costly.
- **p. 5 / Dataset - extractive body cue:** We use binary task completion rewards for all our experiments.
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 3 (Dataset), p. 1 (Abstract), p. 2 (1 Introduction), p. 5 (Dataset).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Offline, policy, learning, sensitive, state, action, space, coverage, dataset, extension, size, itself, study, effect | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | Offline, policy, learning, sensitive, state, action, space, coverage, dataset, extension | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | present, success, rates, averaged, over, seeds, across, low-dim, Machine-Generated, Proficient-Human | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | Unlike, traditional, supervised, learning, where, model, selection, achieved, lowest, validation | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / Dataset - extractive body cue:** Offline policy learning is sensitive to the state and action space coverage in the dataset, and by extension, the size of the dataset itself.
- **p. 4 / Dataset - extractive body cue:** To study the effect of observation modalities, we capture a diverse set of sensor streams when collecting the dataset, including end-effector, gripper fingers, and joints, ...
- **p. 2 / 1 Introduction - extractive body cue:** Human demonstrations can differ from machine-generated datasets (a recent trend in benchmarks for offline policy learning [18, 19]) due to a non-Markovian decision process, since ...
- **p. 2 / 1 Introduction - extractive body cue:** We find that history-dependent models can be extremely effective in learning from single and multi-human datasets while state-of-the-art batch RL algorithms struggle to learn from ...
- **p. 3 / Dataset - extractive body cue:** In our study, we explore how agent design decisions affect policy performances, including the choice of agent architecture, agent observation space, and hyperparameter choices per ...
- **p. 4 / Dataset - extractive body cue:** Both include end-effector poses and gripper finger positions, and only differ in whether ground-truth object information is used (low-dim) or whether that information is replaced ...
- **p. 1 / Abstract - extractive body cue:** While recent advances have been made in imitation learning and batch (offline) reinforcement learning, a lack of open-source human datasets and reproducible learning methods make ...
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | (larger MLP) Using a larger MLP size at each RNN timestep reduces performance uniformly, suggesting that it is possible to overfit to ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | Each agent is trained for N epochs, where each epoch consists of M gradient steps, and evaluated every E epochs, by running ... | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | External factors (teleoperation device, past actions, history of episode) may all play a role. | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | Each agent is trained for N epochs, where each epoch consists of M gradient steps, and evaluated every E epochs, by running ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 Introduction - extractive body cue:** We find that history-dependent models can be extremely effective in learning from single and multi-human datasets while state-of-the-art batch RL algorithms struggle to learn from ...
- **p. 3 / Dataset - extractive body cue:** Unlike traditional supervised learning, where model selection can be achieved by using the model with the lowest validation loss [21], offline policy learning often suffers ...
- **p. 4 / Dataset - extractive body cue:** We collected these datasets by first training a state-of-the-art RL algorithm [30] on the Lift and Can task, taking agent checkpoints that are saved regularly ...
- **p. 1 / Abstract - extractive body cue:** Based on the study, we derive a series of lessons including the sensitivity to different algorithmic design choices, the dependence on the quality of the ...
- **p. 2 / 1 Introduction - extractive body cue:** Differences from classic supervised learning, such as a mismatch between training and evaluation objectives (task success rate), can make selecting a final policy challenging [21, ...
- **p. 5 / 4 Experiments - extractive body cue:** 4.1 Algorithm Comparison on Single and Multi-Human Demonstrations (C1, C2) We trained and evaluated all algorithms on the Proficient-Human (PH) and Multi-Human (MH) datasets and ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** find, history-dependent, models, extremely, effective, learning, single, multi-human, datasets, while, state-of-the-art, batch, algorithms, struggle, learn, choice, observation, space, hyperparameters, play.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | We collected 3 additional real-world datasets with a Franka robotic arm - Lift (Real), Can (Real), and Tool Hang (Real). | p. 8 (4 Experiments), p. 4 (Dataset) |
| Baseline harness | BC-RNN is a strong baseline on suboptimal human data, but there is room for improvement. | p. 6 (4 Experiments), p. 4 (Dataset) |
| Metric / failure reporting | Unlike traditional supervised learning, where model selection can be achieved by using the model with the lowest validation loss [21], offline policy ... | p. 3 (Dataset), p. 6 (4 Experiments) |

## Failure and Ablation Link

- **p. 6 / 4 Experiments - extractive body cue:** 4.3 Effect of Observation Space (C5) Learning from image observations can match low-dim agent performance.
- **p. 6 / 4 Experiments - extractive body cue:** (a) Effect of Policy Selection Criteria Dataset BC BC-RNN BCQ CQL Lift (PH) 100.0±0.0 100.0±0.0 98.0±1.6 52.0±13.0 Can (PH) 97.3±1.9 98.0±0.9 86.7±2.5 0.7±0.9 Square (PH) ...
- **p. 7 / 4 Experiments - extractive body cue:** In Fig 2a, we study the effect of adding end effector velocities to the observations (+ EEF Vel), and joint positions and velocities to the ...
- **p. 7 / 4 Experiments - extractive body cue:** 4.6 Effect of Dataset Size (C3) To study how dataset size impacts performance, we formed smaller 20% and 50% subsets of our human datasets by ...
- **p. 4 / Dataset - extractive body cue:** 3.2 Data Collection To study the effect of dataset source, we collected data from three different sources - MachineGenerated, Proficient-Human, and Multi-Human (more details in ...
- **p. 4 / Dataset - extractive body cue:** To study the effect of observation modalities, we capture a diverse set of sensor streams when collecting the dataset, including end-effector, gripper fingers, and joints, ...
- **p. 5 / Dataset - extractive body cue:** (a) Low-Dim (b) Image Figure 3: Effect of Dataset Size.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1 Introduction), p. 3 (Dataset), p. 4 (Dataset), p. 3 (Dataset), p. 1 (Abstract), p. 2 (1 Introduction), objective p. 3 (Dataset), p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (Dataset), p. 5 (Dataset), temporal p. 7 (4 Experiments), p. 5 (Dataset), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (4 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** We find that history-dependent models can be extremely effective in learning from single and multi-human datasets while state-of-the-art batch RL algorithms struggle to learn from such datasets, and that the ... (p. 2, 1 Introduction).
- **Objective/update evidence:** Unlike traditional supervised learning, where model selection can be achieved by using the model with the lowest validation loss [21], offline policy learning often suffers from the fact that the ... (p. 3, Dataset).
- **Temporal/runtime evidence:** Observation history is crucial for good performance. (p. 5, 4 Experiments).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
