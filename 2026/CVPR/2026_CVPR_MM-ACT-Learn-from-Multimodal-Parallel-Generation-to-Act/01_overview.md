# MM-ACT: Learn from Multimodal Parallel Generation to Act

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
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
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

의미 이해와 예측을 행동 생성에 함께 활용하는 generalist policy 학습이 필요하다.

## Core Idea and Contribution

텍스트·영상·행동을 공유 token 공간과 context로 학습하고 modality별 병렬 decoding을 사용한다.

## Observation–State–Action Interface

공유 multimodal context → text/image/action generation; action은 one-step parallel decoding.

## Evaluation Scope and Claim Boundary

LIBERO, 실제 Franka, RoboTwin2.0의 in-domain·out-of-domain 조작을 평가한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Liang_MM-ACT_Learn_from_Multimodal_Parallel_Generation_to_Act_CVPR_2026_paper.html) · [저자 project/code](https://github.com/HHYHRHY/MM-ACT). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

하나의 VLA 내부 통합을 설계할 architecture 선행이며 RL objective 통합 효과로 해석하지 않는다.

## Verification Boundary

modality별 loss·compute 균형, 생성 token이 action에 주는 영향, RL 미검증 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
