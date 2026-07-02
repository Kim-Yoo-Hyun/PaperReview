# 3D-VisTA: Pre-trained Transformer for 3D Vision and Text Alignment

- Year/Venue: 2023 / ICCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision-Language, alignment, Transformer
- Paper link: ./2023/ICCV/2023_ICCV_3D-VisTA-Pre-trained-Transformer-for-3D-Vision-and-Text-Al/paper.pdf
- Code/Project: https://3d-vista.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- ScanScribe contains 2,995 RGBD scans for 1,185 unique indoor scenes originating from ScanNet and 3R-Scan datasets, along with paired 278K scene descriptions generated from existing 3D-VL tasks, templates, ...

## Core Idea
- In this paper, we propose 3D-VisTA, a pre-trained Transformer for 3D Vision and Text Alignment that can be easily adapted to various downstream tasks.
- 3D-VisTA In this section, we introduce 3D-VisTA, a simple and unified Transformer for aligning 3D scenes and text.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- It achieves state-of-the-art results on various 3D-VL tasks, ranging from visual grounding and dense captioning to question answering and situated reasoning.
- Moreover, 3D-VisTA demonstrates superior data efficiency, obtaining strong performance even with limited annotations during downstream task fine-tuning.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this paper, we propose 3D-VisTA, a pre-trained Transformer for 3D Vision and Text Alignment that can be easily adapted to various downstream tasks.
- It achieves state-of-the-art results on various 3D-VL tasks, ranging from visual grounding and dense captioning to question answering and situated reasoning.
- Next On 3D scan Object Table On Floor GPT-3 Ask GPT Template Human Ask human ScanScribe dataset for 3D-VL pre-training (Large-scale scene-text pairs) 3D-VisTA: Pre-trained Transformer (Masked Language ...

## Abstract Cue
- 3D vision-language grounding (3D-VL) is an emerging field that aims to connect the 3D physical world with natural language, which is crucial for achieving embodied intelligence.
