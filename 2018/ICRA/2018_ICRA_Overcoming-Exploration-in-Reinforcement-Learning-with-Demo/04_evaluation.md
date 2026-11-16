# Overcoming Exploration in Reinforcement Learning with Demonstrations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Evaluated Setting and Evidence

시뮬레이션 로봇 팔의 sparse-reward 조작을 다룬다. VLA 연구가 아니며 현재 후보의 두 reference 규칙을 원 논문의 재현이라고 부를 수 없다.

## Comparison and Reproducibility Boundary

이번 확인은 Q-filter 수식과 서지에 한정한다. 정확한 seed·전체 baseline/ablation·현재 공식 code 상태는 확인하지 않았다.

정확한 dataset 규모·train/test 분할·trial/seed·수치·모든 baseline/ablation은 이 노트에서 미기록이다. 논문 자체의 미보고라는 뜻이 아니다. 공개 code 링크는 실행 검증이 아니다.

근거: [지정 본문](https://arxiv.org/pdf/1709.10089) — Q-Filter subsection / Eq. 8; arXiv abstract and publisher-deposited metadata.

## Minimal Check — Researcher Proposal

연구자 제안: 같은 reference 행동·critic·데이터·loss 계수를 사용한 원리 수준 Q-filter와 무조건 모방을 분리하고, 원 논문 전체 알고리즘 재현 여부를 명시한다.

실행하지 않았다. 재개는 해당 연구의 local Docker 환경·입출력 확인 뒤에 한정하며 큰 학습을 자동 실행하지 않는다.
