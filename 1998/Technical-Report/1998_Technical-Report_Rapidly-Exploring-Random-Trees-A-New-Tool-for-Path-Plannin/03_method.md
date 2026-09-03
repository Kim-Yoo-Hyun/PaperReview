# Method - Rapidly-Exploring Random Trees: A New Tool for Path Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (4 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://lavalle.pl/rrtpubs.html; PDF retrieval source: https://lavalle.pl/papers/Lav98c.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (3. Nice Properties of RRTs), p. 1 (Abstract), p. 2 (2. Rapidly-Exploring Random Trees), p. 1 (1 Introduction), p. 3 (3. Nice Properties of RRTs), p. 3 (3. Nice Properties of RRTs)): The key advantages of RRTs are: 1) the expansion of an RRT is heavily biased. toward unexplored portions of the state space; 2) the dis tribution of vertices in an ...

## Method Body Digest

- **p. 2 / 3. Nice Properties of RRTs - extractive body cue:** The key advantages of RRTs are: 1) the expansion of an RRT is heavily biased. toward unexplored portions of the state space; 2) the dis ...
- **p. 1 / Abstract - extractive body cue:** We introduce the concept of a Rapidly-exploring Random Tree (RRT) as a randomized data structure that is designed for a broad class of path planning ...
- **p. 2 / 2. Rapidly-Exploring Random Trees - extractive body cue:** Path planning will generally be viewed as a search in a metric space, X, foF a continuous path from an initial state, nie to A ...
- **p. 1 / 1 Introduction - extractive body cue:** Using state-space representations, this class of problems includes kinodynamic planning [3], which is an extremely general and important area in robotics, virtual prototyping, and many ...
- **p. 3 / 3. Nice Properties of RRTs - extractive body cue:** For these reasons and out preliminary observations from. experimentation, it appears that an RRT-based planner may generally yield better performance than a probabilistic roadmap-based planner; ...
- **p. 3 / 3. Nice Properties of RRTs - extractive body cue:** This leads to a ptobabilistically complete [4] holonomic planner.
- **p. 2 / 2. Rapidly-Exploring Random Trees - extractive body cue:** A state transition equation of the form # = f(2,u) is defined to express the nonholonomic constraints, The vector u is selected from a set, ...
- **p. 1 / 1 Introduction - extractive body cue:** The randomized potential field method depends heavily on the choice of a good heuristic potential function, which becomes a daunting task when confronted with obstacles, ...

## Design Rationale

- **p. 1 / 1 Introduction - extractive body cue:** Tn this paper, we introduce a randomized data structure for path planning that is designed for problems that, have nonholonomic constraints.
- **p. 1 / 1 Introduction - extractive body cue:** Both are designed with as few heutisties and arbitrary

## Source Evidence Cues

