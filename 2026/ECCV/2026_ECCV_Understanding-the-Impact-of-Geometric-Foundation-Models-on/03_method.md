# Understanding the Impact of Geometric Foundation Models on Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

GR00T-N1.5와 VGGT를 고정한 비교에서 geometry를 읽어내는 probe와 세 가지 geometry 결합 구조를 분석한다.

## Observation–State–Action Interface

영상/언어 기반 VLA에 geometric foundation model의 정보를 결합한다. 정책 입력·학습 방식·카메라 수의 차이를 비교 변수로 구별한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Probe 용량 차이·architecture별 파라미터/학습량·재구성 품질의 측정 단위·task/data split·real-robot 범위.

Source가 명시한 evaluation 범위: 공식 초록은 특정 VLA/GFM 조합의 표현 probing, 결합 구조 세 가지, 데이터·카메라 수·재구성 품질의 영향을 비교한다. 모든 VLA에 대한 보편 결론이나 동일 상태 오류 개입 실험을 뜻하지 않는다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 checkpoint·RGB·K를 고정하고 geometry 입력 오차만 바꿔 원래 오차–성공 관계와 비교한다. Action/policy 변경은 별도 비교다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://link.springer.com/chapter/10.1007/978-3-032-37271-0_2). 수식·세부 구현·코드 실행은 미검증이다.
