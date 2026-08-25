# 3D Vision, Robotics, and Vision-Language Paper Survey

This repository is a structured literature survey for research at the intersection of 3D vision, robotics, and vision-language intelligence.

It collects papers, PDFs, and compact reading notes for topics such as vision-language-action models, 3D scene graphs, embodied navigation, Gaussian Splatting, NeRF, SLAM, sensor fusion, grounding, calibration, planning, reinforcement learning, imitation learning, and foundation models.

The full paper registry is maintained in [PAPER.md](./PAPER.md).
The consolidated robotics-first priority and reading roadmap is maintained in [READING_PLAN.md](./research/READING_PLAN.md).
Reading progress and cross-paper comparison are maintained in [READING_STATUS.csv](./research/READING_STATUS.csv) and [synthesis](./synthesis/README.md).
Cross-track research gaps and experiment-ready hypotheses are maintained in [RESEARCH_GAPS.md](./research/RESEARCH_GAPS.md) and [RESEARCH_IDEAS.md](./research/RESEARCH_IDEAS.md).
The latest registry and frontier audit is recorded in [UPDATES_2026-08-25.md](./research/UPDATES_2026-08-25.md).

## Scope

The survey focuses on papers that connect at least one of the following core areas:

- 3D Vision
- Robotics
- Vision-Language

Secondary keywords include:

- Vision-Language-Action, Vision-Language Navigation, 3D Scene Graphs
- Gaussian Splatting, NeRF, 3D reconstruction, SLAM
- Grounding, alignment, consistency, calibration, sensor fusion
- Diffusion, generation, representation learning
- Reinforcement learning, imitation learning, planning
- LLMs, VLMs, graph reasoning, semantic and geometric scene understanding

## Current Snapshot

| Item | Count |
|---|---:|
| Papers | 821 |
| Local PDFs | 194 |
| Per-paper markdown notes | 4,105 |
| Canonical categories | 23 |
| Years covered | 1987-2026 |

## Venue Coverage

| Venue | Count |
|---|---:|
| CVPR | 157 |
| ICCV | 91 |
| ICLR | 101 |
| ICML | 75 |
| NeurIPS | 68 |
| ECCV | 49 |
| ICRA | 55 |
| CoRL | 52 |
| IROS | 20 |
| RSS | 61 |
| RA-L | 21 |
| 3DV | 16 |

Additional papers are included from ICAPS, WACV, TMLR, SIGGRAPH, T-RO, TOG, AAAI, NAACL, AISTATS, EMNLP, ISMAR, and arXiv when they are foundational or directly relevant.

## Directory Layout

Papers are organized first by year, then by venue or journal.

```text
<year>/<venue>/<year>_<venue>_<short-title>/
```

Example:

```text
2026/ICRA/2026_ICRA_Audio-VLA-Adding-Contact-Audio-Perception-to-Vision-Langua/
2025/ICCV/2025_ICCV_EmbodiedOcc-Embodied-3D-Occupancy-Prediction-for-Vision-ba/
2024/ECCV/2024_ECCV_SceneVerse-Scaling-3D-Vision-Language-Learning-for-Grounde/
```

Each paper folder contains:

```text
01_overview.md
02_problem.md
03_method.md
04_evaluation.md
05_insights.md
paper.pdf  # optional local cache
```

## Note Format

Each paper is summarized with the same structure:

- `01_overview.md`: problem, core idea, input/output, claims, limitations, contributions, project/code link
- `02_problem.md`: motivation, target problem, relation to prior work
- `03_method.md`: method summary, principle, key mechanisms
- `04_evaluation.md`: datasets, benchmarks, metrics, splits, baselines, main results, reproducibility notes
- `05_insights.md`: strengths, limitations, paper claims, future work, personal research directions

## Main Registry

Use [PAPER.md](./PAPER.md) as the primary navigation file. Use [READING_PLAN.md](./research/READING_PLAN.md) for priority criteria, reading order, and the CORE/NEXT intensive-reading set.

It groups papers by research theme:

- Vision-Language-Action and Robot Manipulation
- 3D Large Multimodal Models
- Navigation and Embodied AI
- Language-Embedded NeRF and Gaussian Fields
- 3D Scene Representations and Neural Fields
- 3D Generative Modeling and Diffusion
- Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- 3D Semantic Understanding and Alignment
- 3D Equivariance, Calibration, and Registration
- 3D Vision-Language Grounding
- 3D Scene Graphs and Graph Reasoning
- Open-Vocabulary 3D Mapping
- 3D Reconstruction, Geometry, and SLAM
- Foundations: Transformers, VLMs, diffusion, 3D geometry, SLAM, RL, and robot policies
- Foundations: robot motion planning, control, robot learning, and sim-to-real
- Reinforcement learning, offline RL, imitation learning, and inverse RL for robotics
- Contact-rich and model-based manipulation
- Robot learning and manipulation
- Legged locomotion, loco-manipulation, mobile manipulation, and whole-body control
- Safe robotics, constrained control, and robot world models
- Failure detection, uncertainty, active perception, and long-horizon replanning
- Tactile/force-aware VLA, articulated interaction, deformable objects, tools, and assembly
- Cross-embodiment learning, robot datasets, and domain-diverse robotics
- Tactile and dexterous manipulation
- Multi-robot systems

