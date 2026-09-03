# PartInstruct: Part-level Instruction Following for Fine-grained Robot Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p148.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p148.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, Benchmark, part-level grounding, 3D manipulation, language instruction, long-horizon
- Official paper: https://www.roboticsproceedings.org/rss21/p148.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p148.pdf
- Code/Project: not identified
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (24 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Kine-grained robot manipulation, such as lifting and rotating a bottle to display the label on the cap, requires robust reasoning about object parts and their relationships with intended tasks.를 문제로 두고, Specifically, the bi-level planner consists of two modules: (1) a high-level task planner and (2) a low-level action policy.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Kine-grained robot manipulation, such as lifting and rotating a bottle to display the label on the cap, requires robust reasoning about object parts and their ...
- **p. 1 / Abstract - extractive body cue:** Despite recent advances in training general-purpose robot manipulation policies guided by language instructions, there is a notable lack of large-scale datasets for fine-grained ‘manipulation tasks ...
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce Partinstruct, the first large-scale benchmark for both
- **p. 1 / Abstract - extractive body cue:** robot manipulation models using part-level instructions.
- **p. 1 / Abstract - extractive body cue:** ‘expert demonstrations synthesized in a 3D simulator, where each demonstration is paired with a high-level task instruction, a in of base part-based skill instructions, and ...

## Core Idea

- **p. 7 / B. Bi-level Planning - extractive body cue:** Specifically, the bi-level planner consists of two modules: (1) a high-level task planner and (2) a low-level action policy.
- **p. 4 / A. Problem Setup - extractive body cue:** ‘To develop an embodied agent capable of executing tasks defined by g, we hypothesize that it would be beneficial to star, With a set of ...
- **p. 6 / A. End-to-End Policy Learning - extractive body cue:** Diffusion Policy (DP) [5] represents a visuomotor policy as a conditional denoising diffusion process in the action space, which allows it to effectively handle multimodal ...
- **p. 8 / B. Bi-level Planning - extractive body cue:** Specifically, given an RGB image and language input, we first utilize a VLM, eg Florence-2 [34] to ground the language onto the tanget part, then ...
- **p. 8 / B. Bi-level Planning - extractive body cue:** Given this result, we then adopt DP3-5 as the low-level action policy and pair it with diferent high-level planners to create bi-level planning baselines.
- **p. 6 / A. End-to-End Policy Learning - extractive body cue:** At each time step, the model outputs an action vector that contains the translation and rotation of the robot end effector, along with ‘one dimension ...
- **p. 7 / 1 Actions .ow-Level Action - extractive body cue:** skill instruction, the low-level action policy then generates actions for achieving that subgoal
- **p. 6 / A. End-to-End Policy Learning - extractive body cue:** These key pose Wi then be executed using a motion planner,

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | for the low-level action policy based on the task instruction and the current observation. | standardized observation, action, task state와 evaluation split | p. 7 (1 Actions .ow-Level Action), p. 6 (A. End-to-End Policy Learning) |
| State/latent | low-level, action, policy, task, instruction, current, observation, Diffuser, Actor, D-DA, tains, jointly | benchmark state/goal와 method decision | p. 7 (1 Actions .ow-Level Action), p. 6 (A. End-to-End Policy Learning), p. 7 (1 Actions .ow-Level Action) |
| Output/action | 3D Diffuser Actor (3D-DA) [18] tains a policy that is jointly conditioned on a tokenized 3D scene, proprioceptive feedback, and a natural-language instruction, It uses diffusion to generate 3D pose trajectories. | policy/controller trajectory 또는 measured result | p. 6 (A. End-to-End Policy Learning), p. 7 (1 Actions .ow-Level Action), p. 8 (B. Bi-level Planning) |
| Objective/outcome | updates the skill instruction once every n steps, while the low-level action policy updates the action at every step. | success metric, robustness, generalization과 reproducibility | p. 7 (1 Actions .ow-Level Action), p. 7 (B. Bi-level Planning) |

## Main Claims and Actual Contribution

- **p. 7 / B. Bi-level Planning - extractive body cue:** Specifically, the bi-level planner consists of two modules: (1) a high-level task planner and (2) a low-level action policy.
- **p. 4 / A. Problem Setup - extractive body cue:** ‘To develop an embodied agent capable of executing tasks defined by g, we hypothesize that it would be beneficial to star, With a set of ...
- **p. 6 / A. End-to-End Policy Learning - extractive body cue:** Diffusion Policy (DP) [5] represents a visuomotor policy as a conditional denoising diffusion process in the action space, which allows it to effectively handle multimodal ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 8: Success Rates of all baselines. The left group represents end-to-end learning policies, while the right group corresponds to bi-level planning models. Error bars ...
- **p. 6 / C. Dataset - extractive body cue:** 11, 13, 5, 49) and (2) bi level planning that first generates high-level plans (typically subgoals), then compute and execute the low-level action plans to ...
- **p. 6 / C. Dataset - extractive body cue:** To achieve general-purpose robot manipulation, there have been two common types of approaches: (1) end-to-end policy learning that directly maps observation and instruction 10 actions ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: An example fine-grained robot manipulation task in Partlnstruet, To successfully perform the task described in the instruction

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 6 (C. Dataset) |
| Embodiment/environment | Early benchmarks in robot manipulation primarily concentrated on object-level and object-scene interactions without delving into the manipulation of specific object parts. | hardware/simulator version and reset protocol | p. 2 (A. Instruction Following Benchmarks for Table-Top Robot), p. 5 (C. Dataset) |
| Dataset/benchmark | These benchmarks typically involve tasks such as object placement, scene arrangement, and basic interaction with objects in their entirety. | role, split, size and leakage | p. 2 (A. Instruction Following Benchmarks for Table-Top Robot), p. 5 (C. Dataset), p. 2 (A. Instruction Following Benchmarks for Table-Top Robot), p. 6 (C. Dataset) |
| Metric | Figure 8: Success Rates of all baselines. The left group represents end-to-end learning policies, while the right group corresponds to bi-level planning models. Error bars denote the standard errors calculated across all ... | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 2 (A. Instruction Following Benchmarks for Table-Top Robot), p. 2 (A. Instruction Following Benchmarks for Table-Top Robot) |
| Baseline/ablation | 3) Demonstration Generation: Each demonstration is. a sequential execution of oracle high-level plans of base skills defined in Table X, To generate the trajectories in the demonstrations, we detect grasping point using ... | fair input/data/compute/action matching | p. 6 (C. Dataset), p. 7 (Figure/Table caption), p. 2 (A. Instruction Following Benchmarks for Table-Top Robot) |

