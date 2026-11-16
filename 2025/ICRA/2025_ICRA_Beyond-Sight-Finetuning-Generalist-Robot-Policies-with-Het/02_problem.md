# Beyond Sight: Finetuning Generalist Robot Policies with Heterogeneous Sensors via Language Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

시각·proprio 중심 generalist policy에 적은 촉각·음향 데이터를 통합하기 어렵다.

## Bottleneck and Changed Formulation

Language grounding과 multimodal contrastive·language generation loss로 새 sensor 의미를 연결한다.

## System and Robotics Loop

Vision·touch·audio·언어 → generalist policy → 조작 action.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

센서 동기화, 모달별 annotation 비용, 입력 결손과 추가 정보의 구별.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Diffusion generalist와 VLA의 실세계 manipulation 및 cross-modal prompting을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2501.04693) · [저자 project/code](https://fuse-model.github.io/) · [공식 code](https://github.com/fuse-model/FuSe). Exact objective, constraints, success definition은 본문 수동 확인 필요.
