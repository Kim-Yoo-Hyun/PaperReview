# RoboPanoptes: The All-Seeing Robot with Whole-body Dexterity

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p042.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p042.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, mobile manipulation, whole-body control, whole-body perception
- Official paper: https://www.roboticsproceedings.org/rss21/p042.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p042.pdf
- Code/Project: https://www.roboticsproceedings.org/rss21/p042.html
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 However, each camera requires an adapter cable that converts the camera board's JST connector to a USB-A port, and the ‘cameras cannot be daisy-chained.를 문제로 두고, In summary, our primary contribution is the RoboPanoptes system, demonstrating novel whole-body dexterity capabilities through whole-body vision.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 2 / 1. Ivrropuction - extractive body cue:** In summary, our primary contribution is the RoboPanoptes system, demonstrating novel whole-body dexterity capabilities through whole-body vision.
- **p. 1 / Abstract - extractive body cue:** We present RoboPanoptes!, a capable yet practical robot system that achieves whole-body dexterity through wholebody vision.
- **p. 3 / IV. MODULAR HARDWARE DESIGN - extractive body cue:** RoboPanoptes' hardware consists of nine modular body units and one head unit.
- **p. 1 / 21 Cameras - extractive body cue:** design enables new robot capabilities such asa) simultaneously sweeping multiple sx
- **p. 2 / 1. Ivrropuction - extractive body cue:** This hyper-redundancy enables them to emulate their biological role models ~ such as snakes, vines [6, /] and elephant trunks [46] ~ to perform tasks ...
- **p. 9 / B. Sweeping Task - extractive body cue:** RoboPanoptes achieves a 96.6% success rate, outperforming all baselines.
- **p. 9 / C. Stowing Task - extractive body cue:** RoboPanoptes achieves an overall success rate of 83.3%, compared to 27.8% for the w/o Camexa Pose policy and 0% for the Top-down Camera policy (Fig.
- **p. 6 / 21 Whole - extractive body cue:** Consistent with observations in previous work [34], this simple strategy significantly improves the robustness of the policy, enabling it to succeed even when some cameras ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

Locomotion, whole-body, mobile manipulation, and humanoids의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 However, each camera requires an adapter cable that converts the camera board's JST connector to a USB-A port, and the ‘cameras cannot be daisy-chained.를 문제로 두고, In summary, our primary contribution is the RoboPanoptes system, demonstrating novel whole-body dexterity capabilities through whole-body vision.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 4 (IV. MODULAR HARDWARE DESIGN), p. 2 (1. Ivrropuction), p. 3 (C. Whole-body Sensing), p. 1 (1. Ivrropuction), p. 1 (Abstract), p. 4 (VI. WHOLE-Bopy VisUoMOTOR POLICY) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, each camera requires an adapter cable that converts the camera board's JST connector to a USB-A port, and the ‘cameras cannot be daisy-chained. (p. 4, IV. MODULAR HARDWARE DESIGN).
- **Actual contribution:** design enables new robot capabilities such asa) simultaneously sweeping multiple sx (p. 1, 21 Cameras).
- **Evaluation boundary:** overall 94.4% success rate, outperforming all baselines. (p. 8, A. Unboxing Task).
- **Explicit failure boundary:** The Top-down Camere policy fails to locate the hance. ‘odiing policy's actions ae less precise, leading to failures ike missing the shoe or misaligning the drawer. (p. 10, IX. LIMITATIONS AND FUTURE WORK).
