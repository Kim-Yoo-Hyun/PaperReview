# Reinforcement Learning for Real-Time Vision-Language-Action Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Paper-supported conclusion

느린 VLA chunk 생성과 최신 관측을 사용하는 빠른 action edit를 분리해 EXPO-FT를 실시간 RL로 확장한다.

Kinetix와 실제 물체 전달·공 균형·테이블 축구·동적 pick을 평가한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.18207). 초록의 주장 범위이며 독립 재현 결과가 아니다.

## Researcher interpretation

### Why This Matters

지연·feedback 공백의 직접 선행이자 단일 정책 선호와 별도로 보존할 강한 editor pipeline baseline이다.

### Dependency and Evolution

EXPO-FT·asynchronous chunk 실행 → Real-Time EXPO-FT → unified VLA와 지연 대응 비교.

이는 개념적 읽기 연결이며 직접 citation 또는 검증된 derivation을 뜻하지 않는다.

### Assumptions and Failure Questions

edit 주파수·관측 timestamp·동기화·robot interaction 비용·단일 정책 여부.

논문이 실제 보고한 failure case로 간주하지 않는다.

### Minimal Comparison

같은 지연 조건에서 비동기 BC·기존 EXPO-FT·실시간 editor를 비교하고 실제 반응 시간을 분리한다.

### Falsifiable Question

단일 VLA RL은 같은 observation age·추론 비용에서 빠른 editor의 이득을 유지할 수 있는가?

같은 정보·데이터·계산 조건에서 단순 대안이 차이를 설명하면 해당 확장 가설을 수정한다. arXiv v1와 저자 project/code에서 EXPO-FT 원 방법과 real-time branch의 구분 확인. 공식 conference acceptance는 확인하지 않았다.
