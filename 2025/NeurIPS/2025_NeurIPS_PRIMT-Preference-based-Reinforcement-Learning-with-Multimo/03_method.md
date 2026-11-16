# PRIMT: Preference-based Reinforcement Learning with Multimodal Feedback and Trajectory Synthesis from Foundation Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

VLM·LLM 피드백 결합, foresight trajectory 생성과 hindsight augmentation·causal auxiliary loss를 사용한다.

## Observation–State–Action Interface

행동 trajectory → multimodal preference/reward → RL; 합성 데이터가 학습 감독에 들어간다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 합성 trajectory 유효성, reward 누출, foundation model 호출 비용.

Source가 명시한 evaluation 범위: Locomotion과 manipulation benchmark에서 foundation-model 및 scripted 비교를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 feedback budget으로 원 trajectory만, 단순 증강, causal 증강을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e0d760e4495abf701b97c8acda111372-Abstract-Conference.html) · [저자 project/code](https://primt25.github.io/) · [공식 code](https://github.com/primt25/PRIMT). 수식·세부 구현·코드 실행은 미검증이다.
