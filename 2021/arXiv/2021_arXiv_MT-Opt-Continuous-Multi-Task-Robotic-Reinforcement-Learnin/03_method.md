# Method - MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2104.08212; PDF retrieval source: https://arxiv.org/abs/2104.08212. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (V. REWARDS VIA MULTI-TASK SUCCESS DETECTORS), p. 3 (III. SYSTEM OVERVIEW), p. 2 (I. INTRODUCTION), p. 3 (III. SYSTEM OVERVIEW), p. 4 (III. SYSTEM OVERVIEW), p. 1 (I. INTRODUCTION)): In fact, we use supervised learning to train a similar neural network architecture model (excluding the inputs responsible for action representation) as for the MT-Opt multi-task policy, which we describe ...

## Method Body Digest

- **p. 5 / V. REWARDS VIA MULTI-TASK SUCCESS DETECTORS - extractive body cue:** In fact, we use supervised learning to train a similar neural network architecture model (excluding the inputs responsible for action representation) as for the MT-Opt ...
- **p. 3 / III. SYSTEM OVERVIEW - extractive body cue:** First, we use a single, multi-task deep neural network to learn a policy for all the tasks simultaneously, which enables parameter sharing between tasks.
- **p. 2 / I. INTRODUCTION - extractive body cue:** First, multi-task reinforcement learning is known to be exceedingly difficult from the optimization standpoint, and the hypothesized benefits of multi-task learning have proven hard to ...
- **p. 3 / III. SYSTEM OVERVIEW - extractive body cue:** Multi-Task Reinforcement Learning Algorithm We first introduce notation and RL fundamentals.
- **p. 4 / III. SYSTEM OVERVIEW - extractive body cue:** Similarly to [36], we use the cross-entropy method (CEM) to perform the stochastic optimization to compute the target value function.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Such shared representations can include basic visual features, as well as more complex concepts, such as learning how to pick up objects.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Lastly, in order to receive the benefits from shared, multi-task representation, we need to significantly scale up our algorithms, the number of tasks in the ...
- **p. 3 / III. SYSTEM OVERVIEW - extractive body cue:** The goal of the multi-task RL policy is to maximize the expected sum of rewards for all tasks drawn from the distribution p(T ).

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** We further make the following contributions: • We address the challenge of providing rewards by creating a scalable and intuitive success-classifier-based approach that allows to ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** D) Sample of behaviorally and visually distinct tasks such as covering, chasing, alignment, which we show our method can adapt to.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We present our multi-task system as well as examples of some of the tasks that it is capable of performing in Fig.

## Source Evidence Cues

