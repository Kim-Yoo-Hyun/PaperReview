# Method - RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p028.html; PDF retrieval source: https://arxiv.org/pdf/2412.09858. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3.3. Generalist Policy Finetuning), p. 4 (3.1. Online RL Training), p. 4 (3.3. Generalist Policy Finetuning), p. 5 (3.3. Generalist Policy Finetuning)): To predict an action, the transformer backbone takes in the tokenized observation and goal, then outputs a readout embedding 𝑒, which is used to condition the denoising process trained on ...

## Method Body Digest

- **p. 5 / 3.3. Generalist Policy Finetuning - extractive body cue:** To predict an action, the transformer backbone takes in the tokenized observation and goal, then outputs a readout embedding 𝑒, which is used to condition ...
- **p. 4 / 3.1. Online RL Training - extractive body cue:** We can formulate each robotic task as a Markov Decision Process (MDP), where the state 𝑠𝑡consists of RGB images and proprioceptive information, and actions 𝑎𝑡represent ...
- **p. 4 / 3.3. Generalist Policy Finetuning - extractive body cue:** Specifically, suppose we have a pre-trained policy 𝜋0, we fine-tune it with taskspecific dataset 𝐷(𝑠𝑡,𝑎𝑡) with the following supervised learning objective: (𝜃) = -𝔼(𝑠𝑡,𝑎𝑡)∼[log 𝜋𝜃(𝑎𝑡/𝑠𝑡)] ...
- **p. 5 / 3.3. Generalist Policy Finetuning - extractive body cue:** To fine-tune the model on our RL-generated dataset, we use the public model weights pre-trained on 970 thousand Open X-Embodiment dataset (Collaboration et al., 2024) ...
- **p. 4 / 3.1. Online RL Training - extractive body cue:** The policy objective 𝜋(𝑎𝑡/𝑠𝑡) is to maximize the expected discounted return: 𝐽(𝜋) = 𝔼 𝑠0∼𝜌0 𝑎𝑡∼𝜋(𝑎𝑡/𝑠𝑡) 𝑠𝑡+1∼𝑃(𝑠𝑡+1/𝑠𝑡,𝑎𝑡) [ 𝑇 ∑ 𝑡=0 𝛾𝑡𝑅(𝑠𝑡, 𝑎𝑡)] (1) where ...
- **p. 4 / 3.1. Online RL Training - extractive body cue:** It incorporates human interventions with RLPD (Ball et al., 2023) to efficiently learn visuomotor policies that consistently achieve 100% success rate by maximizing (1).
- **p. 5 / 3.3. Generalist Policy Finetuning - extractive body cue:** RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning are discretized into 256 bins per dimension autoregressively using the standard cross-entropy loss.
- **p. 4 / 3.3. Generalist Policy Finetuning - extractive body cue:** It takes a single image as observation input along with a language instruction.

## Design Rationale

- **p. 1 / 1. Introduction - extractive body cue:** To tackle this challenge, we propose Reinforcement Learning Distilled Generalist (RLDG), a simple yet effective method that leverages reinforcement learning to generate high-quality training data ...
- **p. 4 / 3.3. Generalist Policy Finetuning - extractive body cue:** Specifically, suppose we have a pre-trained policy 𝜋0, we fine-tune it with taskspecific dataset 𝐷(𝑠𝑡,𝑎𝑡) with the following supervised learning objective: (𝜃) = -𝔼(𝑠𝑡,𝑎𝑡)∼[log 𝜋𝜃(𝑎𝑡/𝑠𝑡)] ...
- **p. 4 / 3.1. Online RL Training - extractive body cue:** We can formulate each robotic task as a Markov Decision Process (MDP), where the state 𝑠𝑡consists of RGB images and proprioceptive information, and actions 𝑎𝑡represent ...

## Source Evidence Cues

