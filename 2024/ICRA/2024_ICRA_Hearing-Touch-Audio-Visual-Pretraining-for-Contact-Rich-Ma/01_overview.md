# Hearing Touch: Audio-Visual Pretraining for Contact-Rich Manipulation

- Year/Venue: 2024 / ICRA
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, tactile sensing, audio-visual pretraining, contact-rich manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sites.google.com/view/hearing-touch
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- This gap arises due to the lack of relevant data at a comparable scale for tactile sensing.
- Prior work has already demonstrated the ability to use contact audio for manipulation tasks , , .

## Core Idea
- To the best of our knowledge, our method is the first approach leveraging largescale multisensory pre-training for robotic manipulation.
- We investigate how large-scale audio-visual training might be beneficial for le

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- INTRODUCTION Two key components consistently improve the performance of robotic manipulation: (1) pre-training on a large amount of data – and (2) using multisensory input, especially tactile sensing ...
- For supplementary information including videos of real robot experiments, please see https://sites.google.com/view/hearing-touch.
- Prior work has already demonstrated the ability to use contact audio for manipulation tasks , , .

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To the best of our knowledge, our method is the first approach leveraging largescale multisensory pre-training for robotic manipulation.
- INTRODUCTION Two key components consistently improve the performance of robotic manipulation: (1) pre-training on a large amount of data – and (2) using multisensory input, especially tactile sensing ...
- Our key insight is that contact microphones capture inherently audio-based information, allowing us to leverage large-scale audio-visual pretraining to obtain representations that boost the performance of robotic manipulation.

## Abstract Cue
- — Although pre-training on a large amount of data is beneficial for robot learning, current paradigms only perform large-scale pretraining for visual representations, whereas representations for other modalities are trained from scratch.
