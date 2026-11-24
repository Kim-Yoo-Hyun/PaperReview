# Insights — LE-Object: Language Embedded Object-Level Neural Radiance Fields for Open-Vocabulary Scene

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> 2026-11-24 IEEE 게재본의 해당 절을 대조했다. [원문](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304)

## Paper-supported conclusion

표 I에서 두 특징을 쓰는 LE-Object는 8개 장면의 평균 분할 점수가 비교법보다 높았다. 표 II에서는 추정 마스크와 정답 마스크를 쓴 행의 기하 성능 차이가 컸다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=5)

저자들은 분할 정밀도에 따라 물체 복원 오차가 달라진다고 보고한다. 표 III의 특징 제거는 두 실내 장면에서 수행됐다. [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=6)

## Researcher interpretation

로봇 조작에 재사용하려면 언어로 맞는 물체를 고르는 능력과 접촉 부근의 표면을 정확히 찾는 능력을 따로 검사하는 편이 타당하다. 산출된 지도에서 실제 파지 성공률을 추론할 근거는 아직 없다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=5)

## Falsifiable research question

같은 RGB-D 영상과 카메라 자세에서 마스크만 추정값과 정답으로 교체하면, 작은 물체의 표면 완전성과 손잡이 위치 오차가 함께 달라지는가? 첫 항목은 표 II와 대조할 수 있고 두 번째는 새로 측정해야 한다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=5)
