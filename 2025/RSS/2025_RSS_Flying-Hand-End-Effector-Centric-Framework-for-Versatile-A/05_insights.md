# Insights — Flying Hand: End-Effector-Centric Framework for Versatile Aerial Manipulation Teleoperation and Policy Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p130.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p130.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / Abstract - extractive body cue:** Our framework consists of a fully-actuated hexarotor with a 4:DoF robotic arm, an end-effector-centrie whole-body: model predictive controller, and a high-level po is end-effector controller ...
- **p. 7 / VII. EE-CENTRIC TELEOPERATION AND POLICY - extractive body cue:** [As we mentioned, our framework enables the decoupling between the high-level policy and low-level controller, with the ee-centric interface serving asthe sole connection between them.
- **p. 2 / B. Mobile Manipulation Framework and EE-Centric Interface - extractive body cue:** [25] proposed a framework that consists of a robust humanoid whole-body controller with a high-level policy, either an autonomous agent like GPT-40 or an imitation ...
- **p. 7 / VII. EE-CENTRIC TELEOPERATION AND POLICY - extractive body cue:** In this section, we introduce two aerial manipulation systems we ‘developed based on this framework: the ee-centrc aerial tele- ‘operation system and the imitaton-Iearning-based autonomous ...
- **p. 2 / 1. Iyrropuction - extractive body cue:** By effectively decoupling high-level policies from low-level control, it enables the development ‘of embodiment-agnostic policies 47}, {10}.
- **p. 7 / B. EE-Centrie Policy Learning - extractive body cue:** The transformerbased decoder generates action sequences from the latent variable (only during training and set to be the mean of the prior during testing), current ...
- **p. 10 / B. Implementation Details - extractive body cue:** ‘To show the advantage of leaming from an ee-centric demonstration compared to a joint space demonstration, we use the same demonstration trajectory but change the ...
- **Contribution anchor:** p. 1 (Abstract), p. 7 (VII. EE-CENTRIC TELEOPERATION AND POLICY), p. 2 (B. Mobile Manipulation Framework and EE-Centric Interface), p. 7 (VII. EE-CENTRIC TELEOPERATION AND POLICY), p. 2 (1. Iyrropuction), p. 7 (B. EE-Centrie Policy Learning)

### Strongest assumption and failure boundary

- **p. 1 / 1. Iyrropuction - extractive body cue:** However, most previous works have been tailored to specific tasks, developing unique platforms and algorithms accordingly, lacking the ability to handle different types of tasks, ...
- **p. 3 / C. Teleportation and Imitation Learning - extractive body cue:** However, there is no precedent to incorporate such IL-based policy into aerial manipulation fields due to the lack of a mature demonstration collection system, such ...
- **p. 2 / 1. Iyrropuction - extractive body cue:** Although the end-effector-centric paradigm has shown the advantage of versatility in the manipulation field, applying it to aerial manipulation systems presents significant challenges due to ...
- **p. 3 / C. Teleportation and Imitation Learning - extractive body cue:** their method is highly coupled with the specific UAM design, and the system struggles with versatile tasks due t0 the workspace limitation.
- **p. 2 / 1. Iyrropuction - extractive body cue:** We believe the proposed framework provides a step toward standardizing and unifying aerial manipulation into the broader manipulation ‘community, advancing the field toward greater versatility ...
- **p. 11 / IX. LIMITATIONS - extractive body cue:** Although we have demonstrated the proposed framework through various real-world experiments, there are still several limitations due to time constraints and methodological limitations.
- **p. 11 / IX. LIMITATIONS - extractive body cue:** Incorporating onboard perception to detect obstacles and generate safety constraints in real-time will be our next step, as various studies have demonstrated the feasibility of ...
- **Boundary to test:** Although we have demonstrated the proposed framework through various real-world experiments, there are still several limitations due to time constraints and methodological limitations.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our framework consists of a fully-actuated hexarotor with a 4:DoF robotic arm, an end-effector-centrie whole-body: model predictive controller, and a high-level po is end-effector controller enables efficient and ‘operation for versatil ... | p. 1 (Abstract), p. 7 (VII. EE-CENTRIC TELEOPERATION AND POLICY) |
| Reported outcome | improvements can be achieved through more accurate system modeling and higher-precision hardware to enhance tracking accuracy. | p. 9 (B. Implementation Details), p. 10 (B. Implementation Details) |
| Failure/limitation | Although we have demonstrated the proposed framework through various real-world experiments, there are still several limitations due to time constraints and methodological limitations. | p. 11 (IX. LIMITATIONS), p. 11 (IX. LIMITATIONS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, reference pose/motion, visual or language command → whole-body pose, balance/contact state와 skill/mode → joint/whole-body action, motion target 또는 task trajectory`.
- 이 논문의 재사용 가능한 지점은 After that, we train a joint space ACT policy with the same training setting as the ee-centric ACT policy, except that the end-effector pose in the observation and action space is replaced ...를 At the most highlevel, the ee-centric policy module gets current observations and generates the target end-effector states online without the need to consider the specific platform jointly.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 whole-body pose, balance/contact state와 skill/mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Although we have demonstrated the proposed framework through various real-world experiments, there are still several limitations due to time constraints and methodological limitations.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our framework consists of a fully-actuated hexarotor with a 4:DoF robotic arm, an end-effector-centrie whole-body: model predictive controller, and a high-level po is end-effector controller enables efficient and ‘operation for versatil ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, aerial manipulation, whole-body control, teleoperation, Imitation Learning, assembly`.
- **Reading predecessor in the generated track queue:** HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** SPIN: Simultaneous Perception, Interaction and Navigation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Although we have demonstrated the proposed framework through various real-world experiments, there are still several limitations due to time constraints and methodological limitations.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Some work also showed amazing results, achieving high-speed grasping, or grasping moving objects [50], but sacrificed payload capacity or precision due to specialized hardware designs..
3. Compare against the body-reported baseline or a matched simpler baseline: 4, compared with our method (blue), the baseline wo..
4. Report the body metric and its denominator/aggregation: + Geometric Precision Advantage: Our ee-centric policy achieves 2.5% higher success rate in geometrically sensitive peg in hole task, directly benefiting from task-space supervision that eliminates the accumulated end-effector error fro ....
5. Re-run the body-reported ablation/failure condition: MPC: This baseline replaces the ee-centric MPC with the Direct Force Feedback Control(DEFC) method from [38]. which directly controls the end-effector acceleration based on the current reference pose..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 7 (B. EE-Centrie Policy Learning), p. 10 (B. Implementation Details), p. 7 (B. EE-Centrie Policy Learning); the primary result is directionally consistent at p. 9 (B. Implementation Details), p. 10 (B. Implementation Details), p. 10 (B. Implementation Details); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 framework, consists, fully-actuated mechanism이 4, compared with our method (blue), the baseline wo. 대비 + Geometric Precision Advantage: Our ee-centric policy achieves 2.5% higher success rate in geometrically sensitive peg in hole ...을 개선하고, Although we have demonstrated the proposed framework through various real-world experiments, there are still several limitations ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
