# Accelerating Residual Reinforcement Learning With Uncertainty Estimation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Evaluated Setting and Evidence

Robosuite·D4RL 비교와 sim-to-real 적용을 보고한다. 여기서는 combined-action critic 경로를 확인했으며 수치·seed·현실 성공률을 재현하지 않았다.

## Comparison and Reproducibility Boundary

IEEE 직접 페이지는 접근 제약이 있어 publisher-deposited Crossref와 저자 accepted 표기로 RA-L 11(1), 2026을 확인했다. 2025 DOI/채택일을 issue 연도와 혼동하지 않는다.

정확한 dataset 규모·train/test 분할·trial/seed·수치·모든 baseline/ablation은 이 노트에서 미기록이다. 논문 자체의 미보고라는 뜻이 아니다. 공개 code 링크는 실행 검증이 아니다.

근거: [지정 본문](https://arxiv.org/html/2506.17564v2) — v2 IV-B / V-D; assymetric_sac.py critic_loss_fn/actor complete-action path. Code 검토 revision: `8125f33dcf490d4cf93d57a27d3e1963a47f52ea`; 실행하지 않았다.

## Minimal Check — Researcher Proposal

연구자 제안: 새 critic·공통 replay를 모든 재사용 대조군에 적용하고 actor 보존/재초기화와 uncertainty/gain 대안을 구분한다.

실행하지 않았다. 재개는 해당 연구의 local Docker 환경·입출력 확인 뒤에 한정하며 큰 학습을 자동 실행하지 않는다.
