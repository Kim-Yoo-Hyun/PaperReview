# MM-ACT: Learn from Multimodal Parallel Generation to Act

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CVPR
- Authors: Haotian Liang, Xinyi Chen, Bin Wang, Mingkang Chen, Yitian Liu, Yuhao Zhang, Zanxin Chen, Tianshuo Yang, Yilun Chen, Jiangmiao Pang, Dong Liu, Xiaokang Yang, Yao Mu, Wenqi Shao, Ping Luo
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: unified-generation, VLA, multimodal-learning
- Aliases: MM-ACT
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Liang_MM-ACT_Learn_from_Multimodal_Parallel_Generation_to_Act_CVPR_2026_paper.html
- Venue verification: https://openaccess.thecvf.com/content/CVPR2026/html/Liang_MM-ACT_Learn_from_Multimodal_Parallel_Generation_to_Act_CVPR_2026_paper.html
- Code/Project: https://github.com/HHYHRHY/MM-ACT
- Code: https://github.com/HHYHRHY/MM-ACT
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

MM-ACT는 텍스트·영상·행동을 공통 토큰 공간에서 생성하며, 같은 관측으로 받는 여러 감독 신호가 조작 정책에 미치는 영향을 평가한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Liang_MM-ACT_Learn_from_Multimodal_Parallel_Generation_to_Act_CVPR_2026_paper.pdf#page=1)

## Core Idea and Contribution

- 텍스트와 영상에는 일부 토큰을 다시 가려 생성하는 병렬 복호화를, 행동에는 한 번의 병렬 복호화를 사용한다. [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Liang_MM-ACT_Learn_from_Multimodal_Parallel_Generation_to_Act_CVPR_2026_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Liang_MM-ACT_Learn_from_Multimodal_Parallel_Generation_to_Act_CVPR_2026_paper.pdf#page=5)
- LIBERO, RoboTwin 2.0, 실제 Franka 조작에서 정책을 평가하고 영상·언어 생성과 행동 생성을 함께 학습할 때의 변화를 비교했다. [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Liang_MM-ACT_Learn_from_Multimodal_Parallel_Generation_to_Act_CVPR_2026_paper.pdf#page=6) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Liang_MM-ACT_Learn_from_Multimodal_Parallel_Generation_to_Act_CVPR_2026_paper.pdf#page=8)

## Observation–State–Action Interface

공유 multimodal context → text/image/action generation; action은 one-step parallel decoding.

## Evaluation Scope and Claim Boundary

LIBERO, 실제 Franka, RoboTwin2.0의 in-domain·out-of-domain 조작을 평가한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Liang_MM-ACT_Learn_from_Multimodal_Parallel_Generation_to_Act_CVPR_2026_paper.html) · [저자 project/code](https://github.com/HHYHRHY/MM-ACT). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

하나의 VLA 내부 통합을 설계할 architecture 선행이며 RL objective 통합 효과로 해석하지 않는다.

## Verification Boundary

modality별 loss·compute 균형, 생성 token이 action에 주는 영향, RL 미검증 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 · MM-ACT 공통 토큰 모델 · models/modeling_mmact.py [배포 파일](https://raw.githubusercontent.com/HHYHRHY/MM-ACT/ee3745212d905edefb381a8f658e7140e4b3d585/models/modeling_mmact.py)
- 가중치 · LIBERO-10용 MM-ACT 정책 · LIBERO/MM-ACT-10/model-00001-of-00004.safetensors [배포 파일](https://huggingface.co/hhyhrhy/MM-ACT-Model/resolve/51c22aaca9a54746977952eb034231a28729f541/LIBERO/MM-ACT-10/model-00001-of-00004.safetensors)
- 데이터 · MM-ACT LIBERO-10 계획 주석 · LIBERO/libero10_planning.jsonl [배포 파일](https://huggingface.co/datasets/hhyhrhy/MM-ACT-data/resolve/0d903db375b6bfb3603c6ce95bbf4d182411e864/LIBERO/libero10_planning.jsonl)
