# Tactile-Guided In-Contact Robotic Insertion via Physically Consistent Force-Array Representation Learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RA-L
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: tactile, force-distribution, insertion, diffusion-policy
- Aliases:
- Official paper: https://ieeexplore.ieee.org/document/11692602/
- Venue verification: https://ieeexplore.ieee.org/document/11692602/
- Code/Project: not identified
- Code: not_identified
- Source audit: IEEE 공식 초록 색인과 Crossref의 IEEE 기탁 DOI·2026년 11월 저널 서지를 확인했다. 공개 코드의 정확한 저장소는 확인되지 않았다.

## Problem and Importance

접촉 뒤 시야가 가려지면 커넥터의 작은 정렬 오차를 영상에서 판독하기 어렵다.

## Core Idea and Contribution

접촉 후 시연에서 힘 분포 표현을 관측하는 diffusion policy를 학습하고 합력·모멘트만 쓰는 경우와 대조한다.

## Observation–State–Action Interface

접촉 중의 촉각 입력을 삽입 동작으로 바꾼다. 센서 배열은 국소 하중의 분포를 보존한다.

## Evaluation Scope and Claim Boundary

IEEE 초록은 학습 분포 안에서 합력·모멘트만 쓴 변형이 약간 우세했고, 새 2·3핀과 USB·HDMI 커넥터 전이에서는 분포 표현이 유리했다고 보고한다.

근거: [공식 paper/abstract](https://ieeexplore.ieee.org/document/11692602/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

순합력과 국소 접촉 정보가 다른 판단을 주는 현재 삽입 연구의 실물 비교 논문이다.

## Verification Boundary

센서 교정, 커넥터별 시행 수, 실물 분포 신호를 재현할 수 있는 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
