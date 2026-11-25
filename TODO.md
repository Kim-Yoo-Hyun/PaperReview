# 다음 작업

## 재개 순서

**다음 원장 작업은 다축 태그가 남은 NEXT 77편 중 앞의 50편이다.** 안정 ID 순으로 *When Life Gives You BC, Make Q-functions* (`pr-1125`)부터 *Tune to Learn* (`pr-1197`)까지다. 행동 복제에서 추출한 가치와 환경 상호작용으로 학습한 가치를 구분하고, 제어 이득이나 실행 주기가 달라지는 비교에서는 같은 정책의 어느 제어 조건을 측정했는지 기록한다. [직전 배치와 매핑](./work/update/REGISTRY.md#taxonomy-batches) · [별도 등록 배치](./work/sources/batches/gapfill_2026_11.yaml)

**다음 연구 작업은 G1이 걸쇠를 당기다가 저항이 갑자기 사라질 때 균형을 유지하는지 시뮬레이션에서 확인하는 것이다.** 후보 4의 첫 비교는 다음 순서로 진행한다. [선행 연구와 판별 기준](./work/research_topics/README.md#g1-load-release) · [공개 G1 모델](https://github.com/google-deepmind/mujoco_menagerie/blob/main/unitree_g1/README.md)

1. 현재 컴퓨터의 로컬 Docker와 G1 전신 제어 기준선을 확인한다. 최소 장면에서 손에 가해지는 힘, 발 접촉, 몸통 각속도를 기록할 수 있는지 점검한다.
2. 저항이 지속되는 시행과 풀리는 시행의 해제 직전 자세·당김 힘·거리를 맞춘다. 장면이 성립하면 CPU Docker에서 고정 자세 제어와 단순 순응·힘 상한을 비교한다.
3. 작업 시간과 해제 후 첫 300 ms의 몸통 각속도를 함께 비교한다. 단순 제어가 두 조건을 모두 만족하면 학습 방법 개발을 보류한다. 실물 검증 여부는 이 결과로 결정한다.

CORE 31편에 남은 공개 여부 55개는 새 배포 파일이나 저자의 공개 범위 명시가 확인되는 항목부터 갱신한다. ActiveZero 재검토 조건은 감독 손실·장면 분할·동일 관측 예산에 대한 원문 근거다. [논문별 대조 기록](./research/SOURCE_AUDIT.md#core-공개-자료) · [ActiveZero 보류 근거](./research/GAPFILL.md#activezero-보류-재검토)

## NVIDIA Docker 대기

| 주제 | 재개 시 첫 검증 |
|---|---|
| 조작용 3D 추정 | 고정 장면에서 깊이 입력에 개입해 정책 입출력을 확인한다. 학습·물리 정책 명령은 0회다. [재개 명령](./work/research_topics/task_geometry_estimation/재현%20방법/README.md#resume) |
| 능동 자세 추정 | 로컬 CUDA/EGL, 제한된 관측과 재채점을 확인한다. 정규화 자료 확보 전에는 물리 정책 명령을 실행하지 않는다. [재개 명령](./work/research_topics/pose_active_perception/재현%20방법/README.md#resume) |
| 접촉 관계 기반 탐색 | 데이터 로더·순기구학·접촉·재채점을 확인한다. 선택적 역전파 1회, optimizer 갱신 0회다. [재개 명령](./work/research_topics/relation_exploration/재현%20방법/README.md#resume) |

세 주제는 실행 준비 상태다. 직전 3D 추정 검사는 Docker daemon 단계에서 중단됐다. 재개할 컴퓨터에서 daemon·GPU·그래픽 지원과 입력 자료를 다시 확인한다. [전체 후보와 보존한 재현 경로](./work/research_topics/README.md#유지와-예비)

## 직전 완료

- 레지스트리 공통 검토 질문을 한곳에 모으고, 논문별 노트에는 원문 근거와 개별 판단을 남겼다. 한 논문의 모든 검색 태그와 별칭은 색인 한 행에서 볼 수 있다. [공통 검토 기준](./research/READING_STATUS.md#note-checks) · [논문 색인](./research/REGISTRY_INDEX.csv)
- 직전 원문 검토 범위는 *PhysTwin*부터 *Force Policy*까지 50편이다. 집중 읽기 500편 중 423편에 다축 태그가 있다. 공개 범위가 미확인인 필드와 교정 전 값은 배치 원장에서 조회한다. [직전 50편](./work/sources/batches/core_next_08.yaml) · [배치 전체](./work/update/REGISTRY.md#taxonomy-batches) · [원문 감사](./research/SOURCE_AUDIT.md)
