# Scaling up Memory for Robotic Control via Experience Retrieval

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Pipeline and Representation

상위 정책이 과거의 중요한 keyframe을 선택·추적하고 최근 관측과 함께 하위 정책용 지시를 만든다.

이력 keyframe·현재 관측·task → 상위 언어 지시 → π0.5 하위 조작 정책. Episode 내 기억과 외부 시연 bank는 다른 정보원이다.

## Training vs Inference

선택 supervision·실패 후 이력 분포·최근 frame 예산. 공식 proceedings는 Qwen 7B, project는 3B로 표기하므로 backbone 크기는 version 확인 필요을 확인해 추가 supervision과 실제 배포 입력을 분리한다. 공개 code link의 존재를 재현 성공으로 간주하지 않는다.

## Objective and Temporal Contract

Exact loss/control law, optimizer, action horizon, control rate와 memory budget은 이번 abstract/project 확인에서 확정하지 않았다. [평가 조건](./04_evaluation.md)과 함께 읽는다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/9da515b1ad19d032a7398f00f5ff9b0c-Abstract-Conference.html) · [저자 project](https://jen-pan.github.io/memer/).
