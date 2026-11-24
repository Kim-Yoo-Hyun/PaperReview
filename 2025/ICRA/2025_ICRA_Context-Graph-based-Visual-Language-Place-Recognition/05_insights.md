# Insights — Context Graph-based Visual-Language Place Recognition

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> 2026-11-24 IEEE 게재본의 해당 절을 대조했다. [원문](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699)

## Paper-supported conclusion

KITTI 00에서 제안법은 NetVLAD보다 상위 5·10·20개 후보의 재현율이 높고 첫 후보의 재현율은 낮다. Pittsburgh의 상위 20개에서는 두 방법 모두 1.00이다. [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=6)

## Researcher interpretation

재검증할 후보가 여러 개 허용되는 위치 추정기와 한 후보를 즉시 채택하는 위치 추정기는 이 결과에서 얻는 이점이 다를 수 있다. [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=6)

## Falsifiable research question

같은 LSeg 히스토그램·후보 예산을 고정하고 그래프 특징만 추가했을 때 Recall@1과 Recall@20이 어떻게 달라지는가? 게재본의 표 II는 완성 모델과 NetVLAD의 비교이므로 이 효과는 별도 비교가 필요하다. [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=4)
