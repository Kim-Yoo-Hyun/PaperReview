# RoboPanoptes: The All-Seeing Robot with Whole-body Dexterity

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p042.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p042.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: Xiaomeng Xu, Dominik Bauer, Shuran Song
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, whole-body manipulation, whole-body control, whole-body perception
- Official paper: https://www.roboticsproceedings.org/rss21/p042.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p042.pdf
- Code/Project: https://robopanoptes.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RoboPanoptes는 로봇 몸체 여러 곳의 카메라와 접촉면을 사용해 말단장치만으로 수행하기 힘든 조작을 학습한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p042.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present RoboPanoptes!, a capable yet practical robot system that achieves whole-body dexterity through wholebody vision.
- **p. 1 / Abstract - extractive body cue:** Its whole-body dexterity allows the robot to utilize its entire body surface for manipulation, such as leveraging ‘multiple contact points or navigating constrained spaces.
- **p. 1 / Abstract - extractive body cue:** Meanwhile, whole-body vision uses a camera system distributed over the robot's surface to provide comprehensive, multiperspective
- **p. 1 / Abstract - extractive body cue:** al feedback of its own and the environment's state.
- **p. 1 / Abstract - extractive body cue:** At its core, RoboPanoptes uses whole-body visuomotor policy that learns complex manipulation s tly from human demonstrations, efficiently aggregating information from the distributed cameras while ...
- **p. 4 / IV. MODULAR HARDWARE DESIGN - extractive body cue:** However, each camera requires an adapter cable that converts the camera board's JST connector to a USB-A port, and the ‘cameras cannot be daisy-chained.
- **p. 2 / 1. Ivrropuction - extractive body cue:** By discussing prior work on designing high-DoF robots, on leveraging them for whole-body manipulation and the closely related challenge of whole-body sensing, we illustrate the ...

## Core Idea

