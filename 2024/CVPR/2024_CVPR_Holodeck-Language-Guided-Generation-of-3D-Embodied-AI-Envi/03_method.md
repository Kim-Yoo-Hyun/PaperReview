# Method - Holodeck: Language Guided Generation of 3D Embodied AI Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3. HOLODECK), p. 3 (3. HOLODECK), p. 1 (Body text (section not recovered)), p. 3 (3. HOLODECK), p. 4 (3. HOLODECK), p. 4 (3. HOLODECK)): The algorithm first uses LLM to identify an anchor object and then explores placements for the anchor object.

## Method Body Digest

- **p. 5 / 3. HOLODECK - extractive body cue:** The algorithm first uses LLM to identify an anchor object and then explores placements for the anchor object.
- **p. 3 / 3. HOLODECK - extractive body cue:** In the following sections, we introduce our prompting approach that converts high-level user natural language specifications into a series of language model queries for constructing ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** Example outputs of HOLODECK-a large language model powered system, which can generate diverse types of environments (arcade, spa, museum), customize for styles (Victorian-style), and understand ...
- **p. 3 / 3. HOLODECK - extractive body cue:** We then provide a detailed overview of each module shown in Figure 2 and how they contribute to the final scene.
- **p. 4 / 3. HOLODECK - extractive body cue:** LLM's high-level responses to these prompts are post-processed and then used as input arguments for the modules to yield low-level specifications of the scene.
- **p. 4 / 3. HOLODECK - extractive body cue:** The Floor & Wall Module, illustrated in the first panel of Figure 2, is responsible for creating floor plans, constructing wall structures, and selecting materials ...
- **p. 2 / 1. Introduction - extractive body cue:** The predominant approach in training embodied agents involves learning in simulators [7, 20, 23, 35, 40, 51].
- **p. 1 / Abstract - extractive body cue:** To address the challenge of positioning objects correctly, we prompt GPT-4 to generate spatial relational constraints between objects and then optimize the layout to satisfy ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our contributions are three-fold: (1) We propose HOLODECK, a language-guided system capable of generating diverse, customized, and interactive 3D environments based on textual ...
- **p. 2 / 1. Introduction - extractive body cue:** In light of these challenges, we present HOLODECK, a language-guided system built upon AI2-THOR [23], to automatically generate diverse, customized, and interactive 3D embodied environments ...
- **p. 5 / 3. HOLODECK - extractive body cue:** To address this, instead of letting LLM directly operate on numerical values, we propose a novel constraint-based approach that employs LLM to generate spatial relations ...

## Source Evidence Cues

