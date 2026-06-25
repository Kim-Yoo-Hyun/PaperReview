# Grounding Image Matching in 3D with MASt3R

- Year/Venue: 2024 / ECCV
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: 3D geometry, matching, calibration
- Authors: Vincent Leroy, Yohann Cabon, Jérôme Revaud
- Paper: https://arxiv.org/abs/2406.09756
- PDF status: downloaded
- GitHub/Project: https://github.com/naver/mast3r

## Problem
현실의 3D reconstruction/SLAM은 calibration, pose, correspondence, temporal consistency가 불완전한 상태에서 metric geometry를 추정해야 한다.

## Core Idea
핵심은 transformer, pointmap, dense matching, SLAM optimization, 또는 3DGS를 사용해 pose/depth/shape를 한 표현 안에서 일관되게 추정하는 것이다.

## Paper-Specific Cues
- Topic cue: Image Matching is a core component of all best-performing algorithms and pipelines in 3D vision.
- Method cue: We introduce a fast reciprocal matching scheme that not only accelerates matching by orders of magnitude, but also comes with theoretical guarantees and, lastly, ...
- Result cue: We aim here to improve the matching capabilities of such an approach while preserving its robustness.

## Input / Output
Input: 3D scene representation plus free-form natural language. Output: target object, 3D box, mask, or referring expression result.

## Main Claims
- 논문은 `3D reconstruction, calibration, and geometric consistency`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
강한 benchmark 성능이 실제 로봇 센서 노이즈, rolling shutter, 동적 객체, 저조도 환경까지 보장하지는 않는다.

## Contribution
- 3D reconstruction, calibration, and geometric consistency 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: 3D geometry, matching, calibration.
- 초록에서 확인되는 주요 cue: Image, Matching, Yet, This, DUSt3R, Transformers, Based, Extensive.
