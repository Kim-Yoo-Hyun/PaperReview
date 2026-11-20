# Method — HARMONIC: A multimodal dataset of assistive human–robot collaboration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-20 · IJRR 41(1), 3–11, 2022년 1월호. 온라인 선공개는 2021-12-07이다. 출판사 서지와 본문 §3–6, 공식 텍스트 배포 및 재생 코드를 확인했다.

## 관측과 출력

작업 목표와 조이스틱 모드를 기록한다. `input_info.csv`는 조이스틱을 로봇 좌표의 속도로 변환한 값이고 `assistance_info.csv`는 추정 목표와 적용 속도다. 관절 상태는 별도 스트림이며, 링크 위치는 순기구학으로 계산한다.

## 학습·실행 방법

Kinova Mico를 조이스틱으로 제어해 지정된 음식 위에 포크를 정렬한다. 직접 조작부터 자율 보조까지 네 조건에서 사용자 입력과 목표 추정에 따른 보조 명령을 다른 비중으로 결합한다. 입력 속도, 적용 속도, 관절 상태, 시선과 팔 근전도 등의 스트림을 시각과 함께 배포한다.
