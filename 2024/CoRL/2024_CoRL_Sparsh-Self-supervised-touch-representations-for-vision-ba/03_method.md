# Method - Sparsh: Self-supervised touch representations for vision-based tactile sensing

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2410.24090; PDF retrieval source: https://arxiv.org/pdf/2410.24090. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction), p. 8 (8 Discussion), p. 8 (8 Discussion), p. 2 (1 Introduction)): In this work, we introduce general purpose touch representations for the increasingly accessible class of vision-based tactile sensors.

## Method Body Digest

- **p. 1 / Abstract - extractive body cue:** In this work, we introduce general purpose touch representations for the increasingly accessible class of vision-based tactile sensors.
- **p. 1 / Abstract - extractive body cue:** We present Sparsh, a family of SSL models that can support various vision-based tactile sensors, alleviating the need for custom labels through pre-training on 460k+ ...
- **p. 2 / 1 Introduction - extractive body cue:** For example, feature extractors trained on GelSight with markers may not transfer to other sensors, and encoders optimized for texture recognition [15] may not be ...
- **p. 8 / 8 Discussion - extractive body cue:** Open-source tactile datasets we considered in this study predominantly feature discrete contact interactions.
- **p. 8 / 8 Discussion - extractive body cue:** Notably, models pre-trained in latent space perform better in downstream tasks when fully fine-tuned, especially in regression tasks like force and pose estimation.
- **p. 2 / 1 Introduction - extractive body cue:** TacBench a benchmark of standardized tasks to evaluate touch representations and models, and 3.
- **p. 2 / 1 Introduction - extractive body cue:** Specifically, we provide a recipe to adapt masking-based objectives from computer vision to the tactile domain, and train general-purpose touch encoders by curating a new ...
- **p. 8 / 8 Discussion - extractive body cue:** Learning touch representations in latent space is more advantageous than in pixel space, as these representations can filter out and generalize over noise or lighting ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** In this work, we introduce a family of touch representations for vision-based tactile sensors trained with SSL.
- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are as follows: 1.
- **p. 1 / Abstract - extractive body cue:** We present Sparsh, a family of SSL models that can support various vision-based tactile sensors, alleviating the need for custom labels through pre-training on 460k+ ...

## Source Evidence Cues

