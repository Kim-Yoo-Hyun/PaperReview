# Cal-QL: Calibrated Offline RL Pre-Training for Efficient Online Fine-Tuning

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2023 / NeurIPS
- Authors: Mitsuhiko Nakamoto, Yuexiang Zhai, Anikait Singh, Max Sobol Mark, Yi Ma, Chelsea Finn, Aviral Kumar, Sergey Levine
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: offline-to-online, value-calibration, conservative-learning, fine-tuning
- Aliases: Cal-QL
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2023/hash/c44a04289beaf0a7d968a94066a1d696-Abstract-Conference.html
- Venue verification: https://proceedings.neurips.cc/paper_files/paper/2023/hash/c44a04289beaf0a7d968a94066a1d696-Abstract-Conference.html
- Code/Project: https://nakamotoo.github.io/Cal-QL/
- Code: https://github.com/nakamotoo/Cal-QL
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

Cal-QL은 오프라인에서 학습한 보수적 가치 추정치가 지나치게 낮아져 온라인 미세조정이 지연되는 문제를 다룬다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2023/file/c44a04289beaf0a7d968a94066a1d696-Paper-Conference.pdf#page=1)

## Core Idea and Contribution

- 학습 중인 정책의 가치를 보수적으로 추정하면서도 기준 정책의 가치보다는 작아지지 않도록 CQL의 벌점을 보정한다. [PDF 4쪽](https://proceedings.neurips.cc/paper_files/paper/2023/file/c44a04289beaf0a7d968a94066a1d696-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.neurips.cc/paper_files/paper/2023/file/c44a04289beaf0a7d968a94066a1d696-Paper-Conference.pdf#page=5)
- 조작과 내비게이션 등 미세조정 과제에서 오프라인 초기 성능, 온라인 학습 후 점수, 상호작용 중 누적 손실을 기준선과 비교했다. [PDF 8쪽](https://proceedings.neurips.cc/paper_files/paper/2023/file/c44a04289beaf0a7d968a94066a1d696-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.neurips.cc/paper_files/paper/2023/file/c44a04289beaf0a7d968a94066a1d696-Paper-Conference.pdf#page=9)

## Observation–State–Action Interface

Offline data → calibrated conservative critic·정책 → online fine-tuning.

## Evaluation Scope and Claim Boundary

Offline-to-online fine-tuning benchmark를 비교한다. 모든 VLA 보존 문제를 해결했다고 해석하지 않는다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2023/hash/c44a04289beaf0a7d968a94066a1d696-Abstract-Conference.html) · [저자 project/code](https://nakamotoo.github.io/Cal-QL/) · [공식 code](https://github.com/nakamotoo/Cal-QL). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

초기 성능 손실을 semantic forgetting으로만 설명하지 않게 하는 critic calibration baseline이다.

## Verification Boundary

본문에서 확인할 항목: reference return·보수성·초기 탐색·데이터 혼합·성능 회복 비용. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 · 가치 보정을 포함한 오프라인–온라인 학습 · JaxCQL/conservative_sac.py [배포 파일](https://raw.githubusercontent.com/nakamotoo/Cal-QL/ac6eafec22e8d60836573e1f488c7f626ce8a77e/JaxCQL/conservative_sac.py)
- 데이터 · Cal-QL 저자가 실험용으로 연결한 Adroit 오프라인 자료 · offpolicy_hand_data.zip [배포 파일](https://drive.google.com/file/d/1yUdJnGgYit94X_AvV6JJP5Y3Lx2JF30Y/view)
