# Insights — Rapidly-Exploring Random Trees: A New Tool for Path Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (4 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://lavalle.pl/rrtpubs.html; PDF retrieval source: https://lavalle.pl/papers/Lav98c.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1 Introduction - extractive body cue:** Tn this paper, we introduce a randomized data structure for path planning that is designed for problems that, have nonholonomic constraints.
- **p. 1 / 1 Introduction - extractive body cue:** Both are designed with as few heutisties and arbitrary
- **p. 2 / 3. Nice Properties of RRTs - extractive body cue:** The key advantages of RRTs are: 1) the expansion of an RRT is heavily biased. toward unexplored portions of the state space; 2) the dis ...
- **p. 2 / 2. Rapidly-Exploring Random Trees - extractive body cue:** Path planning will generally be viewed as a search in a metric space, X, foF a continuous path from an initial state, nie to A ...
- **p. 1 / 1 Introduction - extractive body cue:** Using state-space representations, this class of problems includes kinodynamic planning [3], which is an extremely general and important area in robotics, virtual prototyping, and many ...
- **p. 3 / 3. Nice Properties of RRTs - extractive body cue:** For these reasons and out preliminary observations from. experimentation, it appears that an RRT-based planner may generally yield better performance than a probabilistic roadmap-based planner; ...
- **p. 3 / 3. Nice Properties of RRTs - extractive body cue:** This leads to a ptobabilistically complete [4] holonomic planner.
- **Contribution anchor:** p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (3. Nice Properties of RRTs), p. 2 (2. Rapidly-Exploring Random Trees), p. 1 (1 Introduction), p. 3 (3. Nice Properties of RRTs)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** The primary difficulty with existing techniques is that, although powerful for standard path planning, they do not naturally extend to general nonholonomic planning problems.
- **p. 1 / 1 Introduction - extractive body cue:** For planning of holonomic systems or steerable nonholonomic systems (see [6] and references therein), the local planning step might be efficient; however, in general, the ...
- **p. 2 / 9 Return T - extractive body cue:** Collision detection can be performed by an incremental method such as Mirtich's V-Clip.
- **p. 2 / 2. Rapidly-Exploring Random Trees - extractive body cue:** States in Xj» could correspond to ver locity bounds, configurations at which a robot is in collision with an obstacle in the world, or several ...
- **p. 3 / 4 Examples - extractive body cue:** In a related paper [7], we presented an RRT-based, planner that computes collision-free kinodynamic trajec~ tories that fire thrusters for hovercrafts and satellites in, cluttered ...
- **p. 3 / 3. Nice Properties of RRTs - extractive body cue:** Collision detection is a key bottleneck in path planning, and an RRT is completely suited for incremental collision detection, This allows the fastest-avaliable collision detection ...
- **Boundary to test:** Collision detection can be performed by an incremental method such as Mirtich's V-Clip.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Tn this paper, we introduce a randomized data structure for path planning that is designed for problems that, have nonholonomic constraints. | p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Reported outcome | For holonomie planning, one can define (ru) = and /lull <1, which implies that any bounded velocity can be achieved. | p. 2 (2. Rapidly-Exploring Random Trees), p. 1 (Abstract) |
| Failure/limitation | Collision detection can be performed by an incremental method such as Mirtich's V-Clip. | p. 2 (9 Return T), p. 2 (2. Rapidly-Exploring Random Trees) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** An RRT is iteratively expanded by applying control inputs that drive the system slightly toward randomly-selected points, 18 opposed to requiring point-to-point convergence, as in the probabilistic roadmap approach. (p. 1, Abstract).
- **Paper-specific mechanism:** Tn this paper, we introduce a randomized data structure for path planning that is designed for problems that, have nonholonomic constraints. (p. 1, 1 Introduction).
- **Evidence boundary:** the reported outcome is For these reasons and out preliminary observations from. experimentation, it appears that an RRT-based planner may generally yield better performance than a probabilistic roadmap-based planner; however, itis difficult to make ... (p. 3, 3. Nice Properties of RRTs); the relevant task/metric cue is parameters as possible, This tends to lead to better performance analysis and consistency of behavior. (p. 2, 1 Introduction). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** The primary difficulty with existing techniques is that, although powerful for standard path planning, they do not naturally extend to general nonholonomic planning problems. (p. 1, 1 Introduction).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `Planning and control`; tags: `Robotics, motion planning, RRT, kinodynamic planning`.
- **Reading predecessor in the generated track queue:** Probabilistic Roadmaps for Path Planning in High-Dimensional Configuration Spaces (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** CHOMP: Gradient Optimization Techniques for Efficient Motion Planning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Collision detection can be performed by an incremental method such as Mirtich's V-Clip.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: An RRT is iteratively expanded by applying control inputs that drive the system slightly toward randomly-selected points, 18 opposed to requiring point-to-point convergence, as in the probabilistic roadmap approach. (p. 1, Abstract); preserve the objective/update rule: A state transition equation of the form # = f(2,u) is defined to express the nonholonomic constraints, The vector u is selected from a set, U, of inputs. (p. 2, 2. Rapidly-Exploring Random Trees).
2. Use the paper-reported task/data/environment cue: Using state-space representations, this class of problems includes kinodynamic planning [3], which is an extremely general and important area in robotics, virtual prototyping, and many other applica. tions. (p. 1, 1 Introduction).
3. Compare against the reported or matched baseline: The key advantages of RRTs are: 1) the expansion of an RRT is heavily biased. toward unexplored portions of the state space; 2) the dis tribution of vertices in an ... (p. 2, 3. Nice Properties of RRTs).
4. Report the body metric with its denominator and aggregation: parameters as possible, This tends to lead to better performance analysis and consistency of behavior. (p. 2, 1 Introduction).
5. Re-run the reported ablation or stress/failure condition: The key advantages of RRTs are: 1) the expansion of an RRT is heavily biased. toward unexplored portions of the state space; 2) the dis tribution of vertices in an ... (p. 2, 3. Nice Properties of RRTs); if none is reported, design one around: The primary difficulty with existing techniques is that, although powerful for standard path planning, they do not naturally extend to general nonholonomic planning problems. (p. 1, 1 Introduction).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (1 Introduction), p. 1 (1 Introduction), match the reported outcome at p. 3 (3. Nice Properties of RRTs), p. 3 (3. Nice Properties of RRTs), p. 1 (1 Introduction), and measure the boundary at p. 1 (1 Introduction), p. 2 (9 Return T).

## Falsifiable research question

Under the paper's stated interface (An RRT is iteratively expanded by applying control inputs that drive the system slightly toward randomly-selected points, 18 opposed to requiring point-to-point ...), does the paper-specific mechanism (Tn this paper, we introduce a randomized data structure for path planning that is designed for problems that, have nonholonomic constraints.) retain the reported evaluation outcome (parameters as possible, This tends to lead to better performance analysis and consistency of behavior.) when tested against the paper's strongest explicit boundary (The primary difficulty with existing techniques is that, although powerful for standard path planning, they do not naturally ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (parameters as possible, This tends to lead to better performance analysis and consistency of behavior.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (4 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Tn this paper, we introduce a randomized data structure for path planning that is designed for problems that, have nonholonomic constraints. (p. 1, 1 Introduction).
- **Paper-supported outcome:** For these reasons and out preliminary observations from. experimentation, it appears that an RRT-based planner may generally yield better performance than a probabilistic roadmap-based planner; however, itis difficult to make ... (p. 3, 3. Nice Properties of RRTs).
- **Strongest explicit boundary:** The primary difficulty with existing techniques is that, although powerful for standard path planning, they do not naturally extend to general nonholonomic planning problems. (p. 1, 1 Introduction).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
