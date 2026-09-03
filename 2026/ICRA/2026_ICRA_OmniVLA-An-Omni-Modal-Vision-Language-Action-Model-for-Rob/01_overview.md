# OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html.
> PDF retrieval source: https://arxiv.org/pdf/2509.19480. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics, Navigation
- Official paper: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html
- Full-text retrieval: https://arxiv.org/pdf/2509.19480
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, prior work in robot navigation typically trains policies with single modalities based on narrow applications.를 문제로 두고, Moreover, our method allows the user to instruct the robot with multiple modalities, making it more user friendly and directly allowing the policy to leverage more than one kind of information about ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Humans can flexibly interpret and compose different goal specifications, such as language instructions, spatial coordinates, or visual references, when navigating to a destination.
- **p. 1 / Abstract - extractive body cue:** In contrast, most existing robotic navigation policies are trained on a single modality, limiting their adaptability to real-world scenarios where different forms of goal specification ...
- **p. 1 / Abstract - extractive body cue:** In this work, we present a training framework for robotic foundation models that enables omni-modal goal conditioning for vision-based navigation.
- **p. 1 / Abstract - extractive body cue:** Our approach leverages a high-capacity vision-language-action (VLA) backbone and trains with three primary goal modalities: 2D poses, egocentric images, and natural language, as well as ...
- **p. 1 / Abstract - extractive body cue:** This design not only expands the pool of usable datasets but also encourages the policy to develop richer geometric, semantic, and visual representations.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, prior work in robot navigation typically trains policies with single modalities based on narrow applications.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Additionally, we address the problem of modality imbalance and scarcity by using modality dropout during training, and modality masking during inference.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** Moreover, our method allows the user to instruct the robot with multiple modalities, making it more user friendly and directly allowing the policy to leverage ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this study, we propose a family of Omni-Modal VisionLanguage-Action Models (OmniVLA) for autonomous navigation that can ingest goals expressed in multiple modalities, leveraging information ...
- **p. 5 / Method - extractive body cue:** To ensure fair comparison with our approach, which relies solely on a single RGB camera without depth or LiDAR, we estimate depth using Depth360 [37] ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** By training on omni-modal goals, we aim to enable stronger and more flexible policies, ultimately acquiring a foundation model that exhibits high adaptability to novel ...
- **p. 5 / Method - extractive body cue:** A state lattice motion planner is then used to generate velocity commands.
- **p. 5 / Method - extractive body cue:** Other VLA backbones: To further understand the role of VLA architectures and pre-training, we also implement our omni-modal goal-conditioning strategy for the 1B MiniVLA [38] ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In this study, we propose a family of Omni-Modal VisionLanguage-Action Models (OmniVLA) for autonomous navigation that can ingest goals expressed in multiple modalities, leveraging information across modalities, and achieving a more fle ... | camera/depth stream, pose, map와 language goal | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| State/latent | study, family, Omni-Modal, VisionLanguage-Action, Models, OmniVLA, autonomous, navigation, ingest, goals, expressed, multiple | robot pose, free-space/semantic map와 local goal | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 5 (Method) |
| Output/action | As a result, our policy exhibits strong generalization and fine-tuning capabilities, following language instructions not seen in the training data, and adapting to completely new modalities. | collision-free trajectory 또는 velocity command | p. 2 (I. INTRODUCTION), p. 5 (Method), p. 2 (I. INTRODUCTION) |
| Objective/outcome | SR and Prog. indicate the success rate and the partial progress towards the goal, respectively. "SRS" averages over simple experiments without obstacles. "SRC" averages over complex experiments with obstacles in the environment. | goal reach, safety, localization error와 replanning latency | p. 5 (Method) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** Moreover, our method allows the user to instruct the robot with multiple modalities, making it more user friendly and directly allowing the policy to leverage ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this study, we propose a family of Omni-Modal VisionLanguage-Action Models (OmniVLA) for autonomous navigation that can ingest goals expressed in multiple modalities, leveraging information ...
- **p. 5 / Method - extractive body cue:** To ensure fair comparison with our approach, which relies solely on a single RGB camera without depth or LiDAR, we estimate depth using Depth360 [37] ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** By training on omni-modal goals, we aim to enable stronger and more flexible policies, ultimately acquiring a foundation model that exhibits high adaptability to novel ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Deploying OmniVLA on multiple embodi- ments. We deploy our policy on the Vizbot and Unitree Go1 robots. Our policy can follow natural language ...
- **p. 3 / Dataset - extractive body cue:** Naturally, we get coverage over all modalities and datasets while using this dropout mechanism to improve training stability.
- **p. 3 / Dataset - extractive body cue:** Training on these mixed-modality batches encourages the model to better represent goal information, yielding improved representations for generalization and fine-tuning.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 3 (Dataset) |
| Embodiment/environment | Training OmniVLA While using multi-modal inputs is enticing, training policies to accept omni-modal inputs requires compiling robot datasets that support training and addressing the relative imbalance and scarcity of the available modal ... | hardware/simulator version and reset protocol | p. 3 (Dataset), p. 3 (Dataset) |
| Dataset/benchmark | We begin by describing our setup for evaluating omnimodal navigation on our real-world robot platforms. | role, split, size and leakage | p. 3 (Dataset), p. 3 (Dataset), p. 4 (IV. EXPERIMENTAL SETUP), p. 4 (IV. EXPERIMENTAL SETUP) |
| Metric | Fig. 6: Deploying OmniVLA on multiple embodi- ments. We deploy our policy on the Vizbot and Unitree Go1 robots. Our policy can follow natural language instructions out of the box and reach ... | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 4 (IV. EXPERIMENTAL SETUP), p. 2 (Figure/Table caption) |
| Baseline/ablation | We conduct extensive real-world evaluations and compare against state-of-the-art specialist and generalist baselines. | fair input/data/compute/action matching | p. 4 (IV. EXPERIMENTAL SETUP), p. 4 (IV. EXPERIMENTAL SETUP), p. 3 (Dataset) |

