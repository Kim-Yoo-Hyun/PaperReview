# NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Privileged information guidance를 이용한 simulation training과 end-to-end local navigation diffusion policy를 제안한다.

## Observation–State–Action Interface

Local visual observation + point/image goal 또는 no-goal setting → trajectory/action proposal; privileged 정보의 train/test 경계 확인 필요.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Training oracle, depth/pose 입력, trajectory selector, robot footprint와 controller 한계.

Source가 명시한 evaluation 범위: 저자 project는 no-goal exploration, point-goal/image-goal navigation과 cross-embodiment real-world transfer를 설명한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

NoMaD/NavDP의 goal·sensor·controller 조건을 맞춘 local navigation task에서 collision·success·latency를 측정한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2505.08712) · [저자 project/code](https://github.com/InternRobotics/NavDP). 수식·세부 구현·코드 실행은 미검증이다.
