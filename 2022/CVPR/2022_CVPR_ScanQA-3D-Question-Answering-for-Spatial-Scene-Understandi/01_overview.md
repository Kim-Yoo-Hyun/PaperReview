# ScanQA: 3D Question Answering for Spatial Scene Understanding

- Year/Venue: 2022 / CVPR
- Category: 3D Vision-Language Grounding
- Tags: 3D Vision, Vision-Language, grounding, 3D QA
- Paper link: ./2022/CVPR/2022_CVPR_ScanQA-3D-Question-Answering-for-Spatial-Scene-Understandi/paper.pdf
- Code/Project: https://github.com/ATR-DBI/ScanQA
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Given inputs of an entire 3D modeling and a linguistic question, models predict an answer phrase and the corresponding 3D-bounding boxes. suitcase located?”, the existing models based on ...
- Unlike the 2D-question answering of visual question answering, the conventional 2D-QA models suffer from problems with spatial understanding of object alignment and directions and fail in object localization ...

## Core Idea
- We propose a new 3D spatial understanding task for 3D question answering (3D-QA).
- We propose a baseline model for 3D-QA, called the ScanQA1 , which learns a fused descriptor from 3D object proposals and encoded sentence embeddings.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Introduction In recent years, significant advances have been achieved in vision-and-language tasks and datasets, and several new datasets have been created to develop models that understand textual expressions, ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We propose a new 3D spatial understanding task for 3D question answering (3D-QA).
- We propose a baseline model for 3D-QA, called the ScanQA1 , which learns a fused descriptor from 3D object proposals and encoded sentence embeddings.
- We introduce the new task of question answering for 3D modeling.

## Abstract Cue
- We propose a new 3D spatial understanding task for 3D question answering (3D-QA).