## Recommended Reading Paths

Start from the foundation papers if you are entering the area:

- Transformers and language models: Attention, BERT, GPT-style few-shot learning
- Vision-language models: CLIP, ViT, Segment Anything, DINOv2
- 3D representation: PointNet, NeRF, 3D Gaussian Splatting
- Geometry and SLAM: ORB-SLAM, DROID-SLAM, DUSt3R, MASt3R, VGGT
- Policy learning: RoboMimic, Decision Transformer, DDPM/Flow Matching, Diffusion Policy, SayCan, RT-1, RT-2, PaLM-E, Open X-Embodiment

For robotics and VLA research:

- Use [READING_PLAN.md](./research/READING_PLAN.md) for the planning/control, RL/IL, contact-rich manipulation, locomotion, whole-body/mobile manipulation, safety, and world-model backbone.
- Then connect that backbone to PDDLStream, RLBench, RT-1, RT-2, PaLM-E, OpenVLA, Octo, π0, FAST, OpenVLA-OFT, Reactive Diffusion Policy, Perceiver-Actor, RVT, VoxPoser, and ReKep.

For 3D vision-language and embodied spatial reasoning:

- Start with ScanRefer, ReferIt3D, 3DVG-Transformer, 3D-VisTA, 3D-LLM, SpatialVLM, SceneVerse, Uni3DL, RoboSpatial.
- Then read open-vocabulary 3D mapping and Gaussian-language field papers such as LERF, CLIP-Fields, ConceptFusion, OpenScene, LangSplat, SceneSplat, ReasonGrounder, and related 3DGS works.

For 3D computer vision-first research:

- Start with PointNet/PointNet++, DGCNN, KPConv, MinkowskiNet, Point Transformer, Point-BERT, Point-MAE, CenterPoint, PV-RCNN, PETR, BEVDepth, VoxFormer.
- Then read modern geometry and reconstruction work such as DUSt3R, MASt3R, VGGT, CUT3R, Dens3R, MASt3R-SfM, FlowMap, Flash3D, VGGT-Motion, WorldMirror.
- For neural scene representations, read 3D Gaussian Splatting, SuGaR, pixelSplat, MVSplat, SplaTAM, SplatFormer, No Pose No Problem, TokenSplat, Uni3R, SDGS, VarSplat.
- For sensor fusion and autonomous 3D perception, read BEVFormer, BEVFusion, VoxFormer, GaussianFormer, RIOcc, V2X-R, SplatAD, L3DR, RadarSplat, SimULi, UniSplat.
- For diffusion and generative 3D, read Marigold, Depth Anything, ReconFusion, LaGeM, DiffSplat, G4Splat, HAD, GaussFusion, PartGen, SeaLion, CraftsMan3D.

## Curation Policy

The collection follows these rules:

- 2024-current: broad coverage of relevant top-tier conference and journal papers with verifiable official records.
- 2021-current: emphasis on highly cited or field-shaping papers.
- Foundational papers: included regardless of year when they define the underlying methods used by later work.
- Each paper should have a stable official venue or arXiv page and a consistent note structure; a local PDF is optional.
- Venue year is not repeated in venue folder names because papers are already grouped by year.

## Maintenance Workflow

The survey is maintained through the idempotent tools documented in [survey_work/README.md](./survey_work/README.md). One-off augmentation and PDF retry scripts are historical artifacts under `survey_work/archive/` and are not part of the normal workflow.

Useful commands:

```bash
python3 survey_work/audit_repository.py
python3 survey_work/register_papers.py --input /path/to/new_papers.json
python3 survey_work/register_papers.py --input /path/to/new_papers.json --apply
python3 survey_work/normalize_taxonomy.py
python3 survey_work/build_reading_tiers.py
python3 survey_work/audit_repository.py
```

The canonical metadata manifest is:

```text
survey_work/sources/papers.json
```

`build_lit_survey.py` is read-only without flags. PDF download and note overwrite require separate explicit flags and are intentionally excluded from the normal workflow.

## Notes on Public Sharing

This repository is designed for literature management and personal research use.

This checkout currently contains 194 local PDFs, but PDFs are an optional cache and never affect registry inclusion, tier, or reading priority. The nine papers in the latest robotics lineage update were intentionally registered without downloading PDFs. If publishing the repository publicly, review publisher and conference copyright policies before redistributing downloaded PDFs; a safer public version can keep the markdown notes and official source links only.

## README Style References

This README follows common patterns used in GitHub paper lists and awesome lists:

- clear scope and target audience
- table of contents or fast navigation
- topic-based grouping
- links to paper, code, project pages, and notes
- update and contribution rules
- citation or attribution section when the list is public

Representative examples:

- [awesome-vla-wam](https://github.com/DravenALG/awesome-vla-wam)
- [Awesome-Robotics-3D](https://github.com/zubair-irshad/Awesome-Robotics-3D)
- [Awesome VLA](https://github.com/Orlando-CS/Awesome-VLA)
- [awesome-physical-ai](https://github.com/keon/awesome-physical-ai)
- [Awesome-Embodied-AI](https://github.com/wadeKeith/Awesome-Embodied-AI)
