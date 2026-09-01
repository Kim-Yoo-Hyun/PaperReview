# Method - Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2209.05451; PDF retrieval source: https://arxiv.org/pdf/2209.05451. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction)): PERACT encodes language goals and RGB-D voxel observations with a Perceiver Transformer [1], and outputs discretized actions by "detecting the next best voxel action".

## Method Body Digest

- **p. 1 / Abstract - extractive body cue:** PERACT encodes language goals and RGB-D voxel observations with a Perceiver Transformer [1], and outputs discretized actions by "detecting the next best voxel action".
- **p. 2 / 1 Introduction - extractive body cue:** But in PERACT, we use a Perceiver2 Transformer [1] to encode very high-dimensional input of up to 1 million voxels with only a small set ...
- **p. 1 / 1 Introduction - extractive body cue:** In contrast, recent works in reinforcement-learning like C2FARM [14] construct a voxelized observation and action space to efficiently learn visual representations of 3D actions with ...
- **p. 2 / 1 Introduction - extractive body cue:** Our results show that PERACT significantly outperforms image-to-action agents (by 34×) and 3D ConvNet baselines (by 2.8×), without using any explicit representations of instance segmentations, ...
- **p. 1 / Abstract - extractive body cue:** Unlike frameworks that operate on 2D images, the voxelized 3D observation and action space provides a strong structural prior for efficiently learning 6-DoF actions.
- **p. 2 / 1 Introduction - extractive body cue:** This voxel-based formulation provides a strong structural prior with several benefits: a natural method for fusing multi-view observations, learning robust action-centric3 representations [18, 19], and ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: • A novel problem formulation for perceiving, acting, and specifying goals with Transformers. • An efficient action-centric framework ...
- **p. 1 / 1 Introduction - extractive body cue:** To this end, we present PERACT (short for PERCEIVER-ACTOR), a language-conditioned BC agent that can learn to imitate a wide variety of 6-DoF manipulation tasks ...
- **p. 2 / 1 Introduction - extractive body cue:** We also demonstrate our approach with a Franka Panda on 7 real-world tasks (k-o; only 5 shown) with a multi-task agent trained with just 53 ...

## Source Evidence Cues

