# OpenMask3D: Open-Vocabulary 3D Instance Segmentation

- Year/Venue: 2023 / NeurIPS
- Category: Open-Vocabulary 3D Mapping
- Tags: open-vocabulary, 3D segmentation, CLIP
- Paper link: ./2023/NeurIPS/2023_NeurIPS_OpenMask3D-Open-Vocabulary-3D-Instance-Segmentation/paper.pdf
- Code/Project: https://openmask3d.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Hence, the second key problem with closed-vocabulary approaches is their inherent limitation to recognize only object classes that are predefined at training time.
- We argue that there are two key problems with closed-vocabulary 3D instance segmentation.
- Our approach is intrinsically different from the existing 3D open-vocabulary scene understanding approaches as we propose an instance-based feature computation approach instead of a point-based one.

## Core Idea
- We propose OpenMask3D, the first open-vocabulary 3D instance 1 Our approach takes as input posed segmentation model.
- 4 Experiments In this section, we present quantitative and qualitative results from our method OpenMa

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments and ablation studies on ScanNet200 and Replica show that OpenMask3D outperforms other open-vocabulary methods, especially on the long-tail distribution.
- 4.1 Quantitative results: closed-vocabulary 3D instance segmentation evaluation We evaluate our approach on the closed-vocabulary 3D instance segmentation task.
- We report our ScanNet200 results on the validation set consisting of 312 scenes, and evaluate for the 3D instance segmentation task using the closed vocabulary of 200 categories ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experiments and ablation studies on ScanNet200 and Replica show that OpenMask3D outperforms other open-vocabulary methods, especially on the long-tail distribution.
- We introduce the task of open-vocabulary 3D instance segmentation.
- Qualitative experiments further showcase OpenMask3D’s ability to segment object properties based on free-form queries describing geometry, affordances, and materials.

## Abstract Cue
- We introduce the task of open-vocabulary 3D instance segmentation.
