# Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons

> Evidence maturity: `ABSTRACT_CHECKED`. 아래의 요약·기여는 인용한 원문 쪽에서 추가 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Anthony Liang, Yigit Korkmaz, Jiahui Zhang, Minyoung Hwang, Abrar Anwar, Sidhant Kaushik, Aditya Shah, Alex S. Huang, Luke Zettlemoyer, Dieter Fox, Yu Xiang, Anqi Li, Andreea Bobu, Abhishek Gupta, Stephen Tu, Erdem Bıyık, Jesse Zhang
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: reward-learning, robot-learning, evaluation
- Aliases:
- Official paper: https://www.roboticsproceedings.org/rss22/p140.html
- Venue verification: https://www.roboticsproceedings.org/rss22/p140.html
- Code/Project: https://robometer.github.io/
- Code: https://github.com/robometer/robometer
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

Robometer는 시각언어 모델을 학습해 로봇 조작 영상의 진행도와 궤적 간 선호를 예측한다. [PDF 3쪽](https://www.roboticsproceedings.org/rss22/p140.pdf#page=3)

## Core Idea and Contribution

- 성공·실패 궤적의 비교와 한 궤적 내 진행도 감독을 결합해 보상을 학습한다. [PDF 4쪽](https://www.roboticsproceedings.org/rss22/p140.pdf#page=4)
- 공개한 RBM-1M으로 학습한 모델을 실제·시뮬레이션 과제와 다운스트림 보상 활용에서 평가했다. [PDF 8쪽](https://www.roboticsproceedings.org/rss22/p140.pdf#page=8)

## Observation–State–Action Interface

영상 trajectory·비교 정보 → progress/reward.

## Evaluation Scope and Claim Boundary

대규모 multi-robot 자료와 downstream 실제 robot RL을 보고한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p140.html) · [저자 project/code](https://robometer.github.io/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

C4/C6의 reward·progress·평가 신호를 비교할 핵심 최신 baseline이다.

## Verification Boundary

policy version chronology, failure labels, reward training 중복, calibration을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 원문 대조

저자 표기와 순서는 이 판본의 표제면을 따른다. [표제면](https://www.roboticsproceedings.org/rss22/p140.pdf#page=1)

## 공개 자료

- 코드 — 시각 보상 모델 · robometer/models/rbm.py [배포 파일](https://raw.githubusercontent.com/robometer/robometer/352d160389daa964788de1ec933d1925f3a6de4f/robometer/models/rbm.py)
- 가중치 — Robometer-4B 가중치 샤드 · model-00001-of-00002.safetensors [배포 파일](https://huggingface.co/robometer/Robometer-4B/blob/beef63bc914c5c189329d49c6d712d96d632aa34/model-00001-of-00002.safetensors)
- 데이터 — RBM-1M 분포 밖 평가 표본 · data/chunk-000/file-000.parquet [배포 파일](https://huggingface.co/datasets/robometer/rbm-1m-ood/blob/3f3ee69ecc0ee0db627684da7d599ec26d08175c/data/chunk-000/file-000.parquet)
