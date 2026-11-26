# Insights — Tactile-VLA: Unlocking Vision-Language-Action Model's Physical Knowledge for Tactile Generalization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §2.1–2.3, §3, Tables 1–2 검토. [방법·평가 원문](https://arxiv.org/html/2507.09160)

## Paper-supported conclusion

π0에 촉각 인코더를 붙이고 conditional flow matching으로 목표 위치·접촉력을 함께 학습한다. CoT 변형은 같은 VLM의 디코더가 주기적으로 실패 원인을 해석해 다음 동작 지시를 갱신한다. [원문 및 평가 절](https://arxiv.org/html/2507.09160)

## Researcher interpretation

Tabero와 함께 촉각 표현을 실제 힘 목표까지 연결한다. 미끄러짐을 감지해 힘의 방향이나 파지 세기를 바꾸는 사례로 재사용할 수 있다.

- π0의 정책 가중치에서 시작해 촉각 인코더와 위치·힘 행동 전문가를 학습한다. §2.1. [pr-0746 · 원문](https://arxiv.org/html/2507.09160)

## 최소 비교 실험

힘 제어기와 닦기 경로를 고정하고 촉각 기반 지시 갱신만 켜거나 끈다. 미끄럼 후 다시 접촉하는 비율과 정상 방향의 최대 힘을 함께 비교한다.

## 검증 질문

새 표면에서 미끄럼 회복 효과가 촉각 기반 재추론과 기존 힘 오차 보정 중 어느 쪽에서 오는지는 같은 제어기를 둔 절제로 확인할 수 있다.
