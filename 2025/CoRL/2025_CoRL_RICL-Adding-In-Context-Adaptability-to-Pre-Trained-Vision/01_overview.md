# RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. 요약·기여와 아래에 인용한 방법·평가를 원문에서 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / CoRL
- Authors: Kaustubh Sridhar, Souradeep Dutta, Dinesh Jayaraman, Insup Lee
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, in-context-learning, retrieval, manipulation
- Aliases: RICL
- Official paper: https://proceedings.mlr.press/v305/sridhar25a.html
- Venue verification: https://proceedings.mlr.press/v305/sridhar25a.html
- Code/Project: https://ricl-vla.github.io/
- Code: https://github.com/ricl-vla/ricl_openpi
- Source audit: 2026-11-25 게재본에서 아래에 인용한 요약·기여와 평가 조건을 대조했다. [평가 노트](./04_evaluation.md)

## Problem and Importance

사전학습 VLA가 새 시연을 문맥으로 읽는 능력을 자동으로 갖추지 못하는 문제를 다룬다.

## Core Idea and Contribution

소규모 robot 시연으로 in-context 적응 능력을 후학습하고, 배포 시 관련 시연 구간을 검색해 정책 문맥에 제공한다.

## Observation–State–Action Interface

현재 관측·지시와 검색된 시연 → π0-FAST 기반 정책 → 로봇 행동. ICL 능력을 만드는 후학습과 새 task에서의 무갱신 적응을 구분한다.

## Evaluation Scope

새 조작 과제의 소수 시연을 이용한 적응과 추가 fine-tuning을 비교한다. 대조 조건과 확인한 원문 위치는 평가 노트에 적었다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/sridhar25a.html) · [저자 project](https://ricl-vla.github.io/).

## Why This Paper Is Here — Researcher Interpretation

OpenVLA·π0 계열의 후학습과 시연 검색을 잇는 직접 선행이다. 현재 bank 확장 질문에서 이미 알려진 ICL 능력·검색 이득을 신규성으로 재주장하지 않도록 NEXT로 등록한다.

범위와 수치의 미확인 항목은 [평가 노트](./04_evaluation.md)에, 제안하는 반증 질문은 [insights](./05_insights.md)에 둔다.

## 공개 자료

- 코드 — π0-FAST 검색 문맥 학습 · scripts/train_pi0_fast_ricl.py [배포 파일](https://raw.githubusercontent.com/ricl-vla/ricl_openpi/a2d35f99d4180fb84344122f804fa8dfe3d8ab6f/scripts/train_pi0_fast_ricl.py)
- 가중치·학습 파라미터 — RICL-π0-FAST-DROID의 파라미터 조각 · params/ocdbt.process_0/d/031e06384a4655f2a5a6ab91f308b6e1 [배포 파일](https://huggingface.co/ricl-vla/pi0_fast_droid_ricl_checkpoint/resolve/ba89f78f16da2a7bd35c5a45fd5922aa0d0081cd/params/ocdbt.process_0/d/031e06384a4655f2a5a6ab91f308b6e1)
- 데이터 — 검색 문맥 학습용 실제 로봇 시연 · 2025-03-14_move_apple_to_the_right/2025-03-14_20-04-47/processed_demo.npz [배포 파일](https://huggingface.co/datasets/ricl-vla/collected_demos_training/resolve/941a0c7092ac04c5dd0948b7e1647df628d1688a/2025-03-14_move_apple_to_the_right/2025-03-14_20-04-47/processed_demo.npz)

## 원문 대조

RICL은 기존 VLA를 검색한 시연을 활용하도록 후학습해, 새 조작 과제에서 파라미터 갱신 없이 시연을 이용하게 한다. [게재본](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/sridhar25a/sridhar25a.pdf#page=4)

- 현재 관측과 유사한 시연의 영상·상태·행동 묶음을 π0-FAST의 문맥에 넣는 지도학습을 설계했다. [원문](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/sridhar25a/sridhar25a.pdf#page=4)
- 실제 Franka에서 검색 문맥만 바꾸는 설정과 새 과제 시연으로 파라미터까지 조정하는 설정을 비교했다. [원문](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/sridhar25a/sridhar25a.pdf#page=7)
