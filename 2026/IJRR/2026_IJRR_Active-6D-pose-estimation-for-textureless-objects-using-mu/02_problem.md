# Active 6D pose estimation for textureless objects using multi-view RGB frames

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

무텍스처·대칭·가림 때문에 단일 RGB 관측만으로 물체 자세를 구별하기 어렵다.

## Bottleneck and Changed Formulation

Translation을 먼저 추정하고 canonical-scale template으로 orientation을 추정한 뒤 pose uncertainty를 줄일 다음 view를 선택한다.

## System and Robotics Loop

다중 RGB·알려진 물체 geometry와 camera 관측에서 pose 및 다음 카메라 시점을 출력한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

CAD·calibration 요구·transparent dataset 조건·실제 이동 비용.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

ROBI·TOD·T-ROBI에서 같은 view의 추정 성능과 적은 view로 얻는 정확도를 비교한다. VLA 행동 효과 평가로 확장하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://journals.sagepub.com/doi/10.1177/02783649251411922) · [저자 project/code](https://trailab.github.io/ActiveODPE/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
