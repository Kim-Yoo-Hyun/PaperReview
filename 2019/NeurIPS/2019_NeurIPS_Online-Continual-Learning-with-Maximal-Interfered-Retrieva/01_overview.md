# Online Continual Learning with Maximal Interfered Retrieval

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Rahaf Aljundi, Eugene Belilovsky, Tinne Tuytelaars, Laurent Charlin, Massimo Caccia, Min Lin, Lucas Page-Caccia
- Category: Robotics Foundations: Robot Learning
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: continual-learning, replay, robot-learning
- Aliases: MIR, Online Continual Learning with Maximally Interfered Retrieval
- Official paper: https://proceedings.neurips.cc/paper/2019/hash/15825aee15eb335cc13f9b559f166ee8-Abstract.html
- Venue verification: https://proceedings.neurips.cc/paper/2019/hash/15825aee15eb335cc13f9b559f166ee8-Abstract.html
- Code/Project: https://github.com/optimass/Maximally_Interfered_Retrieval
- Code: https://github.com/optimass/Maximally_Interfered_Retrieval
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

Continual 학습에서 과거 memory를 무작위로 고르는 한계를 다룬다.

## Core Idea and Contribution

예상 parameter update 뒤 손실이 많이 증가할 sample을 선택해 replay한다.

## Observation–State–Action Interface

현재 minibatch·stored memory → virtual update → 간섭 score.

## Evaluation Scope and Claim Boundary

Continual learning benchmark에서 경험/생성 replay 비교를 보고한다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper/2019/hash/15825aee15eb335cc13f9b559f166ee8-Abstract.html) · [저자 project/code](https://github.com/optimass/Maximally_Interfered_Retrieval). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

E1에서 loss/gradient interference를 신규 원리로 재주장하지 않게 하는 foundation이다.

## Verification Boundary

virtual step, candidate memory budget, classification과 robot rollout의 차이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
