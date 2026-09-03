# LL3DA: Visual Interactive Instruction Tuning for Omni-3D Understanding, Reasoning, and Planning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2311.18651.
> PDF retrieval source: https://arxiv.org/pdf/2311.18651. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: ARCHIVE
- Tags: LLM, 3D Vision, Planning
- Official paper: https://arxiv.org/abs/2311.18651
- Full-text retrieval: https://arxiv.org/pdf/2311.18651
- Code/Project: https://github.com/Open3DA/LL3DA
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Though these methods have achieved remarkable success addressing different challenges in understanding 3D worlds with natural language, there are certain limitations.를 문제로 두고, To summarize, our key contributions lie in: • We present a LLM-based solution for understanding, reasoning, and planning in complex 3D environments. • Our model takes both the textual instructions and visual ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent advances in Large Multimodal Models (LMM) have made it possible for various applications in humanmachine interactions.
- **p. 1 / Abstract - extractive body cue:** However, developing LMMs that can comprehend, reason, and plan in complex and diverse 3D environments remains a challenging topic, especially considering the demand for understanding ...
- **p. 1 / Abstract - extractive body cue:** Existing works seek help from multi-view images, and project 2D features to 3D space as 3D scene representations.
- **p. 1 / Abstract - extractive body cue:** This, however, leads to huge computational overhead and performance degradation.
- **p. 1 / Abstract - extractive body cue:** In this paper, we present LL3DA, a Large Language 3D Assistant that takes point cloud as direct input and respond to both textualinstructions and visual-prompts.
- **p. 2 / 1. Introduction - extractive body cue:** Though these methods have achieved remarkable success addressing different challenges in understanding 3D worlds with natural language, there are certain limitations.
- **p. 1 / 1. Introduction - extractive body cue:** During this LLM carnival, researchers are also seeking generalized LLM solutions to various vision language tasks [16, 54, 59].

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our key contributions lie in: • We present a LLM-based solution for understanding, reasoning, and planning in complex 3D environments. • Our model ...
- **p. 2 / 1. Introduction - extractive body cue:** Additionally, by introducing additional visual interactions, our method could further remove the ambiguities within the vague textual instructions.
- **p. 3 / 3. Methodology - extractive body cue:** Next, we introduce our model design in details (Sec.
- **p. 3 / 3.1. Problem Formatting - extractive body cue:** 2 (a), the input of our model consists of a 3D scene represented by a set of points PC, the textual instruction It, and potential ...
- **p. 4 / 3.2. Model Design - extractive body cue:** (1) Here, fenc consists of d-dimensioned features for M points uniformly down-sampled from the input 3D scene through the Farthest Point Sampling (FPS) algorithm.
- **p. 3 / 3.2. Model Design - extractive body cue:** 2 (b), which consists of a frozen 3D scene encoder E3D, a visual prompt encoder, and a Q-Former to transform the permutation-invariant 3D embeddings into ...
- **p. 4 / 3.2. Model Design - extractive body cue:** We consider the decoder-only generative pre-trained transformers [49, 58] as our large language model backbone, which are sensitive to the input orders because of the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | To summarize, our key contributions lie in: • We present a LLM-based solution for understanding, reasoning, and planning in complex 3D environments. • Our model takes both the textual instructions and visual ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 3 (3.1. Problem Formatting) |
| State/latent | summarize, contributions, present, LLM-based, solution, understanding, reasoning, planning, complex, environments, model, takes | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 3 (3.1. Problem Formatting), p. 3 (3.2. Model Design) |
| Output/action | 2 (a), the input of our model consists of a 3D scene represented by a set of points PC, the textual instruction It, and potential visual interactions Iv that serve as supplementary ... | point map, pose, scene graph, affordance 또는 query result | p. 3 (3.1. Problem Formatting), p. 3 (3.2. Model Design), p. 4 (3.2. Model Design) |
| Objective/outcome | The parameters and the embedding layers of the LLM are kept frozen to save memory cost. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.2. Model Design), p. 4 (3.2. Model Design) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our key contributions lie in: • We present a LLM-based solution for understanding, reasoning, and planning in complex 3D environments. • Our model ...
- **p. 2 / 1. Introduction - extractive body cue:** Additionally, by introducing additional visual interactions, our method could further remove the ambiguities within the vague textual instructions.
- **p. 3 / 3. Methodology - extractive body cue:** Next, we introduce our model design in details (Sec.
- **p. 3 / 3.1. Problem Formatting - extractive body cue:** 2 (a), the input of our model consists of a 3D scene represented by a set of points PC, the textual instruction It, and potential ...
- **p. 4 / 3.2. Model Design - extractive body cue:** (1) Here, fenc consists of d-dimensioned features for M points uniformly down-sampled from the input 3D scene through the Farthest Point Sampling (FPS) algorithm.
- **p. 5 / 5.2. Comparison with SoTA Specialists - extractive body cue:** Results show that our method consistently outperforms existing methods on all the evaluation sets, and surpasses the generation based method, 3D-LLM, by a large margin ...
- **p. 7 / 5.3. Ablation Studies - extractive body cue:** Results show that the additional textual instructions and visual prompts improve the task diversity and further improve the performance on 3D Question Answering.
- **p. 6 / 5.3. Ablation Studies - extractive body cue:** The "early fusion" enables direct interaction with the 3D scene, thus it achieves a better performance.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 5 (5.2. Comparison with SoTA Specialists), p. 7 (5.3. Ablation Studies) |
| Embodiment/environment | In this paper, we experiment with 3D data from ScanNet [15], a 3D dataset covering 1,201 and 312 diverse and complex indoor 3D scenes for training and validation. | hardware/simulator version and reset protocol | p. 5 (5. Experiments), p. 5 (5.2. Comparison with SoTA Specialists) |
| Dataset/benchmark | However, the generalist model achieves poor results on Nr3D [1], which is because we did not try to differentiate between Nr3D and ScanRefer during training as these two datasets are used for ... | role, split, size and leakage | p. 5 (5. Experiments), p. 5 (5.2. Comparison with SoTA Specialists), p. 7 (5.3. Ablation Studies), p. 6 (5.3. Ablation Studies) |
| Metric | Here, m ∈{C, B-4, M, R}, and the m score of a caption is set to 0 if the IoU between the predicted box and the object is less than the given ... | definition, denominator, direction and uncertainty | p. 5 (5.2. Comparison with SoTA Specialists), p. 17 (Figure/Table caption), p. 5 (5.2. Comparison with SoTA Specialists) |
| Baseline/ablation | The baseline method directly generates the captions given the input 3D scene and visual prompts without any textual instructions. | fair input/data/compute/action matching | p. 7 (5.3. Ablation Studies), p. 5 (5.2. Comparison with SoTA Specialists), p. 5 (5.2. Comparison with SoTA Specialists) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusions - extractive body cue:** In this paper, we present LL3DA, a large language 3D assistant that could take both textual- and visual- interactions from human for understanding, reasoning, and ...
- **p. 8 / 6. Conclusions - extractive body cue:** Our model directly encodes 3D point cloud for scene representations, and aggregates information from scenes and human interactions with the atten8

## Why Read It

Planning and control의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Though these methods have achieved remarkable success addressing different challenges in understanding 3D worlds with natural language, there are certain limitations.를 문제로 두고, To summarize, our key contributions lie in: • We present a LLM-based solution for understanding, reasoning, and planning in complex 3D environments. • Our model takes both the textual instructions and visual ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Formatting), p. 3 (3.1. Problem Formatting) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
