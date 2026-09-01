# Problem - RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p028.html; PDF retrieval source: https://arxiv.org/pdf/2412.09858. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction)): While directly finetuning foundation models with reinforcement learning is possible in principle, it presents significant challenges including optimization instability, computational costs, and potential catastrophic forgetting of pre-t ...

## PDF Body Digest

- **p. 1 / 1. Introduction - extractive body cue:** Recent advances in robotic foundation models have demonstrated impressive capabilities in understanding and executing diverse manipulation skills (Collaboration et al., 2024; Brohan et al., 2023b;a; ...
- **p. 1 / 1. Introduction - extractive body cue:** By leveraging Internet-scale pretraining and grounding with robot actions, these models can achieve zero-shot and few-shot generalization across various domains.
- **p. 1 / 1. Introduction - extractive body cue:** Deploying these models typically requires fine-tuning them with task-specific data to adapt to the target task or domain.
- **p. 1 / 1. Introduction - extractive body cue:** The quality of this fine-tuning data is therefore critical to the performance of the resulting policies.
- **p. 1 / 1. Introduction - extractive body cue:** While human teleoperation is a common and accessible source for such data, human demonstrations often contain inconsistencies in execution quality and style.
- **p. 1 / 1. Introduction - extractive body cue:** While directly finetuning foundation models with reinforcement learning is possible in principle, it presents significant challenges including optimization instability, computational costs, and potential catastrophic forgetting ...
- **p. 1 / 1. Introduction - extractive body cue:** This challenge affects all robotic tasks but becomes particularly pronounced in scenarios requiring precise control and dexterity, such as contact-rich manipulation.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | While directly finetuning foundation models with reinforcement learning is possible in principle, it presents significant challenges including optimization instability, computational costs, and ... | multi-robot demonstration/dataset ecosystem | body wording is the source claim |
| Observation / input | It takes a single image as observation input along with a language instruction. | multi-view observation, language/task label과 action trajectory | exact sensor/frame/preprocessing from PDF |
| State / latent | takes, single, image, observation, input, along, language, instruction, Octo, another | shared representation, embodiment/task identity와 data distribution | notation and tensor shape require body check |
| Output / action | predict, action, transformer, backbone, takes, tokenized, observation, goal | dataset sample 또는 learned policy action | exact unit/frame/decoder require body check |
| Target outcome | cross-domain transfer and task performance | coverage, cross-embodiment transfer, data efficiency와 task success | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | trajectory D with task/embodiment metadata; body terms: takes, single, image, observation, input, along, language, instruction, Octo, another | p. 4 (3.3. Generalist Policy Finetuning), p. 5 (3.3. Generalist Policy Finetuning), p. 5 (3.3. Generalist Policy Finetuning) |
| Decision / output variable | normalized sample or downstream action; body terms: tackle, challenge, Reinforcement, Learning, Distilled, Generalist, RLDG, simple | p. 1 (1. Introduction), p. 4 (3.3. Generalist Policy Finetuning), p. 4 (3.1. Online RL Training) |
| Objective / loss / cost | coverage/data efficiency/transfer objective; cue terms: policy, objective, maximize, expected, discounted, return, where, defines | p. 4 (3.1. Online RL Training), p. 4 (3.3. Generalist Policy Finetuning), p. 5 (3.3. Generalist Policy Finetuning), p. 5 (3.3. Generalist Policy Finetuning) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.1. Online RL Training), p. 5 (3.3. Generalist Policy Finetuning), p. 5 (3.3. Generalist Policy Finetuning) |
| Success / guarantee | cross-domain transfer and task performance | p. 7 (4.2. RLDG vs. Conventional Fine-tuning), p. 6 (4.2. RLDG vs. Conventional Fine-tuning), p. 6 (4.2. RLDG vs. Conventional Fine-tuning) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** This challenge affects all robotic tasks but becomes particularly pronounced in scenarios requiring precise control and dexterity, such as contact-rich manipulation.

## What the Paper Changes

PDF contribution framing (p. 1 (1. Introduction), p. 4 (3.3. Generalist Policy Finetuning), p. 4 (3.1. Online RL Training), p. 5 (3.3. Generalist Policy Finetuning)): To tackle this challenge, we propose Reinforcement Learning Distilled Generalist (RLDG), a simple yet effective method that leverages reinforcement learning to generate high-quality training data for robotic foundation models.

- **p. 4 / 3.3. Generalist Policy Finetuning - extractive body cue:** Specifically, suppose we have a pre-trained policy 𝜋0, we fine-tune it with taskspecific dataset 𝐷(𝑠𝑡,𝑎𝑡) with the following supervised learning objective: (𝜃) = -𝔼(𝑠𝑡,𝑎𝑡)∼[log 𝜋𝜃(𝑎𝑡/𝑠𝑡)] ...
- **p. 4 / 3.1. Online RL Training - extractive body cue:** We can formulate each robotic task as a Markov Decision Process (MDP), where the state 𝑠𝑡consists of RGB images and proprioceptive information, and actions 𝑎𝑡represent ...
- **p. 5 / 3.3. Generalist Policy Finetuning - extractive body cue:** Octo is another open-source generalist robotic policy, designed to adapt to diverse sensory inputs and action spaces efficiently.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | The second part focuses on dissecting the failure modes of the fine-tuned policies on each individual task. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | However, an interesting RL-specific failure mode was observed: objects were sometimes dropped too early, bouncing out of the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Data collection, RL, and Octo policies command actions at 10Hz, while OpenVLA runs at 4Hz due to inference ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | (B) Pick and Place involves an unseen scenario that tests the policy's visual robustness to different backgrounds and ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

robot_data writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3.3. Generalist Policy Finetuning), p. 5 (3.3. Generalist Policy Finetuning), p. 5 (3.3. Generalist Policy Finetuning), p. 4 (3.1. Online RL Training). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), interface p. 4 (3.3. Generalist Policy Finetuning), p. 5 (3.3. Generalist Policy Finetuning), p. 5 (3.3. Generalist Policy Finetuning), p. 4 (3.1. Online RL Training), objective p. 4 (3.1. Online RL Training), p. 4 (3.3. Generalist Policy Finetuning), p. 5 (3.3. Generalist Policy Finetuning), p. 5 (3.3. Generalist Policy Finetuning).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
