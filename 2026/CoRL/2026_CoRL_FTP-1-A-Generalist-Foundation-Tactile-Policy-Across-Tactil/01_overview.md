# FTP-1: A Generalist Foundation Tactile Policy Across Tactile Sensors for Contact-Rich Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · 저자판 v4 PDF 3–9쪽, §§2–4, Tables 1–3 확인. [서지·게재 상태](https://2026.corl.org/program/accepted-papers/)

- Year/Venue: 2026 / CoRL
- Authors: Chengbo Yuan, Zicheng Zhang, Mingjie Zhou, Wendi Chen, Yi Wang, Zhuoyang Liu, Dantong Niu, Shuo Wang, Hui Zhang, Wenkang Zhang, Yingdong Hu, Yuanqing Gong, Wanli Xing, Chuan Wen, Cewu Lu, Kaifeng Zhang, Yang Gao
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: VLA, tactile sensing, cross-sensor transfer, contact, Flow Matching
- Official paper: https://arxiv.org/abs/2606.13102
- Code/Project: https://ftp1-policy.github.io/

## 연구 질문과 기여

촉각 센서마다 출력의 차원과 배열이 달라 로봇 간 접촉 조작 데이터를 함께 학습하기 어렵다. 한 촉각 정책에서 다양한 센서의 사전학습을 재사용할 수 있는지 묻는다.

형태와 신호 종류에 따른 촉각 토큰을 시각·언어 문맥과 결합해 행동을 생성한다. 이미 본 센서와 새로운 센서·기체를 구분하고 하류 과제의 시연으로 미세조정한다.

## 평가 범위

UniVTAC 시뮬레이션 및 실물 로봇에서 비교했다. 새로운 센서로 미세조정한 실물 세 과제의 평균 성공률은 46.6%, 동일 촉각 구조에서 촉각 사전학습을 생략한 기준은 15.0%였다. Table 3의 차이는 미세조정 이후의 결과다. [원문 및 평가 절](https://arxiv.org/pdf/2606.13102v4#page=6)

## 선정 근거

센서 간 촉각 표현 전이를 비교할 때 사전학습과 하류 시연의 기여를 구분할 기준을 제공한다.

## 공개 자료의 확인 범위

- 코드는 UniVTAC의 촉각 정책 평가 진입점 · UniVTAC/scripts/eval_policy.py에서 확인했다. [코드 배포처](https://github.com/michaelyuancb/ftp1-policy/blob/89fa681d6c014cce28300946b7526db808e0b1c1/README.md)
- 가중치는 FTP-1 사전학습 정책 가중치 · model.safetensors에서 확인했다. [가중치 배포처](https://huggingface.co/MJJJJ1064/ftp1_v0426_50kstep/blob/d6e5b73e473d3e70fb5f53132a2b1c35b5031156/model.safetensors)
- 데이터는 FTP-1 사전학습용 배포 모음에 포함된 RDP 촉각 자료 · RDP/RDP.tar에서 확인했다. [데이터 배포처](https://huggingface.co/datasets/MJJJJ1064/FTP-1-Dataset/blob/d287c9c532514a08b2eb29bf1259997bb32f4f3b/RDP/RDP.tar)
