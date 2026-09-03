# Method - Octopi: Object Property Reasoning with Large Tactile-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2405.02794; PDF retrieval source: https://arxiv.org/pdf/2405.02794. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (III. PHYSICLEAR - TACTILE AND PHYSICAL), p. 4 (IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED), p. 1 (Abstract), p. 6 (IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED), p. 5 (IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED), p. 5 (IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED)): Our framework consists of CLIP's visual encoder, a projection module with two linear layers, and Vicuna v1.5 as the LLM.

## Method Body Digest

- **p. 4 / III. PHYSICLEAR - TACTILE AND PHYSICAL - extractive body cue:** Our framework consists of CLIP's visual encoder, a projection module with two linear layers, and Vicuna v1.5 as the LLM.
- **p. 4 / IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED - extractive body cue:** We leverage the capabilities of pre-trained vision models, notably the CLIP [39] visual encoder ViT-L/14, as the foundation for our tactile encoder to derive meaningful ...
- **p. 1 / Abstract - extractive body cue:** We then introduce OCTOPI, a system that leverages both tactile representation learning and large vision-language models to predict and reason about tactile inputs with minimal ...
- **p. 6 / IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED - extractive body cue:** Tactile Feature Alignment We discard the fine-tuned CLIP's classification layers and use the outputs from its visual encoder as output embeddings.
- **p. 5 / IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED - extractive body cue:** We list the three scenarios we use to evaluate our model's physical reasoning capabilities.
- **p. 5 / IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED - extractive body cue:** We follow a three-step training methodology: (i) encoder fine-tuning, (ii) tactile feature alignment, and (iii) end-to-end fine-tuning.
- **p. 6 / 3) Can OCTOPI's understanding of the physical properties - extractive body cue:** We randomly sampled 5 frames from these salient frames during training and selected 5 frames at uniform intervals from the first salient frame during evaluation.
- **p. 6 / IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED - extractive body cue:** Finally, we add three separate classification heads to ViFiCLIP, each of which predicts a label for one property (i.e. hardness, roughness or bumpiness), and train ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** PHYSICLEAR and OCTOPI (with key contributions starred).
- **p. 2 / I. INTRODUCTION - extractive body cue:** Dataset Property Label Availability Property Diversity Object Diversity Material Diversity Hardness Dataset (2016) [59] Yes (only hardness) Yes Yes Medium Clothing Dataset (2018) [61] Yes ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In experiments, we show that OCTOPI is able to use its tactile modality to predict object properties and reason about scenarios including avocado ripeness.

## Source Evidence Cues

