# Gen2Act: Human Video Generation in Novel Scenarios enables Generalizable Robot Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
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
- Source audit: 2026-10-25 공식 abstract/서지정보 및 명시된 저자 링크 확인. 이번 노트는 abstract 기반이며 본문 전체·코드 실행·payload는 미검증이다.

## Problem and Importance

Robot 데이터에 없는 물체 종류와 동작으로 언어 조건 조작을 확장해야 한다.

## Core Idea and Contribution

고정된 생성 모델의 인간 영상을 조건으로 공통 robot policy를 실행한다.

## Observation–State–Action Interface

장면·언어 → 생성 인간 영상 → 영상 조건 closed-loop robot action.

## Evaluation Scope and Claim Boundary

새 물체 종류·동작을 포함한 실환경 manipulation을 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/bharadhwaj25a.html) · [저자 project/code](https://homangab.github.io/gen2act/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

VLA의 video prior가 action supervision을 어떻게 보완하는지 비교할 직접 선행이다.

## Verification Boundary

robot-data holdout, video 사전학습 중복, motion conditioning과 실행 latency을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
