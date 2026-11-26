# On Bringing Robots Home

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (32 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2311.16098.
> PDF retrieval source: https://arxiv.org/pdf/2311.16098. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / arXiv
- Authors: Nur Muhammad Mahi Shafiullah, Anant Rai, Haritheja Etukuru, Yiqian Liu, Ishan Misra, Soumith Chintala, Lerrel Pinto
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, mobile manipulation, home robotics, Imitation Learning, human demonstrations
- Official paper: https://arxiv.org/abs/2311.16098
- Full-text retrieval: https://arxiv.org/pdf/2311.16098
- Code/Project: https://dobb-e.com/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (32 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

Dobb·E는 가정에서 휴대용 도구로 수집한 조작 시연으로 시각 표현을 사전학습하고 새 집의 소수 시연으로 Stretch의 정책을 훈련한다. [PDF 1쪽](https://arxiv.org/pdf/2311.16098v1#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Throughout history, we have successfully integrated various machines into our homes.
- **p. 1 / Abstract - extractive body cue:** Dishwashers, laundry machines, stand mixers, and robot vacuums are just a few recent examples.
- **p. 1 / Abstract - extractive body cue:** However, these machines excel at performing only a single task effectively.
- **p. 1 / Abstract - extractive body cue:** The concept of a "generalist machine" in homes - a domestic assistant that can adapt and learn from our needs, all while remaining cost-effective - ...
- **p. 1 / Abstract - extractive body cue:** In this work, we initiate a large-scale effort towards this goal by introducing Dobb·E, an affordable yet versatile general-purpose system for learning robotic manipulation within ...
- **p. 4 / 1 Introduction - extractive body cue:** Such an effort requires a shift from the prevailing paradigm - current research in robotics is predominantly either conducted in industrial environments or in academic ...

## Core Idea

- **p. 4 / 1 Introduction - extractive body cue:** In this work we present Dobb·E, a framework for teaching robots in homes by embodying three core principles: efficiency, safety, and user comfort.
- **p. 1 / Abstract - extractive body cue:** Success 81% Pick up hat Open microwave door Pick up paper towel roll Place rag in laundry Open cabinet door Close cabinet door Open shower ...
- **p. 7 / C D - extractive body cue:** Our method can be divided into four broad stages: (a) designing a hardware setup that helps us in the collection of demonstrations and their seamless ...
- **p. 1 / Abstract - extractive body cue:** Then, in a novel home environment, with five minutes of demonstrations and fifteen minutes of adapting the HPR model, we show that Dobb·E can reliably ...
- **p. 4 / 1 Introduction - extractive body cue:** For user comfort, we have developed an ergonomic demonstration collection tool, enabling us to gather task-specific demonstrations in unfamiliar homes without direct robot operation.
- **p. 4 / 1 Introduction - extractive body cue:** This dataset serves to pretrain representation models for Dobb·E. • Models and algorithms: Given the pretraining dataset we train a streamlined vision model, called Home ...
- **p. 6 / C D - extractive body cue:** Behavior cloning involves training a model to mimic a demonstrated behavior or action, often through the use of labeled training data mapping observations to desired ...
- **p. 6 / C D - extractive body cue:** Our key experimental findings are: • Surprising effectiveness of simple methods: Dobb·E follows a simple behavior cloning recipe for visual imitation learning using a ResNet ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Behavior cloning involves training a model to mimic a demonstrated behavior or action, often through the use of labeled training data mapping observations to desired actions. | egocentric RGB-D, language/task goal, base-arm proprioception | p. 6 (C D), p. 6 (C D) |
| State/latent | Behavior, cloning, involves, training, model, mimic, demonstrated, action, often, through, labeled, data | map/object/contact state와 base-arm coordination decision | p. 6 (C D), p. 6 (C D), p. 7 (C D) |
| Output/action | On average, only using 91 seconds of data on each task collected over five minutes, Dobb·E can achieve a 81% success rate in homes (see Section 3). • Impact of effective SSL ... | base motion plus arm/gripper action | p. 6 (C D), p. 7 (C D), p. 7 (C D) |
| Objective/outcome | The concept of a "generalist machine" in homes - a domestic assistant that can adapt and learn from our needs, all while remaining cost-effective - has long been a goal in robotics ... | long-horizon task success, reachability, collision과 recovery | p. 1 (Abstract), p. 6 (C D), p. 6 (C D) |

## Main Claims and Actual Contribution

- 아이폰을 부착한 시연 수집기와 가정 내 데이터셋을 구축해 로봇 없이도 사람의 시각·동작 기록을 수집한다. [PDF 5쪽](https://arxiv.org/pdf/2311.16098v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2311.16098v1#page=6) · [PDF 9쪽](https://arxiv.org/pdf/2311.16098v1#page=9)
- 새 가정에서 과제별 시연을 모아 정책을 조정한 뒤 실제 시행을 반복해 작업별 성공률을 기록한다. [PDF 12쪽](https://arxiv.org/pdf/2311.16098v1#page=12) · [PDF 13쪽](https://arxiv.org/pdf/2311.16098v1#page=13)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 1 (Figure/Table caption), p. 22 (Figure/Table caption) |
| Embodiment/environment | 25 4.4 Robustifying Robot Hardware . . . . . . . . . . . . . . . . . . . . . . . . . . . ... | hardware/simulator version and reset protocol | p. 3 (3 Experiments), p. 20 (3 Experiments) |
| Dataset/benchmark | We found that 6D pick and place tasks generally fail because they generally require robot motion in a variety of axes: like translations and rotations at different axes at different parts of ... | role, split, size and leakage | p. 3 (3 Experiments), p. 20 (3 Experiments), p. 17 (3 Experiments), p. 18 (3 Experiments) |
| Metric | 0 20 40 60 80 100 Success rate (%) Air-fryer closing Cushion flipping Door closing Drawer closing Chair pulling Pulling from shelf Bag pickup Drawer opening Towel pickup Unplugging Tissue pickup Door ... | definition, denominator, direction and uncertainty | p. 16 (3 Experiments), p. 23 (3 Experiments), p. 21 (Figure/Table caption) |
| Baseline/ablation | Alongside these household experiments, we also set up a "home" area in our lab, with a benchmark suite with 10 tasks that we use to run our baselines and ablations. | fair input/data/compute/action matching | p. 12 (3 Experiments), p. 17 (3 Experiments), p. 17 (3 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 20 / Figure/Table caption - extractive body cue:** Figure 20: First-person POV rollouts of Home 3 Pick and Place comparing (top) a policy trained on demos where the object is picked and placed ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 18: Opening an outward facing window blind (top row) both without depth (second row) and with depth (third row). The depth values (bottom row) ...
- **p. 17 / 3 Experiments - extractive body cue:** We discuss the failure cases further in Section 3.3.
- **p. 17 / 3 Experiments - extractive body cue:** Once we turned on an overhead light for even lighting, there were no more failures.
- **p. 21 / 3 Experiments - extractive body cue:** The failure modes for tasks without depth are generally concentrated around cases where the robot end-effector (and thus the camera) is very close to some ...
- **p. 23 / 3 Experiments - extractive body cue:** This failure mode points to the need of better designed, less bare-boned robot grippers for household tasks.
- **p. 23 / 3 Experiments - extractive body cue:** In both cases, the sub-task causing primary failure was not letting go of the grasped object (cup or muffin).

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 4 (1 Introduction), p. 6 (C D), p. 1 (Abstract)이다.
