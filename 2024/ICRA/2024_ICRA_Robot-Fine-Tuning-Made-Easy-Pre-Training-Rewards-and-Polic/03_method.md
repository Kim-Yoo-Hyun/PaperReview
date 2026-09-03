# Method - Robot Fine-Tuning Made Easy: Pre-Training Rewards and Policies for Autonomous Real-World Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ieeexplore.ieee.org/document/10610421/; PDF retrieval source: https://arxiv.org/pdf/2310.15145. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (IV. ROBOFUME), p. 1 (I. INTRODUCTION), p. 4 (IV. ROBOFUME), p. 4 (IV. ROBOFUME), p. 1 (I. INTRODUCTION), p. 3 (IV. ROBOFUME)): The policy then takes as inputs a concatenation of the encoded image observation ϕ(simg), task representation z, and proprioceptive information sp, processes the concatenated vector through an MLP, and produces ...

## Method Body Digest

- **p. 3 / IV. ROBOFUME - extractive body cue:** The policy then takes as inputs a concatenation of the encoded image observation ϕ(simg), task representation z, and proprioceptive information sp, processes the concatenated vector ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Pretraining a policy with offline reinforcement learning and then fine-tuning it with online reinforcement learning is a natural way to implement this paradigm in robotics.
- **p. 4 / IV. ROBOFUME - extractive body cue:** We design a VLM-based reward model that takes the current observation and the task name as input and outputs a binary label of whether the ...
- **p. 4 / IV. ROBOFUME - extractive body cue:** Leveraging existing vision-language models offers a number of benefits compared to utilizing a pre-trained visual representation or training a reward model from scratch using in-domain ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In many domains that involve machine learning, a widely successful paradigm for learning task-specific models is to first pre-train a general-purpose model from an existing ...
- **p. 3 / IV. ROBOFUME - extractive body cue:** Since we use image observations, we additionally train an encoder ϕ(simg) that projects the images into a lower-dimensional space before giving them as inputs to ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Meanwhile, the agent uses the pre-trained VLM model as a surrogate reward for updating the policy.
- **p. 4 / IV. ROBOFUME - extractive body cue:** The VLM outputs a sparse binary reward, returning success if the ‘yes' token has a higher probability than ‘no' token.

## Design Rationale

- **p. 3 / III. PRELIMINARIES - extractive body cue:** Our method assumes access to a prior dataset Dprior = ∪N j=1Dj = ∪N j=1{(sj i, aj i, s′j i )}K i=1, which consists of ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** 1: We propose a system that enables autonomous and efficient real-world robot learning.
- **p. 1 / Abstract - extractive body cue:** In a diverse set of five real robot manipulation tasks, we show that our method can incorporate data from an existing robot dataset collected at ...

## Source Evidence Cues

