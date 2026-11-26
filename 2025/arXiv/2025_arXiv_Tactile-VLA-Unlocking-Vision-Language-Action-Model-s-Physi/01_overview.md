# Tactile-VLA: Unlocking Vision-Language-Action Model's Physical Knowledge for Tactile Generalization

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §2.1–2.3, §3, Tables 1–2 검토. [방법·평가 원문](https://arxiv.org/html/2507.09160)

- Year/Venue: 2025 / arXiv
- Authors: Jialei Huang, Shuo Wang, Fanqi Lin, Yihang Hu, Chuan Wen, Yang Gao
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: VLA, tactile sensing, hybrid force-position control, Flow Matching, slip
- Official paper: https://arxiv.org/abs/2507.09160
- Code/Project: https://jialeihuang.github.io/tactileVLA.github.io/

## 연구 질문과 기여

물체와 경로가 같아도 표현의 세기와 미끄러짐에 따라 파지력이나 누르는 힘을 바꿔야 한다.

π0에 촉각 인코더를 붙이고 conditional flow matching으로 목표 위치·접촉력을 함께 학습한다. CoT 변형은 같은 VLM의 디코더가 주기적으로 실패 원인을 해석해 다음 동작 지시를 갱신한다.

## 정책 출력

영상·촉각·언어·자세 → 목표 위치와 접촉력. 힘 오차가 임계값을 넘으면 제어기가 위치를 보정한다. 물체에 가하는 외력과 양쪽 손가락 사이 파지력은 각각 손의 위치와 그리퍼 폭으로 조절한다. [방법 원문](https://arxiv.org/html/2507.09160)

## 평가 범위

실물 USB·충전기 탈착, 탁상 파지, 보드 닦기에서 평가했다. Table 1에서 제안 모델의 USB/충전기 성공률은 35%/90%로 과제 차이가 크다. 미끄러짐 후 지시를 수정하는 시험은 CoT 변형에 해당한다. [원문 및 평가 절](https://arxiv.org/html/2507.09160)

## 선정 근거

Tabero와 함께 촉각 표현을 실제 힘 목표까지 연결한다. 미끄러짐을 감지해 힘의 방향이나 파지 세기를 바꾸는 사례로 재사용할 수 있다.
