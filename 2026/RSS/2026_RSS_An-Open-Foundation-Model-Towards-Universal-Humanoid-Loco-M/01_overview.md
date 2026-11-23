# Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Source audit: 2026-11-16: RSS metadata·공식 project/code 및 arXiv v1 §III–IV, Appendix IX–X의 지정 내용 확인. RSS 최종본문 전체 대조·사용자 정독·실험을 의미하지 않는다.

- Year/Venue: 2026 / RSS
- Authors: Songlin Wei, Hongyi Jing, Boqian Li, Zhenyu Zhao, Jiageng Mao, Zhenhao Ni, Sicheng He, Sheng Zang, Xiawei Liu, Kaidi Kang, Jie Liu, Weiduo Yuan, Marco Pavone, Di Huang, Yue Wang
- Primary track: VLA and generalist robot policies
- Tags: VLA, humanoid, loco-manipulation, human-video, flow-matching, whole-body-control
- Official paper: https://www.roboticsproceedings.org/rss22/p021.html
- Project: https://psi-lab.ai/Psi0/
- Code: https://github.com/physical-superintelligence-lab/Psi0
- Public identifiers: {"arxiv": "2603.12263", "doi": "10.15607/RSS.2026.XXII.021"}

## Why This Paper Is Here

필수 추가 요청 논문. Human-video 사전학습에서 humanoid loco-manipulation으로 이어지는 데이터·행동 표현·제어 경계를 비교할 NEXT다. 공식 명칭은 **Ψ₀(Psi-Zero)**이며 φ₀·π₀와 다른 논문이다. [RSS 2026 게재](https://www.roboticsproceedings.org/rss22/p021.html)를 확인했다.

## Problem and Core Ideas

인간과 로봇의 운동학 차이를 고려해 VLM의 행동 표현 학습과 로봇 action expert 학습을 단계별로 나눈다. Task-space token 예측 뒤 joint-space flow matching을 적용한다. [공식 project](https://psi-lab.ai/Psi0/).

## Interface and Scope

Head RGB·지시·상태 → VLM/action expert → 상체 관절·하체 명령 → 별도 RL 제어기. 논문 v1의 실물평가는 Unitree G1이다. 다양한 embodiment에 대한 보편적 성공이나 VLA와 RL의 동일 가중치 공동 학습을 입증한 결과로 해석하지 않는다.

## Version Boundary

본문 노트는 [arXiv v1](https://arxiv.org/html/2603.12263v1) 기준이다. [공개 repository](https://github.com/physical-superintelligence-lab/Psi0)의 후속 SONIC checkpoint·데이터 recipe는 논문 당시 AMO 구성과 구분한다. 구현 공개와 이 저장소에서의 재현 성공도 별개다.
