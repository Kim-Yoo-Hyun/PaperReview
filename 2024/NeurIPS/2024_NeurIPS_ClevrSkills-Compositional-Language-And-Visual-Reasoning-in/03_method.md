# ClevrSkills: Compositional Language And Visual Reasoning in Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

ManiSkill2 기반 환경과 demonstration dataset, 단계별 조합 과제로 언어·시각 지시 이행을 비교한다.

## Observation–State–Action Interface

언어·시각 task prompt와 로봇 관측 → 조작 정책 → simulator predicate 평가. Dataset annotation과 정책에 허용되는 입력을 구분해야 한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: task 생성의 정답 정보와 자동 입력, 부분집합 허용 범위, release/contact predicate, 조합 split의 학습 support.

Source가 명시한 evaluation 범위: 기초 조작에서 복합 과제로 이어지는 세 수준의 curriculum에서 VLM 기반 baseline을 평가한다. 이 등록에서는 정확한 trial 수·성공률을 새로 확정하지 않는다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

고정 task/predicate와 정책 입력을 먼저 대조하고, 호환 로컬 Docker에서 기본 조작을 확인한 뒤 단순 지시 대조를 설계한다. 이 등록은 실행 승인·재현 결과가 아니다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2024/hash/439539557e9ba0d04055773ff1f3241c-Abstract-Datasets_and_Benchmarks_Track.html) · [저자 project/code](https://github.com/Qualcomm-AI-research/ClevrSkills). 수식·세부 구현·코드 실행은 미검증이다.
