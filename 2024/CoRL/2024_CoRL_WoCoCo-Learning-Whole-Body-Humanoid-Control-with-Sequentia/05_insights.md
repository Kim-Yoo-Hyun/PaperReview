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

- **Closed-loop position:** `proprioception, reference pose/motion, visual or language command → whole-body pose, balance/contact state와 skill/mode → joint/whole-body action, motion target 또는 task trajectory`.
- 이 논문의 재사용 가능한 지점은 [28, 40], we stack 3 control steps of previous joint states and actions, and append them to the policy observations to enhance the robustness by temporal memory.를 To develop RL-based controllers for these tasks, we formulate the policy learning problem as an extended Markov Decision Process (MDP) M = ⟨S, A, T , R, γ, Gcon, Gtask⟩of state st ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 whole-body pose, balance/contact state와 skill/mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 6 Limitation and Future Works One limitation of our work is the lacking knowledge of when the controller will fail.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In Section 4, we show how our framework, WoCoCo, can be applied to a variety of challenging dynamic tasks with flexible definitions and representations of contact and task goals.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, humanoid, whole-body control, sequential contacts, Reinforcement Learning`.
- **Reading predecessor in the generated track queue:** SPIN: Simultaneous Perception, Interaction and Navigation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** end of this track queue (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 6 Limitation and Future Works One limitation of our work is the lacking knowledge of when the controller will fail.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Left Middle Right Figure 4: Learned dancing motions in simulation and the real-world..
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 6: We train the dinosaur robot to push the ball towards destinations with different end effec- tors. By altering the destinations, we make the robot generate ball trajectories forming "WoCoCo". 5 ....
4. Report the body metric and its denominator/aggregation: Figure 4: Learned dancing motions in simulation and the real-world. Black bounding boxes indicate the foot contact goals and the hand task goals. Reward. There are two task-related rewards, one encourageing spreading ....
5. Re-run the body-reported ablation/failure condition: In comparison, our curiosity rewards achieves effective exploration without overfitting specific behaviors..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (1 Introduction), p. 6 (1 Introduction), p. 1 (1 Introduction); the primary result is directionally consistent at p. 6 (Figure/Table caption), p. 6 (1 Introduction), p. 8 (1 Introduction); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Section, framework, WoCoCo mechanism이 Figure 6: We train the dinosaur robot to push the ball towards destinations with different end ... 대비 Figure 4: Learned dancing motions in simulation and the real-world. Black bounding boxes indicate the foot contact goals ...을 개선하고, 6 Limitation and Future Works One limitation of our work is the lacking knowledge of when ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
