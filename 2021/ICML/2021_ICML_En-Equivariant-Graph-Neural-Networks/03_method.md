# Method - E(n) Equivariant Graph Neural Networks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2102.09844; PDF retrieval source: https://arxiv.org/pdf/2102.09844. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (5.2. Graph Autoencoder), p. 7 (5.2. Graph Autoencoder), p. 8 (5.2. Graph Autoencoder), p. 6 (5.2. Graph Autoencoder), p. 7 (5.2. Graph Autoencoder), p. 8 (5.2. Graph Autoencoder)): The decoder g(·) proposed by (Liu et al., 2019) takes as input the embedding space z and outputs the reconstructed adjacency matrix ˆA = g(z), this decoder function is defined ...

## Method Body Digest

- **p. 6 / 5.2. Graph Autoencoder - extractive body cue:** The decoder g(·) proposed by (Liu et al., 2019) takes as input the embedding space z and outputs the reconstructed adjacency matrix ˆA = g(z), ...
- **p. 7 / 5.2. Graph Autoencoder - extractive body cue:** Implementation details: Our Equivariant Graph AutoEncoder is composed of an EGNN encoder followed by the decoder from Equation 9.
- **p. 8 / 5.2. Graph Autoencoder - extractive body cue:** Our EGNN network consists of 7 layers, 128 features per hidden layer and the Swish activation function as a non-linearity.
- **p. 6 / 5.2. Graph Autoencoder - extractive body cue:** The symmetry problem: The above stated autoencoder may seem straightforward to implement at first sight but in some cases there is a strong limitation regarding ...
- **p. 7 / 5.2. Graph Autoencoder - extractive body cue:** As mentioned before, the encoder outputs an equivariant transformation on the coordinates which is the graph embedding and input to the decoder z = xL ...
- **p. 8 / 5.2. Graph Autoencoder - extractive body cue:** Additionally, since we are not provided with an adjacency matrix and molecules can scale up to 29 nodes, we use the extension of our model ...
- **p. 6 / 5.2. Graph Autoencoder - extractive body cue:** The training loss is defined as the binary cross entropy between the estimated and the ground truth edges L = P ij BCE( ˆAij, Aij).
- **p. 8 / 5.2. Graph Autoencoder - extractive body cue:** Since this is an invariant task and also x0 positions are static, there is no need to update the particle's position x by running Equation ...

## Design Rationale

- **p. 2 / 2. Background - extractive body cue:** In this section we introduce the relevant materials on equivariance and graph neural networks which will later complement the definition of our method.
- **p. 1 / 1. Introduction - extractive body cue:** In this work we present a new architecture that is translation, rotation and reflection equivariant (E(n)), and permutation equivariant with respect to an input set ...
- **p. 2 / 1. Introduction - extractive body cue:** Our method reports the best or very competitive performance in all three experiments.

## Source Evidence Cues

