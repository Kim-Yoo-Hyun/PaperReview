# SymSkill: Symbol and Skill Co-Invention for Data-Efficient and Reactive Long-Horizon Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 IEEE 게재 DOI와 저자판 PDF 3–7쪽의 방법·표 Ⅱ 및 실물 평가 대조. Full-text scope의 수치·조건만 기록했다.

- Year/Venue: 2026 / ICRA
- Authors: Yifei Simon Shao, Yuchen Zheng, Sunan Sun, Pratik Chaudhari, Vijay Kumar, Nadia Figueroa
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: symbolic planning, Imitation Learning, skill composition, failure recovery, long-horizon
- Official paper: https://symskill.github.io/
- Code/Project: https://symskill.github.io/
- Code: https://github.com/shaoyifei96/Symskill

## 연구 질문과 기여

시연으로 얻은 기술을 긴 작업에서 조합하려면 완료와 실패를 인식할 조건을 함께 알아야 한다.

분절·라벨 없는 play 데이터에서 상대 자세 술어, 이산 연산자와 안정적인 SE(3) 동역학 기술을 함께 학습한다. 유지 조건이 깨지면 기술을 중단하고 상위 계획을 다시 고른다.

## 평가 범위

RoboCasa에서 기술 조합과 상태 변화에 대한 반응을 비교하고 실물 Franka에서 학습한 기술을 사용했다. [원문 및 평가 절](https://arxiv.org/pdf/2510.01661#page=6)

## 선정 근거

관측 가능한 실패 조건과 재계획을 갖춘 비-VLA 장기 조작 기준선이다.
