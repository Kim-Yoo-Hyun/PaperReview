# Insights — RMMBench: A Comprehensive Benchmark for Robotic Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 CoRL 공식 채택 목록과 저자판 PDF 4–9쪽의 과제·과정 지표 및 평가 대조. Full-text scope의 수치·조건만 기록했다.

## Paper-supported conclusion

이동과 조작에 고수준 지시를 적용하고, 실행 중의 국소 위치 정확도·행동 반복·과제 진행을 별도로 기록한다. [원문 및 평가 절](https://arxiv.org/pdf/2610.05414#page=7)

## Researcher interpretation

내비게이션의 위치 오차가 길어진 조작 계획에 어떻게 전파되는지 확인할 평가 자원이다.

- 표 1에서 언어 조건 조작 범위의 비교 대상으로 VLABench를 포함한다. [pr-0788 · 원문](https://arxiv.org/pdf/2610.05414#page=3)

## 최소 비교 실험

배포 지도 조건과 일인칭 영상만 제공하는 조건을 고정 시드에서 비교하고, 성공률과 이동·조작 단계별 완료를 함께 남긴다.
