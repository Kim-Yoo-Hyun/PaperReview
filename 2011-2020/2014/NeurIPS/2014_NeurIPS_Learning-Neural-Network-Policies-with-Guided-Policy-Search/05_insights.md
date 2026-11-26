# Insights - Learning Neural Network Policies with Guided Policy Search under Unknown Dynamics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> 2026-11-20 게재본의 표제면·방법·평가 절 대조. [게재 정보](https://proceedings.neurips.cc/paper_files/paper/2014/hash/c7c9344b5a3c0533e29fa69ce807cf08-Abstract.html) · [원문](https://proceedings.neurips.cc/paper_files/paper/2014/file/c7c9344b5a3c0533e29fa69ce807cf08-Paper.pdf)

## Paper-supported conclusion

전역 동역학 모델이 없는 연속 제어에서, 궤적 주변의 시변 선형 모델로 국소 제어기를 학습하고 그 행동을 신경망 정책에 전달한다. 물리 시뮬레이션의 접촉·부분관측에서 얻은 결과다. 실제 로봇에서 영상으로 병뚜껑을 조이는 실험은 별개 논문에 속한다.

## Researcher interpretation

삽입에서 초기 슬롯 위치 분포를 고정하고 훈련 시 동역학 적합을 위한 표본 수만 바꾸면, 표본 효율과 정책 일반화를 분리해 비교할 수 있다.