- **p. 4 / III. PHYSICLEAR - TACTILE AND PHYSICAL - extractive body cue:** Our framework consists of CLIP's visual encoder, a projection module with two linear layers, and Vicuna v1.5 as the LLM.
- **p. 4 / IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED - extractive body cue:** We leverage the capabilities of pre-trained vision models, notably the CLIP [39] visual encoder ViT-L/14, as the foundation for our tactile encoder to derive meaningful ...
- **p. 1 / Abstract - extractive body cue:** We then introduce OCTOPI, a system that leverages both tactile representation learning and large vision-language models to predict and reason about tactile inputs with minimal ...
- **p. 6 / IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED - extractive body cue:** Tactile Feature Alignment We discard the fine-tuned CLIP's classification layers and use the outputs from its visual encoder as output embeddings.
- **p. 5 / IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED - extractive body cue:** We list the three scenarios we use to evaluate our model's physical reasoning capabilities.
- **p. 5 / IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED - extractive body cue:** We follow a three-step training methodology: (i) encoder fine-tuning, (ii) tactile feature alignment, and (iii) end-to-end fine-tuning.
- **p. 6 / 3) Can OCTOPI's understanding of the physical properties - extractive body cue:** We randomly sampled 5 frames from these salient frames during training and selected 5 frames at uniform intervals from the first salient frame during evaluation.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multi-modal contact encoding | vision과 touch를 contact feature로 결합한다 | tactile image/force, vision, proprioception | tactile encoder, calibration, fusion 또는 temporal feature extraction을 수행 | contact feature/state | Our framework consists of CLIP's visual encoder, a projection module with two linear layers, and Vicuna v1.5 as the LLM. | p. 4 (III. PHYSICLEAR - TACTILE AND PHYSICAL), p. 4 (IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED) |
| Contact / dynamics inference | contact mode와 object response를 추정한다 | contact feature와 action history | mode classifier, force/dynamics model 또는 state estimator를 update | contact/force prediction | We leverage the capabilities of pre-trained vision models, notably the CLIP [39] visual encoder ViT-L/14, as the foundation for our tactile encoder ... | p. 4 (IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED), p. 1 (Abstract) |
| Force-aware action correction | interaction feedback으로 command를 보정한다 | predicted contact와 current wrench/touch | policy/control law가 action, force 또는 grasp를 재계산 | contact-safe action/torque | We then introduce OCTOPI, a system that leverages both tactile representation learning and large vision-language models to predict and reason about tactile ... | p. 1 (Abstract), p. 6 (IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED - extractive body cue:** Finally, we add three separate classification heads to ViFiCLIP, each of which predicts a label for one property (i.e. hardness, roughness or bumpiness), and train ...
- **p. 6 / 3) Can OCTOPI's understanding of the physical properties - extractive body cue:** Training Hyperparameters Encoder fine-tuning was performed for 30 epochs using the AdamW optimizer [35] with no weight decay, a learning rate of 10-3, batch size ...
- **Formal bridge:** visual/tactile/proprioceptive contact history -> contact-aware action/force -> contact prediction/control error -> slip/contact success and safe interaction.
- **Equation/algorithm anchors:** p. 6 (IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | five, tasks, tactile, data, natural, language, instructions, inputs, Table, sensor, OCTOPI, identifies, left, avocado | tactile image/force, vision과 proprioceptive history | body cue; exact tensor/frame verify |
| State/latent | five, tasks, tactile, data, natural, language, instructions, inputs, Table, sensor | contact geometry, force state 또는 latent dynamics | body cue; notation verify |
| Action/output | PHYSICLEAR, OCTOPI, contributions, starred, Dataset, Property, Label, Availability, Diversity, Object | grasp/contact action, force command 또는 object motion | body cue; unit/decoder verify |
| Objective/constraint | Finally, three, separate, classification, heads, ViFiCLIP, predicts, label, property, hardness | contact prediction/control error | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / III. PHYSICLEAR - TACTILE AND PHYSICAL - extractive body cue:** All five tasks use tactile data and natural language instructions as inputs (Table IV).
- **p. 1 / I. INTRODUCTION - extractive body cue:** Using inputs from its tactile sensor, OCTOPI identifies the left avocado as softer.
- **p. 1 / Abstract - extractive body cue:** Although these works have demonstrated success on a variety of physical reasoning tasks, they are limited to physical properties that can be inferred from visual ...
- **p. 3 / III. PHYSICLEAR - TACTILE AND PHYSICAL - extractive body cue:** Dataset Collection & Annotation To facilitate the grounding of our physical reasoning on tactile inputs, we collected a dataset of 74 everyday objects, totalling 408 ...
- **p. 4 / III. PHYSICLEAR - TACTILE AND PHYSICAL - extractive body cue:** The language instructions are variants of "Describe the physical properties of <tact start>T1, ..., TN<tact end>." The unstructured description is generated using ChatGPT 3.5 and ...
- **p. 5 / IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED - extractive body cue:** Encoder Fine-tuning Existing LVLM models take natural videos as input and can use CLIP's visual encoder without modification.
- **p. 5 / IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED - extractive body cue:** However, our work involves vision-based tactile inputs, which marks a significant distribution shift from natural images, necessitating
- **Normalized interface:** observation=tactile image/force, vision과 proprioceptive history; state=contact geometry, force state 또는 latent dynamics; output/action=grasp/contact action, force command 또는 object motion.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | contact episode 또는 action chunk horizon; contact event timing이 핵심이다. | We evaluated OCTOPI's physical understanding with the same single-step prompts used during training and on 500 question-answer pairs in total across the ... | episode/sequence/action-chunk boundary |
| Rate / latency | tactile sampling/control loop가 visual policy rate와 다를 수 있다; numeric values 확인 필요. | Since the tactile data is in video form, we follow prior LVLM work and represent it as a sequence of frames: X1, ... | Hz/fps, inference time and control rate |
| Memory | recent tactile/force history와 visual state; recurrent memory 여부 확인 필요. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | sensor fusion, contact inference와 high-frequency correction이 latency를 결정한다. | Training Hyperparameters Encoder fine-tuning was performed for 30 epochs using the AdamW optimizer [35] with no weight decay, a learning rate of ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED - extractive body cue:** We leverage the capabilities of pre-trained vision models, notably the CLIP [39] visual encoder ViT-L/14, as the foundation for our tactile encoder to derive meaningful ...
- **p. 1 / Abstract - extractive body cue:** We then introduce OCTOPI, a system that leverages both tactile representation learning and large vision-language models to predict and reason about tactile inputs with minimal ...
- **p. 6 / IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED - extractive body cue:** Tactile Feature Alignment We discard the fine-tuned CLIP's classification layers and use the outputs from its visual encoder as output embeddings.
- **p. 5 / IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED - extractive body cue:** We follow a three-step training methodology: (i) encoder fine-tuning, (ii) tactile feature alignment, and (iii) end-to-end fine-tuning.
- **p. 6 / 3) Can OCTOPI's understanding of the physical properties - extractive body cue:** We randomly sampled 5 frames from these salient frames during training and selected 5 frames at uniform intervals from the first salient frame during evaluation.
- **p. 6 / 3) Can OCTOPI's understanding of the physical properties - extractive body cue:** Training Hyperparameters Encoder fine-tuning was performed for 30 epochs using the AdamW optimizer [35] with no weight decay, a learning rate of 10-3, batch size ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** framework, consists, CLIP, visual, encoder, projection, module, linear, layers, Vicuna, LLM, leverage, capabilities, pre-trained, vision, models, notably, ViT-L/14, foundation, tactile.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multi-modal contact encoding | To address the above questions, we evaluated OCTOPI using (i) accuracy on the physical understanding tasks in PHYSICLEAR's test set, (ii) accuracy ... | p. 6 (VI. EXPERIMENTAL RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS) |
| Contact / dynamics inference | OCTOPI13b outperforms OCTOPI-7b by 6.96% on PC, 9.33% on PSS and 16.04% on POM. | p. 7 (VI. EXPERIMENTAL RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS) |
| Force-aware action correction | For both OCTOPI7b and OCTOPI-13b, including the object property significantly improves performance, which supports our overall hypothesis that leveraging these properties is ... | p. 7 (VI. EXPERIMENTAL RESULTS), p. 8 (VI. EXPERIMENTAL RESULTS) |

