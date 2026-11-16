# RoboAlign: Learning Test-Time Reasoning for Language-Action Alignment in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Paper-supported conclusion

자연어 추론에서 action token을 생성하고 RL로 행동 정확도를 정렬한 MLLM 위에 diffusion action head를 학습한다.

LIBERO·CALVIN·실물 조작에서 alignment와 후속 VLA를 평가한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2603.21341). 초록의 주장 범위이며 독립 재현 결과가 아니다.

## Researcher interpretation

### Why This Matters

VLM의 RL 정렬과 배포 VLA의 직접 RL 갱신을 구분할 선행으로 단일 정책 연구의 기여 경계를 보완한다.

### Dependency and Evolution

VLM pretraining·OpenVLA → RoboAlign → VLA 내부 RL의 학습 단계 구분.

이는 개념적 읽기 연결이며 직접 citation 또는 검증된 derivation을 뜻하지 않는다.

### Assumptions and Failure Questions

RL action token과 최종 행동 차이·head 학습 데이터·추론 비용·공유 weight 경로.

논문이 실제 보고한 failure case로 간주하지 않는다.

### Minimal Comparison

고정 head와 재학습 head를 분리하고 같은 RL 데이터·계산에서 alignment 이득을 비교한다.

### Falsifiable Question

정렬된 backbone의 이득은 action head를 다시 학습하지 않아도 유지되는가?

같은 정보·데이터·계산 조건에서 단순 대안이 차이를 설명하면 해당 확장 가설을 수정한다. arXiv v1의 정확한 제목 사용. 저자 페이지의 이전 제목은 alias로 보존한다. 검색 색인의 ICLR 2026 표기는 공식 acceptance로 확인하지 못해 arXiv로 등록한다. RoboAlign-R1 world-model 논문과 다르다.
