# Scalable Deep Reinforcement Learning for Vision-Based Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1806.10293.
> PDF retrieval source: https://arxiv.org/pdf/1806.10293. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2018 / CoRL
- Authors: Dmitry Kalashnikov, Alex Irpan, Peter Pastor, Julian Ibarz, Alexander Herzog, Eric Jang, Deirdre Quillen, Ethan Holly, Mrinal Kalakrishnan, Vincent Vanhoucke, Sergey Levine
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, Reinforcement Learning, Q-learning, manipulation
- Official paper: https://arxiv.org/abs/1806.10293
- Full-text retrieval: https://arxiv.org/pdf/1806.10293
- Code/Project: https://ai.googleblog.com/2018/06/scalable-deep-reinforcement-learning.html
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

QT-Opt는 실물 로봇의 파지 시도로 시각 행동가치 함수를 학습해 파지 중에도 관측에 따라 동작을 수정한다. [PDF 1쪽](https://proceedings.mlr.press/v87/kalashnikov18a/kalashnikov18a.pdf#page=1)

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

- 분산 벨만 갱신과 교차 엔트로피 탐색을 사용해 연속 행동의 가치를 학습하고 큰 가치의 행동을 선택한다. [PDF 3쪽](https://proceedings.mlr.press/v87/kalashnikov18a/kalashnikov18a.pdf#page=3) · [PDF 4쪽](https://proceedings.mlr.press/v87/kalashnikov18a/kalashnikov18a.pdf#page=4)
- 새 물체의 실물 파지에서 정책을 평가하고 물체 재배치와 재파지가 나타난 사례를 제시한다. [PDF 7쪽](https://proceedings.mlr.press/v87/kalashnikov18a/kalashnikov18a.pdf#page=7) · [PDF 8쪽](https://proceedings.mlr.press/v87/kalashnikov18a/kalashnikov18a.pdf#page=8)

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

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 1 (1 Introduction), p. 8 (Method), p. 7 (Method)이다.
