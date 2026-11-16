# 시연 저장소 확장 후보 — 자산 확인과 재개

2026-11-03 폴더 정리: 과거 실행 JSON의 명령·hash는 당시 기록을 유지한다. 현재 실행은 이 문서의 명령을 사용하고, 이전 경로는 [이동·병합 대응표](../../ORGANIZATION.json)에서 찾는다.

- Updated: 2026-11-02 KST
- 연구 질문·판단: [통합 buildup](../내용/README.md#retrieval-n1).
- 비교 기준: [COMPARISON_CONTRACT.json](COMPARISON_CONTRACT.json). 실제 결과: [ASSET_AUDIT.json](ASSET_AUDIT.json).
- **N1 내부 비실험 buildup 완료:** 직접 충돌·H/G/S/U 비교·반대 설명·제어/분할 설계·claim 경계를 정리했다. 정책 효과·성공/provenance·평가 중복·독립 피드백은 미검증이다.
- 현재 준비된 것은 **CPU Docker 자산 감사**다. Policy/embedding 실행, simulator, 성공률 비교, native P0는 준비 완료 상태가 아니다.

## 다른 컴퓨터에서 실행

이 디렉토리의 5개 파일을 포함한 revision을 전달한 뒤 clone한다. 현재 원격 게시 여부는 확인하지 않았으며 로컬 untracked 파일은 clone만으로 전달되지 않는다. 아래는 repository root 기준이다. Host에는 패키지·weights·시연을 설치하지 않는다.

```bash
sh "work/research_topics/context_retrieval/재현 방법/resume_assets.sh" check
sh "work/research_topics/context_retrieval/재현 방법/resume_assets.sh" audit
sh "work/research_topics/context_retrieval/재현 방법/resume_assets.sh" clean
```

`audit`는 고정된 Python 3.11.14 multi-architecture image와 standard library만 사용한다. ARM64/AMD64 **로컬** Linux Docker에서 CPU 2개·메모리 512 MiB로 실행한다. 인터넷 접근과 Docker 저장 공간이 필요하다. Remote endpoint와 emulation은 사용하지 않는다. 필요한 이미지만 Docker에 pull하며 별도 pip/apt 설치는 없다.

12,840,960-byte archive를 Docker volume `paper-retrieval-a1-assets`의 `/scratch/demo_pack.tar`에 저장하고 SHA-256 확인 후 tar 안에서 읽는다. Filesystem으로 extract하지 않는다. 결과는 metadata/hash/판정 JSON으로 stdout에 출력된다. 현행 `ASSET_AUDIT.json`을 자동 덮어쓰지 않는다. `clean`은 label을 확인한 이 volume만 지운다. 기존 image/다른 volume은 보존한다.

선택한 첫·마지막 frame을 확인해야 할 때 `clean` 전에 `preview`를 사용할 수 있다. 출력은 base64 image JSON이며 repository에 redirect하지 않는다. 반복 문헌 작업을 위해 동일 preview를 다시 생성할 필요는 없다.

```bash
sh "work/research_topics/context_retrieval/재현 방법/resume_assets.sh" preview
```

## 확인된 범위

40개 pool 각각 시연 1개, payload 40개, referenced PNG 261개의 경로·header·hash·ID join을 검사했다. Byte-identical 중복은 없었다. 이것은 trajectory·평가 split 중복 배제와 다르다. 목표 시연은 `libero_goal#0`, `libero_goal#19`, donor는 `libero_goal#1`이며 각각 8·5·6 frame이다. 선택된 첫/마지막 6개 이미지만 수동 시각 확인했다. 성공 predicate·물체 release·원 trajectory provenance는 미확인이다.

2026-11-02 현재 local Docker는 ARM64·약 7.65 GiB이며 GPU allocation은 exit 125였다. **이 실패가 CPU 자산 감사를 막지는 않았지만, StellaVLA 추론을 확인한 것은 아니다.** Archive는 감사 후 전용 volume과 함께 삭제했고 이번에 pull한 Python image 참조도 제거했다. 기존 사용자 image는 보존했다.

## 다음 native 준비

[비교 계약의 `native_resume_requirements`](COMPARISON_CONTRACT.json)에 공개 recipe의 Python/torch/transformers·LIBERO/MuJoCo 설정, source/checkpoint/encoder/base-VLM revision, mount와 남은 검증을 기록했다. 해당 설정은 아직 빌드되지 않았다. CUDA base tag만으로 driver 호환성이나 GPU 메모리 충분성을 판정하지 않는다.

호환 Linux x86-64/NVIDIA local Docker에서 다음을 순서대로 진행한다.

1. 현 endpoint·daemon·GPU allocation·driver/torch CUDA·EGL과 여유 메모리를 확인한다. 기존 준비 후보의 실행 우선순위는 REVISION이다.
2. StellaVLA의 LIBERO-only image와 고정 package lock을 준비한다. 공개 전체 Dockerfile은 불필요한 LIBERO-plus/VLA-Arena까지 받으므로 그대로 큰 다운로드를 시작하지 않는다.
3. 고정 weight·normalizer·Qwen processor·DINOv2를 Docker `/data` volume에 확보하고 local hash를 검증한다. 실제 prefix token 수와 truncation, current RGB 방향/전처리를 확인한다. Frame ceiling 8·전체 입력 2,200-token guard는 설계값이다. 실제 processor가 모든 입력을 잘리지 않게 처리하는지는 미검증이다.
4. 별도의 작은 IO/cache 검증용 adapter와 실행 manifest를 만든다. H/G/S/U 선택·prefix 교체·queue 초기화·동일 reset snapshot을 확인한 후에만 연구 비교를 검토한다. 첫 비교는 optional prefix KV를 끄고 full forward로 설계했다. 현재 최대 24개 고유 rollout/64개 논리 칸을 실행하는 명령은 제공하지 않는다.

실제 시연 성공과 평가 데이터 중복은 원 trajectory/evaluator 근거가 필요하다. Manifest의 `ep_idx`를 benchmark initial-state 번호로 쓰지 않는다. 자산 감사의 exit 0이나 GPU 확보만으로 이 조건들이 해결되지는 않는다.

제어·분할 값은 계약의 `protocol_design`이 소유한다. Settling 10회 후 최대 300 policy step·20 Hz·8-action chunk, seed 7, 각 task init slot 0 dev/1–4 서술적 비교를 지정했다. 이는 실행 확인이나 학습-disjoint split 인증이 아니다. 같은 자산 감사를 재실행하기보다 실제 image/adapter·초기 상태·입력 검증을 진행한다.
