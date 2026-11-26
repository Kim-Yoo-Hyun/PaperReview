# Bi-VLA: Bilateral Control-Based Imitation Learning via Vision-Language Fusion for Action Generation

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §III, §IV, Tables II–IV 검토. [방법·평가 원문](https://arxiv.org/html/2509.18865)

- Year/Venue: 2026 / IEEE ARSO
- Authors: Masato Kobayashi, Thanpimon Buamanee
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: VLA, bilateral control, joint torque, joint velocity, visuolinguistic grounding
- Official paper: https://ieeexplore.ieee.org/document/11536111
- Code/Project: https://mertcookimg.github.io/bi-vla/

## 연구 질문과 기여

같은 장면에서 어느 물체를 옮기고 어느 위치에 놓을지는 언어에 따라 달라진다. 관절 힘을 재현하는 정책도 목표를 잘못 고를 수 있다.

천장·그리퍼 RGB와 언어를 FiLM으로 결합하고 follower 관절 상태와 함께 Transformer CVAE에 넣는다. SigLIP와 DistilBERT를 사용한 변형을 비교한다.

## 정책 출력

다섯 관절의 leader 각도·각속도·토크를 함께 예측해 한 시점당 15개 참조값을 낸다. 4채널 양방향 제어기가 참조를 follower의 전류 명령으로 변환한다. [방법 원문](https://arxiv.org/html/2509.18865)

## 평가 범위

실물 팔에서 지시가 정하는 출발지 또는 목적지에 공을 옮겼다. 조건당 10회이며 집기·이동·놓기 전체가 성공해야 성공으로 계산한다. 두 목표가 같은 외관을 가질 때의 지시 구별을 평가했다. [원문 및 평가 절](https://arxiv.org/html/2509.18865)

## 선정 근거

Bi-LAT의 운동·토크 인터페이스에서 시각과 언어의 결합 방식을 바꿨다. 단순히 토크를 학습 보조량으로 예측한 연구와 구별할 직접 선행이다.
