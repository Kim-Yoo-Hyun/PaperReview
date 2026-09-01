# Method - Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (54 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2410.21845; PDF retrieval source: https://arxiv.org/pdf/2410.21845. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 9 (3.5. Training Process), p. 9 (3.5. Training Process), p. 8 (3.5. Training Process), p. 8 (3.5. Training Process)): Finally, we start the policy training process.

## Method Body Digest

- **p. 9 / 3.5. Training Process - extractive body cue:** Finally, we start the policy training process.
- **p. 9 / 3.5. Training Process - extractive body cue:** Such an intervention strategy will cause the overestimation of the value function, particularly in the early stages of the training process; which can result in ...
- **p. 8 / 3.5. Training Process - extractive body cue:** This is approximately equivalent to 10 human trajectories, assuming each trajectory takes about 10 seconds.
- **p. 8 / 3.5. Training Process - extractive body cue:** For all cameras, we perform image cropping to focus on the area of interest and resize the images to 128x128 for the neural network to ...
- **p. 8 / 3.5. Training Process - extractive body cue:** Additionally, we may collect extra data to address any false negative and false positive issues with the reward classifier.
- **p. 8 / 3.5. Training Process - extractive body cue:** Next, we collect data to train the reward classifier, which is a crucial step in defining the reward function that guides the learning process.
- **p. 9 / 3.5. Training Process - extractive body cue:** HIL-SERL: Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning trained reward classifier generally achieves an accuracy of greater than 95% in the evaluation data ...
- **p. 4 / 3.1. Preliminaries and Problem Statement - extractive body cue:** Robotic reinforcement learning tasks can be defined via an MDP = {, , 𝜌, , 𝑟, 𝛾}, where 𝐬∈is the state observation (e.g., an image ...

## Design Rationale

- **p. 3 / 1. Introduction - extractive body cue:** To assess the effectiveness of our system, we compare it against several state-of-the-art RL methods and conduct ablation studies to understand the contribution of each ...
- **p. 3 / 1. Introduction - extractive body cue:** In summary, our contributions demonstrate that with the appropriate system-level design choices, RL can effectively solve a wide range of dexterous and complex vision-based manipulation ...
- **p. 1 / 1. Introduction - extractive body cue:** However, developing general-purpose vision-based methods that can efficiently acquire physically complex skills, with proficiency exceeding imitation learning and hand-designed controllers, has been comparatively difficult.

## Source Evidence Cues

- **p. 9 / 3.5. Training Process - extractive body cue:** Finally, we start the policy training process.
- **p. 9 / 3.5. Training Process - extractive body cue:** Such an intervention strategy will cause the overestimation of the value function, particularly in the early stages of the training process; which can result in ...
- **p. 8 / 3.5. Training Process - extractive body cue:** This is approximately equivalent to 10 human trajectories, assuming each trajectory takes about 10 seconds.
- **p. 8 / 3.5. Training Process - extractive body cue:** For all cameras, we perform image cropping to focus on the area of interest and resize the images to 128x128 for the neural network to ...
- **Detected method headings:** 5.2. Reactive Policy and Predictive Policy (p. 19)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data schema / normalization | heterogeneous robot trajectory를 공통 sample로 만든다 | observation, action, task와 embodiment metadata | sensor/action schema alignment, filtering, normalization을 수행 | shared dataset representation | Finally, we start the policy training process. | p. 9 (3.5. Training Process), p. 9 (3.5. Training Process) |
| Coverage / augmentation | task·embodiment·failure variation을 확장한다 | dataset과 metadata | retargeting, relabeling, synthetic/teleoperation augmentation 또는 sampling을 적용 | expanded data support | Such an intervention strategy will cause the overestimation of the value function, particularly in the early stages of the training process; which ... | p. 9 (3.5. Training Process), p. 8 (3.5. Training Process) |
| Downstream learning interface | 정규화된 data를 policy/representation이 사용한다 | shared observations/actions | pretraining, BC, action-token 또는 representation learning을 수행 | checkpoint/policy action | This is approximately equivalent to 10 human trajectories, assuming each trajectory takes about 10 seconds. | p. 8 (3.5. Training Process), p. 8 (3.5. Training Process) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 8 / 3.5. Training Process - extractive body cue:** Additionally, we may collect extra data to address any false negative and false positive issues with the reward classifier.
- **p. 8 / 3.5. Training Process - extractive body cue:** Next, we collect data to train the reward classifier, which is a crucial step in defining the reward function that guides the learning process.
- **p. 9 / 3.5. Training Process - extractive body cue:** HIL-SERL: Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning trained reward classifier generally achieves an accuracy of greater than 95% in the evaluation data ...
- **p. 9 / 3.5. Training Process - extractive body cue:** Such an intervention strategy will cause the overestimation of the value function, particularly in the early stages of the training process; which can result in ...
- **Formal bridge:** trajectory D with task/embodiment metadata -> normalized sample or downstream action -> coverage/data efficiency/transfer objective -> cross-domain transfer and task performance.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Robotic, reinforcement, learning, tasks, defined, MDP, where, state, observation, image, combination, robot, proprioceptive, information | multi-view observation, language/task label과 action trajectory | body cue; exact tensor/frame verify |
| State/latent | Robotic, reinforcement, learning, tasks, defined, MDP, where, state, observation, image | shared representation, embodiment/task identity와 data distribution | body cue; notation verify |
| Action/output | assess, effectiveness, system, compare, against, several, state-of-the-art, methods, conduct, ablation | dataset sample 또는 learned policy action | body cue; unit/decoder verify |
| Objective/constraint | Additionally, collect, extra, data, address, false, negative, positive, issues, reward | coverage/data efficiency/transfer objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.1. Preliminaries and Problem Statement - extractive body cue:** Robotic reinforcement learning tasks can be defined via an MDP = {, , 𝜌, , 𝑟, 𝛾}, where 𝐬∈is the state observation (e.g., an image ...
- **p. 5 / 3.1. Preliminaries and Problem Statement - extractive body cue:** To implement reinforcement learning algorithms for robotic tasks, we must carefully select appropriate state observation spaces and action spaces .
- **p. 5 / 3.1. Preliminaries and Problem Statement - extractive body cue:** HIL-SERL: Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning state distribution, transition probabilities, and policy 𝜋.
- **p. 2 / 1. Introduction - extractive body cue:** These tasks present significant challenges in terms of complex and intricate dynamics, high-dimensional state and action spaces, long horizons, or combinations thereof.
- **p. 4 / 3.1. Preliminaries and Problem Statement - extractive body cue:** An optimal policy 𝜋is one that maximizes the cumulative expected value of the reward, i.e., 𝐸[∑𝐻 𝑡=0 𝛾𝑡𝑟(𝐬𝑡, 𝐚𝑡)], where the expectation is taken with ...
- **p. 3 / 1. Introduction - extractive body cue:** This analysis explores why RL achieves a near-perfect success rate, and further examines the flexibility of RL policies to serve as a general-purpose vision-based policy ...
- **p. 3 / 1. Introduction - extractive body cue:** Notably, our system is, to the best of our knowledge, the first to achieve dual-arm coordination with image inputs using RL in real-world settings, as ...
- **Normalized interface:** observation=multi-view observation, language/task label과 action trajectory; state=shared representation, embodiment/task identity와 data distribution; output/action=dataset sample 또는 learned policy action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | trajectory demonstration horizon; training sample window와 deployment task horizon을 분리한다. | Specifically, we report the intervention rate, for which we calculate the ratio of intervened timesteps to total timesteps within an episode and ... | episode/sequence/action-chunk boundary |
| Rate / latency | data recording/action sampling rate와 policy inference/control rate를 분리한다. | For an autonomous rollout trajectory from time step 𝑡0 to 𝑡𝑁, a human can intervene at any time step 𝑡𝑖 where 𝑡0 ... | Hz/fps, inference time and control rate |
| Memory | trajectory, embodiment/task metadata와 dataset index. | not recovered | window and reset |
| Compute | data decoding, normalization/augmentation과 downstream training budget이 결정한다. | Specifically, we report the intervention rate, for which we calculate the ratio of intervened timesteps to total timesteps within an episode and ... | hardware, batch and throughput |

## Training vs Inference

- **p. 9 / 3.5. Training Process - extractive body cue:** Finally, we start the policy training process.
- **p. 9 / 3.5. Training Process - extractive body cue:** Such an intervention strategy will cause the overestimation of the value function, particularly in the early stages of the training process; which can result in ...
- **p. 13 / 4.3. Experimental Results - extractive body cue:** The training time includes all scripted motion, policy rollouts, intended stops, as well as onboard computation which is carried on a single NVIDIA RTX 4090 ...
- **p. 14 / 4.3. Experimental Results - extractive body cue:** We then run this policy and collect human expert corrections, such that the total amount of trials and interventions matches RL training.
- **p. 13 / 4.3. Experimental Results - extractive body cue:** For each task, we report the success rate, cycle time, and training time.
- **p. 15 / 4.3. Experimental Results - extractive body cue:** Additionally, it achieves such performance within practical training times, even for highdimensional observations and action spaces, such as those required for bimanual manipulation.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Finally, start, policy, training, process, intervention, strategy, will, cause, overestimation, value, function, particularly, early, stages, result, unstable, dynamics, approximately, equivalent.
- **Relevant PDF headings:** 5.2. Reactive Policy and Predictive Policy (p. 19).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data schema / normalization | Each task also uses either a scripted robot motion or manually human reset to randomize the initial state of the task. | p. 9 (4.1. Overview of Experiments), p. 9 (4.1. Overview of Experiments) |
| Coverage / augmentation | In the remainder of this section, we will first describe each task in detail, and present relevant results as well as comparisons ... | p. 9 (4.1. Overview of Experiments), p. 13 (4.3. Experimental Results) |
| Downstream learning interface | This is a significant improvement over the HG-DAgger baseline, which achieved an average success rate of 49.7% across all tasks. | p. 15 (4.3. Experimental Results), p. 15 (4.3. Experimental Results) |

## Failure and Ablation Link

- **p. 13 / 4.3. Experimental Results - extractive body cue:** Our method is also ablated with two versions: one initialized from scratch without demonstrations or corrections, and another initialized from demonstrations but without corrections.
- **p. 14 / 4.3. Experimental Results - extractive body cue:** DAgger and its variants (Ross et al., 2011; Kelly et al., 2018) address this problem by incorporating human corrections to refine the policy through supervised ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 4: Illustrations of the tasks in our experiments. (A)-(E) A sequence of motherboard assembly tasks: SSD installation, RAM insertion, USB cable grasping and insertion ...
- **p. 9 / 4.1. Overview of Experiments - extractive body cue:** These tasks encompass a range of manipulation challenges, including dynamic object manipulation (e.g., flipping an object in a pan), precise and delicate manipulation (e.g., inserting ...
- **p. 14 / 4.3. Experimental Results - extractive body cue:** We first pretrain a base policy with behavioral cloning (BC) using an equivalent amount of offline human demonstrations as provided to our method.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2: Overview of HIL-SERL. This figure illustrates the architecture of HIL-SERL, which comprises three primary components: the actor process, the learner process, and replay ...
- **p. 21 / 6. Discussion - extractive body cue:** We also see some limitations of our approach.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 9 (3.5. Training Process), p. 9 (3.5. Training Process), p. 8 (3.5. Training Process), p. 8 (3.5. Training Process), objective p. 8 (3.5. Training Process), p. 8 (3.5. Training Process), p. 9 (3.5. Training Process), p. 9 (3.5. Training Process), temporal p. 15 (4.3. Experimental Results), p. 7 (3.4. Human-in-the-Loop Reinforcement Learning), p. 19 (5.2. Reactive Policy and Predictive Policy), p. 9 (4.1. Overview of Experiments), p. 13 (4.3. Experimental Results), p. 13 (4.3. Experimental Results).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
