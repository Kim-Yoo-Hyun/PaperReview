# PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. 아래에 인용한 원문 절·표의 평가 조건을 대조했다.
> Source audit: 2026-11-25 원문 방법·평가 대조.

## 평가 조건

여러 시점의 RGB-D 영상에서 변형 물체의 형상·동역학·외관을 각각 추정한다. 사람의 상호작용 영상이 물체 모델의 학습 입력이다. [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Jiang_PhysTwin_Physics-Informed_Reconstruction_and_Simulation_of_Deformable_Objects_from_Videos_ICCV_2025_paper.pdf#page=3)

표 1은 관측한 동작의 재시뮬레이션과 미래 프레임 예측을 구분하고 형상·추적·렌더링 지표를 비교한다. 표 2는 같은 물체에 학습 때와 다른 상호작용을 가한다. [PDF 7쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Jiang_PhysTwin_Physics-Informed_Reconstruction_and_Simulation_of_Deformable_Objects_from_Videos_ICCV_2025_paper.pdf#page=7)

로봇 응용에서는 맞춘 물체 모델을 이용해 로프가 목표 형상이 되도록 계획한다. 앞선 예측 표의 영상 지표와 이 조작 사례는 서로 다른 결과다. [PDF 8쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Jiang_PhysTwin_Physics-Informed_Reconstruction_and_Simulation_of_Deformable_Objects_from_Videos_ICCV_2025_paper.pdf#page=8)

## Proposed Evaluation — Researcher Interpretation

동일 관측 적합도의 여러 모델을 새 interaction으로 구분하고 planning regret을 비교한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.
