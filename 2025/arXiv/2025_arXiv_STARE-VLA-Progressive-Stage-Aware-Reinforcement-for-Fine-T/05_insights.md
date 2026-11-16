# STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Paper-supported conclusion

의미 있는 단계로 trajectory를 나누고 stage-aware TPO/PPO 및 imitation–preference–interaction 후학습을 구성한다.

SimplerEnv와 ManiSkill3의 조작 과제를 평가한다. 실제 로봇 결과로 확대하지 않는다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2512.05107). 초록의 주장 범위이며 독립 재현 결과가 아니다.

## Researcher interpretation

### Why This Matters

단계별 credit·보상 shaping 자체가 기존 방법임을 반영하고 원 보상 보존·추가 supervision을 비교하는 직접 선행이다.

### Dependency and Evolution

Potential shaping·GAE·TPO/PPO → STARE-VLA → 장시간 VLA RL의 보상 접근권 비교.

이는 개념적 읽기 연결이며 직접 citation 또는 검증된 derivation을 뜻하지 않는다.

### Assumptions and Failure Questions

stage label·geometric/contact predicate·potential 경계·TPO/PPO 비용.

논문이 실제 보고한 failure case로 간주하지 않는다.

### Minimal Comparison

동일 stage 정보에서 단순 potential shaping과 STARE식 갱신을 원 sparse 성공 지표로 비교한다.

### Falsifiable Question

단계 보상 이득은 더 많은 privileged stage 정보를 준 효과인가?

같은 정보·데이터·계산 조건에서 단순 대안이 차이를 설명하면 해당 확장 가설을 수정한다. arXiv v2 및 저자 project 확인. 검색 색인의 ICLR 표기는 공식 proceedings/forum으로 확인하지 못해 arXiv 2025로 유지한다. 공개 구현 URL은 식별하지 못했다.
