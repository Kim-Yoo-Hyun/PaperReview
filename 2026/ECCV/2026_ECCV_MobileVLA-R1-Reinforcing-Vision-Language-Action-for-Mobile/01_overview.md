# MobileVLA-R1: Reinforcing Vision-Language-Action for Mobile Robots

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ECCV
- Authors: Ting Huang, Dongjian Li, Rui Yang, Zeyu Zhang, Zida Yang, Hao Tang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, GRPO, quadruped, Navigation
- Aliases: MobileVLA-R1, MobileVLA-CoT
- Official paper: https://arxiv.org/abs/2511.17889
- Venue verification: https://eccv.ecva.net/Conferences/2026/AcceptedPapers
- Code/Project: https://aigeeksgroup.github.io/MobileVLA-R1/
- Code: https://github.com/AIGeeksGroup/MobileVLA-R1
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인. ECCV 원 논문과 MobileVLA-R1 2.0(preprint)의 주장·코드를 구분한다. 현 repository 실행 및 원 버전 일치는 미검증. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

MobileVLA-R1은 자연어 지시와 시각 관측에서 추론 과정을 생성하고 사족 로봇이 실행할 연속 이동 명령을 예측한다. [PDF 1쪽](https://arxiv.org/pdf/2511.17889v1#page=1)

## Core Idea and Contribution

- MobileVLA-CoT로 지시와 이동 궤적의 대응을 지도학습한 뒤 GRPO로 추론과 연속 속도 출력에 관한 보상을 최적화한다. [PDF 3쪽](https://arxiv.org/pdf/2511.17889v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2511.17889v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2511.17889v1#page=5)
- 언어 지시 내비게이션과 사족 제어 과제에서 평가하고 실제 Unitree Go2에서 관측을 되먹임하며 명령을 수행하는 과정을 검증했다. [PDF 6쪽](https://arxiv.org/pdf/2511.17889v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2511.17889v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2511.17889v1#page=8)

## Observation–State–Action Interface

영상·지시 → reasoning과 navigation command/control output → quadruped execution. 출력 형식을 low-level motor torque와 혼동하지 않는다.

## Evaluation Scope and Claim Boundary

VLN·VLA benchmark와 실제 사족 로봇 배포를 보고한다. MobileVLA-R1 2.0의 추가 주장은 포함하지 않는다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2511.17889) · [저자 project/code](https://aigeeksgroup.github.io/MobileVLA-R1/) · [공식 code](https://github.com/AIGeeksGroup/MobileVLA-R1). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Manipulation 외에 단일 VLA 후학습을 검토할 모바일 로봇 선행이다.

## Verification Boundary

속도·이산 행동 output 형식, low-level controller 고정 여부, 2.0 코드와 원 논문 차이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 · MobileVLA-R1 이동 명령 추론 · inference.py [배포 파일](https://raw.githubusercontent.com/AIGeeksGroup/MobileVLA-R1/9d98cce3b623dfddf479740d78869ec30364b75a/inference.py)
- 가중치 · MobileVLA-R1 가중치 압축본 조각 · weight.zip.part-aa [배포 파일](https://huggingface.co/AIGeeksGroup/MobileVLA-R1/resolve/0c757f3e9d1b95d8416b42e7089e1c04f3e6118a/weight.zip.part-aa)
- 데이터 · 이동 경로 추론 감독 자료 · MobileVLA-CoT-Nav-38K/Nav_CoT_FINAL_38K.jsonl [배포 파일](https://huggingface.co/datasets/AIGeeksGroup/MobileVLA-CoT/resolve/1f80df559fa088010fd6654ceceda000084f644f/MobileVLA-CoT-Nav-38K/Nav_CoT_FINAL_38K.jsonl)
