# PhysSplat: Efficient Physics Simulation for 3D Scenes via MLLM-Guided Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhao_PhysSplat_Efficient_Physics_Simulation_for_3D_Scenes_via_MLLM-Guided_Gaussian_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhao_PhysSplat_Efficient_Physics_Simulation_for_3D_Scenes_via_MLLM-Guided_Gaussian_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, Gaussian Splatting
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Zhao_PhysSplat_Efficient_Physics_Simulation_for_3D_Scenes_via_MLLM-Guided_Gaussian_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhao_PhysSplat_Efficient_Physics_Simulation_for_3D_Scenes_via_MLLM-Guided_Gaussian_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Some recent approaches aim to bridge the gap between rendering and simulation integrating physics-based This ICCV paper is the Open Access version, provided by the Computer Vision Foundation.를 문제로 두고, Our method is the only one that can simulate the entire scene at a much faster speed. priors into 3D object representations using physical simulators [4, 7, 27].를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent advancements in 3D generation models have opened new possibilities for simulating dynamic 3D object movements and customizing behaviors, yet creating this content remains challenging.
- **p. 1 / Abstract - extractive body cue:** Current methods often require manual assignment of precise physical properties for simulations or rely on video generation models to predict them, which is computationally intensive.
- **p. 1 / Abstract - extractive body cue:** In this paper, we rethink the usage of multi-modal large language model (MLLM) in physics-based simulation, and present PhysSplat, a physics-based approach that efficiently endows ...
- **p. 1 / Abstract - extractive body cue:** We begin with detailed scene reconstruction and object-level 3D open-vocabulary segmentation, progressing to multi-view image in-painting.
- **p. 1 / Abstract - extractive body cue:** Inspired by human visual reasoning, we propose MLLMbased Physical Property Perception (MLLM-P3) to predict the mean physical properties of objects in a zero-shot manner.
- **p. 1 / 1. Introduction - extractive body cue:** Some recent approaches aim to bridge the gap between rendering and simulation integrating physics-based This ICCV paper is the Open Access version, provided by the ...
- **p. 2 / 1. Introduction - extractive body cue:** However, learning material physical properties from video diffusion priors is computationally expensive and time-consuming in practice.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our method is the only one that can simulate the entire scene at a much faster speed. priors into 3D object representations using physical simulators ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose PhysSplat, a physics-based method that efficiently transforms static 3D objects into interactive ones capable of responding to new interactions, as ...
- **p. 3 / 4. Our Methodology - extractive body cue:** We propose MLLM-based Physical Property Perception (MLLM-P3) to predict the mean values of these properties (Section 4.2).
- **p. 4 / 4.2. MLLM-based Physical Property Perception - extractive body cue:** Inspired by human reasoning, we propose MLLM-based Physical Property Perception (MLLM-P3), which uses MLLM for open-vocabulary semantic reasoning about materials and their physical properties.
- **p. 5 / 4.3. Physics-Based Dynamics - extractive body cue:** To address these challenges, we propose material property distribution prediction (MPDP), and reformulate the problem from a regression task to a probability distribution estimation task.
- **p. 4 / 4.2. MLLM-based Physical Property Perception - extractive body cue:** Then we use a VQA model, such as BLIP [19] to produce a text description of the image.
- **p. 3 / 4. Our Methodology - extractive body cue:** We then use the Material Property Distribution Prediction (MPDP) model to estimate the full distribution, simulating object dynamics with driving particles sampled using the Physical-Geometric ...
- **p. 3 / 4.1. 3D Open-vocabulary Segmentation - extractive body cue:** For each scene, we first train a 3DGS model on given images and camera poses.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Finally, the selected material name, image, and text description provide a structured input to the MLLM, grounding its outputs in a reliable context. | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (4.2. MLLM-based Physical Property Perception), p. 5 (4.3. Physics-Based Dynamics) |
| State/latent | Finally, selected, material, name, image, text, description, provide, structured, input, MLLM, grounding | geometry, map, object/relationship state | p. 4 (4.2. MLLM-based Physical Property Perception), p. 5 (4.3. Physics-Based Dynamics), p. 3 (4.1. 3D Open-vocabulary Segmentation) |
| Output/action | We train a network Dθ using part of the synthesized dataset, with the object's point cloud and predicted mean values (Section 4.2) as input. | point map, pose, scene graph, affordance 또는 query result | p. 5 (4.3. Physics-Based Dynamics), p. 3 (4.1. 3D Open-vocabulary Segmentation), p. 1 (1. Introduction) |
| Objective/outcome | Following PhysGaussian[42], we define each Gaussian kernel's time-dependent state as: x_i ( t) = \De lta ( x _i, t), \ \Si gma _i(t) = F_i(t) \Sigma _i F_i(t)^T, (1) where ∆(·, ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (3.1. Material Point Method), p. 4 (4.2. MLLM-based Physical Property Perception), p. 4 (4.2. MLLM-based Physical Property Perception) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our method is the only one that can simulate the entire scene at a much faster speed. priors into 3D object representations using physical simulators ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose PhysSplat, a physics-based method that efficiently transforms static 3D objects into interactive ones capable of responding to new interactions, as ...
- **p. 3 / 4. Our Methodology - extractive body cue:** We propose MLLM-based Physical Property Perception (MLLM-P3) to predict the mean values of these properties (Section 4.2).
- **p. 4 / 4.2. MLLM-based Physical Property Perception - extractive body cue:** Inspired by human reasoning, we propose MLLM-based Physical Property Perception (MLLM-P3), which uses MLLM for open-vocabulary semantic reasoning about materials and their physical properties.
- **p. 5 / 4.3. Physics-Based Dynamics - extractive body cue:** To address these challenges, we propose material property distribution prediction (MPDP), and reformulate the problem from a regression task to a probability distribution estimation task.
- **p. 6 / 5.3. Comparison with SOTA Methods - extractive body cue:** Our PhysSplat achieves better performance in both metrics, which demonstrates that PhysSplat generates videos that are both realistic and physically plausible, with a high degree ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Ablation Study on PhysDreamer [47] dataset. AS denotes the average aesthetic quality score predicted using the LAION aesthetic predictor. property distribution prediction is ...
- **p. 6 / 5.3. Comparison with SOTA Methods - extractive body cue:** 2 presents the user study results (RS) and aesthetic score (AS) predicted by LAION aesthetic predictor following [14].

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (5.3. Comparison with SOTA Methods), p. 8 (Figure/Table caption) |
| Embodiment/environment | We also conduct experiments on the physical simulation of single objects on four real-world static scenes from PhysDreamer [47] for fair comparison. | hardware/simulator version and reset protocol | p. 6 (5.2. Datasets), p. 6 (5.3. Comparison with SOTA Methods) |
| Dataset/benchmark | Visual results on Open-world dataset and 3D assets generated by LGM [36]. patterns, accurately capturing the natural flow and details of real-world movements. | role, split, size and leakage | p. 6 (5.2. Datasets), p. 6 (5.3. Comparison with SOTA Methods), p. 7 (5.3. Comparison with SOTA Methods), p. 7 (5.3. Comparison with SOTA Methods) |
| Metric | PhysDreamer [47] scores lower than DreamGaussian4D [30] in RS and PhysGaussian [42] in AS, which indicates that pre-generated videos may not be a proper ground truth for supervision. | definition, denominator, direction and uncertainty | p. 6 (5.3. Comparison with SOTA Methods), p. 6 (5.1. Implementation Details), p. 8 (Figure/Table caption) |
| Baseline/ablation | Figure 7. Ablation study. Visualization of space-time slices for ablation study on PhysDreamer [47]. Our method can generate closer content compared with the real capture. gle objects. Therefore, we omit direct comparisons ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 6 (5.1. Implementation Details) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 7. Conclusion - extractive body cue:** Future work will explore to reconstruct occluded parts, further enhancing realism and expanding applications in interactive virtual experiences.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Some recent approaches aim to bridge the gap between rendering and simulation integrating physics-based This ICCV paper is the Open Access version, provided by the Computer Vision Foundation.를 문제로 두고, Our method is the only one that can simulate the entire scene at a much faster speed. priors into 3D object representations using physical simulators [4, 7, 27].를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (4.2. MLLM-based Physical Property Perception), p. 3 (4. Our Methodology), p. 3 (4.1. 3D Open-vocabulary Segmentation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
