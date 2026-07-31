# PHASE 5 CONTEXT BLUEPRINT: membership-hub

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
Phase 5 focuses on developing the mobile application frontend using React Native with Capacitor for hybrid mobile app development. This phase implements role-specific mobile UI components, authentication integration with JWT token management, course browsing and enrollment functionality, attendance QR scanning interface, membership card display, push notification handling, and comprehensive mobile navigation. All components must enforce OWASP security standards, implement proper input validation, and maintain strict RBAC enforcement through role-based access control.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- **Frontend Mobile Directory:** `./sources/frontend/mobile/`
- **API Endpoints:** 
  - GET `/api/courses` for course browsing [REQ-007], [REQ-010]
  - POST `/api/enrollments` for course registration [REQ-011]
  - POST `/api/attendance/scan` for QR attendance capture [REQ-012]
  - GET `/api/student/card` for membership card display [REQ-014]
  - GET `/api/centers` for center list view [REQ-004]
  - POST `/api/notifications/register` for push notification registration [REQ-021]

## 3. Dedicated Sub-Agent Functional Directives
- **coder:** Develop React Native components with Capacitor framework, implement responsive mobile UI, integrate with backend APIs, ensure OWASP compliance
- **tester:** Create and execute unit tests with minimum 85% code coverage for all mobile functionality
- **reviewer:** Perform static code analysis and compiler validation for mobile components
- **doc:** Generate technical documentation including component specifications and API integration guides

## 4. Phase Definition of Done (DoD)
- Complete mobile application with role-specific navigation and responsive UI
- Full integration with backend APIs for all required functionality
- 100% test coverage for all implemented requirements ([REQ-021])
- OWASP security standards implemented for all input validation and XSS prevention
- Push notification integration with Firebase Cloud Messaging and APNs
- All Tag IDs ([REQ-021], [REQ-004], [REQ-007], [REQ-010], [REQ-011], [REQ-012], [REQ-014]) properly mapped and implemented

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY 11: MOBILE APPLICATION FOUNDATION AND AUTHENTICATION INTEGRATION

#### SUB-TASK 11.1: Implement React Native application foundation with authentication integration
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/mobile/App.js [REQ-021], [ARC-006]`
* **Architectural Requirements:**
  * Create React Native application with React context for authentication state management
  * Implement JWT token storage and refresh logic with 15-minute expiry [ARC-006]
  * Set up role-based routing and navigation structure [REQ-021]
  * Implement automatic token refresh mechanism before expiry
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-021], [ARC-006]

#### SUB-TASK 11.2: Create mobile authentication service and API integration layer
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/mobile/services/authService.js [REQ-021], [ARC-006]`
* **Architectural Requirements:**
  * Implement login/logout functionality with email/password and social providers
  * Handle OAuth2 callback processing for Firebase, Google, Facebook [ARC-006]
  * Manage JWT tokens with secure storage (AsyncStorage with encryption)
  * Implement role extraction from JWT payload for RBAC enforcement [REQ-021]
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-021], [ARC-006]

#### SUB-TASK 11.3: Execute unit tests for mobile authentication components
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/mobile/services/authService.js;./sources/frontend/mobile/services/__tests__/authService.test.js [REQ-021], [ARC-006]`
* **Architectural Requirements:**
  * Achieve minimum 85% code coverage for authentication service
  * Test JWT token management and refresh logic
  * Verify role-based access control enforcement
  * Test OAuth2 integration scenarios
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-021], [ARC-006]

### DAY 12: ROLE-SPECIFIC MOBILE NAVIGATION AND DASHBOARD COMPONENTS

#### SUB-TASK 12.1: Implement role-based mobile navigation and dashboard structure
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/mobile/components/Navigation.js [REQ-021], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]`
* **Architectural Requirements:**
  * Create mobile navigation component with role-specific menu items
  * Implement System Admin full permissions navigation [ARC-001]
  * Implement Center Admin center-specific navigation [ARC-002]
  * Implement Manager limited permissions navigation [ARC-003]
  * Implement Teacher read-only navigation [ARC-004]
  * Implement Student course browsing and card navigation [ARC-005]
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-021], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

