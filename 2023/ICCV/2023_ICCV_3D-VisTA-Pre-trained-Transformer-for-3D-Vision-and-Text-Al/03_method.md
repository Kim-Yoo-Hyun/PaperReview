# Method - 3D-VisTA: Pre-trained Transformer for 3D Vision and Text Alignment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2308.04352; PDF retrieval source: https://arxiv.org/pdf/2308.04352. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.4. Self-supervised Pre-training), p. 4 (3.4. Self-supervised Pre-training)): Our final pre-training objective is obtained by simply adding the losses of the proxy tasks above: Lpre-train = LMLM + LMOM + LSTM (5) Notably, the proposed pre-training scheme is ...

## Method Body Digest

- **p. 4 / 3.4. Self-supervised Pre-training - extractive PDF cue:** Our final pre-training objective is obtained by simply adding the losses of the proxy tasks above: Lpre-train = LMLM + LMOM + LSTM (5) Notably, ...
- **p. 4 / 3.4. Self-supervised Pre-training - extractive PDF cue:** However, we mask a 3D object token by only replacing its point features and semantic embedding (i.e., "fi + Wcci" in Eq.
- **p. 4 / 3.4. Self-supervised Pre-training - extractive PDF cue:** More specifically, we extract the output corresponds to [CLS] as the global representation of the input scene-text pair, and feed it into a two-layer MLP ...
- **p. 2 / 1. Introduction - extractive PDF cue:** It effectively learns the 3D point cloud and text alignment and further simplifies and improves downstream task fine-tuning. • We fine-tune 3D-VisTA and achieve state-of-the-art ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Aligning the 3D physical world with natural language is a crucial step towards embodied artificial intelligence [18, 26, 37], where intelligent agents can understand and ...
- **p. 2 / 1. Introduction - extractive PDF cue:** The proposed pretraining procedure effectively learns the alignment between 3D point clouds and texts, which eliminates the need for auxiliary losses and optimization tricks in ...
- **p. 4 / 3.4. Self-supervised Pre-training - extractive PDF cue:** (4) In practice, 30% of the samples in a training batch are negative pairs, created by replacing the scene point cloud or text with a ...
- **p. 1 / 1. Introduction - extractive PDF cue:** The lack of a simple and unified approach creates a significant gap in developing a general-purpose 3D-VL model.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Our main contributions can be summarized as follows: • We propose 3D-VisTA, a simple and unified Transformer for aligning 3D vision and text.
- **p. 1 / 1. Introduction - extractive PDF cue:** To fill such gap, we introduce 3D-VisTA, a Transformerbased model for 3D Vision and Text Alignment that can be easily adapted to various downstream tasks.
- **p. 2 / 1. Introduction - extractive PDF cue:** Inspired by the success of large-scale pre-training in NLP [15, 41, 42, 6, 52, 31], CV [22, 17, 21, 25, 38], and 2D-VL [30, 2, ...

## Source Evidence Cues

- **p. 4 / 3.4. Self-supervised Pre-training - extractive PDF cue:** Our final pre-training objective is obtained by simply adding the losses of the proxy tasks above: Lpre-train = LMLM + LMOM + LSTM (5) Notably, ...
- **p. 4 / 3.4. Self-supervised Pre-training - extractive PDF cue:** However, we mask a 3D object token by only replacing its point features and semantic embedding (i.e., "fi + Wcci" in Eq.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Our final pre-training objective is obtained by simply adding the losses of the proxy tasks above: Lpre-train = LMLM + LMOM + ... | p. 4 (3.4. Self-supervised Pre-training), p. 4 (3.4. Self-supervised Pre-training) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | However, we mask a 3D object token by only replacing its point features and semantic embedding (i.e., "fi + Wcci" in Eq. | p. 4 (3.4. Self-supervised Pre-training) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Our final pre-training objective is obtained by simply adding the losses of the proxy tasks above: Lpre-train = LMLM + LMOM + ... | p. 4 (3.4. Self-supervised Pre-training) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.4. Self-supervised Pre-training - extractive PDF cue:** Our final pre-training objective is obtained by simply adding the losses of the proxy tasks above: Lpre-train = LMLM + LMOM + LSTM (5) Notably, ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3.4. Self-supervised Pre-training).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | More, specifically, extract, output, corresponds, CLS, global, representation, input, scene-text, pair, feed, two-layer, MLP | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | More, specifically, extract, output, corresponds, CLS, global, representation, input, scene-text | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | main, contributions, summarized, follows, D-VisTA, simple, unified, Transformer, aligning, vision | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | final, pre-training, objective, obtained, simply, adding, losses, proxy, tasks, above | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.4. Self-supervised Pre-training - extractive PDF cue:** More specifically, we extract the output corresponds to [CLS] as the global representation of the input scene-text pair, and feed it into a two-layer MLP ...
- **p. 2 / 1. Introduction - extractive PDF cue:** It effectively learns the 3D point cloud and text alignment and further simplifies and improves downstream task fine-tuning. • We fine-tune 3D-VisTA and achieve state-of-the-art ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Aligning the 3D physical world with natural language is a crucial step towards embodied artificial intelligence [18, 26, 37], where intelligent agents can understand and ...
- **p. 2 / 1. Introduction - extractive PDF cue:** The proposed pretraining procedure effectively learns the alignment between 3D point clouds and texts, which eliminates the need for auxiliary losses and optimization tricks in ...
- **p. 4 / 3.4. Self-supervised Pre-training - extractive PDF cue:** (4) In practice, 30% of the samples in a training batch are negative pairs, created by replacing the scene point cloud or text with a ...
- **p. 1 / 1. Introduction - extractive PDF cue:** The lack of a simple and unified approach creates a significant gap in developing a general-purpose 3D-VL model.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | The learning rate is set to 1e-4, with a warmup of 3,000 steps, and cosine decay. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | 3D Dense Captioning (e.g., Scan2Cap) Figure 1: Overall framework of our 3D-VisTA pipeline. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | The learning rate is set to 1e-4, with a warmup of 3,000 steps, and cosine decay. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.4. Self-supervised Pre-training - extractive PDF cue:** Our final pre-training objective is obtained by simply adding the losses of the proxy tasks above: Lpre-train = LMLM + LMOM + LSTM (5) Notably, ...
- **p. 5 / 5.1. Experimental Settings - extractive PDF cue:** The pre-training runs for 30 epochs with a batch size of 128.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** final, pre-training, objective, obtained, simply, adding, losses, proxy, tasks, above, Lpre-train, LMLM, LMOM, LSTM, Notably, scheme, self-supervised, task-agnostic, unlike, supervised.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We evaluate our model on three datasets for this task: ScanRefer [8], Nr3D, and Sr3D [1]. | p. 5 (5.1. Experimental Settings), p. 5 (5.1. Experimental Settings) |
| Semantic / temporal fusion | 3D-VisTA achieves competitive results with SOTA on Nr3D and outperforms SOTA on Sr3D. | p. 6 (5.1. Experimental Settings), p. 6 (5.2. Downstream Task Results) |
| Robot query / planning handoff | Table 4: Grounding accuracy (%) on Nr3D and Sr3D with ground-truth object proposals. ∆denotes the performance difference between 3D-VisTA and 3D-VisTA (scratch). ... | p. 6 (Figure/Table caption), p. 6 (5.1. Experimental Settings) |

## Failure and Ablation Link

- **p. 5 / 5.1. Experimental Settings - extractive PDF cue:** In ablation studies, we use ground-truth masks in all tasks for simplicity.
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: The model architecture of our 3D-VisTA, which includes text encoding, scene encoding, and multi-modal fusion modules. 3D-VisTA is pre-trained by self-supervised learning objectives, ...
- **p. 6 / 5.2. Downstream Task Results - extractive PDF cue:** Of note, 3DVisTA is trained on these datasets simply using the task losses, without any auxiliary losses or optimization tricks,
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 9: Ablation studies of 3D-VisTA w.r.t. Transformer depth, pre- training objectives, and pre-training data. We report the grounding accuracy on ScanRefer for Visual Grounding ...
- **p. 5 / 5.1. Experimental Settings - extractive PDF cue:** Both pre-training and fine-tuning are conducted on a single NVIDIA A100 80GB GPU.
- **p. 7 / 5.2. Downstream Task Results - extractive PDF cue:** Pretraining improves the results of most question types.
- **p. 8 / 5.4. Qualitative Studies and Additional Results - extractive PDF cue:** 4, pretraining improves the spatial understanding of 3D-VisTA for visual grounding, so it can better align with human prior viewpoint and reason over spatial relations.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.4. Self-supervised Pre-training), p. 4 (3.4. Self-supervised Pre-training), objective p. 4 (3.4. Self-supervised Pre-training), temporal p. 5 (5.1. Experimental Settings), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.1. Text Encoding), p. 3 (3.2. Scene Encoding).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
