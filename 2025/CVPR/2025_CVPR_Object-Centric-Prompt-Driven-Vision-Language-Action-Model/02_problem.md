# Problem - Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Li_Object-Centric_Prompt-Driven_Vision-Language-Action_Model_for_Robotic_Manipulation_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_Object-Centric_Prompt-Driven_Vision-Language-Action_Model_for_Robotic_Manipulation_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction)): In contrast, RT-Trajectory [20] (Figure1.(c)) illustrates the entire movement path of the endeffector, which helps bridge the gap between task components and enhances generalization.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** In robotic, task goals can be conveyed through various modalities, such as language, goal images, and goal videos.
- **p. 1 / Abstract - extractive body cue:** However, natural language can be ambiguous, while images or videos may offer overly detailed specifications.
- **p. 1 / Abstract - extractive body cue:** To tackle these challenges, we introduce CrayonRobo that leverages comprehensive multi-modal prompts that explicitly convey both low-level actions and high-level planning in a simple manner.
- **p. 1 / Abstract - extractive body cue:** Specifically, for each key-frame in the task sequence, our method allows for manual or automatic generation of simple and expressive 2D visual prompts overlaid on ...
- **p. 1 / Abstract - extractive body cue:** These prompts represent the required task goals, such as the end-effector pose and the desired movement direction after contact.
- **p. 1 / 1. Introduction - extractive body cue:** In contrast, RT-Trajectory [20] (Figure1.(c)) illustrates the entire movement path of the endeffector, which helps bridge the gap between task components and enhances generalization.
- **p. 1 / 1. Introduction - extractive body cue:** Language instructions [2, 23, 24, 31, 33, 38, 41, 45, 46, 56] can be ambiguous and brief, making it challenging for the robot to understand ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | In contrast, RT-Trajectory [20] (Figure1.(c)) illustrates the entire movement path of the endeffector, which helps bridge the gap between task components and ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Given the visual and language input, the model outputs the predicted action 푎0. | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | Given, visual, language, input, model, outputs, predicted, action, Therefore, introduce | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Execution, Input, effector, pose, z-axis, y-axis, contact, point | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Given, visual, language, input, model, outputs, predicted, action, Therefore, introduce | p. 5 (3.4.1. Model Inference), p. 4 (3.3.2. Policy Learning), p. 2 (1. Introduction) |
| Decision / output variable | action, pose, option or chunk a; body terms: summary, contributions, follows, employing, sequence, key-frames, presented, prompts | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.3.2. Policy Learning) |
| Objective / loss / cost | policy/action modeling objective; cue terms: aforementioned, losses, trained, simultaneously, under, total, objective, function | p. 4 (3.3.2. Policy Learning), p. 3 (3.1. Problem Formulation), p. 4 (3.3.2. Policy Learning) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3.1. Problem Formulation), p. 3 (3.3.2. Policy Learning), p. 6 (3.4.2. Interaction Strategy) |
| Success / guarantee | instruction-conditioned task success | p. 6 (4.1. Setup Details), p. 8 (4.3. Ablation Study), p. 8 (4.4. Real-world Experiment) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** Language instructions [2, 23, 24, 31, 33, 38, 41, 45, 46, 56] can be ambiguous and brief, making it challenging for the robot to understand ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.3.2. Policy Learning), p. 1 (1. Introduction), p. 3 (3.3.2. Policy Learning)): In summary, our contributions are as follows: • 1) We propose employing a sequence of key-frames presented with prompts to explicitly convey the task objectives in both low-level action and ...

- **p. 2 / 1. Introduction - extractive body cue:** Our experimental setup includes a diverse range of manipulation tasks, both familiar and novel, where our method achieves a promising success rate in manipulation.
- **p. 4 / 3.3.2. Policy Learning - extractive body cue:** To establish an explicit connection between the input 2D directional prompt and the output 3D directions, we introduce a projection loss designed to guide their ...
- **p. 1 / 1. Introduction - extractive body cue:** Since key-frames represent important or bottleneck steps of the gripper during the task execution [18, 19, 26, 46, 58], we propose CrayonRobo, an approach that ...
- **p. 3 / 3.3.2. Policy Learning - extractive body cue:** This gradual progression enables the model to develop a deeper understanding of the physical significance 27640

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Limitation: As for the limitation, though our method can not directly avoid obstacles, we can incorporate collision-free motion ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Ablation experiments regarding the effectiveness of each loss and failure case analysis are shown in Appendix.5 and Appendix.6. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | However, our results demonstrate the robustness of CrayonRobo in handling such input inaccuracies. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | This is because the model is trained to manipulate objects, it can, to some extent, correct the noise ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (3.4.1. Model Inference), p. 4 (3.3.2. Policy Learning), p. 2 (1. Introduction), p. 4 (3.3.2. Policy Learning). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), interface p. 5 (3.4.1. Model Inference), p. 4 (3.3.2. Policy Learning), p. 2 (1. Introduction), p. 4 (3.3.2. Policy Learning), objective p. 4 (3.3.2. Policy Learning), p. 3 (3.1. Problem Formulation), p. 4 (3.3.2. Policy Learning).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