- **p. 5 / 3. HOLODECK - extractive body cue:** The algorithm first uses LLM to identify an anchor object and then explores placements for the anchor object.
- **p. 3 / 3. HOLODECK - extractive body cue:** In the following sections, we introduce our prompting approach that converts high-level user natural language specifications into a series of language model queries for constructing ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** Example outputs of HOLODECK-a large language model powered system, which can generate diverse types of environments (arcade, spa, museum), customize for styles (Victorian-style), and understand ...
- **p. 3 / 3. HOLODECK - extractive body cue:** We then provide a detailed overview of each module shown in Figure 2 and how they contribute to the final scene.
- **p. 4 / 3. HOLODECK - extractive body cue:** LLM's high-level responses to these prompts are post-processed and then used as input arguments for the modules to yield low-level specifications of the scene.
- **p. 4 / 3. HOLODECK - extractive body cue:** The Floor & Wall Module, illustrated in the first panel of Figure 2, is responsible for creating floor plans, constructing wall structures, and selecting materials ...
- **p. 2 / 1. Introduction - extractive body cue:** The predominant approach in training embodied agents involves learning in simulators [7, 20, 23, 35, 40, 51].
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | The algorithm first uses LLM to identify an anchor object and then explores placements for the anchor object. | p. 5 (3. HOLODECK), p. 3 (3. HOLODECK) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | In the following sections, we introduce our prompting approach that converts high-level user natural language specifications into a series of language model ... | p. 3 (3. HOLODECK), p. 1 (Body text (section not recovered)) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | Example outputs of HOLODECK-a large language model powered system, which can generate diverse types of environments (arcade, spa, museum), customize for styles ... | p. 1 (Body text (section not recovered)), p. 3 (3. HOLODECK) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / Abstract - extractive body cue:** To address the challenge of positioning objects correctly, we prompt GPT-4 to generate spatial relational constraints between objects and then optimize the layout to satisfy ...
- **p. 2 / 1. Introduction - extractive body cue:** Shown in Figure 2, given a description (e.g., a 1b1b apartment of a researcher who has a cat), HOLODECK uses a Large Language Model (GPT-4 ...
- **p. 5 / 3. HOLODECK - extractive body cue:** To find layouts that satisfy constraints sampled by LLMs, we adopt an optimization algorithm to place objects autoregressively.
- **p. 5 / 3. HOLODECK - extractive body cue:** The algorithm is executed for a fixed time (30 seconds) to get multiple candidate layouts and return the one that satisfies the most total constraints.
- **p. 6 / 3. HOLODECK - extractive body cue:** To import Objaverse assets into AI2-THOR for embodied AI applications, we optimize the assets by reducing mesh counts to minimize the loading time in AI2-THOR, ...
- **p. 3 / 3. HOLODECK - extractive body cue:** As shown in Figure 2, HOLODECK employs a systematic approach to scene construction, utilizing a series of specialized modules: (1) the Floor & Wall Module ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 1 (Abstract), p. 2 (1. Introduction), p. 3 (3. HOLODECK), p. 5 (3. HOLODECK), p. 5 (3. HOLODECK).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Example, outputs, HOLODECK-a, large, language, model, powered, system, generate, diverse, types, environments, arcade, museum | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Example, outputs, HOLODECK-a, large, language, model, powered, system, generate, diverse | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | summarize, contributions, three-fold, HOLODECK, language-guided, system, capable, generating, diverse, customized | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | address, challenge, positioning, objects, correctly, prompt, GPT-4, generate, spatial, relational | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Body text (section not recovered) - extractive body cue:** Example outputs of HOLODECK-a large language model powered system, which can generate diverse types of environments (arcade, spa, museum), customize for styles (Victorian-style), and understand ...
- **p. 4 / 3. HOLODECK - extractive body cue:** An LLM prompt is designed for each module with three elements: (1) Task Description: outlines the context and goals of the task; (2) Output Format: ...
- **p. 2 / Abstract - extractive body cue:** human evaluation shows that annotators prefer HOLODECK over manually designed procedural baselines in residential scenes and that HOLODECK can produce high-quality outputs for diverse scene ...
- **p. 2 / 1. Introduction - extractive body cue:** Through large-scale user studies involving 680 participants, we demonstrate that HOLODECK significantly surpasses existing procedural baseline PROCTHOR [6] in generating residential scenes and achieves high-quality ...
- **p. 4 / 3. HOLODECK - extractive body cue:** HOLODECK can adjust the size, quantity, position, etc., of doors & windows based on the input.
- **p. 5 / 3. HOLODECK - extractive body cue:** HOLODECK can generate multiple variants for the same input with different assets and layouts. objects in the scene.
- **p. 5 / 3. HOLODECK - extractive body cue:** Examples of Spatial Relational Constraints generated by LLM and their solutions found by our constraint satisfaction algorithm. a classic dining room with a long wooden ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | 7Limited by the PROCTHOR framework, we filter those scenes types that require special structures such as swimming pool, subway, etc. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | The three horizontal lines represent the average score of iTHOR, HOLODECK, and PROCTHOR on four types of residential scenes (bedroom, living room, ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | We train each model with 100 scenes for 50M steps, which takes approximately one day on 8 Quadro RTX 8000 GPUs. | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1. Introduction - extractive body cue:** The predominant approach in training embodied agents involves learning in simulators [7, 20, 23, 35, 40, 51].

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** algorithm, first, uses, LLM, identify, anchor, object, then, explores, placements, following, sections, introduce, prompting, converts, high-level, user, natural, language, specifications.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | To evaluate HOLODECK's capability beyond residential scenes, we have humans rate its performance on 52 scene types7 from MIT Scenes Dataset [36], ... | p. 6 (4.2. HOLODECK on Diverse Scenes), p. 7 (4.2. HOLODECK on Diverse Scenes) |
| Global / local decision | We conduct comprehensive human evaluations to assess the quality of HOLODECK scenes, with a total of 680 graduate students participating in three ... | p. 6 (4. Human Evaluation), p. 6 (4.1. Comparative Analysis on Residential Scenes) |
| Motion execution / recovery | Compared to PROCTHOR's performance in residential scenes, HOLODECK achieves higher human preference scores over half of (28 out of 52) the diverse ... | p. 7 (4.2. HOLODECK on Diverse Scenes), p. 7 (4.3. Ablation Study on Layout Design) |

## Failure and Ablation Link

- **p. 6 / 4. Human Evaluation - extractive body cue:** We conduct comprehensive human evaluations to assess the quality of HOLODECK scenes, with a total of 680 graduate students participating in three user studies: (1) ...
- **p. 7 / 4.3. Ablation Study on Layout Design - extractive body cue:** ABSOLUTE: directly obtaining the absolute coordinates and orientation of each object from LLM akin to LayoutGPT [9]; (3) RANDOM: randomly place all objects in the ...
- **p. 8 / 4.3. Ablation Study on Layout Design - extractive body cue:** Novel Environment: music room Novel object: piano Zero-shot Object Navigation on NOVELTYTHOR Pretraining on PROCTHOR Fine-tuning on HOLODECK Figure 12.
- **p. 8 / 4.3. Ablation Study on Layout Design - extractive body cue:** Given a novel scene type, e.g., Music Room, HOLODECK can synthesize new scenes for fine-tuning to improve the performance of pretrained agents in expert-designed environments.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 8. Output Diversity. HOLODECK can generate multiple variants for the same input with different assets and layouts. objects in the scene. Queries are constructed ...
- **p. 7 / 4.3. Ablation Study on Layout Design - extractive body cue:** The ABSOLUTE method performs no better than RANDOM due to its tendency to create scenes with collision and boundary errors (see examples in the supplement), ...
- **p. 7 / 4.3. Ablation Study on Layout Design - extractive body cue:** We present humans with four shuffled top-down images from each layout strategy and ask them to rank the four layouts considering out-of-boundary, object collision, reachable ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3. HOLODECK), p. 3 (3. HOLODECK), p. 1 (Body text (section not recovered)), p. 3 (3. HOLODECK), p. 4 (3. HOLODECK), p. 4 (3. HOLODECK), objective p. 1 (Abstract), p. 2 (1. Introduction), p. 5 (3. HOLODECK), p. 5 (3. HOLODECK), p. 6 (3. HOLODECK), p. 3 (3. HOLODECK), temporal p. 6 (4.2. HOLODECK on Diverse Scenes), p. 7 (4.2. HOLODECK on Diverse Scenes), p. 2 (2. Related Work), p. 2 (Abstract), p. 8 (5. Object Navigation in Novel Environments), p. 8 (5. Object Navigation in Novel Environments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
