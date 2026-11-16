# Evaluation — VLA-Trace: Diagnosing Vision-Language-Action Models through Representation and Behavior Tracing

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Paper-Supported Evaluation Scope

π0.5·OpenVLA의 representation과 행동을 비교한다. 읽은 §3의 stage 비교는 data-matched RL 대 SFT의 인과 추정이 아니다.

## Interpretation Boundary

읽은 arXiv v1과 EMNLP 최종본의 전체 동등성은 확인하지 않았다. 공개 toolkit의 존재와 우리 checkpoint adapter의 호환·실행은 별개다.

## Reproduction Status

이번 작업의 정책 실행·학습은 0회다. 위에서 명시하지 않은 dataset 크기·split·trial·hardware·metric·baseline 수치는 미기록이며 논문 자체의 미보고를 뜻하지 않는다. Resource 자동 연결은 cue_only다.

근거: [확인한 원문](https://arxiv.org/html/2605.30117v1), 공식 EMNLP metadata; arXiv v1 §3.1–3.3; code README.
