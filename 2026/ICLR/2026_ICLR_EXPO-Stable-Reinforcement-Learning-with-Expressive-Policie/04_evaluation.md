# EXPO: Stable Reinforcement Learning with Expressive Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Evaluated Setting and Evidence

공식 proceedings의 online RL 비교와 공개 구현을 확인했다. 현재 registry 노트는 학습 경로에 초점을 두며 개별 점수·독립 재현 결과를 제시하지 않는다.

## Comparison and Reproducibility Boundary

공개 code를 읽었지만 실행하지 않았다. Co-adaptation 결과를 독립 base release 교체 후 동결 editor의 전이 근거로 확대하지 않는다.

정확한 dataset 규모·train/test 분할·trial/seed·수치·모든 baseline/ablation은 이 노트에서 미기록이다. 논문 자체의 미보고라는 뜻이 아니다. 공개 code 링크는 실행 검증이 아니다.

근거: [지정 본문](https://arxiv.org/html/2507.07986v3) — §4 / Algorithm 1; expo_learner.py selected update paths. Code 검토 revision: `bbd571306b413e05d5d4b01a6efa20352c2b891a`; 실행하지 않았다.

## Minimal Check — Researcher Proposal

연구자 제안: co-adaptation과 독립 교체를 분리하고 base-only·warm-start·fresh editor·value 선택의 입력과 새 환경 상호작용 예산을 맞춘다.

실행하지 않았다. 재개는 해당 연구의 local Docker 환경·입출력 확인 뒤에 한정하며 큰 학습을 자동 실행하지 않는다.
