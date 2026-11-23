# DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / ICRA
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
- Source audit: 2026-10-25 공식 abstract/서지정보 및 명시된 저자 링크 확인. 이번 노트는 abstract 기반이며 본문 전체·코드 실행·payload는 미검증이다. ICRA 2025 저자 project 표기와 IEEE-deposited Crossref metadata 대조. IEEE 직접 페이지는 browser challenge; abstract/project 범위만 확인. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

DexMimicGen은 소수의 양손 시연에서 두 손의 협응을 유지하는 새로운 조작 궤적을 만들어 모방학습 자료를 확장한다. [PDF 1쪽](https://arxiv.org/pdf/2410.24185v2#page=1)

## Core Idea and Contribution

- 각 손의 하위 동작을 물체에 맞게 변환하고 동시 실행이나 순서가 필요한 두 손의 구간을 조율해 시연을 재생성한다. [PDF 3쪽](https://arxiv.org/pdf/2410.24185v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2410.24185v2#page=4)
- 60개 시연에서 2만 1천 개의 시뮬레이션 시연을 생성했으며 휴머노이드의 캔 분류로 실물 시연에서 합성 자료를 거쳐 실물 정책으로 이어지는 절차를 시험했다. [PDF 1쪽](https://arxiv.org/pdf/2410.24185v2#page=1) · [PDF 6쪽](https://arxiv.org/pdf/2410.24185v2#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2410.24185v2#page=7)

## Observation–State–Action Interface

source demonstration·새 초기 상태 → 합성 trajectory → imitation policy.

## Evaluation Scope and Claim Boundary

양팔 조작 simulation과 real2sim2real 사례를 제시한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2410.24185) · [저자 project/code](https://dexmimicgen.github.io/) · [공식 code](https://github.com/NVlabs/dexmimicgen). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

여러 embodiment의 데이터를 늘릴 때 실제 시연과 합성 trajectory의 역할을 비교할 자산이다.

## Verification Boundary

object-state/segmentation 접근, source-target task 대응, 생성 실패 및 sim-to-real 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
