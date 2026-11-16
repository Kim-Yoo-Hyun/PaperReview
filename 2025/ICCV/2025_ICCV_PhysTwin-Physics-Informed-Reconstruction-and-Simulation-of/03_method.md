# PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

물리 simulation·geometry·Gaussian rendering을 결합해 상호작용 영상에서 역모델링한다.

## Observation–State–Action Interface

부분 interaction video → geometry/물리/외관 모델 → 새 action의 simulation.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: material/boundary 식별성, interaction 데이터 접근, planning 평가와 reconstruction의 분리.

Source가 명시한 evaluation 범위: 변형체 재구성·미래 예측·새 상호작용과 model-based robot planning 사례를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 관측 적합도의 여러 모델을 새 interaction으로 구분하고 planning regret을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/ICCV2025/html/Jiang_PhysTwin_Physics-Informed_Reconstruction_and_Simulation_of_Deformable_Objects_from_Videos_ICCV_2025_paper.html) · [저자 project/code](https://jianghanxiao.github.io/phystwin-web/) · [공식 code](https://github.com/Jianghanxiao/PhysTwin). 수식·세부 구현·코드 실행은 미검증이다.
