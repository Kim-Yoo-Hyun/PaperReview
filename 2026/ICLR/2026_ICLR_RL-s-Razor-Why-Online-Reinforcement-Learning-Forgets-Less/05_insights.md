# RL's Razor: Why Online Reinforcement Learning Forgets Less

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

같은 신규 과제 성능에서 RL과 SFT의 망각·정책 KL을 비교하고 on-policy RL의 작은 분포 변화 편향을 분석한다.

언어 모델과 로봇 foundation model에서 적응 성능과 기존 능력 보존을 평가한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/618c95f4557c15b253fb0e6f548ea0c0-Abstract-Conference.html) · [저자 project/code](https://jyopari.github.io/posts/rl_razor). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 미확인 항목: KL 방향·평가 관측 분포·기존 능력 정의·단순 학습률/모방 대안.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

RL이 지시 능력을 잃는다는 가정을 먼저 반박할 직접 선행이며 KL 진단의 기준이다.

### Dependency and Evolution

PPO/on-policy 학습·KL 제약에서 SimpleVLA-RL 후학습 보존 질문으로 연결한다. 직접 인용 관계와는 구별한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 초기 정책·적응 성능·비용에서 목표별 행동 변화와 관측별 KL의 관계를 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

신규 목표 관측의 작은 token KL이 미학습 목표의 closed-loop 행동 보존도 예측하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.

## Related Research Review

[지시별 행동 보존의 선행 대조](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/8303fdd74fedbd456c0ab94230bde5cfd64c40ba/work/research_topics/unified_vla_rl/%EB%82%B4%EC%9A%A9/README.md#langret-n1)와 [source 원장](../../../work/sources/vla_masters_gap_scout_2026-11-12.json)에 지정 본문·공개 코드 검토 범위를 보존한다. 이 링크가 위 초록 노트나 사용자 reading status를 정독 완료로 승격하지 않는다.
