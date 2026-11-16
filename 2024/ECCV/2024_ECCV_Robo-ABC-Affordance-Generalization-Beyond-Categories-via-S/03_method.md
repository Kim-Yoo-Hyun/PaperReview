# Robo-ABC: Affordance Generalization Beyond Categories via Semantic Correspondence for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Human video의 affordance memory에서 유사 물체를 찾고 semantic correspondence로 contact point를 옮긴다.

## Observation–State–Action Interface

새 물체 영상·contact memory → affordance/contact point → robot manipulation.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 2D/3D lifting, grasp 실행기, source별 수치 차이.

Source가 명시한 evaluation 범위: 시각 affordance 추정과 실세계 cross-category grasping을 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 object에서 retrieval 정확도와 실제 reachable grasp 성공을 분리 측정한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5748_ECCV_2024_paper.php) · [저자 project/code](https://tea-lab.github.io/Robo-ABC/) · [공식 code](https://github.com/TEA-Lab/Robo-ABC). 수식·세부 구현·코드 실행은 미검증이다.
