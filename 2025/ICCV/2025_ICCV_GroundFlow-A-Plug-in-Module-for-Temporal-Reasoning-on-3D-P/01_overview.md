# GroundFlow: A Plug-in Module for Temporal Reasoning on 3D Point Cloud Sequential Grounding

- Year/Venue: 2025 / ICCV
- Category: 3D Vision-Language Grounding
- Tags: 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_GroundFlow-A-Plug-in-Module-for-Temporal-Reasoning-on-3D-P/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Effectively retrieving relevant previous information is essential for solving this problem, yet current visual grounding methods lack a design for temporal fusion.
- Due to the lack of an effective module for collecting related historical information, state-of-theart 3DVG methods face significant challenges in adapting to the SG3D task.
- However, these methods are primarily designed for object-centric 3DVG tasks and face significant challenges when applied to sequential grounding tasks.

## Core Idea
- To fill this gap, we propose GroundFlow — a plug-in module for temporal reasoning on 3D point cloud sequential grounding.
- In summary, we make the following contributions: • We propose the GroundFlow module with a recurrent framework, which can be integrated into previous 3DVG baselines and introduce important ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- This allows GroundFlow to improve the 3DVG baseline methods consistently as task steps increases. • We achieve state-of-the-art performance on SG3D benchmark across five datasets without using large ...
- Firstly, we demonstrate that integrating GroundFlow improves the task accuracy of 3DVG baseline methods by a large margin (+7.5% and +10.2%) in the SG3D benchmark, even outperforming a ...
- While 3D LLMs achieve state-of-the-art results in various 3D tasks, they still face significant difficulty adapting to the complex SG3D problem .

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Training Objective Following the SG3D benchmark , we use the same cross-entropy loss to optimize the dual-stream model and the query-based model.
- This allows GroundFlow to improve the 3DVG baseline methods consistently as task steps increases. • We achieve state-of-the-art performance on SG3D benchmark across five datasets without using large ...
- While 3D LLMs achieve state-of-the-art results in various 3D tasks, they still face significant difficulty adapting to the complex SG3D problem .

## Abstract Cue
- T : Refresh yourself with a beverage T : Task Description P : 3D Point Cloud St : Step t’s Instruction Ot : Step t’s Target Object Grounding Sequences Sequential grounding in 3D point clouds (SG3D) refers to locating sequences of objects by following text ...
