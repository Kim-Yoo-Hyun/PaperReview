# Evaluation — DRILL: Training World Models to Improve Policies, Not Predict Pixels

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Paper-Supported Evaluation Scope

시뮬레이터와 VLA backbone 비교, PUR 진단을 보고한다. §6은 simulation-only 범위와 meta-gradient 계산 부담을 명시한다.

## Interpretation Boundary

VWI와 IMG의 관계는 가정에 의존한다. Pixel 품질과 control utility 차이 자체는 이 논문이 이미 직접 다룬다. 실제 로봇 검증으로 확대하지 않는다.

## Reproduction Status

이번 작업의 정책 실행·학습은 0회다. 위에서 명시하지 않은 dataset 크기·split·trial·hardware·metric·baseline 수치는 미기록이며 논문 자체의 미보고를 뜻하지 않는다. Resource 자동 연결은 cue_only다.

근거: [확인한 원문](https://arxiv.org/html/2610.30814v1), §3, §5.5, §6 limitations.
