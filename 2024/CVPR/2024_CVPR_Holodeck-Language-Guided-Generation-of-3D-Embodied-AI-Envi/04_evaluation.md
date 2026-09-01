# Evaluation - Holodeck: Language Guided Generation of 3D Embodied AI Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.2. HOLODECK on Diverse Scenes), p. 7 (4.3. Ablation Study on Layout Design), p. 8 (4.3. Ablation Study on Layout Design), p. 6 (4.2. HOLODECK on Diverse Scenes), p. 6 (4.1. Comparative Analysis on Residential Scenes), p. 8 (4.3. Ablation Study on Layout Design)): Compared to PROCTHOR's performance in residential scenes, HOLODECK achieves higher human preference scores over half of (28 out of 52) the diverse scenes.

## Evaluation Body Digest

- **p. 6 / 4.2. HOLODECK on Diverse Scenes - extractive PDF cue:** To evaluate HOLODECK's capability beyond residential scenes, we have humans rate its performance on 52 scene types7 from MIT Scenes Dataset [36], covering five categories: ...
- **p. 7 / 4.2. HOLODECK on Diverse Scenes - extractive PDF cue:** Given that PROCTHOR relies on human-defined rules and residential scenes are relatively easy to build with common objects and simple layout, HOLODECK's breadth of competence ...
- **p. 7 / 4.3. Ablation Study on Layout Design - extractive PDF cue:** We modify the residential scenes of HOLODECK used in 4.1 by altering the layouts using the previously mentioned methods while keeping the objects in the ...
- **p. 8 / 4.3. Ablation Study on Layout Design - extractive PDF cue:** Zero-shot object navigation in novel scenes.
- **p. 8 / 4.3. Ablation Study on Layout Design - extractive PDF cue:** Given a novel scene type, e.g., Music Room, HOLODECK can synthesize new scenes for fine-tuning to improve the performance of pretrained agents in expert-designed environments.
- **p. 6 / 4.1. Comparative Analysis on Residential Scenes - extractive PDF cue:** Besides, we add human-designed scenes from iTHOR [23] as the upper bound for reference.
- **p. 7 / 4.3. Ablation Study on Layout Design - extractive PDF cue:** The ABSOLUTE method performs no better than RANDOM due to its tendency to create scenes with collision and boundary errors (see examples in the supplement), ...
- **p. 6 / 4.1. Comparative Analysis on Residential Scenes - extractive PDF cue:** CLIP Score comparison over four residential scene types. * denotes iTHOR scenes are designed by human experts. as the prompt to generate the scenes.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4. Human Evaluation (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. HOLODECK on Diverse Scenes | SYSTEM / EVALUATION SCOPE UNRESOLVED | Compared to PROCTHOR's performance in residential scenes, HOLODECK achieves higher human preference scores over half of (28 out of 52) the diverse scenes. | p. 7 (4.2. HOLODECK on Diverse Scenes) |
| 4.3. Ablation Study on Layout Design | SYSTEM / EVALUATION SCOPE UNRESOLVED | HOLODECK's constraint-based approach outperforms the other methods significantly on bathroom, bedroom and living room. | p. 7 (4.3. Ablation Study on Layout Design) |
| 4.3. Ablation Study on Layout Design | SYSTEM / EVALUATION SCOPE UNRESOLVED | Given a novel scene type, e.g., Music Room, HOLODECK can synthesize new scenes for fine-tuning to improve the performance of pretrained agents in expert-designed ... | p. 8 (4.3. Ablation Study on Layout Design) |
| 4.2. HOLODECK on Diverse Scenes | SYSTEM / EVALUATION SCOPE UNRESOLVED | We use cosine similarity times 100 as the CLIP Score. | p. 6 (4.2. HOLODECK on Diverse Scenes) |
| 4.1. Comparative Analysis on Residential Scenes | SYSTEM / EVALUATION SCOPE UNRESOLVED | The CLIP Score experiment agrees with our human evaluation. | p. 6 (4.1. Comparative Analysis on Residential Scenes) |

## Dataset / Benchmark Role

- **p. 6 / 4.2. HOLODECK on Diverse Scenes - extractive PDF cue:** To evaluate HOLODECK's capability beyond residential scenes, we have humans rate its performance on 52 scene types7 from MIT Scenes Dataset [36], covering five categories: ...
- **p. 7 / 4.2. HOLODECK on Diverse Scenes - extractive PDF cue:** Given that PROCTHOR relies on human-defined rules and residential scenes are relatively easy to build with common objects and simple layout, HOLODECK's breadth of competence ...
- **p. 7 / 4.3. Ablation Study on Layout Design - extractive PDF cue:** We modify the residential scenes of HOLODECK used in 4.1 by altering the layouts using the previously mentioned methods while keeping the objects in the ...
- **p. 8 / 4.3. Ablation Study on Layout Design - extractive PDF cue:** Zero-shot object navigation in novel scenes.
- **p. 8 / 4.3. Ablation Study on Layout Design - extractive PDF cue:** Given a novel scene type, e.g., Music Room, HOLODECK can synthesize new scenes for fine-tuning to improve the performance of pretrained agents in expert-designed environments.
- **p. 6 / 4.1. Comparative Analysis on Residential Scenes - extractive PDF cue:** Besides, we add human-designed scenes from iTHOR [23] as the upper bound for reference.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Example outputs of HOLODECK-a large language model powered system, which can generate diverse types of environments (arcade, spa, museum), customize for styles (Victorian-style), ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Given a text input, HOLODECK generates the 3D environment through multiple rounds of conversation with an LLM. as 3D-FRONT [11] restricts their applicability. ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Floorplan Customizability. HOLODECK can interpret complicated input and craft reasonable floor plans correspondingly. a prison cell a bedroom of a girl who loves ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4. Material Customizability. HOLODECK can select appropriate floor and wall materials to make the scenes more realistic. an apartment for a disabled person who ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 5. Door & window Customizability. HOLODECK can adjust the size, quantity, position, etc., of doors & windows based on the input. Overall Prompt Design. ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 6. Objects Customizability. HOLODECK can select and place appropriate floor/wall/small/ceiling objects conditioned on the input. bed cabinet bathtub toilet basket towel rail toilet paper
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 7. Examples of Spatial Relational Constraints generated by LLM and their solutions found by our constraint satisfaction algorithm. a classic dining room with a ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 8. Output Diversity. HOLODECK can generate multiple variants for the same input with different assets and layouts. objects in the scene. Queries are constructed ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To evaluate HOLODECK's capability beyond residential scenes, we have humans rate its performance on 52 scene types7 from MIT Scenes Dataset [36], covering five ... | embodiment, simulator version and control stack | p. 6 (4.2. HOLODECK on Diverse Scenes), p. 7 (4.2. HOLODECK on Diverse Scenes) |
| Task/environment | Given that PROCTHOR relies on human-defined rules and residential scenes are relatively easy to build with common objects and simple layout, HOLODECK's breadth of ... | reset, timeout, object/scene variation | p. 7 (4.2. HOLODECK on Diverse Scenes), p. 7 (4.3. Ablation Study on Layout Design) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 4 (3. HOLODECK), p. 2 (Abstract) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 2 (1. Introduction), p. 4 (3. HOLODECK) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The ABSOLUTE method performs no better than RANDOM due to its tendency to create scenes with collision and boundary errors (see examples in the ... | definition/direction/unit from same section | p. 7 (4.3. Ablation Study on Layout Design) |
| CLIP Score comparison over four residential scene types. * denotes iTHOR scenes are designed by human experts. as the prompt to generate the scenes. | definition/direction/unit from same section | p. 6 (4.1. Comparative Analysis on Residential Scenes) |
| Compared to PROCTHOR's performance in residential scenes, HOLODECK achieves higher human preference scores over half of (28 out of 52) the diverse scenes. | definition/direction/unit from same section | p. 7 (4.2. HOLODECK on Diverse Scenes) |
| We report Success (%) and Success weighted by Path Length (SPL). | definition/direction/unit from same section | p. 8 (4.3. Ablation Study on Layout Design) |
| Office Daycare Music Room Gym Arcade Average Method Success SPL Success SPL Success SPL Success SPL Success SPL Success SPL Random 3.90 0.039 4.05 ... | definition/direction/unit from same section | p. 8 (4.3. Ablation Study on Layout Design) |
| We use cosine similarity times 100 as the CLIP Score. | definition/direction/unit from same section | p. 6 (4.2. HOLODECK on Diverse Scenes) |
| Figure 1. Example outputs of HOLODECK-a large language model powered system, which can generate diverse types of environments (arcade, spa, museum), customize for styles ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. Given a text input, HOLODECK generates the 3D environment through multiple rounds of conversation with an LLM. as 3D-FRONT [11] restricts their ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We conduct comprehensive human evaluations to assess the quality of HOLODECK scenes, with a total of 680 graduate students participating in three user studies: ... | comparison identity and matched condition | p. 6 (4. Human Evaluation) |
| The PROCTHOR baseline has access to the same set of Objaverse assets as HOLODECK. | comparison identity and matched condition | p. 6 (4.1. Comparative Analysis on Residential Scenes) |
| HOLODECK's constraint-based approach outperforms the other methods significantly on bathroom, bedroom and living room. | comparison identity and matched condition | p. 7 (4.3. Ablation Study on Layout Design) |
| Compared to PROCTHOR's performance in residential scenes, HOLODECK achieves higher human preference scores over half of (28 out of 52) the diverse scenes. | comparison identity and matched condition | p. 7 (4.2. HOLODECK on Diverse Scenes) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We conduct comprehensive human evaluations to assess the quality of HOLODECK scenes, with a total of 680 graduate students participating in three user studies: ... | component/input/data sensitivity | p. 6 (4. Human Evaluation) |
| ABSOLUTE: directly obtaining the absolute coordinates and orientation of each object from LLM akin to LayoutGPT [9]; (3) RANDOM: randomly place all objects in ... | component/input/data sensitivity | p. 7 (4.3. Ablation Study on Layout Design) |
| Novel Environment: music room Novel object: piano Zero-shot Object Navigation on NOVELTYTHOR Pretraining on PROCTHOR Fine-tuning on HOLODECK Figure 12. | component/input/data sensitivity | p. 8 (4.3. Ablation Study on Layout Design) |
| Given a novel scene type, e.g., Music Room, HOLODECK can synthesize new scenes for fine-tuning to improve the performance of pretrained agents in expert-designed ... | component/input/data sensitivity | p. 8 (4.3. Ablation Study on Layout Design) |
| Figure 8. Output Diversity. HOLODECK can generate multiple variants for the same input with different assets and layouts. objects in the scene. Queries are ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To summarize, our contributions are three-fold: (1) We propose HOLODECK, a language-guided system capable of generating diverse, customized, and interactive 3D environments based on ... | Compared to PROCTHOR's performance in residential scenes, HOLODECK achieves higher human preference scores over half of (28 out of 52) the diverse scenes. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.2. HOLODECK on Diverse Scenes), p. 7 (4.3. Ablation Study on Layout Design), p. 8 (4.3. Ablation Study on Layout Design), p. 6 (4.2. HOLODECK on Diverse Scenes), p. 6 (4.1. Comparative Analysis on Residential Scenes), p. 8 (4.3. Ablation Study on Layout Design) |
| Primary metric/result | HOLODECK's constraint-based approach outperforms the other methods significantly on bathroom, bedroom and living room. | numeric claim only at cited anchor | p. 7 (4.3. Ablation Study on Layout Design) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Comparative Analysis on Residential Scenes - extractive PDF cue:** We prepared 120 scenes for human evaluation, comprising 30 scenes per scene type, for both HOLODECK and the PROCTHOR baseline.
- **p. 6 / 4.2. HOLODECK on Diverse Scenes - extractive PDF cue:** To evaluate HOLODECK's capability beyond residential scenes, we have humans rate its performance on 52 scene types7 from MIT Scenes Dataset [36], covering five categories: ...
- **p. 7 / 4.2. HOLODECK on Diverse Scenes - extractive PDF cue:** Human evaluation on 52 scene types from MIT Scenes [36] with qualitative examples.
- **p. 7 / 4.2. HOLODECK on Diverse Scenes - extractive PDF cue:** We prompt HOLODECK to produce five outputs for each type using only the scene name as the input, accumulating 260 examples across the 52 scene ...
- **p. 7 / 4.2. HOLODECK on Diverse Scenes - extractive PDF cue:** To provide context for these scores, we include residential scenes from PROCTHOR and iTHOR in this study, with 20 scenes from each system.
- **p. 4 / 3. HOLODECK - extractive PDF cue:** HOLODECK can interpret complicated input and craft reasonable floor plans correspondingly. a prison cell a bedroom of a girl who loves the pink color a ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The ABSOLUTE method performs no better than RANDOM due to its tendency to create scenes with collision and boundary errors (see examples in the ... | p. 7 (4.3. Ablation Study on Layout Design) |
| body limitation/failure cue | We present humans with four shuffled top-down images from each layout strategy and ask them to rank the four layouts considering out-of-boundary, object collision, ... | p. 7 (4.3. Ablation Study on Layout Design) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Our large-scale This CVPR paper is the Open Access version, provided by the Computer Vision Foundation. | p. 1 (Abstract) |
| Existing Embodied AI environments are typically crafted through manual design [5, 12, 23, 24], 3D scanning [7, 38, 40], or procedurally generated with hard-coded ... | p. 2 (1. Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.3. Ablation Study on Layout Design - extractive PDF cue:** The ABSOLUTE method performs no better than RANDOM due to its tendency to create scenes with collision and boundary errors (see examples in the supplement), ...
- **p. 7 / 4.3. Ablation Study on Layout Design - extractive PDF cue:** We present humans with four shuffled top-down images from each layout strategy and ask them to rank the four layouts considering out-of-boundary, object collision, reachable ...

- **PDF anchors reviewed:** datasets p. 6 (4.2. HOLODECK on Diverse Scenes), p. 7 (4.2. HOLODECK on Diverse Scenes), p. 7 (4.3. Ablation Study on Layout Design), p. 8 (4.3. Ablation Study on Layout Design), p. 8 (4.3. Ablation Study on Layout Design), p. 6 (4.1. Comparative Analysis on Residential Scenes), metrics p. 7 (4.3. Ablation Study on Layout Design), p. 6 (4.1. Comparative Analysis on Residential Scenes), p. 7 (4.2. HOLODECK on Diverse Scenes), p. 8 (4.3. Ablation Study on Layout Design), p. 8 (4.3. Ablation Study on Layout Design), p. 6 (4.2. HOLODECK on Diverse Scenes), baselines p. 6 (4. Human Evaluation), p. 6 (4.1. Comparative Analysis on Residential Scenes), p. 7 (4.3. Ablation Study on Layout Design), p. 7 (4.2. HOLODECK on Diverse Scenes), results p. 7 (4.2. HOLODECK on Diverse Scenes), p. 7 (4.3. Ablation Study on Layout Design), p. 8 (4.3. Ablation Study on Layout Design), p. 6 (4.2. HOLODECK on Diverse Scenes), p. 6 (4.1. Comparative Analysis on Residential Scenes), p. 8 (4.3. Ablation Study on Layout Design).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
