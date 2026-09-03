# Method - Dynam3D: Dynamic Layered 3D Tokens Empower VLM for Vision-and-Language Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=s6k9l5yX8e; PDF retrieval source: https://arxiv.org/pdf/2505.11383. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (Abstract)): In summary, our main contributions include: • We propose Dynam3D, a multi-level patch-instance-zone 3D representation model that performs online 3D instance and zone-level encoding and real-time hierarchical updates in dynamic ...

## Method Body Digest

- **p. 2 / 1 Introduction - extractive body cue:** In summary, our main contributions include: • We propose Dynam3D, a multi-level patch-instance-zone 3D representation model that performs online 3D instance and zone-level encoding and ...
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we propose Dynam3D, a dynamic layered 3D representation model that leverages language-aligned, generalizable, and hierarchical 3D representations as visual input to ...
- **p. 2 / 1 Introduction - extractive body cue:** These rendered 3D patch features combined with instance and zone representations serve as visual input to the 3D Vision-Language Model (VLM).
- **p. 1 / Abstract - extractive body cue:** By leveraging large-scale 3D-language pretraining and task-specific adaptation, our Dynam3D sets new state-of-the-art performance on VLN benchmarks including R2R-CE, REVERIE-CE and NavRAG-CE under monocular settings.
- **p. 1 / 1 Introduction - extractive body cue:** This is due to the practical constraint that most robots are equipped with monocular cameras instead of panoramic cameras.
- **p. 2 / 1 Introduction - extractive body cue:** A 3D instance merging discriminator aligns 2D instances with existing 3D instances based on geometry and semantics to enable dynamic updates of 3D instance representations.
- **p. 2 / 1 Introduction - extractive body cue:** Compared to previous video-based representations (a), our Dynam3D (b) adopts dynamic hierarchical 3D representations offering advantages in spatial geometry and semantic understanding. pre-exploration knowledge and ...
- **p. 2 / 1 Introduction - extractive body cue:** Instruction: "Please go to the kitchen and take the bread out of the microwave for me." … Video-Language Large Model … Action 3D-Language Large Model ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** In summary, our main contributions include: • We propose Dynam3D, a multi-level patch-instance-zone 3D representation model that performs online 3D instance and zone-level encoding and ...
- **p. 2 / 1 Introduction - extractive body cue:** We propose Dynam3D to alleviate the limitations mentioned above.
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we propose Dynam3D, a dynamic layered 3D representation model that leverages language-aligned, generalizable, and hierarchical 3D representations as visual input to ...

## Source Evidence Cues

