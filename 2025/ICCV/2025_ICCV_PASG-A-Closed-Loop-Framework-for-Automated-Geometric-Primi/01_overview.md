# PASG: A Closed-Loop Framework for Automated Geometric Primitive Extraction and Semantic Anchoring in Robotic Manipulation

- Year/Venue: 2025 / ICCV
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, semantic
- Paper link: ./2025/ICCV/2025_ICCV_PASG-A-Closed-Loop-Framework-for-Automated-Geometric-Primi/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- The fragmentation between high-level task semantics and low-level geometric features remains a persistent challenge in robotic manipulation.
- While vision-language models (VLMs) have shown promise in generating affordanceaware visual representations, the lack of semantic grounding in canonical spaces and reliance on manual annotations severely limit their ...

## Core Idea
- To address these, we propose Primitive-Aware Semantic Grounding (PASG), a closed ReKep CoPa OmniManip FUNCTO Robotwin Geometric Primitives Keypoints Keypoints, Function Axes Keypoints, Main Axes Keypoints, Function Axes ...
- OmniManip employs computational constraint optimization and scene rendering for VLM validation, while our method directly detects annotation-primitive misalignment for efficient self-correction. addresses this limitation by proposing direction-aware spatial ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- PASG achieves a finer-grained semantic-affordance understanding of objects, establishing a unified paradigm for bridging geometric primitives with task semantics in robotic manipulation.
- We demonstrate PASG’s effectiveness in practical robotic manipulation tasks across diverse scenarios, achieving performance comparable to manual annotations.
- While vision-language models (VLMs) have shown promise in generating affordanceaware visual representations, the lack of semantic grounding in canonical spaces and reliance on manual annotations severely limit their ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To address these, we propose Primitive-Aware Semantic Grounding (PASG), a closed
- While vision-language models (VLMs) have shown promise in generating affordanceaware visual representations, the lack of semantic grounding in canonical spaces and reliance on manual annotations severely limit their ...
- PASG achieves a finer-grained semantic-affordance understanding of objects, establishing a unified paradigm for bridging geometric primitives with task semantics in robotic manipulation.

## Abstract Cue
- loop framework that introduces: (1) Automatic primitive extraction through geometric feature aggregation, enabling cross-category detection of keypoints and axes; (2) VLM-driven semantic anchoring that dynamically couples geometric primitives with functional affordances and task-relevant description; (3) A spatial-semantic reasoning benchmark and a fine-tuned VLM (Qwen2.5VL-PA).
