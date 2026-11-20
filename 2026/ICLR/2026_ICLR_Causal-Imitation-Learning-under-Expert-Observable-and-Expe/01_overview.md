# Causal Imitation Learning under Expert-Observable and Expert-Unobservable Confounding

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Daqian Shao, Thomas Kleine Buening, Marta Kwiatkowska
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Imitation Learning, causal-inference, hidden-confounding, history
- Aliases: DML-IL
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/4415e8cb0741bc0beb79b316f0856108-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2026/hash/4415e8cb0741bc0beb79b316f0856108-Abstract-Conference.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-25 공식 abstract/서지정보 및 명시된 저자 링크 확인. 이번 노트는 abstract 기반이며 본문 전체·코드 실행·payload는 미검증이다.

## Problem and Importance

Expert만 아는 정보와 양측 모두 모르는 confounder를 imitation에서 구별해야 한다.

## Core Idea and Contribution

Trajectory history를 instrumental variable로 이용하는 conditional moment 기반 DML-IL을 제안한다.

## Observation–State–Action Interface

expert trajectory history → instrumental-variable regression → imitation policy.

## Evaluation Scope and Claim Boundary

MuJoCo를 포함한 연속 상태·행동 환경에서 causal IL baseline과 비교한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/4415e8cb0741bc0beb79b316f0856108-Abstract-Conference.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

VLA history 추가를 새 해결책으로 주장하기 전에 정보 비대칭과 도구변수 조건을 점검할 선행이다.

## Verification Boundary

instrument relevance/exclusion, 시간적 confounding, history 접근, imitation-gap 가정을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
