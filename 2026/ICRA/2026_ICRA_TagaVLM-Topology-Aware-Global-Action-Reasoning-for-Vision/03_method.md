# Method - TagaVLM: Topology-Aware Global Action Reasoning for Vision-Language Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_5.html; PDF retrieval source: https://arxiv.org/pdf/2603.02972. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD), p. 3 (III. METHOD)): In the following subsections, we will elaborate on the four key components of our framework: (1) online topological map for global environment representation, (2) Interleaved Navigation Prompt for task adaptation, ...

## Method Body Digest

- **p. 3 / III. METHOD - extractive PDF cue:** In the following subsections, we will elaborate on the four key components of our framework: (1) online topological map for global environment representation, (2) Interleaved ...
- **p. 4 / III. METHOD - extractive PDF cue:** Given Gt and the stored visual representations of each node Vt = {vt i}Kt i=1, an effective pretrained Vision Transformer (ViT) [37] is employed as ...
- **p. 4 / III. METHOD - extractive PDF cue:** (1) This approach ensures that the visual features of each node contextually correspond to the node IDs and node types within the prompt, thereby strengthening ...
- **p. 5 / III. METHOD - extractive PDF cue:** 4, with the global action reasoning ability, the proposed model is able to efficiently correct the decision error in the first navigation step.
- **p. 5 / III. METHOD - extractive PDF cue:** In the training process, the TagaVLM is finetuned with the single-step action prediction (SAP) task to align the instruction-trajectory paired data of VLN with the ...
- **p. 3 / III. METHOD - extractive PDF cue:** Each node vt i ∈Vt is represented by its observations.
- **p. 5 / III. METHOD - extractive PDF cue:** The training is conducted entirely in a teacher-forcing manner, where cross-entropy loss is computed between the predicted node index and the ground truth.
- **p. 3 / III. METHOD - extractive PDF cue:** Online Topological Map Environment Representation The online topological map, crucial in traditional VLN, can provide explicit visual-spatial correspondences at a low computational cost.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Our contribution can be summarized as follows: • We introduce TagaVLM, an end-to-end VLN framework that architecturally embeds topological structures into the VLM backbone. • ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Instead, other methods usually act on local space, which only consists of local navigable viewpoints directly connected to the current viewpoint.
- **p. 3 / III. METHOD - extractive PDF cue:** In the following subsections, we will elaborate on the four key components of our framework: (1) online topological map for global environment representation, (2) Interleaved ...

## Source Evidence Cues

