# Insights — HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (21 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p070.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p070.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 4 / B. Humanoid Whole-body Control - extractive body cue:** We introduce the training settings and three key techniques of our framework in this section
- **p. 2 / Abstract - extractive body cue:** Unlike previous whole-body contro! methods that depend on motion priors derived from MoCap data [12], our framework eliminates this dependency, resulting in a more cfficient ...
- **p. 2 / Abstract - extractive body cue:** In responce, we introduce HOMIE, a semi-autonomous humanoid teleoperation system that integrates a RL policy for body control mapped to a pedal, an isomorphic exoskeleton ...
- **p. 4 / A. System Overview - extractive body cue:** 2, HOMIE consists of low-level policy Toco and an exoskeleton-based hardware system.
- **p. 3 / A. Teleoperation Systems - extractive body cue:** HOMIE is designed to combine all the advantages mentioned above, integrating isomorphic exoskeleton arms with a pair of novel motionsensing gloves.
- **p. 8 / A. Humanoid Whole-body Control - extractive body cue:** Symmetry Utilization, We introduce three algorithmic variants for comparison with ours in terms of symmetry ut tion: w/ aug, which uses only symmetrical data augmentation; ...
- **p. 3 / B. Whole-body Loco-Manipulation - extractive body cue:** Reinforcement Learning (RL)-based algorithms, especially those based on Proximal Policy Optimization (PPO) [32], offer a more powerful altemative.
- **Contribution anchor:** p. 4 (B. Humanoid Whole-body Control), p. 2 (Abstract), p. 2 (Abstract), p. 4 (A. System Overview), p. 3 (A. Teleoperation Systems), p. 8 (A. Humanoid Whole-body Control)

### Strongest assumption and failure boundary

