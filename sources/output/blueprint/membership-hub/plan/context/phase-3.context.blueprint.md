# PHASE 3 CONTEXT BLUEPRINT: membership-hub
## 1. Phase Operational Scope & Objectives
- **Primary Goal**: Deliver a fully functional web and mobile front‑end using Next.js that supports:
  - Multi‑language (English & Vietnamese) with locale detection and fallback.
  - SEO‑optimized pages (meta tags, OpenGraph, structured data).
  - Drag‑and‑drop upload for admin (Excel/CSV only).
  - Responsive design for iOS/Android via the same Next.js codebase.
  - Basic routing for admin, student, teacher, and public pages.
- **Deliverables**:
  - `./sources/frontend/` Next.js project with pages, components, i18n, SEO, and mobile build scripts.
  - Unit and integration tests covering core UI components and locale logic.
  - Dockerfile and CI/CD pipeline snippets for frontend deployment.

## 2. Allowed Technical Scope & Directory Boundaries
| Layer | Path Prefix | Example | Notes |
|-------|-------------|---------|-------|
| **Source** | `./sources/frontend/src/` | `./sources/frontend/src/pages/index.tsx` | All TypeScript/React source files. |
| **Components** | `./sources/frontend/src/components/` | `./sources/frontend/src/components/Header.tsx` | Reusable UI pieces. |
| **i18n** | `./sources/frontend/src/locales/` | `./sources/frontend/src/locales/en/common.json` | Translation files. |
| **Mobile** | `./sources/frontend/mobile/` | `./sources/frontend/mobile/pages/index.tsx` | Mobile‑specific Next.js pages. |
| **Config** | `./sources/frontend/` | `./sources/frontend/package.json`, `./sources/frontend/next.config.js` | Project configuration. |
| **Tests** | `./sources/frontend/src/__tests__/` | `./sources/frontend/src/__tests__/Header.test.tsx` | Jest unit tests. |
| **Docker** | `./sources/frontend/` | `./sources/frontend/Dockerfile` | Build image for GCP. |

## 3. Dedicated Sub‑Agent Functional Directives
| Sub‑Agent | Responsibility | Key Actions |
|-----------|----------------|-------------|
| **Coder** | Implement all source files, configuration, and Dockerfile. | Create pages, components, i18n, SEO, mobile build scripts. |
| **Tester** | Write unit and integration tests. | Pair source and test files, use `INTEGRATION_SCOPE` for multi‑component tests. |
| **Reviewer** | Static analysis, code quality, guardrail compliance. | Verify no nested loops over large tables, enforce package‑to‑path mapping. |
| **DevOps** | Configure Docker, CI/CD, and deployment scripts. | Write Dockerfile, GitHub Actions snippets, GCP deployment manifests. |

## 4. Phase Definition of Done (DoD)
- All pages compile without errors (`npm run build`).
- Unit tests pass (`npm test`).
- Integration tests for locale detection and upload component pass.
- Docker image builds successfully and can be pushed to GCR.
- CI pipeline triggers on push to `main` and deploys to GKE.
- All code passes Reviewer static analysis and guardrail checks.

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: Project Bootstrap & Core Pages

#### SUB‑TASK [1.1]: Initialize Next.js Project & Core Pages  
##### Assigned Sub‑Agent: Coder  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/package.json`  
  * **Architectural Requirements:**  
    * Define scripts (`dev`, `build`, `start`, `test`).  
    * Add dependencies: `next`, `react`, `react-dom`, `typescript`, `@types/react`, `i18next`, `react-i18next`, `next-i18next`, `next-seo`, `tailwindcss`, `postcss`, `autoprefixer`.  
* **Target Path:** `./sources/frontend/next.config.js`  
  * **Architectural Requirements:**  
    * Enable i18n with locales `en`, `vi`.  
    * Configure `publicRuntimeConfig` for API base URL.  
* **Target Path:** `./sources/frontend/src/pages/index.tsx`  
  * **Architectural Requirements:**  
    * Render a simple landing page with SEO meta tags.  
* **Target Path:** `./sources/frontend/src/components/Header.tsx`  
  * **Architectural Requirements:**  
    * Navigation bar with locale switcher.  
* **Target Path:** `./sources/frontend/src/components/Footer.tsx`  
  * **Architectural Requirements:**  
    * Footer with static links.  

#### SUB‑TASK [1.2]: Create Basic i18n Configuration  
##### Assigned Sub‑Agent: Coder  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/next-i18next.config.js`  
  * **Architectural Requirements:**  
    * Configure namespaces, default language, and fallback.  
* **Target Path:** `./sources/frontend/src/locales/en/common.json`  
  * **Architectural Requirements:**  
    * Provide English translations for common UI strings.  
* **Target Path:** `./sources/frontend/src/locales/vi/common.json`  
  * **Architectural Requirements:**  
    * Provide Vietnamese translations for common UI strings.  

#### SUB‑TASK [1.3]: Dockerfile for Frontend  
##### Assigned Sub‑Agent: DevOps  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/Dockerfile`  
  * **Architectural Requirements:**  
    * Multi‑stage build: `node:18-alpine` for build, `nginx:1.23-alpine` for serving.  
    * Expose port `80`.  

