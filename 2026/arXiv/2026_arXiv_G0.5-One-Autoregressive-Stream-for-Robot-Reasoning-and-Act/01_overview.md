# G0.5: One Autoregressive Stream for Robot Reasoning and Action

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §3–5, BEHAVIOR Challenge evaluation, §6 limitations 검토. [방법·평가 원문](https://arxiv.org/html/2608.11739) · [저자 코드](https://github.com/OpenGalaxea/GalaxeaVLA)

- Year/Venue: 2026 / arXiv
- Authors: Yicheng Liu, Zibin Dong, Baijun Ye, Tianyuan Yuan, Tao Jiang, Anqi Yang, Shicheng Cao, Haonan Liu, Yue Sun, Zihan Guo, Xiao Liu, Dong Ke, Changxun Pan, Chenru Wu, Tailai Cheng, Xiaoshu Ren, Xinlei Zhang, Jianning Cui, Zijie Zhao, Haoyu Zhang, Kaiming Xu, Haodong Yang, Bowen Zhang, Jiahui Niu, Shaoting Zhu, Shiduo Zhang, Hang Zhao
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, autoregressive policy, action tokenization, mobile manipulation, task decomposition
- Official paper: https://arxiv.org/abs/2608.11739
- Code/Project: https://opengalaxea.github.io/G05/

## 연구 질문과 기여

추론 텍스트와 다기체 행동을 하나의 자기회귀 모델에서 처리할 때, 로봇마다 제어 축과 토큰 길이가 달라지는 문제를 다룬다.

Qwen3.5 기반 모델이 선택적으로 물체·하위 과제·그리퍼 경로를 텍스트로 생성한 뒤 행동 코드를 같은 스트림에서 예측한다. ActionCodec이 신체 부위별 이산 코드를 연속 명령으로 복원한다.

## 정책 출력

다중 영상·언어 지시·기체 ID·고유수용 상태에서 27차원 공용 명령을 부위별로 부호화한다. 좌우 제어가 각 9축, 그리퍼가 각 1축, 하부가 7축이다. 기체가 쓰지 않는 슬롯은 비운다. 기본 자기회귀 경로와 선택적인 연속 후처리 전문가를 구분한다. [방법 원문](https://arxiv.org/html/2608.11739)

## 평가 범위

BEHAVIOR 2025 시뮬레이션의 이동·조작 50과제와 실물 기체의 조작 평가를 보고한다. 하부 구동만의 성능은 독립 평가하지 않았고, 일부 삽입과 반투명 문에서 실패가 남는다. [원문 및 평가 절](https://arxiv.org/html/2608.11739)

## 선정 근거

FAST의 시간축 행동 압축, π0.5의 텍스트·연속 전문가와 비교할 수 있는 부위별 자기회귀 표현이다. 실제로 채워진 기체별 슬롯을 확인해야 한다.
