# Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

- Year/Venue: 2026 / NeurIPS
- Authors: Bryce Grant, Xijia Zhao, Peng Wang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, mechanistic-interpretability, activation-intervention, feedback
- Official paper: https://arxiv.org/abs/2603.19233
- Venue verification: https://neurips.cc/Downloads/2026
- Code/Project: https://cwru-aism.github.io/vla-interp-page/
- Code: https://github.com/CWRU-AISM/action-atlas
- Source audit: 2026-11-05: v6 (2026-11-02), §4.7–4.8, Appendix B. 지정 본문 절만 확인; 전체 정독·수식 검증 아님. Venue와 읽은 preprint version을 구별. Native 실행 0; 사용자 읽기 UNREAD. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 다른 작업의 내부 활성값을 VLA에 주입해 지시·관측·기록된 운동 궤적 중 무엇이 실제 행동을 좌우하는지 검사한다. [PDF 1쪽](https://arxiv.org/pdf/2603.19233v6#page=1)

## Core Idea and Contribution

- 한 작업에서 기록한 활성값을 다른 장면에 주입해 행동이 어느 과제로 바뀌는지 비교하고 이 영향이 모델 구조에 따라 달라짐을 보였다. [PDF 4쪽](https://arxiv.org/pdf/2603.19233v6#page=4) · [PDF 7쪽](https://arxiv.org/pdf/2603.19233v6#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2603.19233v6#page=8)
- 실물 UR10e에서 기록 때의 물체를 옮긴 뒤에도 로봇이 기억한 위치에서 손을 닫는지 시험해 물체를 추적하는 동작과 위치에 묶인 동작을 구별했다. [PDF 9쪽](https://arxiv.org/pdf/2603.19233v6#page=9) · [PDF 10쪽](https://arxiv.org/pdf/2603.19233v6#page=10)

## Scope and Limitation

하드웨어 결과는 한 모델·task pair에 제한된다. 좌표계 해석과 off-manifold 개입의 영향을 분리해야 한다. 모든 정상 VLA가 피드백을 무시한다는 증거가 아니다.

## Why This Paper Is Here — Researcher Interpretation

FEEDBACK의 출발 근거이자 과장 방지 선행. Activation replay 결과와 자연 정책의 closed-loop 행동을 구별하는 NEXT.

입력·행동은 [method](./03_method.md), 실제 평가 범위는 [evaluation](./04_evaluation.md)을 따른다. 자동 노트는 사용자의 읽기 완료 기록이 아니다.

근거: [확인한 원문](https://arxiv.org/pdf/2603.19233v6), v6 (2026-11-02), §4.7–4.8, Appendix B.
