# RePlan-Bot: Multi-Level Replanning for Embodied Instruction Following

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

고수준 계획 감사와 탐색·저수준 보정을 연결한다.

## Observation–State–Action Interface

지시·환경 관측 → subgoal/map 판단 → 행동 보정.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: ALFRED predicate, oracle map 접근, action executor, VLA와의 차이.

Source가 명시한 evaluation 범위: ALFRED instruction following 평가를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

Plan 수정과 action 보정을 분리하고 task success·개입 비용을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026W/GRAIL-V/html/Gong_RePlan-Bot_Multi-Level_Replanning_for_Embodied_Instruction_Following_CVPRW_2026_paper.html). 수식·세부 구현·코드 실행은 미검증이다.
