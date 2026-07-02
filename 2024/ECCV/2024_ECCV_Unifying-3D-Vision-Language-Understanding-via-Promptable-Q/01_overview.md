# Unifying 3D Vision-Language Understanding via Promptable Queries

- Year/Venue: 2024 / ECCV
- Category: 3D Large Multimodal Models
- Tags: Vision-Language Model, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_Unifying-3D-Vision-Language-Understanding-via-Promptable-Q/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, a considerable gap exists between existing methods and such a unified model, due to the independent application of representation and insufficient exploration of 3D multi-task training.

## Core Idea
- In this section, we present PQ3D, which consists of three main modules: Task Prompt Encoding, 3D Scene Encoding, and Prompt-guided Query Learning, as depicted in Fig.
- In this paper, we introduce PQ3D, a unified model capable of using Promptable Queries to tackle a wide range of 3D-VL tasks, from low-level instance segmentation to high-level ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- This is achieved through three key innovations: (1) unifying various 3D scene representations (i.e., voxels, point clouds, multi-view images) into a shared 3D coordinate space by segment-level grouping, ...
- Particularly, PQ3D improves the state-ofthe-art on ScanNet200 by 4.9% (AP25), ScanRefer by 5.4% (acc@0.5), Multi3DRefer by 11.7% (F1@0.5), and Scan2Cap by 13.4% (CIDEr@0.5).
- Tested across ten diverse 3D-VL datasets, PQ3D demonstrates impressive performance on these tasks, setting new records on most benchmarks.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- This is achieved through three key innovations: (1) unifying various 3D scene representations (i.e., voxels, point clouds, multi-view images) into a shared 3D coordinate space by segment-level grouping, ...
- However, a considerable gap exists between existing methods and such a unified model, due to the independent application of representation and insufficient exploration of 3D multi-task training.
- In this paper, we introduce PQ3D, a unified model capable of using Promptable Queries to tackle a wide range of 3D-VL tasks, from low-level instance segmentation to high-level ...

## Abstract Cue
- A unified model for 3D vision-language (3D-VL) understanding is expected to take various scene representations and perform a wide range of tasks in a 3D scene.
