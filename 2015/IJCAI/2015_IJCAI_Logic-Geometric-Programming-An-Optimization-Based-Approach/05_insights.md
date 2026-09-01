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

- **Closed-loop position:** `start/goal, map, dynamics와 successor/operator description → path, trajectory, symbolic state 또는 task-motion decision → feasible action sequence 또는 minimum-cost plan`.
- 이 논문의 재사용 가능한 지점은 We propose to formulate the problem holistically as a 1storder logic extension of a mathematical program: a non-linear constrained program over the full world trajectory where the symbolic state-action sequence defines the ...를 We tackle the challenge of solving such programs by proposing three levels of approximation: The coarsest level introduces the concept of the effective end state kinematics, parametrically describing all possible end state ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 path, trajectory, symbolic state 또는 task-motion decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Further constraints concern standard motion optimization aspects such as collision avoidance.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Besides the novel formulation of manipulation planning as an LGP, we think of the concept of the effective end space and its optimization as a search heuristic as the core contributions of ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Planning and control`; tags: `Robotics, Planning, task and motion planning, optimization`.
- **Reading predecessor in the generated track queue:** Whole-Body Nonlinear Model Predictive Control Through Contacts for Quadrupeds (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** FFRob: Leveraging Symbolic Planning for Efficient Task and Motion Planning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Further constraints concern standard motion optimization aspects such as collision avoidance.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Instead we optimize the grasp pose (the relative object-hand pose), assuming that a compliant real-world gripper could perform the actual grasp..
3. Compare against the body-reported baseline or a matched simpler baseline: baseline not recovered.
4. Report the body metric and its denominator/aggregation: When blocks are placed on a board, we reward more central positionings..
5. Re-run the body-reported ablation/failure condition: Further constraints concern standard motion optimization aspects such as collision avoidance..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction); the primary result is directionally consistent at p. 5 (5 Experiments), p. 6 (5 Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Besides, novel, formulation mechanism이 a matched simpler baseline 대비 When blocks are placed on a board, we reward more central positionings.을 개선하고, Further constraints concern standard motion optimization aspects such as collision avoidance. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
