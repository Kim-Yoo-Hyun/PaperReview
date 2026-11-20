# Docker 재현

현행 연구의 최소 실험은 [각 후보의 재현 방법](../research_topics/README.md)과 [다음 작업](../../TODO.md)을 따른다. 현재 컴퓨터의 로컬 Docker와 대상 장치를 확인한 뒤 지정한 범위까지 실행한다.

| 재현 가능한 자료 | 실행·근거 |
|---|---|
| 조립 실패의 원인별 복구 | 파지·손목·접촉 관측에 따른 복구와 탐색 폭·시작 방향을 두 접촉 예산에서 비교했다. [CPU 재현 방법](../research_topics/assembly_recovery/재현%20방법/README.md) · [탐색 폭 결과](../research_topics/assembly_recovery/내용/README.md#scan-results) |
| 시연의 선택적 재수집 | 공개 원격조작 표본에서 시연자 요청과 적용 명령을 대조했다. [CPU 재검산 명령·표본 버전](../research_topics/demonstration_recollection/재현%20방법/README.md) |
| 리셋 후 접촉 상태 | [서랍·문 기구](../research_topics/reset_carryover/재현%20방법/README.md) · 서랍 96쌍과 기구 대조. [공개 Panda 문 정책](../research_topics/reset_carryover/재현%20방법/README.md#next-sim) · 독립 시작 8회, 후행 배정 128개, 고유 후행 궤적 80개. 모두 로컬 CPU Docker에서 실행 |
| C3 저장 logits | [Docker 재분석](./portable/README.md) · 한 checkpoint, 관측 16개 |
| 반응형 주행 계약과 제한 비교 | [계약 검사](./reactive_nav_contract/README.md) · [저장된 비교 재분석](./reactive_nav_pilot/README.md) |
| 관측 정보 계약 | [Docker 계약 검사](./proxy_observation_contract/README.md) · ARM64에서 제어·합성 검사 17개 확인 |

과거 native 실행 시도와 현재 투자 판정은 [종료·보류 결과](../research_topics/RESULTS.md)에서 확인한다.
