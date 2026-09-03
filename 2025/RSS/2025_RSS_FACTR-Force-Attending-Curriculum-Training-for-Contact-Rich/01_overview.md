# FACTR: Force-Attending Curriculum Training for Contact-Rich Policy Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p079.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p079.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, tactile/force, force feedback, contact-rich manipulation, Imitation Learning, curriculum learning
- Official paper: https://www.roboticsproceedings.org/rss21/p079.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p079.pdf
- Code/Project: https://jasonjzliu.com/factr/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 4: FACTR allows our policy to beter integrate force information without overfittng to visual information, resulting in better generalization를 문제로 두고, For the decoder, we introduce & action tokens, A ¢ R**¢.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Many contact-rich tasks humans perform, such as, box pickup or rolling dough, rely on force feedback for reliable execution.
- **p. 1 / Abstract - extractive body cue:** However, this force information, which is readily avail able in most robot arms, is not commonly used in teleoperation and policy learning.
- **p. 1 / Abstract - extractive body cue:** Consequently, robot behavior is often limited to quasi-static kinematic tasks that do not require intr
- **p. 1 / Abstract - extractive body cue:** In this paper, we first present a low-cost, intuitive, bilateral teleoperation setup that relays external forces of the follower arm back to the teacher arm, ...
- **p. 1 / Abstract - extractive body cue:** We then introduce FACTR, a policy learning method that employs a curriculum which corrupts the visual input with decreasing intensity throughout training. ‘The curriculum prevents ...
- **p. 5 / A. Problem Statement and Base Model - extractive body cue:** 4: FACTR allows our policy to beter integrate force information without overfittng to visual information, resulting in better generalization

## Core Idea

