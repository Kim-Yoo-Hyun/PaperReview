# Problem - LE-Object: Language Embedded Object-Level Neural Radiance Fields for Open-Vocabulary Scene

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> 2026-11-24 IEEE 게재본의 해당 절을 대조했다. [원문](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304)

## 문제와 가정

연속 RGB-D 영상에서 화면의 일부만 차지하는 물체를 여러 프레임에 걸쳐 동일 개체로 식별해야 한다. 인접 물체가 합쳐지거나 한 물체가 갈라지면 언어 질의가 맞더라도 복원할 표면에 다른 물체가 들어간다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=1)

입력은 장면의 RGB-D 관측과 카메라 자세다. 각 프레임에서 물체 마스크를 구하고 관측 좌표를 공통 3D 공간에 놓을 수 있어야 한다. [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=3)

## 로보틱스에서의 위치

이 논문에서 측정한 출력은 의미 영역과 물체 표면이다. 계획기가 쓸 수 있는 지도 표현의 품질은 Replica의 분할·복원 지표에서 확인할 수 있다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=5)
