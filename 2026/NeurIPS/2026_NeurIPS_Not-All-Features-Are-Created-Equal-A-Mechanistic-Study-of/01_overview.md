# Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

- Year/Venue
- Authors: Bryce Grant, Xijia Zhao, Peng Wang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, mechanistic-interpretability, activation-intervention, feedback
- Official paper: https://arxiv.org/abs/2603.19233
- Venue verification: https://neurips.cc/Downloads/2026
- Code/Project: https://cwru-aism.github.io/vla-interp-page/
- Code: https://github.com/CWRU-AISM/action-atlas
- Source audit: 2026-11-05: v6 (2026-11-02), §4.7–4.8, Appendix B. 지정 본문 절만 확인; 전체 정독·수식 검증 아님. Venue와 읽은 preprint version을 구별. Native 실행 0; 사용자 읽기 UNREAD.

## Problem and Contribution

언어·시각 표현과 실제 운동 생성 사이의 관계를 intervention으로 조사한다.

Sparse autoencoder 분석과 activation 주입으로 task 선택과 motor trajectory 생성 경로를 분해한다.

## Scope and Limitation

하드웨어 결과는 한 모델·task pair에 제한된다. 좌표계 해석과 off-manifold 개입의 영향을 분리해야 한다. 모든 정상 VLA가 피드백을 무시한다는 증거가 아니다.

## Why This Paper Is Here — Researcher Interpretation

FEEDBACK의 출발 근거이자 과장 방지 선행. Activation replay 결과와 자연 정책의 closed-loop 행동을 구별하는 NEXT.

입력·행동은 [method](./03_method.md), 실제 평가 범위는 [evaluation](./04_evaluation.md)을 따른다. 자동 노트는 사용자의 읽기 완료 기록이 아니다.

근거: [확인한 원문](https://arxiv.org/pdf/2603.19233v6), v6 (2026-11-02), §4.7–4.8, Appendix B.
