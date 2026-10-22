# C5 — Physical reset가 자율 VLA RL의 학습 범위를 제한하는가

- 요약일: 2026-10-22. **일반 reset/coverage 방법 NO-GO / 구체적 진단 HOLD.**
- 질문: Policy update로 종료 상태가 달라질 때 reset 도달 가능성이 다음 학습 분포와 고정 target 분포의 성능을 어떻게 바꾸는가?

## 실제 진행과 결과

EARL·MEDAL·AutoEval·MiDAS 등을 대조했다. Training/target 분포 분리, reset policy의 분포 조정, VLA reset curriculum 자체는 기존 연구다.

Docker에서 4 repository의 text source 22개를 고정해 읽고 AutoEval 파일 목록 13,152개를 확인했다. 실제 payload 검사는 metadata24개·trajectory2개에 한정됐다. Pickle은 opcode/문자열만 검사했으며 역직렬화·이미지 분석·성공률 계산은 없었다. Human intervention/retry 흔적은 있었지만 요청–실패–재시도–rescue 전체 reset ledger와 동일 VLA RL chronology는 확보하지 못했다.

## GPU가 확보되면 가능한 최소 검증

Qualified native frozen policy에서 complete reset ledger를 수집·검증한 뒤 고정 target 시작 분포와 실제 achieved start 분포를 분리 평가할 수 있다. 이후 같은 robot time·rescue budget으로 quota/단순 reset 조정과 RL update를 비교한다. Simulator reset과 physical reset 비용은 별도다.

## GPU 외 한계

평가 selection bias, 학습 coverage, 운영 throughput은 다른 결과다. 학습 분포가 target과 다르다고 결함은 아니며 curriculum 이득도 가능하다. 관측되지 않은 reset 실패를 성공 denominator에서 빼면 판단이 달라진다. Coverage 밖 효과를 importance weighting만으로 알아낼 수 없다.

**현재 권고:** GPU만으로 reset bias 가설이 검증되지 않는다. Complete ledger·native headroom·기존 quota 이후 gap이 있어야 재개한다. AutoEval이 실제 편향됐다는 결론은 얻지 못했다.

근거: [C5 결과](../2026-10-21_c5_reset_audit/README.md), [자료 감사](../2026-10-21_c5_reset_audit/DATA_AND_CODE_REVIEW.md), [진단 계약](../2026-10-21_c5_reset_audit/DIAGNOSTIC_PROTOCOL.md).

## Registry 연결 — 2026-10-22 등록

- [EARL](../../../2022/ICLR/2022_ICLR_Autonomous-Reinforcement-Learning-Formalism-and-Benchmarki/01_overview.md) — 2022 ICLR, `pr-1023`.
- [MEDAL](../../../2022/ICML/2022_ICML_A-State-Distribution-Matching-Approach-to-Non-Episodic-Rei/01_overview.md) — 2022 ICML, `pr-1024`.
- [AutoEval: Autonomous Evaluation of Generalist Robot Manipulation Policies in the Real World](../../../2025/CoRL/2025_CoRL_AutoEval-Autonomous-Evaluation-of-Generalist-Robot-Manipul/01_overview.md) — 2025 CoRL, `pr-1025`.
- [RSA](../../../2025/NeurIPS/2025_NeurIPS_Robust-and-Scalable-Autonomous-Reinforcement-Learning-in-I/01_overview.md) — 2025 NeurIPS, `pr-1015`.

발표 status와 신규 5개 note의 근거는 각 overview를 따른다. 이전 buildup의 정독/코드 감사와 이번 abstract 기반 등록의 범위를 합치지 않는다.
