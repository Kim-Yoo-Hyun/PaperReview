# Evaluation - Context Graph-based Visual-Language Place Recognition

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> 2026-11-24 IEEE 게재본의 해당 절을 대조했다. [원문](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699)

- **Evaluation type:** `EMPIRICAL / BENCHMARK OR DATASET`.

## Evaluation in One Sentence

표 II의 KITTI 00에서 제안법과 NetVLAD의 Recall@1은 각각 0.14와 0.18, Recall@20은 0.85와 0.51이다. 정답 여부는 상위 N개 후보에 실제 위치 25 m 이내의 영상이 있는지로 정한다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=5) · [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=6)

## Embodiment / Environment

Pittsburgh 거리 영상과 주행 차량에서 기록한 KITTI 영상으로 오프라인 장소 검색을 평가했다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=5)

## Dataset / Benchmark Role

Pitts30k-val은 일부 표본을 무작위 추출해 사용했다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=5)

KITTI 시퀀스 00의 영상 4,541장을 질의 2,271장과 데이터베이스 2,270장으로 나눴다. [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=6)

## Metrics and Success Definition

상위 N개 중 질의의 실제 위치에서 25 m 이내인 영상이 하나 이상 있는 질의의 비율을 구한다. N은 1, 5, 10, 20이다. [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=6)

## Baselines and Fairness

표 II에서 제안법의 Pitts30k-val Recall@1은 0.32, NetVLAD는 0.54다. KITTI 00에서는 첫 후보의 정확도와 상위 20개까지 고려한 결과에서 순위가 달라졌다. [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=6)

## Generalization and Failure Cases

문맥 그래프는 영상 평면에서 의미 영역 중심 사이의 배치를 표현한다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=5)

검색 후보 수와 장면에 따라 기준선 대비 결과가 달라진다. 실시간 주행 중 잘못 닫힌 루프의 비용은 이 표에서 측정하지 않는다. [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=6)
