# Method - SUGAR: Pre-training 3D Visual Representations for Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Chen_SUGAR_Pre-training_3D_Visual_Representations_for_Robotics_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_SUGAR_Pre-training_3D_Visual_Representations_for_Robotics_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (1) OBJ ONLY which only includes ground truth segmented), p. 6 (1) OBJ ONLY which only includes ground truth segmented), p. 7 (4.2. Referring Expression Grounding), p. 1 (1. Introduction)): To jointly train multiple properties, we propose a versatile transformer-based model comprising a point cloud encoder and a prompt-based decoder.

## Method Body Digest

- **p. 2 / 1. Introduction - extractive body cue:** To jointly train multiple properties, we propose a versatile transformer-based model comprising a point cloud encoder and a prompt-based decoder.
- **p. 2 / 1. Introduction - extractive body cue:** In summary, the contributions of our work are three-fold: • We present SUGAR - a framework with versatile transformer architecture for 3D point cloud representation ...
- **p. 6 / 1) OBJ ONLY which only includes ground truth segmented - extractive body cue:** First, we only use a small transformer model which may not have sufficient capacity to jointly solve the five pre-training tasks when the pre-training data ...
- **p. 6 / 1) OBJ ONLY which only includes ground truth segmented - extractive body cue:** As in the CML pretraining task, we use [img] and [txt] prompt tokens to extract point cloud features that are in the same space of ...
- **p. 7 / 4.2. Referring Expression Grounding - extractive body cue:** We use Ne = 1536 for our SUGAR models if not stated otherwise.
- **p. 1 / 1. Introduction - extractive body cue:** We introduce SUGAR , a pre-training framework for robotic-related tasks, which learns semantic, geometry and affordance on both single- and multi-object scenes. robotics.
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we introduce a novel 3D pre-training framework for robotics named SUGAR that captures semantic, geometric and affordance properties of objects through ...
- **p. 1 / Abstract - extractive body cue:** We underscore the importance of cluttered scenes in 3D representation learning, and automatically construct a multi-object dataset benefiting from cost-free supervision in simulation.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In summary, the contributions of our work are three-fold: • We present SUGAR - a framework with versatile transformer architecture for 3D point cloud representation ...
- **p. 2 / 1. Introduction - extractive body cue:** To enhance the capability of 3D representation in robotics, we propose SUGAR - a novel pre-training framework that learns semantics, geometry and affordance properties of ...
- **p. 1 / 1. Introduction - extractive body cue:** We introduce SUGAR , a pre-training framework for robotic-related tasks, which learns semantic, geometry and affordance on both single- and multi-object scenes. robotics.

## Source Evidence Cues

