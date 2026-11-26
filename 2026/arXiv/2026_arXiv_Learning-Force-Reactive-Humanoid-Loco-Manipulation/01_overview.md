# Learning Force-Reactive Humanoid Loco-Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 arXiv PDF 2–8쪽의 힘 관측·명령 어블레이션과 저자 코드. 게재 확정은 확인되지 않음 대조. Full-text scope의 수치·조건만 기록했다.

- Year/Venue: 2026 / arXiv
- Authors: Sihang Li, Xiaofeng Guo, Jinkun Cao, Charlie Cheng, Ruihan Yang, Chen Feng, Guanya Shi, Haozhi Qi
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: humanoid, whole-body control, force control, Diffusion, Imitation Learning, contact
- Official paper: https://arxiv.org/abs/2610.35862
- Code/Project: https://louis-leee.github.io/FLoRe/
- Code: https://github.com/amazon-far/FLoRe

## 연구 질문과 기여

양손으로 힘을 내면서 균형을 유지해야 하는 휴머노이드 과제에서는 위치 명령만으로 접촉 반응을 지정하기 어렵다.

휴대형 힘 센서 그리퍼와 착용형 추적기로 시연을 얻는다. 확산 정책이 양손 힘과 운동 명령을 예측하며, 전신 제어기가 손목의 힘 오차를 적분해 명령 방향의 힘을 추종한다.

## 평가 범위

모의 힘·운동 추종 및 G1 실물의 보드 닦기, 상자 돌리기, 갠트리 밀기를 평가했다. 표 Ⅱ는 같은 제어기에서 위치 전용 정책과 힘 관측·명령 변형을 비교한다. [원문 및 평가 절](https://arxiv.org/pdf/2610.35862#page=7)

## 선정 근거

G1 걸쇠 해제 연구와 가장 가까운 공개 힘 반응 정책 중 하나다. 접촉력 추종과 해제 직후 균형 반응을 구분할 근거를 준다.

## 공개 범위

- 공식 README는 저수준 5-keypoint 제어기 ONNX를 안내한다. 상위 확산 정책의 학습·배포 가이드는 공개 계획에 남아 있다. [저자 배포 자료](https://github.com/amazon-far/FLoRe/tree/cb99fd05ac3e43eefdd1269647a29b98be2b6ea3#-release-plan)
