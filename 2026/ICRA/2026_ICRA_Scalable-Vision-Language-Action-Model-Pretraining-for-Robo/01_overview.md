# Scalable Vision-Language-Action Model Pretraining for Robotic Dexterous Manipulation with Real-Life Human Activity Videos

- Year/Venue: 2026 / ICRA
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2026/ICRA/2026_ICRA_Scalable-Vision-Language-Action-Model-Pretraining-for-Robo/paper.pdf
- Code/Project: not identified from venue audit
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Existing Vision-Language-Action data for robotic manipulation are typically collected in laboratory settings through human teleoperations .
- Although such robot action data is invaluable, its high acquisition cost significantly limits both the scale of the collected data and its diversity in skills, object categories, and ...
- Treating human hand as dexterous robot end-effector, we show that “inthe-wild” egocentric human videos without any annotations can be transformed into data formats fully aligned with existing robotic ...

## Core Idea
- Our model consists of a VLM backbone and a diffusion action expert.
- We use PaliGemma-2 as the VLM, which combines a SigLIP vision encoder with linear projection for alignment and a Gemma-2 language model for multi-modal token processing.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Additionally, fine-tuning it on a small amount of real robot action data significantly improves task success rates and generalization to novel objects in real robotic experiments.
- Our dataset achieves higher values on both metrics compared to the other datasets.
- This is achieved by the development of a fully-automated holistic human activity analysis approach for arbitrary human hand videos.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Treating human hand as dexterous robot end-effector, we show that “inthe-wild” egocentric human videos without any annotations can be transformed into data formats fully aligned with existing robotic ...
- We also demonstrate the appealing scaling behavior of the model’s task performance with respect to pretraining data scale.
- This training data covers a wide range of objects and concepts, dexterous manipulation tasks, and environment variations in real life, vastly exceeding the coverage of existing robot data.

## Abstract Cue
- This paper presents a novel approach for pretraining robotic manipulation Vision-LanguageAction (VLA) models using a large corpus of unscripted real-life video recordings of human hand activities.
