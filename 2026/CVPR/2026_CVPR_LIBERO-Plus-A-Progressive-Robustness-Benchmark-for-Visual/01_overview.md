# LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CVPR
- Authors: Senyu Fei, Siyin Wang, Junhao Shi, Zihao Dai, Jikun Cai, Pengfang Qian, Li Ji, Xinzhe He, Shiduo Zhang, Zhaoye Fei, Jinlan Fu, Jingjing Gong, Xipeng Qiu
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, Benchmark, generalization
- Aliases: LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.html
- Venue verification: https://openaccess.thecvf.com/content/CVPR2026/html/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.html
- Code/Project: https://github.com/sylvestf/LIBERO-plus
- Code: https://github.com/sylvestf/LIBERO-plus
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

LIBERO-Plus는 LIBERO 작업에 단계별 교란을 가해 높은 표준 성공률이 환경 변화에서도 유지되는지 평가한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.pdf#page=1)

## Core Idea and Contribution

- 물체 배치·카메라·로봇 시작 상태·지시·조명·배경·센서 잡음의 일곱 축을 조절해 단일 변화에 대한 취약성을 측정한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.pdf#page=4)
- 여러 VLA의 지시 의존성과 복합 변화에서의 일반화를 평가해 원래 환경의 성공률로는 드러나지 않던 실패를 보고했다. [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.pdf#page=6) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.pdf#page=8)

## Observation–State–Action Interface

Perturbed 환경/지시 → 기존 VLA → task success와 조건별 분석.

## Evaluation Scope and Claim Boundary

다수 VLA의 simulation robustness를 비교한다. 수치·정확한 난도 split은 본문 확인 필요.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.html) · [저자 project/code](https://github.com/sylvestf/LIBERO-plus). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

기본 성공률과 일반화 성능을 구분하는 현재 VLA 평가의 직접 기준이다.

## Verification Boundary

난도 선정에 쓰인 model, perturbation validity, test contamination을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 — LIBERO-Plus 조명 변화 과제 정의 · libero/libero/bddl_files/libero_10/KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_light_1.bddl [배포 파일](https://raw.githubusercontent.com/sylvestf/LIBERO-plus/4976dc30028e805ff8094b55501d532c48fec182/libero/libero/bddl_files/libero_10/KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_light_1.bddl)
- 가중치 — 혼합 자료로 조정한 OpenVLA-OFT 행동 헤드 · action_head--150000_checkpoint.pt [배포 파일](https://huggingface.co/Sylvest/openvla-7b-oft-finetuned-libero-plus-mixdata/blob/a85655ec941bae6644c9fbdf62db02b9726d7cf5/action_head--150000_checkpoint.pt)
- 데이터 — LIBERO-Plus 변형 장면 혼합 시연 · libero_plus_mixdata.zip [배포 파일](https://huggingface.co/datasets/Sylvest/libero_plus_rlds/blob/fb0c7029b076030d5d57227229e4f7460def1f7c/libero_plus_mixdata.zip)