- **p. 1 / Abstract - extractive body cue:** In this work, we introduce general purpose touch representations for the increasingly accessible class of vision-based tactile sensors.
- **p. 1 / Abstract - extractive body cue:** We present Sparsh, a family of SSL models that can support various vision-based tactile sensors, alleviating the need for custom labels through pre-training on 460k+ ...
- **p. 2 / 1 Introduction - extractive body cue:** For example, feature extractors trained on GelSight with markers may not transfer to other sensors, and encoders optimized for texture recognition [15] may not be ...
- **p. 8 / 8 Discussion - extractive body cue:** Open-source tactile datasets we considered in this study predominantly feature discrete contact interactions.
- **p. 8 / 8 Discussion - extractive body cue:** Notably, models pre-trained in latent space perform better in downstream tasks when fully fine-tuned, especially in regression tasks like force and pose estimation.
- **p. 2 / 1 Introduction - extractive body cue:** TacBench a benchmark of standardized tasks to evaluate touch representations and models, and 3.
- **Detected method headings:** C.2 Architecture details (p. 17); C.4 Short summary of SSL methods (p. 19); Model (p. 22)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multi-modal contact encoding | vision과 touch를 contact feature로 결합한다 | tactile image/force, vision, proprioception | tactile encoder, calibration, fusion 또는 temporal feature extraction을 수행 | contact feature/state | In this work, we introduce general purpose touch representations for the increasingly accessible class of vision-based tactile sensors. | p. 1 (Abstract), p. 1 (Abstract) |
| Contact / dynamics inference | contact mode와 object response를 추정한다 | contact feature와 action history | mode classifier, force/dynamics model 또는 state estimator를 update | contact/force prediction | We present Sparsh, a family of SSL models that can support various vision-based tactile sensors, alleviating the need for custom labels through ... | p. 1 (Abstract), p. 2 (1 Introduction) |
| Force-aware action correction | interaction feedback으로 command를 보정한다 | predicted contact와 current wrench/touch | policy/control law가 action, force 또는 grasp를 재계산 | contact-safe action/torque | For example, feature extractors trained on GelSight with markers may not transfer to other sensors, and encoders optimized for texture recognition [15] ... | p. 2 (1 Introduction), p. 8 (8 Discussion) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1 Introduction - extractive body cue:** Specifically, we provide a recipe to adapt masking-based objectives from computer vision to the tactile domain, and train general-purpose touch encoders by curating a new ...
- **p. 2 / 1 Introduction - extractive body cue:** For example, feature extractors trained on GelSight with markers may not transfer to other sensors, and encoders optimized for texture recognition [15] may not be ...
- **p. 8 / 8 Discussion - extractive body cue:** Learning touch representations in latent space is more advantageous than in pixel space, as these representations can filter out and generalize over noise or lighting ...
- **Formal bridge:** visual/tactile/proprioceptive contact history -> contact-aware action/force -> contact prediction/control error -> slip/contact success and safe interaction.
- **Equation/algorithm anchors:** p. 2 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Vision-based, tactile, sensors, have, emerged, leading, form, factor, capable, capturing, images, physical, interactions, sensor-objectenvironment | tactile image/force, vision과 proprioceptive history | body cue; exact tensor/frame verify |
| State/latent | Vision-based, tactile, sensors, have, emerged, leading, form, factor, capable, capturing | contact geometry, force state 또는 latent dynamics | body cue; notation verify |
| Action/output | introduce, family, touch, representations, vision-based, tactile, sensors, trained, SSL, contributions | grasp/contact action, force command 또는 object motion | body cue; unit/decoder verify |
| Objective/constraint | Specifically, provide, recipe, adapt, masking-based, objectives, computer, vision, tactile, domain | contact prediction/control error | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive body cue:** Vision-based tactile sensors [1, 2, 3, 4] have emerged as the leading form factor capable of capturing images of physical interactions at the sensor-objectenvironment interface, ...
- **p. 8 / 8 Discussion - extractive body cue:** In particular, we find Sparsh (DINO) is well suited for physics-based tasks like force and pose estimation, while Sparsh (IJEPA) performs better at touch semantic ...
- **p. 2 / 1 Introduction - extractive body cue:** The prevailing approach to incorporating vision-based tactile sensors in robot tasks is to train custom models using labeled data [6, 12, 13, 14] to estimate ...
- **p. 8 / 8 Discussion - extractive body cue:** We believe that incorporating data rich in shear interactions can further improve the representations.
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce general purpose touch representations for the increasingly accessible class of vision-based tactile sensors.
- **p. 1 / Abstract - extractive body cue:** Collecting real data at scale with task centric ground truth labels, like contact forces and slip, is a challenge further compounded by sensors of various ...
- **Normalized interface:** observation=tactile image/force, vision과 proprioceptive history; state=contact geometry, force state 또는 latent dynamics; output/action=grasp/contact action, force command 또는 object motion.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | contact episode 또는 action chunk horizon; contact event timing이 핵심이다. | Due to covariate shift [72] in behavior cloning, prediction errors can accumulate over time; therefore, we report position error between the predicted ... | episode/sequence/action-chunk boundary |
| Rate / latency | tactile sampling/control loop가 visual policy rate와 다를 수 있다; numeric values 확인 필요. | Although all models detect slip from the 80 ms history of tactile data, Sparsh (VJEPA) benefits from a detailed temporal perspective, as ... | Hz/fps, inference time and control rate |
| Memory | recent tactile/force history와 visual state; recurrent memory 여부 확인 필요. | Although all models detect slip from the 80 ms history of tactile data, Sparsh (VJEPA) benefits from a detailed temporal perspective, as ... | window and reset |
| Compute | sensor fusion, contact inference와 high-frequency correction이 latency를 결정한다. | Although all models detect slip from the 80 ms history of tactile data, Sparsh (VJEPA) benefits from a detailed temporal perspective, as ... | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / Abstract - extractive body cue:** We present Sparsh, a family of SSL models that can support various vision-based tactile sensors, alleviating the need for custom labels through pre-training on 460k+ ...
- **p. 2 / 1 Introduction - extractive body cue:** For example, feature extractors trained on GelSight with markers may not transfer to other sensors, and encoders optimized for texture recognition [15] may not be ...
- **p. 8 / 8 Discussion - extractive body cue:** Notably, models pre-trained in latent space perform better in downstream tasks when fully fine-tuned, especially in regression tasks like force and pose estimation.
- **p. 2 / 1 Introduction - extractive body cue:** Specifically, we provide a recipe to adapt masking-based objectives from computer vision to the tactile domain, and train general-purpose touch encoders by curating a new ...
- **p. 8 / 8 Discussion - extractive body cue:** Fine-tuning Sparsh encoders is another method of assessing the quality of pre-trained representations.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** introduce, general, purpose, touch, representations, increasingly, accessible, class, vision-based, tactile, sensors, present, Sparsh, family, SSL, models, support, various, alleviating, need.
- **Relevant PDF headings:** C.2 Architecture details (p. 17); C.4 Short summary of SSL methods (p. 19); Model (p. 22).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multi-modal contact encoding | Finally, we construct TacBench, a benchmark consisting of six touch-centric tasks that cover the space of relevant problems on tactile properties such ... | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Contact / dynamics inference | Figure 2: (a) We curate new and existing datasets of vision-based tactile sensors to train touch representations by adapting state-of-the-art SSL vision ... | p. 3 (Figure/Table caption), p. 1 (Front matter) |
| Force-aware action correction | Figure 4: Summary of results comparing Sparsh and E2E on [T1]-[T6] tasks in TacBench across varying amounts of labeled data. Pre-training with ... | p. 7 (Figure/Table caption), p. 8 (8 Discussion) |

