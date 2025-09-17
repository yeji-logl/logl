# logl - 로컬 & 글로벌 연결 SNS
체류(예정)외국인의 현지적응 및 자립지원, 로컬 주민과의 연결

## 리포지토리 구조
```
/flutter_app   # Flutter 앱(모바일 및 웹)
/backend       # Django + DRF API 서버
/docs          # 아키텍처·API 명세·운영 핸드북
```

---

## Frontend (Flutter)
* **런타임**: Flutter Stable
* **라우팅**: `go_router`
* **상태관리**: `flutter_riverpod`
* **네트워킹**: `dio` (+ `interceptor` 토큰 자동 첨부)
* **모델/코드생성**: `freezed` 및 `json_serializable`
* **로컬 보안 저장소**: `flutter_secure_storage` (액세스/리프레시 토큰)
* **국제화(i18n)**: `flutter_localizations` 및 `intl` + `gen-l10n`
* **이미지 로딩**: `cached_network_image`
* **푸시 알림**: `firebase_messaging` (Android FCM 및 iOS APNs 브리지)
* **웹뷰/HTML 렌더**(옵션): `webview_flutter`, `flutter_html`
* **에러 리포팅**: `sentry_flutter`
* **테스트**: `flutter_test`(unit·widget·integration), `mocktail`
* **린트/포맷**: `dart_code_metrics`, `very_good_analysis`

---

## Backend (Django + DRF)
* **프레임워크**: Django LTS(예: 4.2) 및 **Django REST Framework**
* **인증**: `djangorestframework-simplejwt` (액세스/리프레시 토큰)
* **권한/스코프**: DRF `Permission` 및 커스텀 Permission 클래스
* **CORS/보안**: `django-cors-headers`, `django-axes`(옵션, 브루트포스 방지)
* **필터/페이지네이션**: `django-filter`, 키셋 페이지네이션 적용
* **스키마/문서**: `drf-spectacular` (OpenAPI 3, `/api/schema` 및 Swagger UI)
* **스토리지**: `django-storages[azure]`(Azure Blob) + `Pillow`(이미지)
* **업로드**: 서버 직업로드 및 사전 서명 URL(SAS) 기반 클라이언트 직업로드
* **비동기 작업**: `Celery` + `Redis`(broker 및 result backend), `celery-beat` 스케줄러
* **실시간(옵션)**: Azure Web PubSub SDK 또는 `channels` + `channels-redis`
* **검색**: PostgreSQL FTS + `pg_trgm`(Trigram) 인덱스, 필요 시 Azure AI Search 연동
* **지리 정보(옵션)**: PostGIS 및 거리/반경 질의
* **번역 파이프라인**: Azure Translator 호출 → Redis 캐시 → 영속화(번역 테이블)
* **메일**: SendGrid(Azure 마켓플레이스) 또는 SMTP 백엔드(프로바이더별 설정)
* **레이트리밋**: DRF Throttling 또는 `django-ratelimit`
* **관리자**: Django Admin 커스터마이징(모더레이션 워크플로)

---

## 캐시·큐·세션
* **Redis(Azure Cache for Redis)**: API 캐시 및 Celery 브로커, 레이트리밋 카운터
* **Django Cache**: Redis 백엔드
* **세션**: JWT 사용 시 서버 세션 미사용(관리자 사이트는 DB/캐시 세션)

---

## 관측성(Observability)
* **로그**: 구조화 로깅(JSON) → Azure Application Insights
* **트레이싱**: OpenTelemetry SDK(요청/DB/외부 API)
* **에러 추적**: Sentry(백엔드 및 Flutter 클라이언트)
* **메트릭**: App Insights(대시보드), 경보 룰(지연·오류율·큐 적체)

---

## CI/CD · 배포
* **CI**: GitHub Actions
  * **백엔드**: 테스트 → 린트(ruff/black) → 빌드(Docker buildx) → ACR 푸시
  * **플러터**: 분석 → 테스트 → 웹 번들 아티팩트(옵션) 및 스토어 빌드 워크플로
* **레지스트리**: Azure Container Registry(ACR)
* **런타임**:

  * **App Service for Containers**(간편) 또는 **AKS**(확장성)
  * 마이그레이션 단계: `python manage.py migrate` 작업 슬롯
* **정적/웹 번들**(옵션): Flutter Web 산출물을 Blob + CDN에 호스팅

---

## 데이터 모델·정책(핵심)
* **게시글**: soft delete 및 상태 플래그(활성·숨김·차단)
* **이미지**: 1\:N, 대표(primary) 1개 제약(조건부 유니크)
* **번역**: 원문 1개 및 언어별 번역 N개, 캐시 적중률 향상 전략
* **신고/모더레이션**: 워크플로 상태, 감사로그, 운영자 권한

---

## 코드 규칙·환경
* **백엔드 설정**: Twelve-Factor, `django-environ` 환경변수 주입
* **API 규칙**: `/api/v1/...` 버저닝, ISO8601 UTC 타임스탬프, 키셋 페이지네이션
* **테스트**:
  * 백엔드: `pytest`, `pytest-django`, 팩토리(`factory_boy`)
  * 프론트: unit/widget/integration 분리, 골든 테스트(옵션)

---

## 운영 체크리스트(요약)
* 비밀/키: Key Vault 반영 및 롤링
* DB 백업/복구: PITR 및 주기 점검
* 모니터링 경보: 에러율·응답시간·큐 적체·번역 호출 실패
* 보안 업데이트: 베이스 이미지 및 의존성 정기 갱신
* 데이터 보존: PII 최소수집 및 보존 주기, 익명화 정책

---

### 비고
* 디바이스 푸시: FCM(APNs 포함) 표준 사용
* 실시간 채팅/알림: 규모에 따라 Azure Web PubSub 또는 Channels 선택
* 이미지·동영상 처리 고도화: 썸네일 규격, WebP/AVIF, 지연 로딩, 원본 보호(SAS) 정책
