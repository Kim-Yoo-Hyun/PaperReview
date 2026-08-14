# Insights — π0.5: a Vision-Language-Action Model with Open-World Generalization

> Evidence maturity: `UNREAD`. 이 문서는 읽기 위치와 검증 질문을 정리한 curation note이며, 정독 완료를 뜻하지 않는다.

## Why CORE

이 논문은 **VLA and generalist robot policies**에서 vision-language prior를 robot state와 action으로 연결하는 data, architecture, action representation의 기준점로 선정됐다.

## Captured Source Cues — Not Yet Independently Verified

- Problem cue: Open-world generalization represents one of the biggest open problems in physical intelligence, and scalable learning systems offer a path to enable such generalization, as they have in domains ...
- Method cue: Our central contribution is a system for training a highly generalizable VLA, π0.5 , together with a proof of concept that generalization can emerge from this model when ...
- Result/evaluation cue: Our experiments show that this kind of knowledge transfer is essential for effective generalization, and we demonstrate for the first time that an end-to-end learning-enabled robotic system can ...

위 cue는 기존 official abstract 또는 local text extraction에서 보존한 것이다. 수치·조건·인과적 해석은 full-text 정독 전까지 `UNVERIFIED`다.

## Dependency Position

`π0: A Vision-Language-Action Flow Model for General Robot Control → π0.5: a Vision-Language-Action Model with Open-World Generalization → 이 track의 frontier 연결`

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
