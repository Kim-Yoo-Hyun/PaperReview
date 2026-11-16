# Force Policy: Learning Hybrid Force-Position Control Policy under Interaction Frame for Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

시연에서 interaction frame을 복원해 전역 시각 정책과 국소 hybrid force-position 제어를 구성한다.

## Observation–State–Action Interface

vision으로 접근하고 접촉 시 힘 피드백·interaction frame으로 제어한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: frame label 생성과 수동 조정, 접촉 전환 조건, 정책·controller 주기.

Source가 명시한 evaluation 범위: 실제 contact-rich 조작과 새로운 형상·물성 객체를 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

관측과 controller를 맞춘 후 접촉 검출, frame 추정, force regulation의 실패를 각각 계측한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p128.html) · [저자 project/code](https://force-policy.github.io/) · [공식 code](https://github.com/force-policy/ForcePolicy). 수식·세부 구현·코드 실행은 미검증이다.