## Explicit Limitations and Failure Boundary

- **p. 3 / Dataset - extractive body cue:** Since existing reannotation approaches cannot account for the large embodiment gap of the BDD-V [29] dataset (an autonomous vehicle dataset vs. the small robot datasets ...
- **p. 4 / Dataset - extractive body cue:** Since we cannot secure a sufficiently large batch size for some models even on a server with multiple GPUs, we accumulate the gradient for several ...
- **p. 5 / V. EVALUATING OMNI-MODAL NAVIGATION - extractive body cue:** However, NaVILA fails, scoring 0.0 on all metrics, due to a domain gap in prompt style: it requires
- **p. 6 / V. EVALUATING OMNI-MODAL NAVIGATION - extractive body cue:** The smaller OmniVLA variant fails to handle the language instructions due to limited modal capacity.
- **p. 3 / Dataset - extractive body cue:** While large datasets enable generalization, large-scale data collection efforts can result in more noise and therefore, be less accurate.
- **p. 4 / IV. EXPERIMENTAL SETUP - extractive body cue:** To assess the benefit of large pre-trained models, we introduced out-of-distribution (OOD) language prompts that go beyond the instructions present in the training data.
- **p. 6 / V. EVALUATING OMNI-MODAL NAVIGATION - extractive body cue:** These prompts are out-of-distribution (OOD) and not included in the training dataset.

## Why Read It

VLA and generalist robot policies의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, prior work in robot navigation typically trains policies with single modalities based on narrow applications.를 문제로 두고, Moreover, our method allows the user to instruct the robot with multiple modalities, making it more user friendly and directly allowing the policy to leverage more than one kind of information about ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 5 (Method), p. 5 (Method), p. 7 (Figure/Table caption) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
