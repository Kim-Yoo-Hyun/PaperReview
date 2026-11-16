# Mobi-π: Mobilizing Your Robot Learning Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

제한된 base pose와 시야로 학습한 조작 정책은 이동 후 달라진 관측 분포에서 실패할 수 있다.

## Bottleneck and Changed Formulation

정책을 다시 학습하는 대신 실행할 base pose를 찾는 policy mobilization을 정식화한다. 3D Gaussian Splatting의 새 시점 영상, pose 적합도와 sampling 기반 최적화를 연결한다.

## System and Robotics Loop

현재 장면과 사전 학습 조작 정책의 데이터 → 장면 표현·후보 pose 점수 → 조작을 시작할 base pose → 기존 정책 실행.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

pose 후보와 collision/reachability 처리, 정책별 학습 시야와 데이터 접근, 장면 구축 비용, 실제 도착 상태·평가 분모.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

RoboCasa 기반 simulated mobile manipulation과 실로봇에서 pose 선택을 비교한다. 이 비교만으로 다른 정책에 선택된 pose를 재사용할 때의 성능을 확정할 수 없다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v305/yang25b.html) · [저자 project/code](https://mobipi.github.io/) · [공식 code](https://github.com/yjy0625/mobipi). Exact objective, constraints, success definition은 본문 수동 확인 필요.