- **p. 3 / III. METHOD - extractive PDF cue:** In the following subsections, we will elaborate on the four key components of our framework: (1) online topological map for global environment representation, (2) Interleaved ...
- **p. 4 / III. METHOD - extractive PDF cue:** Given Gt and the stored visual representations of each node Vt = {vt i}Kt i=1, an effective pretrained Vision Transformer (ViT) [37] is employed as ...
- **p. 4 / III. METHOD - extractive PDF cue:** (1) This approach ensures that the visual features of each node contextually correspond to the node IDs and node types within the prompt, thereby strengthening ...
- **p. 5 / III. METHOD - extractive PDF cue:** 4, with the global action reasoning ability, the proposed model is able to efficiently correct the decision error in the first navigation step.
- **p. 5 / III. METHOD - extractive PDF cue:** In the training process, the TagaVLM is finetuned with the single-step action prediction (SAP) task to align the instruction-trajectory paired data of VLN with the ...
- **p. 3 / III. METHOD - extractive PDF cue:** Each node vt i ∈Vt is represented by its observations.
- **Detected method headings:** III. METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | In the following subsections, we will elaborate on the four key components of our framework: (1) online topological map for global environment ... | p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Given Gt and the stored visual representations of each node Vt = {vt i}Kt i=1, an effective pretrained Vision Transformer (ViT) [37] ... | p. 4 (III. METHOD), p. 4 (III. METHOD) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | (1) This approach ensures that the visual features of each node contextually correspond to the node IDs and node types within the ... | p. 4 (III. METHOD), p. 5 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / III. METHOD - extractive PDF cue:** The training is conducted entirely in a teacher-forcing manner, where cross-entropy loss is computed between the predicted node index and the ground truth.
- **p. 3 / III. METHOD - extractive PDF cue:** Online Topological Map Environment Representation The online topological map, crucial in traditional VLN, can provide explicit visual-spatial correspondences at a low computational cost.
- **p. 4 / III. METHOD - extractive PDF cue:** The system prompt employs a structured organization, sequentially specifying the role, task, context, execution rules, response format, and constraint conditions for the LLM.
- **p. 5 / III. METHOD - extractive PDF cue:** Its core design-a learnable, per-head residual attention bias-implements the topological map as a flexible inductive prior, not a rigid constraint.
- **p. 3 / III. METHOD - extractive PDF cue:** As the navigation process progresses, the agent moves between navigable nodes along connected edges, and more nodes are gradually observed.
- **p. 4 / III. METHOD - extractive PDF cue:** Et is updated accordingly, and the visual representations of current and candidate nodes are simultaneously updated based on new observations from vt c.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 4 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD), p. 4 (III. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Then, matrix, STAR-Att, together, input, prompt, output, features, Observation/Map, text, format, RGB, Observation, Global/Local | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Then, matrix, STAR-Att, together, input, prompt, output, features, Observation/Map, text | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | contribution, summarized, follows, introduce, TagaVLM, end-to-end, VLN, framework, architecturally, embeds | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | training, conducted, entirely, teacher-forcing, manner, where, cross-entropy, loss, computed, between | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / III. METHOD - extractive PDF cue:** Then, this matrix is fed into the proposed STAR-Att, together with the input prompt Pt to get the output features ˜Pt.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Observation/Map In text format RGB Observation RGB Observation Global/Local Action Global Action Topology information LLM (c) Other Methods TagaVLM STAR-Att STAR-Att STAR-Att (b) Our TagaVLM ...
- **p. 5 / III. METHOD - extractive PDF cue:** In the training process, the TagaVLM is finetuned with the single-step action prediction (SAP) task to align the instruction-trajectory paired data of VLN with the ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** 1(c), most large-model-based methods, e.g., NavGPT [12], LangNav [13], NavCot [14] etc., employ a pretrained VLM to preprocess visual observations into text format, and use ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** First, the proposed method designs a specialized image-text Interleaved Navigation Prompt (INP) to better align the textual and visual information from the same node in ...
- **p. 3 / III. METHOD - extractive PDF cue:** To endow the VLM with inherent spatial understanding ability and topological-visual alignment power, while keeping its pretrained knowledge, in this work, a fully end-toend Topology-Aware ...
- **p. 3 / III. METHOD - extractive PDF cue:** In the following subsections, we will elaborate on the four key components of our framework: (1) online topological map for global environment representation, (2) Interleaved ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | At each time step, the agent selects at i and is required to output in a fixed format, such as: "<node>i</node>" or ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | At the navigation step t, the online topological map is denoted by Gt = {Vt,Et} ⊂G, where Vt = {vi}Kt i=1 is ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / III. METHOD - extractive PDF cue:** In the following subsections, we will elaborate on the four key components of our framework: (1) online topological map for global environment representation, (2) Interleaved ...
- **p. 4 / III. METHOD - extractive PDF cue:** Given Gt and the stored visual representations of each node Vt = {vt i}Kt i=1, an effective pretrained Vision Transformer (ViT) [37] is employed as ...
- **p. 5 / III. METHOD - extractive PDF cue:** In the training process, the TagaVLM is finetuned with the single-step action prediction (SAP) task to align the instruction-trajectory paired data of VLN with the ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** following, subsections, will, elaborate, four, components, framework, online, topological, global, environment, representation, Interleaved, Navigation, Prompt, task, adaptation, Spatial, Topology, Aware.
- **Relevant PDF headings:** III. METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | For testing, we utilize 1,021 navigation paths from the val seen split and 2,349 paths from the val unseen split in the ... | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Global / local decision | It is worth noting that, our 0.5B parameter model already outperforms most largemodel-based methods and achieves comparable performance to state-of-the-art approaches with ... | p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Motion execution / recovery | It is worth noting that, our 0.5B parameter model already outperforms most largemodel-based methods and achieves comparable performance to state-of-the-art approaches with ... | p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** Ablation Study To explore the effectiveness of key components in our approach and their impacts on navigation performance, we designed a series of ablation experiments ...
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** II, all the essential components, including STAR-Att, are removed, and by solely finetuning the VLM to adapt the VLN task, it only achieves an SR ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** Cross-modal-based methods typically employ a smaller-scale LSTM or Transformer to either train from scratch or pretrain and then fine-tune for the VLN task.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** We perform full fine-tuning on the parameters of the multimodal projector and the Qwen2 [8] LLM backbone.
- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1. Motivation of the proposed method. Previous methods (c) usually employ a two-stage pipeline that uses VLMs to convert visual observations to text for ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2. Overview of the TagaVLM. The pretrained observation encoder and projector encode RGB observations from each node to the semantic space. Textual information containing ...
- **p. 7 / V. CONCLUSIONS - extractive PDF cue:** Future work will build on this strong baseline by scaling training on larger datasets, enriching STAR-Att with more complex geometric priors, and extending our framework ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD), p. 3 (III. METHOD), objective p. 5 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), temporal p. 5 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 2 (I. INTRODUCTION), p. 4 (III. METHOD), p. 4 (III. METHOD).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
