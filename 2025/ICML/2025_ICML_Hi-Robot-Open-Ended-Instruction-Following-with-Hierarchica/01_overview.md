# Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v267/shi25d.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/165445. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICML
- Authors: Lucy Xiaoyang Shi, Brian Ichter, Michael Robert Equi, Liyiming Ke, Karl Pertsch, Quan Vuong, James Tanner, Anna Walling, Haohuan Wang, Niccolo Fusai, Adrian Li-Bell, Danny Driess, Lachy Groom, Sergey Levine, Chelsea Finn
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://proceedings.mlr.press/v267/shi25d.html
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25d/shi25d.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

Hi Robot은 복잡한 요청이나 실행 도중의 사용자 피드백을 고수준 VLM이 다음 단계 지시로 해석하고 저수준 정책이 그 단계를 실행하는 구조다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/shi25d/shi25d.pdf#page=1)

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

- 현장 관측과 대화에서 단순 행동 지시를 내리는 상위 모델을 구성하고, 합성한 언어 예시와 로봇 시연을 각 학습 단계에 활용했다. [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/shi25d/shi25d.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/shi25d/shi25d.pdf#page=5)
- 단팔·양팔·이동형 양팔 로봇에 적용해 식탁 정리, 샌드위치 만들기와 장보기에서 복합 요청 및 중간 피드백에 대한 행동 변화를 평가했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/shi25d/shi25d.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/shi25d/shi25d.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/shi25d/shi25d.pdf#page=8)

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

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminaries and Problem Statement), p. 4 (3. Preliminaries and Problem Statement), p. 5 (5.1. Tasks and Baseline Methods)이다.
