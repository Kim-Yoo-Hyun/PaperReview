# Insights — RoboPack: Learning Tactile-Informed Dynamics Models for Dense Packing

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p130.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p130.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** To tackle these challenges, in this work, we propose to 1) learn dynamics directly from real physical interaction data using powerful deep function approximators, 2) ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We find that our method can successfully leverage histories of visuo-tactile information to improve prediction, with models trained on just 30 minutes of real-world interaction ...
- **p. 4 / III. METHOD - extractive body cue:** For multi-object packing settings with significant occlusion, we introduce an objective that constrains tracked points to be near the corresponding object masks, providing more consistent ...
- **p. 5 / III. METHOD - extractive body cue:** In the following paragraphs, we describe how our method performs state estimation using history information and future prediction.
- **p. 5 / III. METHOD - extractive body cue:** For a training trajectory of length H, the state estimator estimates the first T states, and the dynamics predictor predicts all remaining states.
- **p. 4 / III. METHOD - extractive body cue:** State Estimation and Latent Physics Vector Inference In real-world robotic manipulation, visual observations are not always available due to occlusion, but knowledge about object dynamics ...
- **p. 4 / III. METHOD - extractive body cue:** F x, F y are the mean of local force vectors across spatial dimensions, and /Q/ is defined as /Q/ = r max i,j /qx ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD), p. 4 (III. METHOD)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** At the same time, tasks such as dense packing present significant challenges due to severe occlusions among objects, creating partially observable scenarios where vision alone ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** These tasks involve multi-object interactions with complex dynamics that cannot be determined from vision alone.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To tackle these challenges, in this work, we propose to 1) learn dynamics directly from real physical interaction data using powerful deep function approximators, 2) ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This process is natural for us humans but very challenging for current robotic systems.
- **p. 6 / IV. EXPERIMENTAL SETUP - extractive body cue:** The test objects are more complex than the training set visually, geometrically, and physically, to showcase the generalizability of our model. yet the same visual ...
- **p. 7 / IV. EXPERIMENTAL SETUP - extractive body cue:** Each episode includes various attempts at packing an object into the box and includes pushing and deforming objects, as well as in-hand slipping of the ...
- **p. 8 / V. EXPERIMENTS - extractive body cue:** Metrics such as EMD and CD that emphasize global shape and distribution but are insensitive to subtle positional changes cannot differentiate the two methods in ...
- **Boundary to test:** The test objects are more complex than the training set visually, geometrically, and physically, to showcase the generalizability of our model. yet the same visual appearance; (ii) the robot has little visual ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To tackle these challenges, in this work, we propose to 1) learn dynamics directly from real physical interaction data using powerful deep function approximators, 2) equip our robotic system with a compliant ... | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | Does integrating tactile sensing information from prior interactions improve future prediction accuracy? ii. | p. 7 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS) |
| Failure/limitation | The test objects are more complex than the training set visually, geometrically, and physically, to showcase the generalizability of our model. yet the same visual appearance; (ii) the robot has little visual ... | p. 6 (IV. EXPERIMENTAL SETUP), p. 7 (IV. EXPERIMENTAL SETUP) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** 2) Tactile Perception: As shown in the top right of Figure 2, our tactile perception module takes global force-torque and local force vectors as input and outputs embeddings for the ... (p. 4, III. METHOD).
- **Paper-specific mechanism:** We find that our method can successfully leverage histories of visuo-tactile information to improve prediction, with models trained on just 30 minutes of real-world interaction data per task on average. (p. 2, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is 2.65 ± 0.18 4.11 ± 0.17 4.57 ± 0.16 Dense RoboPack 0.070 ± 0.005 1.12 ± 0.036 2.01 ± 0.050 Packing RoboPack (no tactile) 0.088 ± 0.006 1.18 ± 0.043 ... (p. 8, V. EXPERIMENTS); the relevant task/metric cue is We use a cost function that (i) penalizes the objects in the box from being pushed out of the boundary, (ii) encourages the robot to make space for placing the ... (p. 7, IV. EXPERIMENTAL SETUP). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Due to heavy occlusions during task execution, the robot does not have access to meaningful visual feedback during robot execution other than the initial frame, but again tactile signals are ... (p. 6, IV. EXPERIMENTAL SETUP).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, contact-rich manipulation, tactile sensing, dynamics model`.
- **Reading predecessor in the generated track queue:** Tactile-Driven Non-Prehensile Object Manipulation via Extrinsic Contact Mode Control (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** DexTrack: Towards Generalizable Neural Tracking Control for Dexterous Manipulation from Human References (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The test objects are more complex than the training set visually, geometrically, and physically, to showcase the generalizability of our model. yet the same visual appearance; (ii) the robot has little visual ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: 2) Tactile Perception: As shown in the top right of Figure 2, our tactile perception module takes global force-torque and local force vectors as input and outputs embeddings for the ... (p. 4, III. METHOD); preserve the objective/update rule: We optimize a translation and rotation transformation for each object with this objective. (p. 4, III. METHOD).
2. Use the paper-reported task/data/environment cue: Benchmarking Real-World Planning Performance Next, we evaluate the performance of our approach in solving real-world robotic planning tasks. (p. 9, V. EXPERIMENTS).
3. Compare against the reported or matched baseline: Our method closely approximates the ground truth and outperforms all the baseline methods. (p. 8, V. EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: We use a cost function that (i) penalizes the objects in the box from being pushed out of the boundary, (ii) encourages the robot to make space for placing the ... (p. 7, IV. EXPERIMENTAL SETUP).
5. Re-run the reported ablation or stress/failure condition: RoboPack (no tactile): To study the effects of using tactile sensing in state estimation and dynamics prediction, we evaluate this ablation of our method, which zeroes out tactile input to ... (p. 7, V. EXPERIMENTS); if none is reported, design one around: Due to heavy occlusions during task execution, the robot does not have access to meaningful visual feedback during robot execution other than the initial frame, but again tactile signals are ... (p. 6, IV. EXPERIMENTAL SETUP).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), match the reported outcome at p. 8 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), and measure the boundary at p. 6 (IV. EXPERIMENTAL SETUP), p. 8 (V. EXPERIMENTS).

## Falsifiable research question

Under the paper's stated interface (2) Tactile Perception: As shown in the top right of Figure 2, our tactile perception module takes global force-torque and local force ...), does the paper-specific mechanism (We find that our method can successfully leverage histories of visuo-tactile information to improve prediction, with models trained on just 30 minutes ...) retain the reported evaluation outcome (We use a cost function that (i) penalizes the objects in the box from being pushed out of ...) when tested against the paper's strongest explicit boundary (Due to heavy occlusions during task execution, the robot does not have access to meaningful visual feedback during ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (We use a cost function that (i) penalizes the objects in the box from being pushed out of ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** We find that our method can successfully leverage histories of visuo-tactile information to improve prediction, with models trained on just 30 minutes of real-world interaction data per task on average. (p. 2, I. INTRODUCTION).
- **Paper-supported outcome:** 2.65 ± 0.18 4.11 ± 0.17 4.57 ± 0.16 Dense RoboPack 0.070 ± 0.005 1.12 ± 0.036 2.01 ± 0.050 Packing RoboPack (no tactile) 0.088 ± 0.006 1.18 ± 0.043 ... (p. 8, V. EXPERIMENTS).
- **Strongest explicit boundary:** Due to heavy occlusions during task execution, the robot does not have access to meaningful visual feedback during robot execution other than the initial frame, but again tactile signals are ... (p. 6, IV. EXPERIMENTAL SETUP).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
