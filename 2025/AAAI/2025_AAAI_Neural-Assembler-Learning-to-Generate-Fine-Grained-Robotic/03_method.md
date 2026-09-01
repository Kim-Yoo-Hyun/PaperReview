# Method - Neural Assembler: Learning to Generate Fine-Grained Robotic Assembly Instructions from Multi-View Images

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ojs.aaai.org/index.php/AAAI/article/view/33613; PDF retrieval source: https://ojs.aaai.org/index.php/AAAI/article/view/33613. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 13 (A.2 Implementation Details), p. 12 (A.2 Implementation Details), p. 13 (A.2 Implementation Details), p. 12 (A.2 Implementation Details)): Model Architecture A pre-trained Vision Transformer (ViT-B/16) processes an image of size 224×224, yielding image features of dimension 768×(196+1).

## Method Body Digest

- **p. 13 / A.2 Implementation Details - extractive body cue:** Model Architecture A pre-trained Vision Transformer (ViT-B/16) processes an image of size 224×224, yielding image features of dimension 768×(196+1).
- **p. 12 / A.2 Implementation Details - extractive body cue:** We use the pre-trained ViT-B/16 weights and fine-tune it with the learning rate setting to the same value as other modules.
- **p. 13 / A.2 Implementation Details - extractive body cue:** These features are then transformed via a fully connected layer into a feature space of 256 × (196 + 1), where 196 represents the number ...
- **p. 12 / A.2 Implementation Details - extractive body cue:** Hyperparameters For training loss: L = α · Lcount + β · Lgraph + Lpose, (6) Lpose = Lkeypoint + Lmask + γ1Lrotation (7) + ...
- **p. 1 / 1 Introduction - extractive body cue:** The goal of the task is to generate a sequence of fine-grained assembly instructions, encompassing all parameters-such as component types, geometric poses of each component, ...
- **p. 2 / 1 Introduction - extractive body cue:** Taking multi-view images and a 3-D component library as input, Neural Assembler not only identifies each component from images but also determines its 3D pose ...
- **p. 2 / 1 Introduction - extractive body cue:** Neural Assembler Object library with Shape / Texture Object Relation Graph 0 1 6 8 7 2 9 3 4 5 0 1 4 2 ...
- **p. 1 / 1 Introduction - extractive body cue:** Given that certain components in the 3D model might be entirely obscured from specific viewpoints, we employ multi-view images (e.g., typically 4 in this study) ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** For this novel task, we propose an end-to-end neural network, dubbed as Neural Assembler.
- **p. 2 / 1 Introduction - extractive body cue:** We present two datasets for the proposed image-guided assembly task, namely the CLEVR-Assembly dataset and LEGO-Assembly dataset.

## Source Evidence Cues

- **p. 13 / A.2 Implementation Details - extractive body cue:** Model Architecture A pre-trained Vision Transformer (ViT-B/16) processes an image of size 224×224, yielding image features of dimension 768×(196+1).
- **p. 12 / A.2 Implementation Details - extractive body cue:** We use the pre-trained ViT-B/16 weights and fine-tune it with the learning rate setting to the same value as other modules.
- **p. 13 / A.2 Implementation Details - extractive body cue:** These features are then transformed via a fully connected layer into a feature space of 256 × (196 + 1), where 196 represents the number ...
- **p. 12 / A.2 Implementation Details - extractive body cue:** Hyperparameters For training loss: L = α · Lcount + β · Lgraph + Lpose, (6) Lpose = Lkeypoint + Lmask + γ1Lrotation (7) + ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | Model Architecture A pre-trained Vision Transformer (ViT-B/16) processes an image of size 224×224, yielding image features of dimension 768×(196+1). | p. 13 (A.2 Implementation Details), p. 12 (A.2 Implementation Details) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | We use the pre-trained ViT-B/16 weights and fine-tune it with the learning rate setting to the same value as other modules. | p. 12 (A.2 Implementation Details), p. 13 (A.2 Implementation Details) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | These features are then transformed via a fully connected layer into a feature space of 256 × (196 + 1), where 196 ... | p. 13 (A.2 Implementation Details), p. 12 (A.2 Implementation Details) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 12 / A.2 Implementation Details - extractive body cue:** Hyperparameters For training loss: L = α · Lcount + β · Lgraph + Lpose, (6) Lpose = Lkeypoint + Lmask + γ1Lrotation (7) + ...
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 12 (A.2 Implementation Details).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | goal, task, generate, sequence, fine-grained, assembly, instructions, encompassing, parameters-such, component, types, geometric, poses, order-in | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | goal, task, generate, sequence, fine-grained, assembly, instructions, encompassing, parameters-such, component | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | novel, task, end-to-end, neural, network, dubbed, Assembler, present, datasets, image-guided | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | Hyperparameters, training, loss, Lcount, Lgraph, Lpose, Lkeypoint, Lmask, Lrotation, Lshape | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1 Introduction - extractive body cue:** The goal of the task is to generate a sequence of fine-grained assembly instructions, encompassing all parameters-such as component types, geometric poses of each component, ...
- **p. 2 / 1 Introduction - extractive body cue:** Taking multi-view images and a 3-D component library as input, Neural Assembler not only identifies each component from images but also determines its 3D pose ...
- **p. 2 / 1 Introduction - extractive body cue:** Neural Assembler Object library with Shape / Texture Object Relation Graph 0 1 6 8 7 2 9 3 4 5 0 1 4 2 ...
- **p. 1 / 1 Introduction - extractive body cue:** Given that certain components in the 3D model might be entirely obscured from specific viewpoints, we employ multi-view images (e.g., typically 4 in this study) ...
- **p. 13 / A.2 Implementation Details - extractive body cue:** Concurrently, the PointNet processes the point cloud of size N1 × 1024 × 3 to extract N1 × 256 shape features of the brick.
- **p. 12 / A.2 Implementation Details - extractive body cue:** Details of 3D Pose Inference The center of each brick is defined as the keypoint.
- **p. 12 / A.2 Implementation Details - extractive body cue:** For 3D pose estimation, we select the perspective with a confidence score greater than a threshold and extract its 12
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | For example, The SLAM (simultaneous localization and mapping) task requires reconstructing the 3D geometric scene and estimating camera poses given a sequence ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | This comparison aims to highlight the enhanced predictive capabilities our GCN model brings to complex assembly sequences. | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | Training is conducted on an RTX 3090 GPU using AdamW, with an initial rate of 5e-4, decaying by 0.8 per epoch, a ... | hardware, batch and throughput |

