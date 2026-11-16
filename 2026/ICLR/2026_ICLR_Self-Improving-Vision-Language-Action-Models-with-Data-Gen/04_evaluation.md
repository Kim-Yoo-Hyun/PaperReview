# Self-Improving Vision-Language-Action Models with Data Generation via Residual RL

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Evaluated Setting and Evidence

LIBERO·SimplerEnv와 실제 Franka 조작을 보고한다. 여기서는 단계별 정책 역할을 확인했으며 성공률·trial 수·전체 ablation은 새로 정리하지 않았다.

## Comparison and Reproducibility Boundary

ICLR 공식 program의 채택과 읽은 arXiv v1을 구별한다. 최종본 동등성·동일 residual의 반복 base 갱신 전이·공식 전체 학습 code는 확인하지 않았다.

정확한 dataset 규모·train/test 분할·trial/seed·수치·모든 baseline/ablation은 이 노트에서 미기록이다. 논문 자체의 미보고라는 뜻이 아니다. 공개 code 링크는 실행 검증이 아니다.

근거: [지정 본문](https://arxiv.org/html/2511.00091v1) — §3, Appendix B.2/C.1/C.2.

## Minimal Check — Researcher Proposal

연구자 제안: 먼저 base 갱신 전후 action/normalizer와 residual 입력을 대조하고 frozen residual·gain 조정·fresh residual을 동일 새 데이터 예산으로 비교한다.

실행하지 않았다. 재개는 해당 연구의 local Docker 환경·입출력 확인 뒤에 한정하며 큰 학습을 자동 실행하지 않는다.
