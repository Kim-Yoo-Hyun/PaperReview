# EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Evaluated Setting and Evidence

실제 로봇을 위한 DROID/π0.5 공개 경로와 human intervention을 포함하는 구성을 확인했다. 이 release는 LIBERO/OpenVLA의 즉시 실행 baseline이 아니다.

## Comparison and Reproducibility Boundary

CoRL accepted list와 arXiv v1/code를 별도로 확인했다. 최종본 동일성·native 실행·독립 release 교체 효과는 미검증이다.

정확한 dataset 규모·train/test 분할·trial/seed·수치·모든 baseline/ablation은 이 노트에서 미기록이다. 논문 자체의 미보고라는 뜻이 아니다. 공개 code 링크는 실행 검증이 아니다.

근거: [지정 본문](https://arxiv.org/html/2605.25477v1) — §4.2–4.3 / Appendix C; expo_ft.py update_actor/_update_jit. Code 검토 revision: `21fe3d3b7d913c80836496817965932f49e0aedf`; 실행하지 않았다.

## Minimal Check — Researcher Proposal

연구자 제안: image encoder·base action·residual actor 중 무엇을 이전/동결하는지 명시하고 warm-start와 같은 replay·새 데이터 예산으로 비교한다.

실행하지 않았다. 재개는 해당 연구의 local Docker 환경·입출력 확인 뒤에 한정하며 큰 학습을 자동 실행하지 않는다.
