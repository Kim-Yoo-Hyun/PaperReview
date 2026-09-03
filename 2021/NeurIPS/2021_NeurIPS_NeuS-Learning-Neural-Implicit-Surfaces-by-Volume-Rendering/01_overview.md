# NeuS: Learning Neural Implicit Surfaces by Volume Rendering for Multi-view Reconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2106.10689.
> PDF retrieval source: https://arxiv.org/pdf/2106.10689. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, NeRF, surface reconstruction, geometry
- Official paper: https://arxiv.org/abs/2106.10689
- Full-text retrieval: https://arxiv.org/pdf/2106.10689
- Code/Project: https://lingjie0206.github.io/papers/NeuS/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, extracting high-fidelity surface from the learned implicit field is difficult because the density-based scene representation lacks sufficient constraints on its level sets.를 문제로 두고, Therefore we propose a novel volume rendering scheme to ensure unbiased surface reconstruction in the first-order approximation of SDF.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present a novel neural surface reconstruction method, called NeuS, for reconstructing objects and scenes with high fidelity from 2D image inputs.
- **p. 1 / Abstract - extractive body cue:** Existing neural surface reconstruction approaches, such as DVR [Niemeyer et al., 2020] and IDR [Yariv et al., 2020], require foreground mask as supervision, easily get ...
- **p. 1 / Abstract - extractive body cue:** Meanwhile, recent neural methods for novel view synthesis, such as NeRF [Mildenhall et al., 2020] and its variants, use volume rendering to produce a neural ...
- **p. 1 / Abstract - extractive body cue:** However, extracting high-quality surfaces from this learned implicit representation is difficult because there are not sufficient surface constraints in the representation.
- **p. 1 / Abstract - extractive body cue:** In NeuS, we propose to represent a surface as the zero-level set of a signed distance function (SDF) and develop a new volume rendering method ...
- **p. 2 / 1 Introduction - extractive body cue:** However, since it is intended for novel view synthesis rather than surface reconstruction, NeRF only learns a volume density field, from which it is difficult ...
- **p. 3 / 1 Introduction - extractive body cue:** Alternatively, volumetric reconstruction methods circumvent the difficulty of explicit correspondence matching by estimating occupancy and color in a voxel grid from multi-view images and evaluating ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Therefore we propose a novel volume rendering scheme to ensure unbiased surface reconstruction in the first-order approximation of SDF.
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we present a new neural rendering scheme, called NeuS, for multi-view surface reconstruction.
- **p. 3 / 1 Introduction - extractive body cue:** On the contrary, our method performs well for such challenging cases without the need of masks.
- **p. 3 / 1 Introduction - extractive body cue:** In contrast, our method combines the advantages of surface rendering based and volume rendering based methods by constraining the scene space as a signed distance ...
- **p. 4 / 3 Method - extractive body cue:** That is, when two points have the same SDF value (thus the same SDF-induced S-density value), the point nearer to the view point should have ...
- **p. 3 / 3 Method - extractive body cue:** (1) In order to apply a volume rendering method to training the SDF network, we first introduce a probability density function φs(f(x)), called S-density, where ...
- **p. 7 / 3 Method - extractive body cue:** (15) Same as IDR[49], we empirically choose R as L1 loss, which in our observation is robust to outliers and stable in training.
- **p. 4 / 3 Method - extractive body cue:** Note that the standard deviation of φs(x) is given by 1/s, which is also a trainable parameter, that is, 1/s approaches to zero as the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In order to learn the weights of the neural network, we developed a novel volume rendering method to render images from the implicit SDF and minimize the difference between the rendered images ... | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3 Method), p. 4 (3 Method) |
| State/latent | order, learn, weights, neural, network, developed, novel, volume, rendering, render, images, implicit | geometry, map, object/relationship state | p. 3 (3 Method), p. 4 (3 Method), p. 4 (3 Method) |
| Output/action | Intuitively, the main idea of NeuS is that, with the aid of the S-density field φs(f(x)), volume rendering is used to train the SDF network with only 2D input images as supervision. | point map, pose, scene graph, affordance 또는 query result | p. 4 (3 Method), p. 4 (3 Method), p. 2 (1 Introduction) |
| Objective/outcome | Upon successful minimization of a loss function based on this supervision, the zero-level set of the network-encoded SDF is expected to represent an accurately reconstructed surface S, with its induced S-density φs(f(x)) ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3 Method), p. 7 (3 Method), p. 3 (3 Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** Therefore we propose a novel volume rendering scheme to ensure unbiased surface reconstruction in the first-order approximation of SDF.
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we present a new neural rendering scheme, called NeuS, for multi-view surface reconstruction.
- **p. 3 / 1 Introduction - extractive body cue:** On the contrary, our method performs well for such challenging cases without the need of masks.
- **p. 3 / 1 Introduction - extractive body cue:** In contrast, our method combines the advantages of surface rendering based and volume rendering based methods by constraining the scene space as a signed distance ...
- **p. 4 / 3 Method - extractive body cue:** That is, when two points have the same SDF value (thus the same SDF-induced S-density value), the point nearer to the view point should have ...
- **p. 8 / 4 Experiments - extractive body cue:** COLMAP results are achieved by trim=0.
- **p. 8 / 4 Experiments - extractive body cue:** The results show that our approach outperforms the baseline methods on the DTU dataset in both settings - w/ and w/o mask in terms of ...
- **p. 20 / Figure/Table caption - extractive body cue:** Table 4: Quantitative comparisons with NeRF on the task of novel view synthesis without mask supervision. E.2 Novel View Synthesis In this experiment, we held ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Embodiment/environment | We further tested on 7 challenging scenes from the low-res set of the BlendedMVS dataset [48](CC-4 License). | hardware/simulator version and reset protocol | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Dataset/benchmark | (b) COLMAP𝑡𝑟𝑖𝑚= 10 (c) COLMAP𝑡𝑟𝑖𝑚= 7 (a) Ours Reference Image Figure 8: Comparison on scenes with thin structure objects. | role, split, size and leakage | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments) |
| Metric | We measure the reconstruction quality with the Chamfer distances in the same way as UNISURF [31] and IDR [49] and report the scores in Table 1. | definition, denominator, direction and uncertainty | p. 8 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments) |
| Baseline/ablation | (1) The state-of-the-art surface rendering approach - IDR [49]: IDR can reconstruct surface with high quality but requires foreground masks as supervision; Since IDR has demonstrated superior quality compared to another surface ... | fair input/data/compute/action matching | p. 7 (4 Experiments), p. 8 (4 Experiments), p. 2 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 5 Conclusion - extractive body cue:** One limitation of our method is that although our method does not heavily rely on correspondence matching of texture features, the performance would still degrade ...
- **p. 21 / Figure/Table caption - extractive body cue:** Figure 16: A failure reconstruction case containing textureless regions. Figure 16 shows a failure case where our method fails to correctly reconstruct the texutreless region ...
- **p. 8 / 4 Experiments - extractive body cue:** As shown in Figure 4 for the setting of w/ mask, IDR shows limited performance for reconstructing thin metals parts in Scan 37 (DTU), and ...
- **p. 10 / 5 Conclusion - extractive body cue:** NeuS produces high-quality reconstruction and successfully reconstructs objects with severe occlusions and complex structures.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: (a) Illustration of the surface rendering and volume rendering. (b) A toy example of bamboo planter, where there are occlusions on the top ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Illustration of (a) weight bias of naive solution, and (b) the weight function defined in our solution, which is unbiased in the first-order ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, extracting high-fidelity surface from the learned implicit field is difficult because the density-based scene representation lacks sufficient constraints on its level sets.를 문제로 두고, Therefore we propose a novel volume rendering scheme to ensure unbiased surface reconstruction in the first-order approximation of SDF.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 3 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