- **p. 2 / 3. Nice Properties of RRTs - extractive body cue:** The key advantages of RRTs are: 1) the expansion of an RRT is heavily biased. toward unexplored portions of the state space; 2) the dis ...
- **p. 1 / Abstract - extractive body cue:** We introduce the concept of a Rapidly-exploring Random Tree (RRT) as a randomized data structure that is designed for a broad class of path planning ...
- **p. 2 / 2. Rapidly-Exploring Random Trees - extractive body cue:** Path planning will generally be viewed as a search in a metric space, X, foF a continuous path from an initial state, nie to A ...
- **p. 1 / 1 Introduction - extractive body cue:** Using state-space representations, this class of problems includes kinodynamic planning [3], which is an extremely general and important area in robotics, virtual prototyping, and many ...
- **p. 3 / 3. Nice Properties of RRTs - extractive body cue:** For these reasons and out preliminary observations from. experimentation, it appears that an RRT-based planner may generally yield better performance than a probabilistic roadmap-based planner; ...
- **p. 3 / 3. Nice Properties of RRTs - extractive body cue:** This leads to a ptobabilistically complete [4] holonomic planner.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Problem / state representation | decision state와 feasible set을 만든다 | state, map, goal, constraints | source-specific graph, symbolic state, belief 또는 configuration representation을 구성 | search/optimization state | The key advantages of RRTs are: 1) the expansion of an RRT is heavily biased. toward unexplored portions of the state space; ... | p. 2 (3. Nice Properties of RRTs), p. 1 (Abstract) |
| Search / trajectory decision | goal을 향한 candidate를 생성·개선한다 | state와 cost/heuristic | search, sampling, dynamic programming 또는 trajectory optimization을 적용 | plan, path, option 또는 trajectory | We introduce the concept of a Rapidly-exploring Random Tree (RRT) as a randomized data structure that is designed for a broad class ... | p. 1 (Abstract), p. 2 (2. Rapidly-Exploring Random Trees) |
| Execution interface | 계획을 실행 가능한 command로 변환한다 | plan과 current feedback | collision/contact/dynamics check, smoothing, replanning 또는 controller handoff를 수행 | waypoint, option, action 또는 reference | Path planning will generally be viewed as a search in a metric space, X, foF a continuous path from an initial state, ... | p. 2 (2. Rapidly-Exploring Random Trees), p. 1 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 2. Rapidly-Exploring Random Trees - extractive body cue:** A state transition equation of the form # = f(2,u) is defined to express the nonholonomic constraints, The vector u is selected from a set, ...
- **p. 1 / 1 Introduction - extractive body cue:** Tn this paper, we introduce a randomized data structure for path planning that is designed for problems that, have nonholonomic constraints.
- **p. 1 / 1 Introduction - extractive body cue:** The randomized potential field method depends heavily on the choice of a good heuristic potential function, which becomes a daunting task when confronted with obstacles, ...
- **p. 3 / 3. Nice Properties of RRTs - extractive body cue:** Tn the case of nonholonomic systems, the resulting RRT remains probabilistically complete under fairly general conditions; however, convergence issues become even more important, For kinodynamic ...
- **p. 2 / 2. Rapidly-Exploring Random Trees - extractive body cue:** Let NEW.STATE(2,u, At) denote an algorithm that returns nous
- **p. 3 / 3. Nice Properties of RRTs - extractive body cue:** In general, if the points rand are sampled from any smooth probability density function, (2), the vertices of the RRT will distributed according to pla).
- **Formal bridge:** s/q -> a/ξ ∈ feasible decisions -> path/task cost or expected utility -> success/reachability and constraint satisfaction.
- **Equation/algorithm anchors:** p. 2 (2. Rapidly-Exploring Random Trees), p. 1 (1 Introduction), p. 1 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Step, selects, input, rizes, distance, year, rand, ensures, state, remains, transition, equation, form, defined | start/goal, map, dynamics와 successor/operator description | body cue; exact tensor/frame verify |
| State/latent | Step, selects, input, rizes, distance, year, rand, ensures, state, remains | path, trajectory, symbolic state 또는 task-motion decision | body cue; notation verify |
| Action/output | introduce, randomized, data, structure, path, planning, designed, problems, have, nonholonomic | feasible action sequence 또는 minimum-cost plan | body cue; unit/decoder verify |
| Objective/constraint | state, transition, equation, form, defined, express, nonholonomic, constraints, vector, selected | path/task cost or expected utility | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 9 Return T - extractive body cue:** Step 5 selects an input, w, that m rizes the distance from year tO rand» and ensures that the state remains in Xj,,..
- **p. 2 / 2. Rapidly-Exploring Random Trees - extractive body cue:** A state transition equation of the form # = f(2,u) is defined to express the nonholonomic constraints, The vector u is selected from a set, ...
- **p. 1 / Abstract - extractive body cue:** An RRT is iteratively expanded by applying control inputs that drive the system slightly toward randomly-selected points, 18 opposed to requiring point-to-point convergence, as in ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** LaValle.
- **p. 3 / 3. Nice Properties of RRTs - extractive body cue:** Consider, for example, a naive random tree that is constructed incrementally by selecting a vertex at random, an input at random, and then applying the ...
- **p. 3 / 3. Nice Properties of RRTs - extractive body cue:** For these reasons and out preliminary observations from. experimentation, it appears that an RRT-based planner may generally yield better performance than a probabilistic roadmap-based planner; ...
- **Normalized interface:** observation=start/goal, map, dynamics와 successor/operator description; state=path, trajectory, symbolic state 또는 task-motion decision; output/action=feasible action sequence 또는 minimum-cost plan.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | start/goal 또는 task sequence까지의 long-horizon plan; exact horizon은 paper-specific. | For planning of holonomic systems or steerable nonholonomic systems (see [6] and references therein), the local planning step might be efficient; however, ... | episode/sequence/action-chunk boundary |
| Rate / latency | query/event-driven planning 뒤 controller가 partial plan을 실행; numeric rate 확인 필요. | The probabilistic roadmap technique might require the connections of thousands of configurations or states to find a soluti and if each connection ... | Hz/fps, inference time and control rate |
| Memory | graph/tree/roadmap/plan and current state; history size는 method-specific. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | collision checking, search branching 또는 optimization iterations가 latency를 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / Abstract - extractive body cue:** We introduce the concept of a Rapidly-exploring Random Tree (RRT) as a randomized data structure that is designed for a broad class of path planning ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** advantages, RRTs, expansion, RRT, heavily, biased, toward, unexplored, portions, state, space, tribution, vertices, approaches, sampling, distribution, leading, consistent, behavior, probabilistically.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Problem / state representation | Using state-space representations, this class of problems includes kinodynamic planning [3], which is an extremely general and important area in robotics, virtual ... | p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Search / trajectory decision | The key advantages of RRTs are: 1) the expansion of an RRT is heavily biased. toward unexplored portions of the state space; ... | p. 2 (3. Nice Properties of RRTs), p. 3 (3. Nice Properties of RRTs) |
| Execution interface | For holonomie planning, one can define (ru) = and /lull <1, which implies that any bounded velocity can be achieved. | p. 2 (2. Rapidly-Exploring Random Trees), p. 1 (Abstract) |

