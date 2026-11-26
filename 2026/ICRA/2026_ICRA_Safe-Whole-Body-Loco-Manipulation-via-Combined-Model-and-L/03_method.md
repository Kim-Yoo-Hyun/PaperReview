# Method — Safe Whole-Body Loco-Manipulation via Combined Model and Learning-based Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 ICRA 서지와 MERL 저자 게재본 PDF 4–9쪽의 제어기·실물 평가 대조. Full-text scope의 수치·조건만 기록했다.

## 관측과 출력

손목 6축 힘·토크와 추정한 베이스 상태를 사용해 팔과 이동 베이스의 속도를 명령한다.

## 학습·실행 방법

손목의 힘·토크를 어드미턴스로 말단 속도에 매핑하고 다리 RL과 팔 제어에 배분한다. Reference Governor가 기준 속도를 허용 범위로 조정한다.
