# PoseIt: A Visual-Tactile Dataset of Holding Poses for Grasp Stability Analysis

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

처음 들어 올렸을 때의 안정성이 팔을 다른 자세로 옮긴 뒤에도 유지되는지 알아야 한다.

## Bottleneck and Changed Formulation

집기·자세 이동·흔들기 전 과정의 시각과 촉각 관측을 수집하고 다중 모달 시계열 분류기를 비교한다.

## System and Robotics Loop

RGB-D, 손가락 촉각, 힘·토크와 로봇 상태가 자세별 안정성 예측의 입력이다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

물체 분할, 파지 명령이 변경된 시점과 단계별 실패 라벨의 의미.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

저자 자료는 26개 물체의 실물 기록을 제공하며 초록은 미관측 물체와 자세에 대한 예측을 평가한다. 자세 이동 중 실패와 마지막 흔들기 결과는 별개다.

## Evidence Anchor

[공식 paper/abstract](https://ieeexplore.ieee.org/document/9981562/) · [저자 project/code](https://publish.illinois.edu/robotouch/poseit-a-visual-tactile-dataset-of-holding-poses-for-grasp-stability-analysis/) · [공식 code](https://github.com/Robo-Touch/PoseIt). Exact objective, constraints, success definition은 본문 수동 확인 필요.
