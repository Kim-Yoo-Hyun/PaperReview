# HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · 저자판 v2 PDF 3–7쪽, §§III–IV의 교사·학생과 실물 과제 확인. [서지·게재 상태](https://2026.ieee-iros.org/program/paper-index/)

- Year/Venue: 2026 / IROS
- Authors: Konstantin Gubernatorov, Mikhail Sannikov, Ilya Mikhalchuk, Egor Kuznetsov, Makar Artemov, Ogunwoye Faith Oluwatobi, Marcelino Julio Fernando, Artem Asanov, Ziang Guo, Dzmitry Tsetserukou
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: VLA, tactile sensing, knowledge distillation, Flow Matching, contact
- Official paper: https://ieeexplore.ieee.org/document/11777360
- Code/Project: https://advanced-robotic-manipulation.github.io/websites/websites/hapticvla/

## 연구 질문과 기여

취약한 물체를 집을 때 훈련에서 측정한 촉각이 배포 시 촉각 센서를 쓰지 않는 정책에도 도움이 되는지 묻는다.

접촉 및 과도한 파지력으로 가중한 flow matching으로 교사를 학습한다. 학생은 시각·상태에서 촉각 표현을 추정하고 교사의 행동을 모방한다.

## 평가 범위

§IV에서 손상되거나 변형되기 쉬운 물체를 포함한 실물 세 과제로 시각·시촉각 기준선과 학생을 비교한다. 성공과 과도한 파지력 문제를 검토했다. 훈련 중의 촉각 보상은 배포 중의 힘 측정과 구별한다. [원문 및 평가 절](https://arxiv.org/pdf/2603.15257v2#page=6)

## 선정 근거

실행 중 촉각 피드백의 효과와 시연·훈련에서 촉각으로 배운 사전 지식의 효과를 나눌 비교 기준이다.

## 공개 자료의 확인 범위

- 코드는 촉각 교사의 표현을 학생 정책으로 증류하는 학습 코드 · training/train_distill_v2.py에서 확인했다. [코드 배포처](https://github.com/Advanced-Robotic-Manipulation/crab/blob/de2362f78eab0988b341d820b4957d8bf2d5e154/README.md)
- 가중치는 촉각 표현을 증류한 Crab 정책 · best/model.pt에서 확인했다. [가중치 배포처](https://huggingface.co/armteam/crab-smolvla-hapticsvla/blob/cec04c7c2f878b242d312b19f861ea8eab0fbe0a/best/model.pt)
- 데이터는 Crab의 실물 촉각 조작 시연 중 공개 에피소드 · egg_carton_to_tray/pick_place_medium_20260226_1638/data/chunk-000/file-000.parquet에서 확인했다. [데이터 배포처](https://huggingface.co/datasets/armteam/crab-manipulation-dataset/blob/740b2b521e78faf97f3872d468b0a35484c6e889/egg_carton_to_tray/pick_place_medium_20260226_1638/data/chunk-000/file-000.parquet)