- **p. 5 / 3.3. Generalist Policy Finetuning - extractive body cue:** To predict an action, the transformer backbone takes in the tokenized observation and goal, then outputs a readout embedding 𝑒, which is used to condition ...
- **p. 4 / 3.1. Online RL Training - extractive body cue:** We can formulate each robotic task as a Markov Decision Process (MDP), where the state 𝑠𝑡consists of RGB images and proprioceptive information, and actions 𝑎𝑡represent ...
- **p. 4 / 3.3. Generalist Policy Finetuning - extractive body cue:** Specifically, suppose we have a pre-trained policy 𝜋0, we fine-tune it with taskspecific dataset 𝐷(𝑠𝑡,𝑎𝑡) with the following supervised learning objective: (𝜃) = -𝔼(𝑠𝑡,𝑎𝑡)∼[log 𝜋𝜃(𝑎𝑡/𝑠𝑡)] ...
- **p. 5 / 3.3. Generalist Policy Finetuning - extractive body cue:** To fine-tune the model on our RL-generated dataset, we use the public model weights pre-trained on 970 thousand Open X-Embodiment dataset (Collaboration et al., 2024) ...
- **Detected method headings:** 1. RL Policy Training (p. 2); 3.3. Generalist Policy Finetuning (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data schema / normalization | heterogeneous robot trajectory를 공통 sample로 만든다 | observation, action, task와 embodiment metadata | sensor/action schema alignment, filtering, normalization을 수행 | shared dataset representation | To predict an action, the transformer backbone takes in the tokenized observation and goal, then outputs a readout embedding 𝑒, which is ... | p. 5 (3.3. Generalist Policy Finetuning), p. 4 (3.1. Online RL Training) |
| Coverage / augmentation | task·embodiment·failure variation을 확장한다 | dataset과 metadata | retargeting, relabeling, synthetic/teleoperation augmentation 또는 sampling을 적용 | expanded data support | We can formulate each robotic task as a Markov Decision Process (MDP), where the state 𝑠𝑡consists of RGB images and proprioceptive information, ... | p. 4 (3.1. Online RL Training), p. 4 (3.3. Generalist Policy Finetuning) |
| Downstream learning interface | 정규화된 data를 policy/representation이 사용한다 | shared observations/actions | pretraining, BC, action-token 또는 representation learning을 수행 | checkpoint/policy action | Specifically, suppose we have a pre-trained policy 𝜋0, we fine-tune it with taskspecific dataset 𝐷(𝑠𝑡,𝑎𝑡) with the following supervised learning objective: (𝜃) ... | p. 4 (3.3. Generalist Policy Finetuning), p. 5 (3.3. Generalist Policy Finetuning) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.1. Online RL Training - extractive body cue:** The policy objective 𝜋(𝑎𝑡/𝑠𝑡) is to maximize the expected discounted return: 𝐽(𝜋) = 𝔼 𝑠0∼𝜌0 𝑎𝑡∼𝜋(𝑎𝑡/𝑠𝑡) 𝑠𝑡+1∼𝑃(𝑠𝑡+1/𝑠𝑡,𝑎𝑡) [ 𝑇 ∑ 𝑡=0 𝛾𝑡𝑅(𝑠𝑡, 𝑎𝑡)] (1) where ...
- **p. 4 / 3.1. Online RL Training - extractive body cue:** It incorporates human interventions with RLPD (Ball et al., 2023) to efficiently learn visuomotor policies that consistently achieve 100% success rate by maximizing (1).
- **p. 5 / 3.3. Generalist Policy Finetuning - extractive body cue:** RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning are discretized into 256 bins per dimension autoregressively using the standard cross-entropy loss.
- **p. 5 / 3.3. Generalist Policy Finetuning - extractive body cue:** To predict an action, the transformer backbone takes in the tokenized observation and goal, then outputs a readout embedding 𝑒, which is used to condition ...
- **Formal bridge:** trajectory D with task/embodiment metadata -> normalized sample or downstream action -> coverage/data efficiency/transfer objective -> cross-domain transfer and task performance.
- **Equation/algorithm anchors:** p. 4 (3.1. Online RL Training), p. 4 (3.3. Generalist Policy Finetuning), p. 5 (3.3. Generalist Policy Finetuning), p. 5 (3.3. Generalist Policy Finetuning).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | takes, single, image, observation, input, along, language, instruction, Octo, another, open-source, generalist, robotic, policy | multi-view observation, language/task label과 action trajectory | body cue; exact tensor/frame verify |
| State/latent | takes, single, image, observation, input, along, language, instruction, Octo, another | shared representation, embodiment/task identity와 data distribution | body cue; notation verify |
| Action/output | tackle, challenge, Reinforcement, Learning, Distilled, Generalist, RLDG, simple, effective, leverages | dataset sample 또는 learned policy action | body cue; unit/decoder verify |
| Objective/constraint | policy, objective, maximize, expected, discounted, return, where, defines, initial, robot | coverage/data efficiency/transfer objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.3. Generalist Policy Finetuning - extractive body cue:** It takes a single image as observation input along with a language instruction.
- **p. 5 / 3.3. Generalist Policy Finetuning - extractive body cue:** Octo is another open-source generalist robotic policy, designed to adapt to diverse sensory inputs and action spaces efficiently.
- **p. 5 / 3.3. Generalist Policy Finetuning - extractive body cue:** To predict an action, the transformer backbone takes in the tokenized observation and goal, then outputs a readout embedding 𝑒, which is used to condition ...
- **p. 4 / 3.1. Online RL Training - extractive body cue:** We can formulate each robotic task as a Markov Decision Process (MDP), where the state 𝑠𝑡consists of RGB images and proprioceptive information, and actions 𝑎𝑡represent ...
- **p. 2 / 1. Introduction - extractive body cue:** RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning Use case 2: RL on Sub-Task Use case 1: Multiple RL Policies
- **p. 1 / 1. Introduction - extractive body cue:** By leveraging Internet-scale pretraining and grounding with robot actions, these models can achieve zero-shot and few-shot generalization across various domains.
- **p. 1 / 1. Introduction - extractive body cue:** These tasks demand fine-grained, reactive control to succeed, making the quality and consistency of demonstration data even more crucial for effective policy learning.
- **Normalized interface:** observation=multi-view observation, language/task label과 action trajectory; state=shared representation, embodiment/task identity와 data distribution; output/action=dataset sample 또는 learned policy action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | trajectory demonstration horizon; training sample window와 deployment task horizon을 분리한다. | There is a single RealSense D405 camera mounted on the robot's wrist for image observations. frame and 1 binary gripper action for ... | episode/sequence/action-chunk boundary |
| Rate / latency | data recording/action sampling rate와 policy inference/control rate를 분리한다. | For a fair comparison, we use the same task setup, training configuration, observation and action space, and the number of successful episodes ... | Hz/fps, inference time and control rate |
| Memory | trajectory, embodiment/task metadata와 dataset index. | not recovered | window and reset |
| Compute | data decoding, normalization/augmentation과 downstream training budget이 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.3. Generalist Policy Finetuning - extractive body cue:** To predict an action, the transformer backbone takes in the tokenized observation and goal, then outputs a readout embedding 𝑒, which is used to condition ...
- **p. 4 / 3.3. Generalist Policy Finetuning - extractive body cue:** Specifically, suppose we have a pre-trained policy 𝜋0, we fine-tune it with taskspecific dataset 𝐷(𝑠𝑡,𝑎𝑡) with the following supervised learning objective: (𝜃) = -𝔼(𝑠𝑡,𝑎𝑡)∼[log 𝜋𝜃(𝑎𝑡/𝑠𝑡)] ...
- **p. 5 / 3.3. Generalist Policy Finetuning - extractive body cue:** To fine-tune the model on our RL-generated dataset, we use the public model weights pre-trained on 970 thousand Open X-Embodiment dataset (Collaboration et al., 2024) ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** predict, action, transformer, backbone, takes, tokenized, observation, goal, then, outputs, readout, embedding, condition, denoising, process, trained, standard, DDPM, objective, formulate.
- **Relevant PDF headings:** 1. RL Policy Training (p. 2); 3.3. Generalist Policy Finetuning (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data schema / normalization | We also use the single object insertion task of FMB (Luo et al., 2024c), a common and reproducible benchmark for comparing robotic ... | p. 6 (4.1. Experimental Setup and Tasks), p. 5 (4.1. Experimental Setup and Tasks) |
| Coverage / augmentation | On the precise FMB Insertion and Connector Insertion tasks, where we anticipated the generalist to benefit the most from higher quality training ... | p. 6 (4.2. RLDG vs. Conventional Fine-tuning), p. 7 (4.2. RLDG vs. Conventional Fine-tuning) |
| Downstream learning interface | When evaluated on seen (VGA) and unseen (Type C) Connector Insertion tasks, RLDG shows superior sample efficiency, requiring significantly fewer demonstrations to ... | p. 7 (4.2. RLDG vs. Conventional Fine-tuning), p. 7 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / 4.2. RLDG vs. Conventional Fine-tuning - extractive body cue:** To further investigate the effectiveness of RLDG, we conduct a scaling experiment studying the success rate of OpenVLA policies on a seen VGA connector and ...
- **p. 9 / 5.1. Is RL data better because of better action - extractive body cue:** Human demonstration policies often maintained contact pressure without necessary exploratory movements.
- **p. 5 / 4.1. Experimental Setup and Tasks - extractive body cue:** For the generalist policies, we fine-tune only using the wrist camera image as input.
- **p. 6 / 4.2. RLDG vs. Conventional Fine-tuning - extractive body cue:** For each task, we fine-tune OpenVLA and Octo on RL-generated data as described in Sec.
- **p. 6 / 4.2. RLDG vs. Conventional Fine-tuning - extractive body cue:** In this section, we seek to answer Question 1 by comparing generalist policies fine-tuned using RLDG and standard generalist fine-tuning via imitation learning.
- **p. 7 / 4.2. RLDG vs. Conventional Fine-tuning - extractive body cue:** These results strongly suggest that fine-tuning generalist policies using RLDG is more sample-efficient and leads to higher performance than human demonstrations for both in-distribution and ...
- **p. 8 / 4.3. Generalization of RLDG vs. Original RL - extractive body cue:** RL data consistently provide better fine-tuning performance than human data.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3.3. Generalist Policy Finetuning), p. 4 (3.1. Online RL Training), p. 4 (3.3. Generalist Policy Finetuning), p. 5 (3.3. Generalist Policy Finetuning), objective p. 4 (3.1. Online RL Training), p. 4 (3.1. Online RL Training), p. 5 (3.3. Generalist Policy Finetuning), p. 5 (3.3. Generalist Policy Finetuning), temporal p. 5 (4.1. Experimental Setup and Tasks), p. 6 (4.2. RLDG vs. Conventional Fine-tuning), p. 7 (4.2. RLDG vs. Conventional Fine-tuning), p. 7 (4.2. RLDG vs. Conventional Fine-tuning), p. 8 (4.3. Generalization of RLDG vs. Original RL), p. 8 (4.2. RLDG vs. Conventional Fine-tuning).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
