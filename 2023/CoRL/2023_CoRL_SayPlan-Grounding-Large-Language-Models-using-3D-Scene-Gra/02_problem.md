# Problem - SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (50 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v229/rana23a.html; PDF retrieval source: https://arxiv.org/pdf/2307.06135. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 3 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction)): We evaluate our framework across a range of 90 tasks organised into four levels of difficulty.

## PDF Body Digest

- **p. 1 / 1 Introduction - extractive body cue:** "Make me a coffee and place it on my desk" - The successful execution of such a seemingly straightforward command remains a daunting task for ...
- **p. 1 / 1 Introduction - extractive body cue:** The associated challenges permeate every aspect of robotics, encompassing navigation, perception, manipulation as well as high-level task planning.
- **p. 1 / 1 Introduction - extractive body cue:** Recent advances in Large Language Models (LLMs) [1, 2, 3] have led to significant progress in incorporating common sense knowledge for robotics [4, 5, 6].
- **p. 1 / 1 Introduction - extractive body cue:** This enables robots to plan complex strategies for a diverse range of tasks that require a substantial amount of background knowledge and semantic comprehension.
- **p. 1 / 1 Introduction - extractive body cue:** For LLMs to be effective planners in robotics, they must be grounded in reality, that is, they must adhere to the constraints presented by the ...
- **p. 3 / 1 Introduction - extractive body cue:** We evaluate our framework across a range of 90 tasks organised into four levels of difficulty.
- **p. 1 / 1 Introduction - extractive body cue:** The challenge lies in scaling these models.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | We evaluate our framework across a range of 90 tasks organised into four levels of difficulty. | mobile base와 one/two-arm manipulation environment | body wording is the source claim |
| Observation / input | Finally, to ensure the feasibility of the proposed plan, we introduce an iterative replanning pipeline that verifies and refines the initial plan ... | egocentric RGB-D, language/task goal, base-arm proprioception | exact sensor/frame/preprocessing from PDF |
| State / latent | Finally, ensure, feasibility, plan, introduce, iterative, replanning, pipeline, verifies, refines | map/object/contact state와 base-arm coordination decision | notation and tensor shape require body check |
| Output / action | Secondly, horizon, task, plans, across, environments, tends, grow | base motion plus arm/gripper action | exact unit/frame/decoder require body check |
| Target outcome | task completion and recovery | long-horizon task success, reachability, collision과 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | base-arm-object state and language/task goal; body terms: Finally, ensure, feasibility, plan, introduce, iterative, replanning, pipeline, verifies, refines | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Decision / output variable | base plus arm/gripper action; body terms: Firstly, present, mechanism, enables, LLM, conduct, semantic, search | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Objective / loss / cost | long-horizon task utility under reachability/contact constraints; cue terms: During, semantic, search, Scene, Graph, Memory, components, input | p. 13 (A Implementation Details) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 13 (A Implementation Details) |
| Success / guarantee | task completion and recovery | p. 6 (5 Results), p. 7 (Figure/Table caption), p. 32 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** The challenge lies in scaling these models.
- **p. 1 / 1 Introduction - extractive body cue:** The associated challenges permeate every aspect of robotics, encompassing navigation, perception, manipulation as well as high-level task planning.
- **p. 2 / 1 Introduction - extractive body cue:** We can leverage a JSON representation of this graph as input to a pre-trained LLM, however, to ensure the scalability of the plans to expansive ...
- **p. 2 / 1 Introduction - extractive body cue:** Finally, to ensure the feasibility of the proposed plan, we introduce an iterative replanning pipeline that verifies and refines the initial plan using feedback from ...

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction)): Firstly, we present a mechanism that enables the LLM to conduct a semantic search for a taskrelevant subgraph G′ by manipulating the nodes of a ‘collapsed' 3DSG, which exposes only ...

- **p. 2 / 1 Introduction - extractive body cue:** To this end, we present a scalable approach to ground LLM-based task planners across environments spanning multiple rooms and floors.
- **p. 3 / 1 Introduction - extractive body cue:** We evaluate our framework across a range of 90 tasks organised into four levels of difficulty.
- **p. 1 / 1 Introduction - extractive body cue:** This enables robots to plan complex strategies for a diverse range of tasks that require a substantial amount of background knowledge and semantic comprehension.
- **p. 3 / 1 Introduction - extractive body cue:** Our approach SayPlan ensures feasible and grounded plan generation for a mobile manipulator robot operating in large-scale environments spanning multiple floors and rooms.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Table 2: 3D Scene Graph Token Count Number of tokens required for the full graph vs. collapsed graph. ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 46 | Figure 8: Evaluating the performance of SayPlan's causal planning capabilities as the scale of the environment increases. For ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 32 | Table 18: Correctness, Executability and Number of Replanning Iterations for Long-Horizon Planning Instructions. Evaluating the performance of SayPlan ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

mobile_manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 13 (A Implementation Details). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 3 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 13 (A Implementation Details), objective p. 13 (A Implementation Details).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
