# Equivariant diffusion policy for sample-efficient robotic manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. 아래에 인용한 원문 절·표의 평가 조건을 대조했다.
> Source audit: 2026-11-25 원문 방법·평가 대조.

## 평가 조건

저널 확장판은 점군을 받는 등변 점 트랜스포머에 병진 T(3)과 회전 SO(2) 대칭을 적용한다. 저자가 이전 CoRL판과 공통으로 연결한 구현 경로의 범위는 배치 원장에 기록했다. [Equivariant point transformer and translation symmetry](https://sage.cnpereading.com/doi/10.1177/02783649261424445#:~:text=Equivariant%20point%20transformer%20and%20translation%20symmetry)

그림 8과 9에 여섯 실제 과제와 Franka Emika·세 대의 RealSense D455 구성이 나온다. 저자들은 실물에서 관측과 시연 행동을 5 Hz로 기록하고, 비교 정책에도 같은 입력 표현을 준 조건을 제시했다. [Real-robot experiment](https://sage.cnpereading.com/doi/10.1177/02783649261424445#:~:text=Real-robot%20experiment)

카메라 관측과 로봇 작업공간이 이론상 대칭을 완전히 만족하지 않는다는 한계를 저자가 논의한다. [Symmetry breakings](https://sage.cnpereading.com/doi/10.1177/02783649261424445#:~:text=Symmetry%20breakings)

## Proposed Evaluation — Researcher Interpretation

같은 입력·시연·action 좌표계에서 augmentation과 equivariant denoising을 비교한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.
