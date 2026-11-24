# Learning to Rearrange Deformable Cables, Fabrics, and Bags with Goal-Conditioned Transporter Networks

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2012.03385.
> PDF retrieval source: https://arxiv.org/pdf/2012.03385. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / ICRA
- Authors: Daniel Seita, Pete Florence, Jonathan Tompson, Erwin Coumans, Vikas Sindhwani, Ken Goldberg, Andy Zeng
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, deformable object, cable manipulation, cloth manipulation, goal-conditioned learning, vision-based control
- Official paper: https://arxiv.org/abs/2012.03385
- Full-text retrieval: https://arxiv.org/pdf/2012.03385
- Code/Project: https://sites.google.com/view/berkeley-deformable/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://arxiv.org/pdf/2012.03385v4) 기준이다.

## Why This Paper Is Here

이 연구는 목표 영상과 현재 관측을 함께 사용해 케이블·천·가방을 원하는 배치로 옮기는 조작 정책을 학습한다. [PDF 1쪽](https://arxiv.org/pdf/2012.03385v4#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Rearranging and manipulating deformable objects such as cables, fabrics, and bags is a long-standing challenge in robotic manipulation.
- **p. 1 / Abstract - extractive body cue:** The complex dynamics and highdimensional configuration spaces of deformables, compared to rigid objects, make manipulation difficult not only for multistep planning, but even for goal ...
- **p. 1 / Abstract - extractive body cue:** Goals cannot be as easily specified as rigid object poses, and may involve complex relative spatial relations such as "place the item inside the bag." ...
- **p. 1 / Abstract - extractive body cue:** We propose embedding goal-conditioning into Transporter Networks, a recently proposed model architecture for learning robotic manipulation that rearranges deep features to infer displacements that can ...
- **p. 1 / Abstract - extractive body cue:** In simulation and in physical experiments, we demonstrate that goal-conditioned Transporter Networks enable agents to manipulate deformable structures into flexibly specified configurations without test-time visual ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Manipulating deformable objects is a long-standing challenge in robotics with a wide range of real-world applications.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In contrast to rigid object manipulation, deformable object manipulation presents additional challenges due to more complex configuration spaces, dynamics, and sensing.

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** For several tasks in the benchmark, we propose to tackle them using novel goal-conditioned variants of Transporter Network [68] architectures.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose a new suite of benchmark tasks, called DeformableRavens, to test manipulation of cables, fabrics, and bags spanning 1D, 2D, and ...
- **p. 3 / IV. GOAL-CONDITIONED TRANSPORTER NETWORKS - extractive body cue:** Goal-Conditioned Transporter Networks We propose two goal-conditioned architectures based on Transporter Networks.
- **p. 3 / III. BACKGROUND - extractive body cue:** To train the policy, we assume access to a small dataset of N stochastic expert demonstrations D = {ξi}N i=1, where each episode ξi of ...
- **p. 4 / IV. GOAL-CONDITIONED TRANSPORTER NETWORKS - extractive body cue:** [53], [54]. with rotations and translations, this enables data augmentation by randomizing a rotation and translation for each training image.
- **p. 3 / IV. GOAL-CONDITIONED TRANSPORTER NETWORKS - extractive body cue:** For the goal-conditioned Transporter Networks, we use the same procedure to get (ok, ak), then additionally use the corresponding observation og after the last action ...
- **p. 1 / Abstract - extractive body cue:** We propose embedding goal-conditioning into Transporter Networks, a recently proposed model architecture for learning robotic manipulation that rearranges deep features to infer displacements that can ...
- **p. 3 / III. BACKGROUND - extractive body cue:** The first FCN fpick takes as input the visual observation ot, and outputs a dense per-pixel prediction of action-values Qpick that correlate with picking success: ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The first FCN fpick takes as input the visual observation ot, and outputs a dense per-pixel prediction of action-values Qpick that correlate with picking success: Tpick = arg max(u,v) Qpick((u, v)/ot) where ... | RGB-D/point cloud, object state와 contact/task observation | p. 3 (III. BACKGROUND), p. 2 (III. BACKGROUND) |
| State/latent | first, FCN, fpick, takes, input, visual, observation, outputs, dense, per-pixel, prediction, action-values | object geometry, affordance, contact mode 또는 end-effector state | p. 3 (III. BACKGROUND), p. 2 (III. BACKGROUND), p. 3 (III. BACKGROUND) |
| Output/action | Problem Formulation We formulate the problem of rearranging deformable objects as learning a policy π that sequences pick and place actions at ∈A with a robot from visual observations ot ∈O: π(ot) ... | grasp, pose, force 또는 end-effector trajectory | p. 2 (III. BACKGROUND), p. 3 (III. BACKGROUND), p. 2 (III. BACKGROUND) |
| Objective/outcome | Contact and friction constraints between soft bodies and multi bodies are solved in a unified constraint solver at the velocity level. | task completion, contact success, pose/force error와 generalization | p. 4 (V. SIMULATOR AND TASKS), p. 4 (V. SIMULATOR AND TASKS), p. 5 (V. SIMULATOR AND TASKS) |

## Main Claims and Actual Contribution

- 목표 영상의 특징을 Transporter Networks의 집기·놓기 예측에 결합해 물체의 상대 이동을 정한다. [PDF 3쪽](https://arxiv.org/pdf/2012.03385v4#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2012.03385v4#page=4)
- ICRA 판은 여러 변형체의 시뮬레이션 과제를 비교했고 저자 개정판은 실물 케이블 재배치 실험을 추가했다. [PDF 5쪽](https://arxiv.org/pdf/2012.03385v4#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2012.03385v4#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2012.03385v4#page=7) · [PDF 10쪽](https://arxiv.org/pdf/2012.03385v4#page=10)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | PyBullet 시뮬레이션과 개정판 v4의 실물 케이블 실험 | 판본별 평가 범위 | [PDF 10쪽](https://arxiv.org/pdf/2012.03385v4#page=10) |
| Embodiment/environment | We next validate experiments on physical hardware using a Franka Panda robot with a standard parallel-jaw gripper. | hardware/simulator version and reset protocol | p. 6 (VIII. PHYSICAL EXPERIMENTS AND RESULTS), p. 5 (VI. SIMULATION EXPERIMENTS) |
| Dataset/benchmark | Task success rate (mean % over 60 test-time episodes in simulation of the best saved snapshot) vs. # of demonstration episodes (1, 10, 100, or 1000) used in training. | role, split, size and leakage | p. 6 (VIII. PHYSICAL EXPERIMENTS AND RESULTS), p. 5 (VI. SIMULATION EXPERIMENTS), p. 6 (VII. SIMULATION RESULTS), p. 5 (VI. SIMULATION EXPERIMENTS) |
| Metric | Transporter-Goal-Stack achieves slightly higher performance among the cable-related tasks, though the gap narrows with more demonstrations in cable-line-notarget, since both goal-conditioned Transporters each achieve 100% success rates ... | definition, denominator, direction and uncertainty | p. 6 (VII. SIMULATION RESULTS), p. 6 (VII. SIMULATION RESULTS), p. 5 (VII. SIMULATION RESULTS) |
| Baseline/ablation | Goal Conditioned Tasks Across all 4 dataset sizes for cable-line-notarget, cableshape-notarget, and fabric-flat-notarget, both TransporterGoal-Stack and Transporter-Goal-Split substantially outperform the two GT-State baselines. | fair input/data/compute/action matching | p. 6 (VII. SIMULATION RESULTS), p. 5 (VII. SIMULATION RESULTS), p. 5 (VI. SIMULATION EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Failure cases we observe from trained Transporter policies on bag tasks. Left: in all bag tasks, a failure case may result from covering ...
- **p. 4 / V. SIMULATOR AND TASKS - extractive body cue:** While prior work with soft bodies in PyBullet [18], [19], [44] use position-based dynamics solvers, we use new soft body physics simulation based on the ...
- **p. 6 / VIII. PHYSICAL EXPERIMENTS AND RESULTS - extractive body cue:** Changes from Simulation Unlike in simulation, we cannot assume "perfect" grasping of deformable objects.
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: The 12 tasks in the proposed DeformableRavens benchmark (see Table I) with suction cup gripper and deformable objects. Top row: (a) cable-ring, (b) ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: The proposed Transporter-Goal-Split, applied to an example on bag-color-goal, where given the current image ot and goal og, the objective is to insert ...
- **p. 5 / V. SIMULATOR AND TASKS - extractive body cue:** Bags with handles (e.g., top right) or with more stiffness will be addressed in future work.
- **p. 5 / VI. SIMULATION EXPERIMENTS - extractive body cue:** A model that uses ground truth pose information as observations ot, and does not use images.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 3 (III. BACKGROUND), p. 2 (III. BACKGROUND), p. 3 (IV. GOAL-CONDITIONED TRANSPORTER NETWORKS)이다.
