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

- **Paper-specific interface:** We use an interactive planning method that considers action feedback and proposes several candidates at each time step. (p. 3, Problem Formulation).
- **Paper-specific mechanism:** To address these limitations, we present the Instruction-Augmented Long-Horizon Planning (IALP) system, a novel framework that employs LLMs to generate feasible and optimal actions based on real-time sensor feedback, including ... (p. 1, Abstract).
- **Evidence boundary:** the reported outcome is Figure 7: All failure cases of predicate checking in the real- world experiments across five long-horizon tasks. recorded the success cases of the LLM planner generating executable actions, as shown ... (p. 7, Figure/Table caption); the relevant task/metric cue is We define the action sequence optimality score Sop = QH x=t p(ax / i, st:x, at:x-1), where the probability of the next skill ax is considered in terms of the ... (p. 3, Problem Formulation). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Planning failures occur when the planner fails to generate the correct action sequence. (p. 7, Problem Formulation).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Planning and control`; tags: `Robotics, task and motion planning, PDDL, mobile manipulation, long horizon, language grounding, real-world`.
- **Reading predecessor in the generated track queue:** Kinodynamic Trajectory Following with STELA: Simultaneous Trajectory Estimation & Local Adaptation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Neural Assembler: Learning to Generate Fine-Grained Robotic Assembly Instructions from Multi-View Images (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Planning failures occur when the planner fails to generate the correct action sequence.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: We use an interactive planning method that considers action feedback and proposes several candidates at each time step. (p. 3, Problem Formulation); preserve the objective/update rule: The later term of Equation 1 represents the probability that the action sequence at:H achieve rewards rt:H when executed from the state st, which is conditionally independent of the instruction ... (p. 3, Problem Formulation).
2. Use the paper-reported task/data/environment cue: Discussion To investigate the types of failure cases in real-world experiments, we conducted 20 trials for each task within a realworld environment and recorded all occurring errors. (p. 7, Problem Formulation).
3. Compare against the reported or matched baseline: Figure 6: The success rate of IALP compared with that of IALP without feasibility feedback and without optimal se- lection, respectively. list the actions and PDDL problems generated for the ... (p. 7, Figure/Table caption).
4. Report the body metric with its denominator and aggregation: We define the action sequence optimality score Sop = QH x=t p(ax / i, st:x, at:x-1), where the probability of the next skill ax is considered in terms of the ... (p. 3, Problem Formulation).
5. Re-run the reported ablation or stress/failure condition: We assume an open-world setting, wherein the robot operates without prior knowledge of task-relevant objects or other ground truth information. (p. 3, Problem Formulation); if none is reported, design one around: Planning failures occur when the planner fails to generate the correct action sequence. (p. 7, Problem Formulation).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (Abstract), p. 1 (Abstract), match the reported outcome at p. 7 (Figure/Table caption), p. 7 (Problem Formulation), p. 7 (Problem Formulation), and measure the boundary at p. 7 (Problem Formulation), p. 7 (Problem Formulation).

## Falsifiable research question

Under the paper's stated interface (We use an interactive planning method that considers action feedback and proposes several candidates at each time step.), does the paper-specific mechanism (To address these limitations, we present the Instruction-Augmented Long-Horizon Planning (IALP) system, a novel framework that employs LLMs to generate feasible and ...) retain the reported evaluation outcome (We define the action sequence optimality score Sop = QH x=t p(ax / i, st:x, at:x-1), where the ...) when tested against the paper's strongest explicit boundary (Planning failures occur when the planner fails to generate the correct action sequence.)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (We define the action sequence optimality score Sop = QH x=t p(ax / i, st:x, at:x-1), where the ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (9 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** To address these limitations, we present the Instruction-Augmented Long-Horizon Planning (IALP) system, a novel framework that employs LLMs to generate feasible and optimal actions based on real-time sensor feedback, including ... (p. 1, Abstract).
- **Paper-supported outcome:** Figure 7: All failure cases of predicate checking in the real- world experiments across five long-horizon tasks. recorded the success cases of the LLM planner generating executable actions, as shown ... (p. 7, Figure/Table caption).
- **Strongest explicit boundary:** Planning failures occur when the planner fails to generate the correct action sequence. (p. 7, Problem Formulation).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
