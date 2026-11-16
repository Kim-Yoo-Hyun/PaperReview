# Diagnosing Compositional Generalization in Sequential Robot Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

지시 marginal·지시 조합·context–action 변화를 분리하고, 데이터 coverage와 단계별 정책을 비교한다.

## Observation–State–Action Interface

시각 관측·로봇 상태·지시 → transformer flow-matching 조작 정책. 현재 연구의 frozen VLA와 동일 checkpoint 실험이 아니다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: v1/v2 차이, 단계별 정책의 입력과 전환 신호, 종속 지시의 정보 병목, demonstration 예산, 공개 release와 논문 설정의 차이.

Source가 명시한 evaluation 범위: Pick-and-place, 후속 버튼 조작, 의존적인 두 단계 조작에서 coverage와 분해를 비교한다. 저자 공개 code는 개선된 pipeline이라 release 결과와 논문 결과가 다를 수 있다고 명시한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

논문의 coverage split과 공개 release 차이를 먼저 확인하고 동일 demonstration 예산·정보 조건을 고정한다. 현재 SET의 D/R 비교를 이 논문의 재현이라고 부르지 않는다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2607.29687) · [저자 project/code](https://yixiaowang7.github.io/Diagnosing_Compositional_Generalization_Robot_Page/) · [공식 code](https://github.com/YixiaoWang7/Diagnosing_Compositional_Generalization_Robot). 수식·세부 구현·코드 실행은 미검증이다.
