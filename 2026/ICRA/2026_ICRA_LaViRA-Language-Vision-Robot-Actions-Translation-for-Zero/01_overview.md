# LaViRA: Language-Vision-Robot Actions Translation for Zero-Shot Vision Language Navigation in Continuous Environments

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html.
> PDF retrieval source: https://arxiv.org/pdf/2510.19655. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Robotics, Navigation
- Official paper: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html
- Full-text retrieval: https://arxiv.org/pdf/2510.19655
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 To bridge the gap to the real world, Vision-and-Language Navigation in Continuous Environments (VLN-CE) [2] was introduced, removing the reliance on connectivity graphs and forcing agents to contend를 문제로 두고, Our contributions are as follows: • We propose a general action decomposition strategy for zero-shot VLN-CE that separates navigation into language-level planning, vision-level grounding, and robot-level control, enabling flexible integ ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Zero-shot Vision-and-Language Navigation in Continuous Environments (VLN-CE) requires an agent to navigate unseen environments based on natural language instructions without any prior training.
- **p. 1 / Abstract - extractive body cue:** Current methods face a critical trade-off: either rely on environment-specific waypoint predictors that limit scene generalization, or underutilize the reasoning capabilities of large models during ...
- **p. 1 / Abstract - extractive body cue:** We introduce LaViRA, a simple yet effective zero-shot framework that addresses this dilemma by decomposing action into a coarse-to-fine hierarchy: Language Action for high-level planning, ...
- **p. 1 / Abstract - extractive body cue:** This modular decomposition allows us to leverage the distinct strengths of different scales of Multimodal Large Language Models (MLLMs) at each stage, creating a system ...
- **p. 1 / Abstract - extractive body cue:** LaViRA significantly outperforms existing state-of-the-art methods on the VLN-CE benchmark, demonstrating superior generalization capabilities in unseen environments, while maintaining transparency and efficiency for real-world deployment.
- **p. 1 / I. INTRODUCTION - extractive body cue:** To bridge the gap to the real world, Vision-and-Language Navigation in Continuous Environments (VLN-CE) [2] was introduced, removing the reliance on connectivity graphs and forcing ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Vision-and-Language Navigation (VLN) presents the challenge of grounding natural language instructions within visual observations to enable an embodied agent to navigate through previously unseen environments ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our contributions are as follows: • We propose a general action decomposition strategy for zero-shot VLN-CE that separates navigation into language-level planning, vision-level grounding, and ...
- **p. 3 / III. PROPOSED METHOD - extractive body cue:** Language Action: High-Level Planning The first stage of our framework addresses the question: Where should I generally go next?
- **p. 3 / III. PROPOSED METHOD - extractive body cue:** To address this, our method decomposes the navigation process into a sequence of three hierarchical actions: a high-level directional plan (Language Action), the grounding of ...
- **p. 4 / III. PROPOSED METHOD - extractive body cue:** (Right) The prompt for the Vision Action model, which uses the output from the first stage to ground the decision in a specific visual target.
- **p. 3 / III. PROPOSED METHOD - extractive body cue:** Specifically, the model receives three types of input: • Language Instruction I: The given natural language instruction provided at the start of the task. • ...
- **p. 4 / III. PROPOSED METHOD - extractive body cue:** It outputs a Vision Action Avis t in a structured format containing a bounding box and its description.
- **p. 5 / III. PROPOSED METHOD - extractive body cue:** A low-level controller then executes this path with local obstacle avoidance.
- **p. 5 / III. PROPOSED METHOD - extractive body cue:** This deterministic final step grounds the reasoning chain in physical action, ensuring interpretability and making the system adaptable to different robot platforms by simply swapping ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Specifically, the model receives three types of input: • Language Instruction I: The given natural language instruction provided at the start of the task. • Current Observation Ot: A set of four ... | camera/depth stream, pose, map와 language goal | p. 3 (III. PROPOSED METHOD), p. 2 (I. INTRODUCTION) |
| State/latent | Specifically, model, receives, three, types, input, Language, Instruction, given, natural, provided, start | robot pose, free-space/semantic map와 local goal | p. 3 (III. PROPOSED METHOD), p. 2 (I. INTRODUCTION), p. 4 (III. PROPOSED METHOD) |
| Output/action | 1) Language Action: A powerful MLLM acts as a highlevel planner, analyzing the instruction, history, and current observation to produce a coarse strategic decision, such as which general direction to head, whether ... | collision-free trajectory 또는 velocity command | p. 2 (I. INTRODUCTION), p. 4 (III. PROPOSED METHOD), p. 2 (I. INTRODUCTION) |
| Objective/outcome | This explicit reasoning step forces the model to track its progress against the overall instruction. | goal reach, safety, localization error와 replanning latency | p. 3 (III. PROPOSED METHOD), p. 3 (III. PROPOSED METHOD), p. 4 (III. PROPOSED METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our contributions are as follows: • We propose a general action decomposition strategy for zero-shot VLN-CE that separates navigation into language-level planning, vision-level grounding, and ...
- **p. 3 / III. PROPOSED METHOD - extractive body cue:** Language Action: High-Level Planning The first stage of our framework addresses the question: Where should I generally go next?
- **p. 3 / III. PROPOSED METHOD - extractive body cue:** To address this, our method decomposes the navigation process into a sequence of three hierarchical actions: a high-level directional plan (Language Action), the grounding of ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Real-world experiment examples. LaViRA guides a Unitree Go1 quadruped (top) and an Agilex Cobot Magic wheeled robot (bottom) in an office. The visualization ...
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** LaViRA significantly outperforms all previous zero-shot methods.
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** We use standard VLN metrics: Navigation Error (NE), the final distance to goal; Success Rate (SR), our primary metric for stopping within 3m; Oracle Success ...
- **p. 6 / IV. SIMULATION EXPERIMENTS - extractive body cue:** Our full framework outperforms the latter by 14.4 points, confirming the effectiveness of coarse-to-fine decomposition.
- **p. 6 / IV. SIMULATION EXPERIMENTS - extractive body cue:** Removing the highlevel planner ("w/o LA") yields 4.4% SPL, while removing the perceptual grounding module ("w/o VA") achieves 13.9% SPL.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 5 (IV. SIMULATION EXPERIMENTS) |
| Embodiment/environment | We use the Habitat simulator [34] with the VLN-CE dataset [2], which extends the R2R benchmark from Matterport3D (MP3D) [10] for continuous navigation. | hardware/simulator version and reset protocol | p. 5 (IV. SIMULATION EXPERIMENTS), p. 6 (V. REAL-WORLD EXPERIMENTS) |
| Dataset/benchmark | Following recent zero-shot works [3], [4], we report results on a standard 100-episode subset from the validation unseen split. | role, split, size and leakage | p. 5 (IV. SIMULATION EXPERIMENTS), p. 6 (V. REAL-WORLD EXPERIMENTS), p. 5 (IV. SIMULATION EXPERIMENTS), p. 6 (V. REAL-WORLD EXPERIMENTS) |
| Metric | We use standard VLN metrics: Navigation Error (NE), the final distance to goal; Success Rate (SR), our primary metric for stopping within 3m; Oracle Success Rate (OSR), SR if stopping at the ... | definition, denominator, direction and uncertainty | p. 5 (IV. SIMULATION EXPERIMENTS), p. 6 (IV. SIMULATION EXPERIMENTS), p. 6 (IV. SIMULATION EXPERIMENTS) |
| Baseline/ablation | Fig. 5: Real-world experiment examples. LaViRA guides a Unitree Go1 quadruped (top) and an Agilex Cobot Magic wheeled robot (bottom) in an office. The visualization shows the third-person view of the robot's ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 5 (IV. SIMULATION EXPERIMENTS), p. 5 (IV. SIMULATION EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / VI. CONCLUSION - extractive body cue:** Its performance ceiling is bounded by off-the-shelf models, as seen in failures on ambiguous instructions and large-area grounding.
- **p. 7 / VI. CONCLUSION - extractive body cue:** (Right) Failure cases visualization: Language Action misjudges direction due to ambiguous instructions; Vision Action selects the wrong region despite correct target description; simulation reconstruction errors ...
- **p. 6 / IV. SIMULATION EXPERIMENTS - extractive body cue:** Qualitative Analysis To offer qualitative insights into LaViRA's decisionmaking, Figure 4 shows a successful navigation run and common failures.
- **p. 6 / IV. SIMULATION EXPERIMENTS - extractive body cue:** The failure cases illustrate three common errors: (1) A Language Action error from ambiguous instructions, e.g., failing to identify the correct door when multiple doors ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: The LaViRA Pipeline. Our framework decomposes navigation into three sequential stages. (1) Language Action: A large MLLM processes the instruction, history, and current ...
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** Low standard deviations across runs highlight the framework's robustness and stability, a key advantage for real-world applications.

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 To bridge the gap to the real world, Vision-and-Language Navigation in Continuous Environments (VLN-CE) [2] was introduced, removing the reliance on connectivity graphs and forcing agents to contend를 문제로 두고, Our contributions are as follows: • We propose a general action decomposition strategy for zero-shot VLN-CE that separates navigation into language-level planning, vision-level grounding, and robot-level control, enabling flexible integ ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. PROPOSED METHOD), p. 3 (III. PROPOSED METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
