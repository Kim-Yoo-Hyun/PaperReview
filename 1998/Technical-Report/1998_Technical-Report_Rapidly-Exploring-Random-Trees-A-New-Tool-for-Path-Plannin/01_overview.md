# Rapidly-Exploring Random Trees: A New Tool for Path Planning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (4 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://lavalle.pl/papers/Lav98c.pdf.
> PDF retrieval source: https://lavalle.pl/papers/Lav98c.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 1998 / Technical Report
- Authors: Steven M. LaValle
- Primary track: Planning and control
- Tier: NEXT
- Tags: Robotics, motion planning, RRT, kinodynamic planning
- Official paper: https://lavalle.pl/papers/Lav98c.pdf
- Full-text retrieval: https://lavalle.pl/papers/Lav98c.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (4 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RRT는 상태 공간에서 무작위로 뽑은 점 쪽으로 도달 가능한 상태를 하나씩 더해 경로 탐색 트리를 키운다. [PDF 1쪽](https://lavalle.pl/papers/Lav98c.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We introduce the concept of a Rapidly-exploring Random Tree (RRT) as a randomized data structure that is designed for a broad class of path planning ...
- **p. 1 / Abstract - extractive body cue:** An RRT is iteratively expanded by applying control inputs that drive the system slightly toward randomly-selected points, 18 opposed to requiring point-to-point convergence, as in ...
- **p. 1 / Abstract - extractive body cue:** Several desir- ‘able properties and a basic implementation of RRTs are discussed.
- **p. 1 / Abstract - extractive body cue:** To date, we have successfully applied RRTs to holonomic, nonholonomic, and kinodynamic planning problems of up to twelve degrees of freedom.
- **p. 1 / 1 Introduction - extractive body cue:** ‘Over the past decade, several randomized approaches have been proposed and successfully applied to the general problem of path planning in a high-dimensional configuration space, ...
- **p. 1 / 1 Introduction - extractive body cue:** The primary difficulty with existing techniques is that, although powerful for standard path planning, they do not naturally extend to general nonholonomic planning problems.
- **p. 1 / 1 Introduction - extractive body cue:** For planning of holonomic systems or steerable nonholonomic systems (see [6] and references therein), the local planning step might be efficient; however, in general, the ...

## Core Idea

- **p. 2 / 3. Nice Properties of RRTs - extractive body cue:** The key advantages of RRTs are: 1) the expansion of an RRT is heavily biased. toward unexplored portions of the state space; 2) the dis ...
- **p. 2 / 2. Rapidly-Exploring Random Trees - extractive body cue:** Path planning will generally be viewed as a search in a metric space, X, foF a continuous path from an initial state, nie to A ...
- **p. 1 / 1 Introduction - extractive body cue:** Using state-space representations, this class of problems includes kinodynamic planning [3], which is an extremely general and important area in robotics, virtual prototyping, and many ...
- **p. 3 / 3. Nice Properties of RRTs - extractive body cue:** This leads to a ptobabilistically complete [4] holonomic planner.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Step 5 selects an input, w, that m rizes the distance from year tO rand» and ensures that the state remains in Xj,,.. | start/goal, map, dynamics와 successor/operator description | p. 2 (9 Return T), p. 2 (2. Rapidly-Exploring Random Trees) |
| State/latent | Step, selects, input, rizes, distance, year, rand, ensures, state, remains, transition, equation | path, trajectory, symbolic state 또는 task-motion decision | p. 2 (9 Return T), p. 2 (2. Rapidly-Exploring Random Trees), p. 1 (Abstract) |
| Output/action | A state transition equation of the form # = f(2,u) is defined to express the nonholonomic constraints, The vector u is selected from a set, U, of inputs. | feasible action sequence 또는 minimum-cost plan | p. 2 (2. Rapidly-Exploring Random Trees), p. 1 (Abstract), p. 1 (Body text (section boundary not confidently recovered)) |
| Objective/outcome | A state transition equation of the form # = f(2,u) is defined to express the nonholonomic constraints, The vector u is selected from a set, U, of inputs. | path cost, goal reachability, feasibility와 computation | p. 2 (2. Rapidly-Exploring Random Trees), p. 1 (1 Introduction), p. 1 (1 Introduction) |

## Main Claims and Actual Contribution

- 가까운 기존 노드를 골라 짧게 제어 입력을 적용한다. 두 표본 사이를 정확히 잇는 국소 해법 없이도 트리를 확장할 수 있다. [PDF 2쪽](https://lavalle.pl/papers/Lav98c.pdf#page=2)
- 논문은 기본 알고리즘과 탐색 성질을 설명하고 홀로노믹·비홀로노믹·동역학 제약이 있는 계획 문제에 적용했다고 보고한다. [PDF 1쪽](https://lavalle.pl/papers/Lav98c.pdf#page=1) · [PDF 3쪽](https://lavalle.pl/papers/Lav98c.pdf#page=3)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 2 (2. Rapidly-Exploring Random Trees), p. 1 (Abstract) |
| Embodiment/environment | Using state-space representations, this class of problems includes kinodynamic planning [3], which is an extremely general and important area in robotics, virtual prototyping, and many other applica. tions. | hardware/simulator version and reset protocol | p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Dataset/benchmark | States in Xj» could correspond to ver locity bounds, configurations at which a robot is in collision with an obstacle in the world, or several other interpretations, depending on the application, A ... | role, split, size and leakage | p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (2. Rapidly-Exploring Random Trees), p. 3 (3. Nice Properties of RRTs) |
| Metric | The key advantages of RRTs are: 1) the expansion of an RRT is heavily biased. toward unexplored portions of the state space; 2) the dis tribution of vertices in an RRT approaches ... | definition, denominator, direction and uncertainty | p. 2 (3. Nice Properties of RRTs), p. 3 (3. Nice Properties of RRTs), p. 1 (Abstract) |
| Baseline/ablation | The key advantages of RRTs are: 1) the expansion of an RRT is heavily biased. toward unexplored portions of the state space; 2) the dis tribution of vertices in an RRT approaches ... | fair input/data/compute/action matching | p. 2 (3. Nice Properties of RRTs), p. 3 (3. Nice Properties of RRTs), p. 3 (3. Nice Properties of RRTs) |

## Explicit Limitations and Failure Boundary

- **p. 2 / 9 Return T - extractive body cue:** Collision detection can be performed by an incremental method such as Mirtich's V-Clip.
- **p. 2 / 2. Rapidly-Exploring Random Trees - extractive body cue:** States in Xj» could correspond to ver locity bounds, configurations at which a robot is in collision with an obstacle in the world, or several ...
- **p. 3 / 4 Examples - extractive body cue:** In a related paper [7], we presented an RRT-based, planner that computes collision-free kinodynamic trajec~ tories that fire thrusters for hovercrafts and satellites in, cluttered ...
- **p. 3 / 3. Nice Properties of RRTs - extractive body cue:** Collision detection is a key bottleneck in path planning, and an RRT is completely suited for incremental collision detection, This allows the fastest-avaliable collision detection ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 Introduction), p. 2 (3. Nice Properties of RRTs), p. 1 (Abstract), p. 2 (2. Rapidly-Exploring Random Trees)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (4 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** For planning of holonomic systems or steerable nonholonomic systems (see [6] and references therein), the local planning step might be efficient; however, in general, the connection problem can be as ... (p. 1, 1 Introduction).
- **Explicit failure boundary:** The primary difficulty with existing techniques is that, although powerful for standard path planning, they do not naturally extend to general nonholonomic planning problems. (p. 1, 1 Introduction).
