# Contact-Grounded Policy: Dexterous Visuotactile Policy with Generative Contact Grounding

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

- Year/Venue: 2026 / RSS
- Authors: Zhengtong Xu, Yeping Wang, Ben Abbatematteo, Jom Preechayasomboon, Sonny Chan, Nicholas Colonnese, Amirhossein H. Memar
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: tactile sensing, dexterous manipulation, compliance control
- Official paper: https://roboticsproceedings.org/rss22/p005.html
- Code/Project: https://contact-grounded-policy.github.io/

## 연구 질문과 기여

접촉의 미래 상태를 예측해 다지 손의 순응 제어 목표를 만든다.

확산 모델로 로봇 상태와 촉각 궤적을 함께 예측한다. 예측을 제어 목표에 대응시켜 실물·시뮬레이션 손에서 평가한다.

## 평가 범위

물리 Allegro 손과 시뮬레이션 손에서 손안 조작·파지 과업을 비교했다. [원문 및 평가 절](https://roboticsproceedings.org/rss22/p005.pdf#page=6)

## 선정 근거

촉각을 정책의 추가 입력으로 쓰는 경우와 미래 접촉을 실행 제어 목표로 만드는 경우를 직접 비교한다.
