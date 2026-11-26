# GentleHumanoid: Learning Upper-Body Compliance for Contact-Rich Human and Object Interaction

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 IEEE 온라인 출판 2026-10-26와 권호 2027-01, 저자판 PDF 3–8쪽 및 배포 코드 대조. Full-text scope의 수치·조건만 기록했다.

- Year/Venue: 2026 / RA-L
- Authors: Qingzhou Lu, Yao Feng, Baiyu Shi, Michael Piseno, Zhenan Bao, C. Karen Liu
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: whole-body control, Impedance Control, humanoid, Reinforcement Learning, force threshold
- Official paper: https://ieeexplore.ieee.org/abstract/document/11753909
- Code/Project: https://gentle-humanoid.axell.top/
- Code: https://github.com/Axellwppr/gentle-humanoid

## 연구 질문과 기여

휴머노이드가 외력을 모두 밀어내는 추종 정책으로는 상체 접촉과 자연스러운 움직임을 함께 만들기 어렵다.

어깨·팔꿈치·손의 스프링-댐퍼 목표를 이용해 동작 추종과 순응을 함께 학습한다. 과제에 따라 조절할 수 있는 힘 상한을 제어에 넣는다.

## 평가 범위

시뮬레이션과 G1 실물의 밀기, 포옹, 물체 조작에서 상체 순응과 힘을 평가했다. 배포 코드와 훈련 코드는 서로 다른 저장소다. [원문 및 평가 절](https://arxiv.org/pdf/2511.04679#page=7)

## 선정 근거

걸쇠 해제 검증에서 순응 목표·힘 상한을 갖춘 공개 전신 제어 기준이다.

## 공개 범위

- G1 배포용 ONNX 파일이 공식 저장소에 있다. [저자 배포 자료](https://github.com/Axellwppr/gentle-humanoid/blob/12aee8d84b9bf998c910b717eb9e3cbedd4d0559/assets/ckpts/G1/policy.onnx)
