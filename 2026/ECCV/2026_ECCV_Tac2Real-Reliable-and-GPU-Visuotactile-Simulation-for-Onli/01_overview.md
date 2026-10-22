# Tac2Real: Reliable and GPU Visuotactile Simulation for Online Reinforcement Learning and Zero-Shot Real-World Deployment

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ECCV
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: visuotactile, contact-rich, sim-to-real
- Aliases: Tac2Real
- Official paper: https://arxiv.org/abs/2603.28475
- Venue verification: https://eccv.ecva.net/Conferences/2026/AcceptedPapers
- Code/Project: https://ningyurichard.github.io/tac2real-project-page/
- Code: not_released
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요. ECCV 2026 accepted/video list의 공식 검색 색인과 저자 abstract 대조; proceedings page/DOI 미확인.

## Problem and Importance

Visuotactile online RL simulation에서 contact physics fidelity와 GPU throughput을 동시에 확보하는 문제다.

## Core Idea and Contribution

PNCG-IPC 기반 tactile simulation, multi-GPU 병렬화 및 TacAlign sim-to-real alignment를 결합한다.

## Observation–State–Action Interface

Contact dynamics → tactile marker displacement/visual signal → RL policy → insertion action.

## Evaluation Scope and Claim Boundary

공식 abstract/project는 contact-rich peg insertion의 zero-shot real-world transfer 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2603.28475) · [저자 project/code](https://ningyurichard.github.io/tac2real-project-page/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Current trend / simulator. Tactile feedback을 이용하는 insertion·contact RL을 선택할 때 relevant하다. HIL-SERL 등 실제 interaction 학습과 simulation fidelity/transfer를 비교한다. Peg insertion 결과를 범용 dexterity로 확대하지 않는다.

## Verification Boundary

Tactile sensor calibration, contact parameter 분포, marker fidelity와 code 공개 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
