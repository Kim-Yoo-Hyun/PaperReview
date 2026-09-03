# Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=lNVHg9npif.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/165445. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://openreview.net/forum?id=lNVHg9npif
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/165445
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 This challenge resembles the distinction between Kahneman's "System 1" and "System 2" cognitive processes (Kahneman, 2011).를 문제로 두고, We show that our framework enables a robot to process much more complex prompts than prior end-to-end instruction following systems and incorporate feedback during task execution (Figure 1).를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Generalist robots that can perform a range of different tasks in open-world settings must be able to not only reason about the steps needed to ...
- **p. 1 / Abstract - extractive body cue:** Intricate instructions (e.g., "Could you make me a vegetarian sandwich?" or "I don't like that one") require not just the ability to physically perform the ...
- **p. 1 / Abstract - extractive body cue:** In this work, we describe a system that uses vision-language models in a hierarchical structure, first reasoning over complex prompts and user feedback to deduce ...
- **p. 1 / Abstract - extractive body cue:** In contrast to direct instruction following methods that can fulfill simple commands ("pick up the cup"), our system can reason through complex prompts and incorporate ...
- **p. 1 / Abstract - extractive body cue:** We evaluate our system across three robotic platforms, including single-arm, dual-arm, and dualarm mobile robots, demonstrating its ability to handle tasks such as cleaning messy ...
- **p. 1 / 1. Introduction - extractive body cue:** This challenge resembles the distinction between Kahneman's "System 1" and "System 2" cognitive processes (Kahneman, 2011).
- **p. 1 / 1. Introduction - extractive body cue:** For instance, consider a robot tasked with tidying up a table after a meal: instead of rigidly following a single predefined set of steps, the ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** We show that our framework enables a robot to process much more complex prompts than prior end-to-end instruction following systems and incorporate feedback during task ...
- **p. 2 / 1. Introduction - extractive body cue:** The main contribution of our paper is a hierarchical interactive robot learning system (Hi Robot), a novel framework that uses VLMs for both high-level reasoning ...
- **p. 5 / 5.1. Tasks and Baseline Methods - extractive body cue:** The training data consists of full table cleaning episodes.
- **p. 7 / 5.1. Tasks and Baseline Methods - extractive body cue:** Hi Robot without synthetic data: This ablation corresponds to our method without synthetic training data, evaluating the importance of including diverse syntheticallygenerated prompts in training.
- **p. 4 / 3. Preliminaries and Problem Statement - extractive body cue:** The policy consists of a high-level and a low-level policy.
- **p. 5 / 4.3. Data Collection and Training Hi Robot - extractive body cue:** To train the low-level policy plo(At/I1 t, ..., In t , ˆℓt, qt), we use Dlabeled ∪Ddemo using a flow-matching objective, following Black et al.
- **p. 6 / 5.1. Tasks and Baseline Methods - extractive body cue:** This requires the high-level model to reason about the task and each object (e.g., recognizing that reusable plastic cups are dishes, while paper cups are ...
- **p. 4 / 4.2. Incorporating User Interaction - extractive body cue:** When ut is included, we use a text to speech system to play the utterance to the user, and remove it from ˆℓt before passing ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | To this end, we provide a state-of-the-art vision-language model with a robot observation and target atomic command, and ask it to come up with a prompt or human interaction that may have ... | image/video, language instruction, proprioception과 history | p. 2 (1. Introduction), p. 4 (3. Preliminaries and Problem Statement) |
| State/latent | provide, state-of-the-art, vision-language, model, robot, observation, target, atomic, command, come, prompt, human | language-grounded task state와 action-policy context | p. 2 (1. Introduction), p. 4 (3. Preliminaries and Problem Statement), p. 3 (3. Preliminaries and Problem Statement) |
| Output/action | We build on the π0 VLA (Black et al., 2024), which additionally handles multiple images and continuous state observations qt, and modifies the VLM to output continuous action chunk distributions via flow-matching, ... | continuous action, pose 또는 action chunk | p. 4 (3. Preliminaries and Problem Statement), p. 3 (3. Preliminaries and Problem Statement), p. 4 (3. Preliminaries and Problem Statement) |
| Objective/outcome | We train the high-level policy phi(ˆℓt/I1 t, ..., In t , ℓt) on Dsyn ∪Dlabeled using the cross-entropy loss for nexttoken prediction. | instruction following, task success, generalization과 latency | p. 5 (4.3. Data Collection and Training Hi Robot), p. 5 (4.3. Data Collection and Training Hi Robot), p. 7 (5.1. Tasks and Baseline Methods) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** We show that our framework enables a robot to process much more complex prompts than prior end-to-end instruction following systems and incorporate feedback during task ...
- **p. 2 / 1. Introduction - extractive body cue:** The main contribution of our paper is a hierarchical interactive robot learning system (Hi Robot), a novel framework that uses VLMs for both high-level reasoning ...
- **p. 5 / 5.1. Tasks and Baseline Methods - extractive body cue:** The training data consists of full table cleaning episodes.
- **p. 7 / 5.1. Tasks and Baseline Methods - extractive body cue:** Hi Robot without synthetic data: This ablation corresponds to our method without synthetic training data, evaluating the importance of including diverse syntheticallygenerated prompts in training.
- **p. 4 / 3. Preliminaries and Problem Statement - extractive body cue:** The policy consists of a high-level and a low-level policy.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 8: Hierarchical policy vs. flat policy. The hierarchical approach outperforms the flat variant trained on the same data, as it effectively integrates user feedback ...
- **p. 8 / 5.3. Core Results - extractive body cue:** We present results for our system and two key baselines: a GPT-4o policy and a flat VLA method.
- **p. 8 / 5.3. Core Results - extractive body cue:** Quantitative and qualitative results are in Figure 5 and Figure 6, and we summarize our findings below.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 9 (Figure/Table caption) |
| Embodiment/environment | Task progress quantifies how closely the robot matches the intended goal and is computed by the proportion of objects that are successfully placed in their correct locations or configurations. | hardware/simulator version and reset protocol | p. 8 (5.2. Metrics and Evaluation Protocol), p. 8 (5.2. Metrics and Evaluation Protocol) |
| Dataset/benchmark | In our experimental evaluation, we study a range of problems that combine challenging physical interactions with complex user interaction, including multi-stage instructions, live user feedback in the middle of the task, and ... | role, split, size and leakage | p. 8 (5.2. Metrics and Evaluation Protocol), p. 8 (5.2. Metrics and Evaluation Protocol), p. 5 (5. Experiments), p. 7 (5.2. Metrics and Evaluation Protocol) |
| Metric | This score measures how well the high-level policy's predicted instruction aligns with human intent, requiring multi-modal understanding of the current environment and prompt. | definition, denominator, direction and uncertainty | p. 7 (5.2. Metrics and Evaluation Protocol), p. 8 (5.3. Core Results), p. 8 (5.2. Metrics and Evaluation Protocol) |
| Baseline/ablation | Across all tasks, Hi Robot exhibits substantially higher Instruction Accuracy and Task Progress, compared to GPT4o and the flat baseline. | fair input/data/compute/action matching | p. 8 (5.3. Core Results), p. 8 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 6. Discussion and Future Work - extractive body cue:** Our system also has a number of limitations that could be studied in future work.
- **p. 8 / 5.3. Core Results - extractive body cue:** With human high-level instructions, the lowlevel policy executes nearly flawlessly, showing that failures stem more from reasoning than actuation.
- **p. 9 / 6. Discussion and Future Work - extractive body cue:** Coupling these two layers more directly, e.g. by allowing the high-level policy to be more aware of how successfully the low-level policy completes each command, ...
- **p. 8 / 5.3. Core Results - extractive body cue:** GPT-4o, however, often fails to maintain a coherent internal state, leading to commands like picking up new objects when the gripper is still occupied or ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 This challenge resembles the distinction between Kahneman's "System 1" and "System 2" cognitive processes (Kahneman, 2011).를 문제로 두고, We show that our framework enables a robot to process much more complex prompts than prior end-to-end instruction following systems and incorporate feedback during task execution (Figure 1).를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminaries and Problem Statement), p. 4 (3. Preliminaries and Problem Statement), p. 5 (5.1. Tasks and Baseline Methods) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
