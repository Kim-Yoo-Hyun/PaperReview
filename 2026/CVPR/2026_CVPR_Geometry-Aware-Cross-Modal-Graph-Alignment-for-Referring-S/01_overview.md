# Geometry-Aware Cross-Modal Graph Alignment for Referring Segmentation in 3D Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Tao_Geometry-Aware_Cross-Modal_Graph_Alignment_for_Referring_Segmentation_in_3D_Gaussian_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Tao_Geometry-Aware_Cross-Modal_Graph_Alignment_for_Referring_Segmentation_in_3D_Gaussian_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, semantic, alignment, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Tao_Geometry-Aware_Cross-Modal_Graph_Alignment_for_Referring_Segmentation_in_3D_Gaussian_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Tao_Geometry-Aware_Cross-Modal_Graph_Alignment_for_Referring_Segmentation_in_3D_Gaussian_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 First, the language encoder inherently lacks explicit positional encoding, which limits its ability to represent spatial prepositions and relational geometry.를 문제로 두고, Our contributions are: • We introduce a geometry-aware perspective for language grounding that embeds explicit spatial structure into linguistic features, enabling more accurate reasoning. • We propose a cross-modal relational alignment ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Referring 3D segmentation seeks to localize and segment target objects in a 3D scene given a natural-language query, requiring joint reasoning over geometric structures and ...
- **p. 1 / Abstract - extractive body cue:** Although recent progress using 3D Gaussian Splatting (3DGS) has improved rendering quality, existing methods still struggle to spatially ground textual references due to two fundamental ...
- **p. 1 / Abstract - extractive body cue:** GeoCGA introduces positionaware prompt expansion to build a semantic-spatial graph capturing relational structure in text, and constructs a Gaussian-based geometric graph encoding 3D topology.
- **p. 1 / Abstract - extractive body cue:** A cross-modal alignment module enforces geometric consistency between the two graphs, enabling stable and spatially grounded correspondence across views.
- **p. 1 / Abstract - extractive body cue:** GeoCGA consistently outperforms prior state-of-the-art methods, yielding relative mIoU improvements of 20.8% on Ref-LERF, 5.7% on LERF-OVS, and 1.0% on 3D-OVS.
- **p. 2 / 1. Introduction - extractive body cue:** First, the language encoder inherently lacks explicit positional encoding, which limits its ability to represent spatial prepositions and relational geometry.
- **p. 2 / 1. Introduction - extractive body cue:** These observations suggest that existing frameworks implicitly entangle geometric and semantic information, without an explicit mechanism to disentangle and align them across modalities.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are: • We introduce a geometry-aware perspective for language grounding that embeds explicit spatial structure into linguistic features, enabling more accurate reasoning. • ...
- **p. 2 / 1. Introduction - extractive body cue:** Guided by these findings, we propose GeoCGA (see Fig.
- **p. 3 / 3. Problem Statement and Notations - extractive body cue:** Spatial awareness deficiency leads to incorrect localization in ReferSplat [13], while our method correctly grounds the target despite challenging spatial cues. ri for each Gaussian ...
- **p. 3 / 3. Problem Statement and Notations - extractive body cue:** While this framework enables basic language-to-geometry grounding, its spatial reasoning capability remains limited, as analyzed in Sec.
- **p. 5 / 5.3. 3D Scene Graph Construction (3DSGC) - extractive body cue:** We use the pretrained model [18] to obtain the object-level representations and construct an object-level 3D scene graph Gsg = (V, E), where each node ...
- **p. 5 / 5.3. 3D Scene Graph Construction (3DSGC) - extractive body cue:** Relying solely on primitive-level reasoning forces the model to infer object structure implicitly from fragmentary cues, leading to ambiguous alignment under viewpoint changes.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our contributions are: • We introduce a geometry-aware perspective for language grounding that embeds explicit spatial structure into linguistic features, enabling more accurate reasoning. • We propose a cross-modal relational alignment ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| State/latent | contributions, introduce, geometry-aware, perspective, language, grounding, embeds, explicit, spatial, structure, linguistic, features | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (5.3. 3D Scene Graph Construction (3DSGC)) |
| Output/action | Instead of treating text as a purely semantic signal, we expand the input description with position-aware prompts to derive a semantic-spatial graph that captures relational structure within language. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 5 (5.3. 3D Scene Graph Construction (3DSGC)), p. 3 (3. Problem Statement and Notations) |
| Objective/outcome | geometric accuracy, semantic consistency와 planning/manipulation utility | geometric accuracy, semantic consistency와 planning/manipulation utility | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are: • We introduce a geometry-aware perspective for language grounding that embeds explicit spatial structure into linguistic features, enabling more accurate reasoning. • ...
- **p. 2 / 1. Introduction - extractive body cue:** Guided by these findings, we propose GeoCGA (see Fig.
- **p. 3 / 3. Problem Statement and Notations - extractive body cue:** Spatial awareness deficiency leads to incorrect localization in ReferSplat [13], while our method correctly grounds the target despite challenging spatial cues. ri for each Gaussian ...
- **p. 3 / 3. Problem Statement and Notations - extractive body cue:** While this framework enables basic language-to-geometry grounding, its spatial reasoning capability remains limited, as analyzed in Sec.
- **p. 7 / 6.2. Comparisons with State-of-the-Arts - extractive body cue:** 3), where scenes are relatively clean and objects are easier to localize, GeoCGA still achieves the best performance across all categories and improves the overall ...
- **p. 7 / 6.2. Comparisons with State-of-the-Arts - extractive body cue:** 2), GeoCGA continues to outperform prior methods with an average improvement of +5.7%.
- **p. 8 / 6.3. Ablation Study - extractive body cue:** (10)) further improves grounding accuracy ( +1.0 and +0.6 ) over relationimplicit matching, showing that aligning linguistic and geometric relations is essential for reliable cross-modal ...
- **p. 8 / 6.3. Ablation Study - extractive body cue:** First, incorporating edge-aware message passing improves performance over the Semantic GNN baseline ( +0.6 on Ramen and +1.2 on Kitchen ), indicating that explicitly modeling ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (6.2. Comparisons with State-of-the-Arts), p. 7 (6.2. Comparisons with State-of-the-Arts) |
| Embodiment/environment | 3), where scenes are relatively clean and objects are easier to localize, GeoCGA still achieves the best performance across all categories and improves the overall average by +1.0%. | hardware/simulator version and reset protocol | p. 7 (6.2. Comparisons with State-of-the-Arts), p. 8 (6.3. Ablation Study) |
| Dataset/benchmark | We evaluate GeoCGA across multiple benchmarks and provide detailed analyses of its performance. | role, split, size and leakage | p. 7 (6.2. Comparisons with State-of-the-Arts), p. 8 (6.3. Ablation Study), p. 6 (6. Experiments), p. 6 (6.1. Experimental Setting) |
| Metric | Following the setting of ReferSplat [13], we employ the official data partitions and generate pseudo masks using the confidenceweighted IoU strategy. | definition, denominator, direction and uncertainty | p. 6 (6.1. Experimental Setting), p. 7 (6.1. Experimental Setting), p. 7 (6.2. Comparisons with State-of-the-Arts) |
| Baseline/ablation | Superscripts indicate absolute improvements over the baseline. | fair input/data/compute/action matching | p. 7 (6.2. Comparisons with State-of-the-Arts), p. 7 (6.2. Comparisons with State-of-the-Arts), p. 8 (6.3. Ablation Study) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6.3. Ablation Study - extractive body cue:** The bottom row illustrates typical failure modes where spatial ambiguity or relational confusion leads to incorrect (ReferSplat [13]) or incomplete (Ours) segmentation. mentary perspectives.
- **p. 8 / 7. Conclusion and Discussion - extractive body cue:** Future work may explore end-to-end differentiable object discovery to reduce reliance on pretrained representations, as well as richer geometric priors and more scalable graph matching ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. Spatial reasoning deficiency leads to coarse segmenta- tion in ReferSplat [13], while our method produces precise masks. consistent segmentation under complex spatial cues. ...
- **p. 6 / 6.1. Experimental Setting - extractive body cue:** Ref-LERF emphasizes fine-grained referring understanding within individual scenes that involve intricate spatial layouts and strong occlusions.
- **p. 7 / 6.3. Ablation Study - extractive body cue:** Combining both modules yields the best performance (+3.8 and +10.2), confirming that explicit linguistic structure and geometric topology are complementary and jointly essential for robust ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 First, the language encoder inherently lacks explicit positional encoding, which limits its ability to represent spatial prepositions and relational geometry.를 문제로 두고, Our contributions are: • We introduce a geometry-aware perspective for language grounding that embeds explicit spatial structure into linguistic features, enabling more accurate reasoning. • We propose a cross-modal relational alignment ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (5.3. 3D Scene Graph Construction (3DSGC)), p. 5 (5.3. 3D Scene Graph Construction (3DSGC)), p. 7 (6.2. Comparisons with State-of-the-Arts), p. 7 (6.2. Comparisons with State-of-the-Arts) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
