# Insights — Instruction-Augmented Long-Horizon Planning: Embedding Grounding Mechanisms in Embodied Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ojs.aaai.org/index.php/AAAI/article/view/33610; PDF retrieval source: https://ojs.aaai.org/index.php/AAAI/article/view/33610. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / Problem Formulation - extractive body cue:** This library consists of four promptable predicates that can be addressed through prompt engineering based on the reasoning ability of state-of-the-art LLMs, such as holding ...
- **p. 3 / Problem Formulation - extractive body cue:** 2, we propose the InstructionAugmented Long-Horizon Planning (IALP) system to inPromptable on, in, holding, opened Grounding Mechanism at, find, graspable, placeable, detected, reachable Table 1: ...
- **p. 5 / Problem Formulation - extractive body cue:** We introduce six feasibility predicates, comprising two navigation predicates and four manipulation predicates, to maximize the feasibility score Sfb thereby increasing the likelihood that the ...
- **p. 7 / Problem Formulation - extractive body cue:** These results demonstrate that our method can accomplish these tasks within a reasonable time.
- **p. 7 / Problem Formulation - extractive body cue:** Conclusion We propose IALP, a framework that leverages promptable and grounding mechanism-based predicates to construct an informative PDDL problem to represent task-relevant information of the ...
- **p. 5 / Problem Formulation - extractive body cue:** Given the PDDL problem P of a specific task, domain D, and user instruction i, we first query the LLM planner to generate K candidates ...
- **p. 4 / Problem Formulation - extractive body cue:** Then, the robot executes the actions generated and selected by the LLM planner based on the constructed PDDL problem.
- **Contribution anchor:** p. 3 (Problem Formulation), p. 3 (Problem Formulation), p. 5 (Problem Formulation), p. 7 (Problem Formulation), p. 7 (Problem Formulation), p. 5 (Problem Formulation)

### Strongest assumption and failure boundary

- **p. 7 / Problem Formulation - extractive body cue:** Planning failures occur when the planner fails to generate the correct action sequence.
- **p. 5 / Problem Formulation - extractive body cue:** We exclude any grasps that cannot be reached in the current state by computing a grasp reachability index for each candidate grasp.
- **p. 6 / Problem Formulation - extractive body cue:** Given the instruction, "Pick the paper box on the wooden table and place it on the black table," and with the 2D and 3D images ...
- **p. 7 / Problem Formulation - extractive body cue:** For the system without feasibility feedback (labeled as IALP w/o Feasibility Feedback), it encounters difficulty in generating feasible actions due to the removal of feasibility ...
- **p. 3 / Problem Formulation - extractive body cue:** If even one skill fails, then the entire action sequence fails.
- **p. 7 / Problem Formulation - extractive body cue:** All instances of predicate-checking failures were systematically aggregated and classified into three categories: planning, promptable, and grounding mechanisms failures.
- **p. 4 / Problem Formulation - extractive body cue:** For instance, a robot cannot move toward a blue jacket if it cannot identify a 14693
- **Boundary to test:** Planning failures occur when the planner fails to generate the correct action sequence.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | This library consists of four promptable predicates that can be addressed through prompt engineering based on the reasoning ability of state-of-the-art LLMs, such as holding and on, and six predicates determined by ... | p. 3 (Problem Formulation), p. 3 (Problem Formulation) |
| Reported outcome | The results indicate that IALP achieves a success rate of over 80% in all long-term tasks. | p. 7 (Problem Formulation), p. 7 (Problem Formulation) |
| Failure/limitation | Planning failures occur when the planner fails to generate the correct action sequence. | p. 7 (Problem Formulation), p. 7 (Problem Formulation) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `egocentric RGB-D, language/task goal, base-arm proprioception → map/object/contact state와 base-arm coordination decision → base motion plus arm/gripper action`.
- 이 논문의 재사용 가능한 지점은 It captures the utility of the action sequence at:H with respect to satisfying the instruction i on current state st.를 The later term of Equation 1 represents the probability that the action sequence at:H achieve rewards rt:H when executed from the state st, which is conditionally independent of the instruction i.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 map/object/contact state와 base-arm coordination decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Planning failures occur when the planner fails to generate the correct action sequence.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: This library consists of four promptable predicates that can be addressed through prompt engineering based on the reasoning ability of state-of-the-art LLMs, such as holding and on, and six predicates determined by ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Planning and control`; tags: `Robotics, task and motion planning, PDDL, mobile manipulation, long horizon, language grounding, real-world`.
- **Reading predecessor in the generated track queue:** Kinodynamic Trajectory Following with STELA: Simultaneous Trajectory Estimation & Local Adaptation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Neural Assembler: Learning to Generate Fine-Grained Robotic Assembly Instructions from Multi-View Images (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Planning failures occur when the planner fails to generate the correct action sequence.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: While 15 errors out of 100 may appear insignificant, they represent a considerable workload in real-world hardware experiments compared with numerical simulations due to factors such as hardware issues, noise, and physical ....
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 6: The success rate of IALP compared with that of IALP without feasibility feedback and without optimal se- lection, respectively. list the actions and PDDL problems generated for the other four ....
4. Report the body metric and its denominator/aggregation: As a result, the success rate is substantially lower than that of other configurations..
5. Re-run the body-reported ablation/failure condition: For the system without optimal selection, denoted as IALP w/o Optimal Selection, a relatively high success rate is still maintained because feasibility checks are applied to all action generation, which ensures a ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (Problem Formulation), p. 4 (Problem Formulation), p. 4 (Problem Formulation); the primary result is directionally consistent at p. 7 (Problem Formulation), p. 7 (Problem Formulation), p. 3 (Problem Formulation); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 library, consists, four mechanism이 Figure 6: The success rate of IALP compared with that of IALP without feasibility feedback and ... 대비 As a result, the success rate is substantially lower than that of other configurations.을 개선하고, Planning failures occur when the planner fails to generate the correct action sequence. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
