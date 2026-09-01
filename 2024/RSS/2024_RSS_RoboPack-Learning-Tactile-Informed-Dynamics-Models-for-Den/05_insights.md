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

- **Closed-loop position:** `tactile image/force, vision과 proprioceptive history → contact geometry, force state 또는 latent dynamics → grasp/contact action, force command 또는 object motion`.
- 이 논문의 재사용 가능한 지점은 To formulate this problem, we define the observation space as O, the state space as S, and the action space as A.를 Secondly, the state estimator g infers object states s from any prior interactions, which includes a single visual frame ovis 0 , the subsequent tactile observations otact 0:t , and the corresponding ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 contact geometry, force state 또는 latent dynamics가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 The test objects are more complex than the training set visually, geometrically, and physically, to showcase the generalizability of our model. yet the same visual appearance; (ii) the robot has little visual ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To tackle these challenges, in this work, we propose to 1) learn dynamics directly from real physical interaction data using powerful deep function approximators, 2) equip our robotic system with a compliant ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, contact-rich manipulation, tactile sensing, dynamics model`.
- **Reading predecessor in the generated track queue:** Tactile-Driven Non-Prehensile Object Manipulation via Extrinsic Contact Mode Control (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** DexTrack: Towards Generalizable Neural Tracking Control for Dexterous Manipulation from Human References (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The test objects are more complex than the training set visually, geometrically, and physically, to showcase the generalizability of our model. yet the same visual appearance; (ii) the robot has little visual ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Benchmarking Real-World Planning Performance Next, we evaluate the performance of our approach in solving real-world robotic planning tasks..
3. Compare against the body-reported baseline or a matched simpler baseline: Fig. 6: Qualitative results on dynamics prediction. Pre- dictions made by our model compared to baseline methods in the Non-prehensile Box Pushing task. Red dots indicate the rod and blue dots represent ....
4. Report the body metric and its denominator/aggregation: We report the minimum error to goal across 10 plan executions per trial, trial success rates, and number of execution steps to solve the task..
5. Re-run the body-reported ablation/failure condition: RoboPack (no tactile): To study the effects of using tactile sensing in state estimation and dynamics prediction, we evaluate this ablation of our method, which zeroes out tactile input to the model. ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD); the primary result is directionally consistent at p. 7 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 tackle, challenges, learn mechanism이 Fig. 6: Qualitative results on dynamics prediction. Pre- dictions made by our model compared to baseline ... 대비 We report the minimum error to goal across 10 plan executions per trial, trial success rates, and number ...을 개선하고, The test objects are more complex than the training set visually, geometrically, and physically, to showcase ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
