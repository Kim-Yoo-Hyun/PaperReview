# MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2024 / ACM Transactions on Graphics
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, whole-body control, motion imitation, NVIDIA
- Official paper: https://research.nvidia.com/labs/par/maskedmimic/
- Code/Project: https://research.nvidia.com/labs/par/maskedmimic/
- Source audit: official NVIDIA project/publication page checked; architecture and benchmark details remain UNVERIFIED.

## Why This Paper Is Here

partial motion constraints를 masked inpainting으로 통합해 다양한 humanoid control modality를 하나의 policy로 다루는 주요 whole-body lineage다.

## Problem

full motion tracking, sparse keypoints, text/object goals 등 서로 다른 control tasks를 별도 specialist 없이 처리한다.

## Core Idea

motion state의 임의 부분을 mask하고 conditioned physics policy가 missing motion을 생성·추종하도록 학습한다.

## Interface

partial motion/task constraints와 humanoid state를 joint-level whole-body actions로 매핑한다.

## Evaluation Scope

여러 conditioning modality와 large motion corpus의 physics-based control을 평가한다.
