# RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p028.html.
> PDF retrieval source: https://arxiv.org/pdf/2412.09858. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Reinforcement Learning, generalist policy, policy distillation, robot data, real-world manipulation
- Official paper: https://www.roboticsproceedings.org/rss21/p028.html
- Full-text retrieval: https://arxiv.org/pdf/2412.09858
- Code/Project: https://generalist-distillation.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 robot_data 문제를 이해하기 위해 읽는다. 본문은 While directly finetuning foundation models with reinforcement learning is possible in principle, it presents significant challenges including optimization instability, computational costs, and potential catastrophic forgetting of pre-t ...를 문제로 두고, To tackle this challenge, we propose Reinforcement Learning Distilled Generalist (RLDG), a simple yet effective method that leverages reinforcement learning to generate high-quality training data for robotic foundation models.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1. Introduction - extractive body cue:** Recent advances in robotic foundation models have demonstrated impressive capabilities in understanding and executing diverse manipulation skills (Collaboration et al., 2024; Brohan et al., 2023b;a; ...
- **p. 1 / 1. Introduction - extractive body cue:** By leveraging Internet-scale pretraining and grounding with robot actions, these models can achieve zero-shot and few-shot generalization across various domains.
- **p. 1 / 1. Introduction - extractive body cue:** Deploying these models typically requires fine-tuning them with task-specific data to adapt to the target task or domain.
- **p. 1 / 1. Introduction - extractive body cue:** The quality of this fine-tuning data is therefore critical to the performance of the resulting policies.
- **p. 1 / 1. Introduction - extractive body cue:** While human teleoperation is a common and accessible source for such data, human demonstrations often contain inconsistencies in execution quality and style.
- **p. 1 / 1. Introduction - extractive body cue:** While directly finetuning foundation models with reinforcement learning is possible in principle, it presents significant challenges including optimization instability, computational costs, and potential catastrophic forgetting ...
- **p. 1 / 1. Introduction - extractive body cue:** This challenge affects all robotic tasks but becomes particularly pronounced in scenarios requiring precise control and dexterity, such as contact-rich manipulation.

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** To tackle this challenge, we propose Reinforcement Learning Distilled Generalist (RLDG), a simple yet effective method that leverages reinforcement learning to generate high-quality training data ...
- **p. 4 / 3.3. Generalist Policy Finetuning - extractive body cue:** Specifically, suppose we have a pre-trained policy 𝜋0, we fine-tune it with taskspecific dataset 𝐷(𝑠𝑡,𝑎𝑡) with the following supervised learning objective: (𝜃) = -𝔼(𝑠𝑡,𝑎𝑡)∼[log 𝜋𝜃(𝑎𝑡/𝑠𝑡)] ...
- **p. 4 / 3.1. Online RL Training - extractive body cue:** We can formulate each robotic task as a Markov Decision Process (MDP), where the state 𝑠𝑡consists of RGB images and proprioceptive information, and actions 𝑎𝑡represent ...
- **p. 5 / 3.3. Generalist Policy Finetuning - extractive body cue:** Octo is another open-source generalist robotic policy, designed to adapt to diverse sensory inputs and action spaces efficiently.
- **p. 5 / 3.3. Generalist Policy Finetuning - extractive body cue:** To predict an action, the transformer backbone takes in the tokenized observation and goal, then outputs a readout embedding 𝑒, which is used to condition ...
- **p. 5 / 3.3. Generalist Policy Finetuning - extractive body cue:** To fine-tune the model on our RL-generated dataset, we use the public model weights pre-trained on 970 thousand Open X-Embodiment dataset (Collaboration et al., 2024) ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | It takes a single image as observation input along with a language instruction. | multi-view observation, language/task label과 action trajectory | p. 4 (3.3. Generalist Policy Finetuning), p. 5 (3.3. Generalist Policy Finetuning) |
| State/latent | takes, single, image, observation, input, along, language, instruction, Octo, another, open-source, generalist | shared representation, embodiment/task identity와 data distribution | p. 4 (3.3. Generalist Policy Finetuning), p. 5 (3.3. Generalist Policy Finetuning), p. 5 (3.3. Generalist Policy Finetuning) |
| Output/action | Octo is another open-source generalist robotic policy, designed to adapt to diverse sensory inputs and action spaces efficiently. | dataset sample 또는 learned policy action | p. 5 (3.3. Generalist Policy Finetuning), p. 5 (3.3. Generalist Policy Finetuning), p. 4 (3.1. Online RL Training) |
| Objective/outcome | The policy objective 𝜋(𝑎𝑡/𝑠𝑡) is to maximize the expected discounted return: 𝐽(𝜋) = 𝔼 𝑠0∼𝜌0 𝑎𝑡∼𝜋(𝑎𝑡/𝑠𝑡) 𝑠𝑡+1∼𝑃(𝑠𝑡+1/𝑠𝑡,𝑎𝑡) [ 𝑇 ∑ 𝑡=0 𝛾𝑡𝑅(𝑠𝑡, 𝑎𝑡)] (1) where 𝜌0 defines the initial robot configurations, 𝑃 ... | coverage, cross-embodiment transfer, data efficiency와 task success | p. 4 (3.1. Online RL Training), p. 4 (3.1. Online RL Training), p. 5 (3.3. Generalist Policy Finetuning) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** To tackle this challenge, we propose Reinforcement Learning Distilled Generalist (RLDG), a simple yet effective method that leverages reinforcement learning to generate high-quality training data ...
- **p. 4 / 3.3. Generalist Policy Finetuning - extractive body cue:** Specifically, suppose we have a pre-trained policy 𝜋0, we fine-tune it with taskspecific dataset 𝐷(𝑠𝑡,𝑎𝑡) with the following supervised learning objective: (𝜃) = -𝔼(𝑠𝑡,𝑎𝑡)∼[log 𝜋𝜃(𝑎𝑡/𝑠𝑡)] ...
- **p. 4 / 3.1. Online RL Training - extractive body cue:** We can formulate each robotic task as a Markov Decision Process (MDP), where the state 𝑠𝑡consists of RGB images and proprioceptive information, and actions 𝑎𝑡represent ...
- **p. 5 / 3.3. Generalist Policy Finetuning - extractive body cue:** Octo is another open-source generalist robotic policy, designed to adapt to diverse sensory inputs and action spaces efficiently.
- **p. 7 / 4.2. RLDG vs. Conventional Fine-tuning - extractive body cue:** When evaluated on seen (VGA) and unseen (Type C) Connector Insertion tasks, RLDG shows superior sample efficiency, requiring significantly fewer demonstrations to achieve perfect success ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Success rate comparison of OpenVLA and Octo policies fine-tuned with RLDG versus conventional methods using human demonstrations. Both generalists trained with RLDG consistently ...
- **p. 6 / 4.2. RLDG vs. Conventional Fine-tuning - extractive body cue:** The benefit of RLDG is equally pronounced for Octo, where it improved the success rate by 10% and 6
- **p. 6 / 4.2. RLDG vs. Conventional Fine-tuning - extractive body cue:** On each task, both OpenVLA and Octo fine-tuned with RL-generated data consistently achieved higher success rates than their counterparts trained with human demonstrations, in both ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4.2. RLDG vs. Conventional Fine-tuning), p. 7 (Figure/Table caption) |
| Embodiment/environment | We also use the single object insertion task of FMB (Luo et al., 2024c), a common and reproducible benchmark for comparing robotic manipulation methods. | hardware/simulator version and reset protocol | p. 6 (4.1. Experimental Setup and Tasks), p. 5 (4.1. Experimental Setup and Tasks) |
| Dataset/benchmark | (C) FMB Insertion involves inserting a pre-grasped object in a moving board while (D) FMB Assembly starts with the object on the table and involves an additional grasping phase. on tasks that ... | role, split, size and leakage | p. 6 (4.1. Experimental Setup and Tasks), p. 5 (4.1. Experimental Setup and Tasks), p. 6 (4.1. Experimental Setup and Tasks), p. 8 (4.3. Generalization of RLDG vs. Original RL) |
| Metric | When evaluated on seen (VGA) and unseen (Type C) Connector Insertion tasks, RLDG shows superior sample efficiency, requiring significantly fewer demonstrations to achieve perfect success rate in both scenarios while the performance ... | definition, denominator, direction and uncertainty | p. 7 (4.2. RLDG vs. Conventional Fine-tuning), p. 6 (4.2. RLDG vs. Conventional Fine-tuning), p. 6 (4.2. RLDG vs. Conventional Fine-tuning) |
| Baseline/ablation | On the precise FMB Insertion and Connector Insertion tasks, where we anticipated the generalist to benefit the most from higher quality training data, OpenVLA with RLDG saw 33% and 23% higher success ... | fair input/data/compute/action matching | p. 6 (4.2. RLDG vs. Conventional Fine-tuning), p. 7 (4.2. RLDG vs. Conventional Fine-tuning), p. 7 (4.2. RLDG vs. Conventional Fine-tuning) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 4.3. Generalization of RLDG vs. Original RL - extractive body cue:** The second part focuses on dissecting the failure modes of the fine-tuned policies on each individual task.
- **p. 9 / 5.1. Is RL data better because of better action - extractive body cue:** However, an interesting RL-specific failure mode was observed: objects were sometimes dropped too early, bouncing out of the bowl.
- **p. 5 / 4.1. Experimental Setup and Tasks - extractive body cue:** Data collection, RL, and Octo policies command actions at 10Hz, while OpenVLA runs at 4Hz due to inference speed limitations.
- **p. 6 / 4.1. Experimental Setup and Tasks - extractive body cue:** (B) Pick and Place involves an unseen scenario that tests the policy's visual robustness to different backgrounds and objects.
- **p. 8 / 4.3. Generalization of RLDG vs. Original RL - extractive body cue:** 4, the RL policy success rate quickly degraded from 20/20 for the training scenario to 1/20 for the unseen scenario of the Pick and Place ...
- **p. 8 / 4.3. Generalization of RLDG vs. Original RL - extractive body cue:** Compared to directly using the RL policies that generated the data, RLDG also demonstrated much greater generalization capabilities and robustness to unseen test scenarios.

## Why Read It

RL, IL, offline learning, and robot data의 robot_data 문제를 이해하기 위해 읽는다. 본문은 While directly finetuning foundation models with reinforcement learning is possible in principle, it presents significant challenges including optimization instability, computational costs, and potential catastrophic forgetting of pre-t ...를 문제로 두고, To tackle this challenge, we propose Reinforcement Learning Distilled Generalist (RLDG), a simple yet effective method that leverages reinforcement learning to generate high-quality training data for robotic foundation models.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 5 (3.3. Generalist Policy Finetuning), p. 4 (3.1. Online RL Training), p. 4 (3.3. Generalist Policy Finetuning), p. 5 (3.3. Generalist Policy Finetuning) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
