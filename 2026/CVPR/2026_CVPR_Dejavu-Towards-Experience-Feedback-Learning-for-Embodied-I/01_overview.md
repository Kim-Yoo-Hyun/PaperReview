# Dejavu: Towards Experience Feedback Learning for Embodied Intelligence

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
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
- Source audit: 2026-11-02 공식 proceedings/publisher의 서지·abstract와 저자 project/code 소개를 확인했다. 노트는 abstract/project 기반이며 본문 정독·native 실행을 뜻하지 않는다. 사용자 읽기 상태는 UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

Dejavu는 배포 중 축적한 조작 경험을 다시 찾아 고정한 VLA의 행동에 잔차 보정을 더한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_Dejavu_Towards_Experience_Feedback_Learning_for_Embodied_Intelligence_CVPR_2026_paper.pdf#page=1)

## Core Idea and Contribution

- 의미적으로 유사한 경험을 검색하고 잔차 강화학습으로 훈련한 경험 피드백 네트워크가 기본 행동을 수정하게 한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_Dejavu_Towards_Experience_Feedback_Learning_for_Embodied_Intelligence_CVPR_2026_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_Dejavu_Towards_Experience_Feedback_Learning_for_Embodied_Intelligence_CVPR_2026_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_Dejavu_Towards_Experience_Feedback_Learning_for_Embodied_Intelligence_CVPR_2026_paper.pdf#page=5)
- LIBERO와 실제 로봇 조작에서 경험이 쌓일 때의 성공률을 측정하고 검색 및 피드백을 제거한 조건과 비교했다. [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_Dejavu_Towards_Experience_Feedback_Learning_for_Embodied_Intelligence_CVPR_2026_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_Dejavu_Towards_Experience_Feedback_Learning_for_Embodied_Intelligence_CVPR_2026_paper.pdf#page=8)

## Observation–State–Action Interface

현재 관측·지시·검색 경험과 base VLA action → EFN 보정 → 실행. Base parameter 고정이 전체 시스템 무학습을 뜻하지 않는다.

## Evaluation Scope

공식 abstract와 author project는 여러 embodied task 및 실제 조작 사례를 보고한다. 정량 성과·matched bank의 범위는 본문 확인 전 확정하지 않는다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Dejavu_Towards_Experience_Feedback_Learning_for_Embodied_Intelligence_CVPR_2026_paper.html) · [저자 project](https://dejavu2025.github.io/).

## Why This Paper Is Here — Researcher Interpretation

Residual RL과 retrieval의 직접 결합이므로 NEXT에 추가한다. Bank 성장·frozen backbone이라는 조합 자체를 새 연구 공백으로 주장하지 않도록 현재 후보의 선행 경계를 보완한다.

범위와 수치의 미확인 항목은 [평가 노트](./04_evaluation.md)에, 제안하는 반증 질문은 [insights](./05_insights.md)에 둔다.

## 공개 자료

- 코드 — 프로젝트의 코드 링크에 공개 예정이라고 명시되어 있다. [저자 공개 안내](https://dejavu2025.github.io/)
