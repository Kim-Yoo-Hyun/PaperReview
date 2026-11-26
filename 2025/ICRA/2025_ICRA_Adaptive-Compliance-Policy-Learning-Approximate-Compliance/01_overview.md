# Adaptive Compliance Policy: Learning Approximate Compliance for Diffusion Guided Control

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · 저자판 PDF 3–6쪽, §III–IV, Tables I–II 확인. [서지·게재 상태](https://api.crossref.org/works/10.1109/ICRA55743.2025.11128452)

- Year/Venue: 2025 / ICRA
- Authors: Yifan Hou, Zeyi Liu, Cheng Chi, Eric Cousineau, Naveen Kuppuswamy, Siyuan Feng, Benjamin Burchfiel, Shuran Song
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: variable-stiffness, diffusion policy, contact, force feedback, Imitation Learning
- Official paper: https://ieeexplore.ieee.org/document/11128452
- Code/Project: https://adaptive-compliance.github.io/

## 연구 질문과 기여

접촉 작업에서는 같은 위치를 지나더라도 물체에 가해야 할 힘이 달라진다. 사람이 시연한 위치·힘으로부터 로봇의 목표 운동과 접촉 방향 강성을 함께 학습할 수 있는지 묻는다.

시연에서 기준 위치·힘과 가상 평형점을 구성하고 주 접촉력 방향의 강성을 근사한다. 시각·힘 이력을 조건으로 한 확산 정책이 출력한 목표를 하위 순응 제어기가 추종한다.

## 평가 범위

실물에서 물체 뒤집기와 꽃병 닦기를 시험했다. 뒤집기 Table I의 다섯 조건, 방법당 총 100회에서 ACP는 96회, 균일 강성의 compliant policy는 23회 성공했다. 꽃병 닦기는 Table II에 따로 보고했다. [원문 및 평가 절](https://arxiv.org/pdf/2410.09309v2#page=4)

## 선정 근거

VLA가 목표 강성을 정하는 연구의 비교 기준이다. 같은 시연에서 운동을 모방하는 것과 접촉 방향의 강성을 선택하는 것의 차이를 점검할 수 있다.

## 공개 자료의 확인 범위

- 코드는 시연에서 순응성 정책을 학습하는 진입점 · PyriteML/train.py에서 확인했다. [코드 배포처](https://github.com/yifan-hou/adaptive_compliance_policy/blob/74d68eca3bfb5cb59da131c6351d9e1c9b129ff6/README.md)
- 데이터는 물체 뒤집기 과제의 가공 시연 · flip_up_230.zip에서 확인했다. [데이터 배포처](https://github.com/yifan-hou/adaptive_compliance_policy)
- 가중치는 ACP 프로젝트 배포 체크포인트 묶음 · checkpoints.zip에서 확인했다. [가중치 배포처](https://github.com/yifan-hou/adaptive_compliance_policy)
