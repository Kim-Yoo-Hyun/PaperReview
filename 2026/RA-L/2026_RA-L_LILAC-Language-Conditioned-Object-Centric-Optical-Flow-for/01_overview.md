# LILAC: Language-Conditioned Object-Centric Optical Flow for Open-Loop Trajectory Generation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Motonari Kambara, Koki Seno, Tomoya Kaichi, Yanan Wang, Komei Sugiura
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, optical-flow, trajectory-generation, human-video
- Aliases: LILAC
- Official paper: https://api.crossref.org/works/10.1109/LRA.2026.3682441
- Venue verification: https://ieeexplore.ieee.org/abstract/document/11478289
- Code/Project: https://lilac-75srg.kinsta.page/
- Code: not_released
- Source audit: 2026-11-02 공식 proceedings/publisher의 서지·abstract와 저자 project/code 소개를 확인했다. IEEE indexed publisher 내용으로 게재를 확인했고 직접 본문 접근은 제한적이었다. 노트는 abstract/project 기반이며 본문 정독·native 실행을 뜻하지 않는다. 사용자 읽기 상태는 UNREAD 유지.

## Problem and Importance

사람/웹 영상에서 얻은 움직임을 언어에 맞는 로봇 궤적으로 변환하는 데 필요한 정렬을 다룬다.

## Core Idea and Contribution

언어와 RGB로 object-centric 2D flow를 생성하고 이를 6-DoF 로봇 trajectory로 변환한다.

## Observation–State–Action Interface

단일 초기 RGB·지시 → motion flow → 로봇 궤적. Open-loop 궤적 생성과 실행 중 feedback/replanning은 구분한다.

## Evaluation Scope

Flow 품질 benchmark와 자유형 지시의 실제 조작을 평가한다. IEEE RA-L 11(6), 2026 게재를 확인했다.

근거: [공식 paper/abstract](https://ieeexplore.ieee.org/abstract/document/11478289) · [저자 project](https://lilac-75srg.kinsta.page/).

## Why This Paper Is Here — Researcher Interpretation

Flow/geometry를 action으로 연결하는 REFERENCE다. 현재 frozen VLA 검색 실험의 직접 prerequisite는 아니므로 NEXT를 늘리기보다 표현·개방루프 비교가 필요할 때 찾도록 둔다.

범위와 수치의 미확인 항목은 [평가 노트](./04_evaluation.md)에, 제안하는 반증 질문은 [insights](./05_insights.md)에 둔다.
