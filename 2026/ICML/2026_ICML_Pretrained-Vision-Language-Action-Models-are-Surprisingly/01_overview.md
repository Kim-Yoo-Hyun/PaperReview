# Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Huihan Liu, Changyeon Kim, Bo Liu, Minghuan Liu, Yuke Zhu
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: continual-learning, replay, robot-learning
- Aliases: Forget-Me-Not
- Official paper: https://proceedings.mlr.press/v306/liu26bu.html
- Venue verification: https://proceedings.mlr.press/v306/liu26bu.html
- Code/Project: https://continual-vlas.github.io/forget-me-not/
- Code: project_only
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

VLA 순차 학습에서 기존 능력이 얼마나 보존되는가.

## Core Idea and Contribution

사전학습과 소량 experience replay의 망각 억제 효과를 분석한다.

## Observation–State–Action Interface

사전학습 VLA → 새 task fine-tuning/replay → robot action.

## Evaluation Scope and Claim Boundary

순차 robot task의 학습·망각 비교를 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v306/liu26bu.html) · [저자 project/code](https://continual-vlas.github.io/forget-me-not/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

E1에서 복잡한 replay selector 전에 확인할 강한 단순 기준이다.

## Verification Boundary

pretraining 중복, replay 비율, old-task 평가와 모듈별 동결을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
