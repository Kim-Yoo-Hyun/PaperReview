# Method - VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=QZYZ0Xm58q; PDF retrieval source: https://arxiv.org/pdf/2502.02175. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3 Methodology), p. 3 (3 Methodology)): To address this, we propose a method that identifies visually static tokens and filters out semantically important ones based on attention scores from the VLA decoder.

## Method Body Digest

- **p. 3 / 3 Methodology - extractive body cue:** To address this, we propose a method that identifies visually static tokens and filters out semantically important ones based on attention scores from the VLA ...
- **p. 3 / 3 Methodology - extractive body cue:** In the following sections, we introduce its core mechanisms: static token selection, task-relevance filtering, and layer-adaptive reuse to accelerate VLA inference while preserving action accuracy.
- **p. 3 / 3 Methodology - extractive body cue:** In robotic action prediction, most visual tokens remain static across frames except for key regions like the manipulator or target object.
- **p. 3 / 3 Methodology - extractive body cue:** By avoiding redundant computation of unchanged static tokens between adjacent frames, our approach directly alleviates the computation bottleneck of language decoder in VLA models while ...
- **p. 3 / 3 Methodology - extractive body cue:** However, most existing Vision-Language-Action (VLA) 3
- **p. 3 / 3 Methodology - extractive body cue:** (3) While KV caching is effective for language decoding within a single query in vision-language models, this technique does not address redundancy in the visual ...
- **p. 1 / 1 Introduction - extractive body cue:** Leveraging large-scale real-world robotic datasets [6, 7], pioneering works [8-11] have introduced Vision-Language-Action (VLA) models, which integrate vision and language modalities to directly generate robotic ...
- **p. 1 / 1 Introduction - extractive body cue:** Learning a robust and generalizable policy for robotic manipulation through policy learning has long been a challenging problem [1], with traditional reinforcement learning approaches [2, ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** To address the inefficiency introduced by repeatedly processing static visual information, we present VLA-Cache, a training-free inference acceleration method that exploits temporal continuity in robotic ...
- **p. 3 / 3 Methodology - extractive body cue:** To address this, we propose a method that identifies visually static tokens and filters out semantically important ones based on attention scores from the VLA ...
- **p. 3 / 3 Methodology - extractive body cue:** In the following sections, we introduce its core mechanisms: static token selection, task-relevance filtering, and layer-adaptive reuse to accelerate VLA inference while preserving action accuracy.

## Source Evidence Cues

- **p. 3 / 3 Methodology - extractive body cue:** To address this, we propose a method that identifies visually static tokens and filters out semantically important ones based on attention scores from the VLA ...
- **p. 3 / 3 Methodology - extractive body cue:** In the following sections, we introduce its core mechanisms: static token selection, task-relevance filtering, and layer-adaptive reuse to accelerate VLA inference while preserving action accuracy.
- **Detected method headings:** 3 Methodology (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | To address this, we propose a method that identifies visually static tokens and filters out semantically important ones based on attention scores ... | p. 3 (3 Methodology), p. 3 (3 Methodology) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | In the following sections, we introduce its core mechanisms: static token selection, task-relevance filtering, and layer-adaptive reuse to accelerate VLA inference while ... | p. 3 (3 Methodology) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | To address this, we propose a method that identifies visually static tokens and filters out semantically important ones based on attention scores ... | p. 3 (3 Methodology) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3 Methodology - extractive body cue:** In robotic action prediction, most visual tokens remain static across frames except for key regions like the manipulator or target object.
- **p. 3 / 3 Methodology - extractive body cue:** By avoiding redundant computation of unchanged static tokens between adjacent frames, our approach directly alleviates the computation bottleneck of language decoder in VLA models while ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | However, most, existing, Vision-Language-Action, VLA, While, caching, effective, language, decoding, within, single, query, vision-language | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | However, most, existing, Vision-Language-Action, VLA, While, caching, effective, language, decoding | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | address, inefficiency, introduced, repeatedly, processing, static, visual, information, present, VLA-Cache | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | robotic, action, prediction, most, visual, tokens, remain, static, across, frames | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3 Methodology - extractive body cue:** However, most existing Vision-Language-Action (VLA) 3
- **p. 3 / 3 Methodology - extractive body cue:** (3) While KV caching is effective for language decoding within a single query in vision-language models, this technique does not address redundancy in the visual ...
- **p. 1 / 1 Introduction - extractive body cue:** Leveraging large-scale real-world robotic datasets [6, 7], pioneering works [8-11] have introduced Vision-Language-Action (VLA) models, which integrate vision and language modalities to directly generate robotic ...
- **p. 1 / 1 Introduction - extractive body cue:** Learning a robust and generalizable policy for robotic manipulation through policy learning has long been a challenging problem [1], with traditional reinforcement learning approaches [2, ...
- **p. 2 / 1 Introduction - extractive body cue:** This motivates our proposed token caching mechanism, which explicitly exploits temporal redundancy in visual inputs to reduce redundant computation without compromising decision quality.
- **p. 2 / 1 Introduction - extractive body cue:** The resulting method VLA-Cache offers a training-free and plug-and-play solution for accelerating VLA models without sacrificing action performance.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | When applied to OpenVLA-OFT, a faster variant with action chunking, VLA-Cache further boosts control frequency by nearly 14 Hz, showing strong compatibility ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | 1 2 3 4 1 4 2 3 6 2 6 1 7 1 3 2 2 6 5 4 8 3 ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | When applied to OpenVLA-OFT, a faster variant with action chunking, VLA-Cache further boosts control frequency by nearly 14 Hz, showing strong compatibility ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3 Methodology - extractive body cue:** In the following sections, we introduce its core mechanisms: static token selection, task-relevance filtering, and layer-adaptive reuse to accelerate VLA inference while preserving action accuracy.
- **p. 9 / 5 Experiment - extractive body cue:** The method also achieves considerable reductions in FLOPs and inference time.
- **p. 9 / 5 Experiment - extractive body cue:** The efficiency gains are evident in the FLOPs and inference time measurements.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** address, identifies, visually, static, tokens, filters, semantically, important, ones, attention, scores, VLA, decoder, following, sections, introduce, core, mechanisms, token, selection.
- **Relevant PDF headings:** 3 Methodology (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | (Hz) ↑ PickPot PlaceCube PutSausage WipeTable Average OpenVLA 95.0% 83.3% 80.0% 70.0% 82.1% 1.814 64.16 4.02 + VLA-Cache 90.0% 90.0% 85.0% 73.3% ... | p. 9 (5 Experiment), p. 7 (5 Experiment) |
| Action / skill decoding | Specifically, we adopt two state-of-the-art token-level acceleration techniques SparseVLM [30] and FastV [29] on OpenVLA as compared methods in the LIBERO benchmark. | p. 7 (5 Experiment), p. 15 (Figure/Table caption) |
| Receding execution / feedback | Figure 4: Visualization of VLA-Cache token reuse across settings. (a) LIBERO simulation with OpenVLA. (b) Real-world task under dynamic background. (c) and ... | p. 9 (Figure/Table caption), p. 8 (5 Experiment) |

## Failure and Ablation Link

- **p. 16 / Figure/Table caption - extractive body cue:** Table 10: Varying the relevance threshold τ (with k=100). Overall, efficiency (FLOPs and latency) improves monotonically with larger k and τ, while success rate remains ...
- **p. 7 / 5 Experiment - extractive body cue:** The SIMPLER simulator [18] offers two settings, Visual Matching and Variant Aggregation, designed to bridge simulation-to-reality gaps.
- **p. 8 / 5 Experiment - extractive body cue:** Ablation on Token Reusing/Pruning Rate.
- **p. 8 / 5 Experiment - extractive body cue:** When applied to OpenVLA-OFT, a faster variant with action chunking, VLA-Cache further boosts control frequency by nearly 14 Hz, showing strong compatibility with high-frequency architectures ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 5: VLA-Cache test results and attention heat map in a simulated environment E.3 Additional Ablations and Comparisons Attention vs. object-mask proxies for task relevance. ...
- **p. 16 / Figure/Table caption - extractive body cue:** Table 8: Attention vs. object-mask proxies for task relevance on LIBERO-SPATIAL. While object masks provide spatial localization, they can miss fine-grained or contextual signals essential ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Tasks on LIBERO Benchmark, the SIMPLER Environment and Real World. Total Complexity Reduction. Bringing all components together, the theoretical overall FLOP reduction per ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3 Methodology), p. 3 (3 Methodology), objective p. 3 (3 Methodology), p. 3 (3 Methodology), temporal p. 8 (5 Experiment), p. 4 (X X), p. 6 (V Hl), p. 6 (V Hl), p. 2 (1 Introduction), p. 3 (3 Methodology).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
