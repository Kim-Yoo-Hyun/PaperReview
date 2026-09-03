# Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Li_Object-Centric_Prompt-Driven_Vision-Language-Action_Model_for_Robotic_Manipulation_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_Object-Centric_Prompt-Driven_Vision-Language-Action_Model_for_Robotic_Manipulation_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, prompting, Robotics
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Li_Object-Centric_Prompt-Driven_Vision-Language-Action_Model_for_Robotic_Manipulation_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_Object-Centric_Prompt-Driven_Vision-Language-Action_Model_for_Robotic_Manipulation_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 In contrast, RT-Trajectory [20] (Figure1.(c)) illustrates the entire movement path of the endeffector, which helps bridge the gap between task components and enhances generalization.를 문제로 두고, In summary, our contributions are as follows: • 1) We propose employing a sequence of key-frames presented with prompts to explicitly convey the task objectives in both low-level action and high-level planning. ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In robotic, task goals can be conveyed through various modalities, such as language, goal images, and goal videos.
- **p. 1 / Abstract - extractive body cue:** However, natural language can be ambiguous, while images or videos may offer overly detailed specifications.
- **p. 1 / Abstract - extractive body cue:** To tackle these challenges, we introduce CrayonRobo that leverages comprehensive multi-modal prompts that explicitly convey both low-level actions and high-level planning in a simple manner.
- **p. 1 / Abstract - extractive body cue:** Specifically, for each key-frame in the task sequence, our method allows for manual or automatic generation of simple and expressive 2D visual prompts overlaid on ...
- **p. 1 / Abstract - extractive body cue:** These prompts represent the required task goals, such as the end-effector pose and the desired movement direction after contact.
- **p. 1 / 1. Introduction - extractive body cue:** In contrast, RT-Trajectory [20] (Figure1.(c)) illustrates the entire movement path of the endeffector, which helps bridge the gap between task components and enhances generalization.
- **p. 1 / 1. Introduction - extractive body cue:** Language instructions [2, 23, 24, 31, 33, 38, 41, 45, 46, 56] can be ambiguous and brief, making it challenging for the robot to understand ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are as follows: • 1) We propose employing a sequence of key-frames presented with prompts to explicitly convey the task objectives ...
- **p. 2 / 1. Introduction - extractive body cue:** Our experimental setup includes a diverse range of manipulation tasks, both familiar and novel, where our method achieves a promising success rate in manipulation.
- **p. 4 / 3.3.2. Policy Learning - extractive body cue:** To establish an explicit connection between the input 2D directional prompt and the output 3D directions, we introduce a projection loss designed to guide their ...
- **p. 1 / 1. Introduction - extractive body cue:** Since key-frames represent important or bottleneck steps of the gripper during the task execution [18, 19, 26, 46, 58], we propose CrayonRobo, an approach that ...
- **p. 3 / 3.3.2. Policy Learning - extractive body cue:** This gradual progression enables the model to develop a deeper understanding of the physical significance 27640
- **p. 4 / 3.3.2. Policy Learning - extractive body cue:** Therefore, we introduce the following losses to guide the policy training: Text Supervision Loss L푇: This loss ensures the effective alignment of the model's visual ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** The objective of the model is to generate an action 푎0 = (푎푝′ 0 , 푎푍 0 , 푎푌 0 , 푎푀 0 ), where ...
- **p. 3 / 3.3.1. Model Architecture - extractive body cue:** Observing the robust language understanding and visual processing capabilities of Vision Language Action Models (VLAs) and inspired by their applications in prior robotic manipulation tasks ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given the visual and language input, the model outputs the predicted action 푎0. | image/video, language instruction, proprioception과 history | p. 5 (3.4.1. Model Inference), p. 4 (3.3.2. Policy Learning) |
| State/latent | Given, visual, language, input, model, outputs, predicted, action, Therefore, introduce, following, losses | language-grounded task state와 action-policy context | p. 5 (3.4.1. Model Inference), p. 4 (3.3.2. Policy Learning), p. 2 (1. Introduction) |
| Output/action | Therefore, we introduce the following losses to guide the policy training: Text Supervision Loss L푇: This loss ensures the effective alignment of the model's visual and linguistic input, making sure it can ... | continuous action, pose 또는 action chunk | p. 4 (3.3.2. Policy Learning), p. 2 (1. Introduction), p. 4 (3.3.2. Policy Learning) |
| Objective/outcome | The aforementioned losses are trained simultaneously under the total objective function: L = 휆1 ∗L푇+휆2 ∗L푂+휆3 ∗L푃. | instruction following, task success, generalization과 latency | p. 4 (3.3.2. Policy Learning), p. 4 (3.3.2. Policy Learning), p. 3 (3.1. Problem Formulation) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are as follows: • 1) We propose employing a sequence of key-frames presented with prompts to explicitly convey the task objectives ...
- **p. 2 / 1. Introduction - extractive body cue:** Our experimental setup includes a diverse range of manipulation tasks, both familiar and novel, where our method achieves a promising success rate in manipulation.
- **p. 4 / 3.3.2. Policy Learning - extractive body cue:** To establish an explicit connection between the input 2D directional prompt and the output 3D directions, we introduce a projection loss designed to guide their ...
- **p. 1 / 1. Introduction - extractive body cue:** Since key-frames represent important or bottleneck steps of the gripper during the task execution [18, 19, 26, 46, 58], we propose CrayonRobo, an approach that ...
- **p. 3 / 3.3.2. Policy Learning - extractive body cue:** This gradual progression enables the model to develop a deeper understanding of the physical significance 27640
- **p. 6 / 4.3. Ablation Study - extractive body cue:** Beginning with Ex1, where only a 2D position prompt is provided, the model achieves impressive performance with scores of 0.42/0.37.
- **p. 8 / 4.3.2. Tolerance Analysis of Prompt Noise - extractive body cue:** The results, shown in Figure 5, indicate that with 10% and 20% noise, our method achieves performance levels comparable to those of the noise-free scenario.
- **p. 6 / 4.2. Comparisons with Baselines - extractive body cue:** For automatically generated prompts, the results are 0.64/0.62 on seen and unseen tasks, still outperforming the baselines.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4.3. Ablation Study), p. 8 (4.3.2. Tolerance Analysis of Prompt Noise) |
| Embodiment/environment | Simulator visualizations are shown in the left of Figure 4, illustrating the prompt input, the robot's contact state with the object, and the final state after movement. | hardware/simulator version and reset protocol | p. 6 (4.2. Comparisons with Baselines), p. 6 (4.1. Setup Details) |
| Dataset/benchmark | We conduct experiments involving interaction with various real-world objects without additional sim-to-real finetuning. | role, split, size and leakage | p. 6 (4.2. Comparisons with Baselines), p. 6 (4.1. Setup Details), p. 8 (4.4. Real-world Experiment), p. 8 (4.4. Real-world Experiment) |
| Metric | We utilize the manipulation success rate to assess the effectiveness of the manipulation, calculated as the ratio of successfully manipulated samples to the total number of test samples. | definition, denominator, direction and uncertainty | p. 6 (4.1. Setup Details), p. 8 (4.3. Ablation Study), p. 8 (4.4. Real-world Experiment) |
| Baseline/ablation | For automatically generated prompts, the results are 0.64/0.62 on seen and unseen tasks, still outperforming the baselines. | fair input/data/compute/action matching | p. 6 (4.2. Comparisons with Baselines), p. 7 (4.3. Ablation Study), p. 6 (4.2. Comparisons with Baselines) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** Limitation: As for the limitation, though our method can not directly avoid obstacles, we can incorporate collision-free motion planner library like curobo [48] to realize ...
- **p. 8 / 4.3.2. Tolerance Analysis of Prompt Noise - extractive body cue:** Ablation experiments regarding the effectiveness of each loss and failure case analysis are shown in Appendix.5 and Appendix.6.
- **p. 6 / 4.2. Comparisons with Baselines - extractive body cue:** However, our results demonstrate the robustness of CrayonRobo in handling such input inaccuracies.
- **p. 6 / 4.2. Comparisons with Baselines - extractive body cue:** This is because the model is trained to manipulate objects, it can, to some extent, correct the noise in the prompts.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 In contrast, RT-Trajectory [20] (Figure1.(c)) illustrates the entire movement path of the endeffector, which helps bridge the gap between task components and enhances generalization.를 문제로 두고, In summary, our contributions are as follows: • 1) We propose employing a sequence of key-frames presented with prompts to explicitly convey the task objectives in both low-level action and high-level planning. ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 4 (3.3.2. Policy Learning), p. 3 (3.1. Problem Formulation), p. 3 (3.3.1. Model Architecture), p. 5 (3.4.1. Model Inference) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
