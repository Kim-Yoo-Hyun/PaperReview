# Cal-QL: Calibrated Offline RL Pre-Training for Efficient Online Fine-Tuning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2023 / NeurIPS
- Authors: Mitsuhiko Nakamoto, Simon Zhai, Anikait Singh, Max Sobol Mark, Yi Ma, Chelsea Finn, Aviral Kumar, Sergey Levine
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: offline-to-online, value-calibration, conservative-learning, fine-tuning
- Aliases: Cal-QL
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2023/hash/c44a04289beaf0a7d968a94066a1d696-Abstract-Conference.html
- Venue verification: https://proceedings.neurips.cc/paper_files/paper/2023/hash/c44a04289beaf0a7d968a94066a1d696-Abstract-Conference.html
- Code/Project: https://nakamotoo.github.io/Cal-QL/
- Code: https://github.com/nakamotoo/Cal-QL
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다.

## Problem and Importance

Offline 정책이 online fine-tuning 시작 때 기존 능력을 잃는 현상을 다룬다.

## Core Idea and Contribution

Conservative value의 scale을 reference policy 가치와 정렬하여 online 갱신에 유용한 초기화를 학습한다.

## Observation–State–Action Interface

Offline data → calibrated conservative critic·정책 → online fine-tuning.

## Evaluation Scope and Claim Boundary

Offline-to-online fine-tuning benchmark를 비교한다. 모든 VLA 보존 문제를 해결했다고 해석하지 않는다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2023/hash/c44a04289beaf0a7d968a94066a1d696-Abstract-Conference.html) · [저자 project/code](https://nakamotoo.github.io/Cal-QL/) · [공식 code](https://github.com/nakamotoo/Cal-QL). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

초기 성능 손실을 semantic forgetting으로만 설명하지 않게 하는 critic calibration baseline이다.

## Verification Boundary

본문에서 확인할 항목: reference return·보수성·초기 탐색·데이터 혼합·성능 회복 비용. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
