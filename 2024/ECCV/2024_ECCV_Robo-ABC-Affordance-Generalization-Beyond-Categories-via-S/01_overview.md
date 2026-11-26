# Robo-ABC: Affordance Generalization Beyond Categories via Semantic Correspondence for Robot Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2024 / ECCV
- Authors: Yuanchen Ju, Kaizhe Hu, Guowei Zhang, Gu Zhang, Mingrun Jiang, Huazhe Xu
- Category: 3D Vision-Language Understanding
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Robotics, evaluation, affordance, human-video, retrieval
- Aliases:
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5748_ECCV_2024_paper.php
- Venue verification: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5748_ECCV_2024_paper.php
- Code/Project: https://tea-lab.github.io/Robo-ABC/
- Code: https://github.com/TEA-Lab/Robo-ABC
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05748.pdf
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다. 평가 조건은 04_evaluation.md에 쪽수와 함께 기록했다.

## Problem and Importance

Robo-ABC는 사람이 물체를 다루는 영상에서 모은 접촉점을 시각적·의미적으로 비슷한 물체에 대응시켜 처음 보는 범주의 파지 위치를 찾는다. [PDF 1쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05748.pdf#page=1) · [PDF 6쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05748.pdf#page=6)

## Core Idea and Contribution

- 사람 손과 물체의 상호작용에서 접촉점 메모리를 구축하고, 사전학습 확산 모델의 특징 대응으로 검색한 접촉점을 목표 이미지에 옮긴다. [PDF 5쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05748.pdf#page=5) · [PDF 6쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05748.pdf#page=6) · [PDF 7쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05748.pdf#page=7)
- 영상의 접촉점 예측과 실물 파지를 따로 평가했으며, 일곱 물체 범주에 걸친 실물 파지 성공률은 85.7%, 비교 기준선은 68.6%였다. [PDF 11쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05748.pdf#page=11) · [PDF 12쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05748.pdf#page=12)

## Observation–State–Action Interface

새 물체 영상·contact memory → affordance/contact point → robot manipulation.

## Evaluation Scope and Claim Boundary

실물 파지 성공률 85.7%와 VRB 기준선의 68.6%는 일곱 물체 범주에서 얻은 값이다. 이미지에 대한 접촉점 예측 정확도는 별도 평가다. [PDF 11쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05748.pdf#page=11) · [PDF 12쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05748.pdf#page=12)

근거: [공식 paper/abstract](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5748_ECCV_2024_paper.php) · [저자 project/code](https://tea-lab.github.io/Robo-ABC/) · [공식 code](https://github.com/TEA-Lab/Robo-ABC).

## 검색 태그 근거

사람이 물체를 만지는 영상에서 접촉점을 저장하고 동결한 확산 모델 특징으로 새 물체에 대응시킨다. 실제 팔의 파지는 깊이 기하와 AnyGrasp를 이용한다. 확산은 특징 추출 구성요소다. [원문 6쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05748.pdf#page=6) · [원문 8쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05748.pdf#page=8)

## Why This Paper Is Here — Researcher Interpretation

Semantic representation을 실제 contact/action에 연결하는 비교용 3D/affordance 지원 연구다.

## Verification Boundary

2D/3D lifting, grasp 실행기, source별 수치 차이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
