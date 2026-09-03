# Flow Equivariant World Models: Structured Memory for Dynamic Environments

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=jgqFnXEDGG.
> PDF retrieval source: https://openreview.net/pdf/25b19208166528c9c48b16cdd741d730218a8089.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: equivariant, 3D Vision
- Official paper: https://openreview.net/forum?id=jgqFnXEDGG
- Full-text retrieval: https://openreview.net/pdf/25b19208166528c9c48b16cdd741d730218a8089.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 While these models achieve impressive perceptual quality and scale well with growing data and compute, their current form inherently lacks the ability to predict long-horizon dynamics, especially in partially observable environments (Fi ...를 문제로 두고, To support more complex tasks, such as 3D partially observed world modeling, we introduce an abstract version of the flow equivariant recurrence relation which supports arbitrary encoders and update operations.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Embodied systems experience the world as ‘a symphony of flows': a combination of many continuous streams of sensory input coupled to selfmotion, interwoven with the ...
- **p. 1 / Abstract - extractive body cue:** These sensory streams and the underlying dynamics of the world obey smooth, timeparameterized symmetries which existing world models ignore.
- **p. 1 / Abstract - extractive body cue:** Without a memory that respects this structure, partial observability presents a major obstacle to existing methods: each observation reveals only a fraction of the world, ...
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce Flow Equivariant World Modeling, a framework that leverages time-parameterized symmetries within a latent memory for stable and accurate dynamics prediction ...
- **p. 1 / Abstract - extractive body cue:** The latent memory shifts and transforms equivariantly with self-motion and inferred external object motion, keeping information about out-of-view regions aligned as time progresses.
- **p. 2 / 2. Background - extractive body cue:** While these models achieve impressive perceptual quality and scale well with growing data and compute, their current form inherently lacks the ability to predict long-horizon ...
- **p. 2 / 2. Background - extractive body cue:** This limitation necessitates a form of memory in order to represent and integrate partial information through time.

## Core Idea

- **p. 3 / 3.1. Generalized Flow Equivariance - extractive body cue:** To support more complex tasks, such as 3D partially observed world modeling, we introduce an abstract version of the flow equivariant recurrence relation which supports ...
- **p. 4 / 3.1. Generalized Flow Equivariance - extractive body cue:** Finally, to complete our framework, we note that motion is relative (i.e. self-motion of an agent is equivalent to global motion of the input).
- **p. 4 / 3.1. Generalized Flow Equivariance - extractive body cue:** For the first set of experiments, to validate our framework in a 2D environment, we construct a recurrent model with self-motion and flow equivariance following ...
- **p. 5 / 3.1. Generalized Flow Equivariance - extractive body cue:** To extend our framework to more complex datasets, we construct a second FloWM instantiation with a Vision Transformer (ViT) (Dosovitskiy et al., 2021) encoder and ...
- **p. 2 / 1. Introduction - extractive body cue:** We show that this yields substantially improved video world modeling performance and generalization to significantly longer sequences than those seen during training, highlighting the benefits ...
- **p. 5 / 3.1. Generalized Flow Equivariance - extractive body cue:** The latent map ht is fully learned, visualized as a map here for clarity. b) The update writes to the memory tokens at the correct ...
- **p. 4 / 3.1. Generalized Flow Equivariance - extractive body cue:** In detail, given the action variable at, denoting the action of the agent between times t and t+1, we transform the hidden state of the ...
- **p. 2 / 3.1. Generalized Flow Equivariance - extractive body cue:** A sequence-to-sequence model Φ defines a map f 7→h for outputs h = {ht}T t=0, ht : X′ →RK′, such as mapping from an input ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | A sequence-to-sequence model Φ defines a map f 7→h for outputs h = {ht}T t=0, ht : X′ →RK′, such as mapping from an input video to a sequence of hidden states. ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (3.1. Generalized Flow Equivariance), p. 3 (3.1. Generalized Flow Equivariance) |
| State/latent | sequence-to-sequence, model, defines, outputs, mapping, input, video, sequence, hidden, states, said, flow | geometry, map, object/relationship state | p. 2 (3.1. Generalized Flow Equivariance), p. 3 (3.1. Generalized Flow Equivariance), p. 3 (3.1. Generalized Flow Equivariance) |
| Output/action | In practice, this means that we must now define the output of Φ to be equivariant with respect to the full world state, implying that the latent representation is structured to encode ... | point map, pose, scene graph, affordance 또는 query result | p. 3 (3.1. Generalized Flow Equivariance), p. 3 (3.1. Generalized Flow Equivariance), p. 4 (3.1. Generalized Flow Equivariance) |
| Objective/outcome | The simple addition is indeed equivariant with respect to linear transformations of its inputs, satisfying Equation 6. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.1. Generalized Flow Equivariance), p. 5 (3.1. Generalized Flow Equivariance), p. 3 (3.1. Generalized Flow Equivariance) |

## Main Claims and Actual Contribution

