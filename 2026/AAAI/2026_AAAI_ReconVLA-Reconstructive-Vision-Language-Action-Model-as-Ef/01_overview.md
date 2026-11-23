# ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / AAAI
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
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인. 직접 HTML 접근 제한은 공식 사이트의 검색 색인 abstract/BibTeX 및 저자 abstract/project 자료로 교차 확인; HTML 전면 열람으로 기록하지 않음. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

ReconVLA는 로봇 정책이 영상에서 조작 대상에 집중하도록 해당 물체 영역을 복원하는 보조 목표로 시각 표현을 학습한다. [PDF 1쪽](https://ojs.aaai.org/index.php/AAAI/article/download/38921/42883#page=1)

## Core Idea and Contribution

- 정책의 시각 토큰에 조건화된 확산 트랜스포머가 목표 영역을 복원하게 하고, 기존 로봇 궤적에서 해당 영역이 표시된 사전학습 예시를 구성한다. [PDF 3쪽](https://ojs.aaai.org/index.php/AAAI/article/download/38921/42883#page=3) · [PDF 4쪽](https://ojs.aaai.org/index.php/AAAI/article/download/38921/42883#page=4)
- CALVIN과 실물 조작에서 목표 영역 복원 학습이 주의 분포와 조작 성공에 미치는 영향을 측정하고 새로운 대상에 대한 일반화도 평가했다. [PDF 5쪽](https://ojs.aaai.org/index.php/AAAI/article/download/38921/42883#page=5) · [PDF 6쪽](https://ojs.aaai.org/index.php/AAAI/article/download/38921/42883#page=6) · [PDF 7쪽](https://ojs.aaai.org/index.php/AAAI/article/download/38921/42883#page=7)

## Observation–State–Action Interface

언어·영상에서 action과 학습용 target-region reconstruction을 연결한다. 3D metric reconstruction 방법은 아니다.

## Evaluation Scope and Claim Boundary

공개 로봇 데이터 기반 사전학습과 simulation·실세계 조작 평가를 보고한다.

근거: [공식 paper/abstract](https://ojs.aaai.org/index.php/AAAI/article/view/38921). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

TASK-GEOMETRY의 이득이 단순 target attention/영역 supervision 때문인지 비교할 선행이다.

## Verification Boundary

Gaze-region label 생성·data overlap·loss weighting·추론 경로을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
