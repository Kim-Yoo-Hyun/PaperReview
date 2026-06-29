# Survey Update Report

- Last updated: 2026-06-29 KST
- Scope: 3D Vision + Robotics + Vision-Language survey in `/home/yoohyun/KAIST/Paper`

## 2026-06-29 Update

- Deleted `FOUNDATION_GAP_AUDIT.md`.
- Removed the `Reading Priority` section from `PAPER.md` so that `PAPER.md` remains a registry-only document.
- Added `PRIORITY.md` as the separate reading-priority and foundation-gap roadmap.
- Reviewed foundation-paper gaps across all categories, not only VLN/navigation.
- Corrected mismatched title/link entries in `PRIORITY.md`: FCGF, COLMAP/SfM, KinectFusion, DepthContrast, ElasticFusion, Semantic-NeRF, and Distilled Feature Fields.
- Added 68 missing priority/foundation papers as actual folders with `paper.pdf` and `01_overview.md` through `05_insights.md`.
- Regenerated `PAPER.md` from the survey manifest. Current registry size: 606 papers, 606 PDFs downloaded.
- Converted all `PRIORITY.md` `Add:` entries to `Local:` links after folder generation.
- Added the priority criterion: `최신 트렌드 중 핵심 flow가 되는 논문`.
- Updated `README.md` snapshot counts and added links to `PRIORITY.md` and `report.md`.

## Current Diagnosis

The registry is now balanced between recent 2024-2026 papers and core foundation papers, especially:

- Vision-language-action and robot manipulation
- 3D Gaussian Splatting and neural scene representations
- 3D large multimodal models
- 3D diffusion and generation
- Open-vocabulary 3D semantics
- Recent embodied navigation and semantic mapping

The previous main weakness was foundation coverage. That has been mostly addressed for the priority categories by adding task-defining, benchmark-defining, and representation-defining papers directly into the registry.

## Foundation Coverage Status

These categories are now covered with both foundation papers and current trend-flow papers:

1. Navigation and Embodied AI:
   - `Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments`
   - `VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation`
   - `Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments`
   - `Room-Across-Room: Multilingual Vision-and-Language Navigation with Dense Spatiotemporal Grounding`
   - `Matterport3D: Learning from RGB-D Data in Indoor Environments`
   - `Habitat: A Platform for Embodied AI Research`

2. 3D Scene Graphs and Graph Reasoning:
   - `3D Scene Graph: A Structure for Unified Semantics, 3D Space, and Camera`
   - `3DSSG: 3D Scene Graph Prediction from 3D Point Clouds`

3. Vision-Language-Action and Robot Manipulation:
   - `CLIPort: What and Where Pathways for Robotic Manipulation`
   - `Transporter Networks: Rearranging the Visual World for Robotic Manipulation`
   - `Neural Descriptor Fields: SE(3)-Equivariant Object Representations for Manipulation`

4. 3D Detection, BEV, Occupancy, and Sensor Fusion:
   - `Lift, Splat, Shoot: Encoding Images from Arbitrary Camera Rigs by Implicitly Unprojecting to 3D`
   - `VoxelNet: End-to-End Learning for Point Cloud Based 3D Object Detection`
   - `PointPillars: Fast Encoders for Object Detection from Point Clouds`
   - `SSCNet: Semantic Scene Completion from a Single Depth Image`

5. Reconstruction, Neural Fields, and SLAM:
   - `Structure-from-Motion Revisited` / COLMAP
   - `KinectFusion: Real-Time Dense Surface Mapping and Tracking`
   - `BundleFusion`
   - `Mip-NeRF`
   - `Instant Neural Graphics Primitives with a Multiresolution Hash Encoding`

6. VLM/LMM and Vision Foundations:
   - `Flamingo: a Visual Language Model for Few-Shot Learning`
   - `BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models`
   - `Visual Instruction Tuning`
   - `Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection`

Remaining secondary checks for future updates:

- `3DSSG: 3D Scene Graph Prediction from 3D Point Clouds`
- `ImageBind: One Embedding Space To Bind Them All`
- Recent 2026 accepted papers that become available after proceedings pages stabilize.

## Update Direction

1. Keep new papers as actual paper folders with `paper.pdf` and the five-note structure.
2. Keep `PAPER.md` as the complete registry only.
3. Keep `PRIORITY.md` as the ranked reading roadmap and update it whenever new papers are added.
4. Keep `README.md` counts and document links synchronized with the manifest.
5. When adding future papers, prioritize papers that define datasets, benchmarks, canonical task formulations, or the latest trend-flow before adding incremental methods.

## Priority Criteria

The reading priority is based on:

- 해당 분야에서의 foundation 핵심성
- 3D CV 중심성
- Robotics 확장 가능성
- 연구 공백 명확성
- 평가 가능성
- 구현 난이도
- 데이터 접근성
- 논문 contribution 가능성
- 최신 트렌드 중 핵심 flow가 되는 논문
