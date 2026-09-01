# Method - RealVLG-R1: A Large-Scale Real-World Visual-Language Grounding Benchmark for Robotic Perception and Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Li_RealVLG-R1_A_Large-Scale_Real-World_Visual-Language_Grounding_Benchmark_for_Robotic_Perception_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_RealVLG-R1_A_Large-Scale_Real-World_Visual-Language_Grounding_Benchmark_for_Robotic_Perception_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 6 (4.3. Task-Specific Pipelines and Verifiable Rewards), p. 5 (4.1. Overview), p. 6 (4.2. Policy Optimization with Verifiable Rewards), p. 7 (4.3. Task-Specific Pipelines and Verifiable Rewards), p. 5 (4.1. Overview), p. 8 (Method)): 3, the policy model receives an image and a task prompt, then generates structured outputs according to task requirements.

## Method Body Digest

- **p. 6 / 4.3. Task-Specific Pipelines and Verifiable Rewards - extractive PDF cue:** 3, the policy model receives an image and a task prompt, then generates structured outputs according to task requirements.
- **p. 5 / 4.1. Overview - extractive PDF cue:** 3, we propose a unified framework, RealVLG-R1, which fine-tunes pretrained LVLMs using a reinforcement-style optimization strategy inspired by DeepSeek-R1 [22].
- **p. 6 / 4.2. Policy Optimization with Verifiable Rewards - extractive PDF cue:** Grasp Contact SAM2 Answer Reference Model Reinforcement Fine-tuning KL Reward Policy Model (LVLMs) Figure 3.
- **p. 7 / 4.3. Task-Specific Pipelines and Verifiable Rewards - extractive PDF cue:** The predicted contact points P p 1 , P p 2 are first converted into a rectangular grasp pose Gp with fixed width, and then ...
- **p. 5 / 4.1. Overview - extractive PDF cue:** Furthermore, we introduce a Verifiable Reward Mechanism that dynamically evaluates and guides model predictions in terms of both semantic correctness and physical feasibility.
- **p. 8 / Method - extractive PDF cue:** These results suggest that GRPO's reward formulation better enhances finegrained action precision in smaller models, while GSPO's sequence-level incentives provide smoother optimization for larger models, ...
- **p. 7 / 4.3. Task-Specific Pipelines and Verifiable Rewards - extractive PDF cue:** Then, the grasping reward is formulated as the negative sum of Huber losses computed over all pose components: R_{\ t e x t {Grasp}} = ...
- **p. 5 / 4.2. Policy Optimization with Verifiable Rewards - extractive PDF cue:** Furthermore, the objective of RealVLG-R1 aims to maximize the expected reward while introducing a KL-divergence regularization 42400

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** 1, we propose the RealVLG framework, which unifies visuallanguage grounding and grasping tasks within a single research paradigm.
- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, our main contributions are as follows: • RealVLG-11B Dataset: The largest real-world grounding and grasping dataset with multi-granularity annotations from semantic localization to ...
- **p. 5 / 4.1. Overview - extractive PDF cue:** 3, we propose a unified framework, RealVLG-R1, which fine-tunes pretrained LVLMs using a reinforcement-style optimization strategy inspired by DeepSeek-R1 [22].

## Source Evidence Cues