- **p. 3 / IV. ROBOFUME - extractive body cue:** The policy then takes as inputs a concatenation of the encoded image observation ϕ(simg), task representation z, and proprioceptive information sp, processes the concatenated vector ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Pretraining a policy with offline reinforcement learning and then fine-tuning it with online reinforcement learning is a natural way to implement this paradigm in robotics.
- **p. 4 / IV. ROBOFUME - extractive body cue:** We design a VLM-based reward model that takes the current observation and the task name as input and outputs a binary label of whether the ...
- **p. 4 / IV. ROBOFUME - extractive body cue:** Leveraging existing vision-language models offers a number of benefits compared to utilizing a pre-trained visual representation or training a reward model from scratch using in-domain ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In many domains that involve machine learning, a widely successful paradigm for learning task-specific models is to first pre-train a general-purpose model from an existing ...
- **p. 3 / IV. ROBOFUME - extractive body cue:** Since we use image observations, we additionally train an encoder ϕ(simg) that projects the images into a lower-dimensional space before giving them as inputs to ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Meanwhile, the agent uses the pre-trained VLM model as a surrogate reward for updating the policy.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Fixed-data support | 온라인 탐색 없이 transition/action 분포를 정의한다 | offline trajectories와 metadata | dataset support, behavior distribution과 task return을 정리 | training batch/support | The policy then takes as inputs a concatenation of the encoded image observation ϕ(simg), task representation z, and proprioceptive information sp, processes ... | p. 3 (IV. ROBOFUME), p. 1 (I. INTRODUCTION) |
| Value / uncertainty update | dataset 밖 action의 과대추정을 억제한다 | batch transition과 value parameters | conservative, implicit, uncertainty 또는 behavior-regularized update를 수행 | Q/V/uncertainty estimate | Pretraining a policy with offline reinforcement learning and then fine-tuning it with online reinforcement learning is a natural way to implement this ... | p. 1 (I. INTRODUCTION), p. 4 (IV. ROBOFUME) |
| Policy extraction / deployment | 학습된 value를 실행 action으로 변환한다 | value와 behavior support | argmax, advantage weighting, sequence decoding 또는 constraint filtering을 적용 | dataset-supported action | We design a VLM-based reward model that takes the current observation and the task name as input and outputs a binary label ... | p. 4 (IV. ROBOFUME), p. 4 (IV. ROBOFUME) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / IV. ROBOFUME - extractive body cue:** The VLM outputs a sparse binary reward, returning success if the ‘yes' token has a higher probability than ‘no' token.
- **p. 3 / IV. ROBOFUME - extractive body cue:** The encoder ϕ is a 4-layer CNN, and is optimized exclusively against the critic loss.
- **p. 3 / IV. ROBOFUME - extractive body cue:** The weight of the BC regularization term is chosen such that the scales of the RL loss and the BC loss are similar throughout the ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Then, we fine-tune the pre-trained policy online reset-free with the VLM reward model.
- **p. 1 / Abstract - extractive body cue:** We also demonstrate in simulation experiments that our method outperforms prior works that use different RL algorithms or different approaches for predicting rewards.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Meanwhile, the agent uses the pre-trained VLM model as a surrogate reward for updating the policy.
- **Formal bridge:** dataset transition (s,a,r,s′) -> dataset-supported policy action -> offline value with OOD control -> offline return and deployment safety.
- **Equation/algorithm anchors:** p. 3 (IV. ROBOFUME), p. 3 (IV. ROBOFUME), p. 1 (Body text (section boundary not confidently recovered)), p. 4 (IV. ROBOFUME), p. 4 (IV. ROBOFUME).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | policy, then, takes, inputs, concatenation, encoded, image, observation, simg, task, representation, proprioceptive, information, processes | dataset state/observation, action, reward와 return-to-go | body cue; exact tensor/frame verify |
| State/latent | policy, then, takes, inputs, concatenation, encoded, image, observation, simg, task | Q/value 또는 sequence-policy state | body cue; notation verify |
| Action/output | assumes, access, prior, dataset, Dprior, consists, demonstrations, different, tasks, system | dataset-supported action sequence | body cue; unit/decoder verify |
| Objective/constraint | VLM, outputs, sparse, binary, reward, returning, success, token, higher, probability | offline value with OOD control | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / IV. ROBOFUME - extractive body cue:** The policy then takes as inputs a concatenation of the encoded image observation ϕ(simg), task representation z, and proprioceptive information sp, processes the concatenated vector ...
- **p. 4 / IV. ROBOFUME - extractive body cue:** We design a VLM-based reward model that takes the current observation and the task name as input and outputs a binary label of whether the ...
- **p. 3 / III. PRELIMINARIES - extractive body cue:** The failure states D/ consist entirely of image observations that correspond to unsuccessful states and are collected to aid with the VLM reward learning.
- **p. 4 / IV. ROBOFUME - extractive body cue:** When the VLM predicts the task has been completed successfully, we terminate the episode and switch the language instruction for the policy to complete the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In the fine-tuning phase, a robot adapts the policy in the real world autonomously by alternating between attempting the task and attempting to reset the ...
- **p. 1 / Abstract - extractive body cue:** Our insights are to utilize calibrated offline reinforcement learning techniques to ensure efficient online finetuning of a pre-trained policy in the presence of distribution shifts ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Pretraining a policy with offline reinforcement learning and then fine-tuning it with online reinforcement learning is a natural way to implement this paradigm in robotics.
- **Normalized interface:** observation=dataset state/observation, action, reward와 return-to-go; state=Q/value 또는 sequence-policy state; output/action=dataset-supported action sequence.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | offline trajectory/discounted return horizon; deployment horizon과 분리한다. | For all methods that require online experience, we reset the environment every 1,000 environment steps, i.e. every 25 episodes of interactions. | episode/sequence/action-chunk boundary |
| Rate / latency | training은 batch update, inference는 environment control tick; exact values 확인 필요. | Our method significantly improves over both offline-only and BC performance after 30k steps of online interaction (2-4 hours). | Hz/fps, inference time and control rate |
| Memory | fixed dataset, value/policy parameters와 optional context/history. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | dataset size, conservative/value update와 sequence/action decoding이 비용을 결정한다. | For all methods that require online experience, we reset the environment every 1,000 environment steps, i.e. every 25 episodes of interactions. | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / I. INTRODUCTION - extractive body cue:** Pretraining a policy with offline reinforcement learning and then fine-tuning it with online reinforcement learning is a natural way to implement this paradigm in robotics.
- **p. 4 / IV. ROBOFUME - extractive body cue:** Leveraging existing vision-language models offers a number of benefits compared to utilizing a pre-trained visual representation or training a reward model from scratch using in-domain ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In many domains that involve machine learning, a widely successful paradigm for learning task-specific models is to first pre-train a general-purpose model from an existing ...
- **p. 3 / IV. ROBOFUME - extractive body cue:** Since we use image observations, we additionally train an encoder ϕ(simg) that projects the images into a lower-dimensional space before giving them as inputs to ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Meanwhile, the agent uses the pre-trained VLM model as a surrogate reward for updating the policy.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Our method significantly improves over both offline-only and BC performance after 30k steps of online interaction (2-4 hours).

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** policy, then, takes, inputs, concatenation, encoded, image, observation, simg, task, representation, proprioceptive, information, processes, concatenated, vector, through, MLP, produces, output.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Fixed-data support | Similarly, we find that one-hot task encodings perform substantially worse than language-conditioned policies, as the prior dataset used in real-robot training is ... | p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Value / uncertainty update | In all simulation tasks, our method ROBOFUME consistently outperforms prior methods, achieving success rates at least 20% higher than all baselines within ... | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Policy extraction / deployment | After 30k steps of autonomous online interaction, our method shows relative improvement of 51% upon the pre-trained performance, and outperforms BC by ... | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 5 / V. EXPERIMENTS - extractive body cue:** Simulation Experiments and Ablations We use a suite of simulated robotic manipulation environments to ablate contributions of different components of our algorithm.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Ablations on RL Algorithm Design Choices.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** When pre-training without using prior data, that is, exclusively using target data, our method is able to sweep less than half the amount of candies ...
- **p. 4 / V. EXPERIMENTS - extractive body cue:** And, how does each component of ROBOFUME or data affect the performance of our method?
- **p. 6 / V. EXPERIMENTS - extractive body cue:** The metrics are computed on the data collected during fine-tuning against a hand-engineered ground truth reward.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We propose a system that enables autonomous and efficient real-world robot learning. First, we pre-train a multi-task policy and fine-tune a pre-trained Vision-Language ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** All tasks use 50 forward and 50 backward demos for the target task, and fewer than 20 combined trajectories of failures.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (IV. ROBOFUME), p. 1 (I. INTRODUCTION), p. 4 (IV. ROBOFUME), p. 4 (IV. ROBOFUME), p. 1 (I. INTRODUCTION), p. 3 (IV. ROBOFUME), objective p. 4 (IV. ROBOFUME), p. 3 (IV. ROBOFUME), p. 3 (IV. ROBOFUME), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Abstract), p. 2 (I. INTRODUCTION), temporal p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 2 (II. RELATED WORK), p. 4 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** The policy then takes as inputs a concatenation of the encoded image observation ϕ(simg), task representation z, and proprioceptive information sp, processes the concatenated vector through an MLP, and produces ... (p. 3, IV. ROBOFUME).
- **Objective/update evidence:** The encoder ϕ is a 4-layer CNN, and is optimized exclusively against the critic loss. (p. 3, IV. ROBOFUME).
- **Temporal/runtime evidence:** For all methods that require online experience, we reset the environment every 1,000 environment steps, i.e. every 25 episodes of interactions. (p. 5, V. EXPERIMENTS).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
