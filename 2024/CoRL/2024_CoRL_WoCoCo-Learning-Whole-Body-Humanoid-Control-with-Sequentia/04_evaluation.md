# Evaluation - WoCoCo: Learning Whole-Body Humanoid Control with Sequential Contacts

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=Czs2xH9114; PDF retrieval source: https://arxiv.org/pdf/2406.06005. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (Figure/Table caption), p. 6 (1 Introduction), p. 8 (1 Introduction), p. 7 (Figure/Table caption), p. 7 (1 Introduction)): Figure 3: Learned whole-body box loco-manipulation behaviors in the real world. Results. As shown in Fig. 3, the humanoid can efficiently turn, transition seamlessly between walking and picking, and simultaneously ...

## Evaluation Body Digest

- **p. 7 / 1 Introduction - extractive body cue:** Left Middle Right Figure 4: Learned dancing motions in simulation and the real-world.
- **p. 7 / 1 Introduction - extractive body cue:** Each end effector's goal region is bounded by a 2-d square. push recover direction Figure 5: Learned cliffside climbing behavior in simulation and the real-world.
- **p. 8 / 1 Introduction - extractive body cue:** By altering the destinations, we make the robot generate ball trajectories forming "WoCoCo".
- **p. 8 / 1 Introduction - extractive body cue:** Besides, if the contact sequence length is unknown a priori, we may need heuristic reward clamping to avoid the robot exploiting the stage count reward.
- **p. 6 / 1 Introduction - extractive body cue:** 3Referred to as "destination" to avoid confusion with contact/task goals.
- **p. 6 / 1 Introduction - extractive body cue:** BD has achieved impressive dancing with model-based control and offline trajectory optimization [50].
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Learned dancing motions in simulation and the real-world. Black bounding boxes indicate the foot contact goals and the hand task goals. Reward. There ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: An overview of WoCoCo and tasks. (A) We decompose the task into separate contact stages, where each contact stage is defined by the ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 3: Learned whole-body box loco-manipulation behaviors in the real world. Results. As shown in Fig. 3, the humanoid can efficiently turn, transition seamlessly ... | p. 6 (Figure/Table caption) |
| 1 Introduction | EMPIRICAL / REAL-ROBOT OR HARDWARE | By defining the contact sequence solely on the hands, we leverage RL to achieve robust locomotion while simplifying the whole task. | p. 6 (1 Introduction) |
| 1 Introduction | EMPIRICAL / REAL-ROBOT OR HARDWARE | In comparison, our curiosity rewards achieves effective exploration without overfitting specific behaviors. | p. 8 (1 Introduction) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4: Learned dancing motions in simulation and the real-world. Black bounding boxes indicate the foot contact goals and the hand task goals. Reward. ... | p. 7 (Figure/Table caption) |
| 1 Introduction | EMPIRICAL / REAL-ROBOT OR HARDWARE | Though model-based controllers [9, 52, 53, 54] have showcased success in such problems, we prove RL is also a promising solution for fast and ... | p. 7 (1 Introduction) |

## Dataset / Benchmark Role

