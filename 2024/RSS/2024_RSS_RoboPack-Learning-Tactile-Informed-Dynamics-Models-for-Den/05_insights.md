# Insights — RoboPack: Learning Tactile-Informed Dynamics Models for Dense Packing

> Evidence maturity: `UNREAD`. 이 문서는 읽기 위치와 검증 질문을 정리한 curation note이며, 정독 완료를 뜻하지 않는다.

## Why CORE

이 논문은 **Manipulation, contact, tactile, and dexterity**에서 geometry와 contact mechanics가 sensing, planning, learned control에 들어가는 방식을 비교하기 위한 physical-interaction 기반로 선정됐다.

## Captured Source Cues — Not Yet Independently Verified

- Problem cue: At the same time, tasks such as dense packing present significant challenges due to severe occlusions among objects,
- Method cue: For Non-Prehensile Box Pushing, we present quantitative results in Figure 9 and Table II.
- Result/evaluation cue: We demonstrate our approach on a real robot equipped with a compliant SoftBubble tactile sensor on non-prehensile manipulation and dense packing tasks, where the robot must infer the ...

위 cue는 기존 official abstract 또는 local text extraction에서 보존한 것이다. 수치·조건·인과적 해석은 full-text 정독 전까지 `UNVERIFIED`다.

## Dependency Position

`Tactile-Driven Non-Prehensile Object Manipulation via Extrinsic Contact Mode Control → RoboPack: Learning Tactile-Informed Dynamics Models for Dense Packing → DexTrack: Towards Generalizable Neural Tracking Control for Dexterous Manipulation from Human References`

이 화살표는 reading dependency다. 직접 citation 관계는 references와 related work를 확인한 뒤 synthesis 문서에만 확정한다.

## Close-Reading Checklist

- contact model/state, sensor, action/control mode, embodiment, contact regime, peak force/slip/failure와 real-robot protocol
- 논문이 고정한 가정과 실제 deployment에서 깨질 조건
- strongest baseline과 공정한 비교가 성립하는 조건
- negative result, failure case, compute/data/hardware dependency

## Research Use

- 명시적 contact structure와 learned feedback의 책임 경계를 설계한다.
- 연결 gap: `G-01 / G-03 / G-05` in [RESEARCH_GAPS.md](../../../research/RESEARCH_GAPS.md)

## Minimal Reproduction

동일 contact-rich task에서 success뿐 아니라 peak force, slip, reaction latency와 recovery를 측정한다.

## Promotion Rule

`READ`로 올리려면 method/evaluation 필드를 채우고, `SYNTHESIZED`로 올리려면 같은 track의 선행·후속 논문과 comparison matrix를 갱신한다.
