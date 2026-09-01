# Problem - LLM+P: Empowering Large Language Models with Optimal Planning Proficiency

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2304.11477; PDF retrieval source: https://arxiv.org/pdf/2304.11477. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (II. BACKGROUND), p. 2 (II. BACKGROUND)): A Failure Example of GPT-4 in Planning Problem (P1): You have 5 blocks.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Large language models (LLMs) have demonstrated remarkable zero-shot generalization abilities: stateof-the-art chatbots can provide plausible answers to many common questions that arise in daily life.
- **p. 1 / Abstract - extractive PDF cue:** However, so far, LLMs cannot reliably solve long-horizon robot planning problems.
- **p. 1 / Abstract - extractive PDF cue:** By contrast, classical planners, once a problem is given in a formatted way, can use efficient search algorithms to quickly identify correct, or even optimal, ...
- **p. 1 / Abstract - extractive PDF cue:** In an effort to get the best of both worlds, this paper introduces LLM+P, the first framework that incorporates the strengths of classical planners into ...
- **p. 1 / Abstract - extractive PDF cue:** LLM+P takes in a natural language description of a planning problem, then returns a correct (or optimal) plan for solving that problem in natural language.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** A Failure Example of GPT-4 in Planning Problem (P1): You have 5 blocks.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** One cannot place more than one block on another block. b5 is on top of b3. b4 is on top of b2. b2 is on ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | A Failure Example of GPT-4 in Planning Problem (P1): You have 5 blocks. | graph, configuration space 또는 task-and-motion planning domain | body wording is the source claim |
| Observation / input | S G are usually specified as a list of goal conditions, all of which must hold in a goal state. • A ... | start/goal, map, dynamics와 successor/operator description | exact sensor/frame/preprocessing from PDF |
| State / latent | usually, specified, list, goal, conditions, must, hold, state, symbolic, actions | path, trajectory, symbolic state 또는 task-motion decision | notation and tensor shape require body check |
| Output / action | Large, Language, Model, PDDL, Writer, LLMs, planning, long-horizon | feasible action sequence 또는 minimum-cost plan | exact unit/frame/decoder require body check |
| Target outcome | success/reachability and constraint satisfaction | path cost, goal reachability, feasibility와 computation | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s/q; body terms: usually, specified, list, goal, conditions, must, hold, state, symbolic, actions | p. 2 (II. BACKGROUND), p. 2 (II. BACKGROUND), p. 3 (III. METHOD) |
| Decision / output variable | a/ξ ∈ feasible decisions; body terms: Given, LLMs, designed, trained, phenomenon, should, come, surprise | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective / loss / cost | path/task cost or expected utility; cue terms: not recovered | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | success/reachability and constraint satisfaction | p. 5 (1) How well does LLM-AS-P work? To what extent), p. 5 (1) How well does LLM-AS-P work? To what extent), p. 6 (1) We observe that though LLM-AS-P provides a plan) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** One cannot place more than one block on another block. b5 is on top of b3. b4 is on top of b2. b2 is on ...
- **p. 2 / II. BACKGROUND - extractive PDF cue:** The PDDL representation of a planning problem P is separated into two files: a domain file and a problem file.
- **p. 2 / II. BACKGROUND - extractive PDF cue:** The problem PDDL file provides a list of objects to ground the domain, the problem's initial state sinit and goal conditions S G.

## What the Paper Changes

PDF contribution framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): Given how LLMs are designed and trained, this phenomenon should come as no surprise.

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Specifically, they can be (relatively) easily fooled by, for example, asking for the result of a straightforward arithmetic problem that does not appear in their ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Fig. 2: Demonstration of the optimal tidy-up plan. The robot starts at the coffee table and 1) picks ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Limitation: In this paper, we do not ask the LLM to recognize that it has been posed a ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Robots can move around and change colors but cannot step on painted tiles. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | In particular, in the BLOCKSWORLD domain, LLM-AS-P cannot keep track of properties like ON and CLEAR. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

planning writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (II. BACKGROUND), p. 2 (II. BACKGROUND), p. 3 (III. METHOD), p. 3 (III. METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (II. BACKGROUND), p. 2 (II. BACKGROUND), interface p. 2 (II. BACKGROUND), p. 2 (II. BACKGROUND), p. 3 (III. METHOD), p. 3 (III. METHOD), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
