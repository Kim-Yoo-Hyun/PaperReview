# Policy Decorator: Model-Agnostic Online Refinement for Large Policy Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Evaluated Setting and Evidence

ManiSkill·Adroit의 8개 task, Behavior Transformer·Diffusion Policy에 적용한다. 보고된 성능 향상은 해당 설정이며 같은 residual의 base 교체 전이를 뜻하지 않는다.

## Comparison and Reproducibility Boundary

Final paper의 지정 절만 검토했고 전체 36쪽 정독은 아니다. 공식 code 링크/README 확인과 실행 검증을 구분한다.

정확한 dataset 규모·train/test 분할·trial/seed·수치·모든 baseline/ablation은 이 노트에서 미기록이다. 논문 자체의 미보고라는 뜻이 아니다. 공개 code 링크는 실행 검증이 아니다.

근거: [지정 본문](https://proceedings.iclr.cc/paper_files/paper/2025/file/45c361d4117d598d4bb6568b407e9ac9-Paper-Conference.pdf) — final paper §4.1–4.3, selected Appendix B.5; project/code README.

## Minimal Check — Researcher Proposal

연구자 제안: 원 residual·0 residual·scalar gain과 fresh residual을 먼저 비교하고 제어 주기/환경 상호작용 수를 맞춘다.

실행하지 않았다. 재개는 해당 연구의 local Docker 환경·입출력 확인 뒤에 한정하며 큰 학습을 자동 실행하지 않는다.
