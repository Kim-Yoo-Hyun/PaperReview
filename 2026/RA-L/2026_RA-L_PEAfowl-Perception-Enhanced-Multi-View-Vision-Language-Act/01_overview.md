# PEAfowl: Perception-Enhanced Multi-View Vision-Language-Action for Bimanual Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2026 / RA-L
- Authors: Qingyu Fan, Zhaoxiang Li, Jinrui Hu, Yi Lu, Wang Chen, Qiu Shen, Xiao-xiao Long, Yinghao Cai, Tao Lu, Shuo Wang, Xun Cao
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: multi-view, 3D-representation, bimanual, VLA, RGB-D, action diffusion
- Aliases: PEAfowl
- Official paper: https://peafowlvla.github.io/
- Venue verification: https://ieeexplore.ieee.org/document/11661761/
- Code/Project: https://peafowlvla.github.io/
- Code: https://github.com/Qingyu-Fan/PEAfowl
- Full-text retrieval: https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11661761
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다.

## Problem and Importance

PEAfowl은 여러 카메라의 시각 토큰을 깊이에 따라 3차원에 배치하고 언어 지시와 결합해, 가림과 시점 변화가 있는 양팔 조작을 학습한다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11661761#page=1) · [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11661761#page=3)

## Core Idea and Contribution

- 토큰별 깊이 분포로 다른 시점의 이웃 특징을 모으고 텍스트 조건부 판독기를 적용하며, 깊이 교사 모델은 훈련 시에만 사용한다. [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11661761#page=3) · [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11661761#page=4) · [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11661761#page=5)
- RoboTwin 2.0의 도메인 무작위화 조건에서 가장 높은 비교 기준선보다 성공률이 23.0%p 높았고 별도의 실물 과제도 평가했다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11661761#page=5) · [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11661761#page=6) · [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11661761#page=7)

## Observation–State–Action Interface

여러 시점의 원시 RGB-D, 언어 지시와 로봇 관절 상태로 양팔 관절 궤적을 예측한다.

## Evaluation Scope and Claim Boundary

RoboTwin2.0과 실제 양팔 조작을 평가한다.

근거: [공식 paper/abstract](https://ieeexplore.ieee.org/document/11661761/) · [저자 project/code](https://peafowlvla.github.io/) · [공식 code](https://github.com/Qingyu-Fan/PEAfowl).

## 검색 태그 근거

그림 2에서 카메라의 원시 깊이는 정책의 깊이 인코더로, 교사가 보정한 깊이는 분포 예측기의 훈련 정답으로 들어간다. [그림 2](https://arxiv.org/pdf/2601.17885v2#page=3) · [교사 모델의 사용 범위](https://arxiv.org/pdf/2601.17885v2#page=9)

## Why This Paper Is Here — Researcher Interpretation

VLA-RL 성능 병목이 reward보다 공간 지각에 있을 때 비교할 표현 대안이다.

## Verification Boundary

깊이 교사 정답 생성 비용과 새로운 시점·물체에서의 일반화를 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
