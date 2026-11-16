# Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Source audit: 2026-11-16: RSS metadata·공식 project/code 및 arXiv v1 §III–IV, Appendix IX–X의 지정 내용 확인. RSS 최종본문 전체 대조·사용자 정독·실험을 의미하지 않는다.
> Canonical metadata: [01_overview.md](./01_overview.md).

## Policy and Training

- System2: Qwen3-VL-2B-Instruct. System1: flow MM-DiT expert. System0: AMO.
- 사전학습: 48D task-space의 FAST next-action token 예측. **EgoDex 829h와 Humanoid Everyday 31h를 함께 사용**하므로 인간 데이터만 사용했다고 쓰지 않는다.
- 후학습·task 적응: VLM을 고정하고 action expert를 flow matching으로 학습한다.
- 출력36D는 상체28D+하체 명령8D다. AMO가 하체15관절 target을 생성해 전신43관절로 연결한다.

근거: [§III-B, IV-A](https://arxiv.org/html/2603.12263v1#S3). §III의 일반 state 설명과 §IV-A2의 28D arm/hand state를 동일 tensor라고 단정하지 않는다.

## Temporal Interface

Training-time RTC와 비동기 실행을 사용한다. Appendix IX의 **60Hz는 control thread**이며 VLA query 주파수로 기록하지 않는다. [Appendix IX](https://arxiv.org/html/2603.12263v1).

## Release Boundary

[공식 코드](https://github.com/physical-superintelligence-lab/Psi0)는 이후 SONIC·UnifoLM/Psi-Dream 기반 공개 구성을 포함한다. 재현 시 branch/checkpoint/controller/data version을 함께 고정해야 하며 최신 release를 v1 학습 recipe와 혼합하지 않는다.