- **p. 7 / 1 Introduction - extractive body cue:** Left Middle Right Figure 4: Learned dancing motions in simulation and the real-world.
- **p. 7 / 1 Introduction - extractive body cue:** Each end effector's goal region is bounded by a 2-d square. push recover direction Figure 5: Learned cliffside climbing behavior in simulation and the real-world.
- **p. 8 / 1 Introduction - extractive body cue:** By altering the destinations, we make the robot generate ball trajectories forming "WoCoCo".
- **p. 8 / 1 Introduction - extractive body cue:** Besides, if the contact sequence length is unknown a priori, we may need heuristic reward clamping to avoid the robot exploiting the stage count reward.
- **p. 6 / 1 Introduction - extractive body cue:** 3Referred to as "destination" to avoid confusion with contact/task goals.
- **p. 6 / 1 Introduction - extractive body cue:** BD has achieved impressive dancing with model-based control and offline trajectory optimization [50].

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: An overview of WoCoCo and tasks. (A) We decompose the task into separate contact stages, where each contact stage is defined by the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2: Learned versatile jumping motions in simulation and the real world. Upper Row: The humanoid performs continuous jumps with varying foot contact sequences and ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Learned whole-body box loco-manipulation behaviors in the real world. Results. As shown in Fig. 3, the humanoid can efficiently turn, transition seamlessly between ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Learned dancing motions in simulation and the real-world. Black bounding boxes indicate the foot contact goals and the hand task goals. Reward. There ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Learned cliffside climbing behavior in simulation and the real-world. The humanoid exhibited resilience against perturbations and compliance during contact with unseen gravels. Reward. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: We train the dinosaur robot to push the ball towards destinations with different end effec- tors. By altering the destinations, we make the ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Left Middle Right Figure 4: Learned dancing motions in simulation and the real-world. | embodiment, simulator version and control stack | p. 7 (1 Introduction), p. 7 (1 Introduction) |
| Task/environment | Each end effector's goal region is bounded by a 2-d square. push recover direction Figure 5: Learned cliffside climbing behavior in simulation and the ... | reset, timeout, object/scene variation | p. 7 (1 Introduction), p. 8 (1 Introduction) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 5 (1 Introduction), p. 3 (1 Introduction) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 3 (1 Introduction), p. 8 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 4: Learned dancing motions in simulation and the real-world. Black bounding boxes indicate the foot contact goals and the hand task goals. Reward. ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 1: An overview of WoCoCo and tasks. (A) We decompose the task into separate contact stages, where each contact stage is defined by ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| There are two task-related reward terms, which incentivize minimizing the distances between the hands and the box, and between the box and its destination. | definition/direction/unit from same section | p. 6 (1 Introduction) |
| Figure 5: Learned cliffside climbing behavior in simulation and the real-world. The humanoid exhibited resilience against perturbations and compliance during contact with unseen gravels. ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 6: We train the dinosaur robot to push the ball towards destinations with different end effec- tors. By altering the destinations, we make ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| This proves the necessity of our dense contact rewards. | definition/direction/unit from same section | p. 8 (1 Introduction) |
| It can also recover after stepping on a belt tied to itself, showcasing robustness. | definition/direction/unit from same section | p. 6 (1 Introduction) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 6: We train the dinosaur robot to push the ball towards destinations with different end effec- tors. By altering the destinations, we make ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| [36]: the agent may over-explore a dangerous behavior pattern while staying alive, as such states are rare in the agent's experience compared to safer ... | comparison identity and matched condition | p. 8 (1 Introduction) |
| Lower Row: We transfer the policy to the real world, testing jumps with double-foot contacts at different heights and a "hug" posture. provided current ... | comparison identity and matched condition | p. 6 (1 Introduction) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In comparison, our curiosity rewards achieves effective exploration without overfitting specific behaviors. | component/input/data sensitivity | p. 8 (1 Introduction) |
| Lower Row: We transfer the policy to the real world, testing jumps with double-foot contacts at different heights and a "hug" posture. provided current ... | component/input/data sensitivity | p. 6 (1 Introduction) |
| Figure 5: Learned cliffside climbing behavior in simulation and the real-world. The humanoid exhibited resilience against perturbations and compliance during contact with unseen gravels. ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| With 0-1 contact rewards r0-1 con = c0-1FconFtask, the humanoid cannot explore to jump over the stones, and tracks upper body postures without moving. | component/input/data sensitivity | p. 8 (1 Introduction) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In Section 4, we show how our framework, WoCoCo, can be applied to a variety of challenging dynamic tasks with flexible definitions and representations ... | Figure 3: Learned whole-body box loco-manipulation behaviors in the real world. Results. As shown in Fig. 3, the humanoid can efficiently turn, transition seamlessly ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (Figure/Table caption), p. 6 (1 Introduction), p. 8 (1 Introduction), p. 7 (Figure/Table caption), p. 7 (1 Introduction) |
| Primary metric/result | By defining the contact sequence solely on the hands, we leverage RL to achieve robust locomotion while simplifying the whole task. | numeric claim only at cited anchor | p. 6 (1 Introduction) |

