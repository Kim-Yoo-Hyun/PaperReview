# Evaluation - Learning Neural Network Policies with Guided Policy Search under Unknown Dynamics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> 2026-11-20 게재본의 표제면·방법·평가 절 대조. [게재 정보](https://proceedings.neurips.cc/paper_files/paper/2014/hash/c7c9344b5a3c0533e29fa69ce807cf08-Abstract.html) · [원문](https://proceedings.neurips.cc/paper_files/paper/2014/file/c7c9344b5a3c0533e29fa69ce807cf08-Paper.pdf)

- **Evaluation type:** `EMPIRICAL / SIMULATION`.

## 평가 설정과 근거

시뮬레이션에서 삽입, 수영 등 비선형 제어를 비교한다. 그림 1은 궤적 제어기, 그림 2는 신경망 정책에서의 표본 수와 과제별 거리 지표를 비교한다. 그림 2의 삽입 과제에서는 슬롯 위치가 정책에 직접 주어지지 않는다. pp. 6–8.

## 적용 범위

물리 시뮬레이션의 접촉·부분관측에서 얻은 결과다. 실제 로봇에서 영상으로 병뚜껑을 조이는 실험은 별개 논문에 속한다.
