# Gen2Act: Human Video Generation in Novel Scenarios enables Generalizable Robot Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / CoRL
- Authors: Homanga Bharadhwaj, Debidatta Dwibedi, Abhinav Gupta, Shubham Tulsiani, Carl Doersch, Ted Xiao, Dhruv Shah, Fei Xia, Dorsa Sadigh, Sean Kirmani
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, human video, Video Generation, generalization
- Aliases: Gen2Act
- Official paper: https://proceedings.mlr.press/v305/bharadhwaj25a.html
- Venue verification: https://proceedings.mlr.press/v305/bharadhwaj25a.html
- Code/Project: https://homangab.github.io/gen2act/
- Code: project_only
- Source audit: 2026-10-25 공식 abstract/서지정보 및 명시된 저자 링크 확인. 이번 노트는 abstract 기반이며 본문 전체·코드 실행·payload는 미검증이다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

Gen2Act는 사전학습된 영상 생성기가 지시로부터 그린 사람의 행동을 참고해 실제 로봇의 조작 행동을 생성한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/bharadhwaj25a/bharadhwaj25a.pdf#page=1)

## Core Idea and Contribution

- 생성 영상을 조작 시연으로 추가 학습하지 않은 영상 모델에서 얻고, 로봇 정책이 영상 특징과 점의 움직임을 활용하도록 훈련한다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/bharadhwaj25a/bharadhwaj25a.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/bharadhwaj25a/bharadhwaj25a.pdf#page=4)
- 로봇 시연에 없던 물체와 움직임 조합에서 생성 영상을 이용한 단일 정책의 일반화와 영상 조건의 영향을 평가했다. [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/bharadhwaj25a/bharadhwaj25a.pdf#page=5) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/bharadhwaj25a/bharadhwaj25a.pdf#page=7)

## Observation–State–Action Interface

장면·언어 → 생성 인간 영상 → 영상 조건 closed-loop robot action.

## Evaluation Scope and Claim Boundary

새 물체 종류·동작을 포함한 실환경 manipulation을 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/bharadhwaj25a.html) · [저자 project/code](https://homangab.github.io/gen2act/). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

VLA의 video prior가 action supervision을 어떻게 보완하는지 비교할 직접 선행이다.

## Verification Boundary

robot-data holdout, video 사전학습 중복, motion conditioning과 실행 latency을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
