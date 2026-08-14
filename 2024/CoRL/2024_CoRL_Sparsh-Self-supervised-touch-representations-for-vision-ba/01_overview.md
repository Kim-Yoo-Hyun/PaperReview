# Sparsh: Self-supervised touch representations for vision-based tactile sensing

- Year/Venue: 2024 / CoRL
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, tactile sensing, self-supervised learning, foundation model, contact
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sparsh-ssl.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Specifically, we provide a recipe to adapt masking-based objectives from computer vision to the tactile domain, and train general-purpose touch encoders by curating a new Touch-Slide dataset and ...
- Pulling together additional unlabeled data points from the existing datasets we train our models on a total of 460k+ tactile images.
- For instance, properties like forces and slip require careful and expensive instrumentation in lab settings, while other properties like tracking deformations or extrinsic contact can be infeasible.

## Core Idea
- We present Sparsh, a family of SSL models that can support various vision-based tactile sensors, alleviating the need for custom labels through pre-training on 460k+ tactile images with ...
- In this work, we introduce a family of touch representations for vision-based tactile sensors trained with SSL.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- In evaluations, we find that SSL pre-training for touch representation outperforms task and sensor-specific end-to-end training by 95.1% on average over TacBench, and Sparsh (DINO) and Sparsh (IJEPA) ...
- To tackle this we turn to self-supervised learning (SSL) that has demonstrated remarkable performance in computer vision.
- We also build TacBench, to facilitate standardized benchmarking across sensors and models, comprising of six tasks ranging from comprehending tactile properties to enabling physical perception and manipulation planning.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We present Sparsh, a family of SSL models that can support various vision-based tactile sensors, alleviating the need for custom labels through pre-training on 460k+ tactile images with ...
- In evaluations, we find that SSL pre-training for touch representation outperforms task and sensor-specific end-to-end training by 95.1% on average over TacBench, and Sparsh (DINO) and Sparsh (IJEPA) ...
- : In this work, we introduce general purpose touch representations for the increasingly accessible class of vision-based tactile sensors.

## Abstract Cue
- : In this work, we introduce general purpose touch representations for the increasingly accessible class of vision-based tactile sensors.