## Failure and Ablation Link

- **p. 7 / VI. EXPERIMENTAL RESULTS - extractive body cue:** Further, we explored the effect of using physical property descriptions by fine-tuning both OCTOPI-7b and OCTOPI13b on the physical understanding tasks without intermediate physical property ...
- **p. 8 / VI. EXPERIMENTAL RESULTS - extractive body cue:** CLIP Fine-tuning Ablation Results on Object Property Prediction.
- **p. 7 / VI. EXPERIMENTAL RESULTS - extractive body cue:** It reasons about the rice state correctly without being trained to do so.
- **p. 8 / VI. EXPERIMENTAL RESULTS - extractive body cue:** Unlike the PHYSICLEAR dataset, these tactile videos are collected with only pressing and without any rotation.
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2. PHYSICLEAR and OCTOPI (with key contributions starred). We collect tactile videos for everyday household objects by hand with two exploratory procedures: pressing and ...
- **p. 17 / Figure/Table caption - extractive body cue:** Fig. 6. Confusion Matrices for the CLIP Classifier's Physical Property Predictions. We visualize the confusion matrices for the fine-tuned CLIP classifier's physical property predictions on ...
- **p. 17 / Figure/Table caption - extractive body cue:** Fig. 7. Visualizations of CLIP Visual Encoder's Embeddings. We visualize the fine-tuned CLIP visual encoder's output embeddings for each tactile video sample for each physical ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (III. PHYSICLEAR - TACTILE AND PHYSICAL), p. 4 (IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED), p. 1 (Abstract), p. 6 (IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED), p. 5 (IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED), p. 5 (IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED), objective p. 6 (IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED), p. 6 (3) Can OCTOPI's understanding of the physical properties), temporal p. 7 (VI. EXPERIMENTAL RESULTS), p. 4 (III. PHYSICLEAR - TACTILE AND PHYSICAL), p. 4 (III. PHYSICLEAR - TACTILE AND PHYSICAL), p. 6 (3) Can OCTOPI's understanding of the physical properties), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Tactile Feature Alignment We discard the fine-tuned CLIP's classification layers and use the outputs from its visual encoder as output embeddings. (p. 6, IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED).
- **Objective/update evidence:** Training Hyperparameters Encoder fine-tuning was performed for 30 epochs using the AdamW optimizer [35] with no weight decay, a learning rate of 10-3, batch size of 32, and a cosine ... (p. 6, 3) Can OCTOPI's understanding of the physical properties).
- **Temporal/runtime evidence:** We evaluated OCTOPI's physical understanding with the same single-step prompts used during training and on 500 question-answer pairs in total across the three tasks. (p. 7, VI. EXPERIMENTAL RESULTS).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
