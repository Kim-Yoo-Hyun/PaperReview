# OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting

- Year/Venue: 2026 / CVPR
- Category: Open-Vocabulary 3D Mapping
- Tags: Gaussian Splatting, semantic mapping, open-vocabulary
- Paper link: ./2026/CVPR/2026_CVPR_OnlinePG-Online-Open-Vocabulary-Panoptic-Mapping-with-3D-G/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, existing methods are predominantly offline or lack instance-level understanding, limiting their applicability to real-world robotic tasks.
- Despite previous approaches that combine VLMs with 3DGS having yielded satisfactory performance, two critical limitations remain: 1) offline reconstruction and perception settings.
- Most existing reconstruction and understanding methods require pre-collected data.

## Core Idea
- In this paper, we propose OnlinePG, a novel and effective system that integrates geometric reconstruction and open-vocabulary perception using 3D Gaussian Splatting in an online setting.
- While a performance gap remains compared to offline methods that use ground truth point clouds and capture global multi-view information, our method substantially narrows this gap.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Building on differentiable rendering techniques such as Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) , several methods have achieved impressive results in fine-grained open-vocabulary scene understanding.
- Technically, to achieve online panoptic mapping, we employ an efficient local-to-global paradigm with a sliding window.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Building on differentiable rendering techniques such as Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) , several methods have achieved impressive results in fine-grained open-vocabulary scene understanding.
- In this paper, we propose OnlinePG, a novel and effective system that integrates geometric reconstruction and open-vocabulary perception using 3D Gaussian Splatting in an online setting.
- Subsequently, to update the global map, we construct explicit and fuse them into the global map via robust bidirectional bipartite 3D Gaussian instance matchi

## Abstract Cue
- Open-vocabulary 3D scene understanding is fundamental for embodied tasks, enabling robots to perceive, reason about, and interact with complex environments using natural language and instruction .
