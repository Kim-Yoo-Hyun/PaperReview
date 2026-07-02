# Detecting Twenty-thousand Classes using Image-level Supervision

- Year/Venue: 2022 / ECCV
- Category: Open-Vocabulary 3D Mapping
- Tags: Vision-Language Model, open-vocabulary, detection, semantic
- Paper link: ./2022/ECCV/2022_ECCV_Detecting-Twenty-thousand-Classes-using-Image-level-Superv/paper.pdf
- Code/Project: https://github.com/facebookresearch/Detic
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Object detection consists of two sub-problems - finding the object (localization) and naming it (classification).
- Traditional methods tightly couple these two subproblems and thus rely on box labels for all classes.
- Unlike prior work, Detic does not need complex assignment schemes to assign image labels to boxes based on model predictions, making it much easier to implement and compatible ...

## Core Idea
- We propose Detic, which simply trains the classifiers of a detector on image classification data and thus expands the vocabulary of detectors to tens of thousands of concepts.
- Object detection consists of two sub-problems - finding the object (localization) and naming it (classification).

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our results show that Detic yields excellent detectors even for classes without box annotations.
- It outperforms prior work on both open-vocabulary and long-tail detection benchmarks.
- We mainly use the open-vocabulary setting proposed by Gu et al. , and also report results on the standard LVIS setting.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- It outperforms prior work on both open-vocabulary and long-tail detection benchmarks.
- Unlike prior work, Detic does not need complex assignment schemes to assign image labels to boxes based on model predictions, making it much easier to implement and compatible ...
- We propose Detic, which simply trains the classifiers of a detector on image classification data and thus expands the vocabulary of detectors to tens of thousands of concepts.

## Abstract Cue
- Current object detectors are limited in vocabulary size due to the small scale of detection datasets.
