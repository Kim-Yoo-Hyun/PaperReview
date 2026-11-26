# Method — LHM-Humanoid: Long-Horizon Human Motion Control for Continuous Object Transport in Cluttered Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §3.1–3.3, §4.2–4.3, Tables 1 and 3; ACCV 2026 programme 검토. [방법·평가 원문](https://arxiv.org/html/2508.16943)

## 관측과 출력

시각언어 버전은 현재 배치 목표를 지정하는 언어와 1인칭 RGB에서 모의 휴머노이드의 전신 행동을 출력한다. 연속 지시는 외부에서 주어지며 공개 본문의 해당 절은 모터 전류나 직접 토크 차원을 명시하지 않는다.

## 학습·실행 방법

첫 물체를 놓고 물러나는 교사와 그 상태에서 다음 과업을 시작하는 교사를 RL로 학습해 하나의 정책으로 증류한다. 이 정책의 스텝별 행동을 다시 1인칭 RGB·언어 학생에게 DAgger로 가르친다.
