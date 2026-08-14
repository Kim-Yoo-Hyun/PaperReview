# Insights — ANYmal Parkour: Learning Agile Navigation for Quadrupedal Robots

> Evidence maturity: `UNREAD`. 이 문서는 읽기 위치와 검증 질문을 정리한 curation note이며, 정독 완료를 뜻하지 않는다.

## Why CORE

이 논문은 **Locomotion, mobile manipulation, and humanoid systems**에서 dynamics adaptation, contact-rich locomotion, whole-body coupling과 embodiment-specific deployment를 비교하기 위한 기반로 선정됐다.

## Captured Source Cues — Not Yet Independently Verified

- Problem cue: In this paper, we propose a fully-learned approach to train such robots and conquer scenarios that are reminiscent of parkour challenges.
- Method cue: In this paper, we propose a fully-learned approach to train such robots and conquer scenarios that are reminiscent of parkour challenges.
- Result/evaluation cue: While these modules are trained from simulated data only, our realworld experiments demonstrate successful transfer on hardware, where the robot navigates and crosses consecutive challenging obstacles with speeds ...

위 cue는 기존 official abstract 또는 local text extraction에서 보존한 것이다. 수치·조건·인과적 해석은 full-text 정독 전까지 `UNVERIFIED`다.

## Dependency Position

`Learning Robust Perceptive Locomotion for Quadrupedal Robots in the Wild → ANYmal Parkour: Learning Agile Navigation for Quadrupedal Robots → HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation`

이 화살표는 reading dependency다. 직접 citation 관계는 references와 related work를 확인한 뒤 synthesis 문서에만 확정한다.

## Close-Reading Checklist

- state/action level, dynamics/contact handling, reward/reference, adaptation signal, sim-to-real protocol, stability와 task metric
- 논문이 고정한 가정과 실제 deployment에서 깨질 조건
- strongest baseline과 공정한 비교가 성립하는 조건
- negative result, failure case, compute/data/hardware dependency

## Research Use

- learned skill과 model-based whole-body constraint 사이의 interface를 설계한다.
- 연결 gap: `G-09 / G-11` in [RESEARCH_GAPS.md](../../../research/RESEARCH_GAPS.md)

## Minimal Reproduction

동일 disturbance set에서 task completion, fall/contact violation, recovery time와 energy를 함께 측정한다.

## Promotion Rule

`READ`로 올리려면 method/evaluation 필드를 채우고, `SYNTHESIZED`로 올리려면 같은 track의 선행·후속 논문과 comparison matrix를 갱신한다.
