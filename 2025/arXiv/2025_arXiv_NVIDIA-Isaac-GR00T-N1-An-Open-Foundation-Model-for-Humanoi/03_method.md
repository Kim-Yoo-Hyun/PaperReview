# Method - NVIDIA Isaac GR00T N1: An Open Foundation Model for Humanoid Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (36 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://research.nvidia.com/publication/2025-03_nvidia-isaac-gr00t-n1-open-foundation-model-humanoid-robots; PDF retrieval source: https://research.nvidia.com/publication/2025-03_nvidia-isaac-gr00t-n1-open-foundation-model-humanoid-robots. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (2.1. Model Architecture), p. 8 (2.3. Training Details), p. 5 (2.2. Training Data Generation), p. 4 (2.1. Model Architecture), p. 8 (2.3. Training Details), p. 3 (2. GR00T N1 Foundation Model)): GR00T N1: An Open Foundation Model for Generalist Humanoid Robots Robot State Eagle-2 VLM Cross-Attention Self-Attention Cross-Attention Self-Attention State Encoder Action Decoder DiT Blocks Motor Action Action Encoder x N ...

## Method Body Digest

- **p. 4 / 2.1. Model Architecture - extractive body cue:** GR00T N1: An Open Foundation Model for Generalist Humanoid Robots Robot State Eagle-2 VLM Cross-Attention Self-Attention Cross-Attention Self-Attention State Encoder Action Decoder DiT Blocks Motor ...
- **p. 8 / 2.3. Training Details - extractive body cue:** Since the generated videos do not have action labels, we use either latent or inverse dynamics models (IDM) labeled actions (Baker et al., 2022) and ...
- **p. 5 / 2.2. Training Data Generation - extractive body cue:** After training, we take the encoder and use it as an inverse dynamics model; given an 𝑥𝑡and 𝑥𝑡+𝐻pair, we extract the continuous pre-quantized embedding and ...
- **p. 4 / 2.1. Model Architecture - extractive body cue:** To deal with different robot embodiment's state observation and action, we use DiT blocks with an embodiment-aware state and action encoder to embed the robot's ...
- **p. 8 / 2.3. Training Details - extractive body cue:** 2.2) used to augment our robot datasets, we use both latent actions as well as predicted actions from an inverse-dynamics model trained on the real ...
- **p. 3 / 2. GR00T N1 Foundation Model - extractive body cue:** We highlight three key features of GR00T N1: • We design a compositional model that integrates Vision-Language Model (VLM)-based reasoning module (System 2) and Diffusion ...
- **p. 5 / 2.2. Training Data Generation - extractive body cue:** In the next paragraph, we first describe how we extract latent actions from videos, which we use to extract labels for web-scaled human egocentric datasets.
- **p. 8 / 2.3. Training Details - extractive body cue:** Pre-training During the pre-training phase, GR00T N1 is trained via flow-matching loss (Equation 1) on a diverse collection of embodiments and data sources, encompassing various ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** We introduce GR00T N1, an open foundation model for generalist humanoid robots.
- **p. 2 / 1. Introduction - extractive body cue:** By unifying all data sources across the data pyramid, we construct a consistent dataset where the input consists of the robot state, visual observations, and ...
- **p. 3 / 2. GR00T N1 Foundation Model - extractive body cue:** 1) for generalization and robustness; • We train a massively multi-task, language-conditioned policy that supports a wide range of robot embodiments and enables rapid adaptation ...

## Source Evidence Cues

