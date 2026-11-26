# Method — Diagnose, Correct, and Learn from Manipulation Failures via Visual Symbols

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 CVF 게재본 PDF 2–8쪽의 데이터·진단·표 4와 배포 자료 대조. Full-text scope의 수치·조건만 기록했다.

## 관측과 출력

카메라 궤적과 작업 지시로부터 실패 프레임과 교정 단서를 내며, 조작 행동은 파인튜닝한 π0.5가 실행한다.

## 학습·실행 방법

실제 로봇 궤적에 실패 구간과 화살표 등의 시각적 교정 지시를 붙인다. ViFailback-8B가 실패 진단과 교정 표식을 생성하고 이를 배포 정책의 입력으로 사용한다.

- 관련 연구에서 AHA를 실패 진단 기반 모델로 구분한다. [pr-0071 · 원문](https://openaccess.thecvf.com/content/CVPR2026/papers/Zeng_Diagnose_Correct_and_Learn_from_Manipulation_Failures_via_Visual_Symbols_CVPR_2026_paper.pdf#page=2)
