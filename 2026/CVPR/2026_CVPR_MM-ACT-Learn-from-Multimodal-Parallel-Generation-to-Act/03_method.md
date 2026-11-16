# MM-ACT: Learn from Multimodal Parallel Generation to Act

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

텍스트·영상·행동을 공유 token 공간과 context로 학습하고 modality별 병렬 decoding을 사용한다.

## Observation–State–Action Interface

공유 multimodal context → text/image/action generation; action은 one-step parallel decoding.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: modality별 loss·compute 균형, 생성 token이 action에 주는 영향, RL 미검증 범위.

Source가 명시한 evaluation 범위: LIBERO, 실제 Franka, RoboTwin2.0의 in-domain·out-of-domain 조작을 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 데이터에서 action-only와 multimodal pretraining을 비교한 뒤 동일 RL update를 적용한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Liang_MM-ACT_Learn_from_Multimodal_Parallel_Generation_to_Act_CVPR_2026_paper.html) · [저자 project/code](https://github.com/HHYHRHY/MM-ACT). 수식·세부 구현·코드 실행은 미검증이다.
