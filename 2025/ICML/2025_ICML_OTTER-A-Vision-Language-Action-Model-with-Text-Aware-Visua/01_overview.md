# OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction

- Year/Venue: 2025 / ICML Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2025/ICML/2025_ICML_OTTER-A-Vision-Language-Action-Model-with-Text-Aware-Visua/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- We propose OTTER, a novel VLA architecture that leverages these existing alignments through explicit, text-aware visual feature extraction.
- This approach requires the policy network to connect the vision and language information and conduct precise robot control, which often presents significant challenges, especially in unseen environments.
- Existing approaches require fine-tuning pre-trained visionlanguage models (VLMs) as visual and language features are independently fed into downstream policies, degrading the pre-trained semantic alignments.

## Core Idea
- We propose OTTER, a novel VLA architecture that leverages these existing alignments through explicit, text-aware visual feature extraction.
- More details about model training and architectures are in Appendix B.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- In simulation and real-world experiments, OTTER significantly outperforms existing VLA models, demonstrating strong zeroshot generalization to novel objects and environments.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We propose OTTER, a novel VLA architecture that leverages these existing alignments through explicit, text-aware visual feature extraction.
- In simulation and real-world experiments, OTTER significantly outperforms existing VLA models, demonstrating strong zeroshot generalization to novel objects and environments.
- Thereby, OTTER preserves and utilizes the rich semantic understanding learned from large-scale pre-training, enabling strong zero-shot generalization capabilities.

## Abstract Cue
- Vision-Language-Action (VLA) models aim to predict robotic actions based on visual observations and language instructions.
