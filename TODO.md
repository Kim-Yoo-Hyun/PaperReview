# 다음 작업

## 재개 순서

**다음 원장 감사.** CORE 36편에 남은 코드·가중치·데이터 공개 여부 68개 항목을 대조한다. 논문별 원장에서 이미 확인한 배포처와 빠진 근거를 먼저 보고, 저자가 배포한 파일이나 명시한 공개 범위를 찾은 항목부터 갱신한다. DeXtreme의 최종 저자열은 ICRA 게재본 인쇄 5977쪽을 확보할 때 대조한다. [공개 자료와 저자 판본](./research/SOURCE_AUDIT.md#core-공개-자료)

**다음 연구 작업은 G1이 걸쇠를 당기다가 저항이 갑자기 사라질 때 균형을 유지하는지 시뮬레이션에서 확인하는 것이다.** 후보 4의 첫 비교는 다음 순서로 진행한다. [선행 연구와 판별 기준](./work/research_topics/README.md#g1-load-release) · [공개 G1 모델](https://github.com/google-deepmind/mujoco_menagerie/blob/main/unitree_g1/README.md)

1. 현재 컴퓨터의 로컬 Docker와 G1 전신 제어 기준선을 확인한다. 최소 장면에서 손에 가해지는 힘, 발 접촉, 몸통 각속도를 기록할 수 있는지 점검한다.
2. 저항이 지속되는 시행과 풀리는 시행의 해제 직전 자세·당김 힘·거리를 맞춘다. 장면이 성립하면 CPU Docker에서 고정 자세 제어와 단순 순응·힘 상한을 비교한다.
3. 작업 시간과 해제 후 첫 300 ms의 몸통 각속도를 함께 비교한다. 단순 제어가 두 조건을 모두 만족하면 학습 방법 개발을 보류한다. 실물 검증 여부는 이 결과로 결정한다.

**다음 원장 작업**은 미처리 CORE 20편과 NEXT 30편의 다축 태그 정규화다. 첫 배치에서 가중치 30편과 데이터 27편은 배포 범위가 미확인이다. 저자의 공개 자료를 확인한 항목부터 갱신한다. ActiveZero 재검토 조건은 감독 손실·장면 분할·동일 관측 예산에 대한 원문 근거다. [정규화 기준](./work/update/REGISTRY.md#첫-배치-태그-매핑) · [ActiveZero 보류 근거](./research/GAPFILL.md#activezero-보류-재검토)

## NVIDIA Docker 대기

| 주제 | 재개 시 첫 검증 |
|---|---|
| 조작용 3D 추정 | 고정 장면에서 깊이 입력에 개입해 정책 입출력을 확인한다. 학습·물리 정책 명령은 0회다. [재개 명령](./work/research_topics/task_geometry_estimation/재현%20방법/README.md#resume) |
| 능동 자세 추정 | 로컬 CUDA/EGL, 제한된 관측과 재채점을 확인한다. 정규화 자료 확보 전에는 물리 정책 명령을 실행하지 않는다. [재개 명령](./work/research_topics/pose_active_perception/재현%20방법/README.md#resume) |
| 접촉 관계 기반 탐색 | 데이터 로더·순기구학·접촉·재채점을 확인한다. 선택적 역전파 1회, optimizer 갱신 0회다. [재개 명령](./work/research_topics/relation_exploration/재현%20방법/README.md#resume) |

세 주제는 실행 준비 상태다. 직전 3D 추정 검사는 Docker daemon 단계에서 중단됐다. 재개할 컴퓨터에서 daemon·GPU·그래픽 지원과 입력 자료를 다시 확인한다. [전체 후보와 보존한 재현 경로](./work/research_topics/README.md#유지와-예비)

## 직전 완료

- **11월 24일 수식·그림 전사 교정.** 10편의 노트 31개에서 91줄을 원문과 대조했다. 전체 표준 노트 6,260개를 다시 검색한 결과 글꼴 전용 문자와 유니코드 대체 문자는 0개였다. TD-MPC2의 문제 정의와 평가 노트에서도 잠재 공간 계획과 단일 과제 지표를 바로잡았다. [교정과 원문 위치](./research/SOURCE_AUDIT.md#노트의-수식과-도식)
- **11월 24일 요약·기여 전수 대조 완료.** ARCHIVE 마지막 98편(*SR3R*~*LangRef3DGS*)의 요약 98개와 기여 196개를 게재본에 연결했다. 저자 표기·순서 12편, 학회 웹 서지와 인쇄 제목이 다른 2편을 반영했다. 평가 노트 49편 중 40편에서 평가 유형을 바로잡고 17편에 원문의 수치·조건을 명시했다. 전체 1,252편이 요약·기여 항목을 통과했다. [배치 원장](./research/SOURCE_AUDIT.md#요약기여-원문-대조) · [판본 교정](./work/update/REGISTRY.md#note-review)
- **시연의 선택적 재수집.** 네 원격조작 자료를 대조했다. 원래 요청을 복원할 수 없으면서 같은 작업에서 가이드 방향만 바꿔 재시연할 수 있는 표본이 확보될 때까지 파일럿을 보류한다. [결과](./work/research_topics/demonstration_recollection/내용/README.md) · [공개 표본 재검산](./work/research_topics/demonstration_recollection/재현%20방법/README.md)
- **레지스트리.** 공유 제어 원문 2편을 등록하고 DROID 공개 자료를 교정했다. 기존 23편의 등록 판정과 이전 실험의 수치·재개 조건은 각 결과 문서에서 확인할 수 있다. [등록과 교정](./work/update/REGISTRY.md) · [누락 심사](./research/GAPFILL.md) · [종료·보류 결과](./work/research_topics/RESULTS.md)
