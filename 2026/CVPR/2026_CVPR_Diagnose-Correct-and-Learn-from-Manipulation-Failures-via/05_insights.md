# Insights — Diagnose, Correct, and Learn from Manipulation Failures via Visual Symbols

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 CVF 게재본 PDF 2–8쪽의 데이터·진단·표 4와 배포 자료 대조. Full-text scope의 수치·조건만 기록했다.

## Paper-supported conclusion

실제 로봇 궤적에 실패 구간과 화살표 등의 시각적 교정 지시를 붙인다. ViFailback-8B가 실패 진단과 교정 표식을 생성하고 이를 배포 정책의 입력으로 사용한다. [원문 및 평가 절](https://openaccess.thecvf.com/content/CVPR2026/papers/Zeng_Diagnose_Correct_and_Learn_from_Manipulation_Failures_via_Visual_Symbols_CVPR_2026_paper.pdf#page=8)

## Researcher interpretation

실제 실패 데이터로 진단 정확도와 이후 제어 복구를 구분해서 비교할 수 있다.

- 관련 연구에서 AHA를 실패 진단 기반 모델로 구분한다. [pr-0071 · 원문](https://openaccess.thecvf.com/content/CVPR2026/papers/Zeng_Diagnose_Correct_and_Learn_from_Manipulation_Failures_via_Visual_Symbols_CVPR_2026_paper.pdf#page=2)

## 최소 비교 실험

동일 실패 상태에서 재시도와 텍스트 교정·시각 교정을 비교하고 제어 복구 성공을 측정한다.
