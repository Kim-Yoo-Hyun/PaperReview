# Prompting with the Future: Open-World Model Predictive Control with Interactive Digital Twins

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p145.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p145.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, world model, model predictive control, digital twin, VLM, contact-rich manipulation
- Official paper: https://www.roboticsproceedings.org/rss21/p145.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p145.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (11 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 We do not assume access to task-specific training data, in-context ‘examples, or hard-coded motion primitives as used in prior work (20, 27, 13, 25].를 문제로 두고, To validate the effectiveness of our framework, in this section, we design eight real-world manipulation tasks that require 6 DoF control, semantic understanding, and diverse ‘manipulation skills, We compare our approach against ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Open-world robotic manipulation requires robots to perform novel tasks described by free-form language in unsteuctured settings.
- **p. 1 / Abstract - extractive body cue:** While vision-language models (VLMs) offer strong, high-level semantic reasoning, they lack the fine-grained physical insight needed for precise low-level control.
- **p. 1 / Abstract - extractive body cue:** To address this gap, we introduce Prompting with the Future (PWTE), a model predictive control framework that augments VLM-based policies With explicit physics modeling.
- **p. 1 / Abstract - extractive body cue:** PWTF builds an interactive digital {win of the workspace from a quick handheld video scan, enabling prediction of future states under candidate action sequences.
- **p. 1 / Abstract - extractive body cue:** [n= stead of asking the VLM to predict actions or results by reasoning ‘dynamics, the framework simulates diverse possible outcomes, renders them as visual prompts ...
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** We do not assume access to task-specific training data, in-context ‘examples, or hard-coded motion primitives as used in prior work (20, 27, 13, 25].

## Core Idea

- **p. 5 / C. Motion Planning via Simulation-Informed Prompting - extractive body cue:** To validate the effectiveness of our framework, in this section, we design eight real-world manipulation tasks that require 6 DoF control, semantic understanding, and diverse ...
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** Central o our framework is a pre-trained vision-language model (VLM). ‘The model processes an ordered sequence of interleaved text and RGB images and returns a ...
- **p. 3 / A. Construction of Interactive Digital Twins - extractive body cue:** Unlike prior work, which often focuses solely on static reconstruction [40, 24), our method produces dynamic, actionconditioned digital twins by combining mesh-based physical modeling with ...
- **p. 4 / A. Construction of Interactive Digital Twins - extractive body cue:** Given a free-form instrition, our framework first performs high-level planning by generating structured subtasks from multi-view observations.
- **p. 4 / A. Construction of Interactive Digital Twins - extractive body cue:** ‘Through this construction pipeline, we obtain an interactive digital twin where the mesh representation provides physical structure, the Gaussian splatting enables efficient and realistic rendering, ...
- **p. 4 / A. Construction of Interactive Digital Twins - extractive body cue:** Physical simulation: Finally, we integrate a physics simulator 'S [17] equipped with the robot's URDF U to model dynamics lunder interaction, The simulator computes physically ...
- **p. 3 / A. Construction of Interactive Digital Twins - extractive body cue:** AS shown in Figure 2, our construction pipeline consists of two key stages: (1) reconstructing scenes with accurate geometry and visual appearance, and (2) making ...
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** We consider a tabletop setting with ‘one robotic arm. ‘The framework's input consists of a natural language instruction { specifying the task, and an RGB ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We consider a tabletop setting with ‘one robotic arm. ‘The framework's input consists of a natural language instruction { specifying the task, and an RGB video sean v of the scene. ‘The ... | observation, uncertainty/risk estimate와 task command | p. 3 (III. PROBLEM FORMULATION), p. 4 (A. Construction of Interactive Digital Twins) |
| State/latent | consider, tabletop, setting, robotic, framework, input, consists, natural, language, instruction, specifying, task | safe set, recovery state 또는 constraint margin | p. 3 (III. PROBLEM FORMULATION), p. 4 (A. Construction of Interactive Digital Twins), p. 4 (A. Construction of Interactive Digital Twins) |
| Output/action | High-level planning Future observations of sampled actions VLM evaluation Fig. | shielded, recovery 또는 safe action | p. 4 (A. Construction of Interactive Digital Twins), p. 4 (A. Construction of Interactive Digital Twins), p. 5 (C. Motion Planning via Simulation-Informed Prompting) |
| Objective/outcome | decomposition localizes the optimization objective, improving sample efficiency and enhancing planning robustness. | task return과 violation/failure probability | p. 5 (C. Motion Planning via Simulation-Informed Prompting), p. 4 (C. Motion Planning via Simulation-Informed Prompting), p. 3 (III. PROBLEM FORMULATION) |

## Main Claims and Actual Contribution

- **p. 5 / C. Motion Planning via Simulation-Informed Prompting - extractive body cue:** To validate the effectiveness of our framework, in this section, we design eight real-world manipulation tasks that require 6 DoF control, semantic understanding, and diverse ...
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** Central o our framework is a pre-trained vision-language model (VLM). ‘The model processes an ordered sequence of interleaved text and RGB images and returns a ...
- **p. 3 / A. Construction of Interactive Digital Twins - extractive body cue:** Unlike prior work, which often focuses solely on static reconstruction [40, 24), our method produces dynamic, actionconditioned digital twins by combining mesh-based physical modeling with ...
- **p. 4 / A. Construction of Interactive Digital Twins - extractive body cue:** Given a free-form instrition, our framework first performs high-level planning by generating structured subtasks from multi-view observations.
- **p. 4 / A. Construction of Interactive Digital Twins - extractive body cue:** ‘Through this construction pipeline, we obtain an interactive digital twin where the mesh representation provides physical structure, the Gaussian splatting enables efficient and realistic rendering, ...
- **p. 6 / B. Quantitative results - extractive body cue:** As shown in Table Ill, while performance varies across df= ferent tasks due to their diverse requirements, our full method achieves the best results in ...
- **p. 8 / B. Quantitative results - extractive body cue:** Lastly, the CEM process significantly improves sampling efficiency, producing action distributions that better align with the goal, which in general contributes the most to our ...
- **p. 6 / B. Quantitative results - extractive body cue:** PWTF better leverages the reasoning ability of VLM and improves the performance ‘on most of the tasks.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (B. Quantitative results), p. 8 (B. Quantitative results) |
| Embodiment/environment | MOKA [13] chooses the 2D keypoints as intermediate representations for VLM to predict, which are then converted into actions based on the depth information from a depth camera, OpenVLA [25] is a ... | hardware/simulator version and reset protocol | p. 5 (A. Experimental setup), p. 6 (B. Quantitative results) |
| Dataset/benchmark | For each task, we construct five manipulation scenes, featuring randomized object layouts and different distractors. | role, split, size and leakage | p. 5 (A. Experimental setup), p. 6 (B. Quantitative results), p. 5 (A. Experimental setup), p. 6 (B. Quantitative results) |
| Metric | We use the success rate as the evaluation metric. | definition, denominator, direction and uncertainty | p. 5 (A. Experimental setup), p. 5 (B. Quantitative results), p. 8 (B. Quantitative results) |
| Baseline/ablation | We adopt GPT-4o [1] for both our method and the baselines. | fair input/data/compute/action matching | p. 5 (A. Experimental setup), p. 5 (B. Quantitative results), p. 6 (B. Quantitative results) |

## Explicit Limitations and Failure Boundary

- **p. 5 / A. Experimental setup - extractive body cue:** A task is considered a failure if the robot causes imeversible results or if the maximum step budget or time limit is reached. ‘The task ...
- **p. 5 / B. Quantitative results - extractive body cue:** Since Voxposer and MOKA rely on ‘open-vocabulary detectors to detect objects before manipula tion, they fail when the perception system cannot recognize specific object parts, ...
- **p. 8 / B. Quantitative results - extractive body cue:** The failure cases can be categorized into four groups:
- **p. 8 / B. Quantitative results - extractive body cue:** Our main failure cases can be divided into four categories.
- **p. 6 / B. Quantitative results - extractive body cue:** We show the action ‘optimization results of one planning step in subtask "wipe the spilled tea", Our digital twin could simulate diverse results with accurate ...
- **p. 6 / B. Quantitative results - extractive body cue:** We visualize the action optimization process for a single planning step in the "clean up" task in Figure 4, Initially, the digital twin simulates a ...

## Why Read It

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 We do not assume access to task-specific training data, in-context ‘examples, or hard-coded motion primitives as used in prior work (20, 27, 13, 25].를 문제로 두고, To validate the effectiveness of our framework, in this section, we design eight real-world manipulation tasks that require 6 DoF control, semantic understanding, and diverse ‘manipulation skills, We compare our approach against ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (III. PROBLEM FORMULATION), p. 4 (A. Construction of Interactive Digital Twins), p. 3 (A. Construction of Interactive Digital Twins), p. 3 (III. PROBLEM FORMULATION), p. 4 (A. Construction of Interactive Digital Twins), p. 5 (C. Motion Planning via Simulation-Informed Prompting) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
