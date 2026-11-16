# Can Small Training Runs Reliably Guide Data Curation? Rethinking Proxy-Model Practice

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

작은 proxy 실험의 데이터 순위가 큰 model 학습에서도 유지되는지 불명확하다.

## Bottleneck and Changed Formulation

Data-dependent tuning에 따라 순위가 바뀌는 문제를 분석하고 작은 learning rate를 쓰는 평가 보정을 제안한다.

## System and Robotics Loop

Data recipe·proxy 학습 설정 → 상대 loss 순위; 로봇 행동 평가는 아니다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

이론 적용 범위, loss와 task success 차이, tuning 총비용.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

LLM pretraining recipe와 random-feature model 이론을 다룬다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/c7d04ce5e71efdfc7a4a78f7161238a9-Abstract-Conference.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
