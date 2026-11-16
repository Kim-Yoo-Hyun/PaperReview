# EvoVLA: Self-evolving Vision-Language-Action Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Frozen VLM reward가 그럴듯한 관측을 실제 단계 완료와 혼동할 수 있다.

## Bottleneck and Changed Formulation

Counterfactual hard negative 기반 stage reward, relative pose 탐색, 선택적 장기 memory를 결합한다.

## System and Robotics Loop

관측·지시 → VLA rollout; stage reward·pose exploration·memory가 RL 후학습을 지원한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

pose·stage annotation의 특권 정보, hard-negative 생성 비용, 세 모듈별 기여.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Discoverse-L 장기 조작과 실제 로봇의 성공·stage hallucination을 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://link.springer.com/chapter/10.1007/978-3-032-37023-5_14) · [저자 project/code](https://aigeeksgroup.github.io/EvoVLA/) · [공식 code](https://github.com/AIGeeksGroup/EvoVLA). Exact objective, constraints, success definition은 본문 수동 확인 필요.
