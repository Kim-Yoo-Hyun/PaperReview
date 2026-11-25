# DyGRO-VLA: Cross-Task Scaling of Vision–Language–Action Models via Dynamic Grouped Residual Optimization

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICML
- Authors: Sixu Lin, Yunpeng Qing, Litao Liu, Ming Zhou, Ruixing Jin, Xiaoyi Fan, Guiliang Liu
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: multitask-RL, residual-policy, generalization
- Aliases: DyGRO-VLA
- Official paper: https://proceedings.mlr.press/v306/lin26af.html
- Venue verification: https://proceedings.mlr.press/v306/lin26af.html
- Code/Project: https://edem-ai.github.io/DyGRO-VLA/
- Code: project_only
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

DyGRO-VLA는 여러 과제에 공통인 표현을 먼저 학습하고 강화학습 단계에서 과제별 보정을 선택해 공동 학습의 간섭을 줄인다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/lin26af/lin26af.pdf#page=1)

## Core Idea and Contribution

- 정보이론적 기준으로 오프라인 표현을 학습한 뒤 여러 잔차 모듈을 조합해 온라인 정책을 갱신한다. [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/lin26af/lin26af.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/lin26af/lin26af.pdf#page=5)
- LIBERO·RoboTwin과 실제 조작에서 다중 과제 학습을 평가하고 전문가 수와 온라인 학습 설정을 바꿔 비교했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/lin26af/lin26af.pdf#page=6) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/lin26af/lin26af.pdf#page=8)

## Observation–State–Action Interface

VLA observation/language → cross-task latent features 및 residual policy update → robot action.

## Evaluation Scope and Claim Boundary

ICML abstract는 LIBERO, RoboTwin2와 real-world 평가 및 multitask/distribution-shift 조건을 명시한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v306/lin26af.html) · [저자 project/code](https://github.com/EDEM-AI/DyGRO-VLA). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Current trend. RL fine-tuning 중 task-specific overfitting을 줄이는 것이 연구 질문일 때 RL4VLA/ConRFT와 비교한다. 새 architecture라는 이유만으로 CORE로 올리지는 않는다.

## Verification Boundary

Task grouping, residual routing, representation loss와 unseen split leakage을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 원문 대조

여러 과제의 시연으로 초기화한 VLA에 온라인 잔차 정책을 학습하고 과제별 기울기 간섭을 조정한다. 실물 네 과제는 시뮬레이션에서 학습한 정책의 전이 평가다. [방법과 평가](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/lin26af/lin26af.pdf#page=6)
