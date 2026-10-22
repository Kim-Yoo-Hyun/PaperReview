# C6 공개 자료 식별 gate

- 고정일: 2026-10-21 KST, 공개 payload 검사 전.
- 범위: C5 보류를 유지하고 C6의 문헌·데이터 전제를 심사한다. 새 selection method의 효과 실험이 아니다.

## 먼저 확인할 조건

1. 같은 native VLA의 RL run과 checkpoint 순서가 식별되는가? 서로 다른 architecture나 BC checkpoint를 RL update로 부르지 않는다.
2. Checkpoint × task × 개별 시행의 outcome, trial/seed ID, 평가 조건과 비용이 연결되는가?
3. 학습 reward와 평가 score의 모델/version/training provenance가 있는가? 둘의 공유 여부를 모르면 shared blind spot을 검증했다고 할 수 없다.
4. Selector가 볼 평가와 독립 reference 평가를 분리할 수 있는가? 집계 success만으로 paired outcome이나 숨겨진 trial sequence를 만들지 않는다.
5. 공개 code는 실제 estimator/selector인가, project website인가? Commit을 고정한 source 검사와 upstream 실행을 구분한다.

## 이번에 허용하는 계산

공식 code link의 접근 상태, git tree와 bounded text source, RACE의 공개 JSON schema·record 수·개별 시행 필드 유무를 검사한다. 원본 payload는 Docker 내부에만 둔다. Host에는 작은 provenance/구조 요약과 검사 script만 남긴다. Script는 Python 표준 라이브러리만 사용하고 upstream code를 import/실행하지 않는다.

Raw outcomes가 확인되지 않으면 sequential selection, bootstrap 성능 비교, 성공률 재현을 수행하지 않는다. 평균에서 Bernoulli sample을 생성해 실제 로봇 데이터로 주장하지 않는다. 작은 schema 검사로 VLA·RL native runtime이 검증되었다고 하지 않는다.

## 통과 후에도 필요한 조건

Frozen checkpoint 집합의 ranking 오류만으로 RL이 evaluator를 이용했다고 인과 해석하지 않는다. Training reward/evaluator의 독립성에 대한 controlled contrast 또는 그에 준하는 로그가 필요하다. Registry·tier·사용자 reading status는 이 검토로 승격하지 않는다.
