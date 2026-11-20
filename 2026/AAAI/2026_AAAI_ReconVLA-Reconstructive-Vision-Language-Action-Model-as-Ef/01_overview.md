# ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Wenxuan Song, Ziyang Zhou, Han Zhao, Jiayi Chen, Pengxiang Ding, Haodong Yan, Yuxin Huang, Feilong Tang, Donglin Wang, Haoang Li
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, visual grounding, reconstruction, manipulation
- Aliases: ReconVLA
- Official paper: https://ojs.aaai.org/index.php/AAAI/article/view/38921
- Venue verification: https://ojs.aaai.org/index.php/AAAI/article/view/38921
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인. 직접 HTML 접근 제한은 공식 사이트의 검색 색인 abstract/BibTeX 및 저자 abstract/project 자료로 교차 확인; HTML 전면 열람으로 기록하지 않음.

## Problem and Importance

VLA의 attention이 실제 조작 대상 대신 관련 없는 영역에 분산될 수 있다.

## Core Idea and Contribution

시각 출력으로 target gaze 영역을 복원하는 diffusion transformer를 학습해 implicit grounding을 유도한다.

## Observation–State–Action Interface

언어·영상에서 action과 학습용 target-region reconstruction을 연결한다. 3D metric reconstruction 방법은 아니다.

## Evaluation Scope and Claim Boundary

공개 로봇 데이터 기반 사전학습과 simulation·실세계 조작 평가를 보고한다.

근거: [공식 paper/abstract](https://ojs.aaai.org/index.php/AAAI/article/view/38921). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

TASK-GEOMETRY의 이득이 단순 target attention/영역 supervision 때문인지 비교할 선행이다.

## Verification Boundary

Gaze-region label 생성·data overlap·loss weighting·추론 경로을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
