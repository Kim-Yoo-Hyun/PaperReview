# MoMa-Kitchen: A 100K+ Benchmark for Affordance-Grounded Last-Mile Navigation in Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

조작 가능 최종 base 위치를 라벨링한 주방 데이터와 affordance baseline을 제공한다.

## Observation–State–Action Interface

RGB-D 관측·로봇 형상 → 조작 가능한 바닥 위치 → 항법 종료.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 형상별 split, oracle grasp label 생성, navigability와 reachability 정의, 실환경 전이.

Source가 명시한 evaluation 범위: 여러 팔·platform 높이를 포함한 simulated kitchen affordance 평가를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 장면·목표에서 proximity와 affordance 종료를 비교하고 실제 grasp 시도 성공을 따로 측정한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_MoMa-Kitchen_A_100K_Benchmark_for_Affordance-Grounded_Last-Mile_Navigation_in_Mobile_ICCV_2025_paper.html) · [저자 project/code](https://momakitchen.github.io/) · [공식 code](https://github.com/MoMaKitchen/MoMaKitchen). 수식·세부 구현·코드 실행은 미검증이다.