## Failure and Ablation Link

- **p. 18 / Figure/Table caption - extractive body cue:** Table 2: Number of parameters and inference time for Sparsh backbones All the models are pretrained without a [cls] token. For DINO, which decodes the ...
- **p. 24 / Figure/Table caption - extractive body cue:** Table 7: Performance of models on slip detection task under different budgets of training data. We use F1 score as metric, given that it ensures ...
- **p. 31 / Figure/Table caption - extractive body cue:** Figure 17: Additional evaluations of Sparsh representations on TacBench. We compare frozen Sparsh ViT-base (most left), Sparsh fully and partially fine-tuned (middle) and finally (most ...
- **p. 29 / Figure/Table caption - extractive body cue:** Table 13: Performance of Sparsh across TacBench and comparison between SSL approaches. E Sparsh ablations E.1 TacBench evaluations via fine-tuning Fine-tuning the Sparsh encoders is ...
- **p. 2 / 1 Introduction - extractive body cue:** However, this can be inefficient and results in repeated effort across different type of sensors like GelSight 2017 [1] (with markers) and DIGIT [3] (without ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: (a) We curate new and existing datasets of vision-based tactile sensors to train touch representations by adapting state-of-the-art SSL vision methods to the ...
- **p. 8 / 8 Discussion - extractive body cue:** Such ablations could provide guidance on improving their quality for downstream tasks.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction), p. 8 (8 Discussion), p. 8 (8 Discussion), p. 2 (1 Introduction), objective p. 2 (1 Introduction), p. 2 (1 Introduction), p. 8 (8 Discussion), temporal p. 7 (2 Related work), p. 5 (2 Related work), p. 2 (2 Related work), p. 2 (2 Related work), p. 3 (2 Related work), p. 4 (2 Related work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
