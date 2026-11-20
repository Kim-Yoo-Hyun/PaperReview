# Insights — Active Perception for Grasp Detection via Neural Graspness Field

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## Paper-supported conclusion

여러 관측에서 신경 파지 가능성 필드를 구성한다. 불일치가 큰 방향을 선택해 새 관측을 실제 파지 검출에 반영한다. [원문 및 평가 절](https://proceedings.neurips.cc/paper_files/paper/2024/file/4364fef031fdf7bfd9d1c9c56b287084-Paper-Conference.pdf#page=8)

## Researcher interpretation

재구성 품질 대신 파지 목표에 대한 불확실성으로 카메라 시점을 고르는 기준이다.

- GraspNet-1Billion에서 시점 선택을 평가하는 능동 파지 벤치마크를 구성한다. 실험 설정 및 p.8 Table 1. [pr-0645 · 원문](https://proceedings.neurips.cc/paper_files/paper/2024/file/4364fef031fdf7bfd9d1c9c56b287084-Paper-Conference.pdf#page=6)

## 최소 비교 실험

동일한 이동 횟수에서 표면 커버리지 기준과 파지 불일치 기준을 대조한다.
