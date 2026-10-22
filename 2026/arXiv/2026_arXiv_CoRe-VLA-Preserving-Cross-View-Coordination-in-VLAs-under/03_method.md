# CoRe-VLA: Preserving Cross-View Coordination in VLAs under Camera Shifts

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Point-cloud reprojection과 render 복원, execution alignment로 training view를 복구한다.

## Observation–State–Action Interface

RGB-D·카메라 관계 → 복원 영상 → frozen VLA action.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: intrinsic/extrinsic 접근, depth 정렬, asynchronous 비용.

Source가 명시한 evaluation 범위: 5 real-robot task, LIBERO-100와 LIBERO-Plus를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

Known-transform comparator와 같은 관측으로 변환을 추정하는 baseline을 분리한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.37150) · [저자 project/code](https://arxiv.org/abs/2609.37150). 수식·세부 구현·코드 실행은 미검증이다.
