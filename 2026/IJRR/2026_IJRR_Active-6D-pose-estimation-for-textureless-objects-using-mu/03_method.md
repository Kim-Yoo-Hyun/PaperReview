# Active 6D pose estimation for textureless objects using multi-view RGB frames

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Translation을 먼저 추정하고 canonical-scale template으로 orientation을 추정한 뒤 pose uncertainty를 줄일 다음 view를 선택한다.

## Observation–State–Action Interface

다중 RGB·알려진 물체 geometry와 camera 관측에서 pose 및 다음 카메라 시점을 출력한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: CAD·calibration 요구·transparent dataset 조건·실제 이동 비용.

Source가 명시한 evaluation 범위: ROBI·TOD·T-ROBI에서 같은 view의 추정 성능과 적은 view로 얻는 정확도를 비교한다. VLA 행동 효과 평가로 확장하지 않는다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 추정 후보와 카메라 budget에서 pose uncertainty 규칙과 task tolerance 규칙을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://journals.sagepub.com/doi/10.1177/02783649251411922) · [저자 project/code](https://trailab.github.io/ActiveODPE/). 수식·세부 구현·코드 실행은 미검증이다.
