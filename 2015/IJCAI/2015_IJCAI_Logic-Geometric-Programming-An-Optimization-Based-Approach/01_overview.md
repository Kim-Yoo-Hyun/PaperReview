# Logic-Geometric Programming: An Optimization-Based Approach to Combined Task and Motion Planning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ijcai.org/Proceedings/15/Papers/274.pdf.
> PDF retrieval source: https://www.ijcai.org/Proceedings/15/Papers/274.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2015 / IJCAI
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: NEXT
- Tags: Robotics, Planning, task and motion planning, optimization
- Official paper: https://www.ijcai.org/Proceedings/15/Papers/274.pdf
- Full-text retrieval: https://www.ijcai.org/Proceedings/15/Papers/274.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 planning 문제를 이해하기 위해 읽는다. 본문은 Most existing TAMP approaches, however, require a well-defined task planning problem including a symbolic goal description.를 문제로 두고, Besides the novel formulation of manipulation planning as an LGP, we think of the concept of the effective end space and its optimization as a search heuristic as the core contributions of ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We consider problems of sequential robot manipulation (aka. combined task and motion planning) where the objective is primarily given in terms of a cost function ...
- **p. 1 / Abstract - extractive body cue:** In this case we should leverage optimization methods to inform search over potential action sequences.
- **p. 1 / Abstract - extractive body cue:** We propose to formulate the problem holistically as a 1storder logic extension of a mathematical program: a non-linear constrained program over the full world trajectory ...
- **p. 1 / Abstract - extractive body cue:** We tackle the challenge of solving such programs by proposing three levels of approximation: The coarsest level introduces the concept of the effective end state ...
- **p. 1 / Abstract - extractive body cue:** Optimization on this level is fast and can inform symbolic search.
- **p. 1 / 1 Introduction - extractive body cue:** Most existing TAMP approaches, however, require a well-defined task planning problem including a symbolic goal description.
- **p. 1 / 1 Introduction - extractive body cue:** The specific methods we propose in this paper are (yet!) in many respects less efficient than existing TAMP approaches; in particular we cannot scale to ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Besides the novel formulation of manipulation planning as an LGP, we think of the concept of the effective end space and its optimization as a ...
- **p. 1 / 1 Introduction - extractive body cue:** The specific methods we propose in this paper are (yet!) in many respects less efficient than existing TAMP approaches; in particular we cannot scale to ...
- **p. 2 / 1 Introduction - extractive body cue:** In this paper we propose three levels on which geometric reasoning (that is, optimization over geometric configurations and paths) may inform symbolic search towards a ...
- **p. 1 / Abstract - extractive body cue:** We propose to formulate the problem holistically as a 1storder logic extension of a mathematical program: a non-linear constrained program over the full world trajectory ...
- **p. 1 / 1 Introduction - extractive body cue:** First, we aim for planners that can deal with arbitrary objective functions ψ(x(T)) on the final geometric configuration x(T) and overall control costs.
- **p. 2 / 1 Introduction - extractive body cue:** This implies the challenge of motion optimization across kinematic switches of the world configuration (across action boundaries) to allow for the optimization over the full ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We propose to formulate the problem holistically as a 1storder logic extension of a mathematical program: a non-linear constrained program over the full world trajectory where the symbolic state-action sequence defines the ... | start/goal, map, dynamics와 successor/operator description | p. 1 (Abstract), p. 1 (Abstract) |
| State/latent | formulate, problem, holistically, storder, logic, extension, mathematical, program, non-linear, constrained, over, full | path, trajectory, symbolic state 또는 task-motion decision | p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction) |
| Output/action | We tackle the challenge of solving such programs by proposing three levels of approximation: The coarsest level introduces the concept of the effective end state kinematics, parametrically describing all possible end state ... | feasible action sequence 또는 minimum-cost plan | p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Objective/outcome | We consider problems of sequential robot manipulation (aka. combined task and motion planning) where the objective is primarily given in terms of a cost function over the final geometric state, rather than ... | path cost, goal reachability, feasibility와 computation | p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** Besides the novel formulation of manipulation planning as an LGP, we think of the concept of the effective end space and its optimization as a ...
- **p. 1 / 1 Introduction - extractive body cue:** The specific methods we propose in this paper are (yet!) in many respects less efficient than existing TAMP approaches; in particular we cannot scale to ...
- **p. 2 / 1 Introduction - extractive body cue:** In this paper we propose three levels on which geometric reasoning (that is, optimization over geometric configurations and paths) may inform symbolic search towards a ...
- **p. 1 / Abstract - extractive body cue:** We propose to formulate the problem holistically as a 1storder logic extension of a mathematical program: a non-linear constrained program over the full world trajectory ...
- **p. 5 / 5 Experiments - extractive body cue:** For brevity, we provide a detailed definition of ψ(x(T)) and quantitative results on achieved scores in an appendix on the author webpage.
- **p. 6 / 5 Experiments - extractive body cue:** The example demonstrates success on our construction problems, leading to (locally, approximately) optimal full manipulation paths across up to 50 manipulations.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (5 Experiments), p. 6 (5 Experiments) |
| Embodiment/environment | Instead we optimize the grasp pose (the relative object-hand pose), assuming that a compliant real-world gripper could perform the actual grasp. | hardware/simulator version and reset protocol | p. 5 (5 Experiments), p. 5 (5 Experiments) |
| Dataset/benchmark | Further, the paths have 20 time steps per manipulation; for 25 objects this is a (15dimensional) trajectory with 1000 time steps across 50 manipulations. | role, split, size and leakage | p. 5 (5 Experiments), p. 5 (5 Experiments), p. 6 (5 Experiments), p. 6 (5 Experiments) |
| Metric | When blocks are placed on a board, we reward more central positionings. | definition, denominator, direction and uncertainty | p. 5 (5 Experiments), p. 5 (5 Experiments), p. 6 (5 Experiments) |
| Baseline/ablation | not stated or recoverable in the selected PDF body | fair input/data/compute/action matching | 본문 anchor 없음 |

## Explicit Limitations and Failure Boundary

- **p. 5 / 2 Related Work - extractive body cue:** Further constraints concern standard motion optimization aspects such as collision avoidance.
- **p. 5 / 5 Experiments - extractive body cue:** The geometric and differential constraints hpath, gpath implement zero velocity of the object-hand pose while inhand, zero velocities and accelerations during pick and place, and ...
- **p. 6 / 5 Experiments - extractive body cue:** The resulting trajectories are smooth and collision free (if keyframe optimization indicated feasibility) and generate the optimized end state.

## Why Read It

Planning and control의 planning 문제를 이해하기 위해 읽는다. 본문은 Most existing TAMP approaches, however, require a well-defined task planning problem including a symbolic goal description.를 문제로 두고, Besides the novel formulation of manipulation planning as an LGP, we think of the concept of the effective end space and its optimization as a search heuristic as the core contributions of ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (7 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Most existing TAMP approaches, however, require a well-defined task planning problem including a symbolic goal description. (p. 1, 1 Introduction).
- **Actual contribution:** Besides the novel formulation of manipulation planning as an LGP, we think of the concept of the effective end space and its optimization as a search heuristic as the core ... (p. 2, 1 Introduction).
- **Evaluation boundary:** For brevity, we provide a detailed definition of ψ(x(T)) and quantitative results on achieved scores in an appendix on the author webpage. (p. 5, 5 Experiments).
- **Explicit failure boundary:** We did not consider articulated fingers and optimize over finger motions for grasping as this is unrealistic to transfer to real-world. (p. 5, 5 Experiments).
