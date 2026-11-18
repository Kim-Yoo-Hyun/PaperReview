# UA-Pose: Uncertainty-Aware 6D Object Pose Estimation and Online Object Completion with Partial References

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

부분 3D 모델의 관측·미관측 영역 불확실성을 활용해 pose 신뢰도와 온라인 completion sampling을 다룬다.

## Observation–State–Action Interface

Known-pose RGB-D 소수 관측 또는 한 장의 reference 이미지에서 출발해 pose와 보완된 물체 표현을 출력한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Image-to-3D 전제·미관측 uncertainty의 calibration·실세계 control 평가.

Source가 명시한 evaluation 범위: YCB-Video·YCBInEOAT·HO3D의 로봇/손 조작 RGB-D 시퀀스를 평가한다. 제어 정책 성공의 실증과 구별한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

관측 coverage를 맞추고 completion 유무의 pose 오차와 downstream 배치 오류를 분리한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2025/html/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.html) · [저자 project/code](https://minfenli.github.io/UA-Pose/) · [공식 저장소(구현 공개 미확인)](https://github.com/minfenli/UA-Pose). 수식·세부 구현·코드 실행은 미검증이다.
