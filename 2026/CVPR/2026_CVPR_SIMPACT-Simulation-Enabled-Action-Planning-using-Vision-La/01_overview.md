# SIMPACT: Simulation-Enabled Action Planning using Vision-Language Models

- Year/Venue: 2026 / CVPR
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLM, Planning, simulation
- Paper link: ./2026/CVPR/2026_CVPR_SIMPACT-Simulation-Enabled-Action-Planning-using-Vision-La/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- This limitation arises from training VLMs on static internet-scale visual-language data that contain no causal interactions or action-conditioned changes.
- However, they lack a grounded understanding of physical dynamics.
- Our method demonstrates state-of-the-art performance on seven challenging, real-world rigid-body and deformable manipulation tasks that require fine-grained physical reasoning, outperforming existing general-purpose robotic manipulation models.

## Core Idea
- To overcome this, we present SIMPACT, a test-time, SIMulation-enabled ACTion Planning framework that equips VLMs with physical reasoning through simulation-in-the-loop world modeling, without requiring any additional training.
- Success rates (%) over 10 trials for each task after removing each component of our method.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our method demonstrates state-of-the-art performance on seven challenging, real-world rigid-body and deformable manipulation tasks that require fine-grained physical reasoning, outperforming existing general-purpose robotic manipulation models.
- Our results demonstrate that embedding physics understanding via efficient simulation into VLM reasoning at test time offers a promising path towards generalizable embodied intelligence.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our method demonstrates state-of-the-art performance on seven challenging, real-world rigid-body and deformable manipulation tasks that require fine-grained physical reasoning, outperforming existing general-purpose robotic manipulation models.
- To overcome this, we present SIMPACT, a test-time, SIMulation-enabled ACTion Planning framework that equips VLMs with physical reasoning through simulation-in-the-loop world modeling, without requiring any additional training.
- This limitation arises from training VLMs on static internet-scale visual-language data that contain no causal interactions or action-conditioned changes.

## Abstract Cue
- Vision-Language Models (VLMs) exhibit remarkable common-sense and semantic reasoning capabilities.
