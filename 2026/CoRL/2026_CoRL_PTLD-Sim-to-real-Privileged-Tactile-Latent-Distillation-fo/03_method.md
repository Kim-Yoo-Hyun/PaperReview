# Method — PTLD: Sim-to-real Privileged Tactile Latent Distillation for Dexterous Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## 관측과 출력

보조 관측이 가능한 교사와 촉각 학생의 학습·배포 입력을 분리한다.

## 학습·실행 방법

보조 관측이 가능한 교사와 촉각 학생의 학습·배포 입력을 분리한다. 시뮬레이션에서 학습한 손안 조작 정책을 실제 회전과 목표 자세 재정렬에서 시험한다.

- DAgger [50]로 학생 정책의 상태 분포에서 자료를 다시 모아 촉각 추정기를 증류한다. Distillation. [pr-0522 · 원문](https://arxiv.org/pdf/2603.04531#page=5)
