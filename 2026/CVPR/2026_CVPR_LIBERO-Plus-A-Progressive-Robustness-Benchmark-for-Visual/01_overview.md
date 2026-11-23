# LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
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
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다.

## Problem and Importance

기본 LIBERO 성공률만으로 VLA의 환경 변화 강건성을 판단하기 어렵다.

## Core Idea and Contribution

배치·camera·robot 초기 상태·언어·조명·배경·sensor noise를 통제한 점진 평가를 구성한다.

## Observation–State–Action Interface

Perturbed 환경/지시 → 기존 VLA → task success와 조건별 분석.

## Evaluation Scope and Claim Boundary

다수 VLA의 simulation robustness를 비교한다. 수치·정확한 난도 split은 본문 확인 필요.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.html) · [저자 project/code](https://github.com/sylvestf/LIBERO-plus). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

기본 성공률과 일반화 성능을 구분하는 현재 VLA 평가의 직접 기준이다.

## Verification Boundary

난도 선정에 쓰인 model, perturbation validity, test contamination을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
