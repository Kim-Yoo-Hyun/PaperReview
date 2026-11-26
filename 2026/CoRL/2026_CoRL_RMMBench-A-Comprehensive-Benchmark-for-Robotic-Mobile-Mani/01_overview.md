# RMMBench: A Comprehensive Benchmark for Robotic Mobile Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 CoRL 공식 채택 목록과 저자판 PDF 4–9쪽의 과제·과정 지표 및 평가 대조. Full-text scope의 수치·조건만 기록했다.

- Year/Venue: 2026 / CoRL
- Authors: Huapeng Li, Fuxiang Feng, Jinqiu Fan, Shuo Yang, Fengjiao Chen, Xuezhi Cao, Ran Song, Wei Zhang
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Benchmark, mobile manipulation, Navigation, long-horizon, process evaluation
- Official paper: https://arxiv.org/abs/2610.05414
- Code/Project: https://mxxq-stack.github.io/rmmbench-project/
- Code: https://github.com/mxxq-stack/RMMBench

## 연구 질문과 기여

장기 이동 조작이 실패했을 때 지도·위치 추정이 문제였는지 물체 조작이 문제였는지 종단 성공률로 판정하기 어렵다.

이동과 조작에 고수준 지시를 적용하고, 실행 중의 국소 위치 정확도·행동 반복·과제 진행을 별도로 기록한다.

## 평가 범위

모의 조작 및 이동-조작을 비교하며 조감도 유무를 나눠 평가한다. [arXiv 랜딩 초록](https://arxiv.org/abs/2610.05414)은 70개, 내려받은 PDF §3.1·§4.1은 90개(조작 60·복합 30)를 제시하므로 결과마다 해당 판본과 표를 함께 사용한다. [원문 및 평가 절](https://arxiv.org/pdf/2610.05414#page=7)

## 선정 근거

내비게이션의 위치 오차가 길어진 조작 계획에 어떻게 전파되는지 확인할 평가 자원이다.