- **p. 5 / V. REWARDS VIA MULTI-TASK SUCCESS DETECTORS - extractive body cue:** In fact, we use supervised learning to train a similar neural network architecture model (excluding the inputs responsible for action representation) as for the MT-Opt ...
- **p. 3 / III. SYSTEM OVERVIEW - extractive body cue:** First, we use a single, multi-task deep neural network to learn a policy for all the tasks simultaneously, which enables parameter sharing between tasks.
- **p. 2 / I. INTRODUCTION - extractive body cue:** First, multi-task reinforcement learning is known to be exceedingly difficult from the optimization standpoint, and the hypothesized benefits of multi-task learning have proven hard to ...
- **p. 3 / III. SYSTEM OVERVIEW - extractive body cue:** Multi-Task Reinforcement Learning Algorithm We first introduce notation and RL fundamentals.
- **p. 4 / III. SYSTEM OVERVIEW - extractive body cue:** Similarly to [36], we use the cross-entropy method (CEM) to perform the stochastic optimization to compute the target value function.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Such shared representations can include basic visual features, as well as more complex concepts, such as learning how to pick up objects.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Lastly, in order to receive the benefits from shared, multi-task representation, we need to significantly scale up our algorithms, the number of tasks in the ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data schema / normalization | heterogeneous robot trajectory를 공통 sample로 만든다 | observation, action, task와 embodiment metadata | sensor/action schema alignment, filtering, normalization을 수행 | shared dataset representation | In fact, we use supervised learning to train a similar neural network architecture model (excluding the inputs responsible for action representation) as ... | p. 5 (V. REWARDS VIA MULTI-TASK SUCCESS DETECTORS), p. 3 (III. SYSTEM OVERVIEW) |
| Coverage / augmentation | task·embodiment·failure variation을 확장한다 | dataset과 metadata | retargeting, relabeling, synthetic/teleoperation augmentation 또는 sampling을 적용 | expanded data support | First, we use a single, multi-task deep neural network to learn a policy for all the tasks simultaneously, which enables parameter sharing ... | p. 3 (III. SYSTEM OVERVIEW), p. 2 (I. INTRODUCTION) |
| Downstream learning interface | 정규화된 data를 policy/representation이 사용한다 | shared observations/actions | pretraining, BC, action-token 또는 representation learning을 수행 | checkpoint/policy action | First, multi-task reinforcement learning is known to be exceedingly difficult from the optimization standpoint, and the hypothesized benefits of multi-task learning have ... | p. 2 (I. INTRODUCTION), p. 3 (III. SYSTEM OVERVIEW) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. SYSTEM OVERVIEW - extractive body cue:** The goal of the multi-task RL policy is to maximize the expected sum of rewards for all tasks drawn from the distribution p(T ).
- **p. 2 / I. INTRODUCTION - extractive body cue:** We further make the following contributions: • We address the challenge of providing rewards by creating a scalable and intuitive success-classifier-based approach that allows to ...
- **p. 4 / III. SYSTEM OVERVIEW - extractive body cue:** While fIorig fails to leverage Algorithm 1 Task Impersonation procedure fI(ei : original episode) expanded episodes = [] SD{ki} ←set of SDs relevant to task ...
- **p. 5 / V. REWARDS VIA MULTI-TASK SUCCESS DETECTORS - extractive body cue:** This sparse-reward assumption allows us to train a neuralnetwork-based success detector model (SD), which given a final image, infers a probability of a task being ...
- **p. 4 / III. SYSTEM OVERVIEW - extractive body cue:** Similarly to [36], we use the cross-entropy method (CEM) to perform the stochastic optimization to compute the target value function.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Prior work indicates that multi-task RL can indeed amortize the cost of single-task learning [20, 56, 60, 80, 30].
- **Formal bridge:** trajectory D with task/embodiment metadata -> normalized sample or downstream action -> coverage/data efficiency/transfer objective -> cross-domain transfer and task performance.
- **Equation/algorithm anchors:** p. 4 (III. SYSTEM OVERVIEW), p. 4 (III. SYSTEM OVERVIEW).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | time, step, policy, selects, action, given, current, state, task, beginning, episode, receives, task-dependent, reward | multi-view observation, language/task label과 action trajectory | body cue; exact tensor/frame verify |
| State/latent | time, step, policy, selects, action, given, current, state, task, beginning | shared representation, embodiment/task identity와 data distribution | body cue; notation verify |
| Action/output | further, make, following, contributions, address, challenge, providing, rewards, creating, scalable | dataset sample 또는 learned policy action | body cue; unit/decoder verify |
| Objective/constraint | goal, multi-task, policy, maximize, expected, rewards, tasks, drawn, distribution, further | coverage/data efficiency/transfer objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. SYSTEM OVERVIEW - extractive body cue:** At each time step, the policy selects an action a given the current state s and the current task Ti that is set at the ...
- **p. 3 / III. SYSTEM OVERVIEW - extractive body cue:** 2C), at each time step, a policy takes as input a camera image and a one-hot encoding of the task, and sends a motor command ...
- **p. 5 / V. REWARDS VIA MULTI-TASK SUCCESS DETECTORS - extractive body cue:** In fact, we use supervised learning to train a similar neural network architecture model (excluding the inputs responsible for action representation) as for the MT-Opt ...
- **p. 4 / III. SYSTEM OVERVIEW - extractive body cue:** The goal is to use all transitions of an episode e(i) generated by task Ti to aid in training a policy for a set of ...
- **p. 4 / III. SYSTEM OVERVIEW - extractive body cue:** Consider an identity impersonation function fIorig(e(i)) = e(i), where no task impersonation takes place, i.e. an episode e(i) generated by task Ti is used to ...
- **p. 5 / V. REWARDS VIA MULTI-TASK SUCCESS DETECTORS - extractive body cue:** Such out of distribution images might be caused by various real-world factors such as different lighting conditions, changing in background surroundings and novel states which ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Finally, by enabling the multi-task RL policy to learn shared representations, learning new tasks can become easier over time as the system acquires more skills ...
- **Normalized interface:** observation=multi-view observation, language/task label과 action trajectory; state=shared representation, embodiment/task identity와 data distribution; output/action=dataset sample 또는 learned policy action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | trajectory demonstration horizon; training sample window와 deployment task horizon을 분리한다. | At each time step, the policy selects an action a given the current state s and the current task Ti that is ... | episode/sequence/action-chunk boundary |
| Rate / latency | data recording/action sampling rate와 policy inference/control rate를 분리한다. | 2C), at each time step, a policy takes as input a camera image and a one-hot encoding of the task, and sends ... | Hz/fps, inference time and control rate |
| Memory | trajectory, embodiment/task metadata와 dataset index. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | data decoding, normalization/augmentation과 downstream training budget이 결정한다. | 5) consists of 5400 episodes collected for that task (i.e. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / V. REWARDS VIA MULTI-TASK SUCCESS DETECTORS - extractive body cue:** In fact, we use supervised learning to train a similar neural network architecture model (excluding the inputs responsible for action representation) as for the MT-Opt ...
- **p. 7 / VII. EXPERIMENTS - extractive body cue:** In addition to fIskill task impersonation, we re-balance each training batch between the tasks as well as within each task to keep the relative proportion ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** While existing methods are effective and able to generalize, they require considerable on-robot training time, as well as extensive engineering effort for setting up each ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** fact, supervised, learning, train, similar, neural, network, architecture, model, excluding, inputs, responsible, action, representation, MT-Opt, multi-task, policy, describe, more, detail.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data schema / normalization | The goal of our real-world experiments is to answer the following questions: (1) How does MT-Opt perform, quantitatively and qualitatively, on a ... | p. 6 (VII. EXPERIMENTS), p. 6 (VII. EXPERIMENTS) |
| Coverage / augmentation | Looking at the average performance across all task, we observe that MT-Opt significantly outperforms the baselines, in some cases with ≈3× average ... | p. 7 (VII. EXPERIMENTS), p. 7 (VII. EXPERIMENTS) |
| Downstream learning interface | Looking at the average performance across all task, we observe that MT-Opt significantly outperforms the baselines, in some cases with ≈3× average ... | p. 7 (VII. EXPERIMENTS), p. 7 (VII. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 7 / VII. EXPERIMENTS - extractive body cue:** Tasks such as lift-carrot and Parameter Sharing Ablation (Success Rate) Model: 2-Task Model 12-Task Model lift-any 0.82 0.89 place-any 0.63 0.85 TABLE I: The effect ...
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 12: Practical effect of task impersonation for successful outcomes. Dark blue indicates data specifically collected for a task; light blue indicates episodes impersonated from ...
- **p. 7 / VII. EXPERIMENTS - extractive body cue:** We use the same fIskill task impersonation strategy, and the exact same offline dataset (i.e. both policies use the data from the extra 10 narrower ...
- **p. 8 / VII. EXPERIMENTS - extractive body cue:** Data Strategies Ablation (min, mean, max, mean of low data tasks) Imperson.
- **p. 8 / VII. EXPERIMENTS - extractive body cue:** Data-Sharing Multi-Task also trains a single network for all tasks and shares the data across all tasks without further re-balancing.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6: Top: 12 tasks trained for ablations, giving rise to Object Acquisition and Object Manipulation skills. Bottom: examples of additional tasks that a skilled ...
- **p. 16 / Figure/Table caption - extractive body cue:** Fig. 16: Evaluation scene used for ablation experiments. Con- tains one of three different color plates. And nine graspable objects: One of each object from ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (V. REWARDS VIA MULTI-TASK SUCCESS DETECTORS), p. 3 (III. SYSTEM OVERVIEW), p. 2 (I. INTRODUCTION), p. 3 (III. SYSTEM OVERVIEW), p. 4 (III. SYSTEM OVERVIEW), p. 1 (I. INTRODUCTION), objective p. 3 (III. SYSTEM OVERVIEW), p. 2 (I. INTRODUCTION), p. 4 (III. SYSTEM OVERVIEW), p. 5 (V. REWARDS VIA MULTI-TASK SUCCESS DETECTORS), p. 4 (III. SYSTEM OVERVIEW), p. 1 (I. INTRODUCTION), temporal p. 3 (III. SYSTEM OVERVIEW), p. 3 (III. SYSTEM OVERVIEW), p. 6 (VII. EXPERIMENTS), p. 6 (VII. EXPERIMENTS), p. 7 (VII. EXPERIMENTS), p. 8 (VII. EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** In fact, we use supervised learning to train a similar neural network architecture model (excluding the inputs responsible for action representation) as for the MT-Opt multi-task policy, which we describe ... (p. 5, V. REWARDS VIA MULTI-TASK SUCCESS DETECTORS).
- **Objective/update evidence:** Prior work indicates that multi-task RL can indeed amortize the cost of single-task learning [20, 56, 60, 80, 30]. (p. 1, I. INTRODUCTION).
- **Temporal/runtime evidence:** In order to further reduce the variance of the evaluation, we shuffle the bins after each episode and (p. 6, VII. EXPERIMENTS).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
