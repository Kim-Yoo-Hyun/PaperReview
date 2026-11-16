# LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

배치·camera·robot 초기 상태·언어·조명·배경·sensor noise를 통제한 점진 평가를 구성한다.

## Observation–State–Action Interface

Perturbed 환경/지시 → 기존 VLA → task success와 조건별 분석.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 난도 선정에 쓰인 model, perturbation validity, test contamination.

Source가 명시한 evaluation 범위: 다수 VLA의 simulation robustness를 비교한다. 수치·정확한 난도 split은 본문 확인 필요.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 checkpoint로 원본/변형 task를 paired 비교하고 reachability와 성공 판정을 감사한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.html) · [저자 project/code](https://github.com/sylvestf/LIBERO-plus). 수식·세부 구현·코드 실행은 미검증이다.
