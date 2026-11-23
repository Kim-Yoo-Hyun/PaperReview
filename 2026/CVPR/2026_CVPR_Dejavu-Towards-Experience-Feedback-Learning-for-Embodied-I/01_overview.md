# Dejavu: Towards Experience Feedback Learning for Embodied Intelligence

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CVPR
- Authors: Shaokai Wu, Yanbiao Ji, Qiuchang Li, Zhiyi Zhang, Qichen He, Wenyuan Xie, Guodong Zhang, Bayram Bayramli, Yue Ding, Hongtao Lu
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: VLA, residual-RL, experience-retrieval, post-deployment
- Aliases: Dejavu, EFN
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Dejavu_Towards_Experience_Feedback_Learning_for_Embodied_Intelligence_CVPR_2026_paper.html
- Venue verification: https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Dejavu_Towards_Experience_Feedback_Learning_for_Embodied_Intelligence_CVPR_2026_paper.html
- Code/Project: https://dejavu2025.github.io/
- Code: not_released
- Source audit: 2026-11-02 공식 proceedings/publisher의 서지·abstract와 저자 project/code 소개를 확인했다. 노트는 abstract/project 기반이며 본문 정독·native 실행을 뜻하지 않는다. 사용자 읽기 상태는 UNREAD 유지.

## Problem and Importance

고정 VLA가 배포 후 쌓이는 경험을 행동 개선에 사용하는 경로를 다룬다.

## Core Idea and Contribution

검색한 경험을 조건으로 residual action을 내는 EFN을 RL로 학습하고, 배포 중 성공 trajectory를 경험 bank에 추가한다.

## Observation–State–Action Interface

현재 관측·지시·검색 경험과 base VLA action → EFN 보정 → 실행. Base parameter 고정이 전체 시스템 무학습을 뜻하지 않는다.

## Evaluation Scope

공식 abstract와 author project는 여러 embodied task 및 실제 조작 사례를 보고한다. 정량 성과·matched bank의 범위는 본문 확인 전 확정하지 않는다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Dejavu_Towards_Experience_Feedback_Learning_for_Embodied_Intelligence_CVPR_2026_paper.html) · [저자 project](https://dejavu2025.github.io/).

## Why This Paper Is Here — Researcher Interpretation

Residual RL과 retrieval의 직접 결합이므로 NEXT에 추가한다. Bank 성장·frozen backbone이라는 조합 자체를 새 연구 공백으로 주장하지 않도록 현재 후보의 선행 경계를 보완한다.

범위와 수치의 미확인 항목은 [평가 노트](./04_evaluation.md)에, 제안하는 반증 질문은 [insights](./05_insights.md)에 둔다.
