# Method - Learning Neural Network Policies with Guided Policy Search under Unknown Dynamics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> 2026-11-20 게재본의 표제면·방법·평가 절 대조. [게재 정보](https://proceedings.neurips.cc/paper_files/paper/2014/hash/c7c9344b5a3c0533e29fa69ce807cf08-Abstract.html) · [원문](https://proceedings.neurips.cc/paper_files/paper/2014/file/c7c9344b5a3c0533e29fa69ce807cf08-Paper.pdf)

## 입력과 계산

수집한 궤적 주변에서 시변 선형 동역학을 반복 적합한다. 이를 이용해 국소 선형 가우시안 제어기의 궤적 분포를 최적화하고, guided policy search로 여러 초기 조건을 처리하는 신경망 정책을 훈련한다. 훈련 중의 상태 정보와 실행 시 정책에 주어지는 관측을 구분한다. pp. 2–5.

## 적용 조건

물리 시뮬레이션의 접촉·부분관측에서 얻은 결과다. 실제 로봇에서 영상으로 병뚜껑을 조이는 실험은 별개 논문에 속한다.
