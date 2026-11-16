# Evaluation — Cooperative Multi-Agent Vision-Language-Action Models via Reinforced Fine Tuning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Paper-Supported Evaluation Scope

π0·π0.5, RoboTwin·RoboFactory·실제 Franka 2대의 총 11개 task를 보고한다. §5의 시뮬레이션 task당 100회·real task당 50회 평가.

## Interpretation Boundary

CHORUS의 local-only 입력과 같지 않다. 읽은 평가에서 독립 학습 partner 교체의 순수 효과는 분리되지 않는다. Anonymous code 링크는 논문에 있으나 실행·내용 확인은 미완료.

## Reproduction Status

이번 작업의 정책 실행·학습은 0회다. 위에서 명시하지 않은 dataset 크기·split·trial·hardware·metric·baseline 수치는 미기록이며 논문 자체의 미보고를 뜻하지 않는다. Resource 자동 연결은 cue_only다.

근거: [확인한 원문](https://arxiv.org/html/2609.36588v1), §4.2–4.3, §5, Appendix C.1.
