# Method — Active Perception for Grasp Detection via Neural Graspness Field

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## 관측과 출력

여러 관측에서 신경 파지 가능성 필드를 구성한다.

## 학습·실행 방법

여러 관측에서 신경 파지 가능성 필드를 구성한다. 불일치가 큰 방향을 선택해 새 관측을 실제 파지 검출에 반영한다.

- GraspNet-1Billion에서 시점 선택을 평가하는 능동 파지 벤치마크를 구성한다. 실험 설정 및 p.8 Table 1. [pr-0645 · 원문](https://proceedings.neurips.cc/paper_files/paper/2024/file/4364fef031fdf7bfd9d1c9c56b287084-Paper-Conference.pdf#page=6)