- **p. 2 / A. Teleoperation Systems - extractive body cue:** However, due to limitations in the accuracy, inference speed, and difficulty in handling occlusions of pose estimation, such approaches cannot guarantee rapid and accurate pose ...
- **p. 1 / Abstract - extractive body cue:** However, the field currently faces a significant
- **p. 1 / Abstract - extractive body cue:** Generalizable humanoid loco-manipulation poses significant challenges, requiring coordinated whole-body control and precise, contact
- **p. 2 / Abstract - extractive body cue:** dichotomy: reinforcement learning (RL)-trained locomotion policies excel at environmental adaptation but lack the interfaces needed for real-time, precise teleoperation [1, 2, 3, 4, 5, 6].
- **p. 3 / B. Whole-body Loco-Manipulation - extractive body cue:** Despite achieving impressive results, these methods still face several common limitations.
- **p. 7 / A. Humanoid Whole-body Control - extractive body cue:** Thus, our curriculum approach leads to better performance compared to rand, Although w/o cur does not use a curriculum, allowing a; to continuously sample from
- **p. 8 / A. Humanoid Whole-body Control - extractive body cue:** We design two additional algorithms w/o knee, which does not USE rinee described in Eq.
- **Boundary to test:** Thus, our curriculum approach leads to better performance compared to rand, Although w/o cur does not use a curriculum, allowing a; to continuously sample from

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We introduce the training settings and three key techniques of our framework in this section | p. 4 (B. Humanoid Whole-body Control), p. 2 (Abstract) |
| Reported outcome | In summary, symmetry data augmentation significantly improves training efficiency, while the use of symmetry loss effectively prevents the policy from sacrificing symmetry to complete tasks and also benefits the task itself. | p. 8 (A. Humanoid Whole-body Control), p. 10 (C. Teleoperation System) |
| Failure/limitation | Thus, our curriculum approach leads to better performance compared to rand, Although w/o cur does not use a curriculum, allowing a; to continuously sample from | p. 7 (A. Humanoid Whole-body Control), p. 8 (A. Humanoid Whole-body Control) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** 1) Training Settings: ‘The observations of one step are defined as O, = [Cry tes dts des de» ei], Where Cy is the command, «is the body's angular velocity, gis ... (p. 4, B. Humanoid Whole-body Control).
- **Paper-specific mechanism:** HOMIE is designed to combine all the advantages mentioned above, integrating isomorphic exoskeleton arms with a pair of novel motionsensing gloves. (p. 3, A. Teleoperation Systems).
- **Evidence boundary:** the reported outcome is These results indicate that just scaling up the height tracking reward in hei may initially lead to faster reduction in height tracking error, but it negatively affects the feedback from ... (p. 8, A. Humanoid Whole-body Control); the relevant task/metric cue is Except for symmetry loss, the performance of ours and w/ aug is similar, However, when considering overall tracking accuracy, ours performs slightly better. (p. 8, A. Humanoid Whole-body Control). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** However, due to limitations in the accuracy, inference speed, and difficulty in handling occlusions of pose estimation, such approaches cannot guarantee rapid and accurate pose acquisition. (p. 2, A. Teleoperation Systems).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, humanoid, loco-manipulation, teleoperation, exoskeleton`.
- **Reading predecessor in the generated track queue:** Demonstrating MOSART: Opening Articulated Structures in the Real World (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Flying Hand: End-Effector-Centric Framework for Versatile Aerial Manipulation Teleoperation and Policy Learning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Thus, our curriculum approach leads to better performance compared to rand, Although w/o cur does not use a curriculum, allowing a; to continuously sample from; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: 1) Training Settings: ‘The observations of one step are defined as O, = [Cry tes dts des de» ei], Where Cy is the command, «is the body's angular velocity, gis ... (p. 4, B. Humanoid Whole-body Control); preserve the objective/update rule: These two losses are added to the network optimization process, thereby enforcing symmetry of the neural network. (p. 5, 1 2001p).
2. Use the paper-reported task/data/environment cue: We capture RGB images, robot states q, the upper body commands quypers and the locomotion commands Cy at 10Hz, and collect 50 episodes per task. (p. 10, 20 Bet).
3. Compare against the reported or matched baseline: Compared to the training setting of Unitree Gl. we only ‘change the range of height tracking and some robot-specific distance values, without any other changes in reward scales or training ... (p. 8, A. Humanoid Whole-body Control).
4. Report the body metric with its denominator and aggregation: Except for symmetry loss, the performance of ours and w/ aug is similar, However, when considering overall tracking accuracy, ours performs slightly better. (p. 8, A. Humanoid Whole-body Control).
5. Re-run the reported ablation or stress/failure condition: 7: Ablation experiments of our RL training framework. (p. 7, C. Hardware System Design); if none is reported, design one around: However, due to limitations in the accuracy, inference speed, and difficulty in handling occlusions of pose estimation, such approaches cannot guarantee rapid and accurate pose acquisition. (p. 2, A. Teleoperation Systems).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 3 (A. Teleoperation Systems), p. 4 (B. Humanoid Whole-body Control), match the reported outcome at p. 8 (A. Humanoid Whole-body Control), p. 10 (C. Teleoperation System), p. 7 (Figure/Table caption), and measure the boundary at p. 2 (A. Teleoperation Systems), p. 11 (V. CONCLUSION AND LIMITATIONS).

## Falsifiable research question

Under the paper's stated interface (1) Training Settings: ‘The observations of one step are defined as O, = [Cry tes dts des de» ei], Where Cy is ...), does the paper-specific mechanism (HOMIE is designed to combine all the advantages mentioned above, integrating isomorphic exoskeleton arms with a pair of novel motionsensing gloves.) retain the reported evaluation outcome (Except for symmetry loss, the performance of ours and w/ aug is similar, However, when considering overall tracking ...) when tested against the paper's strongest explicit boundary (However, due to limitations in the accuracy, inference speed, and difficulty in handling occlusions of pose estimation, such ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Except for symmetry loss, the performance of ours and w/ aug is similar, However, when considering overall tracking ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (21 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** HOMIE is designed to combine all the advantages mentioned above, integrating isomorphic exoskeleton arms with a pair of novel motionsensing gloves. (p. 3, A. Teleoperation Systems).
- **Paper-supported outcome:** These results indicate that just scaling up the height tracking reward in hei may initially lead to faster reduction in height tracking error, but it negatively affects the feedback from ... (p. 8, A. Humanoid Whole-body Control).
- **Strongest explicit boundary:** However, due to limitations in the accuracy, inference speed, and difficulty in handling occlusions of pose estimation, such approaches cannot guarantee rapid and accurate pose acquisition. (p. 2, A. Teleoperation Systems).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
