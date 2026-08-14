# Insights — TrajOpt: A Sequential Convex Optimization Algorithm for Robot Motion Planning

> Evidence maturity: `UNREAD`. 이 문서는 읽기 위치와 검증 질문을 정리한 curation note이며, 정독 완료를 뜻하지 않는다.

## Why CORE

이 논문은 **Planning, control, and whole-body foundations**에서 feasibility, constraint handling, search/optimization, and feedback control을 구분하기 위한 robotics 좌표계로 선정됐다.

## Captured Source Cues — Not Yet Independently Verified

- Problem cue: So, at the present time the general state of the GRB problem and progress in this field could be categorized in the following way: 1) GRBs belong to ...
- Method cue: Gamma-ray bursts (GRBs) are the brief (~0.01-100s), intense flashes of γ-rays (mostly sub-MeV) with enormous electromagnetic energy release up to ~1051-1054 ergs.
- Result/evaluation cue: UNVERIFIED — full-text close reading에서 paper-supported cue를 기록한다.

위 cue는 기존 official abstract 또는 local text extraction에서 보존한 것이다. 수치·조건·인과적 해석은 full-text 정독 전까지 `UNVERIFIED`다.

## Dependency Position

`CHOMP: Gradient Optimization Techniques for Efficient Motion Planning → TrajOpt: A Sequential Convex Optimization Algorithm for Robot Motion Planning → PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning`

이 화살표는 reading dependency다. 직접 citation 관계는 references와 related work를 확인한 뒤 synthesis 문서에만 확정한다.

## Close-Reading Checklist

- state와 dynamics model, decision variable, constraint, convergence/completeness 성질, planning/control rate, failure case
- 논문이 고정한 가정과 실제 deployment에서 깨질 조건
- strongest baseline과 공정한 비교가 성립하는 조건
- negative result, failure case, compute/data/hardware dependency

## Research Use

- 학습 정책이 맡을 부분과 명시적 planner/controller가 유지해야 할 부분을 분리한다.
- 연결 gap: `G-01 / G-09` in [RESEARCH_GAPS.md](../../../research/RESEARCH_GAPS.md)

## Minimal Reproduction

대표 저차원 task에서 feasible rate, solve time, trajectory cost와 disturbance 후 replanning을 비교한다.

## Promotion Rule

`READ`로 올리려면 method/evaluation 필드를 채우고, `SYNTHESIZED`로 올리려면 같은 track의 선행·후속 논문과 comparison matrix를 갱신한다.
