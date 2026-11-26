# Method — TactileStep: Sole Tactile Learning for Regulating Foot–Terrain Interaction in Humanoid Locomotion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 CoRL 공식 채택·Spotlight S7과 저자판 PDF 3–9쪽의 학습·실물 표 3 대조. Full-text scope의 수치·조건만 기록했다.

## 관측과 출력

발바닥 압력 기반 특징과 로봇 운동 정보를 사용해 보행 관절 명령을 생성한다.

## 학습·실행 방법

발 접촉을 압력 배열로 바꾸는 모의 센서를 구성하고 실물 깔창과 같은 접촉 특징을 정책이 읽게 한다. 접지 위상별 보상은 착지 충격과 지지 상태를 따로 조절한다.
