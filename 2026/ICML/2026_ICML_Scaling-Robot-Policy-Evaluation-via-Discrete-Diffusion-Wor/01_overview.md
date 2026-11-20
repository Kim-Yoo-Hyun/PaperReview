# Scaling Robot Policy Evaluation via Discrete Diffusion World Model

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Yaxuan Li, Junjie Wen, Zhongyi Zhou, Yefei Chen, Chaomin Shen, Yaxin Peng, Yichen Zhu
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, evaluation, robustness
- Aliases: dWorldEval, dWorldEval: Scalable Robotic Policy Evaluation via Discrete Diffusion World Model
- Official paper: https://proceedings.mlr.press/v306/li26hi.html
- Venue verification: https://proceedings.mlr.press/v306/li26hi.html
- Code/Project: https://dworldeval.github.io/
- Code: project_only
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다. 공식 final title과 preprint/project title을 alias로 통합했으며 본문 동등성은 미검증이다.

## Problem and Importance

World model이 실패를 정상 장면으로 보정하면 policy 평가와 순위가 왜곡된다.

## Core Idea and Contribution

Action을 unified token으로 다루는 discrete diffusion과 keyframe memory·progress 출력을 결합한다.

## Observation–State–Action Interface

관측·언어·action chunk → 미래 관측·성공 지표 → policy ranking.

## Evaluation Scope and Claim Boundary

LIBERO·RoboTwin 및 real-robot task 기반 평가를 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v306/li26hi.html) · [저자 project/code](https://dworldeval.github.io/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

World-model 평가를 연구할 때 시각 품질과 행동별 순위 신뢰도를 구분할 직접 비교군이다.

## Verification Boundary

성공 평가기 독립성, 실패 데이터, final/preprint 차이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
