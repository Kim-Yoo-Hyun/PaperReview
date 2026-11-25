# TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction

> Evidence maturity: `ABSTRACT_CHECKED`. 아래의 요약·기여는 인용한 원문 쪽에서 추가 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2024 / CoRL
- Authors: Yunfan Jiang, Chen Wang, Ruohan Zhang, Jiajun Wu, Li Fei-Fei
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, sim-to-real, human-in-the-loop, residual-policy
- Aliases: TRANSIC
- Official paper: https://proceedings.mlr.press/v270/jiang25a.html
- Venue verification: https://proceedings.mlr.press/v270/jiang25a.html
- Conference edition: 2024 · https://proceedings.mlr.press/v270/
- Code/Project: https://transic-robot.github.io/
- Code: https://github.com/transic-robot/transic
- Source audit: 2026-10-25 공식 abstract/서지정보 및 명시된 저자 링크 확인. 이번 노트는 abstract 기반이며 본문 전체·코드 실행·payload는 미검증이다. CoRL 개최 2024, PMLR 출판 2025.

## Problem and Importance

TRANSIC은 시뮬레이션 조작 정책을 실물에 옮긴 뒤 사람이 제공한 국소 교정으로 잔차 정책을 학습한다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/jiang25a/jiang25a.pdf#page=3)

## Core Idea and Contribution

- 시뮬레이션 RL 전문가를 관측 기반 정책으로 증류하고 실물 교정이 필요한 지점에서 보정하도록 학습한다. [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/jiang25a/jiang25a.pdf#page=4)
- 가구 조립의 세부 기술에서 증류 정책과 교정을 결합한 결과를 비교했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/jiang25a/jiang25a.pdf#page=6)

## Observation–State–Action Interface

point-cloud 기반 base policy + 인간 correction으로 학습한 residual → 실행 action.

## Evaluation Scope and Claim Boundary

가구 조립 등 실로봇 접촉 조작의 sim-to-real 전이를 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/jiang25a.html) · [저자 project/code](https://transic-robot.github.io/) · [공식 code](https://github.com/transic-robot/transic). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

새 RL/VLA 적응 기여를 주장하기 전에 인간 개입·residual 학습으로 설명되는 이득을 대조한다.

## Verification Boundary

개입 시점/시간 비용, residual 제어 권한, correction과 평가 분할을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 — 실물 교정에서 잔차 정책 학습 · main/residual/train.py [배포 파일](https://raw.githubusercontent.com/transic-robot/transic/9af4ff7a392d9b033bb3a05d16f1aaa1aa2472d6/main/residual/train.py)
- 가중치 — 삽입 과제 잔차 정책 · residual/insert.pth [배포 파일](https://huggingface.co/transic-robot/models/blob/305ceba1ad1eda4536b0ce9311ce68fa3f46902a/residual/insert.pth)
- 데이터 — 실물 삽입 작업의 사람 교정 시연 · correction_data/insert/2024-01-04-15-25-37.hdf5 [배포 파일](https://huggingface.co/datasets/transic-robot/data/blob/9c2b5b0dc89f520f66f72ead3816292f54ea86cc/correction_data/insert/2024-01-04-15-25-37.hdf5)
