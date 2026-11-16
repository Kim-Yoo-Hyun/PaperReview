# Diagnosing Compositional Generalization in Sequential Robot Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

순차 조작의 모든 지시 조합을 수집하기 어려울 때 어떤 training coverage가 새로운 조합에 필요한지 묻는다.

## Bottleneck and Changed Formulation

지시 marginal·지시 조합·context–action 변화를 분리하고, 데이터 coverage와 단계별 정책을 비교한다.

## System and Robotics Loop

시각 관측·로봇 상태·지시 → transformer flow-matching 조작 정책. 현재 연구의 frozen VLA와 동일 checkpoint 실험이 아니다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

v1/v2 차이, 단계별 정책의 입력과 전환 신호, 종속 지시의 정보 병목, demonstration 예산, 공개 release와 논문 설정의 차이.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Pick-and-place, 후속 버튼 조작, 의존적인 두 단계 조작에서 coverage와 분해를 비교한다. 저자 공개 code는 개선된 pipeline이라 release 결과와 논문 결과가 다를 수 있다고 명시한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2607.29687) · [저자 project/code](https://yixiaowang7.github.io/Diagnosing_Compositional_Generalization_Robot_Page/) · [공식 code](https://github.com/YixiaoWang7/Diagnosing_Compositional_Generalization_Robot). Exact objective, constraints, success definition은 본문 수동 확인 필요.