- **p. 1 / Abstract - extractive body cue:** PERACT encodes language goals and RGB-D voxel observations with a Perceiver Transformer [1], and outputs discretized actions by "detecting the next best voxel action".
- **p. 2 / 1 Introduction - extractive body cue:** But in PERACT, we use a Perceiver2 Transformer [1] to encode very high-dimensional input of up to 1 million voxels with only a small set ...
- **p. 1 / 1 Introduction - extractive body cue:** In contrast, recent works in reinforcement-learning like C2FARM [14] construct a voxelized observation and action space to efficiently learn visual representations of 3D actions with ...
- **p. 2 / 1 Introduction - extractive body cue:** Our results show that PERACT significantly outperforms image-to-action agents (by 34×) and 3D ConvNet baselines (by 2.8×), without using any explicit representations of instance segmentations, ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | PERACT encodes language goals and RGB-D voxel observations with a Perceiver Transformer [1], and outputs discretized actions by "detecting the next best ... | p. 1 (Abstract), p. 2 (1 Introduction) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | But in PERACT, we use a Perceiver2 Transformer [1] to encode very high-dimensional input of up to 1 million voxels with only ... | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | In contrast, recent works in reinforcement-learning like C2FARM [14] construct a voxelized observation and action space to efficiently learn visual representations of ... | p. 1 (1 Introduction), p. 2 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | PERACT, encodes, language, goals, RGB-D, voxel, observations, Perceiver, Transformer, outputs, discretized, actions, detecting, next | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | PERACT, encodes, language, goals, RGB-D, voxel, observations, Perceiver, Transformer, outputs | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | summary, contributions, follows, novel, problem, formulation, perceiving, acting, specifying, goals | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | not recovered | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Abstract - extractive body cue:** PERACT encodes language goals and RGB-D voxel observations with a Perceiver Transformer [1], and outputs discretized actions by "detecting the next best voxel action".
- **p. 2 / 1 Introduction - extractive body cue:** Our results show that PERACT significantly outperforms image-to-action agents (by 34×) and 3D ConvNet baselines (by 2.8×), without using any explicit representations of instance segmentations, ...
- **p. 1 / Abstract - extractive body cue:** Unlike frameworks that operate on 2D images, the voxelized 3D observation and action space provides a strong structural prior for efficiently learning 6-DoF actions.
- **p. 2 / 1 Introduction - extractive body cue:** This voxel-based formulation provides a strong structural prior with several benefits: a natural method for fusing multi-view observations, learning robust action-centric3 representations [18, 19], and ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | The per-voxel features are then used to predict the next best action in terms of discretized translation, rotation, and gripper state at ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | So instead, for each demonstration ζ, we extract a set of keyframe actions {k1, k2, . . . , km} ⊂A that ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | During evaluation, an agent keeps taking actions until an oracle indicates task-completion or reaches a maximum of 25 steps. | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 Introduction - extractive body cue:** The code and pre-trained models will be made available at peract.github.io.
- **p. 7 / 4 Results - extractive body cue:** 0 10000 20000 30000 40000 Training Steps 0 20 40 60 80 100 Success Rate PerAct PerAct w/o skip PerAct w/o Perceiver PerAct w/ random ...
- **p. 7 / 4 Results - extractive body cue:** Local Receptive Fields 0 10000 20000 30000 40000 Training Steps 0 20 40 60 80 100 Success Rate PerAct C2FARM-BC [16,16] C2FARM-BC [32,32] C2FARM-BC [64,64] ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** PERACT, encodes, language, goals, RGB-D, voxel, observations, Perceiver, Transformer, outputs, discretized, actions, detecting, next, best, action, But, Perceiver2, encode, very.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | All keyframes from an episode have the same language goal, which is constructed from templates (but human-annotated for real-world tasks). | p. 6 (4 Results), p. 6 (4 Results) |
| Action / skill decoding | PERACT outperforms C2FARM-BC [14], the most competitive baseline, with an average improvement of 1.33× with 10 demos and 2.83× with 100 demos. | p. 7 (4 Results), p. 6 (4 Results) |
| Receding execution / feedback | Table 1. Multi-Task Test Results. Success rates (mean %) of various multi-task agents tasks trained with either 10 or 100 demonstrations per ... | p. 7 (Figure/Table caption), p. 24 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Ablation Experiments. Success rate of PER- ACT after ablating key components. Ablations. Table 1 reports PERACT w/o Lang, an agent without any language ...
- **p. 6 / 4 Results - extractive body cue:** The focus here is to evaluate the performance of a single multi-task agent trained on all tasks and variants.
- **p. 6 / 4 Results - extractive body cue:** These variants are randomly sampled during data generation, but kept consistent during evaluations for one-to-one comparisons.
- **p. 7 / 4 Results - extractive body cue:** Since additional training demonstrations include additional task variants to optimize for, they might end up hurting performance.
- **p. 8 / 4 Results - extractive body cue:** This could be addressed by scaling up expert data with more diverse tasks and task variants.
- **p. 8 / 4 Results - extractive body cue:** And [64] indicates a single level of a 643 voxel grid without the coarse-to-fine-grain scheme.
- **p. 23 / Figure/Table caption - extractive body cue:** Table 4. Sensitivity Analysis. Success rates (mean %) of various PERACT agents trained with 100 demonstrations per task. We investigate three factors that affect PERACT's ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), objective 본문 anchor 없음, temporal p. 3 (2 Related Work), p. 4 (2 Related Work), p. 5 (2 Related Work), p. 6 (4 Results), p. 1 (1 Introduction), p. 1 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