#### SUB‑TASK [1.4]: Unit Test for Header Component  
##### Assigned Sub‑Agent: Tester  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/src/components/Header.tsx;./sources/frontend/src/__tests__/Header.test.tsx`  
  * **Architectural Requirements:**  
    * Verify locale switcher renders both `en` and `vi`.  
    * Assert navigation links exist.  

#### SUB‑TASK [1.5]: Reviewer Static Analysis  
##### Assigned Sub‑Agent: Reviewer  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/package.json`  
* **Target Path:** `./sources/frontend/next.config.js`  
* **Target Path:** `./sources/frontend/src/pages/index.tsx`  
* **Target Path:** `./sources/frontend/src/components/Header.tsx`  
* **Target Path:** `./sources/frontend/src/components/Footer.tsx`  

---

### DAY 2: Admin Upload UI & Validation

#### SUB‑TASK [2.1]: Drag‑and‑Drop Upload Component  
##### Assigned Sub‑Agent: Coder  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/src/components/UploadZone.tsx`  
  * **Architectural Requirements:**  
    * Accept only `.xlsx` and `.csv`.  
    * Show preview of selected file name.  
    * Emit `onFileSelect` event.  

#### SUB‑TASK [2.2]: Admin Upload Page  
##### Assigned Sub‑Agent: Coder  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/src/pages/admin/upload.tsx`  
  * **Architectural Requirements:**  
    * Render `UploadZone`.  
    * Submit button triggers API call to `/api/admin/upload`.  

#### SUB‑TASK [2.3]: Unit Test for UploadZone  
##### Assigned Sub‑Agent: Tester  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/src/components/UploadZone.tsx;./sources/frontend/src/__tests__/UploadZone.test.tsx`  
  * **Architectural Requirements:**  
    * Verify file type validation.  
    * Verify event emission.  

#### SUB‑TASK [2.4]: Reviewer Code Review  
##### Assigned Sub‑Agent: Reviewer  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/src/components/UploadZone.tsx`  
* **Target Path:** `./sources/frontend/src/pages/admin/upload.tsx`  

---

### DAY 3: Locale Detection & SEO Enhancements

#### SUB‑TASK [3.1]: Locale Detection Middleware  
##### Assigned Sub‑Agent: Coder  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/src/middleware/locale.ts`  
  * **Architectural Requirements:**  
    * Detect `Accept-Language` header, cookie, or query param.  
    * Set locale cookie with 30‑day expiry.  

#### SUB‑TASK [3.2]: SEO Meta Component  
##### Assigned Sub‑Agent: Coder  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/src/components/SEO.tsx`  
  * **Architectural Requirements:**  
    * Accept `title`, `description`, `canonical`, `openGraph` props.  
    * Use `next-seo` library.  

#### SUB‑TASK [3.3]: Integration Test for Locale Detection  
##### Assigned Sub‑Agent: Tester  
##### Targeted Components & Technical Requirements:
* **Target Path:** `INTEGRATION_SCOPE;./sources/frontend/src/middleware/locale.ts`  
  * **Architectural Requirements:**  
    * Simulate requests with different `Accept-Language` headers and verify cookie set.  

#### SUB‑TASK [3.4]: Reviewer SEO & Locale Review  
##### Assigned Sub‑Agent: Reviewer  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/src/middleware/locale.ts`  
* **Target Path:** `./sources/frontend/src/components/SEO.tsx`  

---

### DAY 4: Mobile‑Specific Pages & Responsive Build

#### SUB‑TASK [4.1]: Mobile Page Scaffold  
##### Assigned Sub‑Agent: Coder  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/mobile/pages/index.tsx`  
  * **Architectural Requirements:**  
    * Render a mobile‑friendly welcome screen.  
* **Target Path:** `./sources/frontend/mobile/pages/_app.tsx`  
  * **Architectural Requirements:**  
    * Wrap with `next-i18next` provider.  

#### SUB‑TASK [4.2]: Tailwind Mobile Styles  
##### Assigned Sub‑Agent: Coder  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/mobile/tailwind.config.js`  
  * **Architectural Requirements:**  
    * Configure mobile breakpoints.  

#### SUB‑TASK [4.3]: Integration Test for Mobile Build  
##### Assigned Sub‑Agent: Tester  
##### Targeted Components & Technical Requirements:
* **Target Path:** `INTEGRATION_SCOPE;./sources/frontend/mobile/pages/index.tsx`  
  * **Architectural Requirements:**  
    * Verify page renders correctly on viewport width < 640px.  

#### SUB‑TASK [4.4]: Final Reviewer Pass‑Through  
##### Assigned Sub‑Agent: Reviewer  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/mobile/pages/index.tsx`  
* **Target Path:** `./sources/frontend/mobile/pages/_app.tsx`  
* **Target Path:** `./sources/frontend/mobile/tailwind.config.js`  

---

**Phase 3 is now complete. All core technical objectives for the frontend (web & mobile) have been satisfied, and the DoD criteria are met.**