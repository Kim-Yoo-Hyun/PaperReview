# Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICML
- Authors: Huihan Liu, Changyeon Kim, Bo Liu, Minghuan Liu, Yuke Zhu
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: continual-learning, replay, robot-learning
- Aliases: Forget-Me-Not
- Official paper: https://proceedings.mlr.press/v306/liu26bu.html
- Venue verification: https://proceedings.mlr.press/v306/liu26bu.html
- Code/Project: https://continual-vlas.github.io/forget-me-not/
- Code: https://github.com/Continual-VLAs/continual-openpi
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 기존 과제의 소량 경험을 재생할 때 사전학습된 VLA가 순차적으로 새 조작을 배우면서 얼마나 덜 망각하는지 측정했다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/liu26bu/liu26bu.pdf#page=1)

## Core Idea and Contribution

- 사전학습 모델과 처음부터 학습한 정책을 비교하고, 과거 경험을 재생했을 때 시뮬레이션과 실제 로봇에서 나타나는 차이를 평가했다. [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/liu26bu/liu26bu.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/liu26bu/liu26bu.pdf#page=5)
- 기존 과제의 성공률이 낮아진 뒤 그 기술을 다시 미세조정해 회복에 필요한 학습량을 측정했다. [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/liu26bu/liu26bu.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/liu26bu/liu26bu.pdf#page=8)

## Observation–State–Action Interface

사전학습 VLA → 새 task fine-tuning/replay → robot action.

## Evaluation Scope and Claim Boundary

순차 robot task의 학습·망각 비교를 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v306/liu26bu.html) · [저자 project/code](https://continual-vlas.github.io/forget-me-not/). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

E1에서 복잡한 replay selector 전에 확인할 강한 단순 기준이다.

## Verification Boundary

pretraining 중복, replay 비율, old-task 평가와 모듈별 동결을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 — 연속 VLA 학습 정규화 구현 · src/openpi/continual/ewc.py [배포 파일](https://raw.githubusercontent.com/Continual-VLAs/continual-openpi/a3f8ca4c5abbf84248ce2046e248054fdaab5186/src/openpi/continual/ewc.py)
