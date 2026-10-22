# VLA 방향 탐색 문서 검증

- 작업일: 2026-10-21 KST
- 범위: 문헌 조사·방향 제안·navigation 정합성. Policy experiment가 아니다.

## 변경 전

- `git status --short`로 기존 dirty tree를 확인하고 보존했다.
- `python3 work/scripts/audit_repository.py`: 974 papers, 4,870 notes, CORE 47 / NEXT 246 / REFERENCE 439 / ARCHIVE 242, errors 0 / warnings 0.
- 기존 paper note 4,870개와 registry·manifest·tier·active/history tracker 6개, 합계 4,876개 파일을 SHA-256 snapshot으로 보호했다.

## 변경 내용

- README, LITERATURE, D1_SENSOR_CONFLICT의 세 문서에 30편 source 대조·후보 비교·반증 설계를 작성했다.
- Root/work/synthesis navigation과 buildup guide의 최신 사례를 새 방향 탐색으로 연결했다.
- Reading plan은 generator의 설명만 수정하여 재생성한다. CORE/NEXT membership은 수정하지 않는다.
- 논문 admission, note overwrite, 사용자 정독 status 변경은 하지 않는다.

## 변경 후

- [x] `python3 -m py_compile work/scripts/build_reading_tiers.py`
- [x] `python3 work/scripts/build_reading_tiers.py`: CORE 47 / NEXT 246 / REFERENCE 439 / ARCHIVE 242 유지.
- [x] `python3 work/scripts/audit_repository.py`: Markdown 4,943개, 상대 링크 8,135개, errors 0 / warnings 0.
- [x] `git diff --check`: 통과.
- [x] 보호한 4,876개 파일 SHA-256 동일성 확인: 변경 0.
- [x] 문헌 표의 30편 / 공식 20편 / 보조 10편 / 기존 16편 / 외부 14편과 registry identity 대조: 정규화 title과 stable ID 불일치 0, 외부로 표기한 항목의 exact normalized-title 기존 entry 0.

## 실질적인 미확인 사항

- 모든 논문의 full-text 완독이나 모든 2024–2026 venue의 전수조사가 아니다.
- L10/L15는 공식 source의 검색 색인 근거이며 direct page 접근은 차단되었다. X09/X10의 저자 venue 표기는 공식 acceptance 검증으로 세지 않았다.
- D1 novelty·native runtime·clean competence·제안 정책 효과는 아직 검증하지 않았다.
- 실험·학습·Docker image pull·host 패키지 설치는 이번 작업에서 수행하지 않았다.
