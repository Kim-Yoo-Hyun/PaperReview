# Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Evaluated Setting and Evidence

Simulation-to-real residual 전이와 base SFT를 다룬다. 여기서 동일 residual의 sim-to-real 사용은 확인했지만 서로 다른 backbone/갱신된 base 간 동일 weights 재사용은 확정하지 않았다.

## Comparison and Reproducibility Boundary

CoRL 공식 accepted list에서 exact title/forum을 확인했다. 읽은 것은 arXiv v1이며 final paper 동등성과 공식 학습 code 공개는 미확인이다.

정확한 dataset 규모·train/test 분할·trial/seed·수치·모든 baseline/ablation은 이 노트에서 미기록이다. 논문 자체의 미보고라는 뜻이 아니다. 공개 code 링크는 실행 검증이 아니다.

근거: [지정 본문](https://arxiv.org/html/2606.18953v1) — §3.1–3.4/5.1–5.4/7, Appendix A.

## Minimal Check — Researcher Proposal

연구자 제안: 같은 로봇·관측·상태 추정기를 고정하고 base만 교체해 base-only·동결 residual·gain 조정부터 비교한다.

실행하지 않았다. 재개는 해당 연구의 local Docker 환경·입출력 확인 뒤에 한정하며 큰 학습을 자동 실행하지 않는다.
