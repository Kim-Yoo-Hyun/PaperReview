# PoseIt: A Visual-Tactile Dataset of Holding Poses for Grasp Stability Analysis

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2022 / IROS
- Category: Benchmarks and Datasets
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: robot-data, tactile, grasp-stability, holding-pose
- Aliases: PoseIt
- Official paper: https://ieeexplore.ieee.org/document/9981562/
- Venue verification: https://ieeexplore.ieee.org/document/9981562/
- Code/Project: https://publish.illinois.edu/robotouch/poseit-a-visual-tactile-dataset-of-holding-poses-for-grasp-stability-analysis/
- Code: https://github.com/Robo-Touch/PoseIt
- Source audit: IROS 논문의 IEEE 기탁 DOI, 저자 소속 대학의 서지, arXiv 초록과 데이터 README를 확인했다.

## Problem and Importance

처음 들어 올렸을 때의 안정성이 팔을 다른 자세로 옮긴 뒤에도 유지되는지 알아야 한다.

## Core Idea and Contribution

집기·자세 이동·흔들기 전 과정의 시각과 촉각 관측을 수집하고 다중 모달 시계열 분류기를 비교한다.

## Observation–State–Action Interface

RGB-D, 손가락 촉각, 힘·토크와 로봇 상태가 자세별 안정성 예측의 입력이다.

## Evaluation Scope and Claim Boundary

저자 자료는 26개 물체의 실물 기록을 제공하며 초록은 미관측 물체와 자세에 대한 예측을 평가한다. 자세 이동 중 실패와 마지막 흔들기 결과는 별개다.

근거: [공식 paper/abstract](https://ieeexplore.ieee.org/document/9981562/) · [저자 project/code](https://publish.illinois.edu/robotouch/poseit-a-visual-tactile-dataset-of-holding-poses-for-grasp-stability-analysis/) · [공식 code](https://github.com/Robo-Touch/PoseIt). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

들기 이후 실패가 발생한 단계를 공개 기록으로 재확인할 때 쓰는 데이터 기준이다.

## Verification Boundary

물체 분할, 파지 명령이 변경된 시점과 단계별 실패 라벨의 의미을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
