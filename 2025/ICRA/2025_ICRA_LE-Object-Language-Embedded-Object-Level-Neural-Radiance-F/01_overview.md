# LE-Object: Language Embedded Object-Level Neural Radiance Fields for Open-Vocabulary Scene

> Evidence maturity: `FULL_TEXT_CHECKED`.

- Year/Venue: 2025 / ICRA
- Authors: Mengting Wang, Yunzhou Zhang, Xingshuo Wang, Zhiyao Zhang, Zhiteng Li
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: semantic
- Official paper: https://api.crossref.org/works/10.1109/icra55743.2025.11128304
- Full-text retrieval: https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304
- Code/Project: not identified
- Paper type: method
- Source audit: 2026-11-24 IEEE ICRA 게재본의 표제면·방법·평가를 대조했다.

## Why This Paper Is Here

LE-Object는 연속 RGB-D 영상에서 같은 물체의 마스크를 연결하고 물체별 신경 방사장을 학습해, 텍스트 질의에 맞는 영역과 개별 물체의 3차원 형상을 복원한다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=1) · [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=3)

## Main Claims and Actual Contribution

- 마스크에서 얻은 점군의 공간적 겹침과 시각 특징의 유사도를 함께 사용해 프레임 사이에서 물체를 대응시킨다. [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=3) · [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=4)
- 물체별 암시적 표현과 장면의 언어 특징을 학습하고, Replica에서 열린 어휘 분할과 물체 표면 복원의 정확도·완전성을 따로 평가했다. [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=4) · [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=5) · [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=6)

## Observation, State, and Output Interface

RGB-D·카메라 자세 → 프레임 간 물체 대응 → 물체별 형상과 언어 질의 결과. [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=3)

## Evaluation Scope

Replica 실내 장면 8개의 표 I에서 LE-Object의 평균 mIoU는 38.79, 별도 비교법 OpenObj는 24.64다. 표 II에서 물체 표면 완전성 비율은 예측 마스크 사용 시 84.59%, 정답 분할을 쓴 LE-Object⋆에서 96.75%다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=5) · [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=6)

## Explicit Limitations and Failure Boundary

추정 마스크로 복원한 결과와 정답 분할을 제공한 조건은 표 II에서 별도 행이다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=5)

게재본은 OpenObj를 표 I의 비교법으로 인용한다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=5) · [OpenObj의 별도 서지](https://arxiv.org/abs/2406.08009)
