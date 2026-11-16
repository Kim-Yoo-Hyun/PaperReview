# Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Source audit: 2026-11-16: RSS metadata·공식 project/code 및 arXiv v1 §III–IV, Appendix IX–X의 지정 내용 확인. RSS 최종본문 전체 대조·사용자 정독·실험을 의미하지 않는다.
> Canonical metadata: [01_overview.md](./01_overview.md).

## Evaluation Type and Scope

EMPIRICAL / REAL-ROBOT OR HARDWARE. [§IV-B](https://arxiv.org/html/2603.12263v1#S4): G1 실물8과제, 과제당 시연80개, 모델·과제당 평가10회. 시연과 평가 rollout을 구분한다.

## Metrics and Success Definition

실패한 subtask 뒤 사람이 도와 이후 skill을 평가할 수 있다. 따라서 subtask 성공을 무개입 full-task 성공으로 합산하면 안 된다.

## Baselines and Fairness

π₀.₅·GR00T N1.6·InternVLA-M1·H-RDT·EgoVLA·DP·ACT 비교. 동일 finetuning 자료라도 pretraining·decoder·RTC·계산량까지 같은 것은 아니다.

## Ablations and Sensitivity

§IV-C ablation은 제한된 실물과제다. Appendix X-A의 GR00T RTC 비교는 전체 성공7/10→6/10으로, 부드러운 실행이 항상 성공 증가를 뜻하지 않는다.

## Generalization and Failure Cases

소수 반복과 특정 hardware의 결과를 unseen robot 일반화로 확장하지 않는다. 독립 재현·전체 평가 표 대조는 미실행이다.

## Dataset / Benchmark Role

[현재 코드](https://github.com/physical-superintelligence-lab/Psi0)의 실물9/시뮬레이션6 task 공개와 논문 v1의 실물8과제를 구분한다. 본문의 EgoDex **900M frames** 표기는 [EgoDex 공식 자료](https://github.com/apple-aiml-research/ml-egodex)의 약90M과 불일치한다. 데이터 크기 기록은 원 데이터 출처를 우선하며 단순히900M을 재인용하지 않는다.

## Statistics, Efficiency, and Reproducibility

[공식 코드·checkpoint](https://github.com/physical-superintelligence-lab/Psi0) 공개 확인만 수행했다. 런타임·자산·속도·성능 검증은 하지 않았다.
