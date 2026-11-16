# Autonomous Improvement of Instruction Following Skills via Foundation Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

VLM으로 의미 있는 경험의 수집·평가를 돕고 언어 조건 이미지 목표 생성과 goal-reaching 정책을 분리하여 자율 데이터로 학습한다.

## Observation–State–Action Interface

언어 → image subgoal → goal-conditioned robot action. 학습 데이터 수집/평가와 배포 정책의 역할을 분리한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 수집 scene과 평가 scene의 분리, 데이터 release의 실제 접근성, 의미 이해와 운동 능력 개선의 기여, 서로 다른 정책 정보량.

Source가 명시한 evaluation 범위: 공식 abstract는 새로운 실세계 환경의 정책 개선과 5개 tabletop 환경에서 수집한 25K trajectory 데이터 공개를 설명한다. Project는 9개 평가 scene을 설명하므로 두 숫자의 분모를 합치지 않는다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 원 경험·성공 판정·학습 예산을 고정하고 언어와 image-goal 감독의 추가 정보 차이를 먼저 감사한 뒤 지시 성공과 goal-reaching 성공을 분리 평가한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v270/zhou25b.html) · [저자 project/code](https://soar-autonomous-improvement.github.io/) · [공식 code](https://github.com/soar-autonomous-improvement/code-release). 수식·세부 구현·코드 실행은 미검증이다.
