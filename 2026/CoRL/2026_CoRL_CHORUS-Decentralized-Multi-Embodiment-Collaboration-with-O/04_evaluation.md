# Evaluation — CHORUS: Decentralized Multi-Embodiment Collaboration with One VLA Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Paper-Supported Evaluation Scope

실제 mobile 협력·handover 등을 평가한다. §4.2는 scripted lateral partner perturbation 20회에서 공유/비공유 가중치의 반응성을 비교한다.

## Interpretation Boundary

Scripted perturbation은 독립 학습한 partner와의 cross-play와 다르다. 엄격한 동시 release는 범위 밖이다. 저자는 CoRL 2026을 표기하지만 이번 공식 acceptance 확인은 미완료다.

## Reproduction Status

이번 작업의 정책 실행·학습은 0회다. 위에서 명시하지 않은 dataset 크기·split·trial·hardware·metric·baseline 수치는 미기록이며 논문 자체의 미보고를 뜻하지 않는다. Resource 자동 연결은 cue_only다.

근거: [확인한 원문](https://arxiv.org/html/2606.12352v1), §3.1–3.3, §4.2, §5 limitations.
