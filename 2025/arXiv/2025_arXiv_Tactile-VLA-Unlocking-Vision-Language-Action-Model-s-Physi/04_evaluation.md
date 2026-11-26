# Evaluation — Tactile-VLA: Unlocking Vision-Language-Action Model's Physical Knowledge for Tactile Generalization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §2.1–2.3, §3, Tables 1–2 검토. [방법·평가 원문](https://arxiv.org/html/2507.09160)

## 평가 조건

실물 USB·충전기 탈착, 탁상 파지, 보드 닦기에서 평가했다. Table 1에서 제안 모델의 USB/충전기 성공률은 35%/90%로 과제 차이가 크다. 미끄러짐 후 지시를 수정하는 시험은 CoT 변형에 해당한다. [원문 및 평가 절](https://arxiv.org/html/2507.09160)

## 해석할 때 확인할 조건

새 표면에서 미끄럼 회복 효과가 촉각 기반 재추론과 기존 힘 오차 보정 중 어느 쪽에서 오는지는 같은 제어기를 둔 절제로 확인할 수 있다.
