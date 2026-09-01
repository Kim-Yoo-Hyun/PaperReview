# SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (50 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v229/rana23a.html.
> PDF retrieval source: https://arxiv.org/pdf/2307.06135. Reading tracker status/evidence was not changed.

- Year/Venue: 2023 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, 3D Vision, LLM planning, 3D Scene Graph, replanning, mobile manipulation
- Official paper: https://proceedings.mlr.press/v229/rana23a.html
- Full-text retrieval: https://arxiv.org/pdf/2307.06135
- Code/Project: https://sayplan.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (50 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 We evaluate our framework across a range of 90 tasks organised into four levels of difficulty.를 문제로 두고, Firstly, we present a mechanism that enables the LLM to conduct a semantic search for a taskrelevant subgraph G′ by manipulating the nodes of a ‘collapsed' 3DSG, which exposes only the top ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** "Make me a coffee and place it on my desk" - The successful execution of such a seemingly straightforward command remains a daunting task for ...
- **p. 1 / 1 Introduction - extractive body cue:** The associated challenges permeate every aspect of robotics, encompassing navigation, perception, manipulation as well as high-level task planning.
- **p. 1 / 1 Introduction - extractive body cue:** Recent advances in Large Language Models (LLMs) [1, 2, 3] have led to significant progress in incorporating common sense knowledge for robotics [4, 5, 6].
- **p. 1 / 1 Introduction - extractive body cue:** This enables robots to plan complex strategies for a diverse range of tasks that require a substantial amount of background knowledge and semantic comprehension.
- **p. 1 / 1 Introduction - extractive body cue:** For LLMs to be effective planners in robotics, they must be grounded in reality, that is, they must adhere to the constraints presented by the ...
- **p. 3 / 1 Introduction - extractive body cue:** We evaluate our framework across a range of 90 tasks organised into four levels of difficulty.
- **p. 1 / 1 Introduction - extractive body cue:** The challenge lies in scaling these models.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Firstly, we present a mechanism that enables the LLM to conduct a semantic search for a taskrelevant subgraph G′ by manipulating the nodes of a ...
- **p. 2 / 1 Introduction - extractive body cue:** To this end, we present a scalable approach to ground LLM-based task planners across environments spanning multiple rooms and floors.
- **p. 3 / 1 Introduction - extractive body cue:** We evaluate our framework across a range of 90 tasks organised into four levels of difficulty.
- **p. 1 / 1 Introduction - extractive body cue:** This enables robots to plan complex strategies for a diverse range of tasks that require a substantial amount of background knowledge and semantic comprehension.
- **p. 3 / 1 Introduction - extractive body cue:** Our approach SayPlan ensures feasible and grounded plan generation for a mobile manipulator robot operating in large-scale environments spanning multiple floors and rooms.
- **p. 13 / A Implementation Details - extractive body cue:** We utilise GPT-4 [3] as the underlying LLM agent unless otherwise stated.
- **p. 13 / A Implementation Details - extractive body cue:** During semantic search, both the 3D Scene Graph and Memory components of the input prompt get updated at each step, while during iterative replanning only ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Finally, to ensure the feasibility of the proposed plan, we introduce an iterative replanning pipeline that verifies and refines the initial plan using feedback from a scene graph simulator in order to ... | egocentric RGB-D, language/task goal, base-arm proprioception | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| State/latent | Finally, ensure, feasibility, plan, introduce, iterative, replanning, pipeline, verifies, refines, initial, feedback | map/object/contact state와 base-arm coordination decision | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Output/action | For LLMs to be effective planners in robotics, they must be grounded in reality, that is, they must adhere to the constraints presented by the physical environment in which the robot operates, ... | base motion plus arm/gripper action | p. 1 (1 Introduction), p. 2 (1 Introduction), p. 13 (A Implementation Details) |
| Objective/outcome | During semantic search, both the 3D Scene Graph and Memory components of the input prompt get updated at each step, while during iterative replanning only the Feedback component gets updated with information ... | long-horizon task success, reachability, collision과 recovery | p. 13 (A Implementation Details) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** Firstly, we present a mechanism that enables the LLM to conduct a semantic search for a taskrelevant subgraph G′ by manipulating the nodes of a ...
- **p. 2 / 1 Introduction - extractive body cue:** To this end, we present a scalable approach to ground LLM-based task planners across environments spanning multiple rooms and floors.
- **p. 3 / 1 Introduction - extractive body cue:** We evaluate our framework across a range of 90 tasks organised into four levels of difficulty.
- **p. 1 / 1 Introduction - extractive body cue:** This enables robots to plan complex strategies for a diverse range of tasks that require a substantial amount of background knowledge and semantic comprehension.
- **p. 3 / 1 Introduction - extractive body cue:** Our approach SayPlan ensures feasible and grounded plan generation for a mobile manipulator robot operating in large-scale environments spanning multiple floors and rooms.
- **p. 6 / 5 Results - extractive body cue:** The table shows the semantic search success rate in finding a suitable subgraph for planning.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Scene Graph Token Progression Dur- ing Semantic Search. This graph illustrates the scalability of our approach to large-scale 3D scene graphs. Note the ...
- **p. 46 / Figure/Table caption - extractive body cue:** Figure 8: Evaluating the performance of SayPlan's causal planning capabilities as the scale of the environment increases. For the office environment used in this study, ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (5 Results), p. 7 (Figure/Table caption) |
| Embodiment/environment | This static prompt is both task- and environment-agnostic and takes up ≈3900 tokens of the LLM's input. | hardware/simulator version and reset protocol | p. 13 (A Implementation Details), p. 13 (A Implementation Details) |
| Dataset/benchmark | 5.1 Semantic Search Office Home Subtask Human SayPlan (GPT-3.5) SayPlan (GPT-4) Human SayPlan (GPT-3.5) SayPlan (GPT-4) Simple Search 100% 6.6% 86.7% 100% 0.0% 86.7% Complex Search 100% 0.0% 73.3% 100% 0.0% 73.3% ... | role, split, size and leakage | p. 13 (A Implementation Details), p. 13 (A Implementation Details), p. 6 (5 Results) |
| Metric | The table shows the semantic search success rate in finding a suitable subgraph for planning. | definition, denominator, direction and uncertainty | p. 6 (5 Results), p. 7 (Figure/Table caption), p. 32 (Figure/Table caption) |
| Baseline/ablation | Figure 3: Scene Graph Token Progression Dur- ing Semantic Search. This graph illustrates the scalability of our approach to large-scale 3D scene graphs. Note the importance of node contraction in maintaining a ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 32 (Figure/Table caption), p. 20 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: 3D Scene Graph Token Count Number of tokens required for the full graph vs. collapsed graph. An odd failure case in the simple ...
- **p. 46 / Figure/Table caption - extractive body cue:** Figure 8: Evaluating the performance of SayPlan's causal planning capabilities as the scale of the environment increases. For the office environment used in this study, ...
- **p. 32 / Figure/Table caption - extractive body cue:** Table 18: Correctness, Executability and Number of Replanning Iterations for Long-Horizon Planning Instructions. Evaluating the performance of SayPlan on each long-horizon planning instruction. Values indicated ...

## Why Read It

VLA and generalist robot policies의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 We evaluate our framework across a range of 90 tasks organised into four levels of difficulty.를 문제로 두고, Firstly, we present a mechanism that enables the LLM to conduct a semantic search for a taskrelevant subgraph G′ by manipulating the nodes of a ‘collapsed' 3DSG, which exposes only the top ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 13 (A Implementation Details) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
