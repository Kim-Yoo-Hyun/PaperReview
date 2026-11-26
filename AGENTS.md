# 레지스트리 작업 지침

이 지침은 저장소 루트와 하위 디렉토리에 적용한다. 작업을 시작할 때 `git status --short`와 [TODO](./TODO.md)를 확인하고 기존 수정과 사용자 읽기 기록을 보존한다. 다음 작업을 요청받으면 TODO의 재개 순서를 따른다.

연구 목표는 석사 과정에서 주요 로보틱스 학회·저널에 기여하는 것이다. 문제의 중요성, 가장 가까운 선행과의 차이, 로봇 행동의 변화, 구현·평가 부담을 함께 본다.

## 작업별 기준

| 작업 | 편집할 곳과 판단 기준 |
|---|---|
| 논문 조사·등록 | 공식 게재처, 저자 원문·배포처에서 서지와 공개 범위를 확인한다. 제목·별칭·DOI·arXiv·OpenReview ID로 중복을 확인하고 기존 게재본은 같은 `paper_id`로 갱신한다. [선정·출처 기준](./research/README.md#paper-admission) · [등록 명령](./work/README.md#registry-maintenance) |
| 등급·읽기 순서 | 후속 연구에 필요한 기반, 직접 비교할 방법·데이터·평가를 우선한다. 등급은 `build_reading_tiers.py`의 `CORE_GROUPS`·`NEXT_GROUPS`에서 변경하고 선정 이유를 남긴다. [등급과 읽기 순서](./research/READING_PLAN.md) |
| 논문 노트·비교 | 원문이 뒷받침하는 주장에 판본과 쪽·절·표를 붙이고 해석은 따로 표시한다. 정독 상태는 사용자의 실제 읽기 근거에 따라 바꾼다. [다섯 노트와 상태 규칙](./research/READING_STATUS.md#note-checks) · [일곱 트랙의 비교 규칙](./synthesis/README.md) |
| 연구 주제 탐색 | 조작·이동·전신 제어에서 답에 따라 달라질 로봇 행동, 가장 가까운 선행, 바꿀 변수와 경쟁 설명을 적는다. VLA·RL 결합에서는 단일 정책 내부 학습과 배포 시의 제어 구조를 구분한다. 3D 인식은 행동·복구에 주는 효과를 본다. [연구 설계](./research/RESEARCH_GUIDE.md) |
| 연구 결과·인계 | 후보별 질문·근거·한계는 `내용/README.md`, 환경·재개 명령·미구현 범위는 `재현 방법/README.md`에 둔다. 보류 재개에는 새 근거가 필요하다. 직전 결과와 다음 행동은 TODO에 연결한다. [현행 후보](./work/research_topics/README.md) · [종료·보류 결과](./work/research_topics/RESULTS.md) |

## 편집 규칙

- 논문 식별자·서지·출처의 원본은 [papers.json](./work/sources/papers.json)이다. 생성되는 목록·등급 CSV·통계는 원본과 생성기를 고친 뒤 재생성한다. 공개 링크와 검색 단서는 실험 재현의 증거와 구별한다.
- 1960–2010년 논문은 `1960-2010/<year>/`, 2011–2020년 논문은 `2011-2020/<year>/`, 그 밖의 연도는 루트의 `<year>/`에 둔다. 각 연도 아래 구조는 `<venue>/<year>_<venue>_<title-slug>/`와 표준 노트 5개다. 기존 경로의 대소문자와 `+`·유니코드 링크를 확인한다. `paper.pdf`는 선택적 로컬 캐시다. 다운로드·삭제는 사용자 요청이 있을 때만 하며 보유 여부를 선정이나 읽기 상태에 반영하지 않는다.
- Markdown 제목은 주제·역할을 나타내는 짧은 명사구, 공통 문서는 `UPPER_SNAKE_CASE.md`, 분야별 비교는 `NN_<short_topic>.md`, 후보 디렉토리는 `lower_snake_case`로 쓴다. 링크는 저장소 상대 경로로 작성한다. 통합한 문서의 참조와 생성기도 같이 고친다.
- 수동 수정에는 `apply_patch`를 우선한다. 수동 노트 전체 덮어쓰기, 기존 안정 ID 제거, 사용자 자산 삭제와 대량 이름 변경을 피한다. 읽기 이력은 활성·이전 CSV를 함께 보존한다. 비교 문서의 `READING_QUEUE` 마커 사이는 생성기가 관리한다.

## 로컬 Docker 실험

실험 준비·재개 요청을 받으면 문헌과 직접 경쟁 연구를 먼저 확인하고 **현재 컴퓨터의 로컬 Docker** endpoint·daemon, 아키텍처·메모리, 과제에 필요한 GPU·CUDA·그래픽·모델·자산을 점검한다. 시뮬레이션·추론·학습·성능 측정과 의존성 설치는 로컬 컨테이너 안에서만 수행한다.

- 조건이 맞으면 정한 최소 실행까지 진행한다. 조건이 부족하면 실패한 단계와 근거, 다른 컴퓨터에서 clone한 뒤 재개할 환경값·명령·남은 구현을 해당 후보에 기록한다.
- 호스트 Python/MPS·원격 GPU로 전환하거나 호스트에 패키지·가중치·자산을 설치하지 않는다. 준비된 것, 실제 실행 결과, 남은 조건을 구분하고 이 작업이 만든 임시 Docker 자산만 정리한다. [실험 준비와 인계](./work/experiments/README.md#local-docker)

## 완료 전 검증

저장소 루트에서 다음을 실행한다. 원장·등급·스키마·감사를 바꿨을 때의 추가 생성 명령은 [레지스트리 유지보수](./work/README.md#registry-maintenance)를 따른다.

```bash
python3 -m py_compile work/scripts/build_reading_tiers.py
python3 work/scripts/build_reading_tiers.py
python3 work/scripts/audit_repository.py
git diff --check
```

생성기 변경은 `python3 -m unittest discover -s work/scripts`로 검증한다. 변경한 범위, 검증 결과, 남은 불확실성이나 재개 조건을 보고한다.