- **p. 6 / 5.2. Graph Autoencoder - extractive body cue:** The decoder g(·) proposed by (Liu et al., 2019) takes as input the embedding space z and outputs the reconstructed adjacency matrix ˆA = g(z), ...
- **p. 7 / 5.2. Graph Autoencoder - extractive body cue:** Implementation details: Our Equivariant Graph AutoEncoder is composed of an EGNN encoder followed by the decoder from Equation 9.
- **p. 8 / 5.2. Graph Autoencoder - extractive body cue:** Our EGNN network consists of 7 layers, 128 features per hidden layer and the Swish activation function as a non-linearity.
- **p. 6 / 5.2. Graph Autoencoder - extractive body cue:** The symmetry problem: The above stated autoencoder may seem straightforward to implement at first sight but in some cases there is a strong limitation regarding ...
- **p. 7 / 5.2. Graph Autoencoder - extractive body cue:** As mentioned before, the encoder outputs an equivariant transformation on the coordinates which is the graph embedding and input to the decoder z = xL ...
- **p. 8 / 5.2. Graph Autoencoder - extractive body cue:** Additionally, since we are not provided with an adjacency matrix and molecules can scale up to 29 nodes, we use the extension of our model ...
- **Detected method headings:** 5.1. Modelling a dynamical system - N-body system (p. 5); 2. Our method outperforms both Radial Field and GNNs (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | The decoder g(·) proposed by (Liu et al., 2019) takes as input the embedding space z and outputs the reconstructed adjacency matrix ... | p. 6 (5.2. Graph Autoencoder), p. 7 (5.2. Graph Autoencoder) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Implementation details: Our Equivariant Graph AutoEncoder is composed of an EGNN encoder followed by the decoder from Equation 9. | p. 7 (5.2. Graph Autoencoder), p. 8 (5.2. Graph Autoencoder) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Our EGNN network consists of 7 layers, 128 features per hidden layer and the Swish activation function as a non-linearity. | p. 8 (5.2. Graph Autoencoder), p. 6 (5.2. Graph Autoencoder) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 5.2. Graph Autoencoder - extractive body cue:** The training loss is defined as the binary cross entropy between the estimated and the ground truth edges L = P ij BCE( ˆAij, Aij).
- **p. 8 / 5.2. Graph Autoencoder - extractive body cue:** Since this is an invariant task and also x0 positions are static, there is no need to update the particle's position x by running Equation ...
- **p. 7 / 5.2. Graph Autoencoder - extractive body cue:** The graph edges Aij are input as edge attributes aij in Equation 3.
- **p. 7 / 5.2. Graph Autoencoder - extractive body cue:** Implementation details: Our Equivariant Graph AutoEncoder is composed of an EGNN encoder followed by the decoder from Equation 9.
- **p. 8 / 5.2. Graph Autoencoder - extractive body cue:** Implementation details: Our EGNN receives as input the 3D coordinate locations of each atom which are provided as x0 i in Equation 3 and an ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 8 (5.2. Graph Autoencoder), p. 6 (5.2. Graph Autoencoder), p. 7 (5.2. Graph Autoencoder), p. 7 (5.2. Graph Autoencoder), p. 8 (5.2. Graph Autoencoder).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | decoder, Liu, takes, input, embedding, space, outputs, reconstructed, adjacency, matrix, function, defined, follows, Aij | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | decoder, Liu, takes, input, embedding, space, outputs, reconstructed, adjacency, matrix | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | section, introduce, relevant, materials, equivariance, graph, neural, networks, will, later | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | training, loss, defined, binary, cross, entropy, between, estimated, ground, truth | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 5.2. Graph Autoencoder - extractive body cue:** The decoder g(·) proposed by (Liu et al., 2019) takes as input the embedding space z and outputs the reconstructed adjacency matrix ˆA = g(z), ...
- **p. 2 / 2.1. Equivariance - extractive body cue:** We say a function φ : X -→Y is equivariant to g if there exists an equivalent transformation on its output space Sg : Y ...
- **p. 1 / 1. Introduction - extractive body cue:** Additionally, in practice for many types of data the inputs and outputs are restricted to scalar values (for instance temperature or energy, referred to as ...
- **p. 7 / 5.2. Graph Autoencoder - extractive body cue:** As mentioned before, the encoder outputs an equivariant transformation on the coordinates which is the graph embedding and input to the decoder z = xL ...
- **p. 7 / 5.2. Graph Autoencoder - extractive body cue:** In our case we will simply input this noise as the input coordinates x0 ∼N(0, σI) ∈RM×n of our EGNN which will output an equivariant ...
- **p. 2 / 2.1. Equivariance - extractive body cue:** If our transformation φ : X -→Y is translation equivariant, translating the input set Tg(x) and then applying the function φ(Tx(x)) on it, will deliver ...
- **p. 6 / 5.2. Graph Autoencoder - extractive body cue:** This method introduces noise sampled from a Gaussian distribution into the input node features of the graph h0 i ∼N(0, σI).
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Each trajectory has a duration of 1.000 timesteps. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The task is to estimate the positions of the five particles after 1.000 timesteps. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | Notice this may reduce the memory complexity to store the graphs from O(M 2) to O(Mn) where n may depend on M ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | All algorithms are composed of 4 layers and have been trained under the same conditions, batch size 100, 10.000 epochs, Adam optimizer, ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 5.1. Modelling a dynamical system - N-body system - extractive body cue:** All algorithms are composed of 4 layers and have been trained under the same conditions, batch size 100, 10.000 epochs, Adam optimizer, the learning rate ...
- **p. 7 / 5.2. Graph Autoencoder - extractive body cue:** All four models have 4 layers, 64 features for the hidden layers, the Swish activation function as a non-linearity and they were all trained for ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** decoder, Liu, takes, input, embedding, space, outputs, reconstructed, adjacency, matrix, function, defined, follows, Aij, Where, only, learnable, parameters, edge, applied.
- **Relevant PDF headings:** 5.1. Modelling a dynamical system - N-body system (p. 5); 2. Our method outperforms both Radial Field and GNNs (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Dataset: We sampled 3.000 trajectories for training, 2.000 for validation and 2.000 for testing. | p. 5 (5.1. Modelling a dynamical system - N-body system), p. 5 (5.1. Modelling a dynamical system - N-body system) |
| Semantic / temporal fusion | A Linear model that simply considers the motion equation p(t) = p(0) + v(0)t is also included as a baseline. | p. 5 (5.1. Modelling a dynamical system - N-body system), p. 5 (5.1. Modelling a dynamical system - N-body system) |
| Robot query / planning handoff | Results As shown in Table 2 our model significantly outperforms the other equivariant and non-equivariant alternatives while still being efficient in terms ... | p. 5 (5.1. Modelling a dynamical system - N-body system), p. 15 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 3 / 3.1. Analysis on E(n) equivariance - extractive body cue:** Inductively, a composition of EGCLs will also be equivariant.
- **p. 3 / 3.1. Analysis on E(n) equivariance - extractive body cue:** Therefore the output hl+1 is E(n) invariant and xl+1 is E(n) equivariant to xl.
- **p. 5 / 5.1. Modelling a dynamical system - N-body system - extractive body cue:** This is an equivariant task since rotations and translations on the input set of particles result in the same transformations throughout the entire trajectory.
- **p. 5 / 5.1. Modelling a dynamical system - N-body system - extractive body cue:** Results As shown in Table 2 our model significantly outperforms the other equivariant and non-equivariant alternatives while still being efficient in terms of running time.
- **p. 6 / 5.1. Modelling a dynamical system - N-body system - extractive body cue:** We compare the performances of our EGNN vs its non-equivariant GNN counterpart and the Radial Field algorithm.
- **p. 6 / 5.1. Modelling a dynamical system - N-body system - extractive body cue:** E(n) Equivariant Graph Neural Networks 50.000 samples and we sweep over different amounts of data from 100 to 50.000 samples.
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1. Comparison over different works from the literature under the message passing framework notation. We created this table with the aim to provide a ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (5.2. Graph Autoencoder), p. 7 (5.2. Graph Autoencoder), p. 8 (5.2. Graph Autoencoder), p. 6 (5.2. Graph Autoencoder), p. 7 (5.2. Graph Autoencoder), p. 8 (5.2. Graph Autoencoder), objective p. 6 (5.2. Graph Autoencoder), p. 8 (5.2. Graph Autoencoder), p. 7 (5.2. Graph Autoencoder), p. 7 (5.2. Graph Autoencoder), p. 8 (5.2. Graph Autoencoder), temporal p. 5 (5.1. Modelling a dynamical system - N-body system), p. 5 (5.1. Modelling a dynamical system - N-body system), p. 6 (5.2. Graph Autoencoder), p. 8 (5.2. Graph Autoencoder), p. 3 (3.2. Extending EGNNs for vector type representations), p. 3 (3. Equivariant Graph Neural Networks).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
