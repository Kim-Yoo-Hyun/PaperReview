# Method - Embodied-R1: Reinforced Embodied Reasoning for General Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=i5wlozMFsQ; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/245153. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1)): As for Embodied-SFT, we used exactly the same data but trained with a supervised learning loss, kept the batch size at 128, and trained for 3 epochs.

## Method Body Digest

- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive body cue:** As for Embodied-SFT, we used exactly the same data but trained with a supervised learning loss, kept the batch size at 128, and trained for ...
- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive body cue:** Training Hyperparameters: We conducted model training on eight NVIDIA A100 40G GPUs.
- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive body cue:** In practice, we found that without this constraint, the model in the VTG task was prone to reward hacking behavior.
- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive body cue:** Each task utilizes a different combination of reward terms.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** This gap is largely attributed to two key challenges: (a) data scarcity, where limited embodied data prevents from sufficiently grounding language and vision with physical ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** To bridge this gap, we propose pointing as an intuitive and effective paradigm to connect high-level understanding with generalizable action.
- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive body cue:** It would tend to output only two points to form a straight line, which easily yields a high reward and prematurely terminates exploration.
- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive body cue:** We would like to add two clarifying points: First, if the task output fails to meet the required parsing format, subsequent analysis cannot proceed successfully, ...

## Design Rationale

- **p. 1 / 1 INTRODUCTION - extractive body cue:** To bridge this gap, we propose pointing as an intuitive and effective paradigm to connect high-level understanding with generalizable action.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Simultaneously, its embodiment-agnostic nature enables knowledge transfer across diverse robot platforms, resolving the heterogeneity challenge.
- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive body cue:** Second, for the VTG task, we introduced an additional constraint on the format: the generated visual trace must consist of exactly 8 points.

## Source Evidence Cues

- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive body cue:** As for Embodied-SFT, we used exactly the same data but trained with a supervised learning loss, kept the batch size at 128, and trained for ...
- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive body cue:** Training Hyperparameters: We conducted model training on eight NVIDIA A100 40G GPUs.
- **Detected method headings:** 3. Methodology & Reasoning (p. 26)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | As for Embodied-SFT, we used exactly the same data but trained with a supervised learning loss, kept the batch size at 128, ... | p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Training Hyperparameters: We conducted model training on eight NVIDIA A100 40G GPUs. | p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | As for Embodied-SFT, we used exactly the same data but trained with a supervised learning loss, kept the batch size at 128, ... | p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive body cue:** In practice, we found that without this constraint, the model in the VTG task was prone to reward hacking behavior.
- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive body cue:** Each task utilizes a different combination of reward terms.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | largely, attributed, challenges, data, scarcity, where, limited, embodied, prevents, sufficiently, grounding, language, vision, physical | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | largely, attributed, challenges, data, scarcity, where, limited, embodied, prevents, sufficiently | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | bridge, pointing, intuitive, effective, paradigm, connect, high-level, understanding, generalizable, action | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | practice, found, without, constraint, model, VTG, task, prone, reward, hacking | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1 INTRODUCTION - extractive body cue:** This gap is largely attributed to two key challenges: (a) data scarcity, where limited embodied data prevents from sufficiently grounding language and vision with physical ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** To bridge this gap, we propose pointing as an intuitive and effective paradigm to connect high-level understanding with generalizable action.
- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive body cue:** It would tend to output only two points to form a straight line, which easily yields a high reward and prematurely terminates exploration.
- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive body cue:** We would like to add two clarifying points: First, if the task output fails to meet the required parsing format, subsequent analysis cannot proceed successfully, ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Embodied-R1 then generated precise visual traces for each stage, successfully managing multi-step sequences. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | On the VABench-V benchmark, Embodied-R1 achieves the lowest RMSE and MAE, indicating its ability to produce precise point sequences for traces, a ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | As for Embodied-SFT, we used exactly the same data but trained with a supervised learning loss, kept the batch size at 128, ... | hardware, batch and throughput |

## Training vs Inference

- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive body cue:** As for Embodied-SFT, we used exactly the same data but trained with a supervised learning loss, kept the batch size at 128, and trained for ...
- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive body cue:** Training Hyperparameters: We conducted model training on eight NVIDIA A100 40G GPUs.
- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive body cue:** As for Embodied-SFT, we used exactly the same data but trained with a supervised learning loss, kept the batch size at 128, and trained for ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** For all experiments, we focus on comparing SFT models trained with the same batch size and data, which we refer to as Embodied-SFT.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Embodied-SFT, exactly, same, data, trained, supervised, learning, loss, kept, batch, size, epochs, Training, Hyperparameters, conducted, model, eight, NVIDIA, A100, GPUs.
- **Relevant PDF headings:** 3. Methodology & Reasoning (p. 26).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Our evaluation encompassed 11 QA benchmarks, 4 simulated tasks (SIMPLEREnv) (Li et al., 2024b), and 8 real-world robot (xArm platform) tasks. | p. 6 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Action / skill decoding | Figure 2: Overview of four embodied pointing abilities. a VLM trained with RFT to resolve the multi-solution dilemma for embodied pointing, delivering ... | p. 3 (Figure/Table caption), p. 8 (4 EXPERIMENTS) |
| Receding execution / feedback | 5, Embodied-R1 achieves an 87.5% zero-shot success rate, an improvement of over 60% compared to the RoboPoint and FSD baselines. | p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We also included two key ablations: Embodied-R1 w/o CS, which excludes the ViRL common-sense dataset, and Embodied-SFT, a variant trained only with SFT.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** It achieves an average rank of 2.1, significantly outperforming its variants trained without common-sense data (Embodied-R1 w/o CS, Rank 3.4) or with only SFT (Embodied-SFT, ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** These results suggest that explicit visual reasoning provides superior zero-shot generalization compared to end-to-end policy learning, particularly when facing unseen instructions and background variations without ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We compared performance against a comprehensive suite of baselines across three categories: (1) End-to-end VLAs, including standard models (Octo, OpenVLA, π0) and stronger variants (π0-fast, ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** We trained four variants on RRG benchmarks.
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** 4.4 FURTHER ANALYSIS AND ABLATIONS Embodied-R1 Exhibits Strong Generalization.
- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive body cue:** In practice, we found that without this constraint, the model in the VTG task was prone to reward hacking behavior.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1), objective p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1), temporal p. 10 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1), p. 2 (8 Real-World Tasks).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
