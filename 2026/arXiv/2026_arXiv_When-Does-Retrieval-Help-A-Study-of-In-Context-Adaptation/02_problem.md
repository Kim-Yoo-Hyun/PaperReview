# Problem — When Does Retrieval Help? A Study of In-Context Adaptation in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Target Problem

검색 representation의 품질이 downstream robot success에 어떻게 연결되는지 조사한다.

## Robotics Loop

공유 시연 buffer에서 4개 entry → π0-FAST context → action. 원 RICL의 DINO distance interpolation은 모든 비교에서 제외한다.

## Assumptions to Check — Researcher Interpretation

연구자 점검: 다른 task의 도움과 다른 task의 오염을 하나의 범주로 합치지 않는다.

개념 연결: RICL → retrieval study/RA-VLA → controlled bank growth.

## Boundary

원 RICL과 보간 규칙이 다르다. Retrieval score가 좋다는 이유만으로 정책 성능을 추정할 수 없다. Main venue는 미확인; 본문 workshop 표기는 main acceptance 근거가 아니다.

근거: [확인한 원문](https://arxiv.org/html/2610.05492v1), §2–3, Appendix D–E.
