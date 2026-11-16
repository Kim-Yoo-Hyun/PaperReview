# Joint-Aligned Latent Action: Towards Scalable VLA Pretraining in the Wild

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

역동역학과 실제 행동에 함께 정렬한 latent action을 학습한다.

## Observation–State–Action Interface

사람 영상 전이 → 행동 중심 embedding → VLA 사전학습.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 실제 action label 요구량, 인간 손과 robot action 대응, 비정형 영상 split.

Source가 명시한 evaluation 범위: 사람 동작 및 simulation·실제 robot manipulation 전이를 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 영상·로봇 데이터에서 역동역학만, 행동 정렬만, 공동 정렬을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Luo_Joint-Aligned_Latent_Action_Towards_Scalable_VLA_Pretraining_in_the_Wild_CVPR_2026_paper.html) · [저자 project/code](https://research.beingbeyond.com/jala) · [공식 code](https://github.com/BeingBeyond/JALA). 수식·세부 구현·코드 실행은 미검증이다.
