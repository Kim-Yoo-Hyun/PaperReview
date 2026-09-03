# MIRAGE: Cross-Embodiment Zero-Shot Policy Transfer with Cross-Painting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss20/p069.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss20/p069.html. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, cross-embodiment, zero-shot transfer, policy transfer, manipulation, domain adaptation
- Official paper: https://www.roboticsproceedings.org/rss20/p069.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss20/p069.html
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 This poses several challenges, as outlined in prior work [108], stemming from variations in kinematic configuration, control scheme, camera viewpoint, and end-effector morphology.를 문제로 두고, To summarize, our key contributions are:를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The ability to reuse collected data and transfer trained policies between robots could alleviate the burden of additional data collection and training.
- **p. 1 / Abstract - extractive body cue:** While existing approaches such as pretraining plus finetuning and co-training show promise, they do not generalize to robots unseen in training.
- **p. 1 / Abstract - extractive body cue:** Focusing on common robot arms with similar workspaces and 2-jaw grippers, we investigate the feasibility of zero-shot transfer.
- **p. 1 / Abstract - extractive body cue:** Through simulation studies on 8 manipulation tasks, we find that state-based Cartesian control policies can successfully zero-shot transfer to a target robot after accounting for ...
- **p. 1 / Abstract - extractive body cue:** To address robot visual disparities for vision-based policies, we introduce Mirage, which uses "cross-painting"-masking out the unseen target robot and inpainting the seen source robot-during ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** This poses several challenges, as outlined in prior work [108], stemming from variations in kinematic configuration, control scheme, camera viewpoint, and end-effector morphology.
- **p. 4 / 4) We assume that the background and lighting conditions - extractive body cue:** This allows us to separate any challenges that arise due to changes in the background environment and focus on the impact of visual differences between ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** To summarize, our key contributions are:
- **p. 1 / Abstract - extractive body cue:** To address robot visual disparities for vision-based policies, we introduce Mirage, which uses "cross-painting"-masking out the unseen target robot and inpainting the seen source robot-during ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Through extensive experiments on 9 manipulation tasks in both simulation and real across 6 different robot and gripper setups, we show that Mirage, despite its ...
- **p. 3 / 1) We assume knowledge of the two robots' coordinate - extractive body cue:** This allows us to render robots in a camera pose that is within the distribution of the training image poses.
- **p. 3 / 1) We assume knowledge of the two robots' coordinate - extractive body cue:** This allows us to transfer between robots with different numbers of joints and compensate for alternate gripper shapes across embodiments.
- **p. 4 / 4) We assume that the background and lighting conditions - extractive body cue:** Given a source policy action aS t+1 = πS(sS t , oS t ), we would like to transform it into a target policy action ...
- **p. 4 / 4) We assume that the background and lighting conditions - extractive body cue:** We consider the setting where there is a policy πS trained on a dataset of the source robot D = {(sS 1 , oS 1 ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To handle differences in control gains, Mirage pairs the source robot policy with a forward dynamics model and executes the action predicted by the policy ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given a source policy action aS t+1 = πS(sS t , oS t ), we would like to transform it into a target policy action aT t+1 = πT (sT t , ... | image/video, language instruction, proprioception과 history | p. 4 (4) We assume that the background and lighting conditions), p. 4 (4) We assume that the background and lighting conditions) |
| State/latent | Given, source, policy, action, would, like, transform, target, takes, inputs, states, observations | language-grounded task state와 action-policy context | p. 4 (4) We assume that the background and lighting conditions), p. 4 (4) We assume that the background and lighting conditions), p. 3 (III. PROBLEM STATEMENT) |
| Output/action | We consider the setting where there is a policy πS trained on a dataset of the source robot D = {(sS 1 , oS 1 , aS 1 , ..., sS Hi, ... | continuous action, pose 또는 action chunk | p. 4 (4) We assume that the background and lighting conditions), p. 3 (III. PROBLEM STATEMENT), p. 7 (2) Can Mirage successfully zero-shot transfer trained vision) |
| Objective/outcome | Focusing on common robot arms with similar workspaces and 2-jaw grippers, we investigate the feasibility of zero-shot transfer. | instruction following, task success, generalization과 latency | p. 1 (Abstract) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** To summarize, our key contributions are:
- **p. 1 / Abstract - extractive body cue:** To address robot visual disparities for vision-based policies, we introduce Mirage, which uses "cross-painting"-masking out the unseen target robot and inpainting the seen source robot-during ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Through extensive experiments on 9 manipulation tasks in both simulation and real across 6 different robot and gripper setups, we show that Mirage, despite its ...
- **p. 3 / 1) We assume knowledge of the two robots' coordinate - extractive body cue:** This allows us to render robots in a camera pose that is within the distribution of the training image poses.
- **p. 3 / 1) We assume knowledge of the two robots' coordinate - extractive body cue:** This allows us to transfer between robots with different numbers of joints and compensate for alternate gripper shapes across embodiments.
- **p. 5 / IV. STATE-BASED TRANSFER EXPERIMENTS - extractive body cue:** Study Results Table I shows that when the target robots have the same gripper as the source robot, most unseen target robots achieve very high ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 5: Mirage applied to first-person wrist camera images and third- person front camera images. For each view, the top row shows the actual observations ...
- **p. 2 / 3) Physical experiments with Franka and UR5 demonstrating - extractive body cue:** that Mirage successfully transfers between robots and grippers on 4 manipulation tasks, suffering only minimal performance degradation from the source policy and significantly outperforming a ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 9 (Figure/Table caption) |
| Embodiment/environment | For simulation experiments, we take into account potential occlusions between the robot and objects by comparing the pixel-wise depth values between the camera observation of the scene and the rendered robot. | hardware/simulator version and reset protocol | p. 6 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS) |
| Dataset/benchmark | At each timestep, the source robot sees the world state (pr, po) of the target environment, where pr and po are the poses of the robot end effector and the objects. | role, split, size and leakage | p. 6 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS) |
| Metric | For all tasks, we train the source state-based policy on the Franka robot and evaluate the success rates on different target robots using the test-time execution strategy mentioned above. | definition, denominator, direction and uncertainty | p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS) |
| Baseline/ablation | that Mirage successfully transfers between robots and grippers on 4 manipulation tasks, suffering only minimal performance degradation from the source policy and significantly outperforming a state-of-the-art generalist model. | fair input/data/compute/action matching | p. 2 (3) Physical experiments with Franka and UR5 demonstrating), p. 9 (Figure/Table caption), p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 5 / IV. STATE-BASED TRANSFER EXPERIMENTS - extractive body cue:** Less robust source policies leave little room for error, while more robust ones tend to retry even if the target robot fails to grasp the ...
- **p. 9 / 2) Can Mirage successfully zero-shot transfer trained vision - extractive body cue:** On the other hand, the failure modes we observe on the different robots or grippers are all very similar to those from the source policy ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 6: (a) An example of camera calibration error resulting in failure to mask all of the target robot out; (b) An example of the ...
- **p. 5 / IV. STATE-BASED TRANSFER EXPERIMENTS - extractive body cue:** We see that there is a significant drop in performance, indicating that the difference in the forward dynamics between robots cannot be ignored when transferring ...
- **p. 9 / 2) Can Mirage successfully zero-shot transfer trained vision - extractive body cue:** This is not surprising as the policy is trained with matching proprioceptive values and image observations, and large offsets in the proprioceptive values correspond to ...
- **p. 2 / 3) Physical experiments with Franka and UR5 demonstrating - extractive body cue:** that Mirage successfully transfers between robots and grippers on 4 manipulation tasks, suffering only minimal performance degradation from the source policy and significantly outperforming a ...
- **p. 6 / IV. STATE-BASED TRANSFER EXPERIMENTS - extractive body cue:** For real experiments, however, we do not use depth due to noise and imprecision in the camera observations.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 This poses several challenges, as outlined in prior work [108], stemming from variations in kinematic configuration, control scheme, camera viewpoint, and end-effector morphology.를 문제로 두고, To summarize, our key contributions are:를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 4 (4) We assume that the background and lighting conditions), p. 3 (III. PROBLEM STATEMENT), p. 3 (III. PROBLEM STATEMENT), p. 4 (4) We assume that the background and lighting conditions), p. 4 (4) We assume that the background and lighting conditions) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** This poses several challenges, as outlined in prior work [108], stemming from variations in kinematic configuration, control scheme, camera viewpoint, and end-effector morphology. (p. 2, I. INTRODUCTION).
- **Actual contribution:** To summarize, our key contributions are: (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** Study Results Table I shows that when the target robots have the same gripper as the source robot, most unseen target robots achieve very high task success rates. (p. 5, IV. STATE-BASED TRANSFER EXPERIMENTS).
- **Explicit failure boundary:** Less robust source policies leave little room for error, while more robust ones tend to retry even if the target robot fails to grasp the object the first time. (p. 5, IV. STATE-BASED TRANSFER EXPERIMENTS).
