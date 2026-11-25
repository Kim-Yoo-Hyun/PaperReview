# Tune to Learn: How Controller Gains Shape Robot Policy Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — RSS 본문과 arXiv v1의 지정 절·부록, 저자 공개 자료 대조 (2026-11-19).

## 직접 확인한 비교

| 설정 | 실험 단위와 관측 결과 |
|---|---|
| 시뮬레이션 행동 복제 | 접시꽂이 싣기·내리기, 식기세척기 열기, 컵 걸기, 양팔 인계, 블록 쌓기. 논문 부록은 이득 셀당 100 rollout을 명시한다. 낮은 강성·높은 감쇠 영역과 나머지 영역의 성공률 차이는 6과제 모두 양수였다. 식기세척기 70.1% 대 45.6%, 블록 쌓기 85.1% 대 39.0%다. 영역 평균이며 최선 단일 설정의 점수와 구분한다. [표 II](https://arxiv.org/html/2604.02523v1#A1.T2) |
| 시뮬레이션 RL | FR3 관절·말단 도달, 큐브 들기, 서랍 열기, G1 속도 추종, Allegro 손 안 큐브 조작, FR3 비파지 큐브 재배향. 표 I은 네 극단 이득마다 성공 설정의 **존재**를 보고했다. 그림 10의 두 과제는 이득당 50회 탐색과 성공 설정의 5시드 학습곡선을 구분한다. [표 I](https://arxiv.org/html/2604.02523v1#S5.T1) · [그림 10](https://arxiv.org/html/2604.02523v1#S5.SS2) |
| 실물 전이 | FR3 관절 도달에서 강성·감쇠가 모두 큰 영역과 그 밖의 평균 궤적 오차는 DR 없이 0.043 대 0.010, DR로 0.060 대 0.018이었다. 말단 도달(DR 없음)은 0.198 대 0.123이다. 실물 폐루프의 주된 실패 양상은 고주파 진동이었다. [궤적 오차 정의](https://arxiv.org/html/2604.02523v1#S4.SS3) · [표 VIII](https://arxiv.org/html/2604.02523v1#A1.T8) |

## 공개 자료의 범위

저자 웹 구현은 BC 5과제의 56셀 점수와 RL 3과제의 Optuna CSV 12개를 표시한다. 큐브 들기 그림 기준은 `lift_goal_fine_rate > 0.95`다. G1에서 중도 중단한 행에는 점수가 없다. 표 I의 전체 7과제와 이 공개 CSV 3과제의 분모가 다르다. 성공률, 제약 위반, 전이 궤적 오차도 서로 다른 측정값이다. 이번에는 저장 점수와 평가 코드를 대조했다. 논문 정책의 재학습·실물 재현은 수행하지 않았다. [저자 점수 정의](https://github.com/younghyopark/tune-to-learn/blob/1775091ee2fdb683e1e767822e5caa87cdfdba4a/static/assets/shapeability_widget.html) · [공개 튜닝 기록](https://github.com/younghyopark/tune-to-learn/tree/1775091ee2fdb683e1e767822e5caa87cdfdba4a/static/assets/optuna_csvs_12)
