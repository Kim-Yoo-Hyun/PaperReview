# Method - RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=yAzN4tz7oI; PDF retrieval source: https://openreview.net/pdf/29d56379d000b8c0e05906c5958e67e2e870ab0c.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)): In this paper, we introduce the Robotics Diffusion Transformer (RDT), the largest bimanual manipulation foundation model with strong generalizability.

## Method Body Digest

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we introduce the Robotics Diffusion Transformer (RDT), the largest bimanual manipulation foundation model with strong generalizability.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To further enable training RDT on heterogeneous data, we propose the Physically Interpretable Unified Action Space, a unified action format for various robots with gripper ...
- **p. 1 / ABSTRACT - extractive body cue:** Bimanual manipulation is essential in robotics, yet developing foundation models is extremely challenging due to the inherent complexity of coordinating two robot arms (leading to ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** First, the doubled action space induces multi-modal action distributions (Li, 2006; Jia et al., 2024) (see Fig.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Compared with unimanual manipulation, bimanual manipulation has more possible action modes, leading to stronger multi-modality.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The prohibitive costs of dual-arm systems create severe data scarcity (Sharma et al., 2018; Collaboration et al., 2023), fundamentally conflicting with the datahungry nature of ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Beyond architectural constraints, physical and action space variations across robots introduce data heterogeneity that risks negative transfer (Pan & Yang, 2009).
- **p. 1 / ABSTRACT - extractive body cue:** It exhibits zeroshot generalization to unseen objects and scenes, understands and follows language instructions, learns new skills with just 1∼5 demonstrations, and effectively handles complex, ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we introduce the Robotics Diffusion Transformer (RDT), the largest bimanual manipulation foundation model with strong generalizability.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To further enable training RDT on heterogeneous data, we propose the Physically Interpretable Unified Action Space, a unified action format for various robots with gripper ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Developing bimanual manipulation foundation models confronts the dual challenges of data scarcity and architectural limitations.

## Source Evidence Cues

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we introduce the Robotics Diffusion Transformer (RDT), the largest bimanual manipulation foundation model with strong generalizability.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To further enable training RDT on heterogeneous data, we propose the Physically Interpretable Unified Action Space, a unified action format for various robots with gripper ...
- **p. 1 / ABSTRACT - extractive body cue:** Bimanual manipulation is essential in robotics, yet developing foundation models is extremely challenging due to the inherent complexity of coordinating two robot arms (leading to ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** First, the doubled action space induces multi-modal action distributions (Li, 2006; Jia et al., 2024) (see Fig.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Compared with unimanual manipulation, bimanual manipulation has more possible action modes, leading to stronger multi-modality.
- **Detected method headings:** B ARCHITECTURE DETAILS (p. 19)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | In this paper, we introduce the Robotics Diffusion Transformer (RDT), the largest bimanual manipulation foundation model with strong generalizability. | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | To further enable training RDT on heterogeneous data, we propose the Physically Interpretable Unified Action Space, a unified action format for various ... | p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Bimanual manipulation is essential in robotics, yet developing foundation models is extremely challenging due to the inherent complexity of coordinating two robot ... | p. 1 (ABSTRACT), p. 1 (1 INTRODUCTION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / 1 INTRODUCTION - extractive body cue:** The prohibitive costs of dual-arm systems create severe data scarcity (Sharma et al., 2018; Collaboration et al., 2023), fundamentally conflicting with the datahungry nature of ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Beyond architectural constraints, physical and action space variations across robots introduce data heterogeneity that risks negative transfer (Pan & Yang, 2009).
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 2 (1 INTRODUCTION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | exhibits, zeroshot, generalization, unseen, objects, scenes, understands, follows, language, instructions, learns, skills, just, demonstrations | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | exhibits, zeroshot, generalization, unseen, objects, scenes, understands, follows, language, instructions | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | introduce, Robotics, Diffusion, Transformer, RDT, largest, bimanual, manipulation, foundation, model | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | prohibitive, costs, dual-arm, systems, create, severe, data, scarcity, Sharma, Collaboration | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / ABSTRACT - extractive body cue:** It exhibits zeroshot generalization to unseen objects and scenes, understands and follows language instructions, learns new skills with just 1∼5 demonstrations, and effectively handles complex, ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To further enable training RDT on heterogeneous data, we propose the Physically Interpretable Unified Action Space, a unified action format for various robots with gripper ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** First, the doubled action space induces multi-modal action distributions (Li, 2006; Jia et al., 2024) (see Fig.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In particular, RDT has exceptional zero-shot and few-shot (1 ∼5 shots) generalizability to unseen objects, scenes, instructions, and even skills.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Compared with unimanual manipulation, bimanual manipulation has more possible action modes, leading to stronger multi-modality.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | It can reduce the diffusion steps required to sample an action chunk from 100 steps to 5 steps, achieving an action chunk ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Inputs: proprioception zt, noisy action chunk ˜at:t+Ta, control frequency c, and diffusion time step k, acting as denoising inputs; image inputs (Timg ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | It can reduce the diffusion steps required to sample an action chunk from 100 steps to 5 steps, achieving an action chunk ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To further enable training RDT on heterogeneous data, we propose the Physically Interpretable Unified Action Space, a unified action format for various robots with gripper ...
- **p. 1 / ABSTRACT - extractive body cue:** Bimanual manipulation is essential in robotics, yet developing foundation models is extremely challenging due to the inherent complexity of coordinating two robot arms (leading to ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** It can reduce the diffusion steps required to sample an action chunk from 100 steps to 5 steps, achieving an action chunk inference frequency of ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** It takes three days to fine-tune this model using the same GPUs for 130K steps.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** introduce, Robotics, Diffusion, Transformer, RDT, largest, bimanual, manipulation, foundation, model, strong, generalizability, further, enable, training, heterogeneous, data, Physically, Interpretable, Unified.
- **Relevant PDF headings:** B ARCHITECTURE DETAILS (p. 19).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | We aim to answer the following questions through real-robot experiments: Q1: Can RDT zero-shot generalize to unseen objects and scenes? | p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Action / skill decoding | 5.2 RESULTS ANALYSIS From the results in Table 3, we can see that RDT consistently outperforms other baselines. | p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Receding execution / feedback | In Wash Cup and Pour Water, RDT can still achieve a high success rate on unseen scenarios, and its performance is not ... | p. 9 (5 EXPERIMENTS), p. 10 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 9 / 5 EXPERIMENTS - extractive body cue:** VARIANT NAME UNSEEN OBJECT UNSEEN SCENE INSTRUCTION FOLLOWING RDT (regress) 12.5 50 12.5 RDT (small) 37.5 62.5 25 RDT (scratch) 0 25 62.5 RDT (ours) ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Ablation study results. Here are the success rates (%) of the original RDT and its three variants in tasks of Wash Cup (unseen ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** In Table 2, there is a serious performance drop without any of these factors, demonstrating the necessity of our contributions.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Overview of Robotics Diffusion Transformer with 1B-Parameters (RDT-1B), a language-conditioned visuomotor policy for bimanual manipulation,with state-of-the-art generaliz- ability to unseen scenarios (See App. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: (a) Unstable loss curve during training without QKNorm & RMSNorm. (b) Success rates of RDT (w/o MLP Decoder or w/o ACI) in tasks ...
- **p. 25 / Figure/Table caption - extractive body cue:** Table 7: Comparision of different baselines. We compare baselines as well as different variants of our model in terms of model size, data size, and ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** We use the pre-training and fine-tuning datasets in Sec.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), objective p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), temporal p. 8 (5 EXPERIMENTS), p. 4 (2 RELATED WORK), p. 5 (2 RELATED WORK), p. 4 (2 RELATED WORK), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (28 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Bimanual manipulation is essential in robotics, yet developing foundation models is extremely challenging due to the inherent complexity of coordinating two robot arms (leading to multi-modal action distributions) and the ... (p. 1, ABSTRACT).
- **Objective/update evidence:** The prohibitive costs of dual-arm systems create severe data scarcity (Sharma et al., 2018; Collaboration et al., 2023), fundamentally conflicting with the datahungry nature of foundation models. (p. 1, 1 INTRODUCTION).
- **Temporal/runtime evidence:** It can reduce the diffusion steps required to sample an action chunk from 100 steps to 5 steps, achieving an action chunk inference frequency of 6 Hz (action chunks per ... (p. 8, 5 EXPERIMENTS).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
