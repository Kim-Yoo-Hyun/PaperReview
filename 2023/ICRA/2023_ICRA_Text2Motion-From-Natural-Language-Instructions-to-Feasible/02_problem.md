# Problem - Text2Motion: From Natural Language Instructions to Feasible Plans

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (30 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2303.12153; PDF retrieval source: https://arxiv.org/pdf/2303.12153. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 3 (3.1 LLM and skill library), p. 4 (3.2 The planning objective), p. 1 (1 Introduction), p. 2 (1 Introduction)): Such strategies are challenged in long-horizon settings, where the 1.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We propose Text2Motion, a language-based planning framework enabling robots to solve sequential manipulation tasks that require long-horizon reasoning.
- **p. 1 / Abstract - extractive body cue:** Given a natural language instruction, our framework constructs both a task- and motion-level plan that is verified to reach inferred symbolic goals.
- **p. 1 / Abstract - extractive body cue:** Text2Motion uses feasibility heuristics encoded in Q-functions of a library of skills to guide task planning with Large Language Models.
- **p. 1 / Abstract - extractive body cue:** Whereas previous language-based planners only consider the feasibility of individual skills, Text2Motion actively resolves geometric dependencies spanning skill sequences by performing geometric feasibility planning during ...
- **p. 1 / Abstract - extractive body cue:** We evaluate our method on a suite of problems that require long-horizon reasoning, interpretation of abstract goals, and handling of partial affordance perception.
- **p. 1 / 1 Introduction - extractive body cue:** Such strategies are challenged in long-horizon settings, where the 1.
- **p. 3 / 3.1 LLM and skill library - extractive body cue:** If the skill succeeds, it receives a binary reward of r (or ¬r if it fails).

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Such strategies are challenged in long-horizon settings, where the 1 | graph, configuration space 또는 task-and-motion planning domain | body wording is the source claim |
| Observation / input | We define a satisfaction function F G sat (s) : S →{0, 1} which takes as input a geometric state s and ... | start/goal, map, dynamics와 successor/operator description | exact sensor/frame/preprocessing from PDF body |
| State / latent | define, satisfaction, function, takes, input, geometric, state, evaluates, goal, proposition | path, trajectory, symbolic state 또는 task-motion decision | notation and tensor shape require body check |
| Output / action | shooting, greedy-search, planners, LLM, predict, valid, goal, states | feasible action sequence 또는 minimum-cost plan | exact unit/frame/decoder require body check |
| Target outcome | success/reachability and constraint satisfaction | path cost, goal reachability, feasibility와 computation | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s/q; body terms: define, satisfaction, function, takes, input, geometric, state, evaluates, goal, proposition | p. 5 (4.1 Goal prediction), p. 3 (3.1 LLM and skill library), p. 5 (4.1 Goal prediction) |
| Decision / output variable | a/ξ ∈ feasible decisions; body terms: Text2Motion, language-based, planning, framework, interfaces, LLM, library, learned | p. 2 (1 Introduction), p. 5 (4.2 Shooting-based planning), p. 6 (4.3 Search-based planning) |
| Objective / loss / cost | path/task cost or expected utility; cue terms: then, raise, planning, failure, maxj, success, return, best | p. 4 (4.1 Goal prediction), p. 4 (4 Methods), p. 5 (4.2 Shooting-based planning), p. 6 (4.3 Search-based planning) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (4.2 Shooting-based planning), p. 6 (4.3 Search-based planning), p. 6 (4.3 Search-based planning) |
| Success / guarantee | success/reachability and constraint satisfaction | p. 10 (5.5 Evaluation and metrics), p. 10 (6.1 Feasibility planning is required), p. 11 (6.2 Search-based reasoning is) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 3 / 3.1 LLM and skill library - extractive body cue:** If the skill succeeds, it receives a binary reward of r (or ¬r if it fails).
- **p. 4 / 3.2 The planning objective - extractive body cue:** If just one skill fails (reward ¬r), then the entire plan fails.
- **p. 1 / 1 Introduction - extractive body cue:** Such systems can generalize within the logical planning domain specified by experts.
- **p. 2 / 1 Introduction - extractive body cue:** Therefore, we ask in this paper: how can we verify the correctness and feasibility of LLM-generated plans prior to execution?

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 5 (4.2 Shooting-based planning), p. 6 (4.3 Search-based planning), p. 2 (1 Introduction), p. 3 (3.1 LLM and skill library)): We propose Text2Motion, a language-based planning framework that interfaces an LLM with a library of learned skills and a geometric feasibility planner [8] to solve complex sequential manipulation tasks (Figure ...

- **p. 5 / 4.2 Shooting-based planning - extractive body cue:** To this end, the first strategy we propose is a shooting-based Algorithm 1 Shooting-based LLM planner 1: globals: Lψ, Lχ, SatFunc, LLM, STAP 2: function ...
- **p. 6 / 4.3 Search-based planning - extractive body cue:** We propose a second planner, greedy-search (see Figure 2, Right), which at each planning iteration ranks candidate skills predicted by the LLM and adds the ...
- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are twofold: (i) a hybrid LLM planner that synergistically integrates shooting-based and search-based planning strategies to construct geometrically feasible plans for tasks not ...
- **p. 3 / 3.1 LLM and skill library - extractive body cue:** Each skill ψ consists of a policy π(a/s) and a parameterized manipulation primitive ϕ(a) [59], and is associated with a contextual bandit, or a single-timestep ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 11 | Text2Motion relies on greedy-search as a fallback if shooting fails, and thus can also contend with PAP tasks. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Two failure cases are tracked: i) planning failure: the method does not produce a sequence of skills ψ1:H ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | 4) results in a state that satisfies F G sat within a maximum plan length of dmax; ii) ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | This is expected because shooting does not exhibit planning failures on these tasks (Figure 6) and Text2Motion starts ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

planning writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (4.1 Goal prediction), p. 3 (3.1 LLM and skill library), p. 5 (4.1 Goal prediction), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 Introduction), p. 3 (3.1 LLM and skill library), p. 4 (3.2 The planning objective), p. 1 (1 Introduction), p. 2 (1 Introduction), interface p. 5 (4.1 Goal prediction), p. 3 (3.1 LLM and skill library), p. 5 (4.1 Goal prediction), p. 2 (1 Introduction), objective p. 4 (4.1 Goal prediction), p. 4 (4 Methods), p. 5 (4.2 Shooting-based planning), p. 6 (4.3 Search-based planning).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
