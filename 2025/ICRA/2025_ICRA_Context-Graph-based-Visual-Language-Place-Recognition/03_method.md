# Method - Context Graph-based Visual-Language Place Recognition

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> 2026-11-24 IEEE 게재본의 해당 절을 대조했다. [원문](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699)

## 영상 설명자

LSeg가 제공하는 픽셀별 영상·언어 특징으로 미리 정한 범주를 구분하고 동적 물체에 해당하는 픽셀을 거른다. [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=3)

남은 픽셀의 임베딩을 시각·언어 어휘로 양자화해 영상 단위의 히스토그램을 만든다. [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=4)

## 문맥 그래프와 검색

같은 의미 라벨에 속한 픽셀 군집의 중심을 노드로 삼고 중심 사이의 영상 좌표 거리를 그래프에 반영한다. graph2vec으로 그래프를 고정 길이 벡터로 표현한다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=5)

히스토그램과 문맥 그래프 벡터를 결합해 질의·참조 영상의 설명자를 구성한다. [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=4)

설명자 사이 거리가 가까운 순서로 참조 영상을 검색한다. 평가는 상위 후보 중 위치 기준을 만족하는 영상이 있는지를 측정한다. [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=6)
