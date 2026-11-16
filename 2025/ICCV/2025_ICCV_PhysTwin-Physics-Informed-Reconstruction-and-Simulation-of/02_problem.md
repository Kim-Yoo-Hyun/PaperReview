# PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

관측한 변형만 재현하는 모델은 새로운 물리적 상호작용을 예측하기 어렵다.

## Bottleneck and Changed Formulation

물리 simulation·geometry·Gaussian rendering을 결합해 상호작용 영상에서 역모델링한다.

## System and Robotics Loop

부분 interaction video → geometry/물리/외관 모델 → 새 action의 simulation.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

material/boundary 식별성, interaction 데이터 접근, planning 평가와 reconstruction의 분리.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

변형체 재구성·미래 예측·새 상호작용과 model-based robot planning 사례를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/ICCV2025/html/Jiang_PhysTwin_Physics-Informed_Reconstruction_and_Simulation_of_Deformable_Objects_from_Videos_ICCV_2025_paper.html) · [저자 project/code](https://jianghanxiao.github.io/phystwin-web/) · [공식 code](https://github.com/Jianghanxiao/PhysTwin). Exact objective, constraints, success definition은 본문 수동 확인 필요.
