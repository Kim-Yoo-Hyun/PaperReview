# Problem - Learning Neural Network Policies with Guided Policy Search under Unknown Dynamics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> 2026-11-20 게재본의 표제면·방법·평가 절 대조. [게재 정보](https://proceedings.neurips.cc/paper_files/paper/2014/hash/c7c9344b5a3c0533e29fa69ce807cf08-Abstract.html) · [원문](https://proceedings.neurips.cc/paper_files/paper/2014/file/c7c9344b5a3c0533e29fa69ce807cf08-Paper.pdf)

## 문제와 가정

접촉으로 동역학이 불연속인 계에서, 표본을 많이 쓰는 직접 정책 탐색과 전역 동역학 추정 사이의 어려움을 다룬다. 초록·§1.

## 정책과 제어에서의 위치

전역 동역학 모델이 없는 연속 제어에서, 궤적 주변의 시변 선형 모델로 국소 제어기를 학습하고 그 행동을 신경망 정책에 전달한다.
