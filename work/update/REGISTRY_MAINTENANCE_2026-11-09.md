# Registry 최신화·접촉 직접 선행 등록·중복 정리

- Work ID: **REG-R13** / 2026-11-09 KST
- 범위: 전체 로컬 registry의 identity·분류·노트·링크·생성 view 정합성과 최근 접촉 적응 검토의 미등록 직접 선행 10편. 전체 1,171편의 최신 게재·본문을 인터넷으로 전수 재조사한 것은 아니다.
- [등록 입력](../sources/registry_admissions_2026-11-09.json) · [정리·보존·검증 원장](../sources/registry_maintenance_2026-11-09.json) · [현재 TODO](../../TODO.md)

<a id="admissions"></a>

## 추가한 직접 선행

| 논문·registry ID | 확인한 상태 | 분류·등록 이유 |
|---|---|---|
| [TacCoRL, pr-1162](../../2026/arXiv/2026_arXiv_TacCoRL-Integrating-Tactile-Feedback-into-VLA-via-Simulati/01_overview.md) | [arXiv 2026](https://arxiv.org/abs/2606.11743) | NEXT · 촉각 VLA 자체의 simulation RL 기준선 |
| [CompVLA, pr-1163](../../2026/arXiv/2026_arXiv_CompVLA-A-Variable-Compliance-Vision-Language-Action-Model/01_overview.md) | [arXiv 2026](https://arxiv.org/abs/2609.23614) | NEXT · 동작·강성 공동 생성의 직접 선행 |
| [TORL-VLA, pr-1164](../../2026/arXiv/2026_arXiv_TORL-VLA-Tactile-Guided-Online-Reinforcement-Learning-for/01_overview.md) | [arXiv 2026](https://arxiv.org/abs/2606.09337) | NEXT · 접촉 online RL·개입 경계의 직접 선행 |
| [ForceRFT, pr-1165](../../2026/arXiv/2026_arXiv_ForceRFT-Refining-VLA-Actions-through-Force-Guided-Residua/01_overview.md) | [arXiv 2026](https://arxiv.org/abs/2609.22840) | NEXT · Force residual RL과 imitation 대조 |
| [FORGE, pr-1166](../../2025/RA-L/2025_RA-L_FORGE-Force-Guided-Exploration-for-Robust-Contact-Rich-Man/01_overview.md) | [RA-L 2025](https://api.crossref.org/works/10.1109/LRA.2025.3551637) | NEXT · 강한 비-VLA 접촉 RL 대안 |
| [ContactBench 1.0, pr-1167](../../2026/arXiv/2026_arXiv_ContactBench-1.0-A-Benchmark-for-Everyday-Contact-Rich-Rob/01_overview.md) | [arXiv 2026](https://arxiv.org/abs/2610.24512) | NEXT · 접촉 task·물리 변화·simulation asset 기준 |
| [Facet-0, pr-1168](../../2026/arXiv/2026_arXiv_Facet-0-A-Robotic-Foundation-Model-for-Contact-Rich-Precis/01_overview.md) | [arXiv 2026](https://arxiv.org/abs/2609.01596) | NEXT · Action–wrench 가치·적응 선행 |
| [CG-RL, pr-1169](../../2026/arXiv/2026_arXiv_Constraint-Grounded-Reinforcement-Learning-for-Variable-Im/01_overview.md) | [arXiv 2026](https://arxiv.org/abs/2609.13516) | REFERENCE · 동작·gain 공동 RL의 controller 대안 |
| [CompliantVLA-adaptor, pr-1170](../../2026/arXiv/2026_arXiv_CompliantVLA-adaptor-VLM-Guided-Variable-Impedance-Action/01_overview.md) | [arXiv 2026](https://arxiv.org/abs/2601.15541) | REFERENCE · VLM/context·force 기반 controller 대안 |
| [πRL, pr-1171](../../2025/arXiv/2025_arXiv_piRL-Online-RL-Fine-tuning-for-Flow-based-Vision-Language/01_overview.md) | [arXiv 2025](https://arxiv.org/abs/2510.25889) | NEXT · Flow-SDE/Flow-Noise likelihood backend |

FORGE의 RA-L 2025 게재는 [IEEE-deposited DOI metadata](https://api.crossref.org/works/10.1109/LRA.2025.3551637)와 [저자 연구실](https://research.nvidia.com/labs/srl/publication/noseworthy-2025-forge/)로 확인했다. IEEE paper endpoint는 HTTP418로 직접 접근하지 못했다. 2024 preprint와 별도 논문으로 중복 등록하지 않았다.

나머지 9편은 arXiv로 등록한다. TacCoRL·CompVLA의 저자 페이지는 CoRL 2026을 표기하지만 이번 확인에서 공식 proceedings/forum을 확보하지 못했으므로 공식 게재로 승격하지 않는다. πRL은 최초 공개 연도 2025를 사용하며 최신 v3는 2026년이다. RLinf-VLA 시스템 논문과 다른 identity다.

신규 10편은 각각 5개 표준 노트와 provenance를 갖는다. **NEXT8·REFERENCE2**, 새 노트는 **ABSTRACT_CHECKED**, 신규 집중 읽기 8건은 **UNREAD**다. CG-RL·CompliantVLA-adaptor는 controller 대안 REFERENCE로 둔다. 제목·정규화 표기·arXiv·DOI 중복 dry-run에서 충돌은 없었다. 기존 논문의 tier·사용자 읽기 기록은 변경하지 않았다.

## 근거 경계와 후속

현재 [접촉 적응 N1/N2](../research_topics/contact_adaptation/내용/README.md)는 지정 버전·절의 본문/code 대조다. CompVLA 최신 v2와 TORL-VLA 최신 v3의 초록을 확인했지만 N1의 v1 본문 대조를 최신 버전 정독으로 승격하지 않는다. P1/신규성 주장 전 버전 간 방법·평가 변경을 확인해야 한다.

CompVLA의 code 링크는 404였다. TORL-VLA는 code Coming Soon이며 연결된 RLT 재현 repository를 TORL 구현으로 기록하지 않았다. FORGE도 code Coming Soon이다. CompliantVLA-adaptor는 anonymous code 공개를 주장하나 구체적 URL은 이번 확인에서 식별하지 못했다. ContactBench의 simulation asset 공개, FACET·RLinf 코드 존재는 native 재현 성공을 뜻하지 않는다.

이 등록으로 접촉 이력·단일 VLA RL·동작/강성 공동 생성·action–wrench 가치 학습이 각각 선행에 있음을 registry에서 추적할 수 있다. **현재 후보의 독립 방법 기여는 미확립**이며 좁은 비교 탐색과 기존 P0-A 자원·구현 대기를 유지한다.

## 삭제·병합·문서 정리

- UNIFIED의 2026-11-06 제어 검사에서 분리돼 있던 `tests.log`와 `execution.json` **2개**를 기존 [control_tests.json](../research_topics/unified_vla_rl/재현%20방법/results/2026-11-06-preparation/control-tests/control_tests.json)에 병합한 뒤 제거했다. Raw test log, image ID, exit code, cleanup 여부와 원래 SHA256·크기를 보존했다. 당시 15개 검사의 결과이며 이번 재실행이나 CUDA 검증이 아니다.
- 비어 있는 `tmp/pdfs`·`tmp` 디렉토리를 제거했다. 논문 PDF·노트·source review manifest·재현 입력은 삭제하지 않았다.
- TODO의 반복 완료 이력은 기존 update index로 연결하고 최신 완료·현재 대기·문헌 후속을 남겼다. 아래 조건부 실행 계약은 그대로 보존했다. Root/research/work/synthesis 안내, 현행 snapshot과 AGENTS의 현재 수량을 맞췄다. 과거 cohort 수치는 소급 변경하지 않았다.
- 동일한 `.dockerignore`는 서로 다른 Docker build context에 필요해 각각 보존했다. 두 navigation 실행의 동일한 `docker_version.json`도 각각의 역사적 증거다. 동결된 launcher·requirements·환경 pin은 임의 공통화하지 않았다.
- 호스트 패키지·의존성 설치/삭제, Docker 실행, PDF·weights 다운로드, git commit/push는 수행하지 않았다. 기존 dirty/staged 작업을 유지했다.

## 현행 규모와 검증

전체 **1,171편·표준 노트5,855개**, **CORE47 / NEXT380 / REFERENCE502 / ARCHIVE242**, active427 / history47이다. Source evidence는 FULL_TEXT_CHECKED967 / ABSTRACT_CHECKED204다. 새 등록 노트만 초록 근거이며 사용자 READ 기록 5편은 그대로다.

등록 dry-run/apply, tier 생성기 compile/rebuild, priority-only reconcile과 catalog/resource/index/stats 재생성을 완료했다. 읽기 이력 검사 **6개 통과**, `git diff --check` 통과, 전체 audit는 **오류0 / 경고0**이다. Markdown6,078개·내부 링크12,952개를 확인했다. 새 ContactBench tag의 대소문자를 기존 `Benchmark`에 맞춘 뒤 재검증했다.

기존 paper metadata **1,161편**, 표준 노트 **5,805개**, 사용자 읽기 입력 **466건**은 유지했고 신규 집중 읽기 **8건**만 UNREAD로 추가했다. 주제별 재현 자료와 과거 실험 파일 **222개**를 비교하여 위 결과 병합 이외 변경이 없음을 확인했다. 기존 staged patch도 byte-identical이다. 제거한 두 source 파일 총2,008bytes는 통합 JSON에서 원래 byte/hash로 복원된다. 이는 파일 수 정리이며 디스크 절감이나 실험 검증 성과를 뜻하지 않는다.

다음 연구 행동은 [CONTACT-RL-P0-A](../../TODO.md)의 호환 local NVIDIA 검증이다. 이번 registry 정리로 native 실행·연구 효과·출판 가능성을 입증한 것으로 판단하지 않는다.
