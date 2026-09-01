# Method - LL3DA: Visual Interactive Instruction Tuning for Omni-3D Understanding, Reasoning, and Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2311.18651; PDF retrieval source: https://arxiv.org/pdf/2311.18651. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3.1. Problem Formatting), p. 3 (3.2. Model Design), p. 4 (3.2. Model Design), p. 4 (3.2. Model Design)): 2 (a), the input of our model consists of a 3D scene represented by a set of points PC, the textual instruction It, and potential visual interactions Iv that serve ...

## Method Body Digest

- **p. 3 / 3.1. Problem Formatting - extractive PDF cue:** 2 (a), the input of our model consists of a 3D scene represented by a set of points PC, the textual instruction It, and potential ...
- **p. 3 / 3.2. Model Design - extractive PDF cue:** 2 (b), which consists of a frozen 3D scene encoder E3D, a visual prompt encoder, and a Q-Former to transform the permutation-invariant 3D embeddings into ...
- **p. 4 / 3.2. Model Design - extractive PDF cue:** (1) Here, fenc consists of d-dimensioned features for M points uniformly down-sampled from the input 3D scene through the Farthest Point Sampling (FPS) algorithm.
- **p. 4 / 3.2. Model Design - extractive PDF cue:** We consider the decoder-only generative pre-trained transformers [49, 58] as our large language model backbone, which are sensitive to the input orders because of the ...
- **p. 4 / 3.2. Model Design - extractive PDF cue:** The parameters and the embedding layers of the LLM are kept frozen to save memory cost.
- **p. 4 / 3.2. Model Design - extractive PDF cue:** In practice, we choose to keep the scene encoder frozen to save the memory cost during training.
- **p. 2 / 1. Introduction - extractive PDF cue:** To summarize, our key contributions lie in: • We present a LLM-based solution for understanding, reasoning, and planning in complex 3D environments. • Our model ...
- **p. 3 / 3.2. Model Design - extractive PDF cue:** Next, the aggregated scene embeddings are projected to the prefix of textual instructions as inputs of a frozen LLM.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** To summarize, our key contributions lie in: • We present a LLM-based solution for understanding, reasoning, and planning in complex 3D environments. • Our model ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Additionally, by introducing additional visual interactions, our method could further remove the ambiguities within the vague textual instructions.
- **p. 3 / 3. Methodology - extractive PDF cue:** Next, we introduce our model design in details (Sec.

## Source Evidence Cues

- **p. 3 / 3.1. Problem Formatting - extractive PDF cue:** 2 (a), the input of our model consists of a 3D scene represented by a set of points PC, the textual instruction It, and potential ...
- **p. 3 / 3.2. Model Design - extractive PDF cue:** 2 (b), which consists of a frozen 3D scene encoder E3D, a visual prompt encoder, and a Q-Former to transform the permutation-invariant 3D embeddings into ...
- **p. 4 / 3.2. Model Design - extractive PDF cue:** (1) Here, fenc consists of d-dimensioned features for M points uniformly down-sampled from the input 3D scene through the Farthest Point Sampling (FPS) algorithm.
- **p. 4 / 3.2. Model Design - extractive PDF cue:** We consider the decoder-only generative pre-trained transformers [49, 58] as our large language model backbone, which are sensitive to the input orders because of the ...
- **Detected method headings:** 3. Methodology (p. 3); 3.2. Model Design (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | 2 (a), the input of our model consists of a 3D scene represented by a set of points PC, the textual instruction ... | p. 3 (3.1. Problem Formatting), p. 3 (3.2. Model Design) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | 2 (b), which consists of a frozen 3D scene encoder E3D, a visual prompt encoder, and a Q-Former to transform the permutation-invariant ... | p. 3 (3.2. Model Design), p. 4 (3.2. Model Design) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | (1) Here, fenc consists of d-dimensioned features for M points uniformly down-sampled from the input 3D scene through the Farthest Point Sampling ... | p. 4 (3.2. Model Design), p. 4 (3.2. Model Design) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.2. Model Design - extractive PDF cue:** The parameters and the embedding layers of the LLM are kept frozen to save memory cost.
- **p. 4 / 3.2. Model Design - extractive PDF cue:** In practice, we choose to keep the scene encoder frozen to save the memory cost during training.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3.2. Model Design).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | summarize, contributions, present, LLM-based, solution, understanding, reasoning, planning, complex, environments, model, takes, textual, instructions | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | summarize, contributions, present, LLM-based, solution, understanding, reasoning, planning, complex, environments | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summarize, contributions, present, LLM-based, solution, understanding, reasoning, planning, complex, environments | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | parameters, embedding, layers, LLM, kept, frozen, save, memory, cost, practice | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive PDF cue:** To summarize, our key contributions lie in: • We present a LLM-based solution for understanding, reasoning, and planning in complex 3D environments. • Our model ...
- **p. 3 / 3.1. Problem Formatting - extractive PDF cue:** 2 (a), the input of our model consists of a 3D scene represented by a set of points PC, the textual instruction It, and potential ...
- **p. 3 / 3.2. Model Design - extractive PDF cue:** Next, the aggregated scene embeddings are projected to the prefix of textual instructions as inputs of a frozen LLM.
- **p. 4 / 3.2. Model Design - extractive PDF cue:** E3D, which takes PC as its input, and outputs the 3D scene embeddings: fenc = E3D (PC) = E3D (pin; fin) ∈RM×d.
- **p. 2 / 1. Introduction - extractive PDF cue:** The querying tokens are projected and used as the prefix of the textual instructions, serving as the input to a pre-trained and frozen LLM.
- **p. 4 / 3.2. Model Design - extractive PDF cue:** We consider the decoder-only generative pre-trained transformers [49, 58] as our large language model backbone, which are sensitive to the input orders because of the ...
- **p. 1 / 1. Introduction - extractive PDF cue:** During this LLM carnival, researchers are also seeking generalized LLM solutions to various vision language tasks [16, 54, 59].
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | The parameters and the embedding layers of the LLM are kept frozen to save memory cost. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | In practice, we choose to keep the scene encoder frozen to save the memory cost during training. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | The parameters and the embedding layers of the LLM are kept frozen to save memory cost. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.2. Model Design - extractive PDF cue:** We consider the decoder-only generative pre-trained transformers [49, 58] as our large language model backbone, which are sensitive to the input orders because of the ...
- **p. 5 / 5. Experiments - extractive PDF cue:** For all the training tasks, we train with a total batch size of 16, and evaluate our method every 4k iterations.
- **p. 3 / 3.2. Model Design - extractive PDF cue:** We adopt the masked transformer encoder pre-trained on ScanNet detection [9] as the scene encoder, 3
- **p. 4 / 3.2. Model Design - extractive PDF cue:** In practice, we choose to keep the scene encoder frozen to save the memory cost during training.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** input, model, consists, scene, represented, points, textual, instruction, potential, visual, interactions, serve, supplementary, spatial, identifiers, frozen, encoder, E3D, prompt, Q-Former.
- **Relevant PDF headings:** 3. Methodology (p. 3); 3.2. Model Design (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | In this paper, we experiment with 3D data from ScanNet [15], a 3D dataset covering 1,201 and 312 diverse and complex indoor ... | p. 5 (5. Experiments), p. 5 (5.2. Comparison with SoTA Specialists) |
| Semantic / temporal fusion | The baseline method directly generates the captions given the input 3D scene and visual prompts without any textual instructions. | p. 7 (5.3. Ablation Studies), p. 5 (5.2. Comparison with SoTA Specialists) |
| Robot query / planning handoff | Results show that our method consistently outperforms existing methods on all the evaluation sets, and surpasses the generation based method, 3D-LLM, by ... | p. 5 (5.2. Comparison with SoTA Specialists), p. 7 (5.3. Ablation Studies) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 7. Effectiveness of Instructions on 3D Dense Captioning. We perform experiments on ScanRefer[6]. The baseline method directly generates the captions given the input 3D ...
- **p. 5 / 5.3. Ablation Studies - extractive PDF cue:** In this section, we provide ablation studies on model designs and training strategies.
- **p. 5 / 5. Experiments - extractive PDF cue:** 5.2), and conduct quantitative ablation studies on the model design and training strategy (Sec.
- **p. 6 / 5.3. Ablation Studies - extractive PDF cue:** For fair comparison, we list methods that are trained under the standard per-word cross-entropy loss without additional 3D scenes.
- **p. 7 / 5.3. Ablation Studies - extractive PDF cue:** The listed methods are evaluated without any visual interactions for fair comparison.
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We propose LL3DA, a Large Language 3D Assistant that demonstrates mighty instruction-following capacities of un- derstanding, reasoning, and planning in complex 3D environments. ...
- **p. 6 / 5.3. Ablation Studies - extractive PDF cue:** The results from 3D-LLM∗come from their fine-tuned version.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3.1. Problem Formatting), p. 3 (3.2. Model Design), p. 4 (3.2. Model Design), p. 4 (3.2. Model Design), objective p. 4 (3.2. Model Design), p. 4 (3.2. Model Design), temporal p. 4 (3.2. Model Design), p. 4 (3.2. Model Design), p. 5 (5. Experiments), p. 8 (5.4. Qualitative Results).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
