# Causal World Modeling for Robot Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Problem and Bottleneck

미래 영상 예측과 실제 행동 생성·feedback을 같은 모델 안에서 다룬다.

## Formulation and Robotics Loop

영상·행동 이력 → 인과적 생성 sequence → 미래 영상·robot action.

RSS abstract의 CauVA는 autoregressive MoT로 frame/action을 처리하고 KV history와 noisy latent augmentation을 사용한다.

## Assumptions to Verify

예측/행동 gradient 경로·추론 history·실제 피드백·버전별 모델 명칭.

위 항목은 연구자의 확인 질문이며 논문이 명시한 가정·실패로 확정한 것이 아니다.

## Prior Work and Why It Matters

영상 world model·Diffusion Policy → frame/action 공동 모델 → 단일 VLA RL과의 목적함수 차이.

Architecture 통합과 RL 공동 갱신을 구별할 world-action 비교 대상으로 보완한다.

## Evidence Boundary

[공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p016.html). 공식 RSS abstract만을 canonical scope로 사용한다. 같은 제목의 arXiv2601.21998은 LingBot-VA와 다른 저자 구성·설계를 표기하므로 version mapping을 확정하지 않았고 arXiv ID/code를 자동 합치지 않았다. 별도 중복 등록도 하지 않았다.
