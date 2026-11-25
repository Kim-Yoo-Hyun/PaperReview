# Tune to Learn: How Controller Gains Shape Robot Policy Learning

> Evidence maturity: `FULL_TEXT_CHECKED`. RSS 본문 §III–V, arXiv v1 부록 표 II·VIII와 저자의 공개 점수·배포 자료를 확인했다.

- Year/Venue: 2026 / RSS
- Authors: Antonia Bronars, Younghyo Park, Pulkit Agrawal
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: controller-gain, imitation-learning, reinforcement-learning, sim-to-real
- Aliases: Tune to Learn, Tune to Learn: How Controller Gains Affect Robot Policy Learning
- Official paper: https://www.roboticsproceedings.org/rss22/p139.html
- Venue verification: https://www.roboticsproceedings.org/rss22/p139.html
- Code/Project: https://younghyopark.me/tune-to-learn/
- Code: [저자 평가 자료·시연 코드·정책 내보내기](https://github.com/younghyopark/tune-to-learn/tree/1775091ee2fdb683e1e767822e5caa87cdfdba4a)
- Source audit: 11월 19일 본문·부록과 저자 공개 자료를, 11월 23일 개요의 세 주장과 RSS 쪽수를 대조했다. 공식 제목·별칭과 저자 순서는 RSS 게재본을 따른다. 공개 점수 재분석과 정책 재학습·실물 재현을 구분한다.

## Problem and Importance

이 연구는 로봇 위치 제어기의 강성과 감쇠 이득이 모방학습·강화학습·시뮬레이션에서 실물로의 전이에 어떤 영향을 주는지 평가한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss22/p139.pdf#page=1)

## Core Idea and Contribution

- 상태에 반응하는 정책에서는 동일한 제어 이득에서도 실효 강성이 달라질 수 있음을 분석하고, 이득과 학습 설정을 바꾸는 비교를 설계했다. [PDF 3쪽](https://www.roboticsproceedings.org/rss22/p139.pdf#page=3) · [PDF 4쪽](https://www.roboticsproceedings.org/rss22/p139.pdf#page=4)
- 시험한 과제에서 행동 복제는 순응적이고 과감쇠인 조건의 이득을 보았으며, 강화학습은 설정 조정으로 여러 이득에 적응했고, 높은 강성과 과감쇠의 조합은 실물 전이에 불리했다. [PDF 7쪽](https://www.roboticsproceedings.org/rss22/p139.pdf#page=7) · [PDF 8쪽](https://www.roboticsproceedings.org/rss22/p139.pdf#page=8) · [PDF 9쪽](https://www.roboticsproceedings.org/rss22/p139.pdf#page=9)

## 실험 설계와 읽는 이유

행동 복제는 같은 토크 시연을 이득별 위치 목표로 바꿨고, 온라인 RL은 고정 이득마다 행동 배율을 다시 탐색했다. 실물 FR3에서는 열린 루프의 동정 오차와 정책을 실행한 궤적 오차를 따로 측정했다. 이 비교는 접촉 정책에 가변 강성을 도입할 때 어떤 고정 이득 기준선이 필요한지를 보여 준다. [방법](./03_method.md) · [과제별 수치와 공개 자료 범위](./04_evaluation.md)

## 공개 산출물

- 저자 웹 도구의 큐브 들기 점수 정의와 튜닝 결과 표시 코드를 확인했다. 전체 BC·PPO 학습 코드는 확인 범위 밖이다. [배포 파일](https://raw.githubusercontent.com/younghyopark/tune-to-learn/1775091ee2fdb683e1e767822e5caa87cdfdba4a/static/assets/shapeability_widget.html)
- 단일 Franka의 식기 선반 과제에서 K1024D128M10 조건으로 내보낸 ONNX 정책 파일을 확인했다. [배포 파일](https://raw.githubusercontent.com/younghyopark/tune-to-learn/1775091ee2fdb683e1e767822e5caa87cdfdba4a/static/assets/models/dishrack_single_franka_2f85_v2/K1024D128M10/policy.onnx)
- 공개한 Optuna CSV 12개 중 FR3 관절 도달 K16·D24 파일에서 시행별 행동 배율과 점수 열을 확인했다. [배포 파일](https://raw.githubusercontent.com/younghyopark/tune-to-learn/1775091ee2fdb683e1e767822e5caa87cdfdba4a/static/assets/optuna_csvs_12/optuna_action_scale_learnability-cat-rel-joint-reach-sysid-franka-v0_new_K16_D24_tpe.csv)
