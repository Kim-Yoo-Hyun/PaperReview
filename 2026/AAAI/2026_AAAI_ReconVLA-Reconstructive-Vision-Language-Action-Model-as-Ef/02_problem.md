# ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

VLA의 attention이 실제 조작 대상 대신 관련 없는 영역에 분산될 수 있다.

## Bottleneck and Changed Formulation

시각 출력으로 target gaze 영역을 복원하는 diffusion transformer를 학습해 implicit grounding을 유도한다.

## System and Robotics Loop

언어·영상에서 action과 학습용 target-region reconstruction을 연결한다. 3D metric reconstruction 방법은 아니다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Gaze-region label 생성·data overlap·loss weighting·추론 경로.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

공개 로봇 데이터 기반 사전학습과 simulation·실세계 조작 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://ojs.aaai.org/index.php/AAAI/article/view/38921). Exact objective, constraints, success definition은 본문 수동 확인 필요.