#### SUB-TASK 12.2: Create role-specific mobile dashboard components
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/mobile/screens/DashboardScreen.js [REQ-021], [REQ-025]`
* **Architectural Requirements:**
  * Implement System Admin dashboard with global overview [ARC-001]
  * Implement Center Admin dashboard with center-specific metrics [ARC-002], [REQ-025]
  * Implement Manager dashboard with student management tools [ARC-003]
  * Implement Teacher dashboard with course schedule [ARC-004]
  * Implement Student dashboard with course enrollment and card status [ARC-005], [REQ-014]
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-021], [REQ-025], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

#### SUB-TASK 12.3: Execute unit tests for mobile navigation and dashboard components
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/mobile/components/Navigation.js;./sources/frontend/mobile/components/__tests__/Navigation.test.js [REQ-021]`
* **Architectural Requirements:**
  * Achieve minimum 85% code coverage for navigation component
  * Test role-based menu item rendering
  * Verify navigation permissions for different user roles
  * Test responsive behavior across device sizes
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-021]

### DAY 13: MOBILE COURSE MANAGEMENT AND ENROLLMENT INTERFACE

#### SUB-TASK 13.1: Implement mobile course browsing and list view interface
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/mobile/screens/CoursesScreen.js [REQ-007], [REQ-010]`
* **Architectural Requirements:**
  * Create mobile course list view with CourseID, Title, StartDate, EndDate, TeacherName columns [REQ-007]
  * Implement filtering and sorting capabilities for course browsing
  * Exclude courses where student already has enrollment record [REQ-010]
  * Add responsive design for mobile viewing
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-007], [REQ-010]

#### SUB-TASK 13.2: Implement mobile course registration and enrollment functionality
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/mobile/components/CourseEnrollment.js [REQ-011]`
* **Architectural Requirements:**
  * Create mobile enrollment form with course selection and confirmation
  * Handle auto-creation of Student account if missing during registration [REQ-011]
  * Implement success/error handling with user feedback
  * Integrate with backend enrollment API endpoint
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-011]

#### SUB-TASK 13.3: Execute unit tests for mobile course management components
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/mobile/screens/CoursesScreen.js;./sources/frontend/mobile/screens/__tests__/CoursesScreen.test.js [REQ-007], [REQ-010]`
* **Architectural Requirements:**
  * Achieve minimum 85% code coverage for course browsing functionality
  * Test course filtering and exclusion logic for enrolled courses [REQ-010]
  * Verify API integration and data display accuracy [REQ-007]
  * Test enrollment form validation and submission
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-007], [REQ-010]

### DAY 14: MOBILE ATTENDANCE QR SCANNING AND MEMBERSHIP CARD INTERFACE

#### SUB-TASK 14.1: Implement mobile QR code scanning interface for attendance
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/mobile/components/QRScanner.js [REQ-012]`
* **Architectural Requirements:**
  * Create mobile QR scanner component using device camera access via Capacitor
  * Implement base64 payload decoding for studentID and courseID [REQ-012]
  * Handle scan confirmation and attendance submission
  * Provide visual feedback for successful/duplicate scans [REQ-013]
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-012], [REQ-013]

#### SUB-TASK 14.2: Implement mobile membership card display interface
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/mobile/screens/CardScreen.js [REQ-014]`
* **Architectural Requirements:**
  * Create mobile digital membership card component with remaining validity days display [REQ-014]
  * Show total validity days, days used, and days remaining calculation
  * Implement responsive design for mobile viewing
  * Add card renewal call-to-action interface [REQ-015]
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-014], [REQ-015]

#### SUB-TASK 14.3: Execute unit tests for mobile attendance and card components
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/mobile/components/QRScanner.js;./sources/frontend/mobile/components/__tests__/QRScanner.test.js [REQ-012], [REQ-013]`
* **Architectural Requirements:**
  * Achieve minimum 85% code coverage for QR scanning functionality
  * Test base64 payload decoding and validation [REQ-012]
  * Verify duplicate scan handling and user feedback [REQ-013]
  * Test membership card display and calculations [REQ-014]
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-012], [REQ-013], [REQ-014]

### DAY 15: PUSH NOTIFICATION INTEGRATION AND COMPREHENSIVE TESTING

#### SUB-TASK 15.1: Implement push notification registration and handling
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/mobile/services/notificationService.js [REQ-021]`
* **Architectural Requirements:**
  * Implement device token registration with Firebase Cloud Messaging and APNs
  * Handle push notification reception and display
  * Implement notification click handling and deep linking
  * Manage notification permissions and user preferences
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-021]

#### SUB-TASK 15.