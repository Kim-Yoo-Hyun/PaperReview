# AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://deepmind.google/research/publications/48151/.
> PDF retrieval source: https://deepmind.google/research/publications/48151/. Reading tracker status/evidence was not changed.

- Year/Venue: 2024 / arXiv
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, robot data, Foundation Models, Fleet Learning, Google DeepMind
- Official paper: https://deepmind.google/research/publications/48151/
- Full-text retrieval: https://deepmind.google/research/publications/48151/
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-02 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 robot_data 문제를 이해하기 위해 읽는다. 본문은 The bottleneck for achieving these goals, however, is the need for large amounts of robotic experience in the real world - much larger than robot datasets collected in lab settings with well-defined ...를 문제로 두고, In this paper, we propose AutoRT, a system that leverages existing foundation models to scale up the deployment of operational robots in completely unseen scenarios with minimal human supervision.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Foundation models that incorporate language, vision, and more recently actions have revolutionized the ability to harness internet scale data to reason about useful tasks.
- **p. 1 / ABSTRACT - extractive body cue:** However, one of the key challenges of training embodied foundation models is the lack of data grounded in the physical world.
- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we propose AutoRT, a system that leverages existing foundation models to scale up the deployment of operational robots in completely unseen scenarios ...
- **p. 1 / ABSTRACT - extractive body cue:** AutoRT leverages vision-language models (VLMs) for scene understanding and grounding, and further uses large language models (LLMs) for proposing diverse and novel instructions to be ...
- **p. 1 / ABSTRACT - extractive body cue:** Guiding data collection by tapping into the knowledge of foundation models enables AutoRT to effectively reason about autonomy tradeoffs and safety while significantly scaling up ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The bottleneck for achieving these goals, however, is the need for large amounts of robotic experience in the real world - much larger than robot ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** While current robotic learning methods offer appealing solutions for acquiring individual robotic skills, and large language models (LLMs), vision-language models (VLMs) and large multimodal models ...

## Core Idea

- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we propose AutoRT, a system that leverages existing foundation models to scale up the deployment of operational robots in completely unseen scenarios ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We show that AutoRT scales robot deployment by allowing 1 human to supervise 3-5 mobile manipulators.
- **p. 1 / ABSTRACT - extractive body cue:** Guiding data collection by tapping into the knowledge of foundation models enables AutoRT to effectively reason about autonomy tradeoffs and safety while significantly scaling up ...
- **p. 4 / 3. Place the napkin onto - extractive body cue:** Green sections are contributions of this work.
- **p. 4 / 3. Place the napkin onto - extractive body cue:** No part of this requires advance knowledge of the layout of the environment or objects it contains, making it easy to run on a fleet ...
- **p. 7 / 3. Place the napkin onto - extractive body cue:** Robot episodes are first embedded by a visual encoder, then k-means unsupervised clustering is done in the space.
- **p. 7 / 3. Place the napkin onto - extractive body cue:** Language diversity: To measure language diversity, we use the L2 distance in a language embedding space - specifically that of Universal Sentence Encoder (Cer et ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** AutoRT is, to the best of our knowledge, the first system where LLM-controlled robots are allowed to drive autonomously in real world settings, propose their ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | For a breakdown of throughput by collect policy, or visualization of action trajectories, see Appendix I. | multi-view observation, language/task label과 action trajectory | p. 5 (3. Place the napkin onto), p. 5 (3. Place the napkin onto) |
| State/latent | breakdown, throughput, collect, policy, visualization, action, trajectories, Appendix, generated, task, LLM, asked | shared representation, embodiment/task identity와 data distribution | p. 5 (3. Place the napkin onto), p. 5 (3. Place the napkin onto), p. 2 (1 INTRODUCTION) |
| Output/action | For each generated task, the LLM is asked to either output a collect policy or a reason to reject that task. | dataset sample 또는 learned policy action | p. 5 (3. Place the napkin onto), p. 2 (1 INTRODUCTION), p. 7 (3. Place the napkin onto) |
| Objective/outcome | This process takes into account constraints specified via "constitutional prompting", where rules about robot behaviour can be defined by the user. | coverage, cross-embodiment transfer, data efficiency와 task success | p. 2 (1 INTRODUCTION), p. 5 (3. Place the napkin onto), p. 5 (3. Place the napkin onto) |

## Main Claims and Actual Contribution

- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we propose AutoRT, a system that leverages existing foundation models to scale up the deployment of operational robots in completely unseen scenarios ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We show that AutoRT scales robot deployment by allowing 1 human to supervise 3-5 mobile manipulators.
- **p. 1 / ABSTRACT - extractive body cue:** Guiding data collection by tapping into the knowledge of foundation models enables AutoRT to effectively reason about autonomy tradeoffs and safety while significantly scaling up ...
- **p. 4 / 3. Place the napkin onto - extractive body cue:** Green sections are contributions of this work.
- **p. 4 / 3. Place the napkin onto - extractive body cue:** No part of this requires advance knowledge of the layout of the environment or objects it contains, making it easy to run on a fleet ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: AutoRT data, split by collect policy used. Scripted policy was used most frequently, while teleoperation had the highest success rate. Collect Method Average ...
- **p. 9 / 3. Place the napkin onto - extractive body cue:** These increases are modest, but we note that the focus of AutoRT was on collecting diverse data, not on achieving high success rates.
- **p. 10 / 3. Place the napkin onto - extractive body cue:** If these policies only handle simpler tasks or have lower success rates in unseen settings, it lowers the throughput of successful episodes.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 9 (3. Place the napkin onto) |
| Embodiment/environment | First, 5 test scenes were set up with objects that the robot should not interact with, including lifelike toy animals, sharp items, and people. | hardware/simulator version and reset protocol | p. 9 (3. Place the napkin onto), p. 10 (3. Place the napkin onto) |
| Dataset/benchmark | If these policies only handle simpler tasks or have lower success rates in unseen settings, it lowers the throughput of successful episodes. | role, split, size and leakage | p. 9 (3. Place the napkin onto), p. 10 (3. Place the napkin onto), p. 10 (3. Place the napkin onto), p. 8 (3. Place the napkin onto) |
| Metric | Table 1: AutoRT data, split by collect policy used. Scripted policy was used most frequently, while teleoperation had the highest success rate. Collect Method Average Language L2 Dist Lang. Table 0.988 BC-Z | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 9 (3. Place the napkin onto), p. 10 (3. Place the napkin onto) |
| Baseline/ablation | Figure 9: Hours of data collected per policy per day. We aimed for teleop collect throughput to exceed a simple 1 person:1 robot baseline. We found a small increase in teleop throughput ... | fair input/data/compute/action matching | p. 26 (Figure/Table caption), p. 10 (3. Place the napkin onto), p. 8 (3. Place the napkin onto) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 3. Place the napkin onto - extractive body cue:** Failures of perception such as hallucination of objects, lack of generalization to novel environments, and motion blur can introduce and propagate failures in the system.
- **p. 10 / 3. Place the napkin onto - extractive body cue:** Despite the promise of AutoRT, the current approach comes with a number of limitations.
- **p. 8 / 3. Place the napkin onto - extractive body cue:** How often does the LLM reject (or fail to reject) tasks that should be rejected?
- **p. 9 / 3. Place the napkin onto - extractive body cue:** Additionally constitutional prompting is able to achieve high recall when given unsafe tasks.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: Effect of constitutional prompting on safety of proposed tasks Task Generation Unsafe prompting Minimal prompting Constitutional prompting Filter % Safe Recall
- **p. 24 / Figure/Table caption - extractive body cue:** Table 9: Tasks generated in Section 5.3 experiments. We present an image the robot sees, tasks generated by the unsafe task generation prompt, and the ...

## Why Read It

VLA and generalist robot policies의 robot_data 문제를 이해하기 위해 읽는다. 본문은 The bottleneck for achieving these goals, however, is the need for large amounts of robotic experience in the real world - much larger than robot datasets collected in lab settings with well-defined ...를 문제로 두고, In this paper, we propose AutoRT, a system that leverages existing foundation models to scale up the deployment of operational robots in completely unseen scenarios with minimal human supervision.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 7 (3. Place the napkin onto), p. 1 (ABSTRACT), p. 7 (3. Place the napkin onto) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
