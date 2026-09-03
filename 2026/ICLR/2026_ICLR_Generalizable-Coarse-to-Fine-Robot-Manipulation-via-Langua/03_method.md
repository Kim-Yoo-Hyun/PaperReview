# Method - Generalizable Coarse-to-Fine Robot Manipulation via Language-Aligned 3D Keypoints

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=WXFfMLyB6y; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/244660. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (4 METHOD), p. 6 (4 METHOD), p. 7 (4 METHOD), p. 6 (4 METHOD), p. 5 (4 METHOD), p. 7 (4 METHOD)): Our hierarchical policy consists of a coarse task planner and a fine-grained action predictor, as shown in Figure 2.

## Method Body Digest

- **p. 5 / 4 METHOD - extractive body cue:** Our hierarchical policy consists of a coarse task planner and a fine-grained action predictor, as shown in Figure 2.
- **p. 6 / 4 METHOD - extractive body cue:** Instead, inspired by Chain-of-Thought reasoning (Mu et al., 2023; Zawalski et al., 2024; Zhao et al., 2025) for robotics, we design a reasoning process by ...
- **p. 7 / 4 METHOD - extractive body cue:** Our feature encoding pipeline consists of three stages to construct a unified 3D-aware and language-aligned representation.
- **p. 6 / 4 METHOD - extractive body cue:** To address this issue, we propose decoupling task planning from keypoint prediction via a two-round inference protocol.
- **p. 5 / 4 METHOD - extractive body cue:** 4.1 COARSE TASK PLANNER Prior coarse-to-fine policies condition all actions within a trajectory on a single high-level task description, limiting compositional generalization.
- **p. 7 / 4 METHOD - extractive body cue:** These components are combined to form a 3D-aware, language-aligned representation for downstream fine-grained action prediction, following the architecture of prior work (Goyal et al., 2024).
- **p. 16 / A.2 TRAINING DATA SPECIFICATION - extractive body cue:** The 3D positions of the objects are projected into canonical views to obtain the pixel positions in each view. • For robot trajectory dataset, we ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The fine-grained action predictor takes as input both the step instruction and the multi-view RGB-D images and outputs an action.

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In real-world experiments, our method demonstrate strong generalization ability to novel tasks and object variations with only 10 demonstrations per task.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address these limitations and issues, we propose Coarse-to-fine Language-Aligned manipulation Policy (CLAP), a novel coarse-to-fine 3D manipulation policy.
- **p. 5 / 4 METHOD - extractive body cue:** Our hierarchical policy consists of a coarse task planner and a fine-grained action predictor, as shown in Figure 2.

## Source Evidence Cues

