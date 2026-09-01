# Method - Flow Equivariant World Models: Structured Memory for Dynamic Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=jgqFnXEDGG; PDF retrieval source: https://openreview.net/pdf/25b19208166528c9c48b16cdd741d730218a8089.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3.1. Generalized Flow Equivariance), p. 4 (3.1. Generalized Flow Equivariance), p. 2 (3.1. Generalized Flow Equivariance), p. 3 (3.1. Generalized Flow Equivariance), p. 3 (3.1. Generalized Flow Equivariance), p. 5 (3.1. Generalized Flow Equivariance)): The latent map ht is fully learned, visualized as a map here for clarity. b) The update writes to the memory tokens at the correct FoV locations, then transforms the ...

## Method Body Digest

- **p. 5 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** The latent map ht is fully learned, visualized as a map here for clarity. b) The update writes to the memory tokens at the correct ...
- **p. 4 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** In detail, given the action variable at, denoting the action of the agent between times t and t+1, we transform the hidden state of the ...
- **p. 2 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** A sequence-to-sequence model Φ defines a map f 7→h for outputs h = {ht}T t=0, ht : X′ →RK′, such as mapping from an input ...
- **p. 3 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** To support more complex tasks, such as 3D partially observed world modeling, we introduce an abstract version of the flow equivariant recurrence relation which supports ...
- **p. 3 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** In practice, this means that we must now define the output of Φ to be equivariant with respect to the full world state, implying that ...
- **p. 5 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** In this setting, the recurrent state ht is a set of spatially organized token embeddings that act as a structured latent map of the 3D ...
- **p. 4 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** When the action space is more sophisticated, such as involving rotations in 3D environments, the representation acts directly on the spatial dimensions and velocity channels ...
- **p. 5 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** The simple addition is indeed equivariant with respect to linear transformations of its inputs, satisfying Equation 6.

## Design Rationale

- **p. 1 / 1. Introduction - extractive PDF cue:** As embodied agents in a dynamic world, our survival critically depends on our ability to accurately model our surrounding environment, our own self-motion through it, ...
- **p. 3 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** To support more complex tasks, such as 3D partially observed world modeling, we introduce an abstract version of the flow equivariant recurrence relation which supports ...
- **p. 4 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** Finally, to complete our framework, we note that motion is relative (i.e. self-motion of an agent is equivalent to global motion of the input).

## Source Evidence Cues