- **p. 4 / 2.1. Model Architecture - extractive body cue:** GR00T N1: An Open Foundation Model for Generalist Humanoid Robots Robot State Eagle-2 VLM Cross-Attention Self-Attention Cross-Attention Self-Attention State Encoder Action Decoder DiT Blocks Motor ...
- **p. 8 / 2.3. Training Details - extractive body cue:** Since the generated videos do not have action labels, we use either latent or inverse dynamics models (IDM) labeled actions (Baker et al., 2022) and ...
- **p. 5 / 2.2. Training Data Generation - extractive body cue:** After training, we take the encoder and use it as an inverse dynamics model; given an 𝑥𝑡and 𝑥𝑡+𝐻pair, we extract the continuous pre-quantized embedding and ...
- **p. 4 / 2.1. Model Architecture - extractive body cue:** To deal with different robot embodiment's state observation and action, we use DiT blocks with an embodiment-aware state and action encoder to embed the robot's ...
- **p. 8 / 2.3. Training Details - extractive body cue:** 2.2) used to augment our robot datasets, we use both latent actions as well as predicted actions from an inverse-dynamics model trained on the real ...
- **p. 3 / 2. GR00T N1 Foundation Model - extractive body cue:** We highlight three key features of GR00T N1: • We design a compositional model that integrates Vision-Language Model (VLM)-based reasoning module (System 2) and Diffusion ...
- **p. 5 / 2.2. Training Data Generation - extractive body cue:** In the next paragraph, we first describe how we extract latent actions from videos, which we use to extract labels for web-scaled human egocentric datasets.
- **Detected method headings:** 2. GR00T N1 Foundation Model (p. 3); 2.1. Model Architecture (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | GR00T N1: An Open Foundation Model for Generalist Humanoid Robots Robot State Eagle-2 VLM Cross-Attention Self-Attention Cross-Attention Self-Attention State Encoder Action Decoder ... | p. 4 (2.1. Model Architecture), p. 8 (2.3. Training Details) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | Since the generated videos do not have action labels, we use either latent or inverse dynamics models (IDM) labeled actions (Baker et ... | p. 8 (2.3. Training Details), p. 5 (2.2. Training Data Generation) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | After training, we take the encoder and use it as an inverse dynamics model; given an 𝑥𝑡and 𝑥𝑡+𝐻pair, we extract the continuous ... | p. 5 (2.2. Training Data Generation), p. 4 (2.1. Model Architecture) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 8 / 2.3. Training Details - extractive body cue:** Pre-training During the pre-training phase, GR00T N1 is trained via flow-matching loss (Equation 1) on a diverse collection of embodiments and data sources, encompassing various ...
- **p. 5 / 2.1. Model Architecture - extractive body cue:** The model prediction 𝑉𝜃(𝜑𝑡, 𝐴𝜏 𝑡, 𝑞𝑡) aims to approximate the denoising vector field 𝜖-𝐴𝑡by minimizing the following loss: ℒfm(𝜃) = E𝜏 [︀ ‖𝑉𝜃(𝜑𝑡, 𝐴𝜏 ...
- **p. 5 / 2.2. Training Data Generation - extractive body cue:** To train GR00T N1, we use a diverse set of data sources and objectives to construct the data pyramid (Fig.
- **p. 7 / 2.2. Training Data Generation - extractive body cue:** These simulation data significantly supplement the real-robot data with minimal human costs.
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 8 (2.3. Training Details), p. 5 (2.2. Training Data Generation), p. 5 (2.2. Training Data Generation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | unifying, data, sources, across, pyramid, construct, consistent, dataset, where, input, consists, robot, state, visual | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | unifying, data, sources, across, pyramid, construct, consistent, dataset, where, input | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | introduce, GR00T, open, foundation, model, generalist, humanoid, robots, unifying, data | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | Pre-training, During, phase, GR00T, trained, flow-matching, loss, Equation, diverse, collection | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** By unifying all data sources across the data pyramid, we construct a consistent dataset where the input consists of the robot state, visual observations, and ...
- **p. 3 / 1. Introduction - extractive body cue:** GR00T N1: An Open Foundation Model for Generalist Humanoid Robots Robot State "Pick up the industry object and place in yellow bin." Joint Positions Joint ...
- **p. 3 / 2. GR00T N1 Foundation Model - extractive body cue:** The model contains a vision-language backbone that encodes language and image input and a DiT-based flow-matching policy that outputs high-frequency actions.
- **p. 4 / 2.1. Model Architecture - extractive body cue:** To deal with different robot embodiment's state observation and action, we use DiT blocks with an embodiment-aware state and action encoder to embed the robot's ...
- **p. 2 / 1. Introduction - extractive body cue:** The GR00T N1 model is a Vision-Language-Action (VLA) model, which generates actions from image and language instruction input.
- **p. 4 / 2.1. Model Architecture - extractive body cue:** The model takes as input noised actions in addition to encodings of the robot's proprioceptive state, image tokens, and text tokens.
- **p. 5 / 2.1. Model Architecture - extractive body cue:** The self-attention blocks operate on noised action token embeddings 𝐴𝜏 𝑡together with state embeddings 𝑞𝑡, while cross-attention blocks allow conditioning on the vision-language token embeddings ...
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | It takes a single frame of observations as input and produces 16 action steps in one inference pass. | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | Given a ground-truth action chunk 𝐴𝑡, a flow-matching timestep 𝜏∈[0, 1] and sampled noise 𝜖∼𝒩(0, I), the noised action chunk 𝐴𝜏 𝑡is ... | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not recovered | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | Evaluation Protocol For simulated benchmark evaluation, we report the average success rate over 100 trials, taking the maximum score of the last ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 2.1. Model Architecture - extractive body cue:** GR00T N1: An Open Foundation Model for Generalist Humanoid Robots Robot State Eagle-2 VLM Cross-Attention Self-Attention Cross-Attention Self-Attention State Encoder Action Decoder DiT Blocks Motor ...
- **p. 8 / 2.3. Training Details - extractive body cue:** Since the generated videos do not have action labels, we use either latent or inverse dynamics models (IDM) labeled actions (Baker et al., 2022) and ...
- **p. 5 / 2.2. Training Data Generation - extractive body cue:** After training, we take the encoder and use it as an inverse dynamics model; given an 𝑥𝑡and 𝑥𝑡+𝐻pair, we extract the continuous pre-quantized embedding and ...
- **p. 8 / 2.3. Training Details - extractive body cue:** 2.2) used to augment our robot datasets, we use both latent actions as well as predicted actions from an inverse-dynamics model trained on the real ...
- **p. 3 / 2. GR00T N1 Foundation Model - extractive body cue:** We highlight three key features of GR00T N1: • We design a compositional model that integrates Vision-Language Model (VLM)-based reasoning module (System 2) and Diffusion ...
- **p. 14 / 4.3. Experiment Setup - extractive body cue:** Evaluation Protocol For simulated benchmark evaluation, we report the average success rate over 100 trials, taking the maximum score of the last 5 checkpoints, where ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** GR00T, Open, Foundation, Model, Generalist, Humanoid, Robots, Robot, State, Eagle-2, VLM, Cross-Attention, Self-Attention, Encoder, Action, Decoder, DiT, Blocks, Motor, Pick.
- **Relevant PDF headings:** 2. GR00T N1 Foundation Model (p. 3); 2.1. Model Architecture (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | We generate 1000 demonstrations for each task using the DexMimicGen data generation system and evaluate the model's ability to generalize to novel ... | p. 12 (4.1. Simulation Benchmarks), p. 14 (4.2. Real-World Benchmarks) |
| Balance-aware whole-body execution | GR00T N1 outperforms both baselines, especially on the GR-1 task where it outperforms by more than 17 %. | p. 15 (4.4. Quantitative Results), p. 15 (4.4. Quantitative Results) |
| Recovery / adaptation | GR00T-N1-2B, achieves a significantly higher success rate across all tasks, outperforming Diffusion Policy by 32.4% in the 10% Data setting and by ... | p. 15 (4.4. Quantitative Results), p. 15 (4.4. Quantitative Results) |

## Failure and Ablation Link

- **p. 16 / 4.5. Qualitative Results - extractive body cue:** It is natural, in the limit of large fine-tuning datasets, that the effect of pre-training dwindles.
- **p. 14 / 4.3. Experiment Setup - extractive body cue:** It employs a U-Net architecture that progressively removes noise from random samples to generate precise robot actions conditioned on observation sequences.
- **p. 14 / 4.3. Experiment Setup - extractive body cue:** Baselines To demonstrate the effectiveness of diverse pretraining of GR00T N1, we compare with two established baselines, BC-Transformer (Mandlekar et al., 2021) and Diffusion Policy ...
- **p. 16 / 4.5. Qualitative Results - extractive body cue:** Since all post-training data exclusively involve the right hand without any inter-hand transfer, the post-trained policy loses the capability to perform this behavior.
- **p. 28 / Figure/Table caption - extractive body cue:** Figure 14: More Examples of Neural Generated Trajectories. We highlight 4 key capabilities of neural trajectories: (1) The first three rows shows an example of ...
- **p. 13 / 4.2. Real-World Benchmarks - extractive body cue:** We design two manipulation tasks to assess our pretrained models.
- **p. 15 / 4.4. Quantitative Results - extractive body cue:** For each task, we evaluate the pretrained GR00T-N1-2B model using five different objects, with three trials per object.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (2.1. Model Architecture), p. 8 (2.3. Training Details), p. 5 (2.2. Training Data Generation), p. 4 (2.1. Model Architecture), p. 8 (2.3. Training Details), p. 3 (2. GR00T N1 Foundation Model), objective p. 8 (2.3. Training Details), p. 5 (2.1. Model Architecture), p. 5 (2.2. Training Data Generation), p. 7 (2.2. Training Data Generation), temporal p. 14 (4.3. Experiment Setup), p. 5 (2.1. Model Architecture), p. 13 (4.2. Real-World Benchmarks), p. 14 (4.3. Experiment Setup), p. 17 (4.5. Qualitative Results), p. 17 (4.6. Limitations).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
