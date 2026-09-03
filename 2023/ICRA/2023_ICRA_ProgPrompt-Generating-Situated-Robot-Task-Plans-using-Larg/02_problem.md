# Problem - ProgPrompt: Generating Situated Robot Task Plans using Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ieeexplore.ieee.org/document/10161317; PDF retrieval source: https://arxiv.org/pdf/2209.11302. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): We illustrate a scenario where an assertion succeeds or fails, and how the generated plan corrects the error before executing the next step.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Task planning can require defining myriad domain knowledge about the world in which a robot needs to act.
- **p. 1 / Abstract - extractive body cue:** To ameliorate that effort, large language models (LLMs) can be used to score potential next actions during task planning, and even generate action sequences directly, ...
- **p. 1 / Abstract - extractive body cue:** However, such methods either require enumerating all possible next steps for scoring, or generate free-form text that may contain actions not possible on a given ...
- **p. 1 / Abstract - extractive body cue:** We present a programmatic LLM prompt structure that enables plan generation functional across situated environments, robot capabilities, and tasks.
- **p. 1 / Abstract - extractive body cue:** Our key insight is to prompt the LLM with program-like specifications of the available actions and objects in an environment, as well as with example ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We illustrate a scenario where an assertion succeeds or fails, and how the generated plan corrects the error before executing the next step.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Everyday household tasks require both commonsense understanding of the world and situated knowledge about the current environment.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | We illustrate a scenario where an assertion succeeds or fails, and how the generated plan corrects the error before executing the next ... | graph, configuration space 또는 task-and-motion planning domain | body wording is the source claim |
| Observation / input | For example, if the LLM produced "reach in and pick up the jar of pickles," that string would have to neatly map ... | start/goal, map, dynamics와 successor/operator description | exact sensor/frame/preprocessing from PDF body |
| State / latent | example, LLM, produced, reach, pick, pickles, string, would, have, neatly | path, trajectory, symbolic state 또는 task-motion decision | notation and tensor shape require body check |
| Output / action | PROMPT, State, Feedback, represents, example, assertion, checks, PROGPROMPTs | feasible action sequence 또는 minimum-cost plan | exact unit/frame/decoder require body check |
| Target outcome | success/reachability and constraint satisfaction | path cost, goal reachability, feasibility와 computation | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s/q; body terms: example, LLM, produced, reach, pick, pickles, string, would, have, neatly | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Decision / output variable | a/ξ ∈ feasible decisions; body terms: present, programmatic, LLM, prompt, structure, enables, plan, generation | p. 1 (Abstract), p. 1 (I. INTRODUCTION) |
| Objective / loss / cost | path/task cost or expected utility; cue terms: make, concrete, recommendations, about, prompt, structure, generation, constraints | p. 1 (Abstract) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (Abstract) |
| Success / guarantee | success/reachability and constraint satisfaction | p. 4 (IV. EXPERIMENTS), p. 2 (Figure/Table caption), p. 4 (IV. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** Everyday household tasks require both commonsense understanding of the world and situated knowledge about the current environment.
- **p. 1 / I. INTRODUCTION - extractive body cue:** The agent needs to know what food is available in the current environment, such as whether the freezer contains fish or the fridge contains chicken.

## What the Paper Changes

PDF body contribution framing (p. 1 (Abstract), p. 1 (I. INTRODUCTION)): We present a programmatic LLM prompt structure that enables plan generation functional across situated environments, robot capabilities, and tasks.

- **p. 1 / I. INTRODUCTION - extractive body cue:** We introduce PROGPROMPT, a prompting scheme that goes beyond conditioning LLMs in natural language.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | Qualitative Analysis and Limitations We manually inspect generated programs and their execution traces from PROGPROMPT and characterize common ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Many failures stem from the decision to make PROGPROMPT agnostic to the deployed environment and its peculiarities, which ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Our physical robot setup did not allow reliably tracking system state and checking assertions, and is prone to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Fig. 2: Our PROGPROMPTs include import statement, object list, and example tasks (PROMPT for Planning). The Generated Plan ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

planning writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), objective p. 1 (Abstract).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
