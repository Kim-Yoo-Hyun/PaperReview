# Method — Tactile-VLA: Unlocking Vision-Language-Action Model's Physical Knowledge for Tactile Generalization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §2.1–2.3, §3, Tables 1–2 검토. [방법·평가 원문](https://arxiv.org/html/2507.09160)

## 관측과 출력

영상·촉각·언어·자세 → 목표 위치와 접촉력. 힘 오차가 임계값을 넘으면 제어기가 위치를 보정한다. 물체에 가하는 외력과 양쪽 손가락 사이 파지력은 각각 손의 위치와 그리퍼 폭으로 조절한다.

## 학습·실행 방법

π0에 촉각 인코더를 붙이고 conditional flow matching으로 목표 위치·접촉력을 함께 학습한다. CoT 변형은 같은 VLM의 디코더가 주기적으로 실패 원인을 해석해 다음 동작 지시를 갱신한다.

- π0의 정책 가중치에서 시작해 촉각 인코더와 위치·힘 행동 전문가를 학습한다. §2.1. [pr-0746 · 원문](https://arxiv.org/html/2507.09160)
