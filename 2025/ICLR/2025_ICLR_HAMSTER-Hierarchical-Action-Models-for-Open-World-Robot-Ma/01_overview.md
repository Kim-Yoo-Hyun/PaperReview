# HAMSTER: Hierarchical Action Models for Open-World Robot Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (29 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=h7aQxzKbq6.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/114802. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics, Reinforcement Learning
- Official paper: https://openreview.net/forum?id=h7aQxzKbq6
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/114802
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (29 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 A line of prior work (Brohan et al., 2023a; Kim et al., 2024; Black et al., 2024) builds open-world vision-language-action models (VLAs) by finetuning off-the-shelf pretrained VLMs to directly produce robot actions.를 문제로 두고, It is important to note that while we are certainly not the first to propose hierarchical VLA models (Gu et al., 2023; Nasiriany et al., 2024a), we propose the novel insight that ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Large foundation models have shown strong open-world generalization to complex problems in vision and language, but similar levels of generalization have yet to be achieved ...
- **p. 1 / ABSTRACT - extractive body cue:** One fundamental challenge is the lack of robotic data, which are typically obtained through expensive on-robot operation.
- **p. 1 / ABSTRACT - extractive body cue:** A promising remedy is to leverage cheaper, "off-domain" data such as action-free videos, handdrawn sketches or simulation data.
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we posit that hierarchical visionlanguage-action (VLA) models can be more effective in utilizing off-domain data than standard monolithic VLA models that directly ...
- **p. 1 / ABSTRACT - extractive body cue:** In particular, we study a class of hierarchical VLA models, where the high-level VLM is finetuned to produce a coarse 2D path indicating the desired ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** A line of prior work (Brohan et al., 2023a; Kim et al., 2024; Black et al., 2024) builds open-world vision-language-action models (VLAs) by finetuning off-the-shelf ...
- **p. 5 / 3 BACKGROUND - extractive body cue:** The primary advantages of finetuning such a hierarchical VLM that produces intermediate representations as opposed to directly producing actions a with a monolithic model (Kim ...

## Core Idea

- **p. 3 / 1 INTRODUCTION - extractive body cue:** It is important to note that while we are certainly not the first to propose hierarchical VLA models (Gu et al., 2023; Nasiriany et al., ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To this end, we propose a hierarchical architecture for VLAs, HAMSTER (Hierarchical Action Models with SeparaTEd Path Representations), where large fine-tuned VLMs are connected to ...
- **p. 5 / 3 BACKGROUND - extractive body cue:** It consists of two interconnected models: first, a higher-level VLM that is finetuned on large-scale, off-domain data to produce intermediate 2D path guidance (detailed in ...
- **p. 6 / 3 BACKGROUND - extractive body cue:** A sample consists of a prompt z like Locate object between the marked items, an input image img and answer ans like [(0.25, 0.11), (0.22, ...
- **p. 6 / 3 BACKGROUND - extractive body cue:** This dataset consists of data automatically generated in simulation and collected from existing real-world datasets; its diverse tasks enable the HAMSTER VLM to reason about ...
- **p. 20 / B.1 VLM IMPLEMENTATION DETAILS - extractive body cue:** We condition the model on an image and the prompt, except when training on Pixel Point Prediction data (i.e., from Robopoint (Yuan et al., 2024b)) ...
- **p. 20 / B.2 LOW-LEVEL POLICY TRAINING DETAILS - extractive body cue:** For low-level policy training, we train the policies on ground truth paths constructed by projecting trajectory end-effector points to the camera image.
- **p. 21 / B.2 LOW-LEVEL POLICY TRAINING DETAILS - extractive body cue:** This is likely due to 3D-DA's visual attention mechanism which cross attends CLIP language token embeddings with CLIP visual features, therefore detailed language instructions are ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Imitation learning trains a policy πθ(a / s, o, z) from expert demonstrations, where s denotes proprioceptive inputs, o includes perceptual observations (e.g., RGB images, depth), and z provides task instructions. | image/video, language instruction, proprioception과 history | p. 4 (3 BACKGROUND), p. 1 (1 INTRODUCTION) |
| State/latent | Imitation, learning, trains, policy, expert, demonstrations, where, denotes, proprioceptive, inputs, includes, perceptual | language-grounded task state와 action-policy context | p. 4 (3 BACKGROUND), p. 1 (1 INTRODUCTION), p. 7 (3 BACKGROUND) |
| Output/action | These VLA models, which we refer to in this work as monolithic VLA models, rely crucially on large robotics datasets, complete with on-robot observations, e.g., images and proprioceptive states, and actions. | continuous action, pose 또는 action chunk | p. 1 (1 INTRODUCTION), p. 7 (3 BACKGROUND), p. 5 (3 BACKGROUND) |
| Objective/outcome | In simulated experiments in Colosseum, no changes were needed. | instruction following, task success, generalization과 latency | p. 21 (B.2 LOW-LEVEL POLICY TRAINING DETAILS), p. 21 (B.2 LOW-LEVEL POLICY TRAINING DETAILS), p. 20 (B.1 VLM IMPLEMENTATION DETAILS) |

## Main Claims and Actual Contribution

- **p. 3 / 1 INTRODUCTION - extractive body cue:** It is important to note that while we are certainly not the first to propose hierarchical VLA models (Gu et al., 2023; Nasiriany et al., ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To this end, we propose a hierarchical architecture for VLAs, HAMSTER (Hierarchical Action Models with SeparaTEd Path Representations), where large fine-tuned VLMs are connected to ...
- **p. 5 / 3 BACKGROUND - extractive body cue:** It consists of two interconnected models: first, a higher-level VLM that is finetuned on large-scale, off-domain data to produce intermediate 2D path guidance (detailed in ...
- **p. 6 / 3 BACKGROUND - extractive body cue:** A sample consists of a prompt z like Locate object between the marked items, an input image img and answer ans like [(0.25, 0.11), (0.22, ...
- **p. 6 / 3 BACKGROUND - extractive body cue:** This dataset consists of data automatically generated in simulation and collected from existing real-world datasets; its diverse tasks enable the HAMSTER VLM to reason about ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Real world results demonstrate HAMSTER general- izes to better to novel camera views (see Fig.Figure 6). We ran 10 trails and report averaged ...
- **p. 25 / Figure/Table caption - extractive body cue:** Table 5: Ranking-based human evaluation of different VLMs, averaged across various real-world evaluation tasks. Results indicate that HAMSTER including simulation data is most effective since ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Overview of HAMSTER, VLAs and "smaller" imitation learning methods. HAMSTER's hierarchi- cal design results in better generalization with a small amount of in-domain ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (Figure/Table caption), p. 25 (Figure/Table caption) |
| Embodiment/environment | Provide a sequence of points denoting the trajectory of a robot gripper to achieve the goal. | hardware/simulator version and reset protocol | p. 20 (B IMPLEMENTATION AND ARCHITECTURE DETAILS), p. 20 (B.1 VLM IMPLEMENTATION DETAILS) |
| Dataset/benchmark | In real-world experiments, we simplify the language instruction in the same way as for RVT2 when conditioning on HAMSTER 2D paths to encourage following the trajectory more closely with limited data. | role, split, size and leakage | p. 20 (B IMPLEMENTATION AND ARCHITECTURE DETAILS), p. 20 (B.1 VLM IMPLEMENTATION DETAILS), p. 21 (B.2 LOW-LEVEL POLICY TRAINING DETAILS), p. 21 (B.2 LOW-LEVEL POLICY TRAINING DETAILS) |
| Metric | Table 1: Results on Colosseum demon- strate that HAMSTER is data efficient, achieving 2X the success score of 3D-DA with just 50% of the data. | definition, denominator, direction and uncertainty | p. 9 (Figure/Table caption), p. 28 (Figure/Table caption), p. 9 (Figure/Table caption) |
| Baseline/ablation | Figure 4: Depiction of quantitative real-world policy execution results on a real-world robot, evaluated across different axes of generalization and across both prehensile and non-prehensile tasks. Across all generalization axes, HAMSTE ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 10 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 3 BACKGROUND - extractive body cue:** See Appendix C for evaluation conditions, a task list, and other experiment details, and Appendix E for failure modes.
- **p. 10 / 3 BACKGROUND - extractive body cue:** 6 CONCLUSION AND LIMITATIONS In summary, we study hierarchical VLA models that achieve robust generalization in robotic manipulation.
- **p. 27 / Figure/Table caption - extractive body cue:** Figure 15: Performance Distribution of RVT2+Sketch and 3DDA+Sketch This section outlines the failure modes observed during our experiments and provides a detailed breakdown of the ...
- **p. 10 / 3 BACKGROUND - extractive body cue:** Moreover, the interface of just using 2D paths is a bandwidth limited one, which cannot communicate nuances such as force or rotation.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Overview of HAMSTER, VLAs and "smaller" imitation learning methods. HAMSTER's hierarchi- cal design results in better generalization with a small amount of in-domain ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: Depiction of HAMSTER's execution. The high-level VLM is called once to generate the 2D path. The low-level policy is conditioned on the 2D ...
- **p. 9 / 3 BACKGROUND - extractive body cue:** This improvement stems from training with path-drawn images, which encourages the policy to focus on the path rather than extraneous visual features, thereby enhancing robustness ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 A line of prior work (Brohan et al., 2023a; Kim et al., 2024; Black et al., 2024) builds open-world vision-language-action models (VLAs) by finetuning off-the-shelf pretrained VLMs to directly produce robot actions.를 문제로 두고, It is important to note that while we are certainly not the first to propose hierarchical VLA models (Gu et al., 2023; Nasiriany et al., 2024a), we propose the novel insight that ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 5 (3 BACKGROUND), p. 10 (3 BACKGROUND), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 20 (B.1 VLM IMPLEMENTATION DETAILS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
