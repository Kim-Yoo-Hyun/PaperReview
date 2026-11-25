# RT-H: Action Hierarchies Using Language

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss20/p049.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss20/p049.html. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / Robotics: Science and Systems
- Authors: Suneel Belkhale, Tianli Ding, Ted Xiao, Pierre Sermanet, Quan Vuong, Jonathan Tompson, Yevgen Chebotar, Debidatta Dwibedi, Dorsa Sadigh
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, VLA, Action Hierarchy, language, Google DeepMind
- Official paper: https://www.roboticsproceedings.org/rss20/p049.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss20/p049.html
- Code/Project: https://rt-hierarchy.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RT-H는 고수준 지시와 로봇 제어 사이에 짧은 동작 언어를 두어 과제 간 움직임을 공유하고 실행 중 사람이 개입할 수 있게 한다. [PDF 1쪽](https://roboticsproceedings.org/rss20/p049.pdf#page=1) · [PDF 3쪽](https://roboticsproceedings.org/rss20/p049.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Language provides a way to break down complex concepts into digestible pieces.
- **p. 1 / Abstract - extractive body cue:** Recent works in robot imitation learning have proposed learning language-conditioned policies that predict actions given visual observations and the high-level task specified in language.
- **p. 1 / Abstract - extractive body cue:** These methods leverage the structure of natural language to share data between semantically similar tasks (e.g., "pick coke can" and "pick an apple") in multi-task ...
- **p. 1 / Abstract - extractive body cue:** However, as tasks become more semantically diverse (e.g., "pick coke can" and "pour cup"), sharing data between tasks becomes harder and thus learning to map ...
- **p. 1 / Abstract - extractive body cue:** To bridge this divide between tasks and actions, our insight is to teach the robot the language of actions, describing lowlevel motions with more fine-grained ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Language is the engine of human reasoning, empowering us to break complex concepts into simpler ones, to correct our misunderstandings, and to generalize concepts in ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** concepts [1], providing language corrections [2, 3], or enabling generalization to new settings [4].

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** Motivated by the benefits of language motions, we propose an end-to-end framework, RT-H (Robot Transformer with Action Hierarchies), for learning these action hierarchies: at each ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Creating such an action hierarchy leads to several benefits: (1) It enables much better data sharing between different tasks at the level of language motions, ...
- **p. 1 / Abstract - extractive body cue:** Our method RT-H builds an action hierarchy using language motions: it first learns to predict language motions, and conditioned on this along with the high-level ...
- **p. 1 / Abstract - extractive body cue:** This enables a new paradigm for flexible policies that can learn from human intervention in language.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** 1: Given a task in language like "close the pistachio jar" and an image of the scene, RT-H utilizes a Vision Language Model (VLM) to ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Then RT-H uses the observation, the task, and the inferred language motion to predict the action for that step (action query), where the language motion ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Recent works in robot imitation learning have proposed learning language-conditioned policies that predict actions given visual observations and the high-level task specified in language. | image/video, language instruction, proprioception과 history | p. 1 (Abstract), p. 1 (Abstract) |
| State/latent | Recent, works, robot, imitation, learning, have, language-conditioned, policies, predict, actions, given, visual | language-grounded task state와 action-policy context | p. 1 (Abstract), p. 1 (Abstract), p. 2 (I. INTRODUCTION) |
| Output/action | Predicting these language motions as an intermediate step between high-level tasks and actions forces the policy to learn the shared structure of low-level motions across seemingly disparate tasks. | continuous action, pose 또는 action chunk | p. 1 (Abstract), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective/outcome | The advantage of language in these settings is to encode the shared structure between similar tasks (e.g., "pick coke can" vs. "pick an apple"), reducing the data needed to learn the mapping ... | instruction following, task success, generalization과 latency | p. 2 (I. INTRODUCTION) |

## Main Claims and Actual Contribution

