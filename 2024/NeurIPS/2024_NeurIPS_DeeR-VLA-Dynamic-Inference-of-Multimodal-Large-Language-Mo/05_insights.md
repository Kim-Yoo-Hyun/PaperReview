# Insights — DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## Paper-supported conclusion

여러 중간 층에서 행동을 출력한다. 평균 계산량과 순간 지연·메모리 요구에 맞춰 종료 조건을 조정한다. [원문 및 평가 절](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b0e7c7c2a5780aeefe3b79caac106e-Paper-Conference.pdf#page=8)

## Researcher interpretation

계산 예산에 따라 같은 VLA의 실행 깊이를 바꾸는 비교 기준이다.

- RoboFlamingo의 시각언어 정책에 중간 행동 출구와 계산 예산 기준을 추가한다. §3, [9]. [pr-0935 · 원문](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b0e7c7c2a5780aeefe3b79caac106e-Paper-Conference.pdf#page=4)

## 최소 비교 실험

평균 지연을 맞춘 고정 깊이 정책과 실패 직전의 행동 오차를 비교한다.