- **p. 5 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** The latent map ht is fully learned, visualized as a map here for clarity. b) The update writes to the memory tokens at the correct ...
- **p. 4 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** In detail, given the action variable at, denoting the action of the agent between times t and t+1, we transform the hidden state of the ...
- **p. 2 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** A sequence-to-sequence model Φ defines a map f 7→h for outputs h = {ht}T t=0, ht : X′ →RK′, such as mapping from an input ...
- **p. 3 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** To support more complex tasks, such as 3D partially observed world modeling, we introduce an abstract version of the flow equivariant recurrence relation which supports ...
- **p. 3 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** In practice, this means that we must now define the output of Φ to be equivariant with respect to the full world state, implying that ...
- **p. 5 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** In this setting, the recurrent state ht is a set of spatially organized token embeddings that act as a structured latent map of the 3D ...
- **p. 4 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** When the action space is more sophisticated, such as involving rotations in 3D environments, the representation acts directly on the spatial dimensions and velocity channels ...
- **Detected method headings:** 3. Flow Equivariant World Models (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | The latent map ht is fully learned, visualized as a map here for clarity. b) The update writes to the memory tokens ... | p. 5 (3.1. Generalized Flow Equivariance), p. 4 (3.1. Generalized Flow Equivariance) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | In detail, given the action variable at, denoting the action of the agent between times t and t+1, we transform the hidden ... | p. 4 (3.1. Generalized Flow Equivariance), p. 2 (3.1. Generalized Flow Equivariance) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | A sequence-to-sequence model Φ defines a map f 7→h for outputs h = {ht}T t=0, ht : X′ →RK′, such as mapping ... | p. 2 (3.1. Generalized Flow Equivariance), p. 3 (3.1. Generalized Flow Equivariance) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** The simple addition is indeed equivariant with respect to linear transformations of its inputs, satisfying Equation 6.
- **p. 5 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** In order to satisfy Equation 5 formally, Eθ must be equivariant with respect to motion of the agent and external objects and perform a ‘trivial-lift' ...
- **p. 3 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** To support more complex tasks, such as 3D partially observed world modeling, we introduce an abstract version of the flow equivariant recurrence relation which supports ...
- **p. 3 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** Specifically, we define our abstract observation encoder as Eθ[ft; ht], a function of the current observation ft and the prior hidden state ht; and we ...
- **p. 4 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** (4) To prove that this is indeed still flow equivariant, both the encoder and update operations are required to be equivariant with respect to transformations ...
- **p. 4 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** In detail, given the action variable at, denoting the action of the agent between times t and t+1, we transform the hidden state of the ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.1. Generalized Flow Equivariance), p. 5 (3.1. Generalized Flow Equivariance), p. 3 (3.1. Generalized Flow Equivariance), p. 3 (3.1. Generalized Flow Equivariance), p. 4 (3.1. Generalized Flow Equivariance), p. 4 (3.1. Generalized Flow Equivariance).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | sequence-to-sequence, model, defines, outputs, mapping, input, video, sequence, hidden, states, said, flow, equivariant, when | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | sequence-to-sequence, model, defines, outputs, mapping, input, video, sequence, hidden, states | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | embodied, agents, dynamic, world, survival, critically, depends, ability, accurately, model | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | simple, addition, indeed, equivariant, respect, linear, transformations, inputs, satisfying, Equation | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** A sequence-to-sequence model Φ defines a map f 7→h for outputs h = {ht}T t=0, ht : X′ →RK′, such as mapping from an input ...
- **p. 3 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** In practice, this means that we must now define the output of Φ to be equivariant with respect to the full world state, implying that ...
- **p. 3 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** Because the elements of the Lie algebra combine in a structured manner, it is then possible to show that when the input sequence is acted ...
- **p. 4 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** Explicitly: ht+1(ν) = ψ1(ν -at)·σ  W ⋆ht(ν)+pad(U ⋆ft)  , (8) where W ⋆ht, and U ⋆ft denote convolutions over the hidden state and spatial ...
- **p. 4 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** In detail, given the action variable at, denoting the action of the agent between times t and t+1, we transform the hidden state of the ...
- **p. 5 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** The latent map ht is fully learned, visualized as a map here for clarity. b) The update writes to the memory tokens at the correct ...
- **p. 5 / 3.1. Generalized Flow Equivariance - extractive PDF cue:** In particular, the hidden state is windowed at each timestep, pixel-wise max-pooled over ‘velocity channels' and passed through a decoder gθ to predict the next ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | The average prediction error per frame is plotted in Figure 6, demonstrating FloWM's consistent rollouts through long horizons. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | FloWM stays consistent until the final frame, while the baselines and ablations hallucinate object position and color. b) Corresponding averaged MSE per ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | In this work, we introduce Flow Equivariant World Modeling, a framework that leverages time-parameterized symmetries within a latent memory for stable and ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 4.2. 2D MNIST World Benchmark - extractive PDF cue:** To test length generalization, we additionally run inference up to 150 prediction frames.
- **p. 7 / 4.2. 2D MNIST World Benchmark - extractive PDF cue:** We further find that models combining SME and VC require orders of magnitude less training steps to converge compared with those without these priors, shown ...
- **p. 7 / 4.2. 2D MNIST World Benchmark - extractive PDF cue:** Predictions from FloWM remain consistent with ground truth for 150 timesteps past the observation window, well beyond its training prediction horizon of 20 timesteps, while ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** latent, fully, learned, visualized, here, clarity, update, writes, memory, tokens, correct, FoV, locations, then, transforms, according, known, action, internal, flow.
- **Relevant PDF headings:** 3. Flow Equivariant World Models (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | To validate FloWM on this more difficult setting, we further introduce a simple 3D dataset, built in the Miniworld environment (Chevalier-Boisvert et ... | p. 7 (4.3. 3D Dynamic Block World Benchmark), p. 8 (4.3. 3D Dynamic Block World Benchmark) |
| Semantic / temporal fusion | We also include ablations FloWM (no VC), FloWM (no VC, no SME), and the diffusion baselines mentioned above. | p. 7 (4.2. 2D MNIST World Benchmark), p. 7 (4.3. 3D Dynamic Block World Benchmark) |
| Robot query / planning handoff | Comparatively, the DFoT model achieves an equivariance error of 2.36. | p. 8 (4.3. 3D Dynamic Block World Benchmark), p. 23 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 6. Flow Equivariant World Models accurately predict moving objects in a 3D environment over long time-spans. a) Visualization of rollout (after 50 observation frames). ...
- **p. 6 / 4.2. 2D MNIST World Benchmark - extractive PDF cue:** We include ablations on data subsets with different combinations of partial observability, presence of object dynamics, and self-motion in §F.
- **p. 7 / 4.2. 2D MNIST World Benchmark - extractive PDF cue:** Flow Equivariant World Models: Structured Memory for Dynamic Environments Figure 6.
- **p. 8 / 4.3. 3D Dynamic Block World Benchmark - extractive PDF cue:** Learned Equivariant Representation.
- **p. 8 / 4.3. 3D Dynamic Block World Benchmark - extractive PDF cue:** Finally, we then leverage these probes to quantitatively test one core assumption made in constructing the 3D FloWM model - that the FloWM ViT Encoder ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 5. FloWM generalizes further and trains faster. a) Timesteps 0 to 49 are given as observations. Models are trained to predict up to t ...
- **p. 24 / Figure/Table caption - extractive PDF cue:** Table 7. MNIST world data subsets demonstrating scaling difficulty in self-motion, dynamics, and partial observability. Here, we describe dataset generation and parameter settings for our ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3.1. Generalized Flow Equivariance), p. 4 (3.1. Generalized Flow Equivariance), p. 2 (3.1. Generalized Flow Equivariance), p. 3 (3.1. Generalized Flow Equivariance), p. 3 (3.1. Generalized Flow Equivariance), p. 5 (3.1. Generalized Flow Equivariance), objective p. 5 (3.1. Generalized Flow Equivariance), p. 5 (3.1. Generalized Flow Equivariance), p. 3 (3.1. Generalized Flow Equivariance), p. 3 (3.1. Generalized Flow Equivariance), p. 4 (3.1. Generalized Flow Equivariance), p. 4 (3.1. Generalized Flow Equivariance), temporal p. 7 (4.3. 3D Dynamic Block World Benchmark), p. 7 (4.2. 2D MNIST World Benchmark), p. 8 (4.3. 3D Dynamic Block World Benchmark), p. 1 (Abstract), p. 2 (3.1. Generalized Flow Equivariance), p. 2 (2. Background).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
