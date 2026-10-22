# Portable replay 검증 — 2026-10-23

저장 C3 지표 재분석을 완료했다. 새 model forward·robot rollout·training은 모두 0회이며 host dependency 설치도 0회다. 상세 image ID·입력/코드 hash·수치 결과는 [validation_result.json](./validation_result.json)에 기록했다.

| 검사 | 결과·범위 |
|---|---|
| Docker ARM64 | Build·4개 unit test·14개 reference 지표 일치 PASS |
| Docker AMD64 | 같은 검사 PASS. 현재 ARM Mac의 Docker Desktop 에뮬레이션이며 물리 x86 host에서 실행한 결과는 아님 |
| 경로 이동 | 최소 recipe+3개 evidence 파일을 임시 Git repository에 commit하고 공백 있는 다른 경로로 clone. 저장소 밖 working directory에서 check/build/test/replay PASS |
| 입력 변조 | Clone의 NPZ 첫 byte 변경 후 hash mismatch로 exit 1. 원본 evidence는 read-only로 보존 |
| 미지원 native 실험 | `E1_NATIVE` 요청 exit 2. HOLD 명시 |
| 원격 daemon | SSH endpoint 지정 시 접속 전에 exit 2 |
| 환경 고정 | Python base image digest, NumPy 2.2.6 Linux wheel hash, 3개 입력 hash 고정 |

T=1.6의 전체 chunk head-score trace 감소는 두 플랫폼에서 약 **0.4962329%**, 제거량의 마지막 slot 비중은 약 **99.6223534%**로 기존 값과 일치했다. 조건부 head score 진단이며 성공률이나 실제 reward-weighted gradient 개선이 아니다.

Unit test는 수동 계산 가능한 alias/marginal trace, singleton-class 동치, hash 손상 거부, 기준 지표 불일치 거부를 확인한다. 원래 PPO/autograd/model-forward 검증은 다시 수행하지 않았다.

사용자 저장소 자체는 commit/push하지 않았다. 이 검사는 필요한 최소 파일의 local Git clone 이동성 검사이며 전체 원격 저장소 cold start 또는 다른 물리 컴퓨터의 GPU qualification이 아니다. Native 연구 실험은 기존 연구·자료 gate를 먼저 충족해야 한다. 테스트용 임시 repository/clone은 삭제했다. 최종 image 정리 상태는 JSON의 cleanup 필드를 따른다.
