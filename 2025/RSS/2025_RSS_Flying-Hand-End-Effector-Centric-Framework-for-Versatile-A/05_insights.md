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

- **Paper-specific interface:** [57] proposed a hierarchical framework that consists of the understanding module, a pre~ trained large visual-language model running in low-frequency. and the execution modale, a visual-based action policy running in ... (p. 2, B. Mobile Manipulation Framework and EE-Centric Interface).
- **Paper-specific mechanism:** Our framework consists of a fully-actuated hexarotor with a 4:DoF robotic arm, an end-effector-centrie whole-body: model predictive controller, and a high-level po is end-effector controller enables efficient and ‘operation for ... (p. 1, Abstract).
- **Evidence boundary:** the reported outcome is Root Mean Square Error (RMSE) is used as the tracking performance evaluation criterion. (p. 8, A. Experimental Setup); the relevant task/metric cue is Researchers mostly developed a point-contact arm, such as a rigid rod, and proposed the hybrid motion-force control framework, although achieving high-precision tracking performance, struggled to handle scenarios requiring grasping: 2) ... (p. 2, 4) Rich real-world experiments demonstrated the versatility). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Although we have demonstrated the proposed framework through various real-world experiments, there are still several limitations due to time constraints and methodological limitations. (p. 11, IX. LIMITATIONS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, aerial manipulation, whole-body control, teleoperation, Imitation Learning, assembly`.
- **Reading predecessor in the generated track queue:** HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** SPIN: Simultaneous Perception, Interaction and Navigation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Although we have demonstrated the proposed framework through various real-world experiments, there are still several limitations due to time constraints and methodological limitations.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: [57] proposed a hierarchical framework that consists of the understanding module, a pre~ trained large visual-language model running in low-frequency. and the execution modale, a visual-based action policy running in ... (p. 2, B. Mobile Manipulation Framework and EE-Centric Interface); preserve the objective/update rule: Eq, (10a) defines the optimization objective, where HT represents the discrete prediction horizon. (p. 6, A. End-Effector-Centric Model Predictive Controller).
2. Use the paper-reported task/data/environment cue: In general, although different works have shown success on different specific tasks, the specific system design and algorithm development make the same hardware and algorithm hard to deploy to different ... (p. 2, 4) Rich real-world experiments demonstrated the versatility).
3. Compare against the reported or matched baseline: 1) Trajectory Tracking Task Setup: To show the effectiveness of our proposed method in end-effector trajectory tracking tasks, we perform a comparison between our control methods against two baseline approaches: (p. 7, A. Experimental Setup).
4. Report the body metric with its denominator and aggregation: Researchers mostly developed a point-contact arm, such as a rigid rod, and proposed the hybrid motion-force control framework, although achieving high-precision tracking performance, struggled to handle scenarios requiring grasping: 2) ... (p. 2, 4) Rich real-world experiments demonstrated the versatility).
5. Re-run the reported ablation or stress/failure condition: MPC: This baseline replaces the ee-centric MPC with the Direct Force Feedback Control(DEFC) method from [38]. which directly controls the end-effector acceleration based on the current reference pose. (p. 7, A. Experimental Setup); if none is reported, design one around: Although we have demonstrated the proposed framework through various real-world experiments, there are still several limitations due to time constraints and methodological limitations. (p. 11, IX. LIMITATIONS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (Abstract), p. 7 (VII. EE-CENTRIC TELEOPERATION AND POLICY), match the reported outcome at p. 8 (A. Experimental Setup), p. 8 (B. Implementation Details), p. 10 (B. Implementation Details), and measure the boundary at p. 11 (IX. LIMITATIONS), p. 3 (C. Teleportation and Imitation Learning).

## Falsifiable research question

Under the paper's stated interface ([57] proposed a hierarchical framework that consists of the understanding module, a pre~ trained large visual-language model running in low-frequency. and the ...), does the paper-specific mechanism (Our framework consists of a fully-actuated hexarotor with a 4:DoF robotic arm, an end-effector-centrie whole-body: model predictive controller, and a high-level po ...) retain the reported evaluation outcome (Researchers mostly developed a point-contact arm, such as a rigid rod, and proposed the hybrid motion-force control framework, ...) when tested against the paper's strongest explicit boundary (Although we have demonstrated the proposed framework through various real-world experiments, there are still several limitations due to ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Researchers mostly developed a point-contact arm, such as a rigid rod, and proposed the hybrid motion-force control framework, ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Our framework consists of a fully-actuated hexarotor with a 4:DoF robotic arm, an end-effector-centrie whole-body: model predictive controller, and a high-level po is end-effector controller enables efficient and ‘operation for ... (p. 1, Abstract).
- **Paper-supported outcome:** Root Mean Square Error (RMSE) is used as the tracking performance evaluation criterion. (p. 8, A. Experimental Setup).
- **Strongest explicit boundary:** Although we have demonstrated the proposed framework through various real-world experiments, there are still several limitations due to time constraints and methodological limitations. (p. 11, IX. LIMITATIONS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