- **p. 5 / A. Problem Statement and Base Model - extractive body cue:** For the decoder, we introduce & action tokens, A ¢ R**¢.
- **p. 5 / A. Problem Statement and Base Model - extractive body cue:** 4: FACTR allows our policy to beter integrate force information without overfittng to visual information, resulting in better generalization
- **p. 5 / A. Problem Statement and Base Model - extractive body cue:** Visual observations and force readings are converted into tokens, fed to the encoder, then decoded into action tokens through cross attention.
- **p. 5 / A. Problem Statement and Base Model - extractive body cue:** then tokenized by a vision encoder and a force encoder before fed into an action transformer to regress joint position targets gee.
- **p. 4 / A. Problem Statement and Base Model - extractive body cue:** We consider a policy o(- / -) that produces a chunk of future actions of length k d..++1 (joint positions) given visual observation [, (image ...
- **p. 4 / A. Problem Statement and Base Model - extractive body cue:** Each trajectory in D comprises tuples (I;,7:, 1).

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We consider a policy o(- / -) that produces a chunk of future actions of length k d..++1 (joint positions) given visual observation [, (image at time 1), and (ii) an external ... | tactile image/force, vision과 proprioceptive history | p. 4 (A. Problem Statement and Base Model), p. 5 (A. Problem Statement and Base Model) |
| State/latent | consider, policy, produces, chunk, future, actions, length, joint, positions, given, visual, observation | contact geometry, force state 또는 latent dynamics | p. 4 (A. Problem Statement and Base Model), p. 5 (A. Problem Statement and Base Model), p. 5 (A. Problem Statement and Base Model) |
| Output/action | attends to vision vs. force tokens at layer [, and will be the Finally, we project the decoder output H/? to action space, | grasp/contact action, force command 또는 object motion | p. 5 (A. Problem Statement and Base Model), p. 5 (A. Problem Statement and Base Model), p. 4 (A. Problem Statement and Base Model) |
| Objective/outcome | slip/contact success, force/pose error와 robustness | slip/contact success, force/pose error와 robustness | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 5 / A. Problem Statement and Base Model - extractive body cue:** For the decoder, we introduce & action tokens, A ¢ R**¢.
- **p. 5 / A. Problem Statement and Base Model - extractive body cue:** 4: FACTR allows our policy to beter integrate force information without overfittng to visual information, resulting in better generalization
- **p. 8 / C. Policy Evaluation - extractive body cue:** For the test objects, the vision-only policy achieves a success rate of 21.3% on average, which is significantly worse than policies incorporating force.
- **p. 8 / C. Policy Evaluation - extractive body cue:** Without a curriculum, policies naively incorporating force achieve a success rate of 61.2%, ‘hile FACTR achieves a success rate of 87.5%, which shows that FACTR ...
- **p. 7 / C. Policy Evaluation - extractive body cue:** We present the average success rate for truining and testing objects, respectively.
- **p. 7 / B. Teleoperation Evaluation - extractive body cue:** Our experiments show that our system allows users to ‘complete tasks with 64.7% higher task completion rate, 37.4% reduced completion time, and 83.3% improvement in ...
- **p. 6 / A. Experimental Setup - extractive body cue:** We describe the tasks details and the success erteria below
- **p. 9 / C. Policy Evaluation - extractive body cue:** The results are presented in TABLE I

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (C. Policy Evaluation), p. 8 (C. Policy Evaluation) |
| Embodiment/environment | These asks are challenging as they require the robot to perceive and respond to the force feedback as it manipulates objects with unseen visual appearances and geometries, | hardware/simulator version and reset protocol | p. 7 (B. Teleoperation Evaluation), p. 8 (C. Policy Evaluation) |
| Dataset/benchmark | We observe that for tasks that require continuous contact between the arm and an object, such as non-prehensile pivoting and bimanual box lifting, the un-actuated teleoperation system often causes the follower arm ... | role, split, size and leakage | p. 7 (B. Teleoperation Evaluation), p. 8 (C. Policy Evaluation), p. 7 (B. Teleoperation Evaluation), p. 6 (A. Experimental Setup) |
| Metric | We present the average success rate for truining and testing objects, respectively. | definition, denominator, direction and uncertainty | p. 7 (C. Policy Evaluation), p. 8 (C. Policy Evaluation), p. 8 (C. Policy Evaluation) |
| Baseline/ablation | ‘+ How does FACTR perform compared to baseline approaches that do not use force feedback and ones that use force feedback without FACTR? | fair input/data/compute/action matching | p. 7 (C. Policy Evaluation), p. 7 (B. Teleoperation Evaluation), p. 8 (C. Policy Evaluation) |

## Explicit Limitations and Failure Boundary

- **p. 9 / VI. CONCLUSION AND LIMITATIONS - extractive body cue:** Developing. adaptive or self-tuning curriculum strategies could help mitigate this issue by dynamically adjusting hyperparameters based on task-specific requirements, Addressing these limitations could further enhance ...
- **p. 8 / C. Policy Evaluation - extractive body cue:** While without the curriculum, the policy does not pay enough attention 10 force, and either fails to lift or balance the novel boxes.
- **p. 9 / VI. CONCLUSION AND LIMITATIONS - extractive body cue:** This limitation can particularly affect tasks that involve subtle force adjustments during finegrained manipulation since the torque readings can be too noisy to be used ...
- **p. 7 / C. Policy Evaluation - extractive body cue:** 6, All the policies perform similarly on the train objects for most tasks, except for the rolling dough task, where the vision-only policy smashes the ...
- **p. 8 / C. Policy Evaluation - extractive body cue:** FACTR leads to better recovery behavior.

## Why Read It

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 4: FACTR allows our policy to beter integrate force information without overfittng to visual information, resulting in better generalization를 문제로 두고, For the decoder, we introduce & action tokens, A ¢ R**¢.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 5 (A. Problem Statement and Base Model), p. 5 (A. Problem Statement and Base Model), p. 5 (A. Problem Statement and Base Model), p. 4 (A. Problem Statement and Base Model), p. 4 (A. Problem Statement and Base Model), p. 8 (C. Policy Evaluation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** 4: FACTR allows our policy to beter integrate force information without overfittng to visual information, resulting in better generalization (p. 5, A. Problem Statement and Base Model).
- **Actual contribution:** For the decoder, we introduce & action tokens, A ¢ R**¢. (p. 5, A. Problem Statement and Base Model).
- **Evaluation boundary:** Our experiments show that our system allows users to ‘complete tasks with 64.7% higher task completion rate, 37.4% reduced completion time, and 83.3% improvement in the subjective ease of use ... (p. 7, B. Teleoperation Evaluation).
- **Explicit failure boundary:** While without the curriculum, the policy does not pay enough attention 10 force, and either fails to lift or balance the novel boxes. (p. 8, C. Policy Evaluation).
