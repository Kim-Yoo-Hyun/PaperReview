# 3D Vision, Robotics, and Vision-Language Paper Survey

This repository is a structured literature survey for research at the intersection of 3D vision, robotics, and vision-language intelligence.

It collects papers, PDFs, and compact reading notes for topics such as vision-language-action models, 3D scene graphs, embodied navigation, Gaussian Splatting, NeRF, SLAM, sensor fusion, grounding, calibration, planning, reinforcement learning, imitation learning, and foundation models.

The full paper registry is maintained in [PAPER.md](./PAPER.md).

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
| Papers | 350 |
| PDFs | 350 |
| Per-paper markdown notes | 1,750 |
| Years covered | 2015-2026 |

## Venue Coverage

| Venue | Count |
|---|---:|
| CVPR | 58 |
| ICCV | 51 |
| ICLR | 43 |
| ICML | 43 |
| NeurIPS | 34 |
| ICRA | 33 |
| ECCV | 29 |
| IROS | 17 |
| RA-L | 16 |
| CoRL | 15 |

Additional papers are included from RSS, WACV, TMLR, SIGGRAPH, T-RO, NAACL, and arXiv when they are foundational or directly relevant.

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
paper.pdf
```

## Note Format

Each paper is summarized with the same structure:

- `01_overview.md`: problem, core idea, input/output, claims, limitations, contributions, project/code link
- `02_problem.md`: motivation, target problem, relation to prior work
- `03_method.md`: method summary, principle, key mechanisms
- `04_evaluation.md`: datasets, benchmarks, metrics, splits, baselines, main results, reproducibility notes
- `05_insights.md`: strengths, limitations, paper claims, future work, personal research directions

## Main Registry

Use [PAPER.md](./PAPER.md) as the primary navigation file.

It groups papers by research theme:

- Vision-Language-Action and Robot Manipulation
- 3D Large Multimodal Models
- Navigation and Embodied AI
- Language-Embedded NeRF and Gaussian Fields
- 3D Vision-Language Grounding
- 3D Scene Graphs and Graph Reasoning
- Open-Vocabulary 3D Mapping
- 3D Reconstruction, Geometry, and SLAM
- Foundations: Transformers, VLMs, diffusion, 3D geometry, SLAM, RL, and robot policies

## Recommended Reading Paths

Start from the foundation papers if you are entering the area:

- Transformers and language models: Attention, BERT, GPT-style few-shot learning
- Vision-language models: CLIP, ViT, Segment Anything, DINOv2
- 3D representation: PointNet, NeRF, 3D Gaussian Splatting
- Geometry and SLAM: ORB-SLAM, DROID-SLAM, DUSt3R, MASt3R, VGGT
- Policy learning: Decision Transformer, Diffusion Policy, SayCan, RT-1, RT-2, PaLM-E, Open X-Embodiment

For robotics and VLA research:

- Read RT-1, RT-2, PaLM-E, OpenVLA, Octo, Diffusion Policy, PerAct, RVT, VoxPoser, ReKep.
- Then move to recent VLA papers from ICRA, ICML, ICLR, NeurIPS, ICCV, CoRL, RA-L, and IROS.

For 3D vision-language and embodied spatial reasoning:

- Start with ScanRefer, ReferIt3D, 3DVG-Transformer, 3D-VisTA, 3D-LLM, SpatialVLM, SceneVerse, Uni3DL, RoboSpatial.
- Then read open-vocabulary 3D mapping and Gaussian-language field papers such as LERF, CLIP-Fields, ConceptFusion, OpenScene, LangSplat, SceneSplat, ReasonGrounder, and related 3DGS works.

## Curation Policy

The collection follows these rules:

- 2024-current: broad coverage of relevant top-tier conference and journal papers where official or public PDFs are available.
- 2021-current: emphasis on highly cited or field-shaping papers.
- Foundational papers: included regardless of year when they define the underlying methods used by later work.
- Each paper should have a stable PDF, venue or arXiv page, and a consistent note structure.
- Venue year is not repeated in venue folder names because papers are already grouped by year.

## Maintenance Workflow

The survey is generated and checked through scripts under [survey_work](./survey_work).

Useful commands:

```bash
python3 survey_work/build_lit_survey.py
python3 survey_work/reorganize_paper_dirs.py
python3 survey_work/create_extra_eccv_iccv_ral_iros.py
```

The generated manifest is:

```text
survey_work/selected_papers.json
```

## Notes on Public Sharing

This repository is designed for literature management and personal research use.

If publishing the repository publicly, review publisher and conference copyright policies before redistributing downloaded PDFs. A safer public version may keep the markdown notes and replace local PDFs with official paper links.

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
