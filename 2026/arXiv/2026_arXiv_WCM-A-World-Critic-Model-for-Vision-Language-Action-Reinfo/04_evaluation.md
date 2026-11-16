# WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Source-Supported Evaluation Scope

여러 VLA backbone과 simulation benchmark·실물 조작에서 평가한다.

## Metrics, Baselines, and Generalization

critic/actor 가중치 공유·history 접근·latent target·on/off-policy 차이.

정확한 dataset/split·trial 수·baseline budget·metric 정의·ablation 수치는 이번 초록 정리에서 확정하지 않았다. 이는 원문에 미보고됐다는 뜻이 아니다.

## Reproducibility and Limitations

arXiv v1와 공식 repository의 configs/scripts/world_critic 존재 확인. 학회 acceptance 및 실제 구현 재현은 확인하지 않았다.

공개 code/project가 있어도 실행 재현을 뜻하지 않는다. 실제 로봇·simulation·이론/survey의 범위를 위 평가 설명대로 구별한다.

## Proposed Comparison — Researcher Interpretation

History·모델 크기·데이터를 맞춰 value-only, future-latent 보조, actor-shared gradient를 분리한다.

아직 실행하지 않았으며 예상 이득을 측정 결과로 기록하지 않는다.

## Evidence

[공식 paper/abstract](https://arxiv.org/abs/2607.29613). Code/project·확인 날짜는 [overview](./01_overview.md)를 따른다.
