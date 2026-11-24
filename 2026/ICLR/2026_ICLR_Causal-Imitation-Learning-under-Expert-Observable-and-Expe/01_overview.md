# Causal Imitation Learning under Expert-Observable and Expert-Unobservable Confounding

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2026 / ICLR
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
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2026/file/4415e8cb0741bc0beb79b316f0856108-Paper-Conference.pdf
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다.

## Problem and Importance

DML-IL은 전문가만 관찰하는 변수와 전문가·모방자 모두에게 숨은 교란 잡음이 시연에 함께 작용하는 인과 모방학습 문제를 다룬다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/4415e8cb0741bc0beb79b316f0856108-Paper-Conference.pdf#page=1) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/4415e8cb0741bc0beb79b316f0856108-Paper-Conference.pdf#page=4)

## Core Idea and Contribution

- 과거 궤적을 도구변수로 사용해 모방을 조건부 적률 제약으로 표현하고 식별 가능성과 관련된 가정 아래 모방 격차의 상한을 구한다. [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/4415e8cb0741bc0beb79b316f0856108-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/4415e8cb0741bc0beb79b316f0856108-Paper-Conference.pdf#page=6) · [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/4415e8cb0741bc0beb79b316f0856108-Paper-Conference.pdf#page=7)
- 연속 상태·행동 예제와 MuJoCo에서 교란이 있는 시연으로 학습한 정책을 다른 인과 모방 기준선과 비교했다. [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/4415e8cb0741bc0beb79b316f0856108-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/4415e8cb0741bc0beb79b316f0856108-Paper-Conference.pdf#page=9) · [PDF 10쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/4415e8cb0741bc0beb79b316f0856108-Paper-Conference.pdf#page=10)

## Observation–State–Action Interface

expert trajectory history → instrumental-variable regression → imitation policy.

## Evaluation Scope and Claim Boundary

MuJoCo를 포함한 연속 상태·행동 환경에서 causal IL baseline과 비교한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/4415e8cb0741bc0beb79b316f0856108-Abstract-Conference.html).

## Why This Paper Is Here — Researcher Interpretation

VLA history 추가를 새 해결책으로 주장하기 전에 정보 비대칭과 도구변수 조건을 점검할 선행이다.

## Verification Boundary

instrument relevance/exclusion, 시간적 confounding, history 접근, imitation-gap 가정을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
