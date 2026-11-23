# Causal World Modeling for Robot Control

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Lin Li, Qihang Zhang, Yiming Luo, Shuai Yang, Ruilin Wang, Luyao Zhang, Mingrui Yu, Zelin Gao, Nan Xue, Boyu Zhou, Xing Zhu, Mingyu Ding, Yujun Shen, Yinghao Xu
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: world-model, action-generation, temporal-context, manipulation
- Aliases: CauVA
- Official paper: https://www.roboticsproceedings.org/rss22/p016.html
- Venue verification: https://www.roboticsproceedings.org/rss22/p016.html
- Code/Project:
- Code: not_identified
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. 공식 RSS abstract만을 canonical scope로 사용한다. 같은 제목의 arXiv2601.21998은 LingBot-VA와 다른 저자 구성·설계를 표기하므로 version mapping을 확정하지 않았고 arXiv ID/code를 자동 합치지 않았다. 별도 중복 등록도 하지 않았다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

Lingbot-VA는 비디오 프레임 예측과 로봇 행동 추론을 같은 인과적 시퀀스로 학습해 과거 상호작용을 조작 제어에 반영한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss22/p016.pdf#page=1)

## Core Idea and Contribution

- 영상과 행동을 처리하는 트랜스포머를 결합하고 과거 관측을 캐시에 보존하며, 영상의 잡음 제거가 끝나기 전에 행동을 복호화하도록 학습한다. [PDF 3쪽](https://www.roboticsproceedings.org/rss22/p016.pdf#page=3) · [PDF 4쪽](https://www.roboticsproceedings.org/rss22/p016.pdf#page=4) · [PDF 5쪽](https://www.roboticsproceedings.org/rss22/p016.pdf#page=5)
- 시뮬레이션과 실제 로봇의 다단계·정밀·변형 물체 조작에서 실행 성능을 평가하고 실제 관측을 이력에 반영하는 설계의 영향을 조사했다. [PDF 6쪽](https://www.roboticsproceedings.org/rss22/p016.pdf#page=6) · [PDF 7쪽](https://www.roboticsproceedings.org/rss22/p016.pdf#page=7)

## Observation–State–Action Interface

영상·행동 이력 → 인과적 생성 sequence → 미래 영상·robot action.

## Evaluation Scope and Claim Boundary

시뮬레이션과 실제 장시간·정밀·변형체 조작을 평가한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p016.html). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Architecture 통합과 RL 공동 갱신을 구별할 world-action 비교 대상으로 보완한다.

## Verification Boundary

본문에서 확인할 항목: 예측/행동 gradient 경로·추론 history·실제 피드백·버전별 모델 명칭. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
