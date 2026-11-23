# Accelerating Residual Reinforcement Learning With Uncertainty Estimation

> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

- Year/Venue: 2026 / RA-L
- Authors: Lakshita Dodeja, Karl Schmeckpeper, Shivam Vats, Thomas Weng, Mingxi Jia, George Konidaris, Stefanie Tellex
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: residual-RL, uncertainty, exploration, manipulation
- Aliases: Uncertainty-Aware Residual RL
- Official paper: https://api.crossref.org/works/10.1109/LRA.2025.3636808
- Venue verification: https://api.crossref.org/works/10.1109/LRA.2025.3636808
- Code/Project: https://lakshitadodeja.github.io/uncertainty-aware-residual-rl/
- Code: https://github.com/lakshitadodeja/uncertainty_aware_residual_rl
- Source audit: 2026-11-03 공식 venue/서지 재확인; 기존 GAP-VRL 검토의 지정 본문 v2 IV-B / V-D; assymetric_sac.py critic_loss_fn/actor complete-action path를 반영. 선택 절 검토이며 전체 논문 정독·native 실행은 아님. IEEE 직접 페이지는 접근 제약이 있어 publisher-deposited Crossref와 저자 accepted 표기로 RA-L 11(1), 2026을 확인했다. 2025 DOI/채택일을 issue 연도와 혼동하지 않는다. 사용자 읽기 상태는 UNREAD 유지.

## Problem and Importance

Residual RL의 탐색을 base 정책의 불확실성에 맞춰 조절해 상호작용 효율을 개선하는 문제다.

## Core Idea and Contribution

불확실성 기반 탐색 제어를 사용한다. 확인한 critic 구현은 base와 residual이 합쳐진 최종 행동을 평가한다.

## Observation–State–Action Interface

Base 예측·불확실성 및 관측 → residual 탐색 → 합성 행동 → Q 평가. Critic 입력에 base action을 반영하는 원리는 이미 선행에 있다.

## Evaluation Scope and Limitations

Robosuite·D4RL 비교와 sim-to-real 적용을 보고한다. 여기서는 combined-action critic 경로를 확인했으며 수치·seed·현실 성공률을 재현하지 않았다.

IEEE 직접 페이지는 접근 제약이 있어 publisher-deposited Crossref와 저자 accepted 표기로 RA-L 11(1), 2026을 확인했다. 2025 DOI/채택일을 issue 연도와 혼동하지 않는다.

근거: [지정 본문](https://arxiv.org/html/2506.17564v2) — v2 IV-B / V-D; assymetric_sac.py critic_loss_fn/actor complete-action path. Code 검토 revision: `8125f33dcf490d4cf93d57a27d3e1963a47f52ea`; 실행하지 않았다.

## Why This Paper Is Here — Researcher Interpretation

현재 후보의 critic mismatch 대안을 검토할 직접 선행이다. 합성 행동 critic을 새 알고리즘으로 재주장하지 않도록 NEXT에 등록한다.
