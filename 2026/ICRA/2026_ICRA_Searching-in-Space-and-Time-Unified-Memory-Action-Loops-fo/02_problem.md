# Searching in Space and Time: Unified Memory-Action Loops for Open-World Object Retrieval

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

동적 환경에서 과거 위치나 속성으로 지칭한 물체를 현재 찾아야 한다.

## Bottleneck and Changed Formulation

장기 기억과 작업 기억을 이용해 과거 기록 조회와 물리적 탐색 중 다음 행동을 선택한다.

## System and Robotics Loop

공간·시간 표현이 포함된 지시와 관측 이력으로 기억 조회·탐색 행동을 선택한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

실물과 시뮬레이션의 과제 수, 기억 관측 주체, 대상 이동 빈도.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

저자는 STARBench와 Tiago 실기에서 비교했다. 프로젝트의 360개 과제는 3개 아파트와 3개 과제군을 포함한다.

## Evidence Anchor

[공식 paper/abstract](https://ieeexplore.ieee.org/document/11696368/) · [저자 project/code](https://amrl.cs.utexas.edu/STAR/) · [공식 code](https://github.com/ut-amrl/STARBench). Exact objective, constraints, success definition은 본문 수동 확인 필요.
