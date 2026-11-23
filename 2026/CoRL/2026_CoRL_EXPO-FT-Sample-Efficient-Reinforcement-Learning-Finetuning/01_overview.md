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
- Source audit: 2026-11-03 공식 venue/서지 재확인; 기존 GAP-VRL 검토의 지정 본문 §4.2–4.3 / Appendix C; expo_ft.py update_actor/_update_jit를 반영. 선택 절 검토이며 전체 논문 정독·native 실행은 아님. CoRL accepted list와 arXiv v1/code를 별도로 확인했다. 최종본 동일성·native 실행·독립 release 교체 효과는 미검증이다. 사용자 읽기 상태는 UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

EXPO-FT는 사전학습 VLA가 만든 행동 묶음을 편집하고 가치로 선별해 실제 로봇 상호작용으로 조작 정책을 개선한다. [PDF 1쪽](https://arxiv.org/pdf/2605.25477v2#page=1) · [PDF 3쪽](https://arxiv.org/pdf/2605.25477v2#page=3)

## Core Idea and Contribution

- 가벼운 편집 정책과 행동 묶음 가치 함수를 함께 학습하고 온라인 자료를 사용해 기본 정책도 갱신한다. [PDF 3쪽](https://arxiv.org/pdf/2605.25477v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2605.25477v2#page=4)
- 줄 조명 배선·당구·꽃 꽂기 등을 포함한 실물 과제 여덟 개에서 각각 30회 중 30회 성공했으며, 과제당 온라인 로봇 자료는 평균 19.1분이었다. [PDF 9쪽](https://arxiv.org/pdf/2605.25477v2#page=9)

## Observation–State–Action Interface

관측·지시 → VLA chunk와 editor → 실행 및 후학습. Image encoder 동결을 전체 VLA 동결로 해석하면 안 된다.

## Evaluation Scope and Limitations

실제 로봇을 위한 DROID/π0.5 공개 경로와 human intervention을 포함하는 구성을 확인했다. 이 release는 LIBERO/OpenVLA의 즉시 실행 baseline이 아니다.

CoRL accepted list와 arXiv v1/code를 별도로 확인했다. 최종본 동일성·native 실행·독립 release 교체 효과는 미검증이다.

근거: [지정 본문](https://arxiv.org/html/2605.25477v1) — §4.2–4.3 / Appendix C; expo_ft.py update_actor/_update_jit. Code 검토 revision: `21fe3d3b7d913c80836496817965932f49e0aedf`; 실행하지 않았다.

## Why This Paper Is Here — Researcher Interpretation

현재 VLA+RL 후보의 가장 가까운 공동 적응 baseline이다. 독립 base 갱신과 editor 공동 학습을 구별할 NEXT다.
