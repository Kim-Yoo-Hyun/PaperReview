# Method - RoboRefer: Towards Spatial Referring with Reasoning in Vision-Language Models for Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (71 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=OGxalNUHbJ; PDF retrieval source: https://openreview.net/pdf/81387e1e7f5169279b63c293ca88b1e4a8bc7e35.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3 Method), p. 4 (3 Method), p. 4 (3 Method), p. 49 (C Implementation Details and Samples of RefSpatial-Bench), p. 5 (3 Method), p. 50 (C Implementation Details and Samples of RefSpatial-Bench)): Then, we elaborate on RoboRefer, including its architecture and training strategies (Sec.

## Method Body Digest

- **p. 3 / 3 Method - extractive body cue:** Then, we elaborate on RoboRefer, including its architecture and training strategies (Sec.
- **p. 4 / 3 Method - extractive body cue:** 2, RoboRefer employs separate RGB and depth encoders to extract features, which are then aligned via projectors with the LLM for VQA or point prediction.
- **p. 4 / 3 Method - extractive body cue:** To address this, we propose a simple yet effective approach: a dedicated depth encoder and projector, initialized from their RGB counterparts.
- **p. 49 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** D.4.1 Sampling Action Groups Given an input state s = (O, Q), where O denotes the visual encoding of the RGB or RGB-D observation and ...
- **p. 5 / 3 Method - extractive body cue:** Rewards are normalized within each group to compute relative advantages (Ai = ri-mean({rj}) std({rj}) ), which are then used to update the policy, reinforcing high-quality ...
- **p. 50 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** We then update the policy based on these advantages, reinforcing actions with higher relative advantages while reducing the likelihood of those deemed less effective.
- **p. 5 / 3 Method - extractive body cue:** A KL-divergence regularization term stabilizes updates by constraining them near the reference policy.
- **p. 49 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** Unlike PPO [154], which relies on a costly value network, GRPO estimates relative advantages by comparing intra-group rewards, reducing computation, and simplifying optimization.

## Design Rationale

- **p. 3 / 1 Introduction - extractive body cue:** Our contributions are summarized as follows: (1) We propose RoboRefer, a 3D-aware reasoning VLM trained using a sequential SFT-RFT strategy with metric-sensitive process reward functions ...
- **p. 2 / 1 Introduction - extractive body cue:** To advance spatial referring, we introduce RefSpatial, a large-scale dataset of 2.5M high-quality examples with 20M QA pairs (2× prior [3]).
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we propose RoboRefer, a 3D-aware VLM that not only acquires precise spatial understanding via SFT but also exhibits generalized strong reasoning capabilities ...

## Source Evidence Cues

- **p. 3 / 3 Method - extractive body cue:** Then, we elaborate on RoboRefer, including its architecture and training strategies (Sec.
- **p. 4 / 3 Method - extractive body cue:** 2, RoboRefer employs separate RGB and depth encoders to extract features, which are then aligned via projectors with the LLM for VQA or point prediction.
- **p. 4 / 3 Method - extractive body cue:** To address this, we propose a simple yet effective approach: a dedicated depth encoder and projector, initialized from their RGB counterparts.
- **p. 49 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** D.4.1 Sampling Action Groups Given an input state s = (O, Q), where O denotes the visual encoding of the RGB or RGB-D observation and ...
- **p. 5 / 3 Method - extractive body cue:** Rewards are normalized within each group to compute relative advantages (Ai = ri-mean({rj}) std({rj}) ), which are then used to update the policy, reinforcing high-quality ...
- **p. 50 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** We then update the policy based on these advantages, reinforcing actions with higher relative advantages while reducing the likelihood of those deemed less effective.
- **p. 5 / 3 Method - extractive body cue:** A KL-divergence regularization term stabilizes updates by constraining them near the reference policy.
- **Detected method headings:** 3 Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Then, we elaborate on RoboRefer, including its architecture and training strategies (Sec. | p. 3 (3 Method), p. 4 (3 Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | 2, RoboRefer employs separate RGB and depth encoders to extract features, which are then aligned via projectors with the LLM for VQA ... | p. 4 (3 Method), p. 4 (3 Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | To address this, we propose a simple yet effective approach: a dedicated depth encoder and projector, initialized from their RGB counterparts. | p. 4 (3 Method), p. 49 (C Implementation Details and Samples of RefSpatial-Bench) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 49 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** Unlike PPO [154], which relies on a costly value network, GRPO estimates relative advantages by comparing intra-group rewards, reducing computation, and simplifying optimization.
- **p. 48 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** The training objective is to maximize the likelihood of generating the answer given the input pair (Q, A): LSFT = -E(O,Q,A)∼D T X t=1 log ...
- **p. 5 / 3 Method - extractive body cue:** Rewards are normalized within each group to compute relative advantages (Ai = ri-mean({rj}) std({rj}) ), which are then used to update the policy, reinforcing high-quality ...
- **p. 4 / 3 Method - extractive body cue:** 2) becomes more complex as multiple spatial constraints are combined.
- **p. 5 / 3 Method - extractive body cue:** For more details about the RFT training and reward design, please see Appx.
- **p. 20 / B.3.5 Question-Answer Pair Generation - extractive body cue:** 49 D.4.2 Reward Design and Policy Update . . . . . . . . . . . . . . . . . . ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3 Method), p. 5 (3 Method), p. 48 (C Implementation Details and Samples of RefSpatial-Bench), p. 54 (C Implementation Details and Samples of RefSpatial-Bench), p. 57 (C Implementation Details and Samples of RefSpatial-Bench), p. 57 (C Implementation Details and Samples of RefSpatial-Bench).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Sampling, Action, Groups, Given, input, state, where, denotes, visual, encoding, RGB, RGB-D, observation, textual | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Sampling, Action, Groups, Given, input, state, where, denotes, visual, encoding | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, summarized, follows, RoboRefer, D-aware, reasoning, VLM, trained, sequential, SFT-RFT | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Unlike, PPO, relies, costly, value, network, GRPO, estimates, relative, advantages | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 49 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** D.4.1 Sampling Action Groups Given an input state s = (O, Q), where O denotes the visual encoding of the RGB or RGB-D observation and ...
- **p. 4 / 3 Method - extractive body cue:** 3.1 Problem Formulation We formulate spatial referring as predicting a single 2D point (x, y) in image space to specify a target location or destination, ...
- **p. 4 / 3 Method - extractive body cue:** RoboRefer can perform single-step precise spatial understanding from RGB(D) inputs with spatially constrained instructions (enabled by the SFT stage introducing depth modality), and multi-step spatial ...
- **p. 7 / 3 Method - extractive body cue:** Notably, RefSpatial is reused with both RGB and RGB-D inputs in the second step to enforce the image encoder to learn spatial understanding beyond depth ...
- **p. 2 / 1 Introduction - extractive body cue:** Specifically, given sensor observations (e.g., RGB or RGB-D) and a spatially constrained instruction, the spatial referring task aims to predict a precise point that satisfies ...
- **p. 5 / 3 Method - extractive body cue:** Therefore, the model is jointly optimized on RGB and RGB-D inputs, with separate updates for the image and depth encoders.
- **p. 49 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** D.4.2 Reward Design and Policy Update Each sampled action ai is assigned a reward R(ai) based on verifiable criteria, yielding a reward set r1, r2, ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | 6, only our method can handle long-horizon tasks requiring complex multi-step spatial referring in cluttered and dynamic environments. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Reasoning Step = 1 Please point out the black framed painting on the right of the lamp. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | E Experimental Setting and Details E.1 Experiments Compute Resources We conduct experiments on an A100 GPU cluster, with each node equipped with ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3 Method - extractive body cue:** Then, we elaborate on RoboRefer, including its architecture and training strategies (Sec.
- **p. 5 / 3 Method - extractive body cue:** A KL-divergence regularization term stabilizes updates by constraining them near the reference policy.
- **p. 49 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** Training is conducted for two epochs with a batch size of 1 per GPU and 8 outputs in GRPO.
- **p. 48 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** The 2B variant is trained with a batch size of 7 per GPU, and the 8B variant with 3, both for one epoch.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Then, elaborate, RoboRefer, including, architecture, training, strategies, Sec, employs, separate, RGB, depth, encoders, extract, features, aligned, projectors, LLM, VQA, point.
- **Relevant PDF headings:** 3 Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | To evaluate more complex multi-step spatial referring, we propose RefSpatial-Bench, a challenging benchmark based on real-world cluttered scenes. | p. 8 (4 Experiments), p. 9 (4 Experiments) |
| Semantic / temporal fusion | 2, the 2B-RFT variant outperforms all baselines, exceeding the prior SOTA (Gemini-2.5-Pro [9]) by 17.4% (absolute) on RefSpatial-Bench. | p. 8 (4 Experiments), p. 10 (4 Experiments) |
| Robot query / planning handoff | By using a single target point predicted by RoboRefer, the system can generate more accurate masks and corresponding grasp poses than those ... | p. 9 (4 Experiments), p. 8 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 10 / 4 Experiments - extractive body cue:** To assess this, we fine-tune NVILA-2B [38] on RefSpatial without the depth encoder, followed by continued RFT.
- **p. 8 / 4 Experiments - extractive body cue:** Moreover, our 2B variant outperforms NVILA-2B by 21.7% (absolute).
- **p. 8 / 4 Experiments - extractive body cue:** 2, the 2B-RFT variant outperforms all baselines, exceeding the prior SOTA (Gemini-2.5-Pro [9]) by 17.4% (absolute) on RefSpatial-Bench.
- **p. 9 / 4 Experiments - extractive body cue:** These findings indicate that although VLMs often struggle with spatial reasoning, targeted spatial VQA training, especially with combined RGB and RGB-D data enriched by general ...
- **p. 10 / 4 Experiments - extractive body cue:** 4.5 Ablation Study Table 7: Ablation Studies.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Performance on current referring and multi-step spatial referring benchmarks. L. and P. denote our benchmark's Location and Placement parts; U. indicates unseen compositional ...
- **p. 25 / Figure/Table caption - extractive body cue:** Figure 6: Visual overview of the multi-stage filtering results. Row 1: Images discarded by SigLIP2 due to insufficient spatial context (e.g., close-ups, text). Row 2: ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3 Method), p. 4 (3 Method), p. 4 (3 Method), p. 49 (C Implementation Details and Samples of RefSpatial-Bench), p. 5 (3 Method), p. 50 (C Implementation Details and Samples of RefSpatial-Bench), objective p. 49 (C Implementation Details and Samples of RefSpatial-Bench), p. 48 (C Implementation Details and Samples of RefSpatial-Bench), p. 5 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 20 (B.3.5 Question-Answer Pair Generation), temporal p. 9 (4 Experiments), p. 61 (C Implementation Details and Samples of RefSpatial-Bench), p. 4 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
