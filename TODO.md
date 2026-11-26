# 다음 작업

## 재개 순서

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

- 접촉·전신 제어, 조작 복구, 내비게이션의 비교 기준 14편을 REFERENCE에 등록했다. G1 걸쇠 해제 검증에는 GentleHumanoid와 FLoRe의 힘·순응 제어 범위를 대조했다. [신규 논문과 선정 근거](./work/update/REGISTRY.md#reg-contact-nav) · [G1 선행 비교](./work/research_topics/README.md#g1-load-release)
- 논문 폴더·표준 노트·문서 링크·생성 색인을 원장과 대조했다. 검색 단서 794편을 동기화하고 PDF 실패 로그를 제거했다. π₀ 프로젝트 주소와 PointWorld PDF 필드를 교정했고, 링크 미확인 논문은 36편에서 26편으로 줄었다. [구조 검증](./work/update/REGISTRY.md#구조-검증)
- ARCHIVE 마지막 31편을 원문과 대조해 표시 태그 22편과 검색 필터 30편을 수정했다. 감사 당시 ARCHIVE 242편과 11월 감사 대상 전체 1,252편의 태그 검토를 완료했다. [ARCHIVE 감사 결과](./research/SOURCE_AUDIT.md#archive-검색-태그) · [전체 항목별 판정](./research/SOURCE_AUDIT.md#항목별-결과)
- 2020년까지의 논문 148편을 두 기간 폴더로 옮기고 읽기 이력과 노트 경로를 연결했다. [기간별 탐색](./README.md#수록-현황)
- NEXT 마지막 27편을 분류하고, 이전 배치에서 검색 태그 판정이 남았던 20편도 원문과 대조했다. 집중 읽기 500편의 다축 분류와 검색 태그 검토를 마쳤다. 접촉 제어 비교에 쓰는 논문 네 편은 REFERENCE에 등록했다. [마지막 27편](./work/sources/batches/core_next_10.yaml) · [접촉 제어 논문](./research/VLA_ACTION_SPACE.md#추가-조사)
- VLA 28편에서 접촉력·강성·감쇠, 관절 명령, 전신 균형, 이동·태스크 전환을 비교하고 10편을 REFERENCE에 등록했다. 실물에서 힘과 이동을 함께 검토할 때에는 Opt2VLA가 결정하는 목표 법선력과 별도 RL 제어기가 결정하는 관절 명령을 구분한다. [논문별 배포·평가 비교](./synthesis/04_vla.md#vla-action-interfaces)
- [문헌 안내](./research/README.md)에 선정·출처 기준을 모으고 [외부 목록 대조와 누락 심사](./research/GAPFILL.md)를 통합했다. [색인](./research/REGISTRY_INDEX.csv)에는 태그·별칭과 정독 500편의 등급 내 순서가 함께 나온다. 논문별 노트의 [공통 검토 기준](./research/READING_STATUS.md#note-checks)은 그대로 참조할 수 있다.