- **p. 6 / 4.3. Task-Specific Pipelines and Verifiable Rewards - extractive PDF cue:** 3, the policy model receives an image and a task prompt, then generates structured outputs according to task requirements.
- **p. 5 / 4.1. Overview - extractive PDF cue:** 3, we propose a unified framework, RealVLG-R1, which fine-tunes pretrained LVLMs using a reinforcement-style optimization strategy inspired by DeepSeek-R1 [22].
- **p. 6 / 4.2. Policy Optimization with Verifiable Rewards - extractive PDF cue:** Grasp Contact SAM2 Answer Reference Model Reinforcement Fine-tuning KL Reward Policy Model (LVLMs) Figure 3.
- **p. 7 / 4.3. Task-Specific Pipelines and Verifiable Rewards - extractive PDF cue:** The predicted contact points P p 1 , P p 2 are first converted into a rectangular grasp pose Gp with fixed width, and then ...
- **p. 5 / 4.1. Overview - extractive PDF cue:** Furthermore, we introduce a Verifiable Reward Mechanism that dynamically evaluates and guides model predictions in terms of both semantic correctness and physical feasibility.
- **p. 8 / Method - extractive PDF cue:** These results suggest that GRPO's reward formulation better enhances finegrained action precision in smaller models, while GSPO's sequence-level incentives provide smoother optimization for larger models, ...
- **p. 7 / 4.3. Task-Specific Pipelines and Verifiable Rewards - extractive PDF cue:** Then, the grasping reward is formulated as the negative sum of Huber losses computed over all pose components: R_{\ t e x t {Grasp}} = ...
- **Detected method headings:** 4. RealVLG-R1 Model (p. 5); 4.2. Policy Optimization with Verifiable Rewards (p. 5); Method (p. 8)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | 3, the policy model receives an image and a task prompt, then generates structured outputs according to task requirements. | p. 6 (4.3. Task-Specific Pipelines and Verifiable Rewards), p. 5 (4.1. Overview) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | 3, we propose a unified framework, RealVLG-R1, which fine-tunes pretrained LVLMs using a reinforcement-style optimization strategy inspired by DeepSeek-R1 [22]. | p. 5 (4.1. Overview), p. 6 (4.2. Policy Optimization with Verifiable Rewards) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | Grasp Contact SAM2 Answer Reference Model Reinforcement Fine-tuning KL Reward Policy Model (LVLMs) Figure 3. | p. 6 (4.2. Policy Optimization with Verifiable Rewards), p. 7 (4.3. Task-Specific Pipelines and Verifiable Rewards) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4.2. Policy Optimization with Verifiable Rewards - extractive PDF cue:** Furthermore, the objective of RealVLG-R1 aims to maximize the expected reward while introducing a KL-divergence regularization 42400
- **p. 8 / Method - extractive PDF cue:** These results suggest that GRPO's reward formulation better enhances finegrained action precision in smaller models, while GSPO's sequence-level incentives provide smoother optimization for larger models, ...
- **p. 5 / 4.2. Policy Optimization with Verifiable Rewards - extractive PDF cue:** Unlike conventional approaches [5, 35, 87] that rely on learned reward models, RLVR leverages task-intrinsic verifiable criteria to provide objective reward signals through a binary ...
- **p. 7 / 4.3. Task-Specific Pipelines and Verifiable Rewards - extractive PDF cue:** Then, the grasping reward is formulated as the negative sum of Huber losses computed over all pose components: R_{\ t e x t {Grasp}} = ...
- **p. 6 / 4.2. Policy Optimization with Verifiable Rewards - extractive PDF cue:** Prompt Grasp Prompt Contact Prompt Image Prompts Verifiable Reward Policy Optimization Completions Format Reward <think> Reasoning </think> <answer> … </answer> Task-Specific Reward IoU Reward Bbox ...
- **p. 6 / 4.2. Policy Optimization with Verifiable Rewards - extractive PDF cue:** RealVLG-R1 fine-tunes pretrained LVLMs via reward-driven RL using task-specific verifiable rewards, enabling adaptive learning and improved generalization over bounding boxes, segmentation, grasp rectangles, and contact ...
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 5 (4.2. Policy Optimization with Verifiable Rewards), p. 5 (4.2. Policy Optimization with Verifiable Rewards), p. 6 (4.2. Policy Optimization with Verifiable Rewards), p. 7 (4.3. Task-Specific Pipelines and Verifiable Rewards), p. 6 (4.2. Policy Optimization with Verifiable Rewards), p. 7 (4.3. Task-Specific Pipelines and Verifiable Rewards).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | During, training, input, images, task, prompts, processed, through, policy, optimization, module, generate, candidate, outputs | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | During, training, input, images, task, prompts, processed, through, policy, optimization | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | RealVLG, framework, unifies, visuallanguage, grounding, grasping, tasks, within, single, research | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | Furthermore, objective, RealVLG-R1, aims, maximize, expected, reward, while, introducing, KL-divergence | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive PDF cue:** During training, input images and task prompts are processed through a policy optimization module to generate candidate outputs, which are then updated using verifiable reward ...
- **p. 6 / 4.3. Task-Specific Pipelines and Verifiable Rewards - extractive PDF cue:** The core of RealVLG-R1 is its composite reward function R(q, o), providing hierarchical and verifiable feedback by combining output format compliance with task-specific geometric accuracy: ...
- **p. 6 / 4.2. Policy Optimization with Verifiable Rewards - extractive PDF cue:** Input Output Object <image> A yellow banana under the white bottle.
- **p. 2 / 1. Introduction - extractive PDF cue:** Leveraging LVLMs (e.g., the QwenVL series) as the backbone, the model is trained using a Reinforcement Fine-tuning strategy to directly predict segmentation masks, bounding boxes, ...
- **p. 5 / 4.2. Policy Optimization with Verifiable Rewards - extractive PDF cue:** Formally, the verifiable reward function R(q, o) is defined as, R( q, o ) = \ b egin { cases} 1 , & \text {if ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Isaac Newton Visual-Language Grounding (VLG) aims to establish semantic correspondences between natural language and visual entities in images, enabling models to accurately identify and localize ...
- **p. 8 / Method - extractive PDF cue:** The visual grasping task imposes higher demands on physical reasoning and action coherence.
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | To systematically evaluate the multi-task performance on the RealVLG benchmark, we utilize a task-specific evaluation framework that rigorously addresses both geometric precision ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | Building upon this, our proposed RealVLG-R1 model employs Qwen2.5-VL as its backbone and is developed within the VERL framework [68]. | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | Following the data split in Table 2, both RealVLG-R1 and Qwen2.5-VL+SFT were fine-tuned for 10 epochs using only 10% of the training ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4.1. Overview - extractive PDF cue:** 3, we propose a unified framework, RealVLG-R1, which fine-tunes pretrained LVLMs using a reinforcement-style optimization strategy inspired by DeepSeek-R1 [22].
- **p. 6 / 4.2. Policy Optimization with Verifiable Rewards - extractive PDF cue:** Grasp Contact SAM2 Answer Reference Model Reinforcement Fine-tuning KL Reward Policy Model (LVLMs) Figure 3.
- **p. 6 / 4.2. Policy Optimization with Verifiable Rewards - extractive PDF cue:** RealVLG-R1 fine-tunes pretrained LVLMs via reward-driven RL using task-specific verifiable rewards, enabling adaptive learning and improved generalization over bounding boxes, segmentation, grasp rectangles, and contact ...
- **p. 8 / Method - extractive PDF cue:** Following the data split in Table 2, both RealVLG-R1 and Qwen2.5-VL+SFT were fine-tuned for 10 epochs using only 10% of the training set.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** policy, model, receives, image, task, prompt, then, generates, structured, outputs, according, requirements, unified, framework, RealVLG-R1, fine-tunes, pretrained, LVLMs, reinforcement-style, optimization.
- **Relevant PDF headings:** 4. RealVLG-R1 Model (p. 5); 4.2. Policy Optimization with Verifiable Rewards (p. 5); Method (p. 8).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | The dataset contains approximately 165,000 images, over 800 object instances, 1.3 million segmentation, detection, and language annotations, and 11 billion grasp examples, ... | p. 4 (3.1. Overview), p. 5 (5 Based on the resulting Rect Grasp Poses) |
| Baseline harness | As summarized in Table 1, compared to existing datasets, RealVLG-11B provides consistent bounding boxes, segmentation masks, rectangular grasp poses, and language descriptions ... | p. 5 (5 Based on the resulting Rect Grasp Poses), p. 7 (5.1. Data Quality Evaluation) |
| Metric / failure reporting | In rectangular grasp pose prediction, performance relies on mean IoU (mIoU) and Grasp Accuracy (gAcc) [26], where gAcc is achieved when the ... | p. 7 (5.2. RealVLG Benchmark), p. 7 (5.1. Data Quality Evaluation) |

## Failure and Ablation Link

- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3. Framework of RealVLG-R1. RealVLG-R1 fine-tunes pretrained LVLMs via reward-driven RL using task-specific verifiable rewards, enabling adaptive learning and improved generalization over bounding boxes, ...
- **p. 8 / 6. Conclusions - extractive PDF cue:** Future work will extend RealVLG to 3D space, and explore efficient models such as SmolVLM [43] to improve runtime without extra fine-tuning.
- **p. 3 / 3.1. Overview - extractive PDF cue:** Existing grasping datasets generally suffer from two major limitations.
- **p. 5 / 5 Based on the resulting Rect Grasp Poses - extractive PDF cue:** The computation is designed to ensure that contact points accurately lie on the object surface: if the midpoint along the gripper's closing direction falls outside ...
- **p. 7 / 5.1. Data Quality Evaluation - extractive PDF cue:** Linguistic and grounding quality comparison. grasp points located within segmentation masks (Rg), and proportion of contact centers falling inside segmentation masks (Rc).

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 6 (4.3. Task-Specific Pipelines and Verifiable Rewards), p. 5 (4.1. Overview), p. 6 (4.2. Policy Optimization with Verifiable Rewards), p. 7 (4.3. Task-Specific Pipelines and Verifiable Rewards), p. 5 (4.1. Overview), p. 8 (Method), objective p. 5 (4.2. Policy Optimization with Verifiable Rewards), p. 8 (Method), p. 5 (4.2. Policy Optimization with Verifiable Rewards), p. 7 (4.3. Task-Specific Pipelines and Verifiable Rewards), p. 6 (4.2. Policy Optimization with Verifiable Rewards), p. 6 (4.2. Policy Optimization with Verifiable Rewards), temporal p. 7 (5.2. RealVLG Benchmark), p. 8 (Method), p. 8 (Method), p. 1 (Abstract), p. 1 (Front matter), p. 2 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
