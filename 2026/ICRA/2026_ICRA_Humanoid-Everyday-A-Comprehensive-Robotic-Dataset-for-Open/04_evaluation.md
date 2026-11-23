# Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`.
> Source audit: 2025년 arXiv 공개 후 ICRA 2026에 게재됐다. 다른 분석의 근거 범위는 각 절에 표시했다. [IEEE DOI 서지](https://doi.org/10.1109/ICRA57385.2026.11696267)
> Canonical metadata: [01_overview.md](./01_overview.md).

## Evaluation Type and Scope

G1과 H1에서 원격조작으로 수집한 시연은 약 1만 300개 궤적, 300만 프레임 이상이며 7개 범주의 260개 작업을 포함한다. [전체 규모](https://arxiv.org/pdf/2510.08807v3#page=1) · [작업별 수집](https://arxiv.org/pdf/2510.08807v3#page=5)

## Dataset / Benchmark Role

Unitree G1/H1의 open-world 조작 학습 자료. Ψ₀에서 쓰는 subset과 전체 corpus를 구분한다.

## Metrics and Success Definition

표 II는 일곱 조작 과제에서 정책별·과제별로 열 번 수행한 시도의 성공률을 보고한다. 과제별 시작 상태의 구성과 학습·평가 장면의 중복 여부는 추가 확인이 필요하다. [실물 평가, 표 II](https://arxiv.org/pdf/2510.08807v3#page=6)

## Baselines and Fairness

not recorded — embodiment별 action dimensionality·teleop 방식·작업/scene 누수를 본문에서 대조해야 한다.

## Ablations and Sensitivity

not recorded — 본문 수동 확인 필요.

## Generalization and Failure Cases

넓은 시연 범위가 unseen robot/scene의 성능 입증은 아니다. Sensor 결측·action 변환·서로 다른 controller 지원 범위가 재사용 제약이다.

## Statistics, Efficiency, and Reproducibility

[공식 code/data 링크](https://github.com/physical-superintelligence-lab/Humanoid-Everyday) 확인. Project의 cloud 평가 안내와 repository 링크 상태가 다르므로 서비스가 실제 작동한다고 기록하지 않는다. 다운로드·runtime 검증은 하지 않았다.
