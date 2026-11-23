# Mobi-π: Mobilizing Your Robot Learning Policy

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / CoRL
- Authors: Jingyun Yang, Isabella Huang, Brandon Vu, Max Bajracharya, Rika Antonova, Jeannette Bohg
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, mobile-manipulation, policy-mobilization, 3d-gaussian-splatting, base-placement
- Aliases: Mobi-pi, Mobi-π
- Official paper: https://proceedings.mlr.press/v305/yang25b.html
- Venue verification: https://proceedings.mlr.press/v305/yang25b.html
- Code/Project: https://mobipi.github.io/
- Code: https://github.com/yjy0625/mobipi
- Source audit: 2026-10-28 공식 서지/abstract·저자 project/code 소개 확인. 신규 표준 노트는 abstract 기반이다. 기존 HANDOFF 지정 구간 검토는 별도 source ledger에 있으며 전체 정독·payload·실행 검증을 뜻하지 않는다.

## Problem and Importance

제한된 base pose와 시야로 학습한 조작 정책은 이동 후 달라진 관측 분포에서 실패할 수 있다.

## Core Idea and Contribution

정책을 다시 학습하는 대신 실행할 base pose를 찾는 policy mobilization을 정식화한다. 3D Gaussian Splatting의 새 시점 영상, pose 적합도와 sampling 기반 최적화를 연결한다.

## Observation–State–Action Interface

현재 장면과 사전 학습 조작 정책의 데이터 → 장면 표현·후보 pose 점수 → 조작을 시작할 base pose → 기존 정책 실행.

## Evaluation Scope and Claim Boundary

RoboCasa 기반 simulated mobile manipulation과 실로봇에서 pose 선택을 비교한다. 이 비교만으로 다른 정책에 선택된 pose를 재사용할 때의 성능을 확정할 수 없다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/yang25b.html) · [저자 project/code](https://mobipi.github.io/) · [공식 code](https://github.com/yjy0625/mobipi). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Mobile ALOHA의 whole-body 데이터와 MoTo의 이동–조작 연결을 보완하며, HANDOFF의 정책별 도착 조건을 비교할 직접 선행이다.

## Verification Boundary

pose 후보와 collision/reachability 처리, 정책별 학습 시야와 데이터 접근, 장면 구축 비용, 실제 도착 상태·평가 분모을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
