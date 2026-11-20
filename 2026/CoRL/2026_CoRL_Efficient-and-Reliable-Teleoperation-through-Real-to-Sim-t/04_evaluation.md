# Evaluation — Efficient and Reliable Teleoperation through Real-to-Sim-to-Real Shared Autonomy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-20 · CoRL 공식 채택 목록에서 제목·포럼 ID·포스터 세션 2의 56번을 대조했다. 저자 원문 §III–V와 표 II, 온라인 수집기 및 공개 학습 자료를 확인했다.

## 평가 조건

§IV-A 및 부록 A-E는 xArm7으로 너트 나사 체결, 기어 맞물림, 핀 삽입을 수행한 참여자 16명의 결과를 보고한다. §IV-C 표 II의 기어 맞물림에서 같은 시도 수로 수집한 시연으로 학습한 Diffusion Policy의 삽입 성공은 보조 11/20, 직접 조작 1/20이다. 같은 성공 시연 수 비교에서는 각각 9/20, 0/20이다. [원문 및 평가 절](https://arxiv.org/html/2603.17016#S4.SS3)

## 해석할 때 확인할 조건

참여자 숙련도, 수집 시도 수, 성공한 시연 수 및 소요 시간을 개별 조건으로 기록한다. 한 종류의 기어 삽입에 대한 하류 정책의 이득을 다른 조립 작업에 적용하려면 별도 평가가 필요하다.

## 저자가 밝힌 한계

§V에서 보조가 들어올 때 사람의 전략이 변해 데이터 수집 당시의 대리 모델과 실제 사용자 행동 사이에 차이가 생길 수 있다고 밝힌다. [원문](https://arxiv.org/html/2603.17016#S5)
