# EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

- Year/Venue: 2026 / CoRL
- Authors: Perry Dong, Kuo-Han Hung, Tian Gao, Dorsa Sadigh, Chelsea Finn
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, reinforcement-learning, action-chunking, residual-policy
- Aliases: EXPO-FT
- Official paper: https://arxiv.org/abs/2605.25477
- Venue verification: https://www.corl.org/program/accepted-papers
- Code/Project: https://pd-perry.github.io/expo-ft/
- Code: https://github.com/pd-perry/expo-ft
- Source audit: 2026-11-03 공식 venue/서지 재확인; 기존 GAP-VRL 검토의 지정 본문 §4.2–4.3 / Appendix C; expo_ft.py update_actor/_update_jit를 반영. 선택 절 검토이며 전체 논문 정독·native 실행은 아님. CoRL accepted list와 arXiv v1/code를 별도로 확인했다. 최종본 동일성·native 실행·독립 release 교체 효과는 미검증이다. 사용자 읽기 상태는 UNREAD 유지.

## Problem and Importance

대규모 VLA를 적은 online 상호작용으로 적응시키면서 chunk 행동의 표현력을 활용하는 문제다.

## Core Idea and Contribution

EXPO 계열의 editor와 VLA를 함께 갱신하는 chunk 수준 후학습을 사용한다. 공개 update_actor는 actor.train_step을 호출한다.

## Observation–State–Action Interface

관측·지시 → VLA chunk와 editor → 실행 및 후학습. Image encoder 동결을 전체 VLA 동결로 해석하면 안 된다.

## Evaluation Scope and Limitations

실제 로봇을 위한 DROID/π0.5 공개 경로와 human intervention을 포함하는 구성을 확인했다. 이 release는 LIBERO/OpenVLA의 즉시 실행 baseline이 아니다.

CoRL accepted list와 arXiv v1/code를 별도로 확인했다. 최종본 동일성·native 실행·독립 release 교체 효과는 미검증이다.

근거: [지정 본문](https://arxiv.org/html/2605.25477v1) — §4.2–4.3 / Appendix C; expo_ft.py update_actor/_update_jit. Code 검토 revision: `21fe3d3b7d913c80836496817965932f49e0aedf`; 실행하지 않았다.

## Why This Paper Is Here — Researcher Interpretation

현재 VLA+RL 후보의 가장 가까운 공동 적응 baseline이다. 독립 base 갱신과 editor 공동 학습을 구별할 NEXT다.
