# AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Source audit: 2026-11-16: RSS metadata·arXiv v1 §III–V/Table II–IV·공식 코드로 OCR/설명 교정. 과거2026-09-03 PDF review 기록은 보존; 사용자 reading status 변경 없음.
> Canonical metadata: [01_overview.md](./01_overview.md).

## Evaluation Type and Scope

EMPIRICAL / REAL-ROBOT OR HARDWARE. Isaac Gym 및 실물 Unitree G1. [§IV](https://arxiv.org/html/2505.03738v1#S4).

## Dataset / Benchmark Role

자율 Paper Bag Picking/Trash Bottle Throwing 두 과제는 각각50개 teleoperation 시연으로 ACT를 학습한다. 시연 수는 evaluation trial 수가 아니다.

## Metrics and Success Definition

Table II는4096환경×500step tracking 집계다. Table IV의 picking/moving/placing은 단계별 성공 횟수이며 이를 full-task 성공률로 곱하거나 합치지 않는다.

## Baselines and Fairness

w/o AMO·w/o privileged observation 등 ablation과 whole-body 제어 기준선을 비교한다. AMO가 모든 velocity/yaw 지표에서 최고라고 요약하지 않는다.

## Ablations and Sensitivity

시각 입력·ACT chunk와 하위 제어 ablation을 구분한다. 장면/지시 일반화 실험으로 확대하지 않는다.

## Generalization and Failure Cases

Double-support 기반 reference 최적화와 실제 foot-swing의 차이가 한계다. 낮은 몸통 자세/비분포 명령의 안정성을 task 성공과 함께 보아야 한다.

## Statistics, Efficiency, and Reproducibility

[공개 모델/추론 예시](https://github.com/OpenTeleVision/AMO)는 확인했지만 full training release·우리 환경 실행·독립 성능 재현은 미확인이다.
