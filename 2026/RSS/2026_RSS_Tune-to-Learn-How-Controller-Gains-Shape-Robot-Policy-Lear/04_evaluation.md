# Tune to Learn: How Controller Gains Shape Robot Policy Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Source-Supported Evaluation Scope

세 비교의 조건이 다르다. 행동 복제는 폐루프 성공률로 제어 이득을 비교했고, RL은 각 이득 설정에 맞춰 학습 하이퍼파라미터를 다시 탐색했다. G1 속도 추종은 시뮬레이션이다. FR3의 실물 도달 시험에서는 큰 강성·과감쇠 조건에서 시스템 식별 오차는 작아도 폐루프 궤적의 시뮬레이션–실물 오차가 컸다. [행동 복제·RL 설계](https://www.roboticsproceedings.org/rss22/p139.pdf#page=5) · [G1 비교와 FR3 전이](https://www.roboticsproceedings.org/rss22/p139.pdf#page=8) · [궤적 오차](https://www.roboticsproceedings.org/rss22/p139.pdf#page=9)

## Metrics, Baselines, and Generalization

gain 단위·controller rate·policy 반응·hyperparameter 예산·sim-to-real 차이.

정확한 dataset/split·trial 수·baseline budget·metric 정의·ablation 수치는 이번 초록 정리에서 확정하지 않았다. 이는 원문에 미보고됐다는 뜻이 아니다.

## Reproducibility and Limitations

RSS의 Shape 제목을 사용하고 저자 페이지의 Affect 제목은 alias로 연결한다. Workshop award를 RSS 수상으로 기록하지 않는다.

공개 code/project가 있어도 실행 재현을 뜻하지 않는다. 실제 로봇·simulation·이론/survey의 범위를 위 평가 설명대로 구별한다.

## Proposed Comparison — Researcher Interpretation

고정 gain grid와 학습 gain을 같은 정책·데이터·튜닝 예산에서 비교한다.

아직 실행하지 않았으며 예상 이득을 측정 결과로 기록하지 않는다.

## Evidence

[공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p139.html). Code/project·확인 날짜는 [overview](./01_overview.md)를 따른다.
