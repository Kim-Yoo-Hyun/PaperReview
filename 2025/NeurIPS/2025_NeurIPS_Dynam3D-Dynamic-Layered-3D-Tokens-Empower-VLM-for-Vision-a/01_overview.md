# Dynam3D: Dynamic Layered 3D Tokens Empower VLM for Vision-and-Language Navigation

- Year/Venue: 2025 / NeurIPS Oral
- Category: Navigation and Embodied AI
- Tags: Vision-Language Model, 3D Vision, Navigation
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Dynam3D-Dynamic-Layered-3D-Tokens-Empower-VLM-for-Vision-a/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- We propose Dynam3D to alleviate the limitations mentioned above.
- Despite these recent advances, several limitations still remain: 1) Video-based models struggle to capture spatial geometry and semantics in large-scale 3D environments.
- A 3D instance merging discriminator aligns 2D instances with existing 3D instances based on geometry and semantics to enable dynamic updates of 3D instance representations.

## Core Idea
- To address these limitations, we propose Dynam3D, a dynamic layered 3D representation model that leverages language-aligned, generalizable, and hierarchical 3D representations as visual input to train 3D-VLM in ...
- To memorize the geometry and semantics of 3D environments, we follow HNR and g3D-LF in using CLIP-ViT-L/14@336px as the encoder for RGB images to extract 2D patch features ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Compared to prior state-of-the-art methods, e.g., g3D-LF and Uni-NaVid, our Dynam3D achieves an improvement of nearly 5% in navigation success rate (SR).
- Our Dynam3D still demonstrates substantial improvements, outperforming NaVid by over 13% in Success Rate (SR) on REVERIE-CE and by over 5% on NavRAG-CE.
- Methods LLM CM2 WS-MGMap InstructNav∗ AO-Planner∗ NaVid VLN-3DFF g3D-LF Uni-NaVid Dynam3D (Ours) × × ✓ ✓ ✓ × × ✓ ✓ 4.2 R2R-CE Val R2R-CE Test NE↓ OSR↑ ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- By leveraging large-scale 3D-language pretraining and task-specific adaptation, our Dynam3D sets new state-of-the-art performance on VLN benchmarks including R2R-CE, REVERIE-CE and NavRAG-CE under monocular settings.
- To address these limitations, we propose Dynam3D, a dynamic layered 3D representation model that leverages language-aligned, generalizable, and hierarchical 3D representations as visual input to train 3D-VLM in ...
- Furthermore, experiments for pre-exploration, lifelong memory, and real-world robot validate the effectiveness of practical deployment.

## Abstract Cue
- Vision-and-Language Navigation (VLN) is a core task where embodied agents leverage their spatial mobility to navigate in 3D environments toward designated destinations based on natural language instructions.
