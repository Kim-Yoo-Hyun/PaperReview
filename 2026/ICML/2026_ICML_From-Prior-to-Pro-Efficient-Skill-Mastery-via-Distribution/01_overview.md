# From Prior to Pro: Efficient Skill Mastery via Distribution Contractive RL Finetuning

> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

- Year/Venue: 2026 / ICML
- Authors: Zhanyi Sun, Shuran Song
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: residual-RL, action-chunking, selective-regularization, value-selection
- Aliases: DICE-RL
- Official paper: https://proceedings.mlr.press/v306/sun26al.html
- Venue verification: https://proceedings.mlr.press/v306/sun26al.html
- Code/Project: https://zhanyisun.github.io/dice.rl.2026/
- Code: https://github.com/zhanyisun/dice-rl
- Source audit: 2026-11-03 공식 venue/서지 재확인; 기존 GAP-VRL 검토의 지정 본문 v2 §4; model/rl/distill_residual_rl_img.py selected filter/loss paths를 반영. 선택 절 검토이며 전체 논문 정독·native 실행은 아님. ICML 공식 metadata와 arXiv v2의 지정 절/code를 확인했다. 현재 deterministic TD3·Q-filter 계획을 DICE-RL 전체 재현으로 부르지 않는다. 사용자 읽기 상태는 UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

DICE-RL은 시연으로 훈련한 확산 또는 흐름 정책으로 행동 후보를 만들고 잔차 강화학습을 통해 긴 조작 과제를 개선한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/sun26al/sun26al.pdf#page=1)

## Core Idea and Contribution

- 잔차 정책에 선택적 행동 복제 정규화를 적용하고 여러 잠재 표본에서 얻은 행동 후보를 가치 함수로 평가해 실행할 행동을 고른다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/sun26al/sun26al.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/sun26al/sun26al.pdf#page=4)
- 고차원 시각 입력과 긴 과제에서의 성능을 비교하고 실물 조작 및 구성 요소 제거 실험으로 보정과 행동 선택의 영향을 조사했다. [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/sun26al/sun26al.pdf#page=8) · [PDF 9쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/sun26al/sun26al.pdf#page=9)

## Observation–State–Action Interface

관측 → 동결 prior chunk·residual chunk → value 선택/실행. 학습 regularization과 inference 선택의 역할을 분리한다.

## Evaluation Scope and Limitations

시각 입력의 simulation·실제 로봇 조작을 보고한다. 공개 Robomimic/flow 구현은 OpenVLA/LIBERO adapter가 아니며 그 호환성을 검증하지 않았다.

ICML 공식 metadata와 arXiv v2의 지정 절/code를 확인했다. 현재 deterministic TD3·Q-filter 계획을 DICE-RL 전체 재현으로 부르지 않는다.

근거: [지정 본문](https://arxiv.org/html/2603.10263v2) — v2 §4; model/rl/distill_residual_rl_img.py selected filter/loss paths. Code 검토 revision: `98d936e52523878f0172e606ea32403176497100`; 실행하지 않았다.

## Why This Paper Is Here — Researcher Interpretation

Frozen prior+residual+선택적 모방의 최신 직접 선행이다. 현재 후보의 규칙 조합만으로 독립 방법 기여를 주장하지 않도록 NEXT에 추가한다.

## 공개 자료

- 코드 — 시각 기반 흐름 기본 정책의 잔차 학습 · agent/finetune/train_distill_residual_flow_img_agent.py [배포 파일](https://raw.githubusercontent.com/zhanyisun/dice-rl/98d936e52523878f0172e606ea32403176497100/agent/finetune/train_distill_residual_flow_img_agent.py)
- 가중치·학습 파라미터 — can 영상 조건의 사전학습 기본 정책 · can_img/checkpoint/state_2400.pt [배포 파일](https://huggingface.co/wintermelontree/robomimic-pretrain-checkpoints/resolve/0c2e238cbc35e1629536dea2730024bebf9878c5/can_img/checkpoint/state_2400.pt)
- 데이터 — can 영상 조건 기본 정책 사전학습 자료 · can_img/train.npz [배포 파일](https://huggingface.co/datasets/wintermelontree/robomimic-pretrain-data/resolve/42b55fc6cf7108beb1aaf089a399e32cf5a523d0/can_img/train.npz)
