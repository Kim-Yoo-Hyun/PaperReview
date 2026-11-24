# LILAC: Language-Conditioned Object-Centric Optical Flow for Open-Loop Trajectory Generation

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2026 / RA-L
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
- Full-text retrieval: https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11478289
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다.

## Problem and Importance

LILAC은 조작 전 RGB 영상과 언어 지시로부터 물체 중심의 2차원 흐름을 생성하고 이를 로봇 팔의 개루프 6자유도 궤적으로 변환한다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11478289#page=1) · [PDF 2쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11478289#page=2)

## Core Idea and Contribution

- 언어와 움직임의 정합 손실 및 프롬프트 조건부 어댑터로 같은 장면에서도 지시에 맞는 흐름을 생성하도록 학습한다. [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11478289#page=3) · [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11478289#page=4)
- 생성한 흐름의 영상 평가와 자유로운 표현의 지시를 받은 실물 로봇의 과제 성공을 별도로 비교했다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11478289#page=5) · [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11478289#page=6) · [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11478289#page=7)

## Observation–State–Action Interface

단일 초기 RGB·지시 → motion flow → 로봇 궤적. Open-loop 궤적 생성과 실행 중 feedback/replanning은 구분한다.

## Evaluation Scope

Flow 품질 benchmark와 자유형 지시의 실제 조작을 평가한다. IEEE RA-L 11(6), 2026 게재를 확인했다.

근거: [공식 paper/abstract](https://ieeexplore.ieee.org/abstract/document/11478289) · [저자 project](https://lilac-75srg.kinsta.page/).

## Why This Paper Is Here — Researcher Interpretation

Flow/geometry를 action으로 연결하는 REFERENCE다. 현재 frozen VLA 검색 실험의 직접 prerequisite는 아니므로 NEXT를 늘리기보다 표현·개방루프 비교가 필요할 때 찾도록 둔다.

범위와 수치의 미확인 항목은 [평가 노트](./04_evaluation.md)에, 제안하는 반증 질문은 [insights](./05_insights.md)에 둔다.
