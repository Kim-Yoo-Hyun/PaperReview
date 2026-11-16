# AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Source audit: 2026-11-16: RSS metadata·arXiv v1 §III–V/Table II–IV·공식 코드로 OCR/설명 교정. 과거2026-09-03 PDF review 기록은 보존; 사용자 reading status 변경 없음.
> Canonical metadata: [01_overview.md](./01_overview.md).

## Method

1. AMASS 상체 동작과 torso 명령으로 trajectory optimization reference를 만들고 adaptation module을 사전학습한다.
2. PPO teacher를 학습한 뒤 privileged 정보 없이25-step proprioceptive history를 쓰는 student로 distill한다.
3. Teleoperation upper policy는 IK, autonomous upper policy는 DINOv2 기반 ACT를 사용한다. Lower15관절은 다리12+허리3이다.

[§III-B–E](https://arxiv.org/html/2505.03738v1#S3). Native language VLA와 동일한 입력/학습 구조라고 기록하지 않는다.

## Public Implementation

[OpenTeleVision/AMO](https://github.com/OpenTeleVision/AMO)에 MuJoCo 예시 `play_amo.py`, G1 model, adapter/normalizer/policy checkpoint가 있다. 추론 예시 공개이며 전체 teacher/student 학습 pipeline 공개까지 확인한 것은 아니다. 저장소에서 실행하지 않았다.
