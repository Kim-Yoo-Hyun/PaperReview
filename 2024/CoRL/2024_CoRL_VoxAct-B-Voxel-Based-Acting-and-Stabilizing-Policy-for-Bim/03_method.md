# Method - VoxAct-B: Voxel-Based Acting and Stabilizing Policy for Bimanual Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v270/liu25i.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v270/main/assets/liu25i/liu25i.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (4 Method), p. 5 (4 Method), p. 14 (A.1 Additional Implementation Details), p. 17 (C Additional Implementation Details for the Baselines), p. 4 (4 Method), p. 16 (C Additional Implementation Details for the Baselines)): The overall training loss for VoxAct-B is: Ltotal = Lacting + Lstabilizing (1) and where for both values of arm ∈{acting, stabilizing}, we have Larm = -EY arm trans[log Varm ...

## Method Body Digest

- **p. 5 / 4 Method - extractive body cue:** The overall training loss for VoxAct-B is: Ltotal = Lacting + Lstabilizing (1) and where for both values of arm ∈{acting, stabilizing}, we have Larm ...
- **p. 5 / 4 Method - extractive body cue:** Then, we use Segment Anything [65], a foundational image segmentation model, to obtain the segmentation mask of the object and use the mask's centroid along ...
- **p. 14 / A.1 Additional Implementation Details - extractive body cue:** We use 2048 latents of dimension 512 in the Perceiver Transformer [70] and optimize the entire network using the LAMB [71] optimizer.
- **p. 17 / C Additional Implementation Details for the Baselines - extractive body cue:** Hyperparameter ACT Value Diffusion Policy Value learning rate 3e-5 1e-4 weight decay (for transformer only) - 1e-3 # encoder layers 4 - # decoder layers ...
- **p. 4 / 4 Method - extractive body cue:** During training, the language goal is given in the data, but during evaluation, we use VLMs to determine which language goal, ℓas or ℓsa, to ...
- **p. 16 / C Additional Implementation Details for the Baselines - extractive body cue:** For Diffusion Policy, lower values (e.g., 16) of the action prediction horizon were inadequate, leading to agents getting stuck at certain poses and failing to ...
- **p. 4 / 4 Method - extractive body cue:** This allows our method to learn to map the appropriate acting or stabilizing actions to a given arm during training.
- **p. 5 / 4 Method - extractive body cue:** While one can increase the number of voxels, this would consume more memory, slow down training, and adversely affect learning as the policy is optimizing ...

## Design Rationale

- **p. 1 / 1 Introduction - extractive body cue:** To this end, we propose VoxAct-B, a novel voxel-based, language-conditioned method for bimanual manipulation.
- **p. 4 / 4 Method - extractive body cue:** This allows our method to learn to map the appropriate acting or stabilizing actions to a given arm during training.
- **p. 1 / 1 Introduction - extractive body cue:** To address this, we propose utilizing VLMs to focus on the most pertinent regions within the scene by cropping out less relevant regions.

## Source Evidence Cues

