# Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Ye Wang, Sipeng Zheng, Hao Luo, Wanpeng Zhang, Haoqi Yuan, Chaoyi Xu, Haiweng Xu, Yicheng Feng, Mingyang Yu, Zhiyu Kang, Zongqing Lu, Qin Jin
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, pretraining, action representation, cross-embodiment
- Aliases: Rethinking VLA Scaling
- Official paper: https://arxiv.org/abs/2602.09722
- Venue verification: https://arxiv.org/abs/2602.09722
- Code/Project: https://research.beingbeyond.com/rethink_vla
- Code: https://github.com/BeingBeyond/Rethink_VLA
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 서로 다른 로봇의 시연을 늘릴 때 행동 좌표계·로봇별 데이터 혼합·정규화가 VLA의 전이에 주는 영향을 비교했다. [PDF 1쪽](https://arxiv.org/pdf/2602.09722v1#page=1)

## Core Idea and Contribution

- 실물 평가에서 정책의 정체를 가리고 실행자와 결과 판정자를 분리하는 절차를 도입했다. [PDF 2쪽](https://arxiv.org/pdf/2602.09722v1#page=2) · [PDF 4쪽](https://arxiv.org/pdf/2602.09722v1#page=4)
- 말단 기준 상대 행동 표현의 전이 이득을 관찰했고, 이질적인 데이터를 단순히 합치거나 정규화를 추가해도 성능이 일관되게 오르지는 않았다. [PDF 5쪽](https://arxiv.org/pdf/2602.09722v1#page=5) · [PDF 7쪽](https://arxiv.org/pdf/2602.09722v1#page=7)

## Observation–State–Action Interface

이종 robot demonstration → 정렬된 action 표현 → VLA.

## Evaluation Scope and Claim Boundary

Simulation과 real-robot 평가에서 데이터 혼합과 negative transfer를 분석한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2602.09722). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

E1에서 정상 action 정렬·mixture 자체의 설명력을 먼저 제거할 기준이다.

## Verification Boundary

EEF frame, normalization, split, grouped blind protocol을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 — VLA 사전학습의 2단계 실행 설정 · shell/pretrain-M1-240k-stage2.sh [배포 파일](https://raw.githubusercontent.com/BeingBeyond/Rethink_VLA/d3739abda923ffddaf01d6d8d74bf3d439068106/shell/pretrain-M1-240k-stage2.sh)
- 가중치 — 저자 공개 OXE 사전학습 정책 · model.safetensors [배포 파일](https://huggingface.co/wwwyyy/pretrain-oxe-eef-relative/blob/ee852ea26ed70b71eb04a62af03532094a5fe991/model.safetensors)
- 데이터 — 저자 변환 RoboCasa 인간 시연 · CloseDoubleDoor/data/chunk-000/episode_000000.parquet [배포 파일](https://huggingface.co/datasets/BeingBeyond/robocasa_human_single_lerobot/blob/2f97c13621549144a702ccd2b61f15b4c32e82ef/CloseDoubleDoor/data/chunk-000/episode_000000.parquet)