- **p. 3 / 3.1. Generalized Flow Equivariance - extractive body cue:** To support more complex tasks, such as 3D partially observed world modeling, we introduce an abstract version of the flow equivariant recurrence relation which supports ...
- **p. 4 / 3.1. Generalized Flow Equivariance - extractive body cue:** Finally, to complete our framework, we note that motion is relative (i.e. self-motion of an agent is equivalent to global motion of the input).
- **p. 4 / 3.1. Generalized Flow Equivariance - extractive body cue:** For the first set of experiments, to validate our framework in a 2D environment, we construct a recurrent model with self-motion and flow equivariance following ...
- **p. 5 / 3.1. Generalized Flow Equivariance - extractive body cue:** To extend our framework to more complex datasets, we construct a second FloWM instantiation with a Vision Transformer (ViT) (Dosovitskiy et al., 2021) encoder and ...
- **p. 2 / 1. Introduction - extractive body cue:** We show that this yields substantially improved video world modeling performance and generalization to significantly longer sequences than those seen during training, highlighting the benefits ...
- **p. 8 / 4.3. 3D Dynamic Block World Benchmark - extractive body cue:** Comparatively, the DFoT model achieves an equivariance error of 2.36.
- **p. 23 / Figure/Table caption - extractive body cue:** Table 6. As with the static MNIST World dataset, in this setting, the default configuration of FloWM with velocity channels only adds noise to the ...
- **p. 6 / 4. Experiments - extractive body cue:** Our results demonstrate that the structured dynamic memory afforded by flow equivariance is critical for modeling partially observed dynamic environments.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4.3. 3D Dynamic Block World Benchmark), p. 23 (Figure/Table caption) |
| Embodiment/environment | To validate FloWM on this more difficult setting, we further introduce a simple 3D dataset, built in the Miniworld environment (Chevalier-Boisvert et al., 2023). | hardware/simulator version and reset protocol | p. 7 (4.3. 3D Dynamic Block World Benchmark), p. 8 (4.3. 3D Dynamic Block World Benchmark) |
| Dataset/benchmark | To test our architecture on partially observable dynamic world modeling, we propose a simple MNIST World dataset. | role, split, size and leakage | p. 7 (4.3. 3D Dynamic Block World Benchmark), p. 8 (4.3. 3D Dynamic Block World Benchmark), p. 6 (4.2. 2D MNIST World Benchmark), p. 6 (4.1. Diffusion-based and Recurrent Baselines) |
| Metric | We find that before training, the FloWM has an equivariance error of 6.96 (in L2 distance) meaning the original predictions are off by roughly 5 units in both the spatial directions ( ... | definition, denominator, direction and uncertainty | p. 8 (4.3. 3D Dynamic Block World Benchmark), p. 8 (4.3. 3D Dynamic Block World Benchmark), p. 7 (4.2. 2D MNIST World Benchmark) |
| Baseline/ablation | We also include ablations FloWM (no VC), FloWM (no VC, no SME), and the diffusion baselines mentioned above. | fair input/data/compute/action matching | p. 7 (4.2. 2D MNIST World Benchmark), p. 7 (4.3. 3D Dynamic Block World Benchmark), p. 6 (4.1. Diffusion-based and Recurrent Baselines) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 6. Discussion - extractive body cue:** Similarly, future work may extend FloWM beyond the current discrete velocity sets V to continuous families; however prior empirical and theoretical results suggest that even ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Existing world model memory is inherently limited in partially observed dynamic environments. a) Standard autoregressive video diffusion evicts frames beyond the sliding window. ...
- **p. 7 / 4.2. 2D MNIST World Benchmark - extractive body cue:** Predictions from FloWM remain consistent with ground truth for 150 timesteps past the observation window, well beyond its training prediction horizon of 20 timesteps, while ...
- **p. 6 / 4.1. Diffusion-based and Recurrent Baselines - extractive body cue:** During inference, DFoT maintains a sliding window composed of context and prediction frames at different noise levels; after denoising is complete on one chunk, the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. FloWM generalizes further and trains faster. a) Timesteps 0 to 49 are given as observations. Models are trained to predict up to t ...
- **p. 7 / 4.3. 3D Dynamic Block World Benchmark - extractive body cue:** Perceptually, the DFoT and SSM models frequently hallucinate new objects and forget old ones, while the RSSM model degrades to a blurry average of many ...
- **p. 23 / Figure/Table caption - extractive body cue:** Table 6. As with the static MNIST World dataset, in this setting, the default configuration of FloWM with velocity channels only adds noise to the ...

## Why Read It

World models, safety, uncertainty, and recovery의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 While these models achieve impressive perceptual quality and scale well with growing data and compute, their current form inherently lacks the ability to predict long-horizon dynamics, especially in partially observable environments (Fi ...를 문제로 두고, To support more complex tasks, such as 3D partially observed world modeling, we introduce an abstract version of the flow equivariant recurrence relation which supports arbitrary encoders and update operations.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (2. Background), p. 2 (2. Background), p. 1 (1. Introduction), p. 5 (3.1. Generalized Flow Equivariance), p. 4 (3.1. Generalized Flow Equivariance), p. 2 (3.1. Generalized Flow Equivariance) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
