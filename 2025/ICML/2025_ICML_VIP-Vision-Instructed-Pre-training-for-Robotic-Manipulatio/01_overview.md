# VIP: Vision Instructed Pre-training for Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=ccUNMIbpcf.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/168016. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics, Imitation Learning
- Official paper: https://openreview.net/forum?id=ccUNMIbpcf
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/168016
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 1, the text instructed policy fails to concentrate on the green block specified in the text instruction, and the robot hand often grasps a block in a false color.를 문제로 두고, To specify the manipulation procedures clearly while maintaining an acceptable computational burden, we propose to represent the intermediate action information with sparse point flows.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The effectiveness of scaling up training data in robotic manipulation is still limited.
- **p. 1 / Abstract - extractive body cue:** A primary challenge in manipulation is the tasks are diverse, and the trained policy would be confused if the task targets are not specified clearly.
- **p. 1 / Abstract - extractive body cue:** Existing works primarily rely on text instruction to describe targets.
- **p. 1 / Abstract - extractive body cue:** However, we reveal that current robotic data cannot train policies to understand text instruction effectively, and vision is much more comprehensible.
- **p. 1 / Abstract - extractive body cue:** Therefore, we introduce utilizing vision instruction to specify targets.
- **p. 1 / 1. Introduction - extractive body cue:** 1, the text instructed policy fails to concentrate on the green block specified in the text instruction, and the robot hand often grasps a block ...
- **p. 1 / 1. Introduction - extractive body cue:** However, we find that existing manipulation data is not diverse sufficiently to train a policy to own this capability, which demands millions of image-text pairs ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To specify the manipulation procedures clearly while maintaining an acceptable computational burden, we propose to represent the intermediate action information with sparse point flows.
- **p. 3 / 3.1. Vision Intructed Pre-training - extractive body cue:** A data sample for robotic manipulation pre-training consists of two parts, a video sequence V = {I1, I2, · · · , IT } and ...
- **p. 5 / 3.3. Vision Instruction after Pre-train - extractive body cue:** 2, the vision instruction in pretraining consists of two parts, the future frame and sparse point flows.
- **p. 5 / 3.3. Vision Instruction after Pre-train - extractive body cue:** To bridge this gap, we propose to replace the future frame in pre-training as the cropped image region of the object to manipulate during fine-tuning ...
- **p. 2 / 1. Introduction - extractive body cue:** Additionally, this design enables us to specify the object manipulation order dynamically.
- **p. 4 / 3.1. Vision Intructed Pre-training - extractive body cue:** In VIP, we first transform I1 and It as visual features F1 and Ft by a shared encoder like ResNet (He et al., 2016) in ...
- **p. 5 / 3.3. Vision Instruction after Pre-train - extractive body cue:** First of all, the future observation ot+1 is affected by both the current state st and action at.
- **p. 4 / 3.1. Vision Intructed Pre-training - extractive body cue:** F1, FT , and Fp are input to the action decoder (e.g., Transformer decoders or diffusion heads) of the pre-trained policy to produce T action ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | A natural idea of using vision instruction is feeding the policy with future images besides the current observation, and the policy is optimized to predict correct actions that make the robot reach ... | image/video, language instruction, proprioception과 history | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| State/latent | natural, idea, vision, instruction, feeding, policy, future, images, besides, current, observation, optimized | language-grounded task state와 action-policy context | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Output/action | These paradigms expect that the trained policy understands what the green block is in the input image and predicts the action sequence of picking it up. | continuous action, pose 또는 action chunk | p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.1. Vision Intructed Pre-training) |
| Objective/outcome | We optimize the pre-trained policy by minimizing a loss L constructed based on {at}T t=1, {σt}T t=1, and {¯at}T t=1 as: L= 1 T T X t=1 ( √ 2/at -¯at/ σt ... | instruction following, task success, generalization과 latency | p. 4 (3.1. Vision Intructed Pre-training), p. 4 (3.2. Sparse Point Flow), p. 5 (3.2. Sparse Point Flow) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To specify the manipulation procedures clearly while maintaining an acceptable computational burden, we propose to represent the intermediate action information with sparse point flows.
- **p. 3 / 3.1. Vision Intructed Pre-training - extractive body cue:** A data sample for robotic manipulation pre-training consists of two parts, a video sequence V = {I1, I2, · · · , IT } and ...
- **p. 5 / 3.3. Vision Instruction after Pre-train - extractive body cue:** 2, the vision instruction in pretraining consists of two parts, the future frame and sparse point flows.
- **p. 5 / 3.3. Vision Instruction after Pre-train - extractive body cue:** To bridge this gap, we propose to replace the future frame in pre-training as the cropped image region of the object to manipulate during fine-tuning ...
- **p. 2 / 1. Introduction - extractive body cue:** Additionally, this design enables us to specify the object manipulation order dynamically.
- **p. 8 / 4.3. Method Analysis - extractive body cue:** As shown, all these designs improve the success rates of VIRT on the three evaluated tasks significantly.
- **p. 8 / 4.3. Method Analysis - extractive body cue:** In addition, we can find that increasing the fine-tuning data volume boosts execution success rates more significantly, which is because the fine-tuning data aligns better ...
- **p. 7 / 4.1. VIP Effectiveness - extractive body cue:** Comparing the various policies, it is found that VIRT achieves the best performance, and its inference speed is also promising.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4.3. Method Analysis), p. 8 (4.3. Method Analysis) |
| Embodiment/environment | A Franka Panda robotic arm is deployed in each simulation environment to manipulate objects, with four cameras strategically positioned to observe the scene from various angles, including three peripheral views and one ... | hardware/simulator version and reset protocol | p. 6 (4. Experiments), p. 5 (4. Experiments) |
| Dataset/benchmark | 7, the three real-robot tasks include Pour Blueberries, Open the Lid, and Clean the Table. | role, split, size and leakage | p. 6 (4. Experiments), p. 5 (4. Experiments), p. 6 (4. Experiments), p. 7 (4.1. VIP Effectiveness) |
| Metric | These policies are tested for 100 times on each task, and we report their success rates as well as inference speeds (test on a Table 2. | definition, denominator, direction and uncertainty | p. 7 (4.1. VIP Effectiveness), p. 7 (4.1. VIP Effectiveness), p. 8 (4.3. Method Analysis) |
| Baseline/ablation | Among them, ConvMLP is the most commonly adopted baseline, which first extracts image feature using convolutional neural network (CNN) and then regresses actions based on the extracted feature. | fair input/data/compute/action matching | p. 7 (4.1. VIP Effectiveness), p. 4 (Figure/Table caption), p. 7 (4.1. VIP Effectiveness) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4.3. Method Analysis - extractive body cue:** Robustness analysis of VIRT to different disturbances, e.g., brightness change, vision noise, and image blur.
- **p. 7 / 4.1. VIP Effectiveness - extractive body cue:** For ConvMLP, its primary problem is its output head is a naive MLP, which is fast but fails to estimate actions precisely.
- **p. 8 / 4.3. Method Analysis - extractive body cue:** This part analyzes the robustness of VIRT to different unseen environment disturbances.
- **p. 7 / 4.2. Instruction Comparison - extractive body cue:** According to the results, we can find that solely using a future image or sparse point flows does not lead to effective pre-training due to ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 1, the text instructed policy fails to concentrate on the green block specified in the text instruction, and the robot hand often grasps a block in a false color.를 문제로 두고, To specify the manipulation procedures clearly while maintaining an acceptable computational burden, we propose to represent the intermediate action information with sparse point flows.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Vision Intructed Pre-training), p. 5 (3.3. Vision Instruction after Pre-train) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
