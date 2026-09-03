# Method - Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=zyMvoKYWMZ; PDF retrieval source: https://openreview.net/pdf/01fd7931fc7be08bf369b6a34264822e6d1de9b9.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (5.1. Overall Architecture), p. 4 (5.1. Overall Architecture), p. 5 (5.3. Training Strategy), p. 5 (5.3. Training Strategy)): The VLM comprises a trainable large language model InternLM2 1.8B (Cai et al., 2024), a visual observation module (§5.2), and a trainable projector that maps visual representations into the language ...

## Method Body Digest

- **p. 4 / 5.1. Overall Architecture - extractive body cue:** The VLM comprises a trainable large language model InternLM2 1.8B (Cai et al., 2024), a visual observation module (§5.2), and a trainable projector that maps ...
- **p. 4 / 5.1. Overall Architecture - extractive body cue:** We use a conditional flow-matching action expert (Lipman et al., 2023) to generate fine-grained end-effector actions.
- **p. 5 / 5.3. Training Strategy - extractive body cue:** The model takes as input image observations and the corresponding point clouds, the language instruction, and proprioceptive data.
- **p. 5 / 5.3. Training Strategy - extractive body cue:** We do not incorporate any explicit reconstruction losses for depth or point clouds, aiming to demonstrate that the performance gains stem primarily from superior spatial ...
- **p. 5 / 5.3. Training Strategy - extractive body cue:** The full form of the loss function is provided in Appendix F.1.
- **p. 4 / 5.1. Overall Architecture - extractive body cue:** ANY3D-VLA integrates a Vision-Language Model (VLM) with an action expert (Black et al., 2025b), and connects them via a Progressive Action Generation (PAG) mechanism (Deng ...
- **p. 1 / 1. Introduction - extractive body cue:** Vision-Language-Action (VLA) models, trained on massive collections of action trajectories paired with language instructions, hold great promise for achieving general-purpose embodied intelligence (Kim et al., ...
- **p. 2 / 1. Introduction - extractive body cue:** Given RGB images with optional depth, we first lift the visual input to point clouds and compress them.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** The contributions of this paper are summarized as follows: (1) We propose ANY3D-VLA.
- **p. 2 / 1. Introduction - extractive body cue:** We propose ANY3D-VLA, a plug-in pipeline for existing VLA backbones (Figure 1).

## Source Evidence Cues

- **p. 4 / 5.1. Overall Architecture - extractive body cue:** The VLM comprises a trainable large language model InternLM2 1.8B (Cai et al., 2024), a visual observation module (§5.2), and a trainable projector that maps ...
- **p. 4 / 5.1. Overall Architecture - extractive body cue:** We use a conditional flow-matching action expert (Lipman et al., 2023) to generate fine-grained end-effector actions.
- **p. 5 / 5.3. Training Strategy - extractive body cue:** The model takes as input image observations and the corresponding point clouds, the language instruction, and proprioceptive data.
- **p. 5 / 5.3. Training Strategy - extractive body cue:** We do not incorporate any explicit reconstruction losses for depth or point clouds, aiming to demonstrate that the performance gains stem primarily from superior spatial ...
- **Detected method headings:** 5.1. Overall Architecture (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | The VLM comprises a trainable large language model InternLM2 1.8B (Cai et al., 2024), a visual observation module (§5.2), and a trainable ... | p. 4 (5.1. Overall Architecture), p. 4 (5.1. Overall Architecture) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | We use a conditional flow-matching action expert (Lipman et al., 2023) to generate fine-grained end-effector actions. | p. 4 (5.1. Overall Architecture), p. 5 (5.3. Training Strategy) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | The model takes as input image observations and the corresponding point clouds, the language instruction, and proprioceptive data. | p. 5 (5.3. Training Strategy), p. 5 (5.3. Training Strategy) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 5.3. Training Strategy - extractive body cue:** The full form of the loss function is provided in Appendix F.1.
- **p. 5 / 5.3. Training Strategy - extractive body cue:** We do not incorporate any explicit reconstruction losses for depth or point clouds, aiming to demonstrate that the performance gains stem primarily from superior spatial ...
- **p. 4 / 5.1. Overall Architecture - extractive body cue:** ANY3D-VLA integrates a Vision-Language Model (VLM) with an action expert (Black et al., 2025b), and connects them via a Progressive Action Generation (PAG) mechanism (Deng ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 5 (5.3. Training Strategy), p. 5 (5.3. Training Strategy).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | model, takes, input, image, observations, corresponding, point, clouds, language, instruction, proprioceptive, data, Vision-Language-Action, VLA | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | model, takes, input, image, observations, corresponding, point, clouds, language, instruction | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | contributions, summarized, follows, ANY3D-VLA, plug-in, pipeline, existing, VLA, backbones, Figure | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | full, form, loss, function, provided, Appendix, incorporate, explicit, reconstruction, losses | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 5.3. Training Strategy - extractive body cue:** The model takes as input image observations and the corresponding point clouds, the language instruction, and proprioceptive data.
- **p. 1 / 1. Introduction - extractive body cue:** Vision-Language-Action (VLA) models, trained on massive collections of action trajectories paired with language instructions, hold great promise for achieving general-purpose embodied intelligence (Kim et al., ...
- **p. 2 / 1. Introduction - extractive body cue:** Given RGB images with optional depth, we first lift the visual input to point clouds and compress them.
- **p. 2 / 1. Introduction - extractive body cue:** However, 3D VLAs still face bottlenecks in scalable training and real deployment: (1) compared to the massive amount of 2D image data, 3D data is ...
- **p. 5 / 5.3. Training Strategy - extractive body cue:** We do not incorporate any explicit reconstruction losses for depth or point clouds, aiming to demonstrate that the performance gains stem primarily from superior spatial ...
- **p. 4 / 5.1. Overall Architecture - extractive body cue:** ANY3D-VLA integrates a Vision-Language Model (VLM) with an action expert (Black et al., 2025b), and connects them via a Progressive Action Generation (PAG) mechanism (Deng ...
- **p. 4 / 5.1. Overall Architecture - extractive body cue:** The VLM comprises a trainable large language model InternLM2 1.8B (Cai et al., 2024), a visual observation module (§5.2), and a trainable projector that maps ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Furthermore, compared to higher-frequency policies, our model executes a larger motion per step (roughly 2-3× longer). | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | As a result, an operating frequency of 1.7-2.0 FPS remains highly feasible for our target scenario of tabletop manipulation. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | As a result, an operating frequency of 1.7-2.0 FPS remains highly feasible for our target scenario of tabletop manipulation. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 5.1. Overall Architecture - extractive body cue:** The VLM comprises a trainable large language model InternLM2 1.8B (Cai et al., 2024), a visual observation module (§5.2), and a trainable projector that maps ...
- **p. 7 / 6.1.3. REAL-WORLD POST-TRAINING - extractive body cue:** Under the same point-cloud source at inference time, hybrid point cloud training consistently performs better than training with RealSense point clouds only, achieving the best ...
- **p. 5 / 5.3. Training Strategy - extractive body cue:** For Setting 2, the model is exposed to all point-cloud types throughout training, encouraging the 3D encoder and fusion layers to learn geometric patterns that ...
- **p. 6 / 6.1.1. REAL-WORLD SETUP - extractive body cue:** Training hyperparameters for each model are provided in Table 9 (Appendix H).
- **p. 7 / 6.2. Inference Efficiency and Latency - extractive body cue:** Inference speeds are measured on a single NVIDIA RTX 3090 GPU.
- **p. 8 / 6.4. Ablation Study - extractive body cue:** To verify the necessity of our 2D-3D fusion design, we conduct an ablation study on the key components of the visual encoder under a setting ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** VLM, comprises, trainable, large, language, model, InternLM2, Cai, visual, observation, module, projector, maps, representations, space, conditional, flow-matching, action, expert, Lipman.
- **Relevant PDF headings:** 5.1. Overall Architecture (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | This dataset includes 15 object categories that appeared in the pre-training data, while the layouts and backgrounds are randomly generated and unseen ... | p. 3 (3. Dataset and Benchmark), p. 3 (3. Dataset and Benchmark) |
| Action / skill decoding | ANY3DVLA outperforms the baselines on both tasks. | p. 7 (6.1.3. REAL-WORLD POST-TRAINING), p. 7 (6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD) |
| Receding execution / feedback | In particular, the overall average success rate for (Setting 2, DA3) reaches 62.5%, representing a 29.2% improvement over the strongest baseline SpatialVLA, ... | p. 7 (6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD), p. 8 (6.5. LIBERO and CALVIN Benchmarks) |

## Failure and Ablation Link

- **p. 8 / 6.4. Ablation Study - extractive body cue:** Ablation study on the effect of 2D-3D fusion.
- **p. 8 / 6.5. LIBERO and CALVIN Benchmarks - extractive body cue:** Specifically, π0.5 and SpatialVLA are fine-tuned from their publicly released pretrained weights, whereas GraspVLA and our model are first pretrained on our synthetic RGBD manipulation ...
- **p. 7 / 6.1.3. REAL-WORLD POST-TRAINING - extractive body cue:** To adapt to more diverse real-world tasks, we employ a two-stage training paradigm: imitation learning pre-training on large-scale synthetic data, followed by fine-tuning on a ...
- **p. 3 / 3. Dataset and Benchmark - extractive body cue:** (2) We uniformly freeze the image encoder and only fine-tune the last four layers of the other branch (if present).
- **p. 4 / 3. Dataset and Benchmark - extractive body cue:** Implicit-depth RGB oimpl-depth t = {I(v) t }v × × Two-branch encoders: (1) standard image encoder (DINOv2+SigLIP), (2) depthpretrained image encoder (Depth Anything v2 encoder; ...
- **p. 4 / 3. Dataset and Benchmark - extractive body cue:** Point cloud-2D patch fusion opc t : {[I(v) t , D(v) t ]}v → Pt √ √ Lift RGBD to point cloud Pt = {(xi, ...
- **p. 8 / 7. Limitations and Future Work - extractive body cue:** Although we have evaluated this work in both simulation and real-world manipulation settings, several limitations remain: (1) Our real-world experiments currently cover only a single ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (5.1. Overall Architecture), p. 4 (5.1. Overall Architecture), p. 5 (5.3. Training Strategy), p. 5 (5.3. Training Strategy), objective p. 5 (5.3. Training Strategy), p. 5 (5.3. Training Strategy), p. 4 (5.1. Overall Architecture), temporal p. 8 (0.3 FPS), p. 8 (0.3 FPS), p. 3 (3. Dataset and Benchmark), p. 6 (6.1.1. REAL-WORLD SETUP), p. 6 (6.1.1. REAL-WORLD SETUP), p. 7 (0.5 FPS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (21 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** The VLM comprises a trainable large language model InternLM2 1.8B (Cai et al., 2024), a visual observation module (§5.2), and a trainable projector that maps visual representations into the language ... (p. 4, 5.1. Overall Architecture).
- **Objective/update evidence:** The full form of the loss function is provided in Appendix F.1. (p. 5, 5.3. Training Strategy).
- **Temporal/runtime evidence:** Furthermore, compared to higher-frequency policies, our model executes a larger motion per step (roughly 2-3× longer). (p. 8, 0.3 FPS).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
