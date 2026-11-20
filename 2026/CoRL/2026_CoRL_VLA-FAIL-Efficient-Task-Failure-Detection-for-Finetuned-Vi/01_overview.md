# VLA-FAIL: Efficient Task Failure Detection for Finetuned Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

- Year/Venue: 2026 / CoRL
- Authors: Florian Seligmann, Emiliyan Gospodinov, Enes Ulas Dincer, Gerhard Neumann
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: VLA, failure detection, action chunking
- Official paper: https://arxiv.org/abs/2606.21386
- Code/Project: https://vla-fail.github.io/vla-fail-2026

## 연구 질문과 기여

미세조정한 VLA의 실행 실패를 가벼운 감지기로 추적한다.

계산 비용이 큰 반복 행동 표집을 줄이는 실패 신호를 검토한다. 서로 다른 실패 양상을 포착하는 신호의 결합을 평가한다.

## 평가 범위

실제 조작 및 LIBERO-Plus에서 정책 특징 거리·행동 청크 일관성·기존 감지기를 비교했다. [원문 및 평가 절](https://arxiv.org/pdf/2606.21386#page=6)

## 선정 근거

실패 감지의 정확도와 알림 시간을 함께 평가하는 지표와 VLA용 감지 기준을 제공한다.
