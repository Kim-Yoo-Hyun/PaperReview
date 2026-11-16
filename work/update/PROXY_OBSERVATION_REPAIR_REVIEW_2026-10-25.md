# GAP-N3 — 수정 source packet과 제한된 계약 검사

- 완료 범위: 2026-10-25 KST, **GAP-N3-A DONE**. [Packet](../experiments/proxy_observation_contract/README.md)·[동결 protocol](../experiments/proxy_observation_contract/PROTOCOL.json)을 만들고 로컬 Docker에서 계약 검사 **17/17 PASS**.
- **전체 GAP-N3는 PARTIAL, 연구 재개 gate NOT_MET. 연구 채택·수집·학습 HOLD.** Source 수정·합성 계약 검사를 native 검증으로 승격하지 않는다.
- 직전 [N2 심사](./PROXY_OBSERVATION_QUALIFICATION_REVIEW_2026-10-25.md)와 [N1 연구 설계](./PROXY_OBSERVATION_CONTRACT_REVIEW_2026-10-25.md)를 보존한다. Canonical 질문은 [DATA-TRANSFER](../../synthesis/02_rl_il_offline.md#gap-data-transfer-2026)다.

## 1. 이번 요청으로 달라진 것

직전 TODO는 수정 source/fixture packet 대기였다. 사용자의 다음 TODO 진행 요청을 받아, 기존 요구사항을 다시 나열하는 대신 **그 packet의 source/계약 부분을 직접 제작**했다. 구현 전에 primary claim·입력·행동 범위·결정 시점·비용·baseline·metric·기각 조건을 제한된 계약 검사 수준으로 동결했다. Learned selector/추정기나 새로운 VLA 방법은 구현하지 않았다.

| N2 미충족 항목 | 이번에 만든 구체 artifact | 아직 미충족인 부분 |
|---|---|---|
| Raw/global identity·group split | Digest/raw key 기반 stable ID와 순서 독립 global index sidecar 함수; duplicate/group split 혼입 거부 | 실제 HDF5/기존 PKL 연결, 모든 sample provenance, attempt log integration |
| 관측/action 시간·memory mask | 알려진 연속 post-step row의 관측 i→action i+1 정렬 함수. 동일 raw-time slot의 cue/control mask와 미래/누락 cue 거부 | 배포 데이터 생성 시점/offset 확인, 실제 feature와 online index 일치, encoder/normalizer |
| 실제 model input | 허용 semantic key, resolved perceptual variant, predictor/encoder digest·유효 memory 검사 함수 | 실제 model tensor capture/정답 비노출 증거. 문자열 기술서 검사로 대체할 수 없음 |
| Goal/planner/evaluator | 원본 3파일 수정 patch + helper 1파일. 독립 색 permutation, 동일 target의 predicate/solve/segment/text, 별도 goal 함수·metadata 전달 | 실제 scene/RGB/proprio equality, native planner·성공 판정·controller 동작 |
| 별도 첫 선택 metric | 이름을 **첫 배타적 접근 구간 진입** 보조 proxy로 좁히고 threshold·중복 tick·모호함·미관측 처리를 고정 | Native trace에서 사건 타당성 확인. 검증 전 “선택률”로 쓰지 않음 |

N2에서 조사한 원본 중 patch에 필요한 3파일만 다시 가져와 **동일 SHA256**를 확인했다. 최신 HEAD나 publication status를 재조사한 작업은 아니다. 원본 경로·revision·hash는 [source lock](../experiments/proxy_observation_contract/sources.lock.json), 생성 변경은 [patch](../experiments/proxy_observation_contract/results/verified/source_repair.patch)에 있다. 임시 원본에 실제 patch 적용 후 새 파일 4개의 hash도 대조했다. 저장소의 논문 원문·기존 실험 source에는 patch를 적용하지 않았다.

## 2. 검사 결과와 해석 경계

[Docker report](../experiments/proxy_observation_contract/results/verified/contract_report.json)는 17개 test 이름, 원본/코드 hash, container image, Python/architecture, 소요 시간과 gate를 기록한다. Source 수정의 근거는 N2의 [VideoUnmask task](https://github.com/RoboMME/robomme_benchmark/blob/1babf64480e28320e0f9db7992554616ceefda0e/src/robomme/robomme_env/VideoUnmask.py#L251), [별도 language goal](https://github.com/RoboMME/robomme_benchmark/blob/1babf64480e28320e0f9db7992554616ceefda0e/src/robomme/robomme_env/utils/task_goal.py#L98), [metadata builder](https://github.com/RoboMME/robomme_benchmark/blob/1babf64480e28320e0f9db7992554616ceefda0e/src/robomme/env_record_wrapper/episode_config_resolver.py#L192)다. GitHub web 열기는 cache miss였고 pinned raw URL과 hash 대조로 내용을 확보했다.

- **Source binding:** 수정된 실제 task assignment/lambda·language-goal branch를 AST로 분리하고 stand-in actor/predicate/planner로 실행했다. 3색×6 permutation에서 target 일치를 확인했다. 전체 simulator나 planner 호출 결과는 아니다.
- **Metadata:** 원본 metadata loader가 fixture 설정을 보존하고, 수정한 builder의 environment 생성 전 kwargs에 전달하는 경로를 분리 검사했다. Wrapper 전체 import/reset 성공을 의미하지 않는다.
- **부정 사례:** 변경된 원본 hash, 잘못된 permutation/seed/difficulty, 중복 raw identity·split 혼입, 시간 gap/episode 혼입, 미래 frame/없는 cue, oracle 필드·symbolic override·all-mask·encoder mismatch, 중복 tick·모호한 접근 등을 검사했다.
- **실행 범위:** ARM64 Linux Docker, Python 3.11.14, 별도 dependency 설치 없음. Tests는 network none·512 MB·2 CPU·60초 상한이다. 저장된 실행 시간은 이 작은 검사에만 해당하며 정책 처리량이 아니다.

**현재 source/계약 부분의 PASS는 새 과학적 결과가 아니다.** 특히 fixture에서 정보 조건을 제대로 만들 수 있는지, 정보가 다른 selector의 subset이 같은 target의 성능을 바꾸는지는 미검증이다. N1의 반례와 단순 층화/tuning 대안을 유지한다. 일반 데이터 전이 방법 NO-GO와 기존 다른 연구 후보의 판정도 유지한다.

## 3. Native 재개를 제한하는 실제 상태

[자원 확인](../experiments/proxy_observation_contract/results/verified/runtime_check.json)에서 현재 local Docker는 ARM64, 약 8.2 GB 메모리이며 `--gpus all` 할당 요청은 **exit 125: GPU capability를 만족하는 device driver를 선택할 수 없음**으로 실패했다. Dummy print 명령조차 시작되지 않아 native episode는 0이다. Docker daemon 자체는 켜져 있으며 계약 검사는 실행됐다.

모든 CPU simulation이 불가능하다고 결론 내리지 않는다. RoboMME의 CPU/Vulkan/native image 경로는 이번에 qualified하지 않았고, host MPS·원격/cloud로 바꾸지 않았다. 데이터·checkpoint·PDF를 받거나 simulator/학습 package를 host에 설치하지 않았다. 작업용 container는 종료 후 남기지 않고 이번에 새로 받은 Python image 참조도 정리한다. 기존 navigation image는 보존한다.

**다음 GAP-N3-B: native fixture qualification, WAITING_RESOURCE.** 사용자 선택 컴퓨터의 적합한 로컬 Docker에서 native image/dependency를 먼저 확인한 뒤, 고정 scene 1개×색 permutation 3개의 reset/demo 종료·첫 decision·current RGB/proprio/pose equality를 확인한다. 이는 새로운 selector나 학습 없이 fixture가 가능한지 판단하는 단계다. Planned 3개 설정은 [fixture plan](../experiments/proxy_observation_contract/results/verified/fixture_plan.json)에 있고 모두 미수집이다.

GPU가 있어도 native runtime·fixture gate가 자동 통과하지 않는다. 이 가장 취약한 연결이 통과하기 전에는 HDF5/model pipeline 전체 adapter를 확대 구현하지 않는다. Native fixture 통과 후에도 실제 ID join·time/feature/tensor 연결·checkpoint provenance·normalizer·selector estimator·예산은 별도 심사한다. N1의 72 episode 수집과 정책 비교는 여전히 실행 계획이 아니다.

## 4. 저장·재개·검증

다른 컴퓨터에서는 [packet README](../experiments/proxy_observation_contract/README.md)의 단일 명령으로 source fetch/hash 확인과 Docker 계약 검사를 재실행한다. 기존 `results/verified`는 덮어쓰지 않는다. 이 portable 경로는 **계약 검사 재개 경로**이며 native rollout launcher로 표시하지 않는다.

TODO·관련 synthesis·root/update/experiments navigation을 동기화한다. Registry 신규 등록·tier·사용자 reading 상태·N1/N2 과거 근거·다른 실험은 보존한다. 유지보수 명령, canonical/dirty hash 보존, 작업용 source/image 정리 결과는 [maintenance 기록](../experiments/proxy_observation_contract/results/verified/maintenance.json)에 남긴다.
