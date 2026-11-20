# Insights — PTLD: Sim-to-real Privileged Tactile Latent Distillation for Dexterous Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## Paper-supported conclusion

보조 관측이 가능한 교사와 촉각 학생의 학습·배포 입력을 분리한다. 시뮬레이션에서 학습한 손안 조작 정책을 실제 회전과 목표 자세 재정렬에서 시험한다. [원문 및 평가 절](https://arxiv.org/pdf/2603.04531#page=6)

## Researcher interpretation

실물의 특권 관측을 학습 때만 사용해 촉각 상태 추정기를 증류하는 전이 기준이다.

- DAgger [50]로 학생 정책의 상태 분포에서 자료를 다시 모아 촉각 추정기를 증류한다. Distillation. [pr-0522 · 원문](https://arxiv.org/pdf/2603.04531#page=5)

## 최소 비교 실험

같은 실물 데이터에서 특권 자세 감독과 촉각 관측 각각의 기여를 비교한다.
