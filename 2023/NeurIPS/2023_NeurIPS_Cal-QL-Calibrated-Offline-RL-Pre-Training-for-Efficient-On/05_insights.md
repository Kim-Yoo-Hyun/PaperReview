# Cal-QL: Calibrated Offline RL Pre-Training for Efficient Online Fine-Tuning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Paper-supported conclusion

Conservative value의 scale을 reference policy 가치와 정렬하여 online 갱신에 유용한 초기화를 학습한다.

Offline-to-online fine-tuning benchmark를 비교한다. 모든 VLA 보존 문제를 해결했다고 해석하지 않는다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2023/hash/c44a04289beaf0a7d968a94066a1d696-Abstract-Conference.html). 초록의 주장 범위이며 독립 재현 결과가 아니다.

## Researcher interpretation

### Why This Matters

초기 성능 손실을 semantic forgetting으로만 설명하지 않게 하는 critic calibration baseline이다.

### Dependency and Evolution

CQL → Cal-QL → AWAC/RLPD 및 VLA online 전환의 초기 손실 분석.

이는 개념적 읽기 연결이며 직접 citation 또는 검증된 derivation을 뜻하지 않는다.

### Assumptions and Failure Questions

reference return·보수성·초기 탐색·데이터 혼합·성능 회복 비용.

논문이 실제 보고한 failure case로 간주하지 않는다.

### Minimal Comparison

같은 actor 초기화에서 critic calibration만 바꾸고 초반 task별 성공·value scale을 비교한다.

### Falsifiable Question

초기 지시 성능 손실은 표현 망각보다 critic scale의 오류로 설명되는가?

같은 정보·데이터·계산 조건에서 단순 대안이 차이를 설명하면 해당 확장 가설을 수정한다. 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.
