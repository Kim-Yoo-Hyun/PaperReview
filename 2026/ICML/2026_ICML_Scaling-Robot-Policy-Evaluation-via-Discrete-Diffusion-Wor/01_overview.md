# Scaling Robot Policy Evaluation via Discrete Diffusion World Model

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICML
- Authors: Yaxuan Li, Junjie Wen, Zhongyi Zhou, Yefei Chen, Chaomin Shen, Yaxin Peng, Yichen Zhu
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: world model, discrete diffusion, policy evaluation, policy ranking
- Aliases: dWorldEval, dWorldEval: Scalable Robotic Policy Evaluation via Discrete Diffusion World Model
- Official paper: https://proceedings.mlr.press/v306/li26hi.html
- Venue verification: https://proceedings.mlr.press/v306/li26hi.html
- Code/Project: https://dworldeval.github.io/
- Code: project_only
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다. 공식 final title과 preprint/project title을 alias로 통합했으며 본문 동등성은 미검증이다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

dWorldEval은 이산 확산 세계 모델이 정책 실행의 미래 관측과 진행 상황을 예측하도록 학습해 로봇 정책을 평가한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/li26hi/li26hi.pdf#page=1)

## Core Idea and Contribution

- 영상·지시·행동을 토큰으로 처리하는 모델에 과거 핵심 프레임을 제공하고 미래 관측과 과제 진행도를 함께 예측한다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/li26hi/li26hi.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/li26hi/li26hi.pdf#page=4)
- LIBERO와 RoboTwin 및 실제 로봇에서 모델이 추정한 정책 간 성능 순위와 직접 실행으로 얻은 순위의 일치도를 평가했다. [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/li26hi/li26hi.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/li26hi/li26hi.pdf#page=8)

## Observation–State–Action Interface

관측·언어·action chunk → 미래 관측·성공 지표 → policy ranking.

## Evaluation Scope and Claim Boundary

LIBERO·RoboTwin 및 real-robot task 기반 평가를 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v306/li26hi.html) · [저자 project/code](https://dworldeval.github.io/). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

World-model 평가를 연구할 때 시각 품질과 행동별 순위 신뢰도를 구분할 직접 비교군이다.

## Verification Boundary

성공 평가기 독립성, 실패 데이터, final/preprint 차이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 원문 대조

이산 확산 세계 모델이 생성한 결과로 여러 정책의 순위를 추정한다. 원래 WorldEval의 공개 파일은 이 논문에 귀속하지 않았다. [방법과 평가](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/li26hi/li26hi.pdf#page=8)
