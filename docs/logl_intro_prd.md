# logl_intro_prd.md

## 1. 개요
인트로 화면 (앱 실행 시 최초 노출).  
브랜드 아이덴티티(logo, slogan)를 보여주고, 이후 로그인/회원가입 화면으로 전환.  
Backend(Django)와 Frontend(Flutter)의 역할을 분리하여 정의한다.

---

## 2. Django (Backend)

### 2.1 기능 요구사항
- 사용자 인증 및 세션 관리 API 제공
- 회원가입/로그인/토큰 갱신 API 지원
- 신규/기존 유저 여부 확인
- 보안 로깅 및 예외 처리

### 2.2 API 목록
- `POST /auth/signup` : 회원가입
- `POST /auth/login` : 로그인
- `POST /auth/refresh` : 토큰 갱신
- `GET /auth/check` : 세션 유효성 확인

### 2.3 데이터베이스 스키마
**users**
- id (PK)
- email
- password_hash
- nickname
- user_type (local/global)
- created_at
- updated_at

**user_sessions**
- id (PK)
- user_id (FK → users.id)
- access_token
- refresh_token
- expires_at

### 2.4 플로우
1. Flutter에서 로그인/회원가입 요청
2. Django가 DB 확인 후 토큰 발급
3. 세션 저장 및 상태 반환

---

## 3. Flutter (Frontend)

### 3.1 기능 요구사항
- 앱 실행 시 인트로 화면 출력
- 로컬 스토리지에서 토큰/세션 확인
- 토큰이 유효 → 홈 화면으로 이동
- 토큰이 없음/만료 → 로그인/회원가입 화면 이동

### 3.2 UI 요소
- 로고 + 슬로건 (중앙 배치)
- 배경 그래픽
- 자동 화면 전환 (3초 후)

### 3.3 로컬 저장소
**SharedPreferences / SecureStorage**
- access_token
- refresh_token
- user_id
- nickname
- user_type
- last_login

### 3.4 플로우
1. 앱 실행 → 인트로 화면 노출 (3초)
2. 로컬 저장된 토큰 확인
   - 유효 → `/auth/check` 호출 → 정상 → 홈 화면 이동
   - 없음/만료 → 로그인 화면 이동
