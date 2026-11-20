# Method — DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## 관측과 출력

여러 중간 층에서 행동을 출력한다.

## 학습·실행 방법

여러 중간 층에서 행동을 출력한다. 평균 계산량과 순간 지연·메모리 요구에 맞춰 종료 조건을 조정한다.

- RoboFlamingo의 시각언어 정책에 중간 행동 출구와 계산 예산 기준을 추가한다. §3, [9]. [pr-0935 · 원문](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b0e7c7c2a5780aeefe3b79caac106e-Paper-Conference.pdf#page=4)