## Explicit Limitations and Failure Boundary

- **p. 9 / V. Discussion - extractive body cue:** Our experimental results demonstrate that the part-level instruction following tasks in our Partinstruct benchmark remains extremely difficult for state-of-the-art end-to-end vision-language policy learning ‘methods. ‘There ...
- **p. 9 / V. Discussion - extractive body cue:** While they can follow simple part-based instructions such as "grasp" or "touch? instructions Tike "touch the left part" introduce fine-grained spatial reasoning that these models ...
- **p. 2 / A. Instruction Following Benchmarks for Table-Top Robot - extractive body cue:** For instance, CALVIN incorporates spatial semantics but lacks explicit partlevel semantics, treating components like a "door handle as standalone objects rather than parts of a ...
- **p. 10 / V. Discussion - extractive body cue:** However, VLM-based planners can still fail during task planning, particularly in tasks that require a long chain of, skill instructions (e.., tasks in Test 4).

## Why Read It

VLA and generalist robot policies의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Kine-grained robot manipulation, such as lifting and rotating a bottle to display the label on the cap, requires robust reasoning about object parts and their relationships with intended tasks.를 문제로 두고, Specifically, the bi-level planner consists of two modules: (1) a high-level task planner and (2) a low-level action policy.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 7 (B. Bi-level Planning), p. 8 (B. Bi-level Planning), p. 8 (B. Bi-level Planning), p. 6 (A. End-to-End Policy Learning), p. 7 (1 Actions .ow-Level Action), p. 6 (A. End-to-End Policy Learning) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (24 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Our experimental results demonstrate that the part-level instruction following tasks in our Partinstruct benchmark remains extremely difficult for state-of-the-art end-to-end vision-language policy learning ‘methods. ‘There are several ... (p. 9, V. Discussion).
- **Actual contribution:** In this work, we introduce Partinstruct, the first large-scale benchmark for both (p. 1, Abstract).
- **Evaluation boundary:** Figure 8: Success Rates of all baselines. The left group represents end-to-end learning policies, while the right group corresponds to bi-level planning models. Error bars denote the standard errors calculated ... (p. 7, Figure/Table caption).
- **Explicit failure boundary:** The Failure Cause was calculated by dividing the number of times a skill chain failed because of a specific skill or part by the total number of skill chain failures. (p. 21, C. Skill and Object Part Impact Study).
