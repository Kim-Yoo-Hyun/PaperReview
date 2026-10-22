# Tac2Real: Reliable and GPU Visuotactile Simulation for Online Reinforcement Learning and Zero-Shot Real-World Deployment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

PNCG-IPC 기반 tactile simulation, multi-GPU 병렬화 및 TacAlign sim-to-real alignment를 결합한다.

## Observation–State–Action Interface

Contact dynamics → tactile marker displacement/visual signal → RL policy → insertion action.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Tactile sensor calibration, contact parameter 분포, marker fidelity와 code 공개 범위.

Source가 명시한 evaluation 범위: 공식 abstract/project는 contact-rich peg insertion의 zero-shot real-world transfer 평가를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

Vision-only, visuotactile without alignment, TacAlign 설정을 같은 insertion 조건으로 비교하고 success·peak contact·latency를 측정한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2603.28475) · [저자 project/code](https://ningyurichard.github.io/tac2real-project-page/). 수식·세부 구현·코드 실행은 미검증이다.