- 동일한 시각 관측 아래 동작 언어를 먼저 예측하고 이를 조건으로 저수준 행동을 생성한다. [PDF 3쪽](https://roboticsproceedings.org/rss20/p049.pdf#page=3) · [PDF 4쪽](https://roboticsproceedings.org/rss20/p049.pdf#page=4)
- 사람이 중간 동작 지시를 바꿔 진행 중인 행동을 교정하는 방식을 제시하고 실제 조작 사례에서 그 효과를 평가했다. [PDF 5쪽](https://roboticsproceedings.org/rss20/p049.pdf#page=5) · [PDF 8쪽](https://roboticsproceedings.org/rss20/p049.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (Figure/Table caption), p. 9 (Figure/Table caption) |
| Embodiment/environment | We use RT-H trained on only the Kitchen dataset [6] unless otherwise noted (i.e., not including the Diverse data), which consists of the following training and evaluation tasks on various objects: 1) ... | hardware/simulator version and reset protocol | p. 10 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Dataset/benchmark | To comprehensively evaluate the performance of RT-H, we study four key experimental questions: • Q1 (Performance): Do action hierarchies with language improve policy performance on diverse multi-task datasets? • Q2 (Contextuality): Are ... | role, split, size and leakage | p. 10 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Metric | 95% Wilson Score confidence intervals [54] are shown on the average success rates (left). | definition, denominator, direction and uncertainty | p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS) |
| Baseline/ablation | Fig. 7: Results when models trained on Kitchen data [6] are deployed on the same tasks, but in a new building with novel backgrounds, lighting, and flooring. RT-H and RT-H-Joint each outperform ... | fair input/data/compute/action matching | p. 11 (Figure/Table caption), p. 8 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Given a task in language like "close the pistachio jar" and an image of the scene, RT-H utilizes a Vision Language Model (VLM) ...
- **p. 9 / V. EXPERIMENTS - extractive body cue:** The oatmeal example also highlights how language motion corrections can make the policy's behavior interpretable and thus more intuitive to debug - more effectively allowing ...
- **p. 9 / V. EXPERIMENTS - extractive body cue:** Since we only care about learning to correct the failure modes of RT-2, we must use RT-2 trained on the Diverse+Kitchen dataset (same as RT-H-Intervene) ...
- **p. 10 / V. EXPERIMENTS - extractive body cue:** This failure mode rarely happens for in-distribution tasks, but as tasks diverge from the data distribution, it becomes more likely.
- **p. 10 / V. EXPERIMENTS - extractive body cue:** Failure Modes: RT-H demonstrates performance boosts on a wide variety of tasks, however the action hierarchy paradigm does lead to interesting failure modes.
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 8: We show the generalization capabilities of RT-H with completely unseen tasks with minimal correction. By breaking down tasks into language motions, RT-H learns ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** To comprehensively evaluate the performance of RT-H, we study four key experimental questions: • Q1 (Performance): Do action hierarchies with language improve policy performance on ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Abstract), p. 1 (Body text (section boundary not confidently recovered))이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (23 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Language is the engine of human reasoning, empowering us to break complex concepts into simpler ones, to correct our misunderstandings, and to generalize concepts in new settings. (p. 1, I. INTRODUCTION).
- **Actual contribution:** Creating such an action hierarchy leads to several benefits: (1) It enables much better data sharing between different tasks at the level of language motions, leading to better language motion ... (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** Fig. 3: Results on Diverse+Kitchen multi-task dataset, consisting of eight challenging evaluation tasks. 95% Wilson Score confidence intervals [54] are shown on the average success rates (left). RT-H outperforms RT-2 ... (p. 6, Figure/Table caption).
- **Explicit failure boundary:** RT-2-IWR: We collect 30 episodes (failed episodes filtered out) of teleoperated corrections for the same eight tasks, using VR-based teleoperation instead of language motion corrections. (p. 9, V. EXPERIMENTS).

## 원문과 공개 자료

- 저자 프로젝트에서 연구와 자료 안내 범위를 확인했다. [프로젝트](https://rt-hierarchy.github.io/)
