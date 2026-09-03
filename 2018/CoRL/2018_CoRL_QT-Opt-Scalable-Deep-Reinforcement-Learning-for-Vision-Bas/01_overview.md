# QT-Opt: Scalable Deep Reinforcement Learning for Vision-Based Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1806.10293.
> PDF retrieval source: https://arxiv.org/pdf/1806.10293. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2018 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, Reinforcement Learning, Q-learning, manipulation
- Official paper: https://arxiv.org/abs/1806.10293
- Full-text retrieval: https://arxiv.org/pdf/1806.10293
- Code/Project: https://ai.googleblog.com/2018/06/scalable-deep-reinforcement-learning.html
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 However, a major challenge with closed-loop grasp control is that the sensorimotor loop must be closed on the visual modality, which is very difficult to utilize effectively with standard optimal control methods ...를 문제로 두고, We show that our method attains a high success rate across a range of objects not seen during training, and our qualitative experiments show that this high success rate is due to ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In this paper, we study the problem of learning vision-based dynamic manipulation skills using a scalable reinforcement learning approach.
- **p. 1 / Abstract - extractive body cue:** We study this problem in the context of grasping, a longstanding challenge in robotic manipulation.
- **p. 1 / Abstract - extractive body cue:** In contrast to static learning behaviors that choose a grasp point and then execute the desired grasp, our method enables closed-loop vision-based control, whereby the ...
- **p. 1 / Abstract - extractive body cue:** To that end, we introduce QT-Opt, a scalable self-supervised vision-based reinforcement learning framework that can leverage over 580k real-world grasp attempts to train a deep ...
- **p. 1 / Abstract - extractive body cue:** Aside from attaining a very high success rate, our method exhibits behaviors that are quite distinct from more standard grasping systems: using only RGB visionbased ...
- **p. 2 / 1 Introduction - extractive body cue:** However, a major challenge with closed-loop grasp control is that the sensorimotor loop must be closed on the visual modality, which is very difficult to ...
- **p. 1 / 1 Introduction - extractive body cue:** While grasping restricts the manipulation problem, it still retains many of its largest challenges: a grasping system should be able to pick up previously unseen ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** We show that our method attains a high success rate across a range of objects not seen during training, and our qualitative experiments show that ...
- **p. 2 / 1 Introduction - extractive body cue:** Each cell (left) consists of a KUKA LBR IIWA arm with a two-finger gripper and an over-theshoulder RGB camera.
- **p. 7 / Method - extractive body cue:** The performance of our method is shown in Table 1.
- **p. 7 / Method - extractive body cue:** The success rate of our method in both cases is very high.
- **p. 8 / Method - extractive body cue:** Our framework is generic with respect to the task, and extending the approach to other manipulation skills would be an exciting direction for future work.
- **p. 8 / Method - extractive body cue:** 7 Discussion and Future Work We presented a framework for scalable robotic reinforcement learning with raw sensory inputs such as images, based on an algorithm ...
- **p. 7 / Method - extractive body cue:** Effective off-policy training is valuable as it allows for rapid iteration on hyperparameters and architecture design without any data collection.
- **p. 7 / Method - extractive body cue:** Dataset Test Bin emptying first 10 first 20 first 30 QT-Opt (ours) 580k off-policy + 28k on-policy 96% 88% 88% 76% Levine et al.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 7 Discussion and Future Work We presented a framework for scalable robotic reinforcement learning with raw sensory inputs such as images, based on an algorithm called QT-Opt, a distributed optimization framework, and ... | RGB-D/point cloud, object state와 contact/task observation | p. 8 (Method), p. 2 (1 Introduction) |
| State/latent | Discussion, Future, presented, framework, scalable, robotic, reinforcement, learning, sensory, inputs, images, algorithm | object geometry, affordance, contact mode 또는 end-effector state | p. 8 (Method), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Output/action | To make maximal use of this diverse dataset, we propose an off-policy training method based on a continuous-action generalization of Q-learning, which we call QTOpt. | grasp, pose, force 또는 end-effector trajectory | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 7 (Method) |
| Objective/outcome | This prior method does not reason about long-horizon rewards: although it can be used in closed-loop, the policy greedily optimizes for grasp success at the next grasp, does not control the opening ... | task completion, contact success, pose/force error와 generalization | p. 7 (Method), p. 8 (Method), p. 7 (Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** We show that our method attains a high success rate across a range of objects not seen during training, and our qualitative experiments show that ...
- **p. 2 / 1 Introduction - extractive body cue:** Each cell (left) consists of a KUKA LBR IIWA arm with a two-finger gripper and an over-theshoulder RGB camera.
- **p. 7 / Method - extractive body cue:** The performance of our method is shown in Table 1.
- **p. 7 / Method - extractive body cue:** The success rate of our method in both cases is very high.
- **p. 8 / Method - extractive body cue:** Our framework is generic with respect to the task, and extending the approach to other manipulation skills would be an exciting direction for future work.
- **p. 8 / Method - extractive body cue:** We apply this framework to the task of grasping, learning closed-loop vision-based policies that attain a high success rate on previously unseen objects, and exhibit ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 4: Off-policy and on-policy ablation of termination condition. Quantitative experiments The performance of our algorithm is evaluated empirically in a set of grasping experiments. ...
- **p. 17 / Figure/Table caption - extractive body cue:** Table 8: Data efficiency comparison in simulation. We argue that the algorithm from Levine et al. [27] is less data efficient because it optimizes a ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 7 (Method) |
| Embodiment/environment | Our results demonstrate that reinforcement learning with vision-based inputs can scale to large datasets and very large models, and can enable policies that generalize effectively for complex real-world tasks such as grasping. | hardware/simulator version and reset protocol | p. 8 (Method), p. 8 (Method) |
| Dataset/benchmark | Here, a single robot unloads a cluttered bin filled with 28 test objects, using 30 grasp attempts. | role, split, size and leakage | p. 8 (Method), p. 8 (Method), p. 7 (Method), p. 7 (Method) |
| Metric | Table 8: Data efficiency comparison in simulation. We argue that the algorithm from Levine et al. [27] is less data efficient because it optimizes a proxy objective of 1-step classification accuracy, which ... | definition, denominator, direction and uncertainty | p. 17 (Figure/Table caption), p. 7 (Figure/Table caption), p. 16 (Figure/Table caption) |
| Baseline/ablation | Table 5: Off-policy performance with and without clipped Double-Q Learning. Data efficiency As discussed in Section 5 we collected 580k grasp attempts across 7 robots with a total of about 800 robot ... | fair input/data/compute/action matching | p. 14 (Figure/Table caption), p. 16 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 13 / Figure/Table caption - extractive body cue:** Figure 5: Illustrations of the bin emptying experiment (a). The (a, right) shows a very small object getting stuck in the corner and requiring a ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Eight grasps from the QT-Opt policy, illustrating some of the strategies discovered by our method: pregrasp manipulation (a, b), grasp readjustment (c, d), ...
- **p. 7 / Method - extractive body cue:** The variant of our method that uses on-policy joint finetuning has a failure rate more than four times lower than prior work on the test ...
- **p. 8 / Method - extractive body cue:** Although the policy was usually successful, we did observe a few failure cases.
- **p. 7 / Method - extractive body cue:** 4 (c), we show examples where the policy repeatedly regrasps a slippery object on the floor, while in Fig.
- **p. 6 / 2 Related Work - extractive body cue:** This penalty may in principle result in target values outside of [0, 1], though we found empirically that this does not happen.
- **p. 6 / 2 Related Work - extractive body cue:** (2) How does its performance compare to a previously proposed self-supervised grasping system that does not explicitly optimize for long-horizon grasp success?

## Why Read It

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 However, a major challenge with closed-loop grasp control is that the sensorimotor loop must be closed on the visual modality, which is very difficult to utilize effectively with standard optimal control methods ...를 문제로 두고, We show that our method attains a high success rate across a range of objects not seen during training, and our qualitative experiments show that this high success rate is due to ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 8 (Method), p. 7 (Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
