# Online Continual Learning with Maximal Interfered Retrieval

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

예상 parameter update 뒤 손실이 많이 증가할 sample을 선택해 replay한다.

## Observation–State–Action Interface

현재 minibatch·stored memory → virtual update → 간섭 score.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: virtual step, candidate memory budget, classification과 robot rollout의 차이.

Source가 명시한 evaluation 범위: Continual learning benchmark에서 경험/생성 replay 비교를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

Virtual-update 비용을 포함해 uniform·MIR·제안 score의 retention을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.neurips.cc/paper/2019/hash/15825aee15eb335cc13f9b559f166ee8-Abstract.html) · [저자 project/code](https://github.com/optimass/Maximally_Interfered_Retrieval). 수식·세부 구현·코드 실행은 미검증이다.
