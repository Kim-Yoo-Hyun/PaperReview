# What Can RL Bring to VLA Generalization? An Empirical Study

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Visual·semantic·execution 변화 축으로 평가하고 PPO와 LLM 계열 RL 방법의 차이를 분석한다.

## Observation–State–Action Interface

Image/language-conditioned VLA → action; 학습 방식과 평가 시 입력 perturbation을 분리한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Generalization split 생성, pretrained overlap, RL별 budget 및 real-robot 범위.

Source가 명시한 evaluation 범위: 공식 NeurIPS abstract는 visual, semantic, execution generalization 및 PPO/DPO/GRPO 비교를 설명한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 VLA의 SFT와 PPO를 고정된 visual/semantic/execution split에서 평가하고 각 축의 성공률을 별도로 보고한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.nips.cc/paper_files/paper/2025/hash/8c0fabe372177d2aded596be2d3b4544-Abstract-Conference.html) · [저자 project/code](https://rlvla.github.io/). 수식·세부 구현·코드 실행은 미검증이다.