- **p. 5 / 4 METHOD - extractive body cue:** Our hierarchical policy consists of a coarse task planner and a fine-grained action predictor, as shown in Figure 2.
- **p. 6 / 4 METHOD - extractive body cue:** Instead, inspired by Chain-of-Thought reasoning (Mu et al., 2023; Zawalski et al., 2024; Zhao et al., 2025) for robotics, we design a reasoning process by ...
- **p. 7 / 4 METHOD - extractive body cue:** Our feature encoding pipeline consists of three stages to construct a unified 3D-aware and language-aligned representation.
- **p. 6 / 4 METHOD - extractive body cue:** To address this issue, we propose decoupling task planning from keypoint prediction via a two-round inference protocol.
- **p. 5 / 4 METHOD - extractive body cue:** 4.1 COARSE TASK PLANNER Prior coarse-to-fine policies condition all actions within a trajectory on a single high-level task description, limiting compositional generalization.
- **p. 7 / 4 METHOD - extractive body cue:** These components are combined to form a 3D-aware, language-aligned representation for downstream fine-grained action prediction, following the architecture of prior work (Goyal et al., 2024).
- **p. 16 / A.2 TRAINING DATA SPECIFICATION - extractive body cue:** The 3D positions of the objects are projected into canonical views to obtain the pixel positions in each view. • For robot trajectory dataset, we ...
- **Detected method headings:** 4 METHOD (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Our hierarchical policy consists of a coarse task planner and a fine-grained action predictor, as shown in Figure 2. | p. 5 (4 METHOD), p. 6 (4 METHOD) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Instead, inspired by Chain-of-Thought reasoning (Mu et al., 2023; Zawalski et al., 2024; Zhao et al., 2025) for robotics, we design a ... | p. 6 (4 METHOD), p. 7 (4 METHOD) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Our feature encoding pipeline consists of three stages to construct a unified 3D-aware and language-aligned representation. | p. 7 (4 METHOD), p. 6 (4 METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 4 METHOD - extractive body cue:** Instead, inspired by Chain-of-Thought reasoning (Mu et al., 2023; Zawalski et al., 2024; Zhao et al., 2025) for robotics, we design a reasoning process by ...
- **p. 7 / 4 METHOD - extractive body cue:** These components are combined to form a 3D-aware, language-aligned representation for downstream fine-grained action prediction, following the architecture of prior work (Goyal et al., 2024).
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 6 (4 METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | fine-grained, action, predictor, takes, input, step, instruction, multi-view, RGB-D, images, outputs, addition, task, decomposition | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | fine-grained, action, predictor, takes, input, step, instruction, multi-view, RGB-D, images | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | real-world, experiments, demonstrate, strong, generalization, ability, novel, tasks, object, variations | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Instead, inspired, Chain-of-Thought, reasoning, Zawalski, Zhao, robotics, design, process, training | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 INTRODUCTION - extractive body cue:** The fine-grained action predictor takes as input both the step instruction and the multi-view RGB-D images and outputs an action.
- **p. 5 / 4 METHOD - extractive body cue:** In addition to task decomposition done at the beginning, at every execution timestep, the VLM fθ is also exploited to predict both the step instruction ...
- **p. 6 / 4 METHOD - extractive body cue:** However, directly training the model fθ to simultaneously generate a task plan L and predict step instruction ℓtk and 3D keypoint ptk, given as inputs ...
- **p. 4 / 3 BACKGROUND - extractive body cue:** In this framework, the goal is to train a policy π to predict the key-frame action atk at the closest next key-frame of timestep tk ...
- **p. 7 / 4 METHOD - extractive body cue:** First, RGB images and step instructions are processed through vision-language encoders to establish semantic alignment between visual and textual inputs.
- **p. 4 / 3 BACKGROUND - extractive body cue:** In coarse-to-fine policies, the 3D position ptk output by the coarse branch for the next key-frame is typically used as the 3D keypoint to zoom ...
- **p. 5 / 3 BACKGROUND - extractive body cue:** The fine-grained action predictor fuses the corresponding step instruction with a 3D-aware visual representation from refined observations to predict the final action.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Finally, we choose to use observations (otk, ...otk+m) at the time steps immediately following each key-frame. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | We initially attempted to sample observations within a window (otk-m, ..., otk, ...otk+m) around the time step tk of the kth key-frame. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | First, we provide to the VLM an additional input: the step instruction predicted in the last timestep, which serves as a short-term ... | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | All experiments are conducted on 4 NVIDIA RTX 4090 GPU. | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 4 METHOD - extractive body cue:** Instead, inspired by Chain-of-Thought reasoning (Mu et al., 2023; Zawalski et al., 2024; Zhao et al., 2025) for robotics, we design a reasoning process by ...
- **p. 6 / 4 METHOD - extractive body cue:** To address this issue, we propose decoupling task planning from keypoint prediction via a two-round inference protocol.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** The hyperparameters, such as batch size and learning rate used in training are listed in Appendix A.3.
- **p. 16 / A.3 EXPERIMENTAL DETAILS - extractive body cue:** The hyperparameters and training time are listed in Table 6.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** 5) CLAP w/o Pre-trained Encoder An ablation study (comparing Exp ID 5 and Exp ID 6) on the coarse planner confirms that incorporating the 3D-aware ...
- **p. 6 / 4 METHOD - extractive body cue:** Considering the significant domain shift between the images focused around predicted ptk from those used to pretrain standard VLMs, we decide to employ instead pre-trained ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** hierarchical, policy, consists, coarse, task, planner, fine-grained, action, predictor, Figure, Instead, inspired, Chain-of-Thought, reasoning, Zawalski, Zhao, robotics, design, process, training.
- **Relevant PDF headings:** 4 METHOD (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | It is LoRA fine-tuned (Hu et al., 2022) with the object keypoint dataset, language plans, and robot trajectories. | p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Action / skill decoding | Table 2: Ablation study of CLAP on GemBench. Here are the average success rates of 4 levels of evaluation tasks from Gembench ... | p. 8 (Figure/Table caption), p. 8 (5 EXPERIMENTS) |
| Receding execution / feedback | Table 2: Ablation study of CLAP on GemBench. Here are the average success rates of 4 levels of evaluation tasks from Gembench ... | p. 8 (Figure/Table caption), p. 7 (5 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Ablation study of CLAP on GemBench. Here are the average success rates of 4 levels of evaluation tasks from Gembench under different training ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** A specific ablation on the inputs of the fine-grained action predictor is include in Appendix A.5.
- **p. 19 / A.6 REAL-WORLD EXPERIMENTS - extractive body cue:** Number of Demos L1 L2 L3 L4 Average 10 84.5 ± 0.8 81.5 ± 0.6 43.3 ± 1.9 30.5 ± 2.1 60.0 ± 0.1 20 ...
- **p. 19 / Figure/Table caption - extractive body cue:** Table 12: Ablation on inputs to Fine-grained Action Predictor. We compare the results of re- moving some inputs to our fine-grained action predictor. The results ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Using all observations around the key-frames to fine-tune the VLM risks confusing it.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** It is LoRA fine-tuned (Hu et al., 2022) with the object keypoint dataset, language plans, and robot trajectories.
- **p. 16 / A.5 ADDITIONAL ABLATION STUDY - extractive body cue:** Further increasing the number of robot trajectory improves on the in-domain performance (L1) while does not help in the average success rate.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (4 METHOD), p. 6 (4 METHOD), p. 7 (4 METHOD), p. 6 (4 METHOD), p. 5 (4 METHOD), p. 7 (4 METHOD), objective p. 6 (4 METHOD), p. 7 (4 METHOD), temporal p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 4 (3 BACKGROUND), p. 6 (4 METHOD), p. 5 (4 METHOD), p. 5 (4 METHOD).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
