# HydroShear: Hydroelastic Shear Simulation for Tactile Sim-to-Real Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 RSS 게재본 PDF 3–9쪽에서 전단 모델, 센서 보정 및 표 Ⅱ 대조. Full-text scope의 수치·조건만 기록했다.

- Year/Venue: 2026 / RSS
- Authors: An Thanh Dang, Jayjun Lee, Mustafa Mukadam, X. Alice Wu, Bernadette Bucher, Manikantan Nambi, Nima Fazeli
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: tactile simulation, contact, slip, sim-to-real, Reinforcement Learning
- Official paper: https://roboticsproceedings.org/rss22/p155.html
- Code/Project: https://hydroshear.github.io/
- Code: https://github.com/MMintLab/hydroshear

## 연구 질문과 기여

정상력과 접촉 이미지만으로는 센서 막이 미끄러지거나 전단을 누적하는 과정을 놓치기 쉽다.

함몰 물체 표면의 변위를 SDF로 추적하고 이력에 따라 축적된 전단과 붙었다 미끄러지는 전이를 모의한다. 이 전단 관측을 사용하는 정책을 시뮬레이션에서 강화학습한다.

## 평가 범위

GelSight Mini에서 전단 예측을 검증한 뒤 삽입, 상자 담기, 책 끼우기, 서랍 당기기를 실물에서 평가했다. 표 Ⅱ는 같은 과제의 촉각 영상과 다른 전단 모델 기준을 제공한다. [원문 및 평가 절](https://roboticsproceedings.org/rss22/p155.pdf#page=9)

## 선정 근거

서랍 같은 미끄럼 과제에서 촉각 모델의 물리적 차이가 실물 정책에 전달되는지 비교할 수 있다.
