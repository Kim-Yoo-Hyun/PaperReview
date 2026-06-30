# SAM 2: Segment Anything in Images and Videos

- Year/Venue: 2025 / ICLR
- Category: Foundations: Vision Foundation Models
- Tags: segmentation, foundation model, prompting, video segmentation, memory
- Authors: Nikhila Ravi, Valentin Gabeur, Yuan-Ting Hu, Ronghang Hu, Chaitanya Ryali, Tengyu Ma, Haitham Khedr, Roman Radle, Chloe Rolland, Laura Gustafson, Eric Mintun, Junting Pan, Kalyan Vasudev Alwala, Nicolas Carion, Chao-Yuan Wu, Ross Girshick, Piotr Dollar, Christoph Feichtenhofer
- Paper: https://openreview.net/forum?id=Ha6RTeWMd0
- PDF: https://proceedings.iclr.cc/paper_files/paper/2025/file/45c1f6a8cbf2da59ebf2c802b4f742cd-Paper-Conference.pdf
- arXiv: https://arxiv.org/abs/2408.00714
- GitHub/Project: https://github.com/facebookresearch/sam2
- Project page: https://ai.meta.com/research/sam2/
- PDF status: downloaded

## Problem
SAM은 promptable image segmentation을 foundation task로 만든 핵심 논문이지만, 실제 로봇/AR/자율주행/동영상 편집 환경에서는 객체가 움직이고 가려지고 다시 등장한다. 이미지 단일 프레임 segmentation만으로는 temporal consistency, object permanence, long video interaction을 처리하기 어렵다.

## Core Idea
SAM 2는 이미지를 1-frame video로 보고, image/video segmentation을 하나의 promptable visual segmentation(PVS) task로 통합한다. 핵심은 SAM 스타일 prompt encoder/mask decoder에 streaming memory를 붙여, 이전 prompt와 mask prediction을 memory bank에 저장하고 현재 frame feature가 memory attention으로 이를 참조하게 만드는 것이다.

## Input / Output
- Input: image 또는 video frames, point/box/mask prompts on one or multiple frames.
- Output: single-frame mask 또는 video 전체의 spatio-temporal masklet.
- Runtime setting: streaming frame processing, interactive refinement with additional prompts.

## Main Claims
- SAM 2는 image와 video를 하나의 promptable segmentation model로 처리한다.
- video segmentation에서 기존 강한 baseline보다 더 적은 interaction으로 더 높은 accuracy를 얻는다.
- image segmentation에서도 SAM보다 더 빠르고 정확한 zero-shot performance를 보인다.
- SA-V는 기존 VOS dataset보다 훨씬 큰 open-source video segmentation dataset이며, object/part/occlusion/reappearance를 폭넓게 포함한다.

## Limitation
- still 2D mask foundation model이라 metric 3D geometry, depth, pose, physical affordance는 직접 모델링하지 않는다.
- prompt quality와 object ambiguity에 영향을 받으며, long video에서는 memory error accumulation이 후속 연구의 주요 문제로 남는다.
- training data와 compute 규모가 크고, 실제 robot perception으로 쓰려면 camera motion, blur, domain shift, multi-view consistency를 별도로 검증해야 한다.

## Contribution
- Promptable Visual Segmentation(PVS) task를 image/video 통합 task로 정의.
- streaming memory 기반 SAM 2 architecture 제안.
- model-in-the-loop data engine으로 SA-V dataset 구축.
- video/image zero-shot segmentation에서 foundation baseline을 갱신.
- 3D CV/Robotics 관점에서는 open-vocabulary 2D mask prior, video-consistent object tracking prior, 2D-to-3D semantic map distillation의 foundation 역할을 한다.
