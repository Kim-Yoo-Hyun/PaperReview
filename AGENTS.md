# PaperReview 작업 규칙

이 규칙은 저장소 전체에 적용한다. 연구 작업은 [TODO](./TODO.md), 실측값과 한계는 [서랍 연구](./work/research_topics/instruction_revision/내용/README.md), 이미 종료한 설계의 재개 조건은 [이전 결과](./work/research_topics/RESULTS.md)에서 확인한다.

## 수정 위치

| 바꾸려는 내용 | 수정할 곳 |
|---|---|
| 논문 식별자·게재 상태·근거 | [논문 원장](./work/sources/papers.json)과 해당 논문의 노트. 신규 등록은 `work/scripts/register_papers.py`를 사용한다. |
| CORE/NEXT 선정·이유·순서 | [생성기](./work/scripts/build_reading_tiers.py)의 그룹과 논문별 근거. 생성한 읽기 계획·등급 CSV·색인을 함께 갱신한다. |
| 사용자 정독·분석 | [활성 읽기 기록](./research/READING_STATUS.csv)과 [이전 기록](./research/READING_STATUS_HISTORY.csv). 등급 이동·경로 변경 전후에 사용자가 쓴 필드를 대조한다. |
| 논문 간 비교·열린 질문 | [분야별 합성](./synthesis/README.md)의 수동 영역. `READING_QUEUE` 표시 사이의 목록은 생성기가 관리한다. |
| 연구의 결과·재현 | 주제별 `내용/README.md`에 질문·비교·해석을, `재현 방법/README.md`에 환경·명령·검사한 범위를 쓴다. 다음 행동은 TODO에 둔다. |
| 사용자가 처음 찾을 안내 | 루트 README에는 목적과 시작 경로를 둔다. 이 파일에는 작업 규칙과 실제 검증 명령을 둔다. |

## 문헌과 연구 판단

- VLA·RL·컴퓨터 비전·로보틱스를 로봇 행동에 연결한다. 실패 원인·신뢰성·복구, 단일 정책 내부의 학습을 우선 검토한다. 새 후보에는 문제 원인, 바꿀 변수, 행동 예측, 직접 선행 대비 차이와 석사 기간의 검증 비용을 적는다. [연구 설계](./research/RESEARCH_GUIDE.md)
- 최신 게재 상태·상·발표 연도는 공식 proceedings, publisher, OpenReview, 저자 자료 순으로 확인한다. 서베이와 공개 목록은 후보 발견에 쓴다. 논문을 추가하기 전 정규화한 제목·별칭·DOI·arXiv·OpenReview ID로 중복과 판본을 확인한다. 기존 안정 ID를 보존한다.
- 각 논문은 연도/행사/논문 폴더 하나와 표준 노트 다섯 개를 갖는다. 개요에 서지·출처·확인 범위를 두고 문제, 방법, 평가, 해석은 각 노트에 둔다. 직접 측정값과 연구자의 해석을 구분한다. 초록만 확인했으면 본문 근거가 필요한 수치는 보류한다. [노트 공통 기준](./research/READING_STATUS.md#note-checks)
- 중요도는 선행 의존성, 방법·제어 인터페이스, 평가로 판단한다. PDF는 사용자가 요청할 때만 내려받거나 삭제한다. 7개 트랙 중 하나를 주 트랙으로 선택한다. 교차 주제는 태그와 합성 링크로 표현한다. 사용자 정독 상태를 노트의 존재나 실험 실행만으로 변경하지 않는다.
- `SYNTHESIZED`에는 원문 위치와 분야별 비교·열린 질문이, `REPRODUCED`에는 실제 실행 근거가 필요하다. 작게 탐색할 조건과 연구 성과를 주장할 증거를 구분한다. [읽기 상태 규칙](./research/READING_STATUS.md)
- 기존 수정과 수작업 근거를 보존한다. 폴더를 통합할 때 상대 링크·앵커, 생성기 입력, 증거 해시와 재현 명령도 점검한다. 외부 공개·푸시는 사용자가 지정한 브랜치에서 수행한다.

## 실행 환경

시뮬레이션, 정책 추론·학습, 성능 측정, 해당 의존성 설치는 사용자가 선택한 컴퓨터의 로컬 Docker 안에서 수행한다. 재개할 때 endpoint·daemon·아키텍처·메모리, 필요한 GPU·CUDA·EGL, 모델과 자산 버전을 실제로 확인한다. 실험 근거에는 배치·자세·시드·시간·비교 단위와 저장 명령의 재생 조건을 적는다. [환경·명령·검산](./work/research_topics/instruction_revision/재현%20방법/README.md)

## 레지스트리 검증

저장소 루트에서 실행한다. 신규 등록은 먼저 `python3 work/scripts/register_papers.py --input <JSON>`으로 시험하고, 중복·원문·노트를 확인한 후 같은 명령에 `--apply`를 붙인다. 등급을 바꿀 때는 다음 순서로 파생 자료를 갱신한다.

```sh
python3 work/scripts/build_reading_tiers.py
python3 work/scripts/reconcile_registry.py --priorities-only --apply
python3 work/scripts/build_registry_views.py --apply
```

주요 변경 전후에 원장·등급·읽기 기록·노트·링크를 검사한다. 원문 감사의 분모와 검토 날짜는 당시 원장을 따른다. 원문 교정을 점검할 때는 별도로 `python3 work/scripts/render_source_audit.py --verify-corrections`를 실행한다.

```sh
python3 work/scripts/test_reading_history.py
python3 work/scripts/test_document_maintenance.py
python3 work/scripts/audit_repository.py
git diff --check
```