- **p. 5 / 4 Method - extractive body cue:** The overall training loss for VoxAct-B is: Ltotal = Lacting + Lstabilizing (1) and where for both values of arm ∈{acting, stabilizing}, we have Larm ...
- **p. 5 / 4 Method - extractive body cue:** Then, we use Segment Anything [65], a foundational image segmentation model, to obtain the segmentation mask of the object and use the mask's centroid along ...
- **p. 14 / A.1 Additional Implementation Details - extractive body cue:** We use 2048 latents of dimension 512 in the Perceiver Transformer [70] and optimize the entire network using the LAMB [71] optimizer.
- **p. 17 / C Additional Implementation Details for the Baselines - extractive body cue:** Hyperparameter ACT Value Diffusion Policy Value learning rate 3e-5 1e-4 weight decay (for transformer only) - 1e-3 # encoder layers 4 - # decoder layers ...
- **p. 4 / 4 Method - extractive body cue:** During training, the language goal is given in the data, but during evaluation, we use VLMs to determine which language goal, ℓas or ℓsa, to ...
- **p. 16 / C Additional Implementation Details for the Baselines - extractive body cue:** For Diffusion Policy, lower values (e.g., 16) of the action prediction horizon were inadequate, leading to agents getting stuck at certain poses and failing to ...
- **p. 4 / 4 Method - extractive body cue:** This allows our method to learn to map the appropriate acting or stabilizing actions to a given arm during training.
- **Detected method headings:** 4 Method (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | The overall training loss for VoxAct-B is: Ltotal = Lacting + Lstabilizing (1) and where for both values of arm ∈{acting, stabilizing}, ... | p. 5 (4 Method), p. 5 (4 Method) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Then, we use Segment Anything [65], a foundational image segmentation model, to obtain the segmentation mask of the object and use the ... | p. 5 (4 Method), p. 14 (A.1 Additional Implementation Details) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | We use 2048 latents of dimension 512 in the Perceiver Transformer [70] and optimize the entire network using the LAMB [71] optimizer. | p. 14 (A.1 Additional Implementation Details), p. 17 (C Additional Implementation Details for the Baselines) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4 Method - extractive body cue:** The overall training loss for VoxAct-B is: Ltotal = Lacting + Lstabilizing (1) and where for both values of arm ∈{acting, stabilizing}, we have Larm ...
- **p. 5 / 4 Method - extractive body cue:** While one can increase the number of voxels, this would consume more memory, slow down training, and adversely affect learning as the policy is optimizing ...
- **p. 16 / C Additional Implementation Details for the Baselines - extractive body cue:** For Diffusion Policy, lower values (e.g., 16) of the action prediction horizon were inadequate, leading to agents getting stuck at certain poses and failing to ...
- **p. 14 / A.1 Additional Implementation Details - extractive body cue:** Note that the batch size is not optimized based on GPU memory capacity.
- **p. 14 / A.1 Additional Implementation Details - extractive body cue:** We use 2048 latents of dimension 512 in the Perceiver Transformer [70] and optimize the entire network using the LAMB [71] optimizer.
- **p. 17 / C Additional Implementation Details for the Baselines - extractive body cue:** As shown in Table 5, the performance of ACT and Diffusion Policy progressively improves as more environment variations are removed.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 5 (4 Method), p. 5 (4 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | time, step, input, voxel, observation, proprioception, data, robot, arms, language, goal, task, predict, action | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | time, step, input, voxel, observation, proprioception, data, robot, arms, language | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | VoxAct-B, novel, voxel-based, language-conditioned, bimanual, manipulation, allows, learn, appropriate, acting | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | overall, training, loss, VoxAct-B, Ltotal, Lacting, Lstabilizing, where, values, acting | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 4 Method - extractive body cue:** At each time step, the input to each arm is a voxel observation v, proprioception data of both robot arms ρ, a language goal l ...
- **p. 1 / 1 Introduction - extractive body cue:** Voxel representations, when coupled with discretized action spaces, can increase sample efficiency and generalization by introducing spatial equivariance into a learned system, where transformations of ...
- **p. 2 / 1 Introduction - extractive body cue:** Then, we provide appropriate language instructions to the bimanual manipulation policy to control the acting and stabilizing arms.
- **p. 4 / 4 Method - extractive body cue:** PerAct uses value maps to represent different components of the action space, where predictions for each arm are Q-functions with state-action values.
- **p. 5 / 4 Method - extractive body cue:** At test time, to select each arm's action, we perform an "argmax" over all the input variables to the arm's five Q-value, to get the ...
- **p. 5 / 4 Method - extractive body cue:** Therefore, given a voxel grid observational input v of size (L×W ×H) that spans x3 meters of the workspace, we keep the number of voxels ...
- **p. 16 / C Additional Implementation Details for the Baselines - extractive body cue:** For Diffusion Policy, lower values (e.g., 16) of the action prediction horizon were inadequate, leading to agents getting stuck at certain poses and failing to ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | At each time step, the input to each arm is a voxel observation v, proprioception data of both robot arms ρ, a ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | The robot also receives the language command l ∈{ℓas, ℓsa}, which is fixed for all time steps in an episode, where the ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | The policy is trained with a batch size of 1 on an Nvidia 3080 GPU for two days. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4 Method - extractive body cue:** The overall training loss for VoxAct-B is: Ltotal = Lacting + Lstabilizing (1) and where for both values of arm ∈{acting, stabilizing}, we have Larm ...
- **p. 17 / C Additional Implementation Details for the Baselines - extractive body cue:** Hyperparameter ACT Value Diffusion Policy Value learning rate 3e-5 1e-4 weight decay (for transformer only) - 1e-3 # encoder layers 4 - # decoder layers ...
- **p. 4 / 4 Method - extractive body cue:** During training, the language goal is given in the data, but during evaluation, we use VLMs to determine which language goal, ℓas or ℓsa, to ...
- **p. 4 / 4 Method - extractive body cue:** This allows our method to learn to map the appropriate acting or stabilizing actions to a given arm during training.
- **p. 17 / C Additional Implementation Details for the Baselines - extractive body cue:** Hyperparameter ACT Value Diffusion Policy Value learning rate 3e-5 1e-4 weight decay (for transformer only) - 1e-3 # encoder layers 4 - # decoder layers ...
- **p. 14 / A.1 Additional Implementation Details - extractive body cue:** The policy is trained with a batch size of 1 on an Nvidia 3080 GPU for two days.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** overall, training, loss, VoxAct-B, Ltotal, Lacting, Lstabilizing, where, values, acting, stabilizing, have, Larm, trans, Varm, open, collide, consists, cross-entropy, classifier-style.
- **Relevant PDF headings:** 4 Method (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | For simulation experiments, we build on top of RLBench [14], a popular robot manipulation benchmark widely used in prior work, including VoxPoser ... | p. 6 (5 Experiments), p. 6 (5 Experiments) |
| Action / skill decoding | When we train all methods using more demonstrations (100), VoxAct-B still outperforms all baselines. | p. 7 (6 Results), p. 6 (5 Experiments) |
| Receding execution / feedback | We found the Time-series Diffusion Transformer to outperform the CNN-based Diffusion Policy on Open Drawer and Open Jar, while both of them ... | p. 16 (C Additional Implementation Details for the Baselines), p. 6 (5 Experiments) |

## Failure and Ablation Link

- **p. 17 / Figure/Table caption - extractive body cue:** Table 5: Ablation results of ACT and Diffusion Policy trained on 100 demonstrations and evaluated across five training seeds. "FAS" refers to the demonstrations with ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Example successful rollouts (one per row) of VoxAct-B on a real-world bimanual setup with UR5s. Ablation experiments. Table 2 reports results on Open ...
- **p. 6 / 5 Experiments - extractive body cue:** Note that the real-world jar and drawer cannot be opened without the use of a second arm.
- **p. 6 / 5 Experiments - extractive body cue:** We also test the following ablations of VoxAct-B: • VoxAct-B w/o VLMs: does not use the VLMs to detect the object of interest and crop ...
- **p. 7 / 6 Results - extractive body cue:** Through ablations of ACT and Diffusion Policy, we found that removing environment variations greatly improved their performance.
- **p. 7 / 6 Results - extractive body cue:** Open Method Drawer VoxAct-B w/o VLMs 19.2 VoxAct-B w/o Segment Anything 67.2 VoxAct-B w/o acting and stabilizing 64.8 VoxAct-B w/o arm ID 68.0 VoxAct-B (ours) ...
- **p. 8 / 6 Results - extractive body cue:** If it does, it will be difficult to crop the voxel grid without losing relevant information.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (4 Method), p. 5 (4 Method), p. 14 (A.1 Additional Implementation Details), p. 17 (C Additional Implementation Details for the Baselines), p. 4 (4 Method), p. 16 (C Additional Implementation Details for the Baselines), objective p. 5 (4 Method), p. 5 (4 Method), p. 16 (C Additional Implementation Details for the Baselines), p. 14 (A.1 Additional Implementation Details), p. 14 (A.1 Additional Implementation Details), p. 17 (C Additional Implementation Details for the Baselines), temporal p. 4 (4 Method), p. 4 (2 Related Work), p. 6 (5 Experiments), p. 14 (A.1 Additional Implementation Details), p. 17 (C Additional Implementation Details for the Baselines), p. 3 (2 Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** At each time step, the input to each arm is a voxel observation v, proprioception data of both robot arms ρ, a language goal l ∈{ℓas, ℓsa}, and an arm ... (p. 4, 4 Method).
- **Objective/update evidence:** While one can increase the number of voxels, this would consume more memory, slow down training, and adversely affect learning as the policy is optimizing over a larger state space. (p. 5, 4 Method).
- **Temporal/runtime evidence:** At each time step, the input to each arm is a voxel observation v, proprioception data of both robot arms ρ, a language goal l ∈{ℓas, ℓsa}, and an arm ... (p. 4, 4 Method).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