- **p. 2 / 1 Introduction - extractive body cue:** In summary, our main contributions include: • We propose Dynam3D, a multi-level patch-instance-zone 3D representation model that performs online 3D instance and zone-level encoding and ...
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we propose Dynam3D, a dynamic layered 3D representation model that leverages language-aligned, generalizable, and hierarchical 3D representations as visual input to ...
- **p. 2 / 1 Introduction - extractive body cue:** These rendered 3D patch features combined with instance and zone representations serve as visual input to the 3D Vision-Language Model (VLM).
- **p. 1 / Abstract - extractive body cue:** By leveraging large-scale 3D-language pretraining and task-specific adaptation, our Dynam3D sets new state-of-the-art performance on VLN benchmarks including R2R-CE, REVERIE-CE and NavRAG-CE under monocular settings.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | In summary, our main contributions include: • We propose Dynam3D, a multi-level patch-instance-zone 3D representation model that performs online 3D instance and ... | p. 2 (1 Introduction), p. 1 (Abstract) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | To address these limitations, we propose Dynam3D, a dynamic layered 3D representation model that leverages language-aligned, generalizable, and hierarchical 3D representations as ... | p. 1 (Abstract), p. 2 (1 Introduction) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | These rendered 3D patch features combined with instance and zone representations serve as visual input to the 3D Vision-Language Model (VLM). | p. 2 (1 Introduction), p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / 1 Introduction - extractive body cue:** This is due to the practical constraint that most robots are equipped with monocular cameras instead of panoramic cameras.
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we propose Dynam3D, a dynamic layered 3D representation model that leverages language-aligned, generalizable, and hierarchical 3D representations as visual input to ...
- **p. 2 / 1 Introduction - extractive body cue:** A 3D instance merging discriminator aligns 2D instances with existing 3D instances based on geometry and semantics to enable dynamic updates of 3D instance representations.
- **p. 2 / 1 Introduction - extractive body cue:** Compared to previous video-based representations (a), our Dynam3D (b) adopts dynamic hierarchical 3D representations offering advantages in spatial geometry and semantic understanding. pre-exploration knowledge and ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | address, limitations, Dynam3D, dynamic, layered, representation, model, leverages, language-aligned, generalizable, hierarchical, representations, visual, input | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | address, limitations, Dynam3D, dynamic, layered, representation, model, leverages, language-aligned, generalizable | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | summary, main, contributions, include, Dynam3D, multi-level, patch-instance-zone, representation, model, performs | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | practical, constraint, most, robots, equipped, monocular, cameras, instead, panoramic, address | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Abstract - extractive body cue:** To address these limitations, we propose Dynam3D, a dynamic layered 3D representation model that leverages language-aligned, generalizable, and hierarchical 3D representations as visual input to ...
- **p. 2 / 1 Introduction - extractive body cue:** Instruction: "Please go to the kitchen and take the bread out of the microwave for me." … Video-Language Large Model … Action 3D-Language Large Model ...
- **p. 1 / 1 Introduction - extractive body cue:** These models pre-trained on large-scale internet data demonstrate strong language understanding and multimodal reasoning abilities, which enable effective instruction following and continuous prediction of navigation ...
- **p. 2 / 1 Introduction - extractive body cue:** Given language instructions and action history, the 3D-VLM directly predicts navigation actions, e.g., turn θ degrees, move forward d cm, or stop.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Most navigation episodes can be completed within 20 to 40 navigation steps, our navigation system supports real-time 3D representation updates and navigation ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | For the Lifelong Memory setting, we group the evaluation episodes by scene with navigation samples from the same scene evaluated consecutively within ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | For the Lifelong Memory setting, we group the evaluation episodes by scene with navigation samples from the same scene evaluated consecutively within ... | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | Methods NE↓OSR↑SR↑ NaVid 3.6 45 20 g3D-LF 4.6 35 10 Dynam3D 1.9 60 45 + Pre-exploration 1.4 75 45 4.4 Computational Cost ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 Introduction - extractive body cue:** In summary, our main contributions include: • We propose Dynam3D, a multi-level patch-instance-zone 3D representation model that performs online 3D instance and zone-level encoding and ...
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we propose Dynam3D, a dynamic layered 3D representation model that leverages language-aligned, generalizable, and hierarchical 3D representations as visual input to ...
- **p. 1 / Abstract - extractive body cue:** By leveraging large-scale 3D-language pretraining and task-specific adaptation, our Dynam3D sets new state-of-the-art performance on VLN benchmarks including R2R-CE, REVERIE-CE and NavRAG-CE under monocular settings.
- **p. 14 / A.1 Datasets and Experimental Details - extractive body cue:** The training is performed with a batch size of 4 and a learning rate of 1e-4.
- **p. 9 / 4 Experiments - extractive body cue:** Most navigation episodes can be completed within 20 to 40 navigation steps, our navigation system supports real-time 3D representation updates and navigation action prediction for ...
- **p. 14 / A.1 Datasets and Experimental Details - extractive body cue:** To mitigate memory consumption and enable efficient training of large models, we employ the Adafactor optimizer [58] in conjunction with Gradient Checkpointing [59].

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** summary, main, contributions, include, Dynam3D, multi-level, patch-instance-zone, representation, model, performs, online, instance, zone-level, encoding, real-time, hierarchical, updates, dynamic, environments, introduce.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Methods Pre-exploration Lifelong Memory R2R-CE Val REVERIE-CE Val NE↓OSR↑SR↑SPL↑NE↓OSR↑SR↑SPL↑ NaVid [5] × × 5.47 49.1 37.4 35.9 6.74 36.3 26.6 20.8 g3D-LF ... | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Global / local decision | Compared to prior state-of-the-art methods, e.g., g3D-LF and Uni-NaVid, our Dynam3D achieves an improvement of nearly 5% in navigation success rate (SR). | p. 7 (4 Experiments), p. 8 (4 Experiments) |
| Motion execution / recovery | Our Dynam3D still demonstrates substantial improvements, outperforming NaVid by over 13% in Success Rate (SR) on REVERIE-CE and by over 5% on ... | p. 7 (4 Experiments), p. 7 (4 Experiments) |

## Failure and Ablation Link

- **p. 9 / 4 Experiments - extractive body cue:** 4.5 Ablation Study Table 6 reports our ablation results.
- **p. 9 / 4 Experiments - extractive body cue:** The navigation performance significantly decreases without Subspace Alignment supervision (Table 6, row 3), highlighting the limitations of naive CLIP feature distillation for 3D instance supervision.
- **p. 14 / A.1 Datasets and Experimental Details - extractive body cue:** After removing samples with impassable paths, we obtain 4M+ instruction-trajectory pairs in continuous settings.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Different vision-language large models for monocular VLN tasks. Compared to previous video-based representations (a), our Dynam3D (b) adopts dynamic hierarchical 3D representations offering ...
- **p. 9 / 4 Experiments - extractive body cue:** The navigation performance significantly decreases without Subspace Alignment supervision (Table 6, row 3), highlighting the limitations of naive CLIP feature distillation for 3D instance supervision.
- **p. 8 / 4 Experiments - extractive body cue:** In the dynamic setting (Figure 4 and Table 5), the target is manually moved to another location once the robot reach within two meters of ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (Abstract), objective p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), temporal p. 9 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 1 (Abstract), p. 2 (1 Introduction), p. 7 (4 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