- Numeric sentences retained from the body:
- **p. 6 / 1 Introduction - extractive body cue:** Efficient Turning in 0.5 s Efficient and Natural Walking-Picking Transition Simultaneous Box-Picking and Destination-Approaching Recovery after Step on Tied Belt Figure 3: Learned whole-body box ...
- **p. 6 / 1 Introduction - extractive body cue:** Efficient Turning in 0.5 s Efficient and Natural Walking-Picking Transition Simultaneous Box-Picking and Destination-Approaching Recovery after Step on Tied Belt Figure 3: Learned whole-body box ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 6 Limitation and Future Works One limitation of our work is the lacking knowledge of when the controller will fail. | p. 8 (1 Introduction) |
| body limitation/failure cue | Therefore, we may explore failure predictors [56] and other safety assessment methods in the future [57]. | p. 8 (1 Introduction) |
| body limitation/failure cue | The contact goal requires foot contact with the ground in their corresponding bounding boxes (predefined in the world frame), plus hand self-collision if the ... | p. 7 (1 Introduction) |
| body limitation/failure cue | [44] use RL to learn double-foot jumping in the 3D space, yet their method does not support continuous jumps, relies on a motion reference, ... | p. 5 (1 Introduction) |
| body limitation/failure cue | 2, demonstrating the humanoid's capability to perform versatile continuous jumping while tracking upper body postures, and robustness against perturbations such as unseen gravels. | p. 5 (1 Introduction) |
| body limitation/failure cue | It can also recover after stepping on a belt tied to itself, showcasing robustness. | p. 6 (1 Introduction) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| [28, 40], we stack 3 control steps of previous joint states and actions, and append them to the policy observations to enhance the robustness ... | p. 5 (1 Introduction) |
| 10 in Appendix C where we plot the learning curves for five different random seeds. | p. 8 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 1 Introduction - extractive body cue:** 6 Limitation and Future Works One limitation of our work is the lacking knowledge of when the controller will fail.
- **p. 8 / 1 Introduction - extractive body cue:** Therefore, we may explore failure predictors [56] and other safety assessment methods in the future [57].
- **p. 7 / 1 Introduction - extractive body cue:** The contact goal requires foot contact with the ground in their corresponding bounding boxes (predefined in the world frame), plus hand self-collision if the move ...
- **p. 5 / 1 Introduction - extractive body cue:** [44] use RL to learn double-foot jumping in the 3D space, yet their method does not support continuous jumps, relies on a motion reference, and ...
- **p. 5 / 1 Introduction - extractive body cue:** 2, demonstrating the humanoid's capability to perform versatile continuous jumping while tracking upper body postures, and robustness against perturbations such as unseen gravels.
- **p. 6 / 1 Introduction - extractive body cue:** It can also recover after stepping on a belt tied to itself, showcasing robustness.

- **Evidence anchors reviewed:** datasets p. 7 (1 Introduction), p. 7 (1 Introduction), p. 8 (1 Introduction), p. 8 (1 Introduction), p. 6 (1 Introduction), p. 6 (1 Introduction), metrics p. 7 (Figure/Table caption), p. 2 (Figure/Table caption), p. 6 (1 Introduction), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (1 Introduction), baselines p. 8 (Figure/Table caption), p. 8 (1 Introduction), p. 6 (1 Introduction), results p. 6 (Figure/Table caption), p. 6 (1 Introduction), p. 8 (1 Introduction), p. 7 (Figure/Table caption), p. 7 (1 Introduction).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 4: Learned dancing motions in simulation and the real-world. Black bounding boxes indicate the foot contact goals and the hand task goals. Reward. There are two task-related rewards, one ... (p. 7, Figure/Table caption).
- **Metric evidence:** There are two task-related reward terms, which incentivize minimizing the distances between the hands and the box, and between the box and its destination. (p. 6, 1 Introduction).
- **Baseline/ablation evidence:** In comparison, our curiosity rewards achieves effective exploration without overfitting specific behaviors. (p. 8, 1 Introduction).
- **Failure/negative evidence:** 6 Limitation and Future Works One limitation of our work is the lacking knowledge of when the controller will fail. (p. 8, 1 Introduction).
