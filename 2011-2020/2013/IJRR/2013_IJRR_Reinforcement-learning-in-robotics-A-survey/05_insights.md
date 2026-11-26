# Reinforcement learning in robotics: A survey

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Paper-supported conclusion

Robot RL의 어려움과 성공 사례를 분류하는 survey이며 단일 새 학습 알고리즘을 제안하지 않는다.

기존 로봇 학습 사례를 종합한다. 단일 benchmark의 새 성능 표나 VLA 실험은 아니다.

근거: [공식 paper/abstract](https://journals.sagepub.com/doi/abs/10.1177/0278364913495721). 초록의 주장 범위이며 독립 재현 결과가 아니다.

## Researcher interpretation

### Why This Matters

로봇 문제의 제약에서 연구 질문을 세우기 위한 기반 survey로 최신 VLA 방법의 전제 점검에 필요하다.

### Dependency and Evolution

고전 robot policy search·제어 → 2013 survey → 2025 real-world DRL survey와 VLA RL.

이는 개념적 읽기 연결이며 직접 citation 또는 검증된 derivation을 뜻하지 않는다.

### Assumptions and Failure Questions

사례별 실제 로봇 여부·상호작용 정의·수동 설계·재개 조건.

논문이 실제 보고한 failure case로 간주하지 않는다.

### Minimal Comparison

선택한 로봇 task에서 interaction·reset·시연·보상 접근권의 비용표를 먼저 작성한다.

### Falsifiable Question

현재 제안의 실제 비용 병목은 sample 수인가, reset·보상·관측·안전한 수집인가?

같은 정보·데이터·계산 조건에서 단순 대안이 차이를 설명하면 해당 확장 가설을 수정한다. Sage 검색의 publisher abstract/metadata와 저자 연구실 BibTeX·원문 초록으로 IJRR 2013 확인. Publisher 직접 open은 timeout. Survey 본문 전체 정독은 하지 않았다.
