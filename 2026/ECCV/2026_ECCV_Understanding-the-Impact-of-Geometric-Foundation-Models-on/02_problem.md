# Understanding the Impact of Geometric Foundation Models on Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

VLA에 3D 정보를 더하면 좋아지는 이유와, architecture·데이터·카메라 구성의 영향을 분리할 필요가 있다.

## Bottleneck and Changed Formulation

GR00T-N1.5와 VGGT를 고정한 비교에서 geometry를 읽어내는 probe와 세 가지 geometry 결합 구조를 분석한다.

## System and Robotics Loop

영상/언어 기반 VLA에 geometric foundation model의 정보를 결합한다. 정책 입력·학습 방식·카메라 수의 차이를 비교 변수로 구별한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Probe 용량 차이·architecture별 파라미터/학습량·재구성 품질의 측정 단위·task/data split·real-robot 범위.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

공식 초록은 특정 VLA/GFM 조합의 표현 probing, 결합 구조 세 가지, 데이터·카메라 수·재구성 품질의 영향을 비교한다. 모든 VLA에 대한 보편 결론이나 동일 상태 오류 개입 실험을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://link.springer.com/chapter/10.1007/978-3-032-37271-0_2). Exact objective, constraints, success definition은 본문 수동 확인 필요.
