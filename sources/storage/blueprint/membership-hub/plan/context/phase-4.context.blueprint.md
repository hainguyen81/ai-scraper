# PHASE 4 CONTEXT BLUEPRINT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260731045806 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date/Time** | 2026/07/31 04:58:06 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 1. Phase Operational Scope & Objectives
Phase 4 focuses on developing the web application frontend using React-based technology stack with Next.js framework. This phase implements role-specific responsive UI components, authentication integration with JWT token management, course browsing and enrollment functionality, attendance QR scanning interface, membership card display, and comprehensive navigation structure. All components must enforce OWASP security standards, implement proper input validation, and maintain strict RBAC enforcement through role-based access control.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- **Frontend Web Directory:** `./sources/frontend/web/`
- **API Endpoints:** 
  - GET `/api/courses` for course browsing [REQ-007], [REQ-010]
  - POST `/api/enrollments` for course registration [REQ-011]
  - POST `/api/attendance/scan` for QR attendance capture [REQ-012]
  - GET `/api/student/card` for membership card display [REQ-014]
  - GET `/api/centers` for center list view [REQ-004]

## 3. Dedicated Sub-Agent Functional Directives
- **coder:** Develop React components with Next.js framework, implement responsive UI, integrate with backend APIs, ensure OWASP compliance
- **tester:** Create and execute unit tests with minimum 85% code coverage for all frontend functionality
- **reviewer:** Perform static code analysis and compiler validation for frontend components
- **doc:** Generate technical documentation including component specifications and API integration guides

## 4. Phase Definition of Done (DoD)
- Complete web application with role-specific navigation and responsive UI
- Full integration with backend APIs for all required functionality
- 100% test coverage for all implemented requirements ([REQ-020])
- OWASP security standards implemented for all input validation and XSS prevention
- All Tag IDs ([REQ-020], [REQ-004], [REQ-007], [REQ-010], [REQ-011], [REQ-012], [REQ-014]) properly mapped and implemented

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY 8: WEB APPLICATION FOUNDATION AND AUTHENTICATION INTEGRATION

#### SUB-TASK 8.1: Implement Next.js application foundation with authentication integration
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/web/pages/_app.js [REQ-020], [ARC-006]`
* **Architectural Requirements:**
  * Create Next.js application with React context for authentication state management
  * Implement JWT token storage and refresh logic with 15-minute expiry [ARC-006]
  * Set up role-based routing and navigation structure [REQ-020]
  * Implement automatic token refresh mechanism before expiry
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-020], [ARC-006]

#### SUB-TASK 8.2: Create authentication service and API integration layer
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/web/services/authService.js [REQ-020], [ARC-006]`
* **Architectural Requirements:**
  * Implement login/logout functionality with email/password and social providers
  * Handle OAuth2 callback processing for Firebase, Google, Facebook [ARC-006]
  * Manage JWT tokens with secure storage (httpOnly cookies recommended)
  * Implement role extraction from JWT payload for RBAC enforcement [REQ-020]
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-020], [ARC-006]

#### SUB-TASK 8.3: Execute unit tests for authentication components
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/web/services/authService.js;./sources/frontend/web/services/__tests__/authService.test.js [REQ-020], [ARC-006]`
* **Architectural Requirements:**
  * Achieve minimum 85% code coverage for authentication service
  * Test JWT token management and refresh logic
  * Verify role-based access control enforcement
  * Test OAuth2 integration scenarios
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-020], [ARC-006]

### DAY 9: ROLE-SPECIFIC NAVIGATION AND DASHBOARD COMPONENTS

#### SUB-TASK 9.1: Implement role-based navigation and dashboard structure
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/web/components/Navigation.js [REQ-020], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]`
* **Architectural Requirements:**
  * Create responsive navigation component with role-specific menu items
  * Implement System Admin full permissions navigation [ARC-001]
  * Implement Center Admin center-specific navigation [ARC-002]
  * Implement Manager limited permissions navigation [ARC-003]
  * Implement Teacher read-only navigation [ARC-004]
  * Implement Student course browsing and card navigation [ARC-005]
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-020], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

#### SUB-TASK 9.2: Create role-specific dashboard components
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/web/pages/dashboard/index.js [REQ-020], [REQ-025]`
* **Architectural Requirements:**
  * Implement System Admin dashboard with global overview [ARC-001]
  * Implement Center Admin dashboard with center-specific metrics [ARC-002], [REQ-025]
  * Implement Manager dashboard with student management tools [ARC-003]
  * Implement Teacher dashboard with course schedule [ARC-004]
  * Implement Student dashboard with course enrollment and card status [ARC-005], [REQ-014]
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-020], [REQ-025], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

#### SUB-TASK 9.3: Execute unit tests for navigation and dashboard components
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/web/components/Navigation.js;./sources/frontend/web/components/__tests__/Navigation.test.js [REQ-020]`
* **Architectural Requirements:**
  * Achieve minimum 85% code coverage for navigation component
  * Test role-based menu item rendering
  * Verify navigation permissions for different user roles
  * Test responsive behavior across device sizes
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-020]

### DAY 10: COURSE MANAGEMENT AND ENROLLMENT INTERFACE

