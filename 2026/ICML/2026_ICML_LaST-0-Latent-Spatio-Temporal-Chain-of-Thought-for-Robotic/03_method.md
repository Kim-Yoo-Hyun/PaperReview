# Method - LaST$_{0}$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=lwOoBzJykL; PDF retrieval source: https://openreview.net/pdf/0e9ec532d1e01f801ca9bc49e258c05cf3a207f5.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. LaST0 Architecture), p. 4 (3.2. LaST0 Architecture), p. 5 (3.3. Latent Spatio-Temporal Chain-of-Thought), p. 3 (3.2. LaST0 Architecture), p. 5 (3.3. Latent Spatio-Temporal Chain-of-Thought), p. 3 (3.1. Preliminaries)): LaST0: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model QKV a) LaST𝟎Architecture QKV t𝒕"𝟏 t𝒕"𝟐 2D Visual Latent 3D Geometric Latent Robot Proprioception Latent LaST CoT t𝒕"𝑯 "Scoop the egg out ...

## Method Body Digest

- **p. 4 / 3.2. LaST0 Architecture - extractive PDF cue:** LaST0: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model QKV a) LaST𝟎Architecture QKV t𝒕"𝟏 t𝒕"𝟐 2D Visual Latent 3D Geometric Latent Robot Proprioception Latent LaST CoT ...
- **p. 4 / 3.2. LaST0 Architecture - extractive PDF cue:** The fast acting expert operates at a higher frequency and generates actions via flow matching, conditioned on high-frequency observations and periodically updated latent representations. b) ...
- **p. 5 / 3.3. Latent Spatio-Temporal Chain-of-Thought - extractive PDF cue:** To better organize LaST CoT reasoning and action generation, we introduce three special tokens: <latent start>, <latent end>, and a placeholder token <latent pad>.
- **p. 3 / 3.2. LaST0 Architecture - extractive PDF cue:** This design enables the model to effectively decouple the generation of slow, high-level latent reasoning from fast, low-level action execution, while maintaining seamless information flow ...
- **p. 5 / 3.3. Latent Spatio-Temporal Chain-of-Thought - extractive PDF cue:** (2) By maximizing directional alignment in the latent space, this objective encourages the model to anticipate future physical dynamics in a structured and compact manner.
- **p. 3 / 3.1. Preliminaries - extractive PDF cue:** Specifically, this control vector consists of 3-DoF for relative positional offsets ([∆x, ∆y, ∆z] ∈R3), 3-DoF for rotation (represented as Euler angles [roll, pitch, yaw] ...
- **p. 6 / 3.5. Training Recipe - extractive PDF cue:** In ablation studies, we find that training with mixed fast-slow operating ratios does not degrade performance; instead, it improves the model's robustness during inference. a) ...
- **p. 5 / 3.5. Training Recipe - extractive PDF cue:** Specifically, the slow reasoning expert is trained by minimizing the Latent CoT regression loss Llatent, aligning its latent representations with domain5

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Our contributions are summarized as follows: • We propose LaST0, a unified VLA model that enables efficient reason-before-act behavior through a Latent SpatioTemporal CoT, performing ...
- **p. 2 / 1. Introduction - extractive PDF cue:** In this paper, we propose LaST0, a dual-system VLA model that enables efficient reason-before-act behavior through a Latent Spatio-Temporal Chain-of-Thought (CoT).
- **p. 3 / 3.1. Preliminaries - extractive PDF cue:** Specifically, this control vector consists of 3-DoF for relative positional offsets ([∆x, ∆y, ∆z] ∈R3), 3-DoF for rotation (represented as Euler angles [roll, pitch, yaw] ...

## Source Evidence Cues

- **p. 4 / 3.2. LaST0 Architecture - extractive PDF cue:** LaST0: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model QKV a) LaST𝟎Architecture QKV t𝒕"𝟏 t𝒕"𝟐 2D Visual Latent 3D Geometric Latent Robot Proprioception Latent LaST CoT ...
- **p. 4 / 3.2. LaST0 Architecture - extractive PDF cue:** The fast acting expert operates at a higher frequency and generates actions via flow matching, conditioned on high-frequency observations and periodically updated latent representations. b) ...
- **p. 5 / 3.3. Latent Spatio-Temporal Chain-of-Thought - extractive PDF cue:** To better organize LaST CoT reasoning and action generation, we introduce three special tokens: <latent start>, <latent end>, and a placeholder token <latent pad>.
- **p. 3 / 3.2. LaST0 Architecture - extractive PDF cue:** This design enables the model to effectively decouple the generation of slow, high-level latent reasoning from fast, low-level action execution, while maintaining seamless information flow ...
- **p. 5 / 3.3. Latent Spatio-Temporal Chain-of-Thought - extractive PDF cue:** (2) By maximizing directional alignment in the latent space, this objective encourages the model to anticipate future physical dynamics in a structured and compact manner.
- **p. 3 / 3.1. Preliminaries - extractive PDF cue:** Specifically, this control vector consists of 3-DoF for relative positional offsets ([∆x, ∆y, ∆z] ∈R3), 3-DoF for rotation (represented as Euler angles [roll, pitch, yaw] ...
- **p. 6 / 3.5. Training Recipe - extractive PDF cue:** In ablation studies, we find that training with mixed fast-slow operating ratios does not degrade performance; instead, it improves the model's robustness during inference. a) ...
- **Detected method headings:** 3. Method (p. 3); 3.2. LaST0 Architecture (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | LaST0: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model QKV a) LaST𝟎Architecture QKV t𝒕"𝟏 t𝒕"𝟐 2D Visual Latent 3D Geometric Latent Robot Proprioception ... | p. 4 (3.2. LaST0 Architecture), p. 4 (3.2. LaST0 Architecture) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | The fast acting expert operates at a higher frequency and generates actions via flow matching, conditioned on high-frequency observations and periodically updated ... | p. 4 (3.2. LaST0 Architecture), p. 5 (3.3. Latent Spatio-Temporal Chain-of-Thought) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | To better organize LaST CoT reasoning and action generation, we introduce three special tokens: <latent start>, <latent end>, and a placeholder token ... | p. 5 (3.3. Latent Spatio-Temporal Chain-of-Thought), p. 3 (3.2. LaST0 Architecture) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.5. Training Recipe - extractive PDF cue:** Specifically, the slow reasoning expert is trained by minimizing the Latent CoT regression loss Llatent, aligning its latent representations with domain5
- **p. 5 / 3.3. Latent Spatio-Temporal Chain-of-Thought - extractive PDF cue:** (2) By maximizing directional alignment in the latent space, this objective encourages the model to anticipate future physical dynamics in a structured and compact manner.
- **p. 4 / 3.2. LaST0 Architecture - extractive PDF cue:** LaST0: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model QKV a) LaST𝟎Architecture QKV t𝒕"𝟏 t𝒕"𝟐 2D Visual Latent 3D Geometric Latent Robot Proprioception Latent LaST CoT ...
- **p. 6 / 3.5. Training Recipe - extractive PDF cue:** In parallel, the fast acting expert is optimized using the standard Flow Matching loss Lflow for action denoising.
- **p. 3 / 3.1. Preliminaries - extractive PDF cue:** The objective of the VLA model πθ is to generate an optimal action sequence at:t+H conditioned on the instruction lt.
- **p. 4 / 3.2. LaST0 Architecture - extractive PDF cue:** The fast acting expert operates at a higher frequency and generates actions via flow matching, conditioned on high-frequency observations and periodically updated latent representations. b) ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (3.2. LaST0 Architecture), p. 3 (3.1. Preliminaries), p. 5 (3.3. Latent Spatio-Temporal Chain-of-Thought), p. 5 (3.3. Latent Spatio-Temporal Chain-of-Thought), p. 6 (3.5. Training Recipe), p. 4 (3.2. LaST0 Architecture).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | fast, acting, expert, operates, higher, frequency, generates, actions, flow, matching, conditioned, high-frequency, observations, periodically | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | fast, acting, expert, operates, higher, frequency, generates, actions, flow, matching | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | contributions, summarized, follows, LaST0, unified, VLA, model, enables, efficient, reason-before-act | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Specifically, slow, reasoning, expert, trained, minimizing, Latent, CoT, regression, loss | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. LaST0 Architecture - extractive PDF cue:** The fast acting expert operates at a higher frequency and generates actions via flow matching, conditioned on high-frequency observations and periodically updated latent representations. b) ...
- **p. 4 / 3.2. LaST0 Architecture - extractive PDF cue:** LaST0: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model QKV a) LaST𝟎Architecture QKV t𝒕"𝟏 t𝒕"𝟐 2D Visual Latent 3D Geometric Latent Robot Proprioception Latent LaST CoT ...
- **p. 3 / 3.1. Preliminaries - extractive PDF cue:** At each timestep t, the policy receives a natural language instruction lt and visual observations It ∈RH×W ×3 that capture the current environment.
- **p. 5 / 3.4. Dual-System Coordination - extractive PDF cue:** For the inputs to the two experts, the slow reasoning expert receives the natural language instruction l and the low-frequency observation Islow, constructing the Latent ...
- **p. 3 / 3.1. Preliminaries - extractive PDF cue:** The objective of the VLA model πθ is to generate an optimal action sequence at:t+H conditioned on the instruction lt.
- **p. 5 / 3.4. Dual-System Coordination - extractive PDF cue:** Conversely, the fast acting expert is optimized for rapid closed-loop feedback and receives only the high-frequency observation Ifast.
- **p. 2 / 1. Introduction - extractive PDF cue:** Rather than simply mapping observations to actions, recent advances in VLA models have been inspired by the Chain-of-Thought (CoT) reasoning paradigm in general VLMs (Guo ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | 5 c), we investigate the effect of the temporal horizon used in latent reasoning by varying the number of future time steps ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | LaST0: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model Zhuoyang Liu * 1 Jiaming Liu * † 1 Hao Chen * 2 Jiale ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | LaST0: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model QKV a) LaST𝟎Architecture QKV t𝒕"𝟏 t𝒕"𝟐 2D Visual Latent 3D Geometric Latent Robot Proprioception ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.2. LaST0 Architecture - extractive PDF cue:** The fast acting expert operates at a higher frequency and generates actions via flow matching, conditioned on high-frequency observations and periodically updated latent representations. b) ...
- **p. 6 / 3.5. Training Recipe - extractive PDF cue:** In ablation studies, we find that training with mixed fast-slow operating ratios does not degrade performance; instead, it improves the model's robustness during inference. a) ...
- **p. 6 / 4.1. Simulation Experiment - extractive PDF cue:** Following (Goyal et al., 2023), we perform 20 rollout trials per task using the final checkpoint, repeat the evaluation across three random seeds, and report ...
- **p. 6 / 4.1. Simulation Experiment - extractive PDF cue:** In alignment with the official LIBERO protocol, each model is trained separately for each task suite, and we evaluate the final checkpoint on 500 trials ...
- **p. 7 / 4.1. Simulation Experiment - extractive PDF cue:** Inference speed is evaluated on an NVIDIA 4090 GPU.
- **p. 3 / 3.2. LaST0 Architecture - extractive PDF cue:** Point Cloud Encoder (training only).

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** LaST0, Latent, Spatio-Temporal, Chain-of-Thought, Robotic, Vision-Language-Action, Model, QKV, LaST, Architecture, Visual, Geometric, Robot, Proprioception, CoT, Scoop, place, bread, Shared, Attention.
- **Relevant PDF headings:** 3. Method (p. 3); 3.2. LaST0 Architecture (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | For the LIBERO (Liu et al., 2024) benchmark, our evaluation leverages its four specialized dataset suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-Long. | p. 6 (4.1. Simulation Experiment), p. 8 (4.3. Real-World Experiment) |
| Action / skill decoding | In this suite, LaST0 achieves a 95.6% success rate, outperforming strong baselines such as OpenVLA-OFT (94.5%) and π0.5 (92.4%). | p. 7 (15.4 Hz), p. 8 (4.3. Real-World Experiment) |
| Receding execution / feedback | As shown in Table 3, LaST0 achieves the best overall performance on realworld manipulation tasks, with a mean success rate of 72% ... | p. 8 (4.3. Real-World Experiment), p. 7 (15.4 Hz) |

## Failure and Ablation Link

- **p. 19 / Figure/Table caption - extractive PDF cue:** Table 10. Ablation on Latent Modalities. The effect of removing individual modalities on the action inter-class distance. Latent Modality Configuration Action Inter-class Distance w/o 2D ...
- **p. 7 / 15.4 Hz - extractive PDF cue:** Models Spatial Object Goal Long Mean S.R. ↑ OpenVLA 84.7 88.4 79.2 53.7 76.5 SpatialVLA 88.2 89.9 84.6 55.5 78.1 CogACT 97.2 98.0 90.2 88.8 ...
- **p. 20 / Figure/Table caption - extractive PDF cue:** Figure 9. Visualization of attention heatmaps. We visualize the attention heatmaps from the final layer of LaST0 on RLBench observations. The red area indicates the ...
- **p. 6 / 4. Experiment - extractive PDF cue:** Section 4.1 evaluates the manipulation performance and inference efficiency of LaST0 in simulation, while Section 4.2 conducts the ablation study of each component.
- **p. 8 / 4.2. Ablation Study - extractive PDF cue:** 5 c), we investigate the effect of the temporal horizon used in latent reasoning by varying the number of future time steps encoded into the ...
- **p. 6 / 4.1. Simulation Experiment - extractive PDF cue:** Since the point cloud modality is unavailable in LIBERO, we remove it from the latent CoT content.
- **p. 7 / 15.4 Hz - extractive PDF cue:** Ablation study on key design choices of LaST0.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.2. LaST0 Architecture), p. 4 (3.2. LaST0 Architecture), p. 5 (3.3. Latent Spatio-Temporal Chain-of-Thought), p. 3 (3.2. LaST0 Architecture), p. 5 (3.3. Latent Spatio-Temporal Chain-of-Thought), p. 3 (3.1. Preliminaries), objective p. 5 (3.5. Training Recipe), p. 5 (3.3. Latent Spatio-Temporal Chain-of-Thought), p. 4 (3.2. LaST0 Architecture), p. 6 (3.5. Training Recipe), p. 3 (3.1. Preliminaries), p. 4 (3.2. LaST0 Architecture), temporal p. 8 (4.2. Ablation Study), p. 1 (Front matter), p. 4 (3.2. LaST0 Architecture), p. 5 (3.4. Dual-System Coordination), p. 5 (3.3. Latent Spatio-Temporal Chain-of-Thought), p. 7 (15.4 Hz).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
