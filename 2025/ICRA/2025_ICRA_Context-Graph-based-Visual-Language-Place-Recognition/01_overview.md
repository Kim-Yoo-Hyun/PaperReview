# Context Graph-based Visual-Language Place Recognition

> Evidence maturity: `FULL_TEXT_CHECKED`.

- Year/Venue: 2025 / ICRA
- Authors: Soojin Woo, Seong-Woo Kim
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Graph Reasoning
- Official paper: https://api.crossref.org/works/10.1109/icra55743.2025.11127699
- Full-text retrieval: https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699
- Code/Project: https://github.com/woo-soojin/context-based-vlpr
- Paper type: method
- Source audit: 2026-11-24 IEEE ICRA 게재본의 표제면·방법·평가를 대조했다.

## Why This Paper Is Here

시점이나 장면 외관이 달라졌을 때 같은 장소를 검색하기 위해 영상의 시각·언어 특징 히스토그램과 의미 영역 사이의 관계 그래프를 결합한다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=1) · [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=4)

## Main Claims and Actual Contribution

- LSeg의 픽셀 임베딩에서 동적 물체에 해당하는 영역을 걸러내고, 남은 영역의 특징 분포와 영역 간 문맥을 각각 벡터로 표현한다. [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=3) · [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=4) · [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=5)
- Pittsburgh와 KITTI의 실제 거리 영상에서 질의와 위치가 가까운 참조 영상을 되찾는 비율을 측정하고 NetVLAD와 후보 수에 따른 차이를 비교했다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=5) · [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=6)

## Observation, State, and Output Interface

질의와 참조 RGB 영상 → LSeg 특징과 문맥 그래프 → 참조 영상의 검색 순위. [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=4)

## Evaluation Scope

표 II의 KITTI 00에서 제안법과 NetVLAD의 Recall@1은 각각 0.14와 0.18, Recall@20은 0.85와 0.51이다. 정답 여부는 상위 N개 후보에 실제 위치 25 m 이내의 영상이 있는지로 정한다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=5) · [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=6)

## Explicit Limitations and Failure Boundary

두 도심 데이터셋에서 후보 수에 따라 방법 간 순위가 달라진다. [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=6)

## 판본과 코드

2024년 저자판의 표제는 *Context-Based Visual-Language Place Recognition*이다. 저자 저장소는 ICRA 2025 게재를 명시하고, 게재본 그림 4와 III-C절은 문맥 그래프의 구성과 결합을 설명한다. [저자판](https://arxiv.org/abs/2410.19341) · [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=4) · [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=5)

저자 저장소에 픽셀 군집 중심, 문맥 그래프와 그래프 임베딩을 만드는 함수가 공개되어 있다. [구현 파일](https://raw.githubusercontent.com/woo-soojin/context-based-vlpr/3556108a08c7c637256e4bb7337d51915a5dd5fa/utils/context_graph.py) · [저자 저장소 안내](https://raw.githubusercontent.com/woo-soojin/context-based-vlpr/3556108a08c7c637256e4bb7337d51915a5dd5fa/README.md)