## Failure and Ablation Link

- **p. 2 / 3. Nice Properties of RRTs - extractive body cue:** The key advantages of RRTs are: 1) the expansion of an RRT is heavily biased. toward unexplored portions of the state space; 2) the dis ...
- **p. 2 / 9 Return T - extractive body cue:** Collision detection can be performed by an incremental method such as Mirtich's V-Clip.
- **p. 2 / 2. Rapidly-Exploring Random Trees - extractive body cue:** States in Xj» could correspond to ver locity bounds, configurations at which a robot is in collision with an obstacle in the world, or several ...
- **p. 3 / 4 Examples - extractive body cue:** In a related paper [7], we presented an RRT-based, planner that computes collision-free kinodynamic trajec~ tories that fire thrusters for hovercrafts and satellites in, cluttered ...
- **p. 3 / 3. Nice Properties of RRTs - extractive body cue:** Collision detection is a key bottleneck in path planning, and an RRT is completely suited for incremental collision detection, This allows the fastest-avaliable collision detection ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (3. Nice Properties of RRTs), p. 1 (Abstract), p. 2 (2. Rapidly-Exploring Random Trees), p. 1 (1 Introduction), p. 3 (3. Nice Properties of RRTs), p. 3 (3. Nice Properties of RRTs), objective p. 2 (2. Rapidly-Exploring Random Trees), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 3 (3. Nice Properties of RRTs), p. 2 (2. Rapidly-Exploring Random Trees), p. 3 (3. Nice Properties of RRTs), temporal p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (9 Return T), p. 2 (9 Return T), p. 3 (3. Nice Properties of RRTs).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (4 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** The key advantages of RRTs are: 1) the expansion of an RRT is heavily biased. toward unexplored portions of the state space; 2) the dis tribution of vertices in an ... (p. 2, 3. Nice Properties of RRTs).
- **Objective/update evidence:** A state transition equation of the form # = f(2,u) is defined to express the nonholonomic constraints, The vector u is selected from a set, U, of inputs. (p. 2, 2. Rapidly-Exploring Random Trees).
- **Temporal/runtime evidence:** For planning of holonomic systems or steerable nonholonomic systems (see [6] and references therein), the local planning step might be efficient; however, in general, the connection problem can be as ... (p. 1, 1 Introduction).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
