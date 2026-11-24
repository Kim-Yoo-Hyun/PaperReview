# Problem - Context Graph-based Visual-Language Place Recognition

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> 2026-11-24 IEEE 게재본의 해당 절을 대조했다. [원문](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699)

## 문제와 가정

질의 영상과 같은 장소에서 촬영한 데이터베이스 영상을 찾는다. 조명과 시점 변화, 지나가는 차량·보행자가 영상의 외관을 바꾸므로 픽셀 수준 의미와 장면 내 영역 배치를 함께 사용한다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=1)

사전학습된 LSeg, 미리 정한 의미 범주, 참조 영상으로 구축한 시각·언어 어휘를 사용한다. [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=3)

## 로보틱스에서의 위치

검색 결과는 루프 폐쇄 후보로 사용할 수 있다. 본문은 알려진 위치에 가까운 참조 영상의 검색을 측정하며 지도 최적화 이후의 궤적은 평가 범위 밖이다. [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=6)
