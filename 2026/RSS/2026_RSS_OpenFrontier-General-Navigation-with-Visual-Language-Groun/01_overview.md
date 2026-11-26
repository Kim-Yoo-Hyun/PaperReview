# OpenFrontier: General Navigation with Visual-Language Grounded Frontiers

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 RSS 게재본 PDF 3–9쪽과 저자 배포 저장소 대조. Full-text scope의 수치·조건만 기록했다.

- Year/Venue: 2026 / RSS
- Authors: Esteban Padilla Cerdio, Boyang Sun, Marc Pollefeys, Hermann Blum
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: Navigation, frontier exploration, vision-language models, zero-shot, RGB-D
- Official paper: https://roboticsproceedings.org/rss22/p067.html
- Code/Project: https://boysun045.github.io/OpenFrontier-Project/
- Code: https://github.com/cvg/OpenFrontier

## 연구 질문과 기여

개방형 언어 목표로 이동하려면 탐색 후보를 관측에 연결하고 현재 지도 밖의 경로도 선택해야 한다.

영상의 frontier를 후보로 만들고 언어 목표와의 관련성을 VLM으로 점수화한다. 후보를 희소한 3D 중간 목표로 유지해 지역 제어와 전역 경로 선택에 사용한다.

## 평가 범위

HM3D·MP3D·OVON의 ObjectNav에서 비교하고 이동 로봇에 배포했다. 기준 비교는 표 Ⅰ, 실패 사례는 그림 10에 있다. [원문 및 평가 절](https://roboticsproceedings.org/rss22/p067.pdf#page=5)

## 선정 근거

학습을 추가하지 않고 3D 관측으로 언어 내비게이션 행동을 개선하는 기준선이다.
