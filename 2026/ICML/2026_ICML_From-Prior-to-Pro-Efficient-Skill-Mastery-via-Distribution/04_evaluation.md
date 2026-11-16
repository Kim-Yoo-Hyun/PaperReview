# From Prior to Pro: Efficient Skill Mastery via Distribution Contractive RL Finetuning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Evaluated Setting and Evidence

시각 입력의 simulation·실제 로봇 조작을 보고한다. 공개 Robomimic/flow 구현은 OpenVLA/LIBERO adapter가 아니며 그 호환성을 검증하지 않았다.

## Comparison and Reproducibility Boundary

ICML 공식 metadata와 arXiv v2의 지정 절/code를 확인했다. 현재 deterministic TD3·Q-filter 계획을 DICE-RL 전체 재현으로 부르지 않는다.

정확한 dataset 규모·train/test 분할·trial/seed·수치·모든 baseline/ablation은 이 노트에서 미기록이다. 논문 자체의 미보고라는 뜻이 아니다. 공개 code 링크는 실행 검증이 아니다.

근거: [지정 본문](https://arxiv.org/html/2603.10263v2) — v2 §4; model/rl/distill_residual_rl_img.py selected filter/loss paths. Code 검토 revision: `98d936e52523878f0172e606ea32403176497100`; 실행하지 않았다.

## Minimal Check — Researcher Proposal

연구자 제안: prior 교체와 학습 대상·critic 재초기화·replay를 명시하고 zero/frozen/gain/warm/fresh 및 선택적 모방을 동일 예산으로 비교한다.

실행하지 않았다. 재개는 해당 연구의 local Docker 환경·입출력 확인 뒤에 한정하며 큰 학습을 자동 실행하지 않는다.
