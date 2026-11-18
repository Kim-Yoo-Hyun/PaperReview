# ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

시각 출력으로 target gaze 영역을 복원하는 diffusion transformer를 학습해 implicit grounding을 유도한다.

## Observation–State–Action Interface

언어·영상에서 action과 학습용 target-region reconstruction을 연결한다. 3D metric reconstruction 방법은 아니다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Gaze-region label 생성·data overlap·loss weighting·추론 경로.

Source가 명시한 evaluation 범위: 공개 로봇 데이터 기반 사전학습과 simulation·실세계 조작 평가를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

ROI·학습 데이터·추가 parameter를 맞추고 2D/3D auxiliary target을 대조한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://ojs.aaai.org/index.php/AAAI/article/view/38921). 수식·세부 구현·코드 실행은 미검증이다.
