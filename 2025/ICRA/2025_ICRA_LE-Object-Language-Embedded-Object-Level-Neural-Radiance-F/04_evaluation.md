# Evaluation - LE-Object: Language Embedded Object-Level Neural Radiance Fields for Open-Vocabulary Scene

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> 2026-11-24 IEEE 게재본의 해당 절을 대조했다. [원문](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304)

- **Evaluation type:** `EMPIRICAL / BENCHMARK OR DATASET`.

## Evaluation in One Sentence

Replica 실내 장면 8개의 표 I에서 LE-Object의 평균 mIoU는 38.79, 별도 비교법 OpenObj는 24.64다. 표 II에서 물체 표면 완전성 비율은 예측 마스크 사용 시 84.59%, 정답 분할을 쓴 LE-Object⋆에서 96.75%다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=5) · [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=6)

## Embodiment / Environment

Replica의 실내 장면 8개에서 다중 뷰 관측을 사용한다. 실험은 의미 분할과 물체 표면 복원을 측정한다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=5)

## Dataset / Benchmark Role

정답 의미 라벨을 텍스트 질의로 사용한다. 표 I은 장면별 분할 결과를, 표 II는 같은 8개 장면에서 평균한 기하 결과를 제시한다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=5)

## Metrics and Success Definition

분할은 mIoU와 mAcc, 물체 복원은 정확도 거리(cm), 완전성 거리(cm), 5 cm 이내 완전성 비율로 측정한다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=5)

## Baselines and Fairness

의미 분할에는 LSeg, LERF, 3DOVS와 별도 연구인 OpenObj를 비교한다. 표 II의 기하 비교에는 TSDF-Fusion, iMAP, NICE-SLAM, vMAP이 포함된다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=5)

## Ablations and Sensitivity

표 III은 room0·office0에서 SAM과 MobileSAM을 바꾸고 시각 특징과 공간 특징을 각각 제거한 결과다. 마스크의 분할 정확도가 낮으면 물체 재구성도 영향을 받는다. [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=6)
