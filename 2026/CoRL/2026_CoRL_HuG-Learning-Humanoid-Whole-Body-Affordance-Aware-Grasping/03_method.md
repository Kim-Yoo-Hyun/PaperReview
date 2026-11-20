# Method — HuG: Learning Humanoid Whole-Body Affordance-Aware Grasping with Active Perception

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## 관측과 출력

전신 동역학 검사로 기구학적으로 가능한 파지 후보를 다시 선별한다.

## 학습·실행 방법

전신 동역학 검사로 기구학적으로 가능한 파지 후보를 다시 선별한다. 선반의 여러 높이에서 실물 파지, 분포 밖 높이에서 시뮬레이션 전이를 구분해 평가한다.

- 저수준 보행에 SONIC [38]을 사용해 상위에서 만든 하체 명령을 추종한다. Whole-body control. [pr-0872 · 원문](https://arxiv.org/pdf/2611.01659#page=5)
