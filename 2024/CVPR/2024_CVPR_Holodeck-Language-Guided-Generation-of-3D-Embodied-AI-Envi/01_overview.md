# Holodeck: Language Guided Generation of 3D Embodied AI Environments

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Generation, 3D scene, Embodied AI
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, these models often produce scenes with significant artifacts, such as mesh distortions, and lack the interactivity necessary for Embodied AI.를 문제로 두고, To summarize, our contributions are three-fold: (1) We propose HOLODECK, a language-guided system capable of generating diverse, customized, and interactive 3D environments based on textual descriptions; (2) The human evaluation validat ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D simulated environments play a critical role in Embodied AI, but their creation requires expertise and extensive manual effort, restricting their diversity and scope.
- **p. 1 / Abstract - extractive body cue:** To mitigate this limitation, we present HOLODECK, a system that generates 3D environments to match a user-supplied prompt fully automatedly.
- **p. 1 / Abstract - extractive body cue:** HOLODECK can generate diverse scenes, e.g., arcades, spas, and museums, adjust the designs for *Equal technical contribution.
- **p. 1 / Abstract - extractive body cue:** HOLODECK leverages a large language model (i.e., GPT-4) for common sense knowledge about what the scene might look like and uses a large collection of ...
- **p. 1 / Abstract - extractive body cue:** To address the challenge of positioning objects correctly, we prompt GPT-4 to generate spatial relational constraints between objects and then optimize the layout to satisfy ...
- **p. 2 / 1. Introduction - extractive body cue:** However, these models often produce scenes with significant artifacts, such as mesh distortions, and lack the interactivity necessary for Embodied AI.
- **p. 2 / 1. Introduction - extractive body cue:** To move beyond these limitations, recent works adapt 2D foundational models to generate 3D scenes from text [10, 16, 53].

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our contributions are three-fold: (1) We propose HOLODECK, a language-guided system capable of generating diverse, customized, and interactive 3D environments based on textual ...
- **p. 2 / 1. Introduction - extractive body cue:** In light of these challenges, we present HOLODECK, a language-guided system built upon AI2-THOR [23], to automatically generate diverse, customized, and interactive 3D embodied environments ...
- **p. 5 / 3. HOLODECK - extractive body cue:** To address this, instead of letting LLM directly operate on numerical values, we propose a novel constraint-based approach that employs LLM to generate spatial relations ...
- **p. 1 / Abstract - extractive body cue:** To mitigate this limitation, we present HOLODECK, a system that generates 3D environments to match a user-supplied prompt fully automatedly.
- **p. 3 / 3. HOLODECK - extractive body cue:** In the following sections, we introduce our prompting approach that converts high-level user natural language specifications into a series of language model queries for constructing ...
- **p. 5 / 3. HOLODECK - extractive body cue:** The algorithm first uses LLM to identify an anchor object and then explores placements for the anchor object.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Example outputs of HOLODECK-a large language model powered system, which can generate diverse types of environments (arcade, spa, museum), customize for styles (Victorian-style), and understand ...
- **p. 3 / 3. HOLODECK - extractive body cue:** We then provide a detailed overview of each module shown in Figure 2 and how they contribute to the final scene.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Example outputs of HOLODECK-a large language model powered system, which can generate diverse types of environments (arcade, spa, museum), customize for styles (Victorian-style), and understand fine-grained requirements ("has a cat", "f ... | camera/depth stream, pose, map와 language goal | p. 1 (Body text (section not recovered)), p. 4 (3. HOLODECK) |
| State/latent | Example, outputs, HOLODECK-a, large, language, model, powered, system, generate, diverse, types, environments | robot pose, free-space/semantic map와 local goal | p. 1 (Body text (section not recovered)), p. 4 (3. HOLODECK), p. 2 (Abstract) |
| Output/action | An LLM prompt is designed for each module with three elements: (1) Task Description: outlines the context and goals of the task; (2) Output Format: specifies the expected structure and type of ... | collision-free trajectory 또는 velocity command | p. 4 (3. HOLODECK), p. 2 (Abstract), p. 2 (1. Introduction) |
| Objective/outcome | To address the challenge of positioning objects correctly, we prompt GPT-4 to generate spatial relational constraints between objects and then optimize the layout to satisfy those constraints. | goal reach, safety, localization error와 replanning latency | p. 1 (Abstract), p. 2 (1. Introduction), p. 5 (3. HOLODECK) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our contributions are three-fold: (1) We propose HOLODECK, a language-guided system capable of generating diverse, customized, and interactive 3D environments based on textual ...
- **p. 2 / 1. Introduction - extractive body cue:** In light of these challenges, we present HOLODECK, a language-guided system built upon AI2-THOR [23], to automatically generate diverse, customized, and interactive 3D embodied environments ...
- **p. 5 / 3. HOLODECK - extractive body cue:** To address this, instead of letting LLM directly operate on numerical values, we propose a novel constraint-based approach that employs LLM to generate spatial relations ...
- **p. 1 / Abstract - extractive body cue:** To mitigate this limitation, we present HOLODECK, a system that generates 3D environments to match a user-supplied prompt fully automatedly.
- **p. 3 / 3. HOLODECK - extractive body cue:** In the following sections, we introduce our prompting approach that converts high-level user natural language specifications into a series of language model queries for constructing ...
- **p. 7 / 4.2. HOLODECK on Diverse Scenes - extractive body cue:** Compared to PROCTHOR's performance in residential scenes, HOLODECK achieves higher human preference scores over half of (28 out of 52) the diverse scenes.
- **p. 7 / 4.3. Ablation Study on Layout Design - extractive body cue:** HOLODECK's constraint-based approach outperforms the other methods significantly on bathroom, bedroom and living room.
- **p. 8 / 4.3. Ablation Study on Layout Design - extractive body cue:** Given a novel scene type, e.g., Music Room, HOLODECK can synthesize new scenes for fine-tuning to improve the performance of pretrained agents in expert-designed environments.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 7 (4.2. HOLODECK on Diverse Scenes), p. 7 (4.3. Ablation Study on Layout Design) |
| Embodiment/environment | To evaluate HOLODECK's capability beyond residential scenes, we have humans rate its performance on 52 scene types7 from MIT Scenes Dataset [36], covering five categories: Stores (deli, bakery), Home (bedroom, dining room), ... | hardware/simulator version and reset protocol | p. 6 (4.2. HOLODECK on Diverse Scenes), p. 7 (4.2. HOLODECK on Diverse Scenes) |
| Dataset/benchmark | We modify the residential scenes of HOLODECK used in 4.1 by altering the layouts using the previously mentioned methods while keeping the objects in the scene identical. | role, split, size and leakage | p. 6 (4.2. HOLODECK on Diverse Scenes), p. 7 (4.2. HOLODECK on Diverse Scenes), p. 7 (4.3. Ablation Study on Layout Design), p. 8 (4.3. Ablation Study on Layout Design) |
| Metric | The ABSOLUTE method performs no better than RANDOM due to its tendency to create scenes with collision and boundary errors (see examples in the supplement), typically rated poorly by humans. | definition, denominator, direction and uncertainty | p. 7 (4.3. Ablation Study on Layout Design), p. 6 (4.1. Comparative Analysis on Residential Scenes), p. 7 (4.2. HOLODECK on Diverse Scenes) |
| Baseline/ablation | We conduct comprehensive human evaluations to assess the quality of HOLODECK scenes, with a total of 680 graduate students participating in three user studies: (1) a comparative analysis on residential scenes with ... | fair input/data/compute/action matching | p. 6 (4. Human Evaluation), p. 6 (4.1. Comparative Analysis on Residential Scenes), p. 7 (4.3. Ablation Study on Layout Design) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.3. Ablation Study on Layout Design - extractive body cue:** The ABSOLUTE method performs no better than RANDOM due to its tendency to create scenes with collision and boundary errors (see examples in the supplement), ...
- **p. 7 / 4.3. Ablation Study on Layout Design - extractive body cue:** We present humans with four shuffled top-down images from each layout strategy and ask them to rank the four layouts considering out-of-boundary, object collision, reachable ...

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, these models often produce scenes with significant artifacts, such as mesh distortions, and lack the interactivity necessary for Embodied AI.를 문제로 두고, To summarize, our contributions are three-fold: (1) We propose HOLODECK, a language-guided system capable of generating diverse, customized, and interactive 3D environments based on textual descriptions; (2) The human evaluation validat ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3. HOLODECK), p. 3 (3. HOLODECK), p. 1 (Body text (section not recovered)), p. 3 (3. HOLODECK) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
