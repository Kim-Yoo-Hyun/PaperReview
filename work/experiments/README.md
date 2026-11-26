# Docker 재현

현행 연구의 최소 실험은 [각 후보의 재현 방법](../research_topics/README.md)과 [다음 작업](../../TODO.md)을 따른다.

<a id="local-docker"></a>

## 로컬 실행과 인계

1. 실행할 컴퓨터에서 Docker context의 endpoint가 로컬인지, daemon이 응답하는지 확인한다. 대상 simulator·모델이 요구하는 아키텍처·메모리·GPU 할당·CUDA/EGL·입출력과 자산 mount를 확인한다. 기존 실패 기록에는 당시 환경을 표시한다.
2. 조건이 맞으면 해당 후보의 최소 검사를 컨테이너 안에서 실행한다. 모델·데이터·패키지도 컨테이너와 지정한 볼륨에 둔다. 큰 학습이나 성능 비교는 그 단계의 범위를 따른다.
3. 실행할 수 없으면 후보의 `재현 방법/README.md`에 실패한 단계·명령·결과, 필요한 OS·드라이버·Docker·패키지 버전, 코드·체크포인트·정규화 파일의 revision 또는 해시, 자산 경로와 재개 명령을 남긴다. 특정 사용자의 절대 경로는 설정값으로 분리한다.
4. TODO에는 준비된 자료, 실제 실행 범위, 남은 자원·구현을 구분한다. 환경이 바뀌어도 과학적 재개 조건은 [종료·보류 결과](../research_topics/RESULTS.md)를 따른다. 작업이 만든 임시 컨테이너·이미지만 확인해 정리한다.

## 재현 자료

| 재현 가능한 자료 | 실행·근거 |
|---|---|
| 조립 실패의 원인별 복구 | 파지·손목·접촉 관측에 따른 복구와 탐색 폭·시작 방향을 두 접촉 예산에서 비교했다. [CPU 재현 방법](../research_topics/assembly_recovery/재현%20방법/README.md) · [탐색 폭 결과](../research_topics/assembly_recovery/내용/README.md#scan-results) |
| 시연의 선택적 재수집 | 공개 원격조작 표본에서 시연자 요청과 적용 명령을 대조했다. [CPU 재검산 명령·표본 버전](../research_topics/demonstration_recollection/재현%20방법/README.md) |
| 리셋 후 접촉 상태 | [서랍·문 기구](../research_topics/reset_carryover/재현%20방법/README.md) · 서랍 96쌍과 기구 대조. [공개 Panda 문 정책](../research_topics/reset_carryover/재현%20방법/README.md#next-sim) · 독립 시작 8회, 후행 배정 128개, 고유 후행 궤적 80개. 모두 로컬 CPU Docker에서 실행 |
| C3 저장 logits | [Docker 재분석](./portable/README.md) · 한 checkpoint, 관측 16개 |
| 반응형 주행 계약과 제한 비교 | [계약 검사](./reactive_nav_contract/README.md) · [저장된 비교 재분석](./reactive_nav_pilot/README.md) |
| 관측 정보 계약 | [Docker 계약 검사](./proxy_observation_contract/README.md) · ARM64에서 제어·합성 검사 17개 확인 |

과거 native 실행 시도와 현재 투자 판정은 [종료·보류 결과](../research_topics/RESULTS.md)에서 확인한다.
