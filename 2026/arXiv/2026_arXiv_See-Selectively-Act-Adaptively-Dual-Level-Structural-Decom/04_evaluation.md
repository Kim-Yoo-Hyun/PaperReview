# Evaluation — See Selectively, Act Adaptively: Dual-Level Structural Decomposition for Bimanual Robot Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`

2026-11-20에 저자 본문 v2의 III–IV절을 확인했다. [논문 정보와 출처](./01_overview.md)

- **Evaluation type:** `simulation and real-robot manipulation`.

## Dataset / Benchmark Role

RoboTwin 2.0의 여섯 과제는 Easy 시연을 작업당 50개씩 이용하고 Easy/Hard에서 평가했다. 실물 장기 조작 세 과제는 작업당 시연 40개를 이용했다. [실험 설정](https://arxiv.org/html/2606.13279v2#S4.SS1)

## Experimental Matrix

| 평가 조건 | 과제당 반복 |
|---|---|
| RoboTwin | 100 rollouts |
| 실물 양팔 시스템 | 10 trials |

## Metrics and Success Definition

저자들은 과제별 완수율과 여섯 시뮬레이션 과제의 평균을 보고했다. [표 I](https://arxiv.org/html/2606.13279v2#S4.SS2)

## Baselines and Fairness

| 6과제 평균 완수율 | 같은 π₀.₅ 단일 경로 | 시각 선택 + 행동 모드 선택 |
|---|---:|---:|
| Easy | 61.5% | 81.2% |
| Hard | 22.3% | 58.0% |

## Ablations and Sensitivity

LoRA 용량 증가, 행동 모듈 단독, 영상 모듈 단독, 전문가별 뷰 마스크 제거 대조가 있다. 표의 효과에는 영상과 행동 양측의 변경이 포함된다. [표 I–II와 대조](https://arxiv.org/html/2606.13279v2#S4.SS2)

## Generalization and Failure Cases

실물 결과와 단계별 라우팅 분석은 미지 물체·방해물과 전환 오류의 영향을 함께 살핀다. 온라인 상호작용 수에 따른 학습 곡선은 이 비교의 지표에 포함되지 않는다. [저자 결과와 영상](https://choiyoonji.github.io/See-Selectively-Act-Adaptively/)
