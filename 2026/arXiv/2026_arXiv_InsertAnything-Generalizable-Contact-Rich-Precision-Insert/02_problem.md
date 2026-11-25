# InsertAnything: Generalizable Contact-Rich Precision Insertion from Simulation to Reality

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

구멍 위치에 오차가 있고 끼워맞춤 여유가 작을 때 정렬 실패와 걸림이 발생한다.

## Bottleneck and Changed Formulation

시뮬레이션에서 정렬과 삽입을 나누어 보상하고 손끝 힘을 이용해 접촉 뒤의 수정 동작을 학습한다.

## System and Robotics Loop

목표 자세와 3차원 손끝 힘이 입력이며 정책은 삽입을 위한 움직임을 출력한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

형상별 시행 수, 목표 자세의 취득 방식과 사람 개입 범위.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

저자는 실제 여러 형상에서 최소 공칭 간극 0.02 mm를 다뤘다. ManipulationNet의 20/20은 사람 개입을 허용한 프로토콜이며 다른 실험의 자율 지표와 구별한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.24511) · [저자 project/code](https://mzhsoul.github.io/InsertAnything/) · [공식 code](https://github.com/mzhsoul/InsertAnything). Exact objective, constraints, success definition은 본문 수동 확인 필요.
