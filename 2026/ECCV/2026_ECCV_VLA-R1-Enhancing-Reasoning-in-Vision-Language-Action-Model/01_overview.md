# VLA-R1: Enhancing Reasoning in Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ECCV
- Authors: Angen Ye, Zeyu Zhang, Boyuan Wang, Xiaofeng Wang, Dapeng Zhang, Zheng Zhu
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: RLVR, GRPO, affordance, trajectory-reasoning
- Aliases: VLA-R1, VLA-CoT-13K
- Official paper: https://arxiv.org/abs/2510.01623
- Venue verification: https://api.crossref.org/works/10.1007/978-3-032-37383-0_20
- Code/Project: https://gigaai-research.github.io/VLA-R1/
- Code: https://github.com/GigaAI-research/VLA-R1
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인. Region/trajectory 출력 뒤 downstream control을 쓰므로 직접 motor-action RL과 동일시하지 않는다. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

VLA-R1은 조작 대상 영역과 이동 궤적에 연결된 추론 예시로 VLA를 학습하고 검증 가능한 보상으로 출력을 개선한다. [PDF 1쪽](https://arxiv.org/pdf/2510.01623v1#page=1)

## Core Idea and Contribution

- VLA-CoT-13K의 어포던스·궤적 주석을 활용하고 영역 정렬, 경로 일관성, 응답 형식을 점수화해 GRPO 후학습에 사용한다. [PDF 3쪽](https://arxiv.org/pdf/2510.01623v1#page=3) · [PDF 5쪽](https://arxiv.org/pdf/2510.01623v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2510.01623v1#page=6)
- 시뮬레이션과 실물 장면에서 대상 영역과 경로 예측을 평가하고 지시·장면의 분포가 달라졌을 때의 일반화를 조사했다. [PDF 7쪽](https://arxiv.org/pdf/2510.01623v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2510.01623v1#page=8) · [PDF 9쪽](https://arxiv.org/pdf/2510.01623v1#page=9)

## Observation–State–Action Interface

시각·지시 → affordance region·trajectory와 reasoning → downstream robot control. 직접 joint action 최적화와 구분한다.

## Evaluation Scope and Claim Boundary

In/out-of-domain, simulation과 실로봇 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2510.01623) · [저자 project/code](https://gigaai-research.github.io/VLA-R1/) · [공식 code](https://github.com/GigaAI-research/VLA-R1). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

VLA의 RL이 환경 return이 아닌 검증 가능한 중간 출력 보상일 때의 직접 비교 기준이다.

## Verification Boundary

annotation 접근, downstream controller의 역할, execution feedback 사용 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
