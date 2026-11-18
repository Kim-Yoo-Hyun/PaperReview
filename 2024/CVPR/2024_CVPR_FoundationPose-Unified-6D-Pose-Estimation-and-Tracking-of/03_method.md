# FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Neural implicit 표현으로 두 입력 조건을 연결해 동일 pose 모듈을 재사용한다. 새 물체별 fine-tuning 없이 적용하는 설정이다.

## Observation–State–Action Interface

RGB-D와 CAD 또는 reference 관측에서 물체 6D pose·tracking 출력을 얻는다. 행동 정책 자체는 아니다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Model-free reference 요구·대칭 처리·ranking score와 보정 확률의 차이.

Source가 명시한 evaluation 범위: 공식 project는 미지 물체 pose estimation/tracking의 일반화를 제시한다. 이번 등록에서는 세부 trial·로봇 성공률을 확정하지 않는다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 CAD·깊이·카메라 조건에서 pose coverage와 실제 배치 성공을 따로 측정한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2024/html/Wen_FoundationPose_Unified_6D_Pose_Estimation_and_Tracking_of_Novel_Objects_CVPR_2024_paper.html) · [저자 project/code](https://nvlabs.github.io/FoundationPose/) · [공식 code](https://github.com/NVlabs/FoundationPose). 수식·세부 구현·코드 실행은 미검증이다.
