# HARMONIC: A multimodal dataset of assistive human–robot collaboration

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-20 · IJRR 41(1), 3–11, 2022년 1월호. 온라인 선공개는 2021-12-07이다. 출판사 서지와 본문 §3–6, 공식 텍스트 배포 및 재생 코드를 확인했다.

- Year/Venue: 2022 / IJRR
- Authors: Benjamin A. Newman, Reuben M. Aronson, Siddhartha S. Srinivasa, Kris Kitani, Henny Admoni
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Dataset, shared autonomy, assistive manipulation, teleoperation, multimodal sensing
- Official paper: https://doi.org/10.1177/02783649211050677
- Code/Project: https://harplab.github.io/harmonic/

## 연구 질문과 기여

로봇팔이 사용자의 조작을 보조할 때, 같은 작업 중에 사람이 요청한 움직임과 로봇이 실행하도록 지시받은 움직임을 각각 관찰할 수 있는가?

Kinova Mico를 조이스틱으로 제어해 지정된 음식 위에 포크를 정렬한다. 직접 조작부터 자율 보조까지 네 조건에서 사용자 입력과 목표 추정에 따른 보조 명령을 다른 비중으로 결합한다. 입력 속도, 적용 속도, 관절 상태, 시선과 팔 근전도 등의 스트림을 시각과 함께 배포한다.

## 평가 범위

§3–4와 표 1에 초심자 24명, 네 보조 조건, 식사 보조 480회 시행의 수집 범위와 스트림별 결측을 제시한다. 같은 참가자가 여러 번 시연하므로 사람 간 일반화 평가에서는 참가자 단위로 나눠야 한다. [원문 및 평가 절](https://harplab.github.io/assets/pubs/newman2021_ijrr_harmonic.pdf#page=6)

## 선정 근거

시연자 요청과 적용 명령을 시각별로 분리할 수 있는 실제 공유 제어 데이터셋이다. 시연 재수집의 필요성과 원격조작 로그의 정보 손실을 판별할 때 조회한다.
