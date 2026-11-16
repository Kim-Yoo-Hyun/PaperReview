# Can Small Training Runs Reliably Guide Data Curation? Rethinking Proxy-Model Practice

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICLR
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Robotics, evaluation, data-selection
- Aliases:
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/c7d04ce5e71efdfc7a4a78f7161238a9-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2026/hash/c7d04ce5e71efdfc7a4a78f7161238a9-Abstract-Conference.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다.

## Problem and Importance

작은 proxy 실험의 데이터 순위가 큰 model 학습에서도 유지되는지 불명확하다.

## Core Idea and Contribution

Data-dependent tuning에 따라 순위가 바뀌는 문제를 분석하고 작은 learning rate를 쓰는 평가 보정을 제안한다.

## Observation–State–Action Interface

Data recipe·proxy 학습 설정 → 상대 loss 순위; 로봇 행동 평가는 아니다.

## Evaluation Scope and Claim Boundary

LLM pretraining recipe와 random-feature model 이론을 다룬다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/c7d04ce5e71efdfc7a4a78f7161238a9-Abstract-Conference.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

GAP-N1에서 관측 정보 효과와 optimizer 설정 효과를 분리하는 필수 방법론 참조다.

## Verification Boundary

이론 적용 범위, loss와 task success 차이, tuning 총비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