- **p. 2 / 1. Introduction - extractive body cue:** To jointly train multiple properties, we propose a versatile transformer-based model comprising a point cloud encoder and a prompt-based decoder.
- **p. 2 / 1. Introduction - extractive body cue:** In summary, the contributions of our work are three-fold: • We present SUGAR - a framework with versatile transformer architecture for 3D point cloud representation ...
- **p. 6 / 1) OBJ ONLY which only includes ground truth segmented - extractive body cue:** First, we only use a small transformer model which may not have sufficient capacity to jointly solve the five pre-training tasks when the pre-training data ...
- **p. 6 / 1) OBJ ONLY which only includes ground truth segmented - extractive body cue:** As in the CML pretraining task, we use [img] and [txt] prompt tokens to extract point cloud features that are in the same space of ...
- **p. 7 / 4.2. Referring Expression Grounding - extractive body cue:** We use Ne = 1536 for our SUGAR models if not stated otherwise.
- **p. 1 / 1. Introduction - extractive body cue:** We introduce SUGAR , a pre-training framework for robotic-related tasks, which learns semantic, geometry and affordance on both single- and multi-object scenes. robotics.
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we introduce a novel 3D pre-training framework for robotics named SUGAR that captures semantic, geometric and affordance properties of objects through ...
- **Detected method headings:** 3.1. Network Architecture (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | To jointly train multiple properties, we propose a versatile transformer-based model comprising a point cloud encoder and a prompt-based decoder. | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | In summary, the contributions of our work are three-fold: • We present SUGAR - a framework with versatile transformer architecture for 3D ... | p. 2 (1. Introduction), p. 6 (1) OBJ ONLY which only includes ground truth segmented) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | First, we only use a small transformer model which may not have sufficient capacity to jointly solve the five pre-training tasks when ... | p. 6 (1) OBJ ONLY which only includes ground truth segmented), p. 6 (1) OBJ ONLY which only includes ground truth segmented) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / Abstract - extractive body cue:** We underscore the importance of cluttered scenes in 3D representation learning, and automatically construct a multi-object dataset benefiting from cost-free supervision in simulation.
- **p. 1 / 1. Introduction - extractive body cue:** Several recent works lift pretrained 2D features to the 3D space [20, 34, 56, 89], which compromise efficiency due to processing multi-view images and do ...
- **p. 2 / 1. Introduction - extractive body cue:** We adopt curriculum learning to progressively train SUGAR on single- and multi-object scenes.
- **p. 6 / 1) OBJ ONLY which only includes ground truth segmented - extractive body cue:** Our model however learns to reconstruct both geometry structures and colors in masked point modeling, taking advantage of both geometric and texture information for semantic ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 7 (4.2. Referring Expression Grounding).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | summary, contributions, three-fold, present, SUGAR, framework, versatile, transformer, architecture, point, cloud, representation, learning, cluttered | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | summary, contributions, three-fold, present, SUGAR, framework, versatile, transformer, architecture, point | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | summary, contributions, three-fold, present, SUGAR, framework, versatile, transformer, architecture, point | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | underscore, importance, cluttered, scenes, representation, learning, automatically, construct, multi-object, dataset | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** In summary, the contributions of our work are three-fold: • We present SUGAR - a framework with versatile transformer architecture for 3D point cloud representation ...
- **p. 7 / 4.3. Language-guided Robotic Manipulation - extractive body cue:** This task aims to train a policy that can follow natural language instruction to perform manipulation tasks.
- **p. 2 / 1. Introduction - extractive body cue:** The first task is zeroshot 3D object recognition [44], a benchmark task for 3D shape understanding; the second task is referring expression grounding [46, 79] ...
- **p. 7 / 4.2. Referring Expression Grounding - extractive body cue:** RoboRefit contains natural scenes and noisy depth observations.
- **p. 1 / 1. Introduction - extractive body cue:** For example, MVP [62], VIP [48] and VC-1 [49] use self-supervised learning on image or video datasets, while EmbCLIP [37], R3M [51] and Voltron [36] ...
- **p. 1 / Abstract - extractive body cue:** Experimental results show that SUGAR's 3D representation outperforms state-of-the-art 2D and 3D representations.
- **p. 6 / 1) OBJ ONLY which only includes ground truth segmented - extractive body cue:** SUGAR (single) achieves 68.0% Top1 accuracy on OBJ BG split of ScanObjectNN, outperforming state of the art by 15.4%.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Each demonstration consists of a sequence of keysteps of RGB-D image observations from three cameras and a 7-DoF action denoting the position, ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | We introduce SUGAR , a pre-training framework for robotic-related tasks, which learns semantic, geometry and affordance on both single- and multi-object scenes. ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1. Introduction - extractive body cue:** To jointly train multiple properties, we propose a versatile transformer-based model comprising a point cloud encoder and a prompt-based decoder.
- **p. 2 / 1. Introduction - extractive body cue:** In summary, the contributions of our work are three-fold: • We present SUGAR - a framework with versatile transformer architecture for 3D point cloud representation ...
- **p. 6 / 1) OBJ ONLY which only includes ground truth segmented - extractive body cue:** First, we only use a small transformer model which may not have sufficient capacity to jointly solve the five pre-training tasks when the pre-training data ...
- **p. 6 / 1) OBJ ONLY which only includes ground truth segmented - extractive body cue:** As in the CML pretraining task, we use [img] and [txt] prompt tokens to extract point cloud features that are in the same space of ...
- **p. 1 / 1. Introduction - extractive body cue:** We introduce SUGAR , a pre-training framework for robotic-related tasks, which learns semantic, geometry and affordance on both single- and multi-object scenes. robotics.
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we introduce a novel 3D pre-training framework for robotics named SUGAR that captures semantic, geometric and affordance properties of objects through ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** jointly, train, multiple, properties, versatile, transformer-based, model, comprising, point, cloud, encoder, prompt-based, decoder, summary, contributions, three-fold, present, SUGAR, framework, transformer.
- **Relevant PDF headings:** 3.1. Network Architecture (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | ScanObjectNN is one of the most challenging 3D datasets, consisting of 15 common categories and 587 real-world 3D scans in the test ... | p. 5 (4.1. Zero-shot Object Recognition), p. 5 (4. Evaluation on Robotic-related Tasks) |
| Action / skill decoding | The objects are synthetic 3D models without colors. | p. 5 (4.1. Zero-shot Object Recognition), p. 5 (4.1. Zero-shot Object Recognition) |
| Receding execution / feedback | Figure 5. Performance of training with 10 demonstrations. (Ens m) significantly boosts the performance of the model trained from scratch with over ... | p. 8 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 5 / 4.1. Zero-shot Object Recognition - extractive body cue:** The objects are synthetic 3D models without colors.
- **p. 5 / 4.1. Zero-shot Object Recognition - extractive body cue:** The task aims to classify unseen 3D objects without training on those specific categories.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Zero-shot object recognition performance on three benchmarks. The Top1 accuracy is reported if not specified otherwise. The blue colored results in brackets on ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (1) OBJ ONLY which only includes ground truth segmented), p. 6 (1) OBJ ONLY which only includes ground truth segmented), p. 7 (4.2. Referring Expression Grounding), p. 1 (1. Introduction), objective p. 1 (Abstract), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 6 (1) OBJ ONLY which only includes ground truth segmented), temporal p. 8 (4.3. Language-guided Robotic Manipulation), p. 1 (1. Introduction), p. 1 (Abstract), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Network Architecture).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
