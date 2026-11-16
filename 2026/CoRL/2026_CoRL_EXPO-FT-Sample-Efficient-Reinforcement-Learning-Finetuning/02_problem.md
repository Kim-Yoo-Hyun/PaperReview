# EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Problem and Bottleneck

대규모 VLA를 적은 online 상호작용으로 적응시키면서 chunk 행동의 표현력을 활용하는 문제다.

## Changed Formulation

EXPO 계열의 editor와 VLA를 함께 갱신하는 chunk 수준 후학습을 사용한다. 공개 update_actor는 actor.train_step을 호출한다.

## Assumptions and Robotics Loop

VLA와 editor가 공동 적응하는 경로 및 intervention·기존 데이터의 역할을 비교 예산에 포함해야 한다.

관측·지시 → VLA chunk와 editor → 실행 및 후학습. Image encoder 동결을 전체 VLA 동결로 해석하면 안 된다.

근거: [지정 본문](https://arxiv.org/html/2605.25477v1) — §4.2–4.3 / Appendix C; expo_ft.py update_actor/_update_jit. Code 검토 revision: `21fe3d3b7d913c80836496817965932f49e0aedf`; 실행하지 않았다.
