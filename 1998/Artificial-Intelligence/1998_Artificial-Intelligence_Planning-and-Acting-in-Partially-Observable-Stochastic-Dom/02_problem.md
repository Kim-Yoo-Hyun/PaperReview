# Problem - Planning and Acting in Partially Observable Stochastic Domains

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (45 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.sciencedirect.com/science/article/pii/S000437029800023X; PDF retrieval source: https://www.cassandra.org/arc/papers/aij98.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction)): Problems like the one described above can be modeled as partially observable Markov decision processes (POMDPs).

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** In this paper, we bring techniques from operations research to bear on the problem of choosing optimal actions in partially observable stochastic domains, We begin ...
- **p. 1 / Abstract - extractive body cue:** We then outline a novel algorithm for solving Pours off line and show how, in some cases, a finitememory controller can be extracted from the ...
- **p. 1 / Abstract - extractive body cue:** We conclude with a discussion of how our approach relates to previous work, the complexity of finding exact solutions to PoMDPs, and of some possibilities ...
- **p. 1 / Abstract - extractive body cue:** Key wonds: planning, uncertainty, partially observable Markov decision processes
- **p. 1 / Abstract - extractive body cue:** Consider the problem of a robot navigating in a large office building.
- **p. 2 / 1 Introduction - extractive body cue:** Problems like the one described above can be modeled as partially observable Markov decision processes (POMDPs).
- **p. 2 / 1 Introduction - extractive body cue:** This is essentially a plareing problem: given a complete and correct model of the world dynamics and a reward structure, find an optimal way to ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Problems like the one described above can be modeled as partially observable Markov decision processes (POMDPs). | graph, configuration space 또는 task-and-motion planning domain | body wording is the source claim |
| Observation / input | The component labeled SE is the state estimator: it is responsible for updating the belief state based on the last action, the ... | start/goal, map, dynamics와 successor/operator description | exact sensor/frame/preprocessing from PDF |
| State / latent | component, labeled, state, estimator, responsible, updating, belief, last, action, current | path, trajectory, symbolic state 또는 task-motion decision | notation and tensor shape require body check |
| Output / action | distributions, encode, agent, subjective, probability, about, state, world | feasible action sequence 또는 minimum-cost plan | exact unit/frame/decoder require body check |
| Target outcome | success/reachability and constraint satisfaction | path cost, goal reachability, feasibility와 computation | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s/q; body terms: component, labeled, state, estimator, responsible, updating, belief, last, action, current | p. 9 (3.2 Problem Structure), p. 3 (1 Introduction), p. 10 (3.2 Problem Structure) |
| Decision / output variable | a/ξ ∈ feasible decisions; body terms: intended, make, contributions, second, describe, novel, algorithmic, solving | p. 3 (1 Introduction), p. 3 (1 Introduction), p. 19 (44 The Witness Algorithm) |
| Objective / loss / cost | path/task cost or expected utility; cue terms: because, maximizing, over, actions, then, policy, trees, same | p. 23 (4.5. Alternative Approaches), p. 19 (44 The Witness Algorithm) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 12 (3.4 Finding an Optimal Policy), p. 23 (4.5. Alternative Approaches), p. 24 (4.5. Alternative Approaches) |
| Success / guarantee | success/reachability and constraint satisfaction | p. 15 (1) I step to go), p. 15 (1) I step to go), p. 24 (5.1 The Tiger Problem) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** This is essentially a plareing problem: given a complete and correct model of the world dynamics and a reward structure, find an optimal way to ...
- **p. 3 / 1 Introduction - extractive body cue:** Section 6 describes the relation between the present approach and prior research in more detail.
- **p. 3 / 1 Introduction - extractive body cue:** Markov decision processes serve as a basis for solving the more complex par tially observable problems that we are ultimately interested in.
- **p. 4 / 1 Introduction - extractive body cue:** An MDP models the synchronous interaction between agent: and world. current state-it has complete and perfect perceptual abilities.

## What the Paper Changes

PDF contribution framing (p. 3 (1 Introduction), p. 3 (1 Introduction), p. 19 (44 The Witness Algorithm)): This paper is intended to make two contributions.

- **p. 3 / 1 Introduction - extractive body cue:** The second is to describe a novel algorithmic approach for solving POMDPs exactly.
- **p. 19 / 44 The Witness Algorithm - extractive body cue:** The code in Table 2 outlines our approach to solving PompPs.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 15 | In such belief states, the agent cannot select | reported limitation/failure wording; scope must be verified |
| body cue at p. 18 | Pruning requires one linear program for each element of the starting set of policy trees and does not ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 25 | The LISTEN action does not change the state of the world. | reported limitation/failure wording; scope must be verified |
| body cue at p. 26 | If the agent starts from the uniform belief state, b= (0.5,0.5), listening once does not change the belief ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

planning writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 9 (3.2 Problem Structure), p. 3 (1 Introduction), p. 10 (3.2 Problem Structure), p. 25 (5.1 The Tiger Problem). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), interface p. 9 (3.2 Problem Structure), p. 3 (1 Introduction), p. 10 (3.2 Problem Structure), p. 25 (5.1 The Tiger Problem), objective p. 23 (4.5. Alternative Approaches), p. 19 (44 The Witness Algorithm).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
