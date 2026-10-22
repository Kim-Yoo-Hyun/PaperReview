# NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Monocular RGB video history를 VLM context로 처리하여 다음 navigation action을 출력한다.

## Observation–State–Action Interface

Language instruction + 누적 RGB video → next-step navigation action; map·odometry·depth 입력 없이 동작하는 formulation을 제안한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Camera-only 가정, action discretization, history truncation, 실제 low-level controller.

Source가 명시한 evaluation 범위: RSS abstract는 continuous navigation simulation과 실제 환경의 cross-dataset/sim-to-real 평가를 명시한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

NaVid의 history context 길이를 변화시키고 fixed task에서 success·SPL·inference latency·wrong-turn recovery를 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss20/p079.html) · [저자 project/code](https://pku-epic.github.io/NaVid/). 수식·세부 구현·코드 실행은 미검증이다.
