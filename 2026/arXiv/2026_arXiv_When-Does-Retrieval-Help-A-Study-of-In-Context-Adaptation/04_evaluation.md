# Evaluation — When Does Retrieval Help? A Study of In-Context Adaptation in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Paper-Supported Evaluation Scope

LIBERO 25개 task·각 10개 고정 scene, task당 20개 expert demo의 buffer를 사용한다. 관련 다른 task 시연도 도움이 될 수 있으며 selector 우위는 일관되지 않는다.

## Interpretation Boundary

원 RICL과 보간 규칙이 다르다. Retrieval score가 좋다는 이유만으로 정책 성능을 추정할 수 없다. Main venue는 미확인; 본문 workshop 표기는 main acceptance 근거가 아니다.

## Reproduction Status

이번 작업의 정책 실행·학습은 0회다. 위에서 명시하지 않은 dataset 크기·split·trial·hardware·metric·baseline 수치는 미기록이며 논문 자체의 미보고를 뜻하지 않는다. Resource 자동 연결은 cue_only다.

근거: [확인한 원문](https://arxiv.org/html/2610.05492v1), §2–3, Appendix D–E.
