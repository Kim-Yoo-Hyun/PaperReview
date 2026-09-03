# Insights — WoCoCo: Learning Whole-Body Humanoid Control with Sequential Contacts

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=Czs2xH9114; PDF retrieval source: https://arxiv.org/pdf/2406.06005. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 1 Introduction - extractive body cue:** In Section 4, we show how our framework, WoCoCo, can be applied to a variety of challenging dynamic tasks with flexible definitions and representations of ...
- **p. 5 / 1 Introduction - extractive body cue:** 4 Case Studies In this section, we show how our framework, WoCoCo, can be applied to various challenging tasks with different contact sequences.
- **p. 3 / 1 Introduction - extractive body cue:** In this paper, we study tasks where contact stages are predefined (e.g., heuristically designed), and our method can seamlessly be integrated with high-level contact planners ...
- **p. 2 / 1 Introduction - extractive body cue:** To better facilitate exploration, we propose a task-agnostic curiosity reward term.
- **p. 4 / 1 Introduction - extractive body cue:** Instead, we propose to use count-based curiosity rewards via random neural network (NN) based hash, inspired by Tang et al.
- **p. 3 / 1 Introduction - extractive body cue:** To develop RL-based controllers for these tasks, we formulate the policy learning problem as an extended Markov Decision Process (MDP) M = ⟨S, A, T ...
- **p. 6 / 1 Introduction - extractive body cue:** Lower Row: We transfer the policy to the real world, testing jumps with double-foot contacts at different heights and a "hug" posture. provided current and ...
- **Contribution anchor:** p. 3 (1 Introduction), p. 5 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 3 (1 Introduction)

### Strongest assumption and failure boundary

- **p. 8 / 1 Introduction - extractive body cue:** 6 Limitation and Future Works One limitation of our work is the lacking knowledge of when the controller will fail.
- **p. 5 / 1 Introduction - extractive body cue:** However, model mismatch and perturbations such as uneven terrains pose significant challenges to these controllers, for which RL can be a promising solution [13, 22].
- **p. 2 / 1 Introduction - extractive body cue:** This drives the robot to explore further stages to maximize cumulative rewards, thus mitigating the shortsightedness caused by the RL policy strategically staying in the ...
- **p. 4 / 1 Introduction - extractive body cue:** Exploring new contact stages can come with failures and penalties, while staying at the current one may bring positive rewards.
- **p. 2 / 1 Introduction - extractive body cue:** This then transforms each challenge to a question: Q1: How to reach desired contact states within each stage?
- **p. 8 / 1 Introduction - extractive body cue:** Therefore, we may explore failure predictors [56] and other safety assessment methods in the future [57].
- **p. 7 / 1 Introduction - extractive body cue:** The contact goal requires foot contact with the ground in their corresponding bounding boxes (predefined in the world frame), plus hand self-collision if the move ...
- **Boundary to test:** 6 Limitation and Future Works One limitation of our work is the lacking knowledge of when the controller will fail.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In Section 4, we show how our framework, WoCoCo, can be applied to a variety of challenging dynamic tasks with flexible definitions and representations of contact and task goals. | p. 3 (1 Introduction), p. 5 (1 Introduction) |
| Reported outcome | Figure 3: Learned whole-body box loco-manipulation behaviors in the real world. Results. As shown in Fig. 3, the humanoid can efficiently turn, transition seamlessly between walking and picking, and simultaneously approach the ... | p. 6 (Figure/Table caption), p. 6 (1 Introduction) |
| Failure/limitation | 6 Limitation and Future Works One limitation of our work is the lacking knowledge of when the controller will fail. | p. 8 (1 Introduction), p. 8 (1 Introduction) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Humanoid activities involving sequential contacts are crucial for complex robotic interactions and operations in the real world and are traditionally solved by model-based motion planning, which is time-consuming and often ... (p. 1, Abstract).
- **Paper-specific mechanism:** In Section 4, we show how our framework, WoCoCo, can be applied to a variety of challenging dynamic tasks with flexible definitions and representations of contact and task goals. (p. 3, 1 Introduction).
- **Evidence boundary:** the reported outcome is Figure 4: Learned dancing motions in simulation and the real-world. Black bounding boxes indicate the foot contact goals and the hand task goals. Reward. There are two task-related rewards, one ... (p. 7, Figure/Table caption); the relevant task/metric cue is There are two task-related reward terms, which incentivize minimizing the distances between the hands and the box, and between the box and its destination. (p. 6, 1 Introduction). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** 6 Limitation and Future Works One limitation of our work is the lacking knowledge of when the controller will fail. (p. 8, 1 Introduction).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, humanoid, whole-body control, sequential contacts, Reinforcement Learning`.
- **Reading predecessor in the generated track queue:** SPIN: Simultaneous Perception, Interaction and Navigation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** end of this track queue (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 6 Limitation and Future Works One limitation of our work is the lacking knowledge of when the controller will fail.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Humanoid activities involving sequential contacts are crucial for complex robotic interactions and operations in the real world and are traditionally solved by model-based motion planning, which is time-consuming and often ... (p. 1, Abstract); preserve the objective/update rule: Provided specific contact plans, the typical solution is to employ model-based motion planning or trajectory optimization to generate whole-body references for tracking [2, 3, 4]. (p. 1, 1 Introduction).
2. Use the paper-reported task/data/environment cue: 3Referred to as "destination" to avoid confusion with contact/task goals. (p. 6, 1 Introduction).
3. Compare against the reported or matched baseline: In comparison, our curiosity rewards achieves effective exploration without overfitting specific behaviors. (p. 8, 1 Introduction).
4. Report the body metric with its denominator and aggregation: There are two task-related reward terms, which incentivize minimizing the distances between the hands and the box, and between the box and its destination. (p. 6, 1 Introduction).
5. Re-run the reported ablation or stress/failure condition: Lower Row: We transfer the policy to the real world, testing jumps with double-foot contacts at different heights and a "hug" posture. provided current and goal positions3 of the box, ... (p. 6, 1 Introduction); if none is reported, design one around: 6 Limitation and Future Works One limitation of our work is the lacking knowledge of when the controller will fail. (p. 8, 1 Introduction).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 3 (1 Introduction), p. 5 (1 Introduction), match the reported outcome at p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), and measure the boundary at p. 8 (1 Introduction), p. 2 (1 Introduction).

## Falsifiable research question

Under the paper's stated interface (Humanoid activities involving sequential contacts are crucial for complex robotic interactions and operations in the real world and are traditionally solved by ...), does the paper-specific mechanism (In Section 4, we show how our framework, WoCoCo, can be applied to a variety of challenging dynamic tasks with flexible definitions ...) retain the reported evaluation outcome (There are two task-related reward terms, which incentivize minimizing the distances between the hands and the box, and ...) when tested against the paper's strongest explicit boundary (6 Limitation and Future Works One limitation of our work is the lacking knowledge of when the controller ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (There are two task-related reward terms, which incentivize minimizing the distances between the hands and the box, and ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In Section 4, we show how our framework, WoCoCo, can be applied to a variety of challenging dynamic tasks with flexible definitions and representations of contact and task goals. (p. 3, 1 Introduction).
- **Paper-supported outcome:** Figure 4: Learned dancing motions in simulation and the real-world. Black bounding boxes indicate the foot contact goals and the hand task goals. Reward. There are two task-related rewards, one ... (p. 7, Figure/Table caption).
- **Strongest explicit boundary:** 6 Limitation and Future Works One limitation of our work is the lacking knowledge of when the controller will fail. (p. 8, 1 Introduction).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
