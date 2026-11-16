# EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Policy and Learning Pipeline

EXPO 계열의 editor와 VLA를 함께 갱신하는 chunk 수준 후학습을 사용한다. 공개 update_actor는 actor.train_step을 호출한다.

## Observation, State, and Action

관측·지시 → VLA chunk와 editor → 실행 및 후학습. Image encoder 동결을 전체 VLA 동결로 해석하면 안 된다.

## Training versus Deployment

VLA와 editor가 공동 적응하는 경로 및 intervention·기존 데이터의 역할을 비교 예산에 포함해야 한다.

제어 주기·horizon·loss 계수 전체는 이번 노트에서 확정하지 않았다. 실제 baseline 이식 전 원문과 code 설정을 함께 대조한다.

근거: [지정 본문](https://arxiv.org/html/2605.25477v1) — §4.2–4.3 / Appendix C; expo_ft.py update_actor/_update_jit. Code 검토 revision: `21fe3d3b7d913c80836496817965932f49e0aedf`; 실행하지 않았다.