## Training vs Inference

- **p. 13 / A.2 Implementation Details - extractive body cue:** Model Architecture A pre-trained Vision Transformer (ViT-B/16) processes an image of size 224×224, yielding image features of dimension 768×(196+1).
- **p. 12 / A.2 Implementation Details - extractive body cue:** We use the pre-trained ViT-B/16 weights and fine-tune it with the learning rate setting to the same value as other modules.
- **p. 12 / A.2 Implementation Details - extractive body cue:** Hyperparameters For training loss: L = α · Lcount + β · Lgraph + Lpose, (6) Lpose = Lkeypoint + Lmask + γ1Lrotation (7) + ...
- **p. 6 / 4 Experiments - extractive body cue:** Training is conducted on an RTX 3090 GPU using AdamW, with an initial rate of 5e-4, decaying by 0.8 per epoch, a weight decay of ...
- **p. 12 / A.2 Implementation Details - extractive body cue:** We use the pre-trained ViT-B/16 weights and fine-tune it with the learning rate setting to the same value as other modules.
- **p. 12 / A.2 Implementation Details - extractive body cue:** Hyperparameters For training loss: L = α · Lcount + β · Lgraph + Lpose, (6) Lpose = Lkeypoint + Lmask + γ1Lrotation (7) + ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Model, Architecture, pre-trained, Vision, Transformer, ViT-B/16, processes, image, size, yielding, features, dimension, weights, fine-tune, learning, rate, setting, same, value, other.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | (2022b) 7.3 21.8 Ours 34.2 58.5 Real-World Dataset LSTM Graves and Graves (2012) 7.3 21.8 DETR3D Wang et al. | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Baseline harness | Neural Assembler outperforms baseline models in all metrics considered. | p. 7 (4 Experiments), p. 6 (4 Experiments) |
| Metric / failure reporting | As indicated in Table 3, the Neural Assembler achieves performance in real-world experiments close to the results obtained in simulated environments, demonstrating ... | p. 9 (4 Experiments), p. 7 (4 Experiments) |

## Failure and Ablation Link

- **p. 7 / 4 Experiments - extractive body cue:** Without scene consensus, it is difficult for the model to integrate information from multi-view images to obtain the overall information of each brick.
- **p. 6 / 4 Experiments - extractive body cue:** Furthermore, for the object pose estimation component, our methodology is rigorously benchmarked against DETR3D Wang et al.
- **p. 8 / 4 Experiments - extractive body cue:** (2022b) 2.4 12.8 Ours 22.0 50.5 Table 3: The performance of the fine-tuned model on the novel simulated dataset and real-world dataset.
- **p. 9 / 4 Experiments - extractive body cue:** This data facilitated the creation of a synthetic dataset, used for fine-tuning the model initially trained on the CLEVR-Assembly dataset.
- **p. 13 / A.4 Real-World Robotic Experiment - extractive body cue:** The manipulation component involves a Robotiq 2F-85 two-finger gripper, providing adept grasping capabilities.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Schematic illustration of the proposed Neural Assembler. See Section 3 for more details. integrate information from images captured from multiple perspectives. Secondly, estimating ...
- **p. 12 / A.2 Implementation Details - extractive body cue:** We use the pre-trained ViT-B/16 weights and fine-tune it with the learning rate setting to the same value as other modules.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 13 (A.2 Implementation Details), p. 12 (A.2 Implementation Details), p. 13 (A.2 Implementation Details), p. 12 (A.2 Implementation Details), objective p. 12 (A.2 Implementation Details), temporal p. 2 (2 Related work), p. 6 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
