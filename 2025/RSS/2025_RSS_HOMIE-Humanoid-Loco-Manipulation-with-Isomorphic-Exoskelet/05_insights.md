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

- **Closed-loop position:** `proprioception, reference pose/motion, visual or language command → whole-body pose, balance/contact state와 skill/mode → joint/whole-body action, motion target 또는 task trajectory`.
- 이 논문의 재사용 가능한 지점은 1) Training Settings: ‘The observations of one step are defined as O, = [Cry tes dts des de» ei], Where Cy is the command, «is the body's angular velocity, gis the projection ...를 The actions ay of the policy correspond one-to-one with the joints of the robot's lower body.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 whole-body pose, balance/contact state와 skill/mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Thus, our curriculum approach leads to better performance compared to rand, Although w/o cur does not use a curriculum, allowing a; to continuously sample from에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We introduce the training settings and three key techniques of our framework in this section
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, humanoid, loco-manipulation, teleoperation, exoskeleton`.
- **Reading predecessor in the generated track queue:** Demonstrating MOSART: Opening Articulated Structures in the Real World (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Flying Hand: End-Effector-Centric Framework for Versatile Aerial Manipulation Teleoperation and Policy Learning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Thus, our curriculum approach leads to better performance compared to rand, Although w/o cur does not use a curriculum, allowing a; to continuously sample from; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: This migration enables the use of HOMIE to control robots within a variety of simulated environments By leveraging these simulated scenes, the robots can perform diverse loco-manipulation tasks more cost-effectively and in ....
3. Compare against the body-reported baseline or a matched simpler baseline: Compared to the training setting of Unitree Gl. we only ‘change the range of height tracking and some robot-specific distance values, without any other changes in reward scales or training pipeline..
4. Report the body metric and its denominator/aggregation: These results indicate that just scaling up the height tracking reward in hei may initially lead to faster reduction in height tracking error, but it negatively affects the feedback from ‘other rewards, ....
5. Re-run the body-reported ablation/failure condition: environments, where components unrelated to the ablation are kept unchanged, and only relevant parts are modified for training, Detailed parameters used in training and evaluation processes are listed in Appendix A..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 8 (A. Humanoid Whole-body Control), p. 3 (B. Whole-body Loco-Manipulation), p. 2 (Abstract); the primary result is directionally consistent at p. 8 (A. Humanoid Whole-body Control), p. 10 (C. Teleoperation System), p. 7 (C. Hardware System Design); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 introduce, training, settings mechanism이 Compared to the training setting of Unitree Gl. we only ‘change the range of height tracking ... 대비 These results indicate that just scaling up the height tracking reward in hei may initially lead to faster ...을 개선하고, Thus, our curriculum approach leads to better performance compared to rand, Although w/o cur does not ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
