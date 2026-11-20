# Evaluation — DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## 평가 조건

CALVIN 장기 지시 조작에서 작업 성능, 연산량과 메모리를 함께 비교했다. [원문 및 평가 절](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b0e7c7c2a5780aeefe3b79caac106e-Paper-Conference.pdf#page=8)

## 해석할 때 확인할 조건

평균 지연을 맞춘 고정 깊이 정책과 실패 직전의 행동 오차를 비교한다.

## 저자가 밝힌 한계

언어 모델 계산량을 줄여도 시각 인코더 비용이 남으며, 평가는 시뮬레이션에 한정됐다. [원문](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b0e7c7c2a5780aeefe3b79caac106e-Paper-Conference.pdf#page=10)
