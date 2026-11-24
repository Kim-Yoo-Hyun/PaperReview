# Method - LE-Object: Language Embedded Object-Level Neural Radiance Fields for Open-Vocabulary Scene

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> 2026-11-24 IEEE 게재본의 해당 절을 대조했다. [원문](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304)

## 입력과 물체 대응

검출·분할 모델이 RGB 영상의 후보 마스크를 제공한다. 깊이로 마스크를 3D 점군으로 되투영하고 기존 물체 가설과 대응시키거나 새 가설을 초기화한다. [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=3)

관측 점군의 공간 겹침과 영상 특징의 코사인 유사도를 결합해 대응을 판정한다. 마스크 영역과 배경을 분리해 OpenCLIP 영상 특징을 추출한 뒤 픽셀에 정렬한다. [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=4)

## 표현과 최적화

색·깊이 관측과 픽셀의 언어 특징을 이용해 장면의 열린 어휘 표현을 학습한다. [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=4)

물체마다 별도 방사장과 키프레임 저장소를 둔다. 마스크 내부 픽셀의 색·깊이·부호 거리 손실로 표면을 학습하며, 구현에서는 5프레임마다 마스크 내부 픽셀의 5%를 보관한다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=5)