#### SUB-TASK 10.1: Implement course browsing and list view interface
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/web/pages/courses/index.js [REQ-007], [REQ-010]`
* **Architectural Requirements:**
  * Create course list view with CourseID, Title, StartDate, EndDate, TeacherName columns [REQ-007]
  * Implement filtering and sorting capabilities for course browsing
  * Exclude courses where student already has enrollment record [REQ-010]
  * Add responsive design for mobile and desktop viewing
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-007], [REQ-010]

#### SUB-TASK 10.2: Implement course registration and enrollment functionality
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/web/components/CourseEnrollment.js [REQ-011]`
* **Architectural Requirements:**
  * Create enrollment form with course selection and confirmation
  * Handle auto-creation of Student account if missing during registration [REQ-011]
  * Implement success/error handling with user feedback
  * Integrate with backend enrollment API endpoint
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-011]

#### SUB-TASK 10.3: Execute unit tests for course management components
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/web/pages/courses/index.js;./sources/frontend/web/pages/courses/__tests__/index.test.js [REQ-007], [REQ-010]`
* **Architectural Requirements:**
  * Achieve minimum 85% code coverage for course browsing functionality
  * Test course filtering and exclusion logic for enrolled courses [REQ-010]
  * Verify API integration and data display accuracy [REQ-007]
  * Test enrollment form validation and submission
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-007], [REQ-010]

### DAY 11: ATTENDANCE QR SCANNING AND MEMBERSHIP CARD INTERFACE

#### SUB-TASK 11.1: Implement QR code scanning interface for attendance
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/web/components/QRScanner.js [REQ-012]`
* **Architectural Requirements:**
  * Create QR scanner component using device camera access
  * Implement base64 payload decoding for studentID and courseID [REQ-012]
  * Handle scan confirmation and attendance submission
  * Provide visual feedback for successful/duplicate scans [REQ-013]
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-012], [REQ-013]

#### SUB-TASK 11.2: Implement membership card display interface
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/web/pages/student/card.js [REQ-014]`
* **Architectural Requirements:**
  * Create digital membership card component with remaining validity days display [REQ-014]
  * Show total validity days, days used, and days remaining calculation
  * Implement responsive design for mobile viewing
  * Add card renewal call-to-action interface [REQ-015]
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-014], [REQ-015]

#### SUB-TASK 11.3: Execute unit tests for attendance and card components
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/web/components/QRScanner.js;./sources/frontend/web/components/__tests__/QRScanner.test.js [REQ-012], [REQ-013]`
* **Architectural Requirements:**
  * Achieve minimum 85% code coverage for QR scanning functionality
  * Test base64 payload decoding and validation [REQ-012]
  * Verify duplicate scan handling and user feedback [REQ-013]
  * Test membership card display and calculations [REQ-014]
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-012], [REQ-013], [REQ-014]

### DAY 12: CENTER MANAGEMENT AND ADMINISTRATION INTERFACE

#### SUB-TASK 12.1: Implement center list view interface
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/web/pages/centers/index.js [REQ-004]`
* **Architectural Requirements:**
  * Create center list table with Name, Address, TaxID, AdminContact columns [REQ-004]
  * Implement responsive table design for various screen sizes
  * Add search and filtering capabilities for center browsing
  * Restrict center management actions based on user role [ARC-001], [ARC-002]
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-004], [ARC-001], [ARC-002]

#### SUB-TASK 12.2: Implement center create/update/delete interface for System Admin
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/web/components/CenterForm.js [REQ-005]`
* **Architectural Requirements:**
  * Create center management form with name, address, tax ID, contact fields [REQ-005]
  * Implement form validation for required fields and unique tax ID constraint
  * Handle duplicate tax ID conflict errors with user feedback
  * Restrict access to System Admin role only [ARC-001]
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-005], [ARC-001]

#### SUB-TASK 12.3: Execute unit tests for center management components
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/web/pages/centers/index.js;./sources/frontend/web/pages/centers/__tests__/index.test.js [REQ-004]`
* **Architectural Requirements:**
  * Achieve minimum 85% code coverage for center list functionality
  * Test role-based access control for center management [ARC-001], [ARC-002]
  * Verify form validation and duplicate tax ID handling [REQ-005]
  * Test responsive table behavior across devices
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-004], [REQ-005], [ARC-001], [ARC-002]

### DAY 13: COMPREHENSIVE TESTING AND SECURITY VALIDATION

#### SUB-TASK 13.1: Execute end-to-end integration testing for web application
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
* **Target Path:** `INTEGRATION_SCOPE;./sources/frontend/web/__tests__/e2e/integration.test.js [REQ-020], [REQ-004], [REQ-007], [REQ-010], [REQ-011], [REQ-012], [REQ-014]`
* **Architectural Requirements:**
  * Achieve 100% test coverage for all implemented requirements
  * Test complete user workflows across different roles
  * Verify API integration and data consistency
  * Test error handling and edge cases for all functionalities
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-020], [REQ-004], [REQ-007], [REQ-010], [REQ-011], [REQ-012], [REQ-014]

#### SUB-TASK 13.2: Perform security audit and OWASP compliance validation
##### Assigned Sub-Agent: reviewer
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/web/ [NFR-003], [NFR-007]`
* **Architectural Requirements:**
  * Validate XSS prevention through automated context sanitization [NFR-003]
  * Verify Content Security Policy implementation
  * Check for proper input validation on all form submissions
  * Validate JWT token security and storage practices [ARC-006]
  * Verify multi-language support implementation [NFR-007]
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [NFR-003], [NFR-007], [ARC-006]

#### SUB-TASK 13.3: Generate comprehensive technical documentation
##### Assigned Sub-Agent: doc
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/web/README.md [REQ-020]`
* **Architectural Requirements:**
  * Document component architecture and API integration patterns
  * Provide setup and deployment instructions
  * Document role-based navigation structure and permissions
  * Include security guidelines and OWASP compliance measures
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-020]