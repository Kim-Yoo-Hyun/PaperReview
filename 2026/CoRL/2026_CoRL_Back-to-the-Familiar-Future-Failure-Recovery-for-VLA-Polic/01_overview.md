# Back to the Familiar Future: Failure Recovery for VLA Policies via Pre-Imagined Milestone Selection

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

- Year/Venue: 2026 / CoRL
- Authors: Suyeon Shin, Juwon Kim, Hyeonbin Park, Hyunseo Kim, Hyundo Lee, Hyung-Sin Kim, Byoung-Tak Zhang
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: VLA, failure recovery, visual goals
- Official paper: https://arxiv.org/abs/2606.09258
- Code/Project: not identified

## 연구 질문과 기여

실행 전 상상한 시각적 이정표에서 복구 목표를 선택해 VLA를 재조건화한다.

예정 경로에서 벗어난 상태를 미래 시각 조건으로 되돌려 연결한다. 하위 행동 생성기의 추가 미세조정 없이 복구를 평가한다.

## 평가 범위

기본 LIBERO와 실패 주입 LIBERO를 구분했다. 주입 시점에 맞춘 복구 수치는 독립적인 실패 감지 성능을 포함하지 않는다. [원문 및 평가 절](https://arxiv.org/pdf/2606.09258#page=6)

## 선정 근거

복구가 가능한 시점에서 미래 시각 목표만 바꾸는 대조군을 제공한다.
