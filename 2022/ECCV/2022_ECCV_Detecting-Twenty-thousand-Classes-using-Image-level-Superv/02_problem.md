# Problem

- Year/Venue: 2022 / ECCV
- Category: Open-Vocabulary 3D Mapping
- Tags: Vision-Language Model, open-vocabulary, detection, semantic
- Paper link: ./2022/ECCV/2022_ECCV_Detecting-Twenty-thousand-Classes-using-Image-level-Superv/paper.pdf
- Code/Project: https://github.com/facebookresearch/Detic
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Object detection consists of two sub-problems - finding the object (localization) and naming it (classification).
- Traditional methods tightly couple these two subproblems and thus rely on box labels for all classes.
- Unlike prior work, Detic does not need complex assignment schemes to assign image labels to boxes based on model predictions, making it much easier to implement and compatible ...

## 해결하려는 문제
- It outperforms prior work on both open-vocabulary and long-tail detection benchmarks.
- Unlike prior work, Detic does not need complex assignment schemes to assign image labels to boxes based on model predictions, making it much easier to implement and compatible ...
- We propose Detic, which simply trains the classifiers of a detector on image classification data and thus expands the vocabulary of detectors to tens of thousands of concepts.

## 선행 연구 / 배경 단서
- Object detection consists of two sub-problems - finding the object (localization) and naming it (classification).
- Traditional methods tightly couple these two subproblems and thus rely on box labels for all classes.
