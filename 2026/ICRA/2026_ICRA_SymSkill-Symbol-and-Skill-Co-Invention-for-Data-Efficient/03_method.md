# Method — SymSkill: Symbol and Skill Co-Invention for Data-Efficient and Reactive Long-Horizon Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 IEEE 게재 DOI와 저자판 PDF 3–7쪽의 방법·표 Ⅱ 및 실물 평가 대조. Full-text scope의 수치·조건만 기록했다.

## 관측과 출력

로봇과 물체의 자세에서 술어를 평가하고 현재 스킬의 연속 행동을 실행한다.

## 학습·실행 방법

분절·라벨 없는 play 데이터에서 상대 자세 술어, 이산 연산자와 안정적인 SE(3) 동역학 기술을 함께 학습한다. 유지 조건이 깨지면 기술을 중단하고 상위 계획을 다시 고른다.

- 저자판 표 Ⅱ에서 Diffusion Policy를 모의 조작 기준선으로 비교한다. [pr-0019 · 원문](https://arxiv.org/pdf/2510.01661#page=6)
