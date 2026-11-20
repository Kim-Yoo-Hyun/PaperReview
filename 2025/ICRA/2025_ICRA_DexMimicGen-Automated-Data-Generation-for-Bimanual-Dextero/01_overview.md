# DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Zhenyu Jiang, Yuqi Xie, Kevin Lin, Zhenjia Xu, Weikang Wan, Ajay Mandlekar, Linxi Jim Fan, Yuke Zhu
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, robot data, bimanual, dexterous manipulation, simulation
- Aliases: DexMimicGen
- Official paper: https://arxiv.org/abs/2410.24185
- Venue verification: https://api.crossref.org/works/10.1109/ICRA55743.2025.11127809
- Code/Project: https://dexmimicgen.github.io/
- Code: https://github.com/NVlabs/dexmimicgen
- Source audit: 2026-10-25 공식 abstract/서지정보 및 명시된 저자 링크 확인. 이번 노트는 abstract 기반이며 본문 전체·코드 실행·payload는 미검증이다. ICRA 2025 저자 project 표기와 IEEE-deposited Crossref metadata 대조. IEEE 직접 페이지는 browser challenge; abstract/project 범위만 확인.

## Problem and Importance

양팔·다지 손의 동시 조작 시연 수집 비용이 크다.

## Core Idea and Contribution

소수 인간 시연을 재사용해 시뮬레이션의 양팔 dexterous trajectory를 생성한다.

## Observation–State–Action Interface

source demonstration·새 초기 상태 → 합성 trajectory → imitation policy.

## Evaluation Scope and Claim Boundary

양팔 조작 simulation과 real2sim2real 사례를 제시한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2410.24185) · [저자 project/code](https://dexmimicgen.github.io/) · [공식 code](https://github.com/NVlabs/dexmimicgen). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

여러 embodiment의 데이터를 늘릴 때 실제 시연과 합성 trajectory의 역할을 비교할 자산이다.

## Verification Boundary

object-state/segmentation 접근, source-target task 대응, 생성 실패 및 sim-to-real 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
