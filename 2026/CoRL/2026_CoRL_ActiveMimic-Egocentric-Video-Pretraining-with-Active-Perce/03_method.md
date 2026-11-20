# Method — ActiveMimic: Egocentric Video Pretraining with Active Perception

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## 관측과 출력

움직이는 카메라의 궤적을 배울 행동으로 취급한다.

## 학습·실행 방법

움직이는 카메라의 궤적을 배울 행동으로 취급한다. 로봇에 적응한 후 능동 관측이 필요한 실제 조작 과제에서 비교한다.

- VGGT [40]에서 구한 카메라 경로를 손목 움직임과 정렬해 관측 행동 사전학습의 감독 신호로 사용한다. §3.1. [pr-0056 · 원문](https://arxiv.org/pdf/2606.06194#page=4)
