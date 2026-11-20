# Insights — HumanoidMimicGen: Data Generation for Loco-Manipulation via Whole-Body Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## Paper-supported conclusion

물체 자세가 바뀐 장면으로 접촉 기술을 옮겨 전신 보행·조작 계획과 교차 실행한다. 시뮬레이션 벤치마크 및 생성 데이터 병용 학습을 평가한다. [원문 및 평가 절](https://arxiv.org/pdf/2605.27724#page=7)

## Researcher interpretation

전신 계획으로 이동 조작 시연을 만드는 기법과 휴머노이드용 시뮬레이션 벤치마크를 함께 제공한다.

- MimicGen의 소수 시연 기반 데이터 생성을 이동 보행과 전신 계획에 확장한다. §2 및 p.7 Table 1. [pr-0637 · 원문](https://arxiv.org/pdf/2605.27724#page=2)

## 최소 비교 실험

동일 원시 시연으로 전신 계획만 제거했을 때 배치별 시연 생성 성공률을 비교한다.
