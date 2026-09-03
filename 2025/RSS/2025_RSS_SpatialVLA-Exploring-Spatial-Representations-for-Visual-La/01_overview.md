# SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p011.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p011.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, Robotics, 3D spatial representation, action representation, cross-embodiment, robot data
- Official paper: https://www.roboticsproceedings.org/rss21/p011.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p011.pdf
- Code/Project: https://github.com/SpatialVLA/SpatialVLA
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, developing such generalist robot policies with 3D spatial intelligence encounters two primary challenges in the aspects of robot observation and action.를 문제로 두고, In summary, the contributions of this work consist of a novel generalist robot policy that explores spatial representations for robot foundation models, sophisticated designs on Ego3D Posi tion Encoding and Adaptive Action ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In this paper, we claim that spatial understanding is the keypoint in robot manipulation, and propose SpatialVLA to ‘explore effective spatial representations for the robot ...
- **p. 1 / Abstract - extractive body cue:** Specifically, we introduce Fgo3D Position Encoding 10 inject 3D information into the input observations of the visuallanguage-action model, and propose Adaptive Action Grids to represent ...
- **p. 1 / Abstract - extractive body cue:** SpatialVLA is, first prestrained on top of a vision-language model with 1.1 Million real-world robot episodes, to learn a generalist manipulation policy across multiple robot ...
- **p. 1 / Abstract - extractive body cue:** After pre-training, SpatialVLA is directly applied to perform ‘numerous tasks in a zero-shot manner.
- **p. 1 / Abstract - extractive body cue:** The superior results in both simulation and real-world robots demonstrate its advantage of inferring complex robot motion trajectories and its strong indomain multitask generalization ability.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, developing such generalist robot policies with 3D spatial intelligence encounters two primary challenges in the aspects of robot observation and action.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Secondly, different robots have different action movement characteristics to accomplish diverse tasks, due to different degrees of freedom, motion controllers, workspace configurations, and task complexity, ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, the contributions of this work consist of a novel generalist robot policy that explores spatial representations for robot foundation models, sophisticated designs on ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** OpenVLA [30] adopts a similar action discretization approach and fine-tune Prismatic VLM [28] only on the OXE dataset [13], which consists of robot data from ...
- **p. 4 / B. The Pre-training and Post-training Scheme - extractive body cue:** ‘To obtain a generalist robot policy model, the training procedure of SpatialVLA consists of pre-training stage and posttraining stage.
- **p. 4 / A. The SpatialVLA Model Architecture - extractive body cue:** space consists Of Myax = Mg *Mo ~M,. diserete spatial stids Ons = {2,...a%}, Similarly, there are Myr = Meat » Myick *Myaw 3D discrete ...
- **p. 3 / A. The SpatialVLA Model Architecture - extractive body cue:** 2, SpatialVLA is developed based on a vision-language model to inherit the general world knowledge.
- **p. 3 / A. The SpatialVLA Model Architecture - extractive body cue:** During training, SpatialVLA model is trained to take the ego3D position encoding representation Ogq and natural language task instruction Las inputs, and autoregressively generate spatial ...
- **p. 5 / B. The Pre-training and Post-training Scheme - extractive body cue:** In detail, we ft a new Gaussian distribution AV (jig, Yacw) for each action variable on posttraining datasets and create discrete spatial action grids Gey ...
- **p. 4 / A. The SpatialVLA Model Architecture - extractive body cue:** 2, we first employ SigLIP [68] visual encoder to extract 2D semantic visual features X ¢ R4**" to inherit the alignment between vision and language, ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We find that the proposed model Spatial VLA bridges observation inputs and aetion outputs in a universal robot-agnostic manner, which explores powerful 3D spatial-aware representations to enhance the VLA model. | image/video, language instruction, proprioception과 history | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| State/latent | find, model, Spatial, VLA, bridges, observation, inputs, aetion, outputs, universal, robot-agnostic, manner | language-grounded task state와 action-policy context | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (A. The SpatialVLA Model Architecture) |
| Output/action | In this work, as illustrated in Fig. /, we propose a generalist robot policy SpatialVLA, which equips the VLA model with 3D spatial intelligence by exploring aligned spatial representations of robot observation ... | continuous action, pose 또는 action chunk | p. 2 (I. INTRODUCTION), p. 3 (A. The SpatialVLA Model Architecture), p. 3 (A. The SpatialVLA Model Architecture) |
| Objective/outcome | In detail, we ft a new Gaussian distribution AV (jig, Yacw) for each action variable on posttraining datasets and create discrete spatial action grids Gey in translation and rotation movement to construct ... | instruction following, task success, generalization과 latency | p. 5 (B. The Pre-training and Post-training Scheme), p. 3 (A. The SpatialVLA Model Architecture), p. 5 (B. The Pre-training and Post-training Scheme) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, the contributions of this work consist of a novel generalist robot policy that explores spatial representations for robot foundation models, sophisticated designs on ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** OpenVLA [30] adopts a similar action discretization approach and fine-tune Prismatic VLM [28] only on the OXE dataset [13], which consists of robot data from ...
- **p. 4 / B. The Pre-training and Post-training Scheme - extractive body cue:** ‘To obtain a generalist robot policy model, the training procedure of SpatialVLA consists of pre-training stage and posttraining stage.
- **p. 4 / A. The SpatialVLA Model Architecture - extractive body cue:** space consists Of Myax = Mg *Mo ~M,. diserete spatial stids Ons = {2,...a%}, Similarly, there are Myr = Meat » Myick *Myaw 3D discrete ...
- **p. 3 / A. The SpatialVLA Model Architecture - extractive body cue:** 2, SpatialVLA is developed based on a vision-language model to inherit the general world knowledge.
- **p. 7 / 10 Ablations on Design - extractive body cue:** Spatial VLA achieves the highest average success rate, outperforming all generalist manipulation policies.
- **p. 9 / B. Adapting to New Robot Setups - extractive body cue:** Compared to 1026-resolution action grids (#ly.s:#4), where Maes = Muss = 512, Myip = 2, Spatial VLA with 8194resolution action grids (Mines = Mrans = ...
- **p. 7 / 10 Ablations on Design - extractive body cue:** Overall, SpatialVLA achieves a higher average success rate, showcasing robust and generalizable operation capabilities in unseen scenarios, objects, language grounding, and dynamic motions.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (10 Ablations on Design), p. 9 (B. Adapting to New Robot Setups) |
| Embodiment/environment | We train SpatialVLA from Paligemma2 backbone [62] on a cross-robot dataset mixture with 1.1 Million real robot demonstrations {615 Gu}> covering a diverse range of robot embodiments, scenes, and tasks, This pre-training ... | hardware/simulator version and reset protocol | p. 4 (B. The Pre-training and Post-training Scheme), p. 5 (3) How well does SpatialVLA perform in scenarios that) |
| Dataset/benchmark | Second, we assess the fine-tuning efficacy of our method in both simulation and real-world settings, including LIBERO [36] and new Franka robot setups, to adapt to new robot environments and tasks. ‘Then, ... | role, split, size and leakage | p. 4 (B. The Pre-training and Post-training Scheme), p. 5 (3) How well does SpatialVLA perform in scenarios that), p. 5 (3) How well does SpatialVLA perform in scenarios that), p. 7 (B. Adapting to New Robot Setups) |
| Metric | We present the success rate (SR) and standard error for each method across four task suites, which are averaged over three random seeds with 500 trials. | definition, denominator, direction and uncertainty | p. 8 (B. Adapting to New Robot Setups), p. 9 (B. Adapting to New Robot Setups), p. 7 (10 Ablations on Design) |
| Baseline/ablation | In particular, SpatialVLA also matches or outperforms te latest SOTA model 7, Tab, I! summarizes the esults across different manipulation policies on the WidowX setup, Our model surpasses the state-of-the-art RoboVLM policy, ... | fair input/data/compute/action matching | p. 7 (10 Ablations on Design), p. 5 (B. The Pre-training and Post-training Scheme), p. 7 (B. Adapting to New Robot Setups) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 10 Ablations on Design - extractive body cue:** However, in moderately complex tasks (#3-7), ‘most policies, such as RT-1-X, Octo, and RoboVLM struggle with manipulation, frequently encountering issues like object nisidentfication and grasp ...
- **p. 7 / 10 Ablations on Design - extractive body cue:** Compared to OpenVLA, ‘our method demonstrates superior robustness in handling motion disturbances (human-induced dynamic object movement in tasks #3 and #4), successfully tracking and grasping ...
- **p. 5 / 3) How well does SpatialVLA perform in scenarios that - extractive body cue:** To assess the robustness of Spatial VLA in diverse environmental variations, we employ the SimplerEnv simulation benchmark [35] to evaluate visual ‘matching and variant aggregation ...
- **p. 6 / 10 Ablations on Design - extractive body cue:** Qualitatively, we find that SpatialVLA exhibits greater generalizability and robustness across diverse robotic manipulation tasks and environmental
- **p. 8 / B. Adapting to New Robot Setups - extractive body cue:** 1), including depth or point cloud, into the VLA framework to improve the model's adaptability and robustness in spatial layout variations.
- **p. 8 / B. Adapting to New Robot Setups - extractive body cue:** Compared to existing policies, SpaIVLA shows superior spatial understanding, achieving 73% accuracy in Franka task #1, which involves spatial prompts, and significantly improving manipulation capabilities ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, developing such generalist robot policies with 3D spatial intelligence encounters two primary challenges in the aspects of robot observation and action.를 문제로 두고, In summary, the contributions of this work consist of a novel generalist robot policy that explores spatial representations for robot foundation models, sophisticated designs on Ego3D Posi tion Encoding and Adaptive Action ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (A. The SpatialVLA Model Architecture), p. 5 (B. The Pre-training and Post-training Scheme), p. 4 (B. The Pre-training and Post-training Scheme) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, developing such generalist robot policies with 3D spatial intelligence encounters two primary challenges in the aspects of robot observation and action. (p. 2, I. INTRODUCTION).
- **Actual contribution:** In summary, the contributions of this work consist of a novel generalist robot policy that explores spatial representations for robot foundation models, sophisticated designs on Ego3D Posi tion Encoding and ... (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** For a more comprehensive evaluation, we conduct expernts on a real-world WidowX robot platform from the BridgeData V2 evaluation [64]. (p. 6, 10 Ablations on Design).
- **Explicit failure boundary:** However, in moderately complex tasks (#3-7), ‘most policies, such as RT-1-X, Octo, and RoboVLM struggle with manipulation, frequently encountering issues like object nisidentfication and grasp failures. (p. 7, 10 Ablations on Design).
