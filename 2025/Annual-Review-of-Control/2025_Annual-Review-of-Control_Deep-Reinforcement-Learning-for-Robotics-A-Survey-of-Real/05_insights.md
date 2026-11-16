# Deep Reinforcement Learning for Robotics: A Survey of Real-World Successes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Paper-supported conclusion

로봇 능력별 실제 성공 사례를 비교하고 sample 효율·수집·평가·장시간 통합의 문제를 분석한다.

실물 DRL 사례의 종합이며 새 통합 VLA 방법의 성능 실험이 아니다.

근거: [공식 paper/abstract](https://www.annualreviews.org/content/journals/10.1146/annurev-control-030323-022510). 초록의 주장 범위이며 독립 재현 결과가 아니다.

## Researcher interpretation

### Why This Matters

석사 연구 후보의 구현 부담과 로봇 행동 기여를 평가할 최신 survey로 2013 원전과 함께 사용한다.

### Dependency and Evolution

Kober 2013 → 실제 deep RL 성공 사례 → SERL/HIL-SERL·VLA RL의 실물 조건.

이는 개념적 읽기 연결이며 직접 citation 또는 검증된 derivation을 뜻하지 않는다.

### Assumptions and Failure Questions

실제 로봇과 simulation 구분·성공 사례 선택 편향·데이터/개입 비용.

논문이 실제 보고한 failure case로 간주하지 않는다.

### Minimal Comparison

가까운 실물 선행들의 reset·reward·시연·상호작용·수동 엔지니어링 비용을 대조한다.

### Falsifiable Question

우리 후보가 줄이려는 실제 로봇 비용은 공개 선행의 어떤 병목과 일치하는가?

같은 정보·데이터·계산 조건에서 단순 대안이 차이를 설명하면 해당 확장 가설을 수정한다. Publisher의 2025 volume 게재를 사용한다. 2024 online-first와 같은 제목의 AAAI 2025 요약은 별도 신규 논문으로 중복 등록하지 않는다.
