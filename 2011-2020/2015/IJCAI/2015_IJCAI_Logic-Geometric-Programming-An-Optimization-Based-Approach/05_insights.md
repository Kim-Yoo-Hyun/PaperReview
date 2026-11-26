# Insights — Logic-Geometric Programming: An Optimization-Based Approach to Combined Task and Motion Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ijcai.org/Proceedings/15/Papers/274.pdf; PDF retrieval source: https://www.ijcai.org/Proceedings/15/Papers/274.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** Besides the novel formulation of manipulation planning as an LGP, we think of the concept of the effective end space and its optimization as a ...
- **p. 1 / 1 Introduction - extractive body cue:** The specific methods we propose in this paper are (yet!) in many respects less efficient than existing TAMP approaches; in particular we cannot scale to ...
- **p. 2 / 1 Introduction - extractive body cue:** In this paper we propose three levels on which geometric reasoning (that is, optimization over geometric configurations and paths) may inform symbolic search towards a ...
- **p. 1 / Abstract - extractive body cue:** We propose to formulate the problem holistically as a 1storder logic extension of a mathematical program: a non-linear constrained program over the full world trajectory ...
- **p. 1 / 1 Introduction - extractive body cue:** First, we aim for planners that can deal with arbitrary objective functions ψ(x(T)) on the final geometric configuration x(T) and overall control costs.
- **p. 2 / 1 Introduction - extractive body cue:** This implies the challenge of motion optimization across kinematic switches of the world configuration (across action boundaries) to allow for the optimization over the full ...
- **Contribution anchor:** p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** Most existing TAMP approaches, however, require a well-defined task planning problem including a symbolic goal description.
- **p. 1 / 1 Introduction - extractive body cue:** The specific methods we propose in this paper are (yet!) in many respects less efficient than existing TAMP approaches; in particular we cannot scale to ...
- **p. 2 / 1 Introduction - extractive body cue:** All three levels raise novel interesting challenges for motion (or configuration) optimizers.
- **p. 2 / 1 Introduction - extractive body cue:** This implies the challenge of motion optimization across kinematic switches of the world configuration (across action boundaries) to allow for the optimization over the full ...
- **p. 5 / 2 Related Work - extractive body cue:** Further constraints concern standard motion optimization aspects such as collision avoidance.
- **p. 5 / 5 Experiments - extractive body cue:** The geometric and differential constraints hpath, gpath implement zero velocity of the object-hand pose while inhand, zero velocities and accelerations during pick and place, and ...
- **p. 6 / 5 Experiments - extractive body cue:** The resulting trajectories are smooth and collision free (if keyframe optimization indicated feasibility) and generate the optimized end state.
- **Boundary to test:** Further constraints concern standard motion optimization aspects such as collision avoidance.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Besides the novel formulation of manipulation planning as an LGP, we think of the concept of the effective end space and its optimization as a search heuristic as the core contributions of ... | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Reported outcome | For brevity, we provide a detailed definition of ψ(x(T)) and quantitative results on achieved scores in an appendix on the author webpage. | p. 5 (5 Experiments), p. 6 (5 Experiments) |
| Failure/limitation | Further constraints concern standard motion optimization aspects such as collision avoidance. | p. 5 (2 Related Work), p. 5 (5 Experiments) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** The specific methods we propose in this paper are (yet!) in many respects less efficient than existing TAMP approaches; in particular we cannot scale to similar depths (action sequence horizons) ... (p. 1, 1 Introduction).
- **Paper-specific mechanism:** Besides the novel formulation of manipulation planning as an LGP, we think of the concept of the effective end space and its optimization as a search heuristic as the core ... (p. 2, 1 Introduction).
- **Evidence boundary:** the reported outcome is For brevity, we provide a detailed definition of ψ(x(T)) and quantitative results on achieved scores in an appendix on the author webpage. (p. 5, 5 Experiments); the relevant task/metric cue is When blocks are placed on a board, we reward more central positionings. (p. 5, 5 Experiments). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** We did not consider articulated fingers and optimize over finger motions for grasping as this is unrealistic to transfer to real-world. (p. 5, 5 Experiments).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Planning and control`; tags: `Robotics, Planning, task and motion planning, optimization`.
- **Reading predecessor in the generated track queue:** Whole-Body Nonlinear Model Predictive Control Through Contacts for Quadrupeds (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** FFRob: Leveraging Symbolic Planning for Efficient Task and Motion Planning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Further constraints concern standard motion optimization aspects such as collision avoidance.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: The specific methods we propose in this paper are (yet!) in many respects less efficient than existing TAMP approaches; in particular we cannot scale to similar depths (action sequence horizons) ... (p. 1, 1 Introduction); preserve the objective/update rule: Further, the above problems are inherently optimization problems, not constraint satisfaction problems. (p. 1, 1 Introduction).
2. Use the paper-reported task/data/environment cue: The control costs penalized accelerations and implemented a weak prior for the robot arm to be in the homing posi1934 (p. 5, 5 Experiments).
3. Compare against the reported or matched baseline: For brevity, we provide a detailed definition of ψ(x(T)) and quantitative results on achieved scores in an appendix on the author webpage. (p. 5, 5 Experiments).
4. Report the body metric with its denominator and aggregation: When blocks are placed on a board, we reward more central positionings. (p. 5, 5 Experiments).
5. Re-run the reported ablation or stress/failure condition: For brevity, we provide a detailed definition of ψ(x(T)) and quantitative results on achieved scores in an appendix on the author webpage. (p. 5, 5 Experiments); if none is reported, design one around: We did not consider articulated fingers and optimize over finger motions for grasping as this is unrealistic to transfer to real-world. (p. 5, 5 Experiments).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1 Introduction), p. 1 (1 Introduction), match the reported outcome at p. 5 (5 Experiments), p. 5 (5 Experiments), p. 5 (5 Experiments), and measure the boundary at p. 5 (5 Experiments), p. 5 (5 Experiments).

## Falsifiable research question

Under the paper's stated interface (The specific methods we propose in this paper are (yet!) in many respects less efficient than existing TAMP approaches; in particular we ...), does the paper-specific mechanism (Besides the novel formulation of manipulation planning as an LGP, we think of the concept of the effective end space and its ...) retain the reported evaluation outcome (When blocks are placed on a board, we reward more central positionings.) when tested against the paper's strongest explicit boundary (We did not consider articulated fingers and optimize over finger motions for grasping as this is unrealistic to ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (When blocks are placed on a board, we reward more central positionings.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (7 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Besides the novel formulation of manipulation planning as an LGP, we think of the concept of the effective end space and its optimization as a search heuristic as the core ... (p. 2, 1 Introduction).
- **Paper-supported outcome:** For brevity, we provide a detailed definition of ψ(x(T)) and quantitative results on achieved scores in an appendix on the author webpage. (p. 5, 5 Experiments).
- **Strongest explicit boundary:** We did not consider articulated fingers and optimize over finger motions for grasping as this is unrealistic to transfer to real-world. (p. 5, 5 Experiments).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
