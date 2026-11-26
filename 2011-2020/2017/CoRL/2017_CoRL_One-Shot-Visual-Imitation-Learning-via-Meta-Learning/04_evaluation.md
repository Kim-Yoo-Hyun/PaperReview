# Evaluation - One-Shot Visual Imitation Learning via Meta-Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> 2026-11-20 게재본의 표제면·방법·평가 절 대조. [게재 정보](https://proceedings.mlr.press/v78/finn17a.html) · [원문](https://proceedings.mlr.press/v78/finn17a/finn17a.pdf)

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT AND SIMULATION`.

## 평가 설정과 근거

시뮬레이션에서는 목표에 손을 뻗거나 물체를 미는 과제를, 실제 PR2에서는 이미 쥔 물체를 시연으로 지정된 용기에 두는 과제를 평가한다. 시연을 문맥으로 입력하는 순환 방식과 목표 영상 방식 등이 비교군이다. §6, 그림 3–5.

## 적용 범위

훈련과 테스트는 논문에서 정의한 과제 분포를 공유한다. 임의의 새 기술에 대한 한 번의 시연 성공을 보장하지 않는다.
