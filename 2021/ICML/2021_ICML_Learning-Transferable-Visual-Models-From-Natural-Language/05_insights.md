# Insights — Learning Transferable Visual Models From Natural Language Supervision

> Evidence maturity: `UNREAD`. 이 문서는 읽기 위치와 검증 질문을 정리한 curation note이며, 정독 완료를 뜻하지 않는다.

## Why CORE

이 논문은 **VLA and generalist robot policies**에서 vision-language prior를 robot state와 action으로 연결하는 data, architecture, action representation의 기준점로 선정됐다.

## Captured Source Cues — Not Yet Independently Verified

- Problem cue: We study the performance of this approach by benchmarking on over 30 different existing computer vision datasets, spanning tasks such as OCR, action recognition in videos, geo-localization, and ...
- Method cue: For instance, we match the accuracy of the original ResNet-50 on ImageNet zero-shot without needing to use any of the 1.28 million training examples it was trained on.
- Result/evaluation cue: State-of-the-art computer vision systems are trained to predict a fixed set of predetermined object categories.

위 cue는 기존 official abstract 또는 local text extraction에서 보존한 것이다. 수치·조건·인과적 해석은 full-text 정독 전까지 `UNVERIFIED`다.

## Dependency Position

`이 track의 출발점 → Learning Transferable Visual Models From Natural Language Supervision → CLIPort: What and Where Pathways for Robotic Manipulation`

이 화살표는 reading dependency다. 직접 citation 관계는 references와 related work를 확인한 뒤 synthesis 문서에만 확정한다.

## Close-Reading Checklist

- input/state, action representation, data/embodiment scale, control rate, horizon, fine-tuning protocol, unseen-task evaluation와 recovery
- 논문이 고정한 가정과 실제 deployment에서 깨질 조건
- strongest baseline과 공정한 비교가 성립하는 조건
- negative result, failure case, compute/data/hardware dependency

## Research Use

- semantic generalization과 low-level control 성능의 기여를 분리한다.
- 연결 gap: `G-01 / G-02 / G-10 / G-12` in [RESEARCH_GAPS.md](../../../research/RESEARCH_GAPS.md)

## Minimal Reproduction

동일 robot/task split에서 representation, action head와 data recipe를 분리해 success, latency와 intervention을 비교한다.

## Promotion Rule

`READ`로 올리려면 method/evaluation 필드를 채우고, `SYNTHESIZED`로 올리려면 같은 track의 선행·후속 논문과 comparison matrix를 갱신한다.
