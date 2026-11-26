# RehearseVLA: Simulated Post-Training for VLAs with Physically-Consistent World Model

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CVPR
- Authors: Junjin Xiao, Yandan Yang, Xinyuan Chang, Ronghan Chen, Feng Xiong, Mu Xu, Wei-Shi Zheng, Qing Zhang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, world-model, model-based-RL, termination
- Aliases: RehearseVLA
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_RehearseVLA_Simulated_Post-Training_for_VLAs_with_Physically-Consistent_World_Model_CVPR_2026_paper.html
- Venue verification: https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_RehearseVLA_Simulated_Post-Training_for_VLAs_with_Physically-Consistent_World_Model_CVPR_2026_paper.html
- Code/Project: https://github.com/iSEE-Laboratory/RehearseVLA
- Code: https://github.com/iSEE-Laboratory/RehearseVLA
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

RehearseVLA는 로봇이 실제 장면을 매번 초기화하지 않고도 후학습할 수 있도록 세계 모델 안에서 VLA의 후보 행동을 실행하고 평가한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Xiao_RehearseVLA_Simulated_Post-Training_for_VLAs_with_Physically-Consistent_World_Model_CVPR_2026_paper.pdf#page=1)

## Core Idea and Contribution

- 행동에 따른 후속 관측을 생성하는 시뮬레이터와 시각언어 모델 기반 평가기를 결합해 단계별 보상과 동작 종료 신호를 산출한다. [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Xiao_RehearseVLA_Simulated_Post-Training_for_VLAs_with_Physically-Consistent_World_Model_CVPR_2026_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Xiao_RehearseVLA_Simulated_Post-Training_for_VLAs_with_Physically-Consistent_World_Model_CVPR_2026_paper.pdf#page=5)
- LIBERO와 실물 조작에서 소수 시연으로 시작한 정책의 후학습 효과를 측정하고 실물에서는 종료 판정 전략에 따른 과제 성공도 비교했다. [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Xiao_RehearseVLA_Simulated_Post-Training_for_VLAs_with_Physically-Consistent_World_Model_CVPR_2026_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Xiao_RehearseVLA_Simulated_Post-Training_for_VLAs_with_Physically-Consistent_World_Model_CVPR_2026_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Xiao_RehearseVLA_Simulated_Post-Training_for_VLAs_with_Physically-Consistent_World_Model_CVPR_2026_paper.pdf#page=8)

## Observation–State–Action Interface

행동 → 미래 영상 예측 → 보상·종료 판단 → VLA 후학습.

## Evaluation Scope and Claim Boundary

소수 시연 조건의 복잡한 로봇 조작 개선을 보고한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_RehearseVLA_Simulated_Post-Training_for_VLAs_with_Physically-Consistent_World_Model_CVPR_2026_paper.html) · [저자 project/code](https://github.com/iSEE-Laboratory/RehearseVLA). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

VLAW 등과 함께 imagined rollout으로 실제 interaction을 대체하는 직접 비교 기준이다.

## Verification Boundary

실제/가상 rollout 분모, 물리 일관성 검증, reflector의 감독 비용, 종료 오탐을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 · LIBERO의 OpenVLA-OFT 실행 어댑터 · lib/env_runner/openvla_oft_libero_runner.py [배포 파일](https://raw.githubusercontent.com/iSEE-Laboratory/RehearseVLA/ed4f343d91aeed160863773b27101bf3103b4d6a/lib/env_runner/openvla_oft_libero_runner.py)
- 가중치 · LIBERO-Goal OpenVLA 어댑터 · lora/GOAL/adapter_model.safetensors [배포 파일](https://www.modelscope.cn/api/v1/models/junjxiao/world-env/repo?Revision=009ba91b5c38c0dde0aa65f61a391b05d852089c&FilePath=lora/GOAL/adapter_model.safetensors)
