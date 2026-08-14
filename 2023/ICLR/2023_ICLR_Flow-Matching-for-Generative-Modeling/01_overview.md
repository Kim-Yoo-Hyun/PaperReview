# Flow Matching for Generative Modeling

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2023 / ICLR
- Category: Foundations: Generative Models
- Tags: Flow Matching, generative modeling, continuous normalizing flow, action generation
- Official paper: https://iclr.cc/virtual/2023/poster/11309
- Official PDF: https://openreview.net/pdf?id=PqvMRDCJT9t
- Code/Project: https://openreview.net/forum?id=PqvMRDCJT9t
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Why This Paper Is Here

DDPM에서 flow/velocity 기반 robot action model로 넘어가는 생성 모델 foundation.

## Problem

Continuous normalizing flow를 likelihood 계산이나 trajectory simulation 없이 대규모로 안정적으로 학습하는 방법이 필요하다.

## Core Idea

- 고정 conditional probability path의 vector field를 회귀하는 simulation-free objective를 정의한다.
- Diffusion path를 포함하는 Gaussian path family와 optimal-transport displacement path를 다룬다.
- 학습된 continuous normalizing flow를 ODE solver로 적분해 sample을 생성한다.

## Observation / State / Action Interface

입력은 time과 noisy sample/conditioning이며 출력은 probability path를 따르는 velocity field다. Robotics에서는 sample을 action chunk로 바꾸는 별도 conditioning과 control interface가 필요하다.

## Evaluation Scope

- 원 논문은 ImageNet generative modeling에서 likelihood와 sample quality를 평가한다.
- Robotics prerequisite로 읽되 robot success나 latency는 원 논문의 직접 평가 범위가 아니다.

## Limitations to Verify

- 이미지 생성 결과만으로 robot action의 dynamics/contact feasibility를 보장하지 않는다.
- ODE integration step과 conditioning 설계가 실제 control latency를 좌우한다.

## Reading Lineage

`DDPM → Flow Matching → π0 / flow-based robot policies`
