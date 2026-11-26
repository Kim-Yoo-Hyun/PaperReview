# Method — Learning Force-Reactive Humanoid Loco-Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 arXiv PDF 2–8쪽의 힘 관측·명령 어블레이션과 저자 코드. 게재 확정은 확인되지 않음 대조. Full-text scope의 수치·조건만 기록했다.

## 관측과 출력

영상, 고유수용감각과 양손 힘·토크를 사용해 자세 변화와 손별 힘 명령을 함께 출력한다.

## 학습·실행 방법

휴대형 힘 센서 그리퍼와 착용형 추적기로 시연을 얻는다. 확산 정책이 양손 힘과 운동 명령을 예측하며, 전신 제어기가 손목의 힘 오차를 적분해 명령 방향의 힘을 추종한다.
