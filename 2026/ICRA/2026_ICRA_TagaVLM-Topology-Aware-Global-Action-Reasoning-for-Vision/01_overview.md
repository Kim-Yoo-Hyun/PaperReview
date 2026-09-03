# TagaVLM: Topology-Aware Global Action Reasoning for Vision-Language Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_5.html.
> PDF retrieval source: https://arxiv.org/pdf/2603.02972. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Vision-Language Model, Navigation
- Official paper: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_5.html
- Full-text retrieval: https://arxiv.org/pdf/2603.02972
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, these methods ignore the gap between disembodied knowledge of pretrained VLMs and the embodied property of the VLN task, requiring the model to understand implicit visual-topological alignment passively and therefore increasing ...를 문제로 두고, Our contribution can be summarized as follows: • We introduce TagaVLM, an end-to-end VLN framework that architecturally embeds topological structures into the VLM backbone. • We propose two synergistic components: the INP ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language Navigation (VLN) presents a unique challenge for Large Vision-Language Models (VLMs) due to their inherent architectural mismatch: VLMs are primarily pretrained on static, disembodied ...
- **p. 1 / Abstract - extractive body cue:** Existing largemodel-based methods often resort to converting rich visual and spatial information into text, forcing models to implicitly infer complex visual-topological relationships or limiting their ...
- **p. 1 / Abstract - extractive body cue:** To bridge this gap, we propose TagaVLM (Topology-Aware Global Action reasoning), an endto-end framework that explicitly injects topological structures into the VLM backbone.
- **p. 1 / Abstract - extractive body cue:** To introduce topological edge information, Spatial Topology Aware Residual Attention (STAR-Att) directly integrates it into the VLM's self-attention mechanism, enabling intrinsic spatial reasoning while preserving ...
- **p. 1 / Abstract - extractive body cue:** To enhance topological node information, an Interleaved Navigation Prompt strengthens node-level visual-text alignment.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, these methods ignore the gap between disembodied knowledge of pretrained VLMs and the embodied property of the VLN task, requiring the model to understand ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, the visionto-text conversion and two-stage pipeline cannot sufficiently preserve and digest fine-grained visual information [15].

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our contribution can be summarized as follows: • We introduce TagaVLM, an end-to-end VLN framework that architecturally embeds topological structures into the VLM backbone. • ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Instead, other methods usually act on local space, which only consists of local navigable viewpoints directly connected to the current viewpoint.
- **p. 3 / III. METHOD - extractive body cue:** In the following subsections, we will elaborate on the four key components of our framework: (1) online topological map for global environment representation, (2) Interleaved ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Second, it memorizes a global action space and enables the model to backtrack once an error occurs.
- **p. 5 / III. METHOD - extractive body cue:** This global action space enables the model to perform global target selection.
- **p. 4 / III. METHOD - extractive body cue:** Given Gt and the stored visual representations of each node Vt = {vt i}Kt i=1, an effective pretrained Vision Transformer (ViT) [37] is employed as ...
- **p. 4 / III. METHOD - extractive body cue:** (1) This approach ensures that the visual features of each node contextually correspond to the node IDs and node types within the prompt, thereby strengthening ...
- **p. 5 / III. METHOD - extractive body cue:** 4, with the global action reasoning ability, the proposed model is able to efficiently correct the decision error in the first navigation step.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Then, this matrix is fed into the proposed STAR-Att, together with the input prompt Pt to get the output features ˜Pt. | camera/depth stream, pose, map와 language goal | p. 5 (III. METHOD), p. 1 (I. INTRODUCTION) |
| State/latent | Then, matrix, STAR-Att, together, input, prompt, output, features, Observation/Map, text, format, RGB | robot pose, free-space/semantic map와 local goal | p. 5 (III. METHOD), p. 1 (I. INTRODUCTION), p. 5 (III. METHOD) |
| Output/action | Observation/Map In text format RGB Observation RGB Observation Global/Local Action Global Action Topology information LLM (c) Other Methods TagaVLM STAR-Att STAR-Att STAR-Att (b) Our TagaVLM 3 2 1 4 5 6 7 ... | collision-free trajectory 또는 velocity command | p. 1 (I. INTRODUCTION), p. 5 (III. METHOD), p. 2 (I. INTRODUCTION) |
| Objective/outcome | The training is conducted entirely in a teacher-forcing manner, where cross-entropy loss is computed between the predicted node index and the ground truth. | goal reach, safety, localization error와 replanning latency | p. 5 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our contribution can be summarized as follows: • We introduce TagaVLM, an end-to-end VLN framework that architecturally embeds topological structures into the VLM backbone. • ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Instead, other methods usually act on local space, which only consists of local navigable viewpoints directly connected to the current viewpoint.
- **p. 3 / III. METHOD - extractive body cue:** In the following subsections, we will elaborate on the four key components of our framework: (1) online topological map for global environment representation, (2) Interleaved ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Second, it memorizes a global action space and enables the model to backtrack once an error occurs.
- **p. 5 / III. METHOD - extractive body cue:** This global action space enables the model to perform global target selection.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** It is worth noting that, our 0.5B parameter model already outperforms most largemodel-based methods and achieves comparable performance to state-of-the-art approaches with significantly larger parameter ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** However, the text-based topological map achieves substantially lower performance improvements than the STAR-Att used in row (c), indicating significant challenges for understanding topological structures through ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Notably, compared to MapGPT[15], our approach achieves an absolute improvement of 3.39% in SR and 9.08 in SPL on the val unseen split.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Embodiment/environment | For testing, we utilize 1,021 navigation paths from the val seen split and 2,349 paths from the val unseen split in the R2R dataset. | hardware/simulator version and reset protocol | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Dataset/benchmark | All ablation experiments are conducted on the TagaVLM-0.5B model and the val unseen split of R2R dataset. | role, split, size and leakage | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Metric | In these metrics, Trajectory Length (TL) denotes average path length in meters; Navigation Error (NE) represents the average distance in meters between the agent's final location and the target; Success Rate (SR) ... | definition, denominator, direction and uncertainty | p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Baseline/ablation | It is worth noting that, our 0.5B parameter model already outperforms most largemodel-based methods and achieves comparable performance to state-of-the-art approaches with significantly larger parameter counts. | fair input/data/compute/action matching | p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / V. CONCLUSIONS - extractive body cue:** Future work will build on this strong baseline by scaling training on larger datasets, enriching STAR-Att with more complex geometric priors, and extending our framework ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** However, due to computational resource limitations, TagaVLM-7B is fine-tuned with only 200K augmented samples.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** However, owing to the limitation of computational resources, the amount of training data used for the proposed method is significantly smaller than that of NaviLLM[16], ...

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, these methods ignore the gap between disembodied knowledge of pretrained VLMs and the embodied property of the VLN task, requiring the model to understand implicit visual-topological alignment passively and therefore increasing ...를 문제로 두고, Our contribution can be summarized as follows: • We introduce TagaVLM, an end-to-end VLN framework that architecturally embeds topological structures into the VLM backbone. • We propose two synergistic components: the INP ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 4 (III. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
