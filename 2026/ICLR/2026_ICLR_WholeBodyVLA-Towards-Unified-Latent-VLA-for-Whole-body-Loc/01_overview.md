# WholeBodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICLR
- Authors: Haoran Jiang, Jin Chen, Qingwen Bu, Li Chen, Modi Shi, Yanjie Zhang, Delong Li, Chuanzhe Suo, wang chuang, zhihui peng, Hongyang Li
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: VLA, mobile-manipulation, control-interface
- Aliases:
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/ff7373914a96956f2a7cacbdf3b0b8d8-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2026/hash/ff7373914a96956f2a7cacbdf3b0b8d8-Abstract-Conference.html
- Code/Project: https://wholebodyvla.github.io/
- Code: https://github.com/OpenDriveLab/WholebodyVLA
- Source audit: 2026-10-21: official abstract / author project 확인. 5개 note는 abstract 기반이며 사용자 정독을 의미하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

WholeBodyVLA는 행동 라벨이 없는 1인칭 영상에서 배운 조작·이동 표현과 휴머노이드 전신 제어기를 결합한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/ff7373914a96956f2a7cacbdf3b0b8d8-Paper-Conference.pdf#page=1)

## Core Idea and Contribution

- 영상의 잠재 행동을 학습하는 경로와 전진·선회·웅크리기 명령을 정밀하게 따르도록 훈련한 강화학습 제어기를 설계했다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/ff7373914a96956f2a7cacbdf3b0b8d8-Paper-Conference.pdf#page=1) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/ff7373914a96956f2a7cacbdf3b0b8d8-Paper-Conference.pdf#page=5)
- 실제 AgiBot X2의 이동 조작 과제와 제어기 설계 제거 실험에서 명령 추종과 과제 수행을 평가했다. [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/ff7373914a96956f2a7cacbdf3b0b8d8-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/ff7373914a96956f2a7cacbdf3b0b8d8-Paper-Conference.pdf#page=9)

## Observation–State–Action Interface

시각·언어 → 상체 action·locomotion command → whole-body control.

## Evaluation Scope and Claim Boundary

Humanoid loco-manipulation과 확장 task를 보고한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ff7373914a96956f2a7cacbdf3b0b8d8-Abstract-Conference.html) · [저자 project/code](https://wholebodyvla.github.io/). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

NaVILA 이후 VLA와 low-level RL의 역할을 비교할 NEXT다.

## Verification Boundary

실행 가능한 codebase, latent supervision, controller budget을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
