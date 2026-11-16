# EC-Flow: Enabling Versatile Robotic Manipulation from Action-Unlabeled Videos via Embodiment-Centric Flow

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Embodiment-centric flow와 goal alignment를 학습하고 URDF 제약으로 행동에 변환한다.

## Observation–State–Action Interface

영상·지시 → embodiment flow → kinematic 제약 기반 robot action.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: URDF만으로 해결되는 변환 범위, calibration, 동역학·접촉 정보 의존성.

Source가 명시한 evaluation 범위: Meta-World와 실제 가림·변형·비변위 조작을 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 task의 object-centric와 embodiment-centric 표현을 비교하고 URDF·제어 오차를 따로 바꾼다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_EC-Flow_Enabling_Versatile_Robotic_Manipulation_from_Action-Unlabeled_Videos_via_Embodiment-Centric_ICCV_2025_paper.html) · [저자 project/code](https://ec-flow1.github.io/) · [공식 code](https://github.com/YixiangChen515/EC-Flow). 수식·세부 구현·코드 실행은 미검증이다.
