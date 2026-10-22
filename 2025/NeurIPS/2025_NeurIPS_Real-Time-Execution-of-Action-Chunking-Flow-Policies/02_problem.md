# Real-Time Execution of Action Chunking Flow Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

무거운 flow policy의 추론 지연 때문에 action chunk 연결이 끊긴다.

## Bottleneck and Changed Formulation

실행이 확정된 prefix를 보존하며 남은 action을 inpainting하는 비동기 추론을 사용한다.

## System and Robotics Loop

새 관측·이전 chunk·지연 → prefix 제약 → 다음 chunk.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

prefix 길이, delay estimate, inpainting cost, simulator와 VLA 범위.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Kinetix 실험과 실제 π0.5 양팔 평가를 구분해 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://papers.nips.cc/paper_files/paper/2025/hash/300ccb2187dedd4edcc07f7e76d8e553-Abstract-Conference.html) · [저자 project/code](https://pi.website/research/real_time_chunking). Exact objective, constraints, success definition은 본문 수동 확인 필요.
