# VGMamba: Attribute-to-Location Clue Reasoning for Quantity-Agnostic 3D Visual Grounding

- Year/Venue: 2025 / ICCV
- Category: 3D Vision-Language Grounding
- Tags: 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_VGMamba-Attribute-to-Location-Clue-Reasoning-for-Quantity/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Most existing methods often follow a two-stage process, i.e., ﬁrst detecting proposal objects and identifying the right objects based on the relevance to the given query.
- Recent studies have attempted to address this challenge by incorporating both object attributes (e.g., color, shape, texture) and spatial relationships (e.g., relative positions) to improve grounding accuracy.

## Core Idea
- Particularly, we propose a VGMamba network that consists of an SVD-based attribute mamba, location mamba, and multi-modal fusion mamba.
- Training Objectives Building on previous work , the loss of VGMamba consists of the 3D Visual Grounding loss Lref , text-object contrastive loss Lcon , and object detection ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experimental results demonstrate the superiority of our method.
- To achieve accurate 3D Visual Grounding, we explore two clues.
- Recent studies have attempted to address this challenge by incorporating both object attributes (e.g., color, shape, texture) and spatial relationships (e.g., relative positions) to improve grounding accuracy.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experimental results demonstrate the superiority of our method.
- Particularly, we propose a VGMamba network that consists of an SVD-based attribute mamba, location mamba, and multi-modal fusion mamba.
- In the experiment, our method is veriﬁed on four datasets.

## Abstract Cue
- 7KH EURZQ VRID EHVLGH WKH SODQW As an important direction of embodied intelligence, 3D Visual Grounding has attracted much attention, aiming to identify 3D objects matching the given language description.
