# Equivariant diffusion policy for sample-efficient robotic manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 요약·기여와 아래에 인용한 방법·평가를 원문에서 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / IJRR
- Authors: Dian Wang, Stephen Hart, David Surovik, Tarik Kelestemur, Haojie Huang, Haibo Zhao, Mark Yeatman, Xupeng Zhu, Boce Hu, Mingxi Jia, Jiuguang Wang, Robin Walters, Robert Platt
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Imitation Learning, Diffusion, equivariance, sample-efficiency
- Aliases: Equivariant Diffusion Policy, EquiDiff
- Official paper: https://api.crossref.org/works/10.1177/02783649261424445
- Venue verification: https://journals.sagepub.com/doi/full/10.1177/02783649261424445
- Code/Project: https://equidiff.github.io/
- Code: https://github.com/pointW/equidiff
- Source audit: 2026-11-25 출판사 저널 본문과 선행 학회판을 대조했다. [평가 노트](./04_evaluation.md)

## Problem and Importance

Diffusion policy의 복잡한 denoising 학습에는 많은 시연이 필요하다.

## Core Idea and Contribution

시연으로 학습하는 확산 정책에 장면과 행동의 대칭성을 반영해 새로운 배치에서 조작을 학습하는 데 필요한 표본을 줄인다.

- 저널 확장판은 점군 입력과 등변 점 트랜스포머로 회전과 3차원 평행이동을 함께 다룬다.
- 시뮬레이션 비교와 실물 로봇 조작 실험에서 대칭성의 효과를 검증한다.

[저널판 서론·실험과 학회판 차이](https://journals.sagepub.com/doi/full/10.1177/02783649261424445)

## Observation–State–Action Interface

관측·noisy action trajectory → equivariant denoiser → action trajectory.

## Evaluation Scope and Claim Boundary

MimicGen simulation과 실로봇 manipulation에서 소량 시연 학습을 비교한다.

근거: [공식 paper/abstract](https://journals.sagepub.com/doi/10.1177/02783649261424445) · [저자 project/code](https://equidiff.github.io/) · [공식 code](https://github.com/pointW/equidiff). 확인한 조건은 [평가 노트](./04_evaluation.md)에 기록했다.

## Why This Paper Is Here — Researcher Interpretation

일반화 이득이 더 큰 VLA보다 대칭성 같은 inductive bias로 설명되는지 대조할 기준이다.

## Verification Boundary

적용 가능한 symmetry, 절대/상대 action, RGB/point-cloud 정보량, checkpoint 선택을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 — 저자가 두 판본에서 공통으로 연결한 등변 정책 학습기 · equi_diffpo/workspace/train_equi_workspace.py [배포 파일](https://raw.githubusercontent.com/pointW/equidiff/e40abb003b25071d4e5b01bfa9933dc16cd32c67/equi_diffpo/workspace/train_equi_workspace.py)

## 원문 대조

회전과 병진에 대한 등변성을 확산 조작 정책에 반영해 시연 수에 따른 성능과 새로운 물체 배치에 대한 일반화를 비교한다. [출판사 저널 본문](https://sage.cnpereading.com/doi/10.1177/02783649261424445#:~:text=Real-robot%20experiment)

- 등변 점 트랜스포머와 행동 잡음 예측을 결합해 점군에서 회전·평행이동의 변환 규칙을 반영한다. [원문](https://sage.cnpereading.com/doi/10.1177/02783649261424445#:~:text=Equivariant%20point%20transformer%20and%20translation%20symmetry)
- 시뮬레이션과 여섯 실제 Franka 과제에서 입력 표현과 대칭 구성에 따른 일반화를 비교한다. [원문](https://sage.cnpereading.com/doi/10.1177/02783649261424445#:~:text=Real-robot%20experiment)

## 판본과 출처

저널 실험은 출판사 본문에서 확인했다. CoRL 선행판은 SO(2) 회전을 중심으로 다루며, 저자는 두 판본에서 동일한 코드 저장소를 연결한다. [원문](https://sage.cnpereading.com/doi/10.1177/02783649261424445)