- **p. 2 / 1. Ivrropuction - extractive body cue:** In summary, our primary contribution is the RoboPanoptes system, demonstrating novel whole-body dexterity capabilities through whole-body vision.
- **p. 1 / Abstract - extractive body cue:** We present RoboPanoptes!, a capable yet practical robot system that achieves whole-body dexterity through wholebody vision.
- **p. 3 / IV. MODULAR HARDWARE DESIGN - extractive body cue:** RoboPanoptes' hardware consists of nine modular body units and one head unit.
- **p. 1 / 21 Cameras - extractive body cue:** design enables new robot capabilities such asa) simultaneously sweeping multiple sx
- **p. 2 / 1. Ivrropuction - extractive body cue:** This hyper-redundancy enables them to emulate their biological role models ~ such as snakes, vines [6, /] and elephant trunks [46] ~ to perform tasks ...
- **p. 4 / VI. WHOLE-Bopy VisUoMOTOR POLICY - extractive body cue:** Using the collected demonstrations, we can train a wholebody visuomotor policy that infers whole-body actions (i.e., rine joint angle sequences) given whole-body vision (i.e., images ...
- **p. 4 / VI. WHOLE-Bopy VisUoMOTOR POLICY - extractive body cue:** Compared to a common manipulation system, RoboPanoptes needs to handle significantly more complex observation spaces due to the following factors:

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Consequently, the policy must efficiently process this complex and high-dimensional input space to infer the appropriate actions. | egocentric RGB-D, language/task goal, base-arm proprioception | p. 2 (1. Ivrropuction), p. 2 (1. Ivrropuction) |
| State/latent | Consequently, policy, must, efficiently, process, complex, high-dimensional, input, space, infer, appropriate, actions | map/object/contact state와 base-arm coordination decision | p. 2 (1. Ivrropuction), p. 2 (1. Ivrropuction), p. 4 (V. DATA COLLECTION INTERFACE) |
| Output/action | + A whole-body visuomotor policy that efficiently processes ‘whole-body visual input through cross-attenton transformers and view-dependent positional encoding, while improving resilience to sensor failures through blink training Our ha ... | base motion plus arm/gripper action | p. 2 (1. Ivrropuction), p. 4 (V. DATA COLLECTION INTERFACE), p. 4 (VI. WHOLE-Bopy VisUoMOTOR POLICY) |
| Objective/outcome | long-horizon task success, reachability, collision과 recovery | long-horizon task success, reachability, collision과 recovery | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- 분산 카메라 관측을 하나의 시각운동 정책에 모으고 사람이 시연한 전신 동작을 학습한다. [PDF 2쪽](https://www.roboticsproceedings.org/rss21/p042.pdf#page=2) · [PDF 5쪽](https://www.roboticsproceedings.org/rss21/p042.pdf#page=5)
- 좁은 곳에서 상자를 열거나 여러 물체를 쓸어 옮기는 과제와 일부 카메라가 작동하지 않는 조건을 시험했다. [PDF 8쪽](https://www.roboticsproceedings.org/rss21/p042.pdf#page=8) · [PDF 9쪽](https://www.roboticsproceedings.org/rss21/p042.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (B. Sweeping Task), p. 9 (C. Stowing Task) |
| Embodiment/environment | Performance: ‘The training dataset contains 147 demonstration episodes, with each demonstration averaging 15s. | hardware/simulator version and reset protocol | p. 7 (A. Unboxing Task), p. 8 (B. Sweeping Task) |
| Dataset/benchmark | During the demonstration, images from all cameras and robot joint positions are recorded at 10 Hz | role, split, size and leakage | p. 7 (A. Unboxing Task), p. 8 (B. Sweeping Task), p. 4 (V. DATA COLLECTION INTERFACE), p. 4 (V. DATA COLLECTION INTERFACE) |
| Metric | overall 94.4% success rate, outperforming all baselines. | definition, denominator, direction and uncertainty | p. 8 (A. Unboxing Task), p. 8 (B. Sweeping Task), p. 9 (B. Sweeping Task) |
| Baseline/ablation | overall 94.4% success rate, outperforming all baselines. | fair input/data/compute/action matching | p. 8 (A. Unboxing Task), p. 4 (VI. WHOLE-Bopy VisUoMOTOR POLICY), p. 6 (VII. PRACTICAL Cons) |

## Explicit Limitations and Failure Boundary

- **p. 10 / IX. LIMITATIONS AND FUTURE WORK - extractive body cue:** The Top-down Camere policy fails to locate the hance. ‘odiing policy's actions ae less precise, leading to failures ike missing the shoe or misaligning the ...
- **p. 10 / X. CONCLUSION - extractive body cue:** Using a whole-body visuomotor policy, RoboPanoptes learns to infer complex whole-body actions from high-dimensional camera observations, while remaining robust to potential sensor failures.
- **p. 4 / VI. WHOLE-Bopy VisUoMOTOR POLICY - extractive body cue:** + Unreliable cameras: A system of many cameras is prone to unpredictable failures and delays, requiring the policy to be robust to such disturbances,
- **p. 9 / C. Stowing Task - extractive body cue:** Since our demonstration data contains behaviors of recovering from a sub-goal failure (c.g. failed grasps), we observe that the learned policy is able to capture ...
- **p. 6 / 21 Whole - extractive body cue:** To make the system robust to such camera failure at test time, we employ a "blink training" strategy that randomly drops out camera inputs during ...
- **p. 8 / A. Unboxing Task - extractive body cue:** This proves that our blink training strategy is critical to the robustness of the policy, especially during unexpected test-time sensor failures.
- **p. 6 / 21 Whole - extractive body cue:** Concretely, we simulate a 5% failure rate for each camera, independently masking out entire images at each time step.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 4 (IV. MODULAR HARDWARE DESIGN), p. 2 (1. Ivrropuction), p. 3 (C. Whole-body Sensing), p. 1 (1. Ivrropuction), p. 1 (Abstract), p. 4 (VI. WHOLE-Bopy VisUoMOTOR POLICY)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, each camera requires an adapter cable that converts the camera board's JST connector to a USB-A port, and the ‘cameras cannot be daisy-chained. (p. 4, IV. MODULAR HARDWARE DESIGN).
- **Actual contribution:** design enables new robot capabilities such asa) simultaneously sweeping multiple sx (p. 1, 21 Cameras).
- **Evaluation boundary:** overall 94.4% success rate, outperforming all baselines. (p. 8, A. Unboxing Task).
- **Explicit failure boundary:** The Top-down Camere policy fails to locate the hance. ‘odiing policy's actions ae less precise, leading to failures ike missing the shoe or misaligning the drawer. (p. 10, IX. LIMITATIONS AND FUTURE WORK).

## 배포 범위 대조

- 코드 — 저자 구현 파일 · train.py [배포 파일](https://raw.githubusercontent.com/real-stanford/RoboPanoptes/765bf79dfdb9cc8f9a1baacb0e928df10f0e9c48/train.py)
- 가중치 — Stanford 배포 디렉토리의 쓸기 정책 체크포인트다. README 명령에 잘못 들어간 호스트 구분자를 바로잡았다. [배포 파일](https://real.stanford.edu/robopanoptes/data/pretrained_models/sweep.ckpt)
- 데이터 — 쓸기 조작의 전처리 시연 묶음이다. 같은 디렉토리에 상자 열기와 정리 자료도 있다. [배포 파일](https://real.stanford.edu/robopanoptes/data/zarr_datasets/sweep.zarr.zip)
