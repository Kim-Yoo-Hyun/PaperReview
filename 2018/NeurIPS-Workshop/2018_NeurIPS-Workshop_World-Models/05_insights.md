# Insights — World Models

> Evidence maturity: `UNREAD`. 이 문서는 읽기 위치와 검증 질문을 정리한 curation note이며, 정독 완료를 뜻하지 않는다.

## Why CORE

이 논문은 **Safety and robot world models**에서 prediction, uncertainty, constraint, monitoring와 recovery를 서로 다른 safety interface로 구분하기 위한 기반로 선정됐다.

## Captured Source Cues — Not Yet Independently Verified

- Problem cue: We explore building generative neural network models of popular reinforcement learning environments.
- Method cue: We explore building generative neural network models of popular reinforcement learning environments.
- Result/evaluation cue: We explore building generative neural network models of popular reinforcement learning environments.

위 cue는 기존 official abstract 또는 local text extraction에서 보존한 것이다. 수치·조건·인과적 해석은 full-text 정독 전까지 `UNVERIFIED`다.

## Dependency Position

`이 track의 출발점 → World Models → DayDreamer: World Models for Physical Robot Learning`

이 화살표는 reading dependency다. 직접 citation 관계는 references와 related work를 확인한 뒤 synthesis 문서에만 확정한다.

## Close-Reading Checklist

- model state/target, uncertainty definition, horizon, policy/planner coupling, calibration, intervention와 recovery outcome
- 논문이 고정한 가정과 실제 deployment에서 깨질 조건
- strongest baseline과 공정한 비교가 성립하는 조건
- negative result, failure case, compute/data/hardware dependency

## Research Use

- 예측 정확도나 detector score를 실제 action selection과 safety constraint로 연결한다.
- 연결 gap: `G-02 / G-07 / G-08` in [RESEARCH_GAPS.md](../../../research/RESEARCH_GAPS.md)

## Minimal Reproduction

통제된 perturbation에서 calibration, unsafe proposal, intervention cost와 최종 recovery success를 함께 측정한다.

## Promotion Rule

`READ`로 올리려면 method/evaluation 필드를 채우고, `SYNTHESIZED`로 올리려면 같은 track의 선행·후속 논문과 comparison matrix를 갱신한다.
