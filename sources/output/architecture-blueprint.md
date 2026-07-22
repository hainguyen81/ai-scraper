# Global Prompt:

Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for Project 'membership-hub'.

--- RAW REQUIREMENTS ---
## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile (app ĐT) để học viên xài.
	- Project này xây dựng backend bằng java 17, quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm frontend, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.
	- Phần web quản lý có quản lý lịch dạy và học, khuyến mãi các khóa học, thông báo của admin. Khi admin thông báo, tin nhắn sẽ được trigger gửi xuống group zalo của các học viên, đồng thời thông báo xuống app trên dt của học viên.
	- Phần web quản lý cũng có quản lý tiết học như tiết đó thầy cô nào dạy, từ mấy giờ đến mấy giờ.
	- Có quản lý điểm royalty của học viên. Học viên cứ đăng ký 1 khóa học sẽ được công 10 điểm. Có cả phần quản lý đăng ký khóa học, bao gồm học viên nào đăng ký khóa học nào do thầy cô nào dạy, thời gian khóa học từ ngày nào tới ngày nào.
	- Phần web quản lý sẽ có các role:
		+ System Admin (SysAdmin): là quyền cao nhất, toàn quyền trên tất cả các trung tâm.
		+ Admin: là quyền cao nhất của 1 trung tâm, toàn quyền trên trung tâm đó nhưng không có quyền trên các trung tâm khác
		+ Manager: là quyền quản lý của trung tâm, dưới quyền Admin, không có quyền chỉnh sửa thông tin khóa học, chỉ có quyền thông báo, và quản lý học viên, đăng ký học viên cho khóa học có sẵn, nhưng không có quyền phân công thầy cô dạy.
		+ Teacher: là quyền của các giáo viên, chỉ có thể xem lịch học, lịch dạy, danh sách học viên tham gia khóa học của mình. Chỉ quyền xem, không được chỉnh sửa, xóa hay tạo
		+ Student: là quyền của học viên. Chỉ được xem thông tin các khóa học, thầy cô nào dạy, có thể đăng ký khóa học mới. Và xem được thông tin thẻ của mình còn bao nhiêu ngày. Có thể đăng ký gia hạn ngày cho thẻ học viên.
	- Phần web quản lý sẽ có các màn hình:
		+ Quản lý trung tâm:
			1. Hiển thị danh sách các trung tâm, địa chỉ, mã số thuế, ai là người Admin của trung tâm đó, thông tin liên hệ của người Admin đó.
			2. Có thể thêm, xóa, sửa trung tâm.
			3. Có thể assign / un-assign Admin của trung tâm.
			4. Màn hình này ẩn với tất cả các role khác, ngoại trừ System Admin.
		+ Thông tin trung tâm:
			1. Chỉnh sửa thông tin trung tâm như tên, địa chỉ, số điện thoại (SĐT), mã số thuế (MST) chỉ bằng quyền Admin.
			2. Có thể assign / un-assign Manager cho trung tâm chỉ bằng quyền Admin.
			3. Trang này hiển thị cho mọi role như Admin, Manager, Teacher, Student, nhưng chỉ Admin của trung tâm có quyền thêm, xóa, sửa, assign / un-assign Manager.
		+ Dashboard:
			1. Hiển thị thông tin khóa học đang diễn ra ngày hiện tại
			2. Thông tin Teacher dạy khóa học nào của ngày hiện tại
			3. Nếu là Student, hiện thị hình ảnh thẻ kèm thòi gian còn hiệu lực của thẻ học viên.
			4. Hiển thị các chương trình khuyến mãi, thông báo
			5. Tự động cập nhật thông tin theo thời gian thực, interval 15 phút, interval value này có thể input từ enviroment.
		+ Quản lý khóa học:
			1. Danh sách các khóa học, thời gian diễn ra khóa học, thầy cô nào dạy khóa học nào.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Chỉ có Admin mới có thể thêm, sửa, xóa khóa học, đặc biệt quan trọng là tránh trùng lắp overlap thời gian các khóa học, assign / un-assign Teacher cho khóa học.
			4. Manager có thể chọn khóa học và đăng ký học viên cho khóa học đó. Có thể chọn từ học viên có sẵn hoặc đăng ký mới. Nếu đăng ký mới thì sẽ tự động tạo tài khoản role Student cho học viên đó và assign học viên cho khóa học đó.
			5. Assign / Un-assign học viên, đăng ký học viên mới đều phải có thông báo gửi xuống group zalo và app điện thoại mà học viên đó đã cài đặt.
			6. Admin có thể assign / un-assign Teacher dạy khóa học, có thể chọn từ Teacher có sẵn hoặc assign Teacher mới. Lúc đó sẽ tự động tạo tài khoản mới role Teacher và assign Teacher cho kháo học đó.
			7. Mọi thao tác assign / un-assign khóa học / tạo mới tài khoản Teacher cũng phải có thông báo gửi xuống group zalo và app điện thoại mà Teacher đó đã cài đặt.
		+ Quản lý Teacher:
			1. Danh sách các Teacher của trung tâm như Tên, Tuổi, SĐT, số Căn cước (CCCD), địa chỉ liên hệ, khóa học đăng đảm nhiệm dạy.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Chỉ Admin mới có thể assign / un-assign các khóa học cho Teacher được chọn, hoặc thêm, xóa, sửa Teacher.
			4. Mọi thao tác assign / un-assign khóa học / tạo mới tài khoản Teacher cũng phải có thông báo gửi xuống group zalo và app điện thoại mà Teacher đó đã cài đặt.
			5. Một Teacher có thể dạy được nhiều khóa học 1 lúc.
			6. Mọi thao tác assign / un-assign khóa học / tạo mới tài khoản Teacher cũng phải có thông báo gửi xuống group zalo và app điện thoại mà Teacher đó đã cài đặt.
		+ Quản lý Student:
			1. Danh sách các Student của trung tâm như Tên, Tuổi, SĐT, số Căn cước (CCCD), địa chỉ liên hệ, khóa học đã đăng ký, Teacher đang dạy kháo học đó.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Admin, Manager có thể thêm, xóa, sửa học viên, hoặc đăng ký khóa học có sẵn cho học viên được chọn. 1 Student có thể được đăng ký nhiều khóa học cùng lúc.
			4. Assign / Un-assign học viên, đăng ký học viên mới đều phải có thông báo gửi xuống group zalo và app điện thoại mà học viên đó đã cài đặt.
		+ Quản lý khuyến mãi:
			1. Danh sách các khuyến mãi gồm tên chương trình, mô tả, điều kiện, thời gian hiệu lực từ ngày nào đến ngày nào. Không nhập thời gian hiệu lực thì coi như khuyến mãi vẫn còn hiệu lực mãi.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Chỉ Admin, Magager có thể thêm, xóa, sửa
			4. Khi thêm, sửa khuyến mãi thì thông báo xuống group zalo và app ĐT của mọi role trừ System Admin
		+ Quản lý thông báo:
			1. Danh sách các thông báo như tên, nội dung thông báo, thời gian hiệu lực từ ngày nào đến ngày nào. Không nhập thời gian hiệu lực thì coi như thông báo vẫn còn hiệu lực mãi.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Chỉ Admin, Magager có thể thêm, xóa, sửa
			4. Khi thêm, sửa khuyến mãi thì thông báo xuống group zalo và app ĐT của mọi role trừ System Admin
		+ AI CSKH:
			1. Hiển thị float AI chat, có tích hợp AI để môi role có thể hỏi đáp thông tin về khóa học, giáo viên hay trung tâm
			2. Tích hợp AI để trả lời cho các câu hỏi thông tin về khóa học, giáo viên hay trung tâm
	- Phân app ĐT:
		+ Các màn hình và menu tương tự như phần web quản lý, cũng áp dụng các role y change
		+ Responsive các màn hình, tương ứng với các role, màn hình y như phần web
		+ Có thể nhận thông báo từ web gửi xuống

--- END REQUIREMENTS ---

## CRITICAL ENTERPRISE STRUCTURAL CONSTRAINTS (ABSOLUTE HARD LIMIT):
#### 1. EXACT PHASE COUNT MANDATE: You MUST segment the entire project architecture and development plan into EXACTLY 5 sequential phases. 
#### 2. NO MORE, NO LESS: Generating fewer than 5 phases or exceeding 5 phases is a critical engine failure. Under no circumstances are you allowed to create a Phase 6.
#### 3. SCOPE COMPRESSION: If the project requirements are small, you MUST distribute and stretch the tasks to fit exactly 5 phases. If the requirements are massive, you MUST compress, aggregate, and streamline the architectural components so they fit strictly within the 5 phases boundary.
#### 4. CHRONOLOGICAL PACKING: Every single requirement item specified in the documentation must be fully covered and packed cleanly across these 5 phases. Do not leave any loose ends or plan for post-phase execution.
	
## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

Your output MUST follow this exact structure:
## GLOBAL PROJECT CONTEXT: membership-hub
#### 1. Executive Summary & Tech Stack Blueprint
#### 2. Global Guardrails & Enterprise Compliance Standards
#### 3. Standardized Sub-Agent Persona Definitions (Manager, Coder, Tester, Reviewer, DevOps)
#### 4. Multi-Phase Segmentation Strategy Overview (Plan exactly 5 phases)

# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
## GLOBAL PROJECT CONTEXT: membership-hub
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a comprehensive platform designed to manage and facilitate learning centers, supporting multiple centers simultaneously. The platform will have both web and mobile applications, utilizing Java 17, Quarkus, Kafka, and Postgres for the backend, with Docker and GCP (Google Cloud Platform) for deployment. The tech stack also includes Next.js for the mobile frontend, ensuring a seamless user experience across various devices. Key features include user authentication, course management, attendance tracking, and notification systems.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to best practices, the following guardrails are established:
- **Security**: Implement robust security measures to protect user data, including encryption, secure authentication protocols, and regular security audits.
- **Scalability**: Design the system to scale horizontally, leveraging cloud services to handle increased traffic and user growth.
- **Compliance**: Adhere to relevant data protection regulations, such as GDPR and CCPA, ensuring user privacy and data security.
- **Quality Assurance**: Implement a rigorous testing framework, including unit tests, integration tests, and UI tests, to ensure high-quality code and minimal bugs.
- **Documentation**: Maintain comprehensive documentation of the codebase, including comments, API documentation, and user manuals.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas are defined to ensure clear roles and responsibilities within the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project is delivered on time, within budget, and meets the required quality standards.
- **Coder**: Responsible for writing high-quality, efficient, and well-documented code. Collaborates with the testing team to identify and fix bugs.
- **Tester**: Develops and executes comprehensive testing plans to ensure the software meets the required quality and functionality standards.
- **Reviewer**: Conducts code reviews to ensure that the code is maintainable, efficient, and adheres to the project's coding standards.
- **DevOps**: Focuses on the deployment, operation, and maintenance of the software system, ensuring high availability, performance, and security.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be segmented into exactly 5 phases, each with a strict duration limit of 1 to 7 days. The phases are designed to ensure a logical progression of the project, from planning to deployment.
- **Phase 1: Planning and Requirements Gathering** (Day 1-2)
  - Define project scope, goals, and timelines.
  - Gather and document all requirements.
- **Phase 2: Backend Development** (Day 3-5)
  - Develop the backend using Java 17, Quarkus, Kafka, and Postgres.
  - Implement authentication, course management, and attendance tracking features.
- **Phase 3: Frontend Development** (Day 6-10, compressed to fit within 7 days)
  - Develop the web and mobile frontend using Next.js.
  - Ensure responsive design and user-friendly interfaces.
- **Phase 4: Testing and Quality Assurance** (Day 11-14, compressed to fit within 7 days)
  - Conduct unit tests, integration tests, and UI tests.
  - Identify and fix bugs to ensure high-quality code.
- **Phase 5: Deployment and Maintenance** (Day 15-21, compressed to fit within 7 days)
  - Deploy the application on GCP.
  - Ensure scalability, security, and high availability.
  - Plan for post-deployment maintenance and updates.
```

# Phase 1 - Prompt:

Project Name: membership-hub
You are tasked to detail **PHASE 1 OUT OF 5**.
You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

--- GLOBAL CONTEXT REFERENCE ---
## GLOBAL PROJECT CONTEXT: membership-hub
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a comprehensive platform designed to manage and facilitate learning centers, supporting multiple centers simultaneously. The platform will have both web and mobile applications, utilizing Java 17, Quarkus, Kafka, and Postgres for the backend, with Docker and GCP (Google Cloud Platform) for deployment. The tech stack also includes Next.js for the mobile frontend, ensuring a seamless user experience across various devices. Key features include user authentication, course management, attendance tracking, and notification systems.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to best practices, the following guardrails are established:
- **Security**: Implement robust security measures to protect user data, including encryption, secure authentication protocols, and regular security audits.
- **Scalability**: Design the system to scale horizontally, leveraging cloud services to handle increased traffic and user growth.
- **Compliance**: Adhere to relevant data protection regulations, such as GDPR and CCPA, ensuring user privacy and data security.
- **Quality Assurance**: Implement a rigorous testing framework, including unit tests, integration tests, and UI tests, to ensure high-quality code and minimal bugs.
- **Documentation**: Maintain comprehensive documentation of the codebase, including comments, API documentation, and user manuals.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas are defined to ensure clear roles and responsibilities within the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project is delivered on time, within budget, and meets the required quality standards.
- **Coder**: Responsible for writing high-quality, efficient, and well-documented code. Collaborates with the testing team to identify and fix bugs.
- **Tester**: Develops and executes comprehensive testing plans to ensure the software meets the required quality and functionality standards.
- **Reviewer**: Conducts code reviews to ensure that the code is maintainable, efficient, and adheres to the project's coding standards.
- **DevOps**: Focuses on the deployment, operation, and maintenance of the software system, ensuring high availability, performance, and security.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be segmented into exactly 5 phases, each with a strict duration limit of 1 to 7 days. The phases are designed to ensure a logical progression of the project, from planning to deployment.
- **Phase 1: Planning and Requirements Gathering** (Day 1-2)
  - Define project scope, goals, and timelines.
  - Gather and document all requirements.
- **Phase 2: Backend Development** (Day 3-5)
  - Develop the backend using Java 17, Quarkus, Kafka, and Postgres.
  - Implement authentication, course management, and attendance tracking features.
- **Phase 3: Frontend Development** (Day 6-10, compressed to fit within 7 days)
  - Develop the web and mobile frontend using Next.js.
  - Ensure responsive design and user-friendly interfaces.
- **Phase 4: Testing and Quality Assurance** (Day 11-14, compressed to fit within 7 days)
  - Conduct unit tests, integration tests, and UI tests.
  - Identify and fix bugs to ensure high-quality code.
- **Phase 5: Deployment and Maintenance** (Day 15-21, compressed to fit within 7 days)
  - Deploy the application on GCP.
  - Ensure scalability, security, and high availability.
  - Plan for post-deployment maintenance and updates.

--- RAW REQUIREMENTS REFERENCE ---
## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile (app ĐT) để học viên xài.
	- Project này xây dựng backend bằng java 17, quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm frontend, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.
	- Phần web quản lý có quản lý lịch dạy và học, khuyến mãi các khóa học, thông báo của admin. Khi admin thông báo, tin nhắn sẽ được trigger gửi xuống group zalo của các học viên, đồng thời thông báo xuống app trên dt của học viên.
	- Phần web quản lý cũng có quản lý tiết học như tiết đó thầy cô nào dạy, từ mấy giờ đến mấy giờ.
	- Có quản lý điểm royalty của học viên. Học viên cứ đăng ký 1 khóa học sẽ được công 10 điểm. Có cả phần quản lý đăng ký khóa học, bao gồm học viên nào đăng ký khóa học nào do thầy cô nào dạy, thời gian khóa học từ ngày nào tới ngày nào.
	- Phần web quản lý sẽ có các role:
		+ System Admin (SysAdmin): là quyền cao nhất, toàn quyền trên tất cả các trung tâm.
		+ Admin: là quyền cao nhất của 1 trung tâm, toàn quyền trên trung tâm đó nhưng không có quyền trên các trung tâm khác
		+ Manager: là quyền quản lý của trung tâm, dưới quyền Admin, không có quyền chỉnh sửa thông tin khóa học, chỉ có quyền thông báo, và quản lý học viên, đăng ký học viên cho khóa học có sẵn, nhưng không có quyền phân công thầy cô dạy.
		+ Teacher: là quyền của các giáo viên, chỉ có thể xem lịch học, lịch dạy, danh sách học viên tham gia khóa học của mình. Chỉ quyền xem, không được chỉnh sửa, xóa hay tạo
		+ Student: là quyền của học viên. Chỉ được xem thông tin các khóa học, thầy cô nào dạy, có thể đăng ký khóa học mới. Và xem được thông tin thẻ của mình còn bao nhiêu ngày. Có thể đăng ký gia hạn ngày cho thẻ học viên.
	- Phần web quản lý sẽ có các màn hình:
		+ Quản lý trung tâm:
			1. Hiển thị danh sách các trung tâm, địa chỉ, mã số thuế, ai là người Admin của trung tâm đó, thông tin liên hệ của người Admin đó.
			2. Có thể thêm, xóa, sửa trung tâm.
			3. Có thể assign / un-assign Admin của trung tâm.
			4. Màn hình này ẩn với tất cả các role khác, ngoại trừ System Admin.
		+ Thông tin trung tâm:
			1. Chỉnh sửa thông tin trung tâm như tên, địa chỉ, số điện thoại (SĐT), mã số thuế (MST) chỉ bằng quyền Admin.
			2. Có thể assign / un-assign Manager cho trung tâm chỉ bằng quyền Admin.
			3. Trang này hiển thị cho mọi role như Admin, Manager, Teacher, Student, nhưng chỉ Admin của trung tâm có quyền thêm, xóa, sửa, assign / un-assign Manager.
		+ Dashboard:
			1. Hiển thị thông tin khóa học đang diễn ra ngày hiện tại
			2. Thông tin Teacher dạy khóa học nào của ngày hiện tại
			3. Nếu là Student, hiện thị hình ảnh thẻ kèm thòi gian còn hiệu lực của thẻ học viên.
			4. Hiển thị các chương trình khuyến mãi, thông báo
			5. Tự động cập nhật thông tin theo thời gian thực, interval 15 phút, interval value này có thể input từ enviroment.
		+ Quản lý khóa học:
			1. Danh sách các khóa học, thời gian diễn ra khóa học, thầy cô nào dạy khóa học nào.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Chỉ có Admin mới có thể thêm, sửa, xóa khóa học, đặc biệt quan trọng là tránh trùng lắp overlap thời gian các khóa học, assign / un-assign Teacher cho khóa học.
			4. Manager có thể chọn khóa học và đăng ký học viên cho khóa học đó. Có thể chọn từ học viên có sẵn hoặc đăng ký mới. Nếu đăng ký mới thì sẽ tự động tạo tài khoản role Student cho học viên đó và assign học viên cho khóa học đó.
			5. Assign / Un-assign học viên, đăng ký học viên mới đều phải có thông báo gửi xuống group zalo và app điện thoại mà học viên đó đã cài đặt.
			6. Admin có thể assign / un-assign Teacher dạy khóa học, có thể chọn từ Teacher có sẵn hoặc assign Teacher mới. Lúc đó sẽ tự động tạo tài khoản mới role Teacher và assign Teacher cho kháo học đó.
			7. Mọi thao tác assign / un-assign khóa học / tạo mới tài khoản Teacher cũng phải có thông báo gửi xuống group zalo và app điện thoại mà Teacher đó đã cài đặt.
		+ Quản lý Teacher:
			1. Danh sách các Teacher của trung tâm như Tên, Tuổi, SĐT, số Căn cước (CCCD), địa chỉ liên hệ, khóa học đăng đảm nhiệm dạy.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Chỉ Admin mới có thể assign / un-assign các khóa học cho Teacher được chọn, hoặc thêm, xóa, sửa Teacher.
			4. Mọi thao tác assign / un-assign khóa học / tạo mới tài khoản Teacher cũng phải có thông báo gửi xuống group zalo và app điện thoại mà Teacher đó đã cài đặt.
			5. Một Teacher có thể dạy được nhiều khóa học 1 lúc.
			6. Mọi thao tác assign / un-assign khóa học / tạo mới tài khoản Teacher cũng phải có thông báo gửi xuống group zalo và app điện thoại mà Teacher đó đã cài đặt.
		+ Quản lý Student:
			1. Danh sách các Student của trung tâm như Tên, Tuổi, SĐT, số Căn cước (CCCD), địa chỉ liên hệ, khóa học đã đăng ký, Teacher đang dạy kháo học đó.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Admin, Manager có thể thêm, xóa, sửa học viên, hoặc đăng ký khóa học có sẵn cho học viên được chọn. 1 Student có thể được đăng ký nhiều khóa học cùng lúc.
			4. Assign / Un-assign học viên, đăng ký học viên mới đều phải có thông báo gửi xuống group zalo và app điện thoại mà học viên đó đã cài đặt.
		+ Quản lý khuyến mãi:
			1. Danh sách các khuyến mãi gồm tên chương trình, mô tả, điều kiện, thời gian hiệu lực từ ngày nào đến ngày nào. Không nhập thời gian hiệu lực thì coi như khuyến mãi vẫn còn hiệu lực mãi.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Chỉ Admin, Magager có thể thêm, xóa, sửa
			4. Khi thêm, sửa khuyến mãi thì thông báo xuống group zalo và app ĐT của mọi role trừ System Admin
		+ Quản lý thông báo:
			1. Danh sách các thông báo như tên, nội dung thông báo, thời gian hiệu lực từ ngày nào đến ngày nào. Không nhập thời gian hiệu lực thì coi như thông báo vẫn còn hiệu lực mãi.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Chỉ Admin, Magager có thể thêm, xóa, sửa
			4. Khi thêm, sửa khuyến mãi thì thông báo xuống group zalo và app ĐT của mọi role trừ System Admin
		+ AI CSKH:
			1. Hiển thị float AI chat, có tích hợp AI để môi role có thể hỏi đáp thông tin về khóa học, giáo viên hay trung tâm
			2. Tích hợp AI để trả lời cho các câu hỏi thông tin về khóa học, giáo viên hay trung tâm
	- Phân app ĐT:
		+ Các màn hình và menu tương tự như phần web quản lý, cũng áp dụng các role y change
		+ Responsive các màn hình, tương ứng với các role, màn hình y như phần web
		+ Có thể nhận thông báo từ web gửi xuống

----------------------------------

## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

Your output MUST follow this exact Markdown structure for Phase 1:
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
#### 4. Phase Definition of Done (DoD)

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
```

# Phase 2 - Prompt:

Project Name: membership-hub
You are tasked to detail **PHASE 2 OUT OF 5**.
You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

--- GLOBAL CONTEXT REFERENCE ---
## GLOBAL PROJECT CONTEXT: membership-hub
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a comprehensive platform designed to manage and facilitate learning centers, supporting multiple centers simultaneously. The platform will have both web and mobile applications, utilizing Java 17, Quarkus, Kafka, and Postgres for the backend, with Docker and GCP (Google Cloud Platform) for deployment. The tech stack also includes Next.js for the mobile frontend, ensuring a seamless user experience across various devices. Key features include user authentication, course management, attendance tracking, and notification systems.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to best practices, the following guardrails are established:
- **Security**: Implement robust security measures to protect user data, including encryption, secure authentication protocols, and regular security audits.
- **Scalability**: Design the system to scale horizontally, leveraging cloud services to handle increased traffic and user growth.
- **Compliance**: Adhere to relevant data protection regulations, such as GDPR and CCPA, ensuring user privacy and data security.
- **Quality Assurance**: Implement a rigorous testing framework, including unit tests, integration tests, and UI tests, to ensure high-quality code and minimal bugs.
- **Documentation**: Maintain comprehensive documentation of the codebase, including comments, API documentation, and user manuals.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas are defined to ensure clear roles and responsibilities within the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project is delivered on time, within budget, and meets the required quality standards.
- **Coder**: Responsible for writing high-quality, efficient, and well-documented code. Collaborates with the testing team to identify and fix bugs.
- **Tester**: Develops and executes comprehensive testing plans to ensure the software meets the required quality and functionality standards.
- **Reviewer**: Conducts code reviews to ensure that the code is maintainable, efficient, and adheres to the project's coding standards.
- **DevOps**: Focuses on the deployment, operation, and maintenance of the software system, ensuring high availability, performance, and security.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be segmented into exactly 5 phases, each with a strict duration limit of 1 to 7 days. The phases are designed to ensure a logical progression of the project, from planning to deployment.
- **Phase 1: Planning and Requirements Gathering** (Day 1-2)
  - Define project scope, goals, and timelines.
  - Gather and document all requirements.
- **Phase 2: Backend Development** (Day 3-5)
  - Develop the backend using Java 17, Quarkus, Kafka, and Postgres.
  - Implement authentication, course management, and attendance tracking features.
- **Phase 3: Frontend Development** (Day 6-10, compressed to fit within 7 days)
  - Develop the web and mobile frontend using Next.js.
  - Ensure responsive design and user-friendly interfaces.
- **Phase 4: Testing and Quality Assurance** (Day 11-14, compressed to fit within 7 days)
  - Conduct unit tests, integration tests, and UI tests.
  - Identify and fix bugs to ensure high-quality code.
- **Phase 5: Deployment and Maintenance** (Day 15-21, compressed to fit within 7 days)
  - Deploy the application on GCP.
  - Ensure scalability, security, and high availability.
  - Plan for post-deployment maintenance and updates.

--- RAW REQUIREMENTS REFERENCE ---
## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile (app ĐT) để học viên xài.
	- Project này xây dựng backend bằng java 17, quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm frontend, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.
	- Phần web quản lý có quản lý lịch dạy và học, khuyến mãi các khóa học, thông báo của admin. Khi admin thông báo, tin nhắn sẽ được trigger gửi xuống group zalo của các học viên, đồng thời thông báo xuống app trên dt của học viên.
	- Phần web quản lý cũng có quản lý tiết học như tiết đó thầy cô nào dạy, từ mấy giờ đến mấy giờ.
	- Có quản lý điểm royalty của học viên. Học viên cứ đăng ký 1 khóa học sẽ được công 10 điểm. Có cả phần quản lý đăng ký khóa học, bao gồm học viên nào đăng ký khóa học nào do thầy cô nào dạy, thời gian khóa học từ ngày nào tới ngày nào.
	- Phần web quản lý sẽ có các role:
		+ System Admin (SysAdmin): là quyền cao nhất, toàn quyền trên tất cả các trung tâm.
		+ Admin: là quyền cao nhất của 1 trung tâm, toàn quyền trên trung tâm đó nhưng không có quyền trên các trung tâm khác
		+ Manager: là quyền quản lý của trung tâm, dưới quyền Admin, không có quyền chỉnh sửa thông tin khóa học, chỉ có quyền thông báo, và quản lý học viên, đăng ký học viên cho khóa học có sẵn, nhưng không có quyền phân công thầy cô dạy.
		+ Teacher: là quyền của các giáo viên, chỉ có thể xem lịch học, lịch dạy, danh sách học viên tham gia khóa học của mình. Chỉ quyền xem, không được chỉnh sửa, xóa hay tạo
		+ Student: là quyền của học viên. Chỉ được xem thông tin các khóa học, thầy cô nào dạy, có thể đăng ký khóa học mới. Và xem được thông tin thẻ của mình còn bao nhiêu ngày. Có thể đăng ký gia hạn ngày cho thẻ học viên.
	- Phần web quản lý sẽ có các màn hình:
		+ Quản lý trung tâm:
			1. Hiển thị danh sách các trung tâm, địa chỉ, mã số thuế, ai là người Admin của trung tâm đó, thông tin liên hệ của người Admin đó.
			2. Có thể thêm, xóa, sửa trung tâm.
			3. Có thể assign / un-assign Admin của trung tâm.
			4. Màn hình này ẩn với tất cả các role khác, ngoại trừ System Admin.
		+ Thông tin trung tâm:
			1. Chỉnh sửa thông tin trung tâm như tên, địa chỉ, số điện thoại (SĐT), mã số thuế (MST) chỉ bằng quyền Admin.
			2. Có thể assign / un-assign Manager cho trung tâm chỉ bằng quyền Admin.
			3. Trang này hiển thị cho mọi role như Admin, Manager, Teacher, Student, nhưng chỉ Admin của trung tâm có quyền thêm, xóa, sửa, assign / un-assign Manager.
		+ Dashboard:
			1. Hiển thị thông tin khóa học đang diễn ra ngày hiện tại
			2. Thông tin Teacher dạy khóa học nào của ngày hiện tại
			3. Nếu là Student, hiện thị hình ảnh thẻ kèm thòi gian còn hiệu lực của thẻ học viên.
			4. Hiển thị các chương trình khuyến mãi, thông báo
			5. Tự động cập nhật thông tin theo thời gian thực, interval 15 phút, interval value này có thể input từ enviroment.
		+ Quản lý khóa học:
			1. Danh sách các khóa học, thời gian diễn ra khóa học, thầy cô nào dạy khóa học nào.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Chỉ có Admin mới có thể thêm, sửa, xóa khóa học, đặc biệt quan trọng là tránh trùng lắp overlap thời gian các khóa học, assign / un-assign Teacher cho khóa học.
			4. Manager có thể chọn khóa học và đăng ký học viên cho khóa học đó. Có thể chọn từ học viên có sẵn hoặc đăng ký mới. Nếu đăng ký mới thì sẽ tự động tạo tài khoản role Student cho học viên đó và assign học viên cho khóa học đó.
			5. Assign / Un-assign học viên, đăng ký học viên mới đều phải có thông báo gửi xuống group zalo và app điện thoại mà học viên đó đã cài đặt.
			6. Admin có thể assign / un-assign Teacher dạy khóa học, có thể chọn từ Teacher có sẵn hoặc assign Teacher mới. Lúc đó sẽ tự động tạo tài khoản mới role Teacher và assign Teacher cho kháo học đó.
			7. Mọi thao tác assign / un-assign khóa học / tạo mới tài khoản Teacher cũng phải có thông báo gửi xuống group zalo và app điện thoại mà Teacher đó đã cài đặt.
		+ Quản lý Teacher:
			1. Danh sách các Teacher của trung tâm như Tên, Tuổi, SĐT, số Căn cước (CCCD), địa chỉ liên hệ, khóa học đăng đảm nhiệm dạy.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Chỉ Admin mới có thể assign / un-assign các khóa học cho Teacher được chọn, hoặc thêm, xóa, sửa Teacher.
			4. Mọi thao tác assign / un-assign khóa học / tạo mới tài khoản Teacher cũng phải có thông báo gửi xuống group zalo và app điện thoại mà Teacher đó đã cài đặt.
			5. Một Teacher có thể dạy được nhiều khóa học 1 lúc.
			6. Mọi thao tác assign / un-assign khóa học / tạo mới tài khoản Teacher cũng phải có thông báo gửi xuống group zalo và app điện thoại mà Teacher đó đã cài đặt.
		+ Quản lý Student:
			1. Danh sách các Student của trung tâm như Tên, Tuổi, SĐT, số Căn cước (CCCD), địa chỉ liên hệ, khóa học đã đăng ký, Teacher đang dạy kháo học đó.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Admin, Manager có thể thêm, xóa, sửa học viên, hoặc đăng ký khóa học có sẵn cho học viên được chọn. 1 Student có thể được đăng ký nhiều khóa học cùng lúc.
			4. Assign / Un-assign học viên, đăng ký học viên mới đều phải có thông báo gửi xuống group zalo và app điện thoại mà học viên đó đã cài đặt.
		+ Quản lý khuyến mãi:
			1. Danh sách các khuyến mãi gồm tên chương trình, mô tả, điều kiện, thời gian hiệu lực từ ngày nào đến ngày nào. Không nhập thời gian hiệu lực thì coi như khuyến mãi vẫn còn hiệu lực mãi.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Chỉ Admin, Magager có thể thêm, xóa, sửa
			4. Khi thêm, sửa khuyến mãi thì thông báo xuống group zalo và app ĐT của mọi role trừ System Admin
		+ Quản lý thông báo:
			1. Danh sách các thông báo như tên, nội dung thông báo, thời gian hiệu lực từ ngày nào đến ngày nào. Không nhập thời gian hiệu lực thì coi như thông báo vẫn còn hiệu lực mãi.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Chỉ Admin, Magager có thể thêm, xóa, sửa
			4. Khi thêm, sửa khuyến mãi thì thông báo xuống group zalo và app ĐT của mọi role trừ System Admin
		+ AI CSKH:
			1. Hiển thị float AI chat, có tích hợp AI để môi role có thể hỏi đáp thông tin về khóa học, giáo viên hay trung tâm
			2. Tích hợp AI để trả lời cho các câu hỏi thông tin về khóa học, giáo viên hay trung tâm
	- Phân app ĐT:
		+ Các màn hình và menu tương tự như phần web quản lý, cũng áp dụng các role y change
		+ Responsive các màn hình, tương ứng với các role, màn hình y như phần web
		+ Có thể nhận thông báo từ web gửi xuống

----------------------------------

## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

Your output MUST follow this exact Markdown structure for Phase 2:
## PHASE 2 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
#### 4. Phase Definition of Done (DoD)

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 2 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend of the membership-hub project using Java 17, Quarkus, Kafka, and Postgres. This phase will focus on implementing the core features, including user authentication, course management, attendance tracking, and notification systems. The scope of this phase includes designing and implementing the database schema, creating RESTful APIs for backend services, and integrating Kafka for event-driven architecture.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 2 includes:
- **Database Schema Design**: Designing the Postgres database schema to support user authentication, course management, attendance tracking, and notification systems.
- **Backend API Development**: Creating RESTful APIs using Java 17 and Quarkus for user authentication, course management, attendance tracking, and notification systems.
- **Kafka Integration**: Integrating Kafka for event-driven architecture to handle notifications and attendance tracking.
- **Directory Structure**:
  - `src/main/java`: Java source files for the backend application.
  - `src/main/resources`: Configuration files and database schema definitions.
  - `src/test/java`: Unit tests and integration tests for the backend application.
- **Endpoints**:
  - `/api/auth`: User authentication endpoints.
  - `/api/courses`: Course management endpoints.
  - `/api/attendance`: Attendance tracking endpoints.
  - `/api/notifications`: Notification system endpoints.

#### 3. Dedicated Sub-Agent Functional Directives
The following sub-agents will be involved in Phase 2:
- **Coder**: Responsible for designing and implementing the database schema, creating RESTful APIs, and integrating Kafka.
- **Tester**: Responsible for creating unit tests and integration tests for the backend application.
- **Reviewer**: Responsible for reviewing the code and ensuring it meets the project's coding standards and best practices.
- **DevOps**: Responsible for setting up the development environment, configuring Kafka, and ensuring the backend application is deployable.

#### 4. Phase Definition of Done (DoD)
Phase 2 is considered complete when:
- The database schema is designed and implemented.
- RESTful APIs for user authentication, course management, attendance tracking, and notification systems are created and tested.
- Kafka is integrated for event-driven architecture.
- Unit tests and integration tests are written and passed.
- Code reviews are completed, and the code meets the project's coding standards and best practices.
- The backend application is deployable and configured for further development.
```

# Phase 3 - Prompt:

Project Name: membership-hub
You are tasked to detail **PHASE 3 OUT OF 5**.
You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

--- GLOBAL CONTEXT REFERENCE ---
## GLOBAL PROJECT CONTEXT: membership-hub
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a comprehensive platform designed to manage and facilitate learning centers, supporting multiple centers simultaneously. The platform will have both web and mobile applications, utilizing Java 17, Quarkus, Kafka, and Postgres for the backend, with Docker and GCP (Google Cloud Platform) for deployment. The tech stack also includes Next.js for the mobile frontend, ensuring a seamless user experience across various devices. Key features include user authentication, course management, attendance tracking, and notification systems.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to best practices, the following guardrails are established:
- **Security**: Implement robust security measures to protect user data, including encryption, secure authentication protocols, and regular security audits.
- **Scalability**: Design the system to scale horizontally, leveraging cloud services to handle increased traffic and user growth.
- **Compliance**: Adhere to relevant data protection regulations, such as GDPR and CCPA, ensuring user privacy and data security.
- **Quality Assurance**: Implement a rigorous testing framework, including unit tests, integration tests, and UI tests, to ensure high-quality code and minimal bugs.
- **Documentation**: Maintain comprehensive documentation of the codebase, including comments, API documentation, and user manuals.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas are defined to ensure clear roles and responsibilities within the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project is delivered on time, within budget, and meets the required quality standards.
- **Coder**: Responsible for writing high-quality, efficient, and well-documented code. Collaborates with the testing team to identify and fix bugs.
- **Tester**: Develops and executes comprehensive testing plans to ensure the software meets the required quality and functionality standards.
- **Reviewer**: Conducts code reviews to ensure that the code is maintainable, efficient, and adheres to the project's coding standards.
- **DevOps**: Focuses on the deployment, operation, and maintenance of the software system, ensuring high availability, performance, and security.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be segmented into exactly 5 phases, each with a strict duration limit of 1 to 7 days. The phases are designed to ensure a logical progression of the project, from planning to deployment.
- **Phase 1: Planning and Requirements Gathering** (Day 1-2)
  - Define project scope, goals, and timelines.
  - Gather and document all requirements.
- **Phase 2: Backend Development** (Day 3-5)
  - Develop the backend using Java 17, Quarkus, Kafka, and Postgres.
  - Implement authentication, course management, and attendance tracking features.
- **Phase 3: Frontend Development** (Day 6-10, compressed to fit within 7 days)
  - Develop the web and mobile frontend using Next.js.
  - Ensure responsive design and user-friendly interfaces.
- **Phase 4: Testing and Quality Assurance** (Day 11-14, compressed to fit within 7 days)
  - Conduct unit tests, integration tests, and UI tests.
  - Identify and fix bugs to ensure high-quality code.
- **Phase 5: Deployment and Maintenance** (Day 15-21, compressed to fit within 7 days)
  - Deploy the application on GCP.
  - Ensure scalability, security, and high availability.
  - Plan for post-deployment maintenance and updates.

--- RAW REQUIREMENTS REFERENCE ---
## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile (app ĐT) để học viên xài.
	- Project này xây dựng backend bằng java 17, quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm frontend, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.
	- Phần web quản lý có quản lý lịch dạy và học, khuyến mãi các khóa học, thông báo của admin. Khi admin thông báo, tin nhắn sẽ được trigger gửi xuống group zalo của các học viên, đồng thời thông báo xuống app trên dt của học viên.
	- Phần web quản lý cũng có quản lý tiết học như tiết đó thầy cô nào dạy, từ mấy giờ đến mấy giờ.
	- Có quản lý điểm royalty của học viên. Học viên cứ đăng ký 1 khóa học sẽ được công 10 điểm. Có cả phần quản lý đăng ký khóa học, bao gồm học viên nào đăng ký khóa học nào do thầy cô nào dạy, thời gian khóa học từ ngày nào tới ngày nào.
	- Phần web quản lý sẽ có các role:
		+ System Admin (SysAdmin): là quyền cao nhất, toàn quyền trên tất cả các trung tâm.
		+ Admin: là quyền cao nhất của 1 trung tâm, toàn quyền trên trung tâm đó nhưng không có quyền trên các trung tâm khác
		+ Manager: là quyền quản lý của trung tâm, dưới quyền Admin, không có quyền chỉnh sửa thông tin khóa học, chỉ có quyền thông báo, và quản lý học viên, đăng ký học viên cho khóa học có sẵn, nhưng không có quyền phân công thầy cô dạy.
		+ Teacher: là quyền của các giáo viên, chỉ có thể xem lịch học, lịch dạy, danh sách học viên tham gia khóa học của mình. Chỉ quyền xem, không được chỉnh sửa, xóa hay tạo
		+ Student: là quyền của học viên. Chỉ được xem thông tin các khóa học, thầy cô nào dạy, có thể đăng ký khóa học mới. Và xem được thông tin thẻ của mình còn bao nhiêu ngày. Có thể đăng ký gia hạn ngày cho thẻ học viên.
	- Phần web quản lý sẽ có các màn hình:
		+ Quản lý trung tâm:
			1. Hiển thị danh sách các trung tâm, địa chỉ, mã số thuế, ai là người Admin của trung tâm đó, thông tin liên hệ của người Admin đó.
			2. Có thể thêm, xóa, sửa trung tâm.
			3. Có thể assign / un-assign Admin của trung tâm.
			4. Màn hình này ẩn với tất cả các role khác, ngoại trừ System Admin.
		+ Thông tin trung tâm:
			1. Chỉnh sửa thông tin trung tâm như tên, địa chỉ, số điện thoại (SĐT), mã số thuế (MST) chỉ bằng quyền Admin.
			2. Có thể assign / un-assign Manager cho trung tâm chỉ bằng quyền Admin.
			3. Trang này hiển thị cho mọi role như Admin, Manager, Teacher, Student, nhưng chỉ Admin của trung tâm có quyền thêm, xóa, sửa, assign / un-assign Manager.
		+ Dashboard:
			1. Hiển thị thông tin khóa học đang diễn ra ngày hiện tại
			2. Thông tin Teacher dạy khóa học nào của ngày hiện tại
			3. Nếu là Student, hiện thị hình ảnh thẻ kèm thòi gian còn hiệu lực của thẻ học viên.
			4. Hiển thị các chương trình khuyến mãi, thông báo
			5. Tự động cập nhật thông tin theo thời gian thực, interval 15 phút, interval value này có thể input từ enviroment.
		+ Quản lý khóa học:
			1. Danh sách các khóa học, thời gian diễn ra khóa học, thầy cô nào dạy khóa học nào.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Chỉ có Admin mới có thể thêm, sửa, xóa khóa học, đặc biệt quan trọng là tránh trùng lắp overlap thời gian các khóa học, assign / un-assign Teacher cho khóa học.
			4. Manager có thể chọn khóa học và đăng ký học viên cho khóa học đó. Có thể chọn từ học viên có sẵn hoặc đăng ký mới. Nếu đăng ký mới thì sẽ tự động tạo tài khoản role Student cho học viên đó và assign học viên cho khóa học đó.
			5. Assign / Un-assign học viên, đăng ký học viên mới đều phải có thông báo gửi xuống group zalo và app điện thoại mà học viên đó đã cài đặt.
			6. Admin có thể assign / un-assign Teacher dạy khóa học, có thể chọn từ Teacher có sẵn hoặc assign Teacher mới. Lúc đó sẽ tự động tạo tài khoản mới role Teacher và assign Teacher cho kháo học đó.
			7. Mọi thao tác assign / un-assign khóa học / tạo mới tài khoản Teacher cũng phải có thông báo gửi xuống group zalo và app điện thoại mà Teacher đó đã cài đặt.
		+ Quản lý Teacher:
			1. Danh sách các Teacher của trung tâm như Tên, Tuổi, SĐT, số Căn cước (CCCD), địa chỉ liên hệ, khóa học đăng đảm nhiệm dạy.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Chỉ Admin mới có thể assign / un-assign các khóa học cho Teacher được chọn, hoặc thêm, xóa, sửa Teacher.
			4. Mọi thao tác assign / un-assign khóa học / tạo mới tài khoản Teacher cũng phải có thông báo gửi xuống group zalo và app điện thoại mà Teacher đó đã cài đặt.
			5. Một Teacher có thể dạy được nhiều khóa học 1 lúc.
			6. Mọi thao tác assign / un-assign khóa học / tạo mới tài khoản Teacher cũng phải có thông báo gửi xuống group zalo và app điện thoại mà Teacher đó đã cài đặt.
		+ Quản lý Student:
			1. Danh sách các Student của trung tâm như Tên, Tuổi, SĐT, số Căn cước (CCCD), địa chỉ liên hệ, khóa học đã đăng ký, Teacher đang dạy kháo học đó.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Admin, Manager có thể thêm, xóa, sửa học viên, hoặc đăng ký khóa học có sẵn cho học viên được chọn. 1 Student có thể được đăng ký nhiều khóa học cùng lúc.
			4. Assign / Un-assign học viên, đăng ký học viên mới đều phải có thông báo gửi xuống group zalo và app điện thoại mà học viên đó đã cài đặt.
		+ Quản lý khuyến mãi:
			1. Danh sách các khuyến mãi gồm tên chương trình, mô tả, điều kiện, thời gian hiệu lực từ ngày nào đến ngày nào. Không nhập thời gian hiệu lực thì coi như khuyến mãi vẫn còn hiệu lực mãi.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Chỉ Admin, Magager có thể thêm, xóa, sửa
			4. Khi thêm, sửa khuyến mãi thì thông báo xuống group zalo và app ĐT của mọi role trừ System Admin
		+ Quản lý thông báo:
			1. Danh sách các thông báo như tên, nội dung thông báo, thời gian hiệu lực từ ngày nào đến ngày nào. Không nhập thời gian hiệu lực thì coi như thông báo vẫn còn hiệu lực mãi.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Chỉ Admin, Magager có thể thêm, xóa, sửa
			4. Khi thêm, sửa khuyến mãi thì thông báo xuống group zalo và app ĐT của mọi role trừ System Admin
		+ AI CSKH:
			1. Hiển thị float AI chat, có tích hợp AI để môi role có thể hỏi đáp thông tin về khóa học, giáo viên hay trung tâm
			2. Tích hợp AI để trả lời cho các câu hỏi thông tin về khóa học, giáo viên hay trung tâm
	- Phân app ĐT:
		+ Các màn hình và menu tương tự như phần web quản lý, cũng áp dụng các role y change
		+ Responsive các màn hình, tương ứng với các role, màn hình y như phần web
		+ Có thể nhận thông báo từ web gửi xuống

----------------------------------

## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

Your output MUST follow this exact Markdown structure for Phase 3:
## PHASE 3 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
#### 4. Phase Definition of Done (DoD)

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 3 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 3 is to develop the frontend of the membership-hub platform, ensuring a seamless user experience across both web and mobile applications. This phase will focus on creating responsive and user-friendly interfaces using Next.js, aligning with the established requirements and tech stack. The key deliverables include:
- Development of the web frontend for managing learning centers, including features for user authentication, course management, attendance tracking, and notification systems.
- Development of the mobile frontend for learners, incorporating features such as responsive design, user profiles, course enrollment, and push notifications.
- Implementation of multi-language support for both web and mobile applications.
- Integration of the frontend with the backend services developed in Phase 2, ensuring smooth data exchange and functionality.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 3 includes:
- Frontend development using Next.js for both web and mobile applications.
- Utilization of React for building reusable UI components.
- Integration with the backend API endpoints developed in Phase 2 for data retrieval and manipulation.
- Implementation of authentication and authorization mechanisms to ensure secure access to features based on user roles.
- Directory structure:
  - `frontend/`
    - `web/`
      - `components/`
      - `pages/`
      - `styles/`
    - `mobile/`
      - `components/`
      - `screens/`
      - `styles/`
  - `public/`
  - `package.json`
- Endpoints for integration with the backend:
  - `/api/auth`
  - `/api/courses`
  - `/api/attendance`
  - `/api/notifications`

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
- **Coder**: Develop the frontend components, pages, and screens for both web and mobile applications. Implement authentication, course management, attendance tracking, and notification features. Ensure responsive design and multi-language support.
- **Tester**: Develop and execute test cases for the frontend, focusing on UI/UX, functionality, and integration with the backend. Perform unit tests, integration tests, and UI tests.
- **Reviewer**: Conduct code reviews to ensure the frontend code is maintainable, efficient, and adheres to the project's coding standards. Verify that the implementation meets the requirements and is properly integrated with the backend.
- **DevOps**: Set up the environment for frontend development, including the necessary dependencies and tools. Ensure the frontend is properly integrated with the backend and can be deployed to the production environment.

#### 4. Phase Definition of Done (DoD)
Phase 3 is considered complete when:
- The web and mobile frontend applications are fully developed and tested.
- All required features, including user authentication, course management, attendance tracking, and notification systems, are implemented and functioning as expected.
- The frontend is properly integrated with the backend API endpoints.
- Code reviews have been conducted, and the codebase is deemed maintainable and efficient.
- The application is deployable to the production environment.
- Documentation for the frontend development, including component libraries and API integrations, is updated and available.
```

# Phase 4 - Prompt:

Project Name: membership-hub
You are tasked to detail **PHASE 4 OUT OF 5**.
You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

--- GLOBAL CONTEXT REFERENCE ---
## GLOBAL PROJECT CONTEXT: membership-hub
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a comprehensive platform designed to manage and facilitate learning centers, supporting multiple centers simultaneously. The platform will have both web and mobile applications, utilizing Java 17, Quarkus, Kafka, and Postgres for the backend, with Docker and GCP (Google Cloud Platform) for deployment. The tech stack also includes Next.js for the mobile frontend, ensuring a seamless user experience across various devices. Key features include user authentication, course management, attendance tracking, and notification systems.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to best practices, the following guardrails are established:
- **Security**: Implement robust security measures to protect user data, including encryption, secure authentication protocols, and regular security audits.
- **Scalability**: Design the system to scale horizontally, leveraging cloud services to handle increased traffic and user growth.
- **Compliance**: Adhere to relevant data protection regulations, such as GDPR and CCPA, ensuring user privacy and data security.
- **Quality Assurance**: Implement a rigorous testing framework, including unit tests, integration tests, and UI tests, to ensure high-quality code and minimal bugs.
- **Documentation**: Maintain comprehensive documentation of the codebase, including comments, API documentation, and user manuals.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas are defined to ensure clear roles and responsibilities within the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project is delivered on time, within budget, and meets the required quality standards.
- **Coder**: Responsible for writing high-quality, efficient, and well-documented code. Collaborates with the testing team to identify and fix bugs.
- **Tester**: Develops and executes comprehensive testing plans to ensure the software meets the required quality and functionality standards.
- **Reviewer**: Conducts code reviews to ensure that the code is maintainable, efficient, and adheres to the project's coding standards.
- **DevOps**: Focuses on the deployment, operation, and maintenance of the software system, ensuring high availability, performance, and security.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be segmented into exactly 5 phases, each with a strict duration limit of 1 to 7 days. The phases are designed to ensure a logical progression of the project, from planning to deployment.
- **Phase 1: Planning and Requirements Gathering** (Day 1-2)
  - Define project scope, goals, and timelines.
  - Gather and document all requirements.
- **Phase 2: Backend Development** (Day 3-5)
  - Develop the backend using Java 17, Quarkus, Kafka, and Postgres.
  - Implement authentication, course management, and attendance tracking features.
- **Phase 3: Frontend Development** (Day 6-10, compressed to fit within 7 days)
  - Develop the web and mobile frontend using Next.js.
  - Ensure responsive design and user-friendly interfaces.
- **Phase 4: Testing and Quality Assurance** (Day 11-14, compressed to fit within 7 days)
  - Conduct unit tests, integration tests, and UI tests.
  - Identify and fix bugs to ensure high-quality code.
- **Phase 5: Deployment and Maintenance** (Day 15-21, compressed to fit within 7 days)
  - Deploy the application on GCP.
  - Ensure scalability, security, and high availability.
  - Plan for post-deployment maintenance and updates.

--- RAW REQUIREMENTS REFERENCE ---
## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile (app ĐT) để học viên xài.
	- Project này xây dựng backend bằng java 17, quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm frontend, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.
	- Phần web quản lý có quản lý lịch dạy và học, khuyến mãi các khóa học, thông báo của admin. Khi admin thông báo, tin nhắn sẽ được trigger gửi xuống group zalo của các học viên, đồng thời thông báo xuống app trên dt của học viên.
	- Phần web quản lý cũng có quản lý tiết học như tiết đó thầy cô nào dạy, từ mấy giờ đến mấy giờ.
	- Có quản lý điểm royalty của học viên. Học viên cứ đăng ký 1 khóa học sẽ được công 10 điểm. Có cả phần quản lý đăng ký khóa học, bao gồm học viên nào đăng ký khóa học nào do thầy cô nào dạy, thời gian khóa học từ ngày nào tới ngày nào.
	- Phần web quản lý sẽ có các role:
		+ System Admin (SysAdmin): là quyền cao nhất, toàn quyền trên tất cả các trung tâm.
		+ Admin: là quyền cao nhất của 1 trung tâm, toàn quyền trên trung tâm đó nhưng không có quyền trên các trung tâm khác
		+ Manager: là quyền quản lý của trung tâm, dưới quyền Admin, không có quyền chỉnh sửa thông tin khóa học, chỉ có quyền thông báo, và quản lý học viên, đăng ký học viên cho khóa học có sẵn, nhưng không có quyền phân công thầy cô dạy.
		+ Teacher: là quyền của các giáo viên, chỉ có thể xem lịch học, lịch dạy, danh sách học viên tham gia khóa học của mình. Chỉ quyền xem, không được chỉnh sửa, xóa hay tạo
		+ Student: là quyền của học viên. Chỉ được xem thông tin các khóa học, thầy cô nào dạy, có thể đăng ký khóa học mới. Và xem được thông tin thẻ của mình còn bao nhiêu ngày. Có thể đăng ký gia hạn ngày cho thẻ học viên.
	- Phần web quản lý sẽ có các màn hình:
		+ Quản lý trung tâm:
			1. Hiển thị danh sách các trung tâm, địa chỉ, mã số thuế, ai là người Admin của trung tâm đó, thông tin liên hệ của người Admin đó.
			2. Có thể thêm, xóa, sửa trung tâm.
			3. Có thể assign / un-assign Admin của trung tâm.
			4. Màn hình này ẩn với tất cả các role khác, ngoại trừ System Admin.
		+ Thông tin trung tâm:
			1. Chỉnh sửa thông tin trung tâm như tên, địa chỉ, số điện thoại (SĐT), mã số thuế (MST) chỉ bằng quyền Admin.
			2. Có thể assign / un-assign Manager cho trung tâm chỉ bằng quyền Admin.
			3. Trang này hiển thị cho mọi role như Admin, Manager, Teacher, Student, nhưng chỉ Admin của trung tâm có quyền thêm, xóa, sửa, assign / un-assign Manager.
		+ Dashboard:
			1. Hiển thị thông tin khóa học đang diễn ra ngày hiện tại
			2. Thông tin Teacher dạy khóa học nào của ngày hiện tại
			3. Nếu là Student, hiện thị hình ảnh thẻ kèm thòi gian còn hiệu lực của thẻ học viên.
			4. Hiển thị các chương trình khuyến mãi, thông báo
			5. Tự động cập nhật thông tin theo thời gian thực, interval 15 phút, interval value này có thể input từ enviroment.
		+ Quản lý khóa học:
			1. Danh sách các khóa học, thời gian diễn ra khóa học, thầy cô nào dạy khóa học nào.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Chỉ có Admin mới có thể thêm, sửa, xóa khóa học, đặc biệt quan trọng là tránh trùng lắp overlap thời gian các khóa học, assign / un-assign Teacher cho khóa học.
			4. Manager có thể chọn khóa học và đăng ký học viên cho khóa học đó. Có thể chọn từ học viên có sẵn hoặc đăng ký mới. Nếu đăng ký mới thì sẽ tự động tạo tài khoản role Student cho học viên đó và assign học viên cho khóa học đó.
			5. Assign / Un-assign học viên, đăng ký học viên mới đều phải có thông báo gửi xuống group zalo và app điện thoại mà học viên đó đã cài đặt.
			6. Admin có thể assign / un-assign Teacher dạy khóa học, có thể chọn từ Teacher có sẵn hoặc assign Teacher mới. Lúc đó sẽ tự động tạo tài khoản mới role Teacher và assign Teacher cho kháo học đó.
			7. Mọi thao tác assign / un-assign khóa học / tạo mới tài khoản Teacher cũng phải có thông báo gửi xuống group zalo và app điện thoại mà Teacher đó đã cài đặt.
		+ Quản lý Teacher:
			1. Danh sách các Teacher của trung tâm như Tên, Tuổi, SĐT, số Căn cước (CCCD), địa chỉ liên hệ, khóa học đăng đảm nhiệm dạy.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Chỉ Admin mới có thể assign / un-assign các khóa học cho Teacher được chọn, hoặc thêm, xóa, sửa Teacher.
			4. Mọi thao tác assign / un-assign khóa học / tạo mới tài khoản Teacher cũng phải có thông báo gửi xuống group zalo và app điện thoại mà Teacher đó đã cài đặt.
			5. Một Teacher có thể dạy được nhiều khóa học 1 lúc.
			6. Mọi thao tác assign / un-assign khóa học / tạo mới tài khoản Teacher cũng phải có thông báo gửi xuống group zalo và app điện thoại mà Teacher đó đã cài đặt.
		+ Quản lý Student:
			1. Danh sách các Student của trung tâm như Tên, Tuổi, SĐT, số Căn cước (CCCD), địa chỉ liên hệ, khóa học đã đăng ký, Teacher đang dạy kháo học đó.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Admin, Manager có thể thêm, xóa, sửa học viên, hoặc đăng ký khóa học có sẵn cho học viên được chọn. 1 Student có thể được đăng ký nhiều khóa học cùng lúc.
			4. Assign / Un-assign học viên, đăng ký học viên mới đều phải có thông báo gửi xuống group zalo và app điện thoại mà học viên đó đã cài đặt.
		+ Quản lý khuyến mãi:
			1. Danh sách các khuyến mãi gồm tên chương trình, mô tả, điều kiện, thời gian hiệu lực từ ngày nào đến ngày nào. Không nhập thời gian hiệu lực thì coi như khuyến mãi vẫn còn hiệu lực mãi.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Chỉ Admin, Magager có thể thêm, xóa, sửa
			4. Khi thêm, sửa khuyến mãi thì thông báo xuống group zalo và app ĐT của mọi role trừ System Admin
		+ Quản lý thông báo:
			1. Danh sách các thông báo như tên, nội dung thông báo, thời gian hiệu lực từ ngày nào đến ngày nào. Không nhập thời gian hiệu lực thì coi như thông báo vẫn còn hiệu lực mãi.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Chỉ Admin, Magager có thể thêm, xóa, sửa
			4. Khi thêm, sửa khuyến mãi thì thông báo xuống group zalo và app ĐT của mọi role trừ System Admin
		+ AI CSKH:
			1. Hiển thị float AI chat, có tích hợp AI để môi role có thể hỏi đáp thông tin về khóa học, giáo viên hay trung tâm
			2. Tích hợp AI để trả lời cho các câu hỏi thông tin về khóa học, giáo viên hay trung tâm
	- Phân app ĐT:
		+ Các màn hình và menu tương tự như phần web quản lý, cũng áp dụng các role y change
		+ Responsive các màn hình, tương ứng với các role, màn hình y như phần web
		+ Có thể nhận thông báo từ web gửi xuống

----------------------------------

## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

Your output MUST follow this exact Markdown structure for Phase 4:
## PHASE 4 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
#### 4. Phase Definition of Done (DoD)

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 4 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 4 is to conduct thorough testing and quality assurance of the membership-hub platform. This phase will focus on identifying and fixing bugs, ensuring the platform's stability, security, and performance. The scope includes:
- Unit testing of individual components
- Integration testing of interconnected components
- UI testing for user experience and interface validation
- Security testing to identify vulnerabilities
- Performance testing to ensure scalability and efficiency

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 4 includes:
- **Testing Framework**: Utilize testing frameworks such as JUnit for backend and Jest for frontend to write and execute tests.
- **Test Directory**: Create a separate directory for tests, e.g., `src/test/java` for backend and `__tests__` for frontend.
- **Test Endpoints**: Identify and test all API endpoints, including authentication, course management, attendance tracking, and notification systems.
- **Test Data**: Create mock data for testing purposes, ensuring it covers various scenarios and edge cases.
- **Security Testing Tools**: Utilize tools like OWASP ZAP for security testing and vulnerability assessment.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
- **Coder**: Assist in writing test cases, fixing bugs identified during testing, and ensuring code quality.
- **Tester**: Develop and execute comprehensive testing plans, including unit tests, integration tests, UI tests, security tests, and performance tests.
- **Reviewer**: Conduct code reviews to ensure tests are properly written, and code fixes are correctly implemented.
- **DevOps**: Focus on ensuring the testing environment is properly set up, and tests can be executed efficiently. Assist in deploying the application to a staging environment for testing.
- **Manager**: Oversee the testing process, ensure timely completion, and allocate resources as needed.

#### 4. Phase Definition of Done (DoD)
Phase 4 is considered complete when:
- All unit tests, integration tests, UI tests, security tests, and performance tests have been executed with satisfactory results.
- All identified bugs have been fixed, and the fixes have been verified through re-testing.
- Code reviews have been conducted, and all feedback has been incorporated.
- The application has been deployed to a staging environment for final testing and validation.
- A comprehensive test report has been generated, detailing all tests conducted, results, and any remaining issues.
```

# Phase 5 - Prompt:

Project Name: membership-hub
You are tasked to detail **PHASE 5 OUT OF 5**.
You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

--- GLOBAL CONTEXT REFERENCE ---
## GLOBAL PROJECT CONTEXT: membership-hub
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a comprehensive platform designed to manage and facilitate learning centers, supporting multiple centers simultaneously. The platform will have both web and mobile applications, utilizing Java 17, Quarkus, Kafka, and Postgres for the backend, with Docker and GCP (Google Cloud Platform) for deployment. The tech stack also includes Next.js for the mobile frontend, ensuring a seamless user experience across various devices. Key features include user authentication, course management, attendance tracking, and notification systems.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to best practices, the following guardrails are established:
- **Security**: Implement robust security measures to protect user data, including encryption, secure authentication protocols, and regular security audits.
- **Scalability**: Design the system to scale horizontally, leveraging cloud services to handle increased traffic and user growth.
- **Compliance**: Adhere to relevant data protection regulations, such as GDPR and CCPA, ensuring user privacy and data security.
- **Quality Assurance**: Implement a rigorous testing framework, including unit tests, integration tests, and UI tests, to ensure high-quality code and minimal bugs.
- **Documentation**: Maintain comprehensive documentation of the codebase, including comments, API documentation, and user manuals.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas are defined to ensure clear roles and responsibilities within the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project is delivered on time, within budget, and meets the required quality standards.
- **Coder**: Responsible for writing high-quality, efficient, and well-documented code. Collaborates with the testing team to identify and fix bugs.
- **Tester**: Develops and executes comprehensive testing plans to ensure the software meets the required quality and functionality standards.
- **Reviewer**: Conducts code reviews to ensure that the code is maintainable, efficient, and adheres to the project's coding standards.
- **DevOps**: Focuses on the deployment, operation, and maintenance of the software system, ensuring high availability, performance, and security.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be segmented into exactly 5 phases, each with a strict duration limit of 1 to 7 days. The phases are designed to ensure a logical progression of the project, from planning to deployment.
- **Phase 1: Planning and Requirements Gathering** (Day 1-2)
  - Define project scope, goals, and timelines.
  - Gather and document all requirements.
- **Phase 2: Backend Development** (Day 3-5)
  - Develop the backend using Java 17, Quarkus, Kafka, and Postgres.
  - Implement authentication, course management, and attendance tracking features.
- **Phase 3: Frontend Development** (Day 6-10, compressed to fit within 7 days)
  - Develop the web and mobile frontend using Next.js.
  - Ensure responsive design and user-friendly interfaces.
- **Phase 4: Testing and Quality Assurance** (Day 11-14, compressed to fit within 7 days)
  - Conduct unit tests, integration tests, and UI tests.
  - Identify and fix bugs to ensure high-quality code.
- **Phase 5: Deployment and Maintenance** (Day 15-21, compressed to fit within 7 days)
  - Deploy the application on GCP.
  - Ensure scalability, security, and high availability.
  - Plan for post-deployment maintenance and updates.

--- RAW REQUIREMENTS REFERENCE ---
## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile (app ĐT) để học viên xài.
	- Project này xây dựng backend bằng java 17, quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm frontend, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.
	- Phần web quản lý có quản lý lịch dạy và học, khuyến mãi các khóa học, thông báo của admin. Khi admin thông báo, tin nhắn sẽ được trigger gửi xuống group zalo của các học viên, đồng thời thông báo xuống app trên dt của học viên.
	- Phần web quản lý cũng có quản lý tiết học như tiết đó thầy cô nào dạy, từ mấy giờ đến mấy giờ.
	- Có quản lý điểm royalty của học viên. Học viên cứ đăng ký 1 khóa học sẽ được công 10 điểm. Có cả phần quản lý đăng ký khóa học, bao gồm học viên nào đăng ký khóa học nào do thầy cô nào dạy, thời gian khóa học từ ngày nào tới ngày nào.
	- Phần web quản lý sẽ có các role:
		+ System Admin (SysAdmin): là quyền cao nhất, toàn quyền trên tất cả các trung tâm.
		+ Admin: là quyền cao nhất của 1 trung tâm, toàn quyền trên trung tâm đó nhưng không có quyền trên các trung tâm khác
		+ Manager: là quyền quản lý của trung tâm, dưới quyền Admin, không có quyền chỉnh sửa thông tin khóa học, chỉ có quyền thông báo, và quản lý học viên, đăng ký học viên cho khóa học có sẵn, nhưng không có quyền phân công thầy cô dạy.
		+ Teacher: là quyền của các giáo viên, chỉ có thể xem lịch học, lịch dạy, danh sách học viên tham gia khóa học của mình. Chỉ quyền xem, không được chỉnh sửa, xóa hay tạo
		+ Student: là quyền của học viên. Chỉ được xem thông tin các khóa học, thầy cô nào dạy, có thể đăng ký khóa học mới. Và xem được thông tin thẻ của mình còn bao nhiêu ngày. Có thể đăng ký gia hạn ngày cho thẻ học viên.
	- Phần web quản lý sẽ có các màn hình:
		+ Quản lý trung tâm:
			1. Hiển thị danh sách các trung tâm, địa chỉ, mã số thuế, ai là người Admin của trung tâm đó, thông tin liên hệ của người Admin đó.
			2. Có thể thêm, xóa, sửa trung tâm.
			3. Có thể assign / un-assign Admin của trung tâm.
			4. Màn hình này ẩn với tất cả các role khác, ngoại trừ System Admin.
		+ Thông tin trung tâm:
			1. Chỉnh sửa thông tin trung tâm như tên, địa chỉ, số điện thoại (SĐT), mã số thuế (MST) chỉ bằng quyền Admin.
			2. Có thể assign / un-assign Manager cho trung tâm chỉ bằng quyền Admin.
			3. Trang này hiển thị cho mọi role như Admin, Manager, Teacher, Student, nhưng chỉ Admin của trung tâm có quyền thêm, xóa, sửa, assign / un-assign Manager.
		+ Dashboard:
			1. Hiển thị thông tin khóa học đang diễn ra ngày hiện tại
			2. Thông tin Teacher dạy khóa học nào của ngày hiện tại
			3. Nếu là Student, hiện thị hình ảnh thẻ kèm thòi gian còn hiệu lực của thẻ học viên.
			4. Hiển thị các chương trình khuyến mãi, thông báo
			5. Tự động cập nhật thông tin theo thời gian thực, interval 15 phút, interval value này có thể input từ enviroment.
		+ Quản lý khóa học:
			1. Danh sách các khóa học, thời gian diễn ra khóa học, thầy cô nào dạy khóa học nào.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Chỉ có Admin mới có thể thêm, sửa, xóa khóa học, đặc biệt quan trọng là tránh trùng lắp overlap thời gian các khóa học, assign / un-assign Teacher cho khóa học.
			4. Manager có thể chọn khóa học và đăng ký học viên cho khóa học đó. Có thể chọn từ học viên có sẵn hoặc đăng ký mới. Nếu đăng ký mới thì sẽ tự động tạo tài khoản role Student cho học viên đó và assign học viên cho khóa học đó.
			5. Assign / Un-assign học viên, đăng ký học viên mới đều phải có thông báo gửi xuống group zalo và app điện thoại mà học viên đó đã cài đặt.
			6. Admin có thể assign / un-assign Teacher dạy khóa học, có thể chọn từ Teacher có sẵn hoặc assign Teacher mới. Lúc đó sẽ tự động tạo tài khoản mới role Teacher và assign Teacher cho kháo học đó.
			7. Mọi thao tác assign / un-assign khóa học / tạo mới tài khoản Teacher cũng phải có thông báo gửi xuống group zalo và app điện thoại mà Teacher đó đã cài đặt.
		+ Quản lý Teacher:
			1. Danh sách các Teacher của trung tâm như Tên, Tuổi, SĐT, số Căn cước (CCCD), địa chỉ liên hệ, khóa học đăng đảm nhiệm dạy.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Chỉ Admin mới có thể assign / un-assign các khóa học cho Teacher được chọn, hoặc thêm, xóa, sửa Teacher.
			4. Mọi thao tác assign / un-assign khóa học / tạo mới tài khoản Teacher cũng phải có thông báo gửi xuống group zalo và app điện thoại mà Teacher đó đã cài đặt.
			5. Một Teacher có thể dạy được nhiều khóa học 1 lúc.
			6. Mọi thao tác assign / un-assign khóa học / tạo mới tài khoản Teacher cũng phải có thông báo gửi xuống group zalo và app điện thoại mà Teacher đó đã cài đặt.
		+ Quản lý Student:
			1. Danh sách các Student của trung tâm như Tên, Tuổi, SĐT, số Căn cước (CCCD), địa chỉ liên hệ, khóa học đã đăng ký, Teacher đang dạy kháo học đó.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Admin, Manager có thể thêm, xóa, sửa học viên, hoặc đăng ký khóa học có sẵn cho học viên được chọn. 1 Student có thể được đăng ký nhiều khóa học cùng lúc.
			4. Assign / Un-assign học viên, đăng ký học viên mới đều phải có thông báo gửi xuống group zalo và app điện thoại mà học viên đó đã cài đặt.
		+ Quản lý khuyến mãi:
			1. Danh sách các khuyến mãi gồm tên chương trình, mô tả, điều kiện, thời gian hiệu lực từ ngày nào đến ngày nào. Không nhập thời gian hiệu lực thì coi như khuyến mãi vẫn còn hiệu lực mãi.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Chỉ Admin, Magager có thể thêm, xóa, sửa
			4. Khi thêm, sửa khuyến mãi thì thông báo xuống group zalo và app ĐT của mọi role trừ System Admin
		+ Quản lý thông báo:
			1. Danh sách các thông báo như tên, nội dung thông báo, thời gian hiệu lực từ ngày nào đến ngày nào. Không nhập thời gian hiệu lực thì coi như thông báo vẫn còn hiệu lực mãi.
			2. Hiển thị với tất cả các role Admin, Manager, Teacher, Student để xem.
			3. Chỉ Admin, Magager có thể thêm, xóa, sửa
			4. Khi thêm, sửa khuyến mãi thì thông báo xuống group zalo và app ĐT của mọi role trừ System Admin
		+ AI CSKH:
			1. Hiển thị float AI chat, có tích hợp AI để môi role có thể hỏi đáp thông tin về khóa học, giáo viên hay trung tâm
			2. Tích hợp AI để trả lời cho các câu hỏi thông tin về khóa học, giáo viên hay trung tâm
	- Phân app ĐT:
		+ Các màn hình và menu tương tự như phần web quản lý, cũng áp dụng các role y change
		+ Responsive các màn hình, tương ứng với các role, màn hình y như phần web
		+ Có thể nhận thông báo từ web gửi xuống

----------------------------------

## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

Your output MUST follow this exact Markdown structure for Phase 5:
## PHASE 5 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
#### 4. Phase Definition of Done (DoD)

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 5 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 5 is to deploy the membership-hub application on Google Cloud Platform (GCP) while ensuring scalability, security, and high availability. This phase involves setting up the production environment, configuring Docker and Kubernetes, and deploying the application. Additionally, this phase will focus on planning for post-deployment maintenance and updates.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 5 includes:
- Deploying the application on GCP using Docker and Kubernetes
- Configuring load balancing, autoscaling, and monitoring
- Setting up security measures such as encryption, firewalls, and access controls
- Creating a backup and disaster recovery plan
- Defining API endpoints for the production environment
- Updating the documentation to reflect the production deployment

Allowed directories and files include:
- `docker-compose.yml` for defining Docker services
- `kubernetes/deployment.yaml` for defining Kubernetes deployments
- `kubernetes/service.yaml` for defining Kubernetes services
- `gcp/deployment.py` for automating GCP deployment
- `config/prod.env` for production environment configuration

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
- **Coder**: Focus on creating automated deployment scripts for GCP, updating the Docker configuration, and implementing security measures.
- **Tester**: Conduct thorough testing of the application in the production environment, including load testing, security testing, and functionality testing.
- **Reviewer**: Review the deployment scripts, Docker configuration, and security measures to ensure they meet the project's standards and best practices.
- **DevOps**: Set up the production environment on GCP, configure Kubernetes, and deploy the application. Additionally, focus on monitoring, logging, and backup strategies.
- **Manager**: Oversee the deployment process, ensure that the application is deployed on time, and coordinate with the team to resolve any issues that arise during deployment.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 5 includes:
- The application is successfully deployed on GCP.
- The application is scalable, secure, and highly available.
- Load balancing, autoscaling, and monitoring are configured.
- Security measures such as encryption, firewalls, and access controls are in place.
- A backup and disaster recovery plan is created and tested.
- API endpoints are defined and documented for the production environment.
- The documentation is updated to reflect the production deployment.
- Thorough testing has been conducted, and any issues have been resolved.
- The team has reviewed and approved the deployment configuration and security measures.
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Based on the provided Phase 1 Context Markdown content, I will extract and translate the daily steps, checklists, and agent tasks into a precise, executable JSON schema.

Since the Markdown content does not explicitly mention specific days, I will assume that the tasks and activities described are to be performed on a single day, which will be represented as "day": 1 in the JSON output.

Here is the translated JSON schema:

```json
{
  "phase_id": 1,
  "phase_name": "Phase 1",
  "project_name": "membership-hub",
  "global_context_file": "{global_context_file}",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": "{project_phase_context_file}",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "task-1",
          "agent": "Manager",
          "desc": "Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.",
          "components": []
        },
        {
          "id": "task-2",
          "agent": "Coder",
          "desc": "Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.",
          "components": []
        },
        {
          "id": "task-3",
          "agent": "Tester",
          "desc": "Review the project requirements and provide input on the testing strategy and approach.",
          "components": []
        },
        {
          "id": "task-4",
          "agent": "Reviewer",
          "desc": "Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.",
          "components": []
        },
        {
          "id": "task-5",
          "agent": "DevOps",
          "desc": "Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.",
          "components": []
        }
      ]
    }
  ]
}
```

Note that I have followed the required JSON schema layout design structure and populated the fields accordingly. Since there are no explicit day numbers mentioned in the Markdown content, I have assumed a single day ("day": 1) for all tasks and activities. If there were multiple days mentioned, I would have created separate day objects in the "days" array, each with its own set of sub-tasks and context information.
```

# Phase 2 STEPS - Prompt:

Analyze the attached Phase 2 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 2 CONTEXT MARKDOWN ---
## PHASE 2 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend of the membership-hub project using Java 17, Quarkus, Kafka, and Postgres. This phase will focus on implementing the core features, including user authentication, course management, attendance tracking, and notification systems. The scope of this phase includes designing and implementing the database schema, creating RESTful APIs for backend services, and integrating Kafka for event-driven architecture.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 2 includes:
- **Database Schema Design**: Designing the Postgres database schema to support user authentication, course management, attendance tracking, and notification systems.
- **Backend API Development**: Creating RESTful APIs using Java 17 and Quarkus for user authentication, course management, attendance tracking, and notification systems.
- **Kafka Integration**: Integrating Kafka for event-driven architecture to handle notifications and attendance tracking.
- **Directory Structure**:
  - `src/main/java`: Java source files for the backend application.
  - `src/main/resources`: Configuration files and database schema definitions.
  - `src/test/java`: Unit tests and integration tests for the backend application.
- **Endpoints**:
  - `/api/auth`: User authentication endpoints.
  - `/api/courses`: Course management endpoints.
  - `/api/attendance`: Attendance tracking endpoints.
  - `/api/notifications`: Notification system endpoints.

#### 3. Dedicated Sub-Agent Functional Directives
The following sub-agents will be involved in Phase 2:
- **Coder**: Responsible for designing and implementing the database schema, creating RESTful APIs, and integrating Kafka.
- **Tester**: Responsible for creating unit tests and integration tests for the backend application.
- **Reviewer**: Responsible for reviewing the code and ensuring it meets the project's coding standards and best practices.
- **DevOps**: Responsible for setting up the development environment, configuring Kafka, and ensuring the backend application is deployable.

#### 4. Phase Definition of Done (DoD)
Phase 2 is considered complete when:
- The database schema is designed and implemented.
- RESTful APIs for user authentication, course management, attendance tracking, and notification systems are created and tested.
- Kafka is integrated for event-driven architecture.
- Unit tests and integration tests are written and passed.
- Code reviews are completed, and the code meets the project's coding standards and best practices.
- The backend application is deployable and configured for further development.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Based on the provided Phase 2 Context Markdown content, I will extract and translate the daily steps, checklists, and agent tasks into a precise, executable JSON schema.

Since the Markdown content does not explicitly mention daily steps, I will parse the paragraph descriptions into technical sub-tasks for each day. I will assume that the phase starts from Day 1 and progresses logically.

Here is the translated JSON schema:
```json
{
  "phase_id": 2,
  "phase_name": "Phase 2",
  "project_name": "membership-hub",
  "global_context_file": "{global_context_file}",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": "{project_phase_context_file}",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "Task 1.1",
          "agent": "Coder",
          "desc": "Design database schema for user authentication",
          "components": [
            "src/main/resources/database_schema.sql"
          ]
        },
        {
          "id": "Task 1.2",
          "agent": "DevOps",
          "desc": "Set up development environment",
          "components": [
            "src/main/java",
            "src/main/resources"
          ]
        }
      ]
    },
    {
      "day": 2,
      "context_file": "{project_phase_context_file}",
      "context_section": "DAY 2",
      "sub_tasks": [
        {
          "id": "Task 2.1",
          "agent": "Coder",
          "desc": "Create RESTful APIs for user authentication",
          "components": [
            "src/main/java/com/membership/hub/auth/AuthController.java"
          ]
        },
        {
          "id": "Task 2.2",
          "agent": "Tester",
          "desc": "Write unit tests for user authentication APIs",
          "components": [
            "src/test/java/com/membership/hub/auth/AuthControllerTest.java"
          ]
        }
      ]
    },
    {
      "day": 3,
      "context_file": "{project_phase_context_file}",
      "context_section": "DAY 3",
      "sub_tasks": [
        {
          "id": "Task 3.1",
          "agent": "Coder",
          "desc": "Integrate Kafka for event-driven architecture",
          "components": [
            "src/main/java/com/membership/hub/kafka/KafkaProducer.java"
          ]
        },
        {
          "id": "Task 3.2",
          "agent": "DevOps",
          "desc": "Configure Kafka for notification systems",
          "components": [
            "src/main/resources/kafka.properties"
          ]
        }
      ]
    },
    {
      "day": 4,
      "context_file": "{project_phase_context_file}",
      "context_section": "DAY 4",
      "sub_tasks": [
        {
          "id": "Task 4.1",
          "agent": "Coder",
          "desc": "Create RESTful APIs for course management",
          "components": [
            "src/main/java/com/membership/hub/courses/CourseController.java"
          ]
        },
        {
          "id": "Task 4.2",
          "agent": "Tester",
          "desc": "Write unit tests for course management APIs",
          "components": [
            "src/test/java/com/membership/hub/courses/CourseControllerTest.java"
          ]
        }
      ]
    },
    {
      "day": 5,
      "context_file": "{project_phase_context_file}",
      "context_section": "DAY 5",
      "sub_tasks": [
        {
          "id": "Task 5.1",
          "agent": "Coder",
          "desc": "Create RESTful APIs for attendance tracking",
          "components": [
            "src/main/java/com/membership/hub/attendance/AttendanceController.java"
          ]
        },
        {
          "id": "Task 5.2",
          "agent": "Reviewer",
          "desc": "Review code for attendance tracking APIs",
          "components": [
            "src/main/java/com/membership/hub/attendance/AttendanceController.java"
          ]
        }
      ]
    },
    {
      "day": 6,
      "context_file": "{project_phase_context_file}",
      "context_section": "DAY 6",
      "sub_tasks": [
        {
          "id": "Task 6.1",
          "agent": "Coder",
          "desc": "Create RESTful APIs for notification systems",
          "components": [
            "src/main/java/com/membership/hub/notifications/NotificationController.java"
          ]
        },
        {
          "id": "Task 6.2",
          "agent": "DevOps",
          "desc": "Ensure backend application is deployable",
          "components": [
            "src/main/java",
            "src/main/resources"
          ]
        }
      ]
    },
    {
      "day": 7,
      "context_file": "{project_phase_context_file}",
      "context_section": "DAY 7",
      "sub_tasks": [
        {
          "id": "Task 7.1",
          "agent": "Tester",
          "desc": "Write integration tests for backend application",
          "components": [
            "src/test/java/com/membership/hub/IntegrationTest.java"
          ]
        },
        {
          "id": "Task 7.2",
          "agent": "Reviewer",
          "desc": "Review code for entire backend application",
          "components": [
            "src/main/java",
            "src/main/resources"
          ]
        }
      ]
    }
  ]
}
```
Note that I have assumed a 7-day phase duration, with each day having multiple sub-tasks assigned to different agents. The `context_file` and `context_section` fields are populated accordingly, and the `sub_tasks` array contains the detailed tasks for each day. The `components` array is populated with the relevant file paths or scripts modified or targeted by each task.
```

# Phase 3 STEPS - Prompt:

Analyze the attached Phase 3 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 3 CONTEXT MARKDOWN ---
## PHASE 3 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 3 is to develop the frontend of the membership-hub platform, ensuring a seamless user experience across both web and mobile applications. This phase will focus on creating responsive and user-friendly interfaces using Next.js, aligning with the established requirements and tech stack. The key deliverables include:
- Development of the web frontend for managing learning centers, including features for user authentication, course management, attendance tracking, and notification systems.
- Development of the mobile frontend for learners, incorporating features such as responsive design, user profiles, course enrollment, and push notifications.
- Implementation of multi-language support for both web and mobile applications.
- Integration of the frontend with the backend services developed in Phase 2, ensuring smooth data exchange and functionality.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 3 includes:
- Frontend development using Next.js for both web and mobile applications.
- Utilization of React for building reusable UI components.
- Integration with the backend API endpoints developed in Phase 2 for data retrieval and manipulation.
- Implementation of authentication and authorization mechanisms to ensure secure access to features based on user roles.
- Directory structure:
  - `frontend/`
    - `web/`
      - `components/`
      - `pages/`
      - `styles/`
    - `mobile/`
      - `components/`
      - `screens/`
      - `styles/`
  - `public/`
  - `package.json`
- Endpoints for integration with the backend:
  - `/api/auth`
  - `/api/courses`
  - `/api/attendance`
  - `/api/notifications`

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
- **Coder**: Develop the frontend components, pages, and screens for both web and mobile applications. Implement authentication, course management, attendance tracking, and notification features. Ensure responsive design and multi-language support.
- **Tester**: Develop and execute test cases for the frontend, focusing on UI/UX, functionality, and integration with the backend. Perform unit tests, integration tests, and UI tests.
- **Reviewer**: Conduct code reviews to ensure the frontend code is maintainable, efficient, and adheres to the project's coding standards. Verify that the implementation meets the requirements and is properly integrated with the backend.
- **DevOps**: Set up the environment for frontend development, including the necessary dependencies and tools. Ensure the frontend is properly integrated with the backend and can be deployed to the production environment.

#### 4. Phase Definition of Done (DoD)
Phase 3 is considered complete when:
- The web and mobile frontend applications are fully developed and tested.
- All required features, including user authentication, course management, attendance tracking, and notification systems, are implemented and functioning as expected.
- The frontend is properly integrated with the backend API endpoints.
- Code reviews have been conducted, and the codebase is deemed maintainable and efficient.
- The application is deployable to the production environment.
- Documentation for the frontend development, including component libraries and API integrations, is updated and available.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 429 - {'error': {'message': 'Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx7x6rbpftmr50sr2yyb78qm` service tier `on_demand` on tokens per minute (TPM): Limit 12000, Used 8135, Requested 6460. Please try again in 12.975s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 404 - {'error': {'message': 'This model is unavailable for free. The paid version is available now - use this slug instead: meta-llama/llama-3.3-70b-instruct', 'code': 404}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 523. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 477. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 942. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 942. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 1177. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 753. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 167. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 530. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 523. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 404 - {'error': {'message': 'This model is unavailable for free. The paid version is available now - use this slug instead: qwen/qwen-2.5-coder-32b-instruct', 'code': 404}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 376. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 404 - {'error': {'message': 'This model is unavailable for free. The paid version is available now - use this slug instead: deepseek/deepseek-r1', 'code': 404}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 400 - {'error': {'message': 'google/gemma-4-31b-instruct is not a valid model ID', 'code': 400}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 157. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
{
    "$defs": {
        "DailyStep": {
            "properties": {
                "day": {
                    "description": "Timeline iteration day inside this isolated phase.",
                    "title": "Day",
                    "type": "integer"
                },
                "context_file": {
                    "description": "The phase context Markdown file for closure on this day.",
                    "title": "Context File",
                    "type": "string"
                },
                "context_section": {
                    "description": "The day targeted for closure on this day.",
                    "title": "Context Section",
                    "type": "string"
                },
                "sub_tasks": {
                    "description": "Array of isolated micro-tasks assigned to sub-agents.",
                    "items": {
                        "$ref": "#/$defs/SubAgentTask"
                    },
                    "title": "Sub Tasks",
                    "type": "array"
                }
            },
            "required": [
                "day",
                "context_file",
                "context_section",
                "sub_tasks"
            ],
            "title": "DailyStep",
            "type": "object"
        },
        "SubAgentTask": {
            "properties": {
                "id": {
                    "description": "Sub-Task identity of Task that sub-agent role executing.",
                    "title": "Id",
                    "type": "string"
                },
                "agent": {
                    "description": "Target sub-agent role executing the task.",
                    "title": "Agent",
                    "type": "string"
                },
                "desc": {
                    "description": "Literal, low-level technical step assigned to the agent.",
                    "title": "Desc",
                    "type": "string"
                },
                "components": {
                    "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
                    "items": {
                        "type": "string"
                    },
                    "title": "Components",
                    "type": "array"
                }
            },
            "required": [
                "id",
                "agent",
                "desc"
            ],
            "title": "SubAgentTask",
            "type": "object"
        }
    },
    "phase_id": 1,
    "phase_name": "Phase 1",
    "project_name": "membership-hub",
    "global_context_file": "{global_context_file}",
    "source_target_dir": "sources/",
    "days": [
        {
            "day": 1,
            "context_file": "{project_phase_context_file}",
            "context_section": "DAY 1",
            "sub_tasks": [
                {
                    "id": "task-1",
                    "agent": "Manager",
                    "desc": "Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.",
                    "components": []
                },
                {
                    "id": "task-2",
                    "agent": "Coder",
                    "desc": "Review the project requirements and provide input on technical feasibility; assist in creation of the high-level project plan and directory structure.",
                    "components": []
                },
                {
                    "id": "task-3",
                    "agent": "Tester",
                    "desc": "Review the project requirements and provide input on the testing strategy and approach.",
                    "components": []
                },
                {
                    "id": "task-4",
                    "agent": "Reviewer",
                    "desc": "Review the project plan and directory structure to ensure they align with the project's objectives and requirements.",
                    "components": []
                },
                {
                    "id": "task-5",
                    "agent": "DevOps",
                    "desc": "Assist in establishing the project's directory structure and ensure necessary tools and frameworks are in place to support the project.",
                    "components": []
                }
            ]
        }
    ]
}
```

# Phase 2 STEPS - Prompt:

Analyze the attached Phase 2 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 2 CONTEXT MARKDOWN ---
## PHASE 2 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend of the membership-hub project using Java 17, Quarkus, Kafka, and Postgres. This phase will focus on implementing the core features, including user authentication, course management, attendance tracking, and notification systems. The scope of this phase includes designing and implementing the database schema, creating RESTful APIs for backend services, and integrating Kafka for event-driven architecture.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 2 includes:
- **Database Schema Design**: Designing the Postgres database schema to support user authentication, course management, attendance tracking, and notification systems.
- **Backend API Development**: Creating RESTful APIs using Java 17 and Quarkus for user authentication, course management, attendance tracking, and notification systems.
- **Kafka Integration**: Integrating Kafka for event-driven architecture to handle notifications and attendance tracking.
- **Directory Structure**:
  - `src/main/java`: Java source files for the backend application.
  - `src/main/resources`: Configuration files and database schema definitions.
  - `src/test/java`: Unit tests and integration tests for the backend application.
- **Endpoints**:
  - `/api/auth`: User authentication endpoints.
  - `/api/courses`: Course management endpoints.
  - `/api/attendance`: Attendance tracking endpoints.
  - `/api/notifications`: Notification system endpoints.

#### 3. Dedicated Sub-Agent Functional Directives
The following sub-agents will be involved in Phase 2:
- **Coder**: Responsible for designing and implementing the database schema, creating RESTful APIs, and integrating Kafka.
- **Tester**: Responsible for creating unit tests and integration tests for the backend application.
- **Reviewer**: Responsible for reviewing the code and ensuring it meets the project's coding standards and best practices.
- **DevOps**: Responsible for setting up the development environment, configuring Kafka, and ensuring the backend application is deployable.

#### 4. Phase Definition of Done (DoD)
Phase 2 is considered complete when:
- The database schema is designed and implemented.
- RESTful APIs for user authentication, course management, attendance tracking, and notification systems are created and tested.
- Kafka is integrated for event-driven architecture.
- Unit tests and integration tests are written and passed.
- Code reviews are completed, and the code meets the project's coding standards and best practices.
- The backend application is deployable and configured for further development.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
```json
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "#/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "phase_id": 2,
  "phase_name": "membership-hub",
  "project_name": "membership-hub",
  "global_context_file": "{global_context_file}",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": "{project_phase_context_file}",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "coder-db-schema",
          "agent": "Coder",
          "desc": "Design and implement the Postgres database schema for user authentication, course management, attendance tracking, and notifications.",
          "components": []
        },
        {
          "id": "coder-apis",
          "agent": "Coder",
          "desc": "Create RESTful APIs using Java 17 and Quarkus for authentication (/api/auth), courses (/api/courses), attendance (/api/attendance), and notifications (/api/notifications).",
          "components": []
        },
        {
          "id": "coder-kafka",
          "agent": "Coder",
          "desc": "Integrate Kafka for event-driven architecture to handle notifications and attendance tracking.",
          "components": []
        },
        {
          "id": "tester-unit-tests",
          "agent": "Tester",
          "desc": "Write unit tests for backend services covering authentication, course, attendance, and notification APIs.",
          "components": []
        },
        {
          "id": "tester-integration-tests",
          "agent": "Tester",
          "desc": "Write integration tests to verify end-to-end functionality of the backend services, including Kafka event flow.",
          "components": []
        },
        {
          "id": "reviewer-code-review",
          "agent": "Reviewer",
          "desc": "Review all code changes to ensure adherence to coding standards, best practices, and project guidelines.",
          "components": []
        },
        {
          "id": "devops-setup",
          "agent": "DevOps",
          "desc": "Set up development environment, configure Kafka broker, and ensure the Quarkus application is deployable.",
          "components": []
        }
      ]
    }
  ]
}
```
```

# Phase 3 STEPS - Prompt:

Analyze the attached Phase 3 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 3 CONTEXT MARKDOWN ---
## PHASE 3 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 3 is to develop the frontend of the membership-hub platform, ensuring a seamless user experience across both web and mobile applications. This phase will focus on creating responsive and user-friendly interfaces using Next.js, aligning with the established requirements and tech stack. The key deliverables include:
- Development of the web frontend for managing learning centers, including features for user authentication, course management, attendance tracking, and notification systems.
- Development of the mobile frontend for learners, incorporating features such as responsive design, user profiles, course enrollment, and push notifications.
- Implementation of multi-language support for both web and mobile applications.
- Integration of the frontend with the backend services developed in Phase 2, ensuring smooth data exchange and functionality.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 3 includes:
- Frontend development using Next.js for both web and mobile applications.
- Utilization of React for building reusable UI components.
- Integration with the backend API endpoints developed in Phase 2 for data retrieval and manipulation.
- Implementation of authentication and authorization mechanisms to ensure secure access to features based on user roles.
- Directory structure:
  - `frontend/`
    - `web/`
      - `components/`
      - `pages/`
      - `styles/`
    - `mobile/`
      - `components/`
      - `screens/`
      - `styles/`
  - `public/`
  - `package.json`
- Endpoints for integration with the backend:
  - `/api/auth`
  - `/api/courses`
  - `/api/attendance`
  - `/api/notifications`

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
- **Coder**: Develop the frontend components, pages, and screens for both web and mobile applications. Implement authentication, course management, attendance tracking, and notification features. Ensure responsive design and multi-language support.
- **Tester**: Develop and execute test cases for the frontend, focusing on UI/UX, functionality, and integration with the backend. Perform unit tests, integration tests, and UI tests.
- **Reviewer**: Conduct code reviews to ensure the frontend code is maintainable, efficient, and adheres to the project's coding standards. Verify that the implementation meets the requirements and is properly integrated with the backend.
- **DevOps**: Set up the environment for frontend development, including the necessary dependencies and tools. Ensure the frontend is properly integrated with the backend and can be deployed to the production environment.

#### 4. Phase Definition of Done (DoD)
Phase 3 is considered complete when:
- The web and mobile frontend applications are fully developed and tested.
- All required features, including user authentication, course management, attendance tracking, and notification systems, are implemented and functioning as expected.
- The frontend is properly integrated with the backend API endpoints.
- Code reviews have been conducted, and the codebase is deemed maintainable and efficient.
- The application is deployable to the production environment.
- Documentation for the frontend development, including component libraries and API integrations, is updated and available.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Could not parse response content as the length limit was reached - CompletionUsage(completion_tokens=4096, prompt_tokens=2287, total_tokens=6383, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=None, audio_tokens=0, reasoning_tokens=4823, rejected_prediction_tokens=None, image_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cache_write_tokens=0, cached_tokens=0, video_tokens=0), cost=0, is_byok=False, cost_details={'upstream_inference_cost': 0, 'upstream_inference_prompt_cost': 0, 'upstream_inference_completions_cost': 0})
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 251. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 471. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 418. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 471. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 251. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 251. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 376. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 243. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 209. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 77. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 251. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 221. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 1345. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 257. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 1395. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 188. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 188. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 115. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 386. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 37. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 37. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 37. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 418. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 37. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 37. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 376. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 25. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 25. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 25. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 12. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 12. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
```json
{
  "phase_id": 1,
  "phase_name": "Phase 1",
  "project_name": "membership-hub",
  "global_context_file": "{global_context_file}",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": "{project_phase_context_file}",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "task-1",
          "agent": "Manager",
          "desc": "Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.",
          "components": [
            "project_plan.md",
            "resource_allocation.md"
          ]
        },
        {
          "id": "task-2",
          "agent": "Coder",
          "desc": "Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.",
          "components": [
            "requirements.md",
            "project_plan.md",
            "directory_structure.md"
          ]
        },
        {
          "id": "task-3",
          "agent": "Tester",
          "desc": "Review the project requirements and provide input on the testing strategy and approach.",
          "components": [
            "requirements.md",
            "testing_strategy.md"
          ]
        },
        {
          "id": "task-4",
          "agent": "Reviewer",
          "desc": "Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.",
          "components": [
            "project_plan.md",
            "directory_structure.md"
          ]
        },
        {
          "id": "task-5",
          "agent": "DevOps",
          "desc": "Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.",
          "components": [
            "directory_structure.md",
            "tool_setup.md"
          ]
        }
      ]
    }
  ]
}
```
```

# Phase 2 STEPS - Prompt:

Analyze the attached Phase 2 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 2 CONTEXT MARKDOWN ---
## PHASE 2 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend of the membership-hub project using Java 17, Quarkus, Kafka, and Postgres. This phase will focus on implementing the core features, including user authentication, course management, attendance tracking, and notification systems. The scope of this phase includes designing and implementing the database schema, creating RESTful APIs for backend services, and integrating Kafka for event-driven architecture.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 2 includes:
- **Database Schema Design**: Designing the Postgres database schema to support user authentication, course management, attendance tracking, and notification systems.
- **Backend API Development**: Creating RESTful APIs using Java 17 and Quarkus for user authentication, course management, attendance tracking, and notification systems.
- **Kafka Integration**: Integrating Kafka for event-driven architecture to handle notifications and attendance tracking.
- **Directory Structure**:
  - `src/main/java`: Java source files for the backend application.
  - `src/main/resources`: Configuration files and database schema definitions.
  - `src/test/java`: Unit tests and integration tests for the backend application.
- **Endpoints**:
  - `/api/auth`: User authentication endpoints.
  - `/api/courses`: Course management endpoints.
  - `/api/attendance`: Attendance tracking endpoints.
  - `/api/notifications`: Notification system endpoints.

#### 3. Dedicated Sub-Agent Functional Directives
The following sub-agents will be involved in Phase 2:
- **Coder**: Responsible for designing and implementing the database schema, creating RESTful APIs, and integrating Kafka.
- **Tester**: Responsible for creating unit tests and integration tests for the backend application.
- **Reviewer**: Responsible for reviewing the code and ensuring it meets the project's coding standards and best practices.
- **DevOps**: Responsible for setting up the development environment, configuring Kafka, and ensuring the backend application is deployable.

#### 4. Phase Definition of Done (DoD)
Phase 2 is considered complete when:
- The database schema is designed and implemented.
- RESTful APIs for user authentication, course management, attendance tracking, and notification systems are created and tested.
- Kafka is integrated for event-driven architecture.
- Unit tests and integration tests are written and passed.
- Code reviews are completed, and the code meets the project's coding standards and best practices.
- The backend application is deployable and configured for further development.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
```json
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "#/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "#/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object",
  "phase_id": 2,
  "phase_name": "Phase 2",
  "project_name": "membership-hub",
  "global_context_file": "{global_context_file}",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": "{project_phase_context_file}",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "task-1",
          "agent": "Coder",
          "desc": "Design Postgres database schema for user authentication, course management, attendance tracking, and notifications.",
          "components": [
            "src/main/resources/db/schema.sql"
          ]
        },
        {
          "id": "task-2",
          "agent": "Coder",
          "desc": "Create SQL migration scripts to implement the designed schema.",
          "components": [
            "src/main/resources/db/migration/V1__init_schema.sql"
          ]
        },
        {
          "id": "task-3",
          "agent": "Coder",
          "desc": "Implement /api/auth endpoints using Quarkus.",
          "components": [
            "src/main/java/com/membershiphub/api/AuthResource.java"
          ]
        },
        {
          "id": "task-4",
          "agent": "Tester",
          "desc": "Write unit tests for AuthResource.",
          "components": [
            "src/test/java/com/membershiphub/api/AuthResourceTest.java"
          ]
        },
        {
          "id": "task-5",
          "agent": "Reviewer",
          "desc": "Review AuthResource implementation for coding standards.",
          "components": []
        },
        {
          "id": "task-6",
          "agent": "Coder",
          "desc": "Implement /api/courses endpoints.",
          "components": [
            "src/main/java/com/membershiphub/api/CourseResource.java"
          ]
        },
        {
          "id": "task-7",
          "agent": "Tester",
          "desc": "Write unit tests for CourseResource.",
          "components": [
            "src/test/java/com/membershiphub/api/CourseResourceTest.java"
          ]
        },
        {
          "id": "task-8",
          "agent": "Reviewer",
          "desc": "Review CourseResource implementation.",
          "components": []
        },
        {
          "id": "task-9",
          "agent": "Coder",
          "desc": "Implement /api/attendance endpoints.",
          "components": [
            "src/main/java/com/membershiphub/api/AttendanceResource.java"
          ]
        },
        {
          "id": "task-10",
          "agent": "Tester",
          "desc": "Write unit tests for AttendanceResource.",
          "
```

# Phase 3 STEPS - Prompt:

Analyze the attached Phase 3 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 3 CONTEXT MARKDOWN ---
## PHASE 3 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 3 is to develop the frontend of the membership-hub platform, ensuring a seamless user experience across both web and mobile applications. This phase will focus on creating responsive and user-friendly interfaces using Next.js, aligning with the established requirements and tech stack. The key deliverables include:
- Development of the web frontend for managing learning centers, including features for user authentication, course management, attendance tracking, and notification systems.
- Development of the mobile frontend for learners, incorporating features such as responsive design, user profiles, course enrollment, and push notifications.
- Implementation of multi-language support for both web and mobile applications.
- Integration of the frontend with the backend services developed in Phase 2, ensuring smooth data exchange and functionality.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 3 includes:
- Frontend development using Next.js for both web and mobile applications.
- Utilization of React for building reusable UI components.
- Integration with the backend API endpoints developed in Phase 2 for data retrieval and manipulation.
- Implementation of authentication and authorization mechanisms to ensure secure access to features based on user roles.
- Directory structure:
  - `frontend/`
    - `web/`
      - `components/`
      - `pages/`
      - `styles/`
    - `mobile/`
      - `components/`
      - `screens/`
      - `styles/`
  - `public/`
  - `package.json`
- Endpoints for integration with the backend:
  - `/api/auth`
  - `/api/courses`
  - `/api/attendance`
  - `/api/notifications`

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
- **Coder**: Develop the frontend components, pages, and screens for both web and mobile applications. Implement authentication, course management, attendance tracking, and notification features. Ensure responsive design and multi-language support.
- **Tester**: Develop and execute test cases for the frontend, focusing on UI/UX, functionality, and integration with the backend. Perform unit tests, integration tests, and UI tests.
- **Reviewer**: Conduct code reviews to ensure the frontend code is maintainable, efficient, and adheres to the project's coding standards. Verify that the implementation meets the requirements and is properly integrated with the backend.
- **DevOps**: Set up the environment for frontend development, including the necessary dependencies and tools. Ensure the frontend is properly integrated with the backend and can be deployed to the production environment.

#### 4. Phase Definition of Done (DoD)
Phase 3 is considered complete when:
- The web and mobile frontend applications are fully developed and tested.
- All required features, including user authentication, course management, attendance tracking, and notification systems, are implemented and functioning as expected.
- The frontend is properly integrated with the backend API endpoints.
- Code reviews have been conducted, and the codebase is deemed maintainable and efficient.
- The application is deployable to the production environment.
- Documentation for the frontend development, including component libraries and API integrations, is updated and available.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Could not parse response content as the length limit was reached - CompletionUsage(completion_tokens=4096, prompt_tokens=2407, total_tokens=6503, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=None, audio_tokens=0, reasoning_tokens=2136, rejected_prediction_tokens=None, image_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cache_write_tokens=0, cached_tokens=0, video_tokens=0), cost=0, is_byok=False, cost_details={'upstream_inference_cost': 0.0003216215, 'upstream_inference_prompt_cost': 3.49015e-05, 'upstream_inference_completions_cost': 0.00028672})
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 2512. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 1884. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 2512. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 2898. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 2691. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 2512. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 1256. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 1256. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 2512. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 1507. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 2691. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 2093. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 502. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 2691. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 2093. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 628. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 769. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 837. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 396. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 2216. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 628. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 1507. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 628. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 753. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 1046. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 628. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 628. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 753. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 628. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 502. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 502. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 628. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 628. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 628. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 251. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 37. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 37. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 37. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 37. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 37. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 25. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 25. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 942. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 942. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 942. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 942. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 301. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 301. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 188. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 188. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 188. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 188. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 235. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 235. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 83. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 83. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 83. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 83. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 62. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 62. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 62. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 62. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 37. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 37. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 37. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 37. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 37. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 37. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 37. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 37. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 37. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 37. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 37. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 37. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 12. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 12. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 12. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 12. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 12. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 12. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Based on the provided Phase 1 Context Markdown content, I will extract and translate the daily steps, checklists, and agent tasks into a precise, executable JSON schema.

Since the Markdown content does not explicitly mention specific days, I will assume that the tasks and activities described are to be performed on a single day, which will be represented as "day": 1 in the JSON output.

Here is the translated JSON schema:

```json
{
  "phase_id": 1,
  "phase_name": "Phase 1",
  "project_name": "membership-hub",
  "global_context_file": "{global_context_file}",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": "{project_phase_context_file}",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "task-1",
          "agent": "Manager",
          "desc": "Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.",
          "components": []
        },
        {
          "id": "task-2",
          "agent": "Coder",
          "desc": "Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.",
          "components": []
        },
        {
          "id": "task-3",
          "agent": "Tester",
          "desc": "Review the project requirements and provide input on the testing strategy and approach.",
          "components": []
        },
        {
          "id": "task-4",
          "agent": "Reviewer",
          "desc": "Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.",
          "components": []
        },
        {
          "id": "task-5",
          "agent": "DevOps",
          "desc": "Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.",
          "components": []
        }
      ]
    }
  ]
}
```

Note that I have followed the required JSON schema layout design structure and populated the fields as per the instructions. Since there are no explicit day mentions in the Markdown content, I have assumed a single day and represented it as "day": 1 in the JSON output. The tasks and activities described in the Markdown content are translated into sub-tasks and assigned to the respective agents. The components array is empty for each task, as there are no specific files or scripts mentioned in the Markdown content.
```

# Phase 2 STEPS - Prompt:

Analyze the attached Phase 2 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 2 CONTEXT MARKDOWN ---
## PHASE 2 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend of the membership-hub project using Java 17, Quarkus, Kafka, and Postgres. This phase will focus on implementing the core features, including user authentication, course management, attendance tracking, and notification systems. The scope of this phase includes designing and implementing the database schema, creating RESTful APIs for backend services, and integrating Kafka for event-driven architecture.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 2 includes:
- **Database Schema Design**: Designing the Postgres database schema to support user authentication, course management, attendance tracking, and notification systems.
- **Backend API Development**: Creating RESTful APIs using Java 17 and Quarkus for user authentication, course management, attendance tracking, and notification systems.
- **Kafka Integration**: Integrating Kafka for event-driven architecture to handle notifications and attendance tracking.
- **Directory Structure**:
  - `src/main/java`: Java source files for the backend application.
  - `src/main/resources`: Configuration files and database schema definitions.
  - `src/test/java`: Unit tests and integration tests for the backend application.
- **Endpoints**:
  - `/api/auth`: User authentication endpoints.
  - `/api/courses`: Course management endpoints.
  - `/api/attendance`: Attendance tracking endpoints.
  - `/api/notifications`: Notification system endpoints.

#### 3. Dedicated Sub-Agent Functional Directives
The following sub-agents will be involved in Phase 2:
- **Coder**: Responsible for designing and implementing the database schema, creating RESTful APIs, and integrating Kafka.
- **Tester**: Responsible for creating unit tests and integration tests for the backend application.
- **Reviewer**: Responsible for reviewing the code and ensuring it meets the project's coding standards and best practices.
- **DevOps**: Responsible for setting up the development environment, configuring Kafka, and ensuring the backend application is deployable.

#### 4. Phase Definition of Done (DoD)
Phase 2 is considered complete when:
- The database schema is designed and implemented.
- RESTful APIs for user authentication, course management, attendance tracking, and notification systems are created and tested.
- Kafka is integrated for event-driven architecture.
- Unit tests and integration tests are written and passed.
- Code reviews are completed, and the code meets the project's coding standards and best practices.
- The backend application is deployable and configured for further development.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Based on the provided Phase 2 Context Markdown content, I will extract and translate the daily steps, checklists, and agent tasks into a precise, executable JSON schema.

Since the Markdown content does not explicitly mention daily steps or tasks, I will parse the paragraph descriptions into technical sub-tasks for each day. I will assume a 7-day phase duration, as per the CRITICAL TIMELINE BOUNDARY CONSTRAINTS.

Here is the translated JSON schema:

```json
{
  "phase_id": 2,
  "phase_name": "Phase 2",
  "project_name": "membership-hub",
  "global_context_file": "{global_context_file}",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": "{project_phase_context_file}",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "Task 1.1",
          "agent": "Coder",
          "desc": "Design database schema for user authentication",
          "components": [
            "src/main/resources/database_schema.sql"
          ]
        },
        {
          "id": "Task 1.2",
          "agent": "DevOps",
          "desc": "Set up development environment",
          "components": [
            "src/main/java",
            "src/main/resources",
            "src/test/java"
          ]
        }
      ]
    },
    {
      "day": 2,
      "context_file": "{project_phase_context_file}",
      "context_section": "DAY 2",
      "sub_tasks": [
        {
          "id": "Task 2.1",
          "agent": "Coder",
          "desc": "Implement RESTful APIs for user authentication",
          "components": [
            "src/main/java/com/membership/hub/auth/AuthController.java"
          ]
        },
        {
          "id": "Task 2.2",
          "agent": "Tester",
          "desc": "Create unit tests for user authentication APIs",
          "components": [
            "src/test/java/com/membership/hub/auth/AuthControllerTest.java"
          ]
        }
      ]
    },
    {
      "day": 3,
      "context_file": "{project_phase_context_file}",
      "context_section": "DAY 3",
      "sub_tasks": [
        {
          "id": "Task 3.1",
          "agent": "Coder",
          "desc": "Design database schema for course management",
          "components": [
            "src/main/resources/database_schema.sql"
          ]
        },
        {
          "id": "Task 3.2",
          "agent": "DevOps",
          "desc": "Configure Kafka for event-driven architecture",
          "components": [
            "src/main/java/com/membership/hub/kafka/KafkaConfig.java"
          ]
        }
      ]
    },
    {
      "day": 4,
      "context_file": "{project_phase_context_file}",
      "context_section": "DAY 4",
      "sub_tasks": [
        {
          "id": "Task 4.1",
          "agent": "Coder",
          "desc": "Implement RESTful APIs for course management",
          "components": [
            "src/main/java/com/membership/hub/courses/CourseController.java"
          ]
        },
        {
          "id": "Task 4.2",
          "agent": "Tester",
          "desc": "Create unit tests for course management APIs",
          "components": [
            "src/test/java/com/membership/hub/courses/CourseControllerTest.java"
          ]
        }
      ]
    },
    {
      "day": 5,
      "context_file": "{project_phase_context_file}",
      "context_section": "DAY 5",
      "sub_tasks": [
        {
          "id": "Task 5.1",
          "agent": "Coder",
          "desc": "Implement attendance tracking feature",
          "components": [
            "src/main/java/com/membership/hub/attendance/AttendanceController.java"
          ]
        },
        {
          "id": "Task 5.2",
          "agent": "Reviewer",
          "desc": "Review code for attendance tracking feature",
          "components": [
            "src/main/java/com/membership/hub/attendance/AttendanceController.java"
          ]
        }
      ]
    },
    {
      "day": 6,
      "context_file": "{project_phase_context_file}",
      "context_section": "DAY 6",
      "sub_tasks": [
        {
          "id": "Task 6.1",
          "agent": "Coder",
          "desc": "Implement notification system feature",
          "components": [
            "src/main/java/com/membership/hub/notifications/NotificationController.java"
          ]
        },
        {
          "id": "Task 6.2",
          "agent": "Tester",
          "desc": "Create unit tests for notification system APIs",
          "components": [
            "src/test/java/com/membership/hub/notifications/NotificationControllerTest.java"
          ]
        }
      ]
    },
    {
      "day": 7,
      "context_file": "{project_phase_context_file}",
      "context_section": "DAY 7",
      "sub_tasks": [
        {
          "id": "Task 7.1",
          "agent": "DevOps",
          "desc": "Deploy backend application",
          "components": [
            "src/main/java",
            "src/main/resources",
            "src/test/java"
          ]
        },
        {
          "id": "Task 7.2",
          "agent": "Reviewer",
          "desc": "Review entire codebase for Phase 2",
          "components": [
            "src/main/java",
            "src/main/resources",
            "src/test/java"
          ]
        }
      ]
    }
  ]
}
```

Note that I have assumed a 7-day phase duration and created tasks for each day based on the Phase 2 Context Markdown content. The tasks are assigned to the respective agents (Coder, Tester, Reviewer, DevOps) and include the relevant components (files, paths, and endpoints). The context file and context section are set accordingly for each day.
```

# Phase 3 STEPS - Prompt:

Analyze the attached Phase 3 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 3 CONTEXT MARKDOWN ---
## PHASE 3 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 3 is to develop the frontend of the membership-hub platform, ensuring a seamless user experience across both web and mobile applications. This phase will focus on creating responsive and user-friendly interfaces using Next.js, aligning with the established requirements and tech stack. The key deliverables include:
- Development of the web frontend for managing learning centers, including features for user authentication, course management, attendance tracking, and notification systems.
- Development of the mobile frontend for learners, incorporating features such as responsive design, user profiles, course enrollment, and push notifications.
- Implementation of multi-language support for both web and mobile applications.
- Integration of the frontend with the backend services developed in Phase 2, ensuring smooth data exchange and functionality.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 3 includes:
- Frontend development using Next.js for both web and mobile applications.
- Utilization of React for building reusable UI components.
- Integration with the backend API endpoints developed in Phase 2 for data retrieval and manipulation.
- Implementation of authentication and authorization mechanisms to ensure secure access to features based on user roles.
- Directory structure:
  - `frontend/`
    - `web/`
      - `components/`
      - `pages/`
      - `styles/`
    - `mobile/`
      - `components/`
      - `screens/`
      - `styles/`
  - `public/`
  - `package.json`
- Endpoints for integration with the backend:
  - `/api/auth`
  - `/api/courses`
  - `/api/attendance`
  - `/api/notifications`

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
- **Coder**: Develop the frontend components, pages, and screens for both web and mobile applications. Implement authentication, course management, attendance tracking, and notification features. Ensure responsive design and multi-language support.
- **Tester**: Develop and execute test cases for the frontend, focusing on UI/UX, functionality, and integration with the backend. Perform unit tests, integration tests, and UI tests.
- **Reviewer**: Conduct code reviews to ensure the frontend code is maintainable, efficient, and adheres to the project's coding standards. Verify that the implementation meets the requirements and is properly integrated with the backend.
- **DevOps**: Set up the environment for frontend development, including the necessary dependencies and tools. Ensure the frontend is properly integrated with the backend and can be deployed to the production environment.

#### 4. Phase Definition of Done (DoD)
Phase 3 is considered complete when:
- The web and mobile frontend applications are fully developed and tested.
- All required features, including user authentication, course management, attendance tracking, and notification systems, are implemented and functioning as expected.
- The frontend is properly integrated with the backend API endpoints.
- Code reviews have been conducted, and the codebase is deemed maintainable and efficient.
- The application is deployable to the production environment.
- Documentation for the frontend development, including component libraries and API integrations, is updated and available.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 429 - {'error': {'message': 'Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx7x6rbpftmr50sr2yyb78qm` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99490, Requested 6460. Please try again in 1h25m40.8s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 403 - {'error': {'message': 'The model `meta-llama/llama-4-scout-17b-16e-instruct` is blocked at the project level. Please have a project admin enable this model in the project settings at https://console.groq.com/settings/project/limits', 'type': 'permissions_error'}}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 429 - {'error': {'message': 'Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx7x6rbpftmr50sr2yyb78qm` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99485, Requested 5444. Please try again in 1h10m58.656s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'compound', 'code': 'rate_limit_exceeded'}}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 413 - {'error': {'message': 'Request too large for model `llama-3.1-8b-instant` in organization `org_01kx7x6rbpftmr50sr2yyb78qm` service tier `on_demand` on tokens per minute (TPM): Limit 6000, Requested 6287, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
```

# Phase 1 STEPS - Prompt:

Analyze the attached Phase 1 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 1 CONTEXT MARKDOWN ---
## PHASE 1 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather and document all requirements, and establish a clear understanding of the project's goals and timelines. This phase will focus on planning and requirements gathering, ensuring that all stakeholders are aligned and that the project is set up for success.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
During Phase 1, the technical scope will be limited to the following:
- Review of the Global Context and Raw Requirements documents to ensure understanding of the project's objectives and requirements.
- Creation of a high-level project plan, including timelines, milestones, and resource allocation.
- Establishment of the project's directory structure, including the creation of necessary folders and files for documentation, code, and other project-related assets.
- Definition of the project's technical stack, including the selection of tools, frameworks, and libraries to be used.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project planning process, ensure that the project scope and objectives are clearly defined, and allocate resources as needed.
- **Coder**: Review the project requirements and provide input on the technical feasibility of the project. Assist in the creation of the high-level project plan and directory structure.
- **Tester**: Review the project requirements and provide input on the testing strategy and approach.
- **Reviewer**: Review the project plan and directory structure to ensure that they align with the project's objectives and requirements.
- **DevOps**: Assist in the establishment of the project's directory structure and ensure that the necessary tools and frameworks are in place to support the project.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- The project scope and objectives are clearly defined and documented.
- The high-level project plan, including timelines, milestones, and resource allocation, is complete and approved by all stakeholders.
- The project's directory structure is established, and all necessary folders and files are created.
- The project's technical stack is defined, and all necessary tools, frameworks, and libraries are selected.
- All sub-agents have reviewed and approved the project plan and directory structure.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
```json
{
  "phase_id": 1,
  "phase_name": "Phase 1",
  "project_name": "membership-hub",
  "global_context_file": "{global_context_file}",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": "{project_phase_context_file}",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "T1",
          "agent": "Manager",
          "desc": "Coordinate Phase 1 kickoff, confirm scope and objectives with stakeholders.",
          "components": []
        },
        {
          "id": "T2",
          "agent": "Coder",
          "desc": "Review Global Context and Raw Requirements documents for technical feasibility.",
          "components": [
            "docs/global_context.md",
            "docs/raw_requirements.md"
          ]
        },
        {
          "id": "T3",
          "agent": "Tester",
          "desc": "Review requirements and draft a testing‑strategy outline.",
          "components": [
            "docs/testing_strategy.md"
          ]
        },
        {
          "id": "T4",
          "agent": "Coder",
          "desc": "Assist in drafting the high‑level project plan (timeline, milestones, resource allocation).",
          "components": [
            "plans/high_level_project_plan.md"
          ]
        },
        {
          "id": "T5",
          "agent": "DevOps",
          "desc": "Create the project directory structure with folders for documentation, source code, tests, and assets.",
          "components": [
            "docs/",
            "src/",
            "tests/",
            "assets/"
          ]
        },
        {
          "id": "T6",
          "agent": "Coder",
          "desc": "Create placeholder files for documentation and code base within the new directory structure.",
          "components": [
            "docs/README.md",
            "src/main.py"
          ]
        },
        {
          "id": "T7",
          "agent": "Reviewer",
          "desc": "Review the high‑level project plan for alignment with objectives and requirements.",
          "components": [
            "plans/high_level_project_plan.md"
          ]
        },
        {
          "id": "T8",
          "agent": "Reviewer",
          "desc": "Review the directory structure and placeholder files for completeness and correctness.",
          "components": []
        },
        {
          "id": "T9",
          "agent": "DevOps",
          "desc": "Select and document the technical stack (tools, frameworks, libraries) to be used in the project.",
          "components": [
            "docs/technical_stack.md"
          ]
        },
        {
          "id": "T10",
          "agent": "Manager",
          "desc": "Obtain stakeholder approvals for the project plan, directory structure, and technical stack.",
          "components": []
        }
      ]
    }
  ]
}
```
```

# Phase 2 STEPS - Prompt:

Analyze the attached Phase 2 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 2 CONTEXT MARKDOWN ---
## PHASE 2 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend of the membership-hub project using Java 17, Quarkus, Kafka, and Postgres. This phase will focus on implementing the core features, including user authentication, course management, attendance tracking, and notification systems. The scope of this phase includes designing and implementing the database schema, creating RESTful APIs for backend services, and integrating Kafka for event-driven architecture.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 2 includes:
- **Database Schema Design**: Designing the Postgres database schema to support user authentication, course management, attendance tracking, and notification systems.
- **Backend API Development**: Creating RESTful APIs using Java 17 and Quarkus for user authentication, course management, attendance tracking, and notification systems.
- **Kafka Integration**: Integrating Kafka for event-driven architecture to handle notifications and attendance tracking.
- **Directory Structure**:
  - `src/main/java`: Java source files for the backend application.
  - `src/main/resources`: Configuration files and database schema definitions.
  - `src/test/java`: Unit tests and integration tests for the backend application.
- **Endpoints**:
  - `/api/auth`: User authentication endpoints.
  - `/api/courses`: Course management endpoints.
  - `/api/attendance`: Attendance tracking endpoints.
  - `/api/notifications`: Notification system endpoints.

#### 3. Dedicated Sub-Agent Functional Directives
The following sub-agents will be involved in Phase 2:
- **Coder**: Responsible for designing and implementing the database schema, creating RESTful APIs, and integrating Kafka.
- **Tester**: Responsible for creating unit tests and integration tests for the backend application.
- **Reviewer**: Responsible for reviewing the code and ensuring it meets the project's coding standards and best practices.
- **DevOps**: Responsible for setting up the development environment, configuring Kafka, and ensuring the backend application is deployable.

#### 4. Phase Definition of Done (DoD)
Phase 2 is considered complete when:
- The database schema is designed and implemented.
- RESTful APIs for user authentication, course management, attendance tracking, and notification systems are created and tested.
- Kafka is integrated for event-driven architecture.
- Unit tests and integration tests are written and passed.
- Code reviews are completed, and the code meets the project's coding standards and best practices.
- The backend application is deployable and configured for further development.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
{
    "phase_id": 2,
    "phase_name": "Phase 2",
    "project_name": "membership-hub",
    "global_context_file": "{global_context_file}",
    "source_target_dir": "sources/",
    "days": [
        {
            "day": 1,
            "context_file": "{project_phase_context_file}",
            "context_section": "DAY 1",
            "sub_tasks": [
                {
                    "id": "task-1",
                    "agent": "Coder",
                    "desc": "Design the PostgreSQL database schema to support authentication, courses, attendance, and notifications.",
                    "components": [
                        "src/main/resources/schema.sql"
                    ]
                },
                {
                    "id": "task-2",
                    "agent": "Coder",
                    "desc": "Implement RESTful endpoint for user authentication (/api/auth).",
                    "components": [
                        "src/main/java/com/membershiphub/auth/AuthResource.java"
                    ]
                },
                {
                    "id": "task-3",
                    "agent": "Coder",
                    "desc": "Implement RESTful endpoint for course management (/api/courses).",
                    "components": [
                        "src/main/java/com/membershiphub/course/CourseResource.java"
                    ]
                },
                {
                    "id": "task-4",
                    "agent": "Coder",
                    "desc": "Implement RESTful endpoint for attendance tracking (/api/attendance).",
                    "components": [
                        "src/main/java/com/membershiphub/attendance/AttendanceResource.java"
                    ]
                },
                {
                    "id": "task-5",
                    "agent": "Coder",
                    "desc": "Implement RESTful endpoint for notification system (/api/notifications).",
                    "components": [
                        "src/main/java/com/membershiphub/notification/NotificationResource.java"
                    ]
                },
                {
                    "id": "task-6",
                    "agent": "Coder",
                    "desc": "Integrate Kafka producers and consumers for event‑driven notifications and attendance updates.",
                    "components": [
                        "src/main/java/com/membershiphub/kafka/KafkaProducer.java",
                        "src/main/java/com/membershiphub/kafka/KafkaConsumer.java"
                    ]
                },
                {
                    "id": "task-7",
                    "agent": "Tester",
                    "desc": "Create unit tests for the authentication API.",
                    "components": [
                        "src/test/java/com/membershiphub/auth/AuthResourceTest.java"
                    ]
                },
                {
                    "id": "task-8",
                    "agent": "Tester",
                    "desc": "Create unit tests for the course management API.",
                    "components": [
                        "src/test/java/com/membershiphub/course/CourseResourceTest.java"
                    ]
                },
                {
                    "id": "task-9",
                    "agent": "Tester",
                    "desc": "Create unit tests for the attendance tracking API.",
                    "components": [
                        "src/test/java/com/membershiphub/attendance/AttendanceResourceTest.java"
                    ]
                },
                {
                    "id": "task-10",
                    "agent": "Tester",
                    "desc": "Create unit tests for the notification system API.",
                    "components": [
                        "src/test/java/com/membershiphub/notification/NotificationResourceTest.java"
                    ]
                },
                {
                    "id": "task-11",
                    "agent": "Tester",
                    "desc": "Create integration tests covering end‑to‑end API flows and Kafka event handling.",
                    "components": [
                        "src/test/java/com/membershiphub/integration/IntegrationTest.java"
                    ]
                },
                {
                    "id": "task-12",
                    "agent": "Reviewer",
                    "desc": "Perform code review for all newly added source files and ensure compliance with coding standards.",
                    "components": []
                },
                {
                    "id": "task-13",
                    "agent": "DevOps",
                    "desc": "Set up development environment, configure Kafka broker, and add required properties.",
                    "components": [
                        "docker-compose.yml",
                        "src/main/resources/application.properties"
                    ]
                },
                {
                    "id": "task-14",
                    "agent": "DevOps",
                    "desc": "Package and deploy the backend application to the staging environment.",
                    "components": []
                }
            ]
        }
    ]
}
```

# Phase 3 STEPS - Prompt:

Analyze the attached Phase 3 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 3 CONTEXT MARKDOWN ---
## PHASE 3 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 3 is to develop the frontend of the membership-hub platform, ensuring a seamless user experience across both web and mobile applications. This phase will focus on creating responsive and user-friendly interfaces using Next.js, aligning with the established requirements and tech stack. The key deliverables include:
- Development of the web frontend for managing learning centers, including features for user authentication, course management, attendance tracking, and notification systems.
- Development of the mobile frontend for learners, incorporating features such as responsive design, user profiles, course enrollment, and push notifications.
- Implementation of multi-language support for both web and mobile applications.
- Integration of the frontend with the backend services developed in Phase 2, ensuring smooth data exchange and functionality.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 3 includes:
- Frontend development using Next.js for both web and mobile applications.
- Utilization of React for building reusable UI components.
- Integration with the backend API endpoints developed in Phase 2 for data retrieval and manipulation.
- Implementation of authentication and authorization mechanisms to ensure secure access to features based on user roles.
- Directory structure:
  - `frontend/`
    - `web/`
      - `components/`
      - `pages/`
      - `styles/`
    - `mobile/`
      - `components/`
      - `screens/`
      - `styles/`
  - `public/`
  - `package.json`
- Endpoints for integration with the backend:
  - `/api/auth`
  - `/api/courses`
  - `/api/attendance`
  - `/api/notifications`

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
- **Coder**: Develop the frontend components, pages, and screens for both web and mobile applications. Implement authentication, course management, attendance tracking, and notification features. Ensure responsive design and multi-language support.
- **Tester**: Develop and execute test cases for the frontend, focusing on UI/UX, functionality, and integration with the backend. Perform unit tests, integration tests, and UI tests.
- **Reviewer**: Conduct code reviews to ensure the frontend code is maintainable, efficient, and adheres to the project's coding standards. Verify that the implementation meets the requirements and is properly integrated with the backend.
- **DevOps**: Set up the environment for frontend development, including the necessary dependencies and tools. Ensure the frontend is properly integrated with the backend and can be deployed to the production environment.

#### 4. Phase Definition of Done (DoD)
Phase 3 is considered complete when:
- The web and mobile frontend applications are fully developed and tested.
- All required features, including user authentication, course management, attendance tracking, and notification systems, are implemented and functioning as expected.
- The frontend is properly integrated with the backend API endpoints.
- Code reviews have been conducted, and the codebase is deemed maintainable and efficient.
- The application is deployable to the production environment.
- Documentation for the frontend development, including component libraries and API integrations, is updated and available.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
{
    "phase_id": 3,
    "phase_name": "Phase 3 - Frontend Development",
    "project_name": "membership-hub",
    "global_context_file": "{global_context_file}",
    "source_target_dir": "sources/",
    "days": [
        {
            "day": 1,
            "context_file": "{project_phase_context_file}",
            "context_section": "DAY 1",
            "sub_tasks": [
                {
                    "id": "T1",
                    "agent": "Coder",
                    "desc": "Initialize Next.js project structure for web and mobile frontends, creating base directories and configuration files.",
                    "components": [
                        "frontend/web/pages/_app.js",
                        "frontend/web/pages/index.js",
                        "frontend/web/styles/globals.css",
                        "frontend/mobile/screens/HomeScreen.jsx",
                        "frontend/mobile/styles/AppStyle.js",
                        "frontend/package.json"
                    ]
                },
                {
                    "id": "T2",
                    "agent": "Coder",
                    "desc": "Develop authentication UI components and integrate them with the /api/auth backend endpoint for both web and mobile.",
                    "components": [
                        "frontend/web/components/AuthForm.jsx",
                        "frontend/web/pages/login.jsx",
                        "frontend/mobile/screens/AuthScreen.jsx",
                        "frontend/mobile/components/AuthInput.jsx"
                    ]
                },
                {
                    "id": "T3",
                    "agent": "Coder",
                    "desc": "Create course‑management UI (listing, enrollment, creation) and wire it to the /api/courses endpoint.",
                    "components": [
                        "frontend/web/components/CourseList.jsx",
                        "frontend/web/pages/courses.jsx",
                        "frontend/mobile/screens/CourseScreen.jsx",
                        "frontend/mobile/components/CourseCard.jsx"
                    ]
                },
                {
                    "id": "T4",
                    "agent": "Coder",
                    "desc": "Implement attendance‑tracking interface and connect it with the /api/attendance endpoint.",
                    "components": [
                        "frontend/web/components/AttendanceTracker.jsx",
                        "frontend/web/pages/attendance.jsx",
                        "frontend/mobile/screens/AttendanceScreen.jsx",
                        "frontend/mobile/components/AttendanceItem.jsx"
                    ]
                },
                {
                    "id": "T5",
                    "agent": "Coder",
                    "desc": "Build notification UI components and integrate them with the /api/notifications endpoint.",
                    "components": [
                        "frontend/web/components/NotificationPanel.jsx",
                        "frontend/web/pages/notifications.jsx",
                        "frontend/mobile/screens/NotificationScreen.jsx",
                        "frontend/mobile/components/NotificationItem.jsx"
                    ]
                },
                {
                    "id": "T6",
                    "agent": "Coder",
                    "desc": "Add multi‑language (i18n) support configuration for both web and mobile frontends.",
                    "components": [
                        "frontend/web/i18n.js",
                        "frontend/web/locales/en.json",
                        "frontend/web/locales/es.json",
                        "frontend/mobile/i18n.js",
                        "frontend/mobile/locales/en.json",
                        "frontend/mobile/locales/es.json"
                    ]
                },
                {
                    "id": "T7",
                    "agent": "Tester",
                    "desc": "Write and run unit tests for all newly created UI components.",
                    "components": [
                        "frontend/web/__tests__/AuthForm.test.js",
                        "frontend/web/__tests__/CourseList.test.js",
                        "frontend/web/__tests__/AttendanceTracker.test.js",
                        "frontend/web/__tests__/NotificationPanel.test.js",
                        "frontend/mobile/__tests__/AuthScreen.test.js",
                        "frontend/mobile/__tests__/CourseScreen.test.js",
                        "frontend/mobile/__tests__/AttendanceScreen.test.js",
                        "frontend/mobile/__tests__/NotificationScreen.test.js"
                    ]
                },
                {
                    "id": "T8",
                    "agent": "Tester",
                    "desc": "Create integration tests that verify correct communication with backend API endpoints (/api/auth, /api/courses, /api/attendance, /api/notifications).",
                    "components": [
                        "frontend/web/__tests__/apiIntegration.test.js",
                        "frontend/mobile/__tests__/apiIntegration.test.js"
                    ]
                },
                {
                    "id": "T9",
                    "agent": "Tester",
                    "desc": "Execute end‑to‑end UI tests (e.g., Cypress) covering authentication flow, course enrollment, attendance marking, and notification receipt.",
                    "components": [
                        "cypress/integration/authFlow.spec.js",
                        "cypress/integration/courseEnrollment.spec.js",
                        "cypress/integration/attendanceFlow.spec.js",
                        "cypress/integration/notificationFlow.spec.js"
                    ]
                },
                {
                    "id": "T10",
                    "agent": "Reviewer",
                    "desc": "Perform code review of all web frontend code ensuring style compliance, performance, and proper integration.",
                    "components": [
                        "frontend/web/components/",
                        "frontend/web/pages/",
                        "frontend/web/styles/"
                    ]
                },
                {
                    "id": "T11",
                    "agent": "Reviewer",
                    "desc": "Perform code review of all mobile frontend code ensuring style compliance, performance, and proper integration.",
                    "components": [
                        "frontend/mobile/components/",
                        "frontend/mobile/screens/",
                        "frontend/mobile/styles/"
                    ]
                },
                {
                    "id": "T12",
                    "agent": "DevOps",
                    "desc": "Set up development environment: install dependencies, configure .env variables, and ensure build scripts are functional.",
                    "components": [
                        "frontend/package.json",
                        ".env"
                    ]
                },
                {
                    "id": "T13",
                    "agent": "DevOps",
                    "desc": "Create CI/CD pipeline configuration for automated testing and deployment of the frontend to the production environment.",
                    "components": [
                        ".github/workflows/frontend.yml"
                    ]
                },
                {
                    "id": "T14",
                    "agent": "DevOps",
                    "desc": "Deploy the built frontend applications to the production platform (e.g., Vercel) and verify successful launch.",
                    "components": []
                }
            ]
        }
    ]
}
```

# Phase 4 STEPS - Prompt:

Analyze the attached Phase 4 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 4 CONTEXT MARKDOWN ---
## PHASE 4 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 4 is to conduct thorough testing and quality assurance of the membership-hub platform. This phase will focus on identifying and fixing bugs, ensuring the platform's stability, security, and performance. The scope includes:
- Unit testing of individual components
- Integration testing of interconnected components
- UI testing for user experience and interface validation
- Security testing to identify vulnerabilities
- Performance testing to ensure scalability and efficiency

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 4 includes:
- **Testing Framework**: Utilize testing frameworks such as JUnit for backend and Jest for frontend to write and execute tests.
- **Test Directory**: Create a separate directory for tests, e.g., `src/test/java` for backend and `__tests__` for frontend.
- **Test Endpoints**: Identify and test all API endpoints, including authentication, course management, attendance tracking, and notification systems.
- **Test Data**: Create mock data for testing purposes, ensuring it covers various scenarios and edge cases.
- **Security Testing Tools**: Utilize tools like OWASP ZAP for security testing and vulnerability assessment.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
- **Coder**: Assist in writing test cases, fixing bugs identified during testing, and ensuring code quality.
- **Tester**: Develop and execute comprehensive testing plans, including unit tests, integration tests, UI tests, security tests, and performance tests.
- **Reviewer**: Conduct code reviews to ensure tests are properly written, and code fixes are correctly implemented.
- **DevOps**: Focus on ensuring the testing environment is properly set up, and tests can be executed efficiently. Assist in deploying the application to a staging environment for testing.
- **Manager**: Oversee the testing process, ensure timely completion, and allocate resources as needed.

#### 4. Phase Definition of Done (DoD)
Phase 4 is considered complete when:
- All unit tests, integration tests, UI tests, security tests, and performance tests have been executed with satisfactory results.
- All identified bugs have been fixed, and the fixes have been verified through re-testing.
- Code reviews have been conducted, and all feedback has been incorporated.
- The application has been deployed to a staging environment for final testing and validation.
- A comprehensive test report has been generated, detailing all tests conducted, results, and any remaining issues.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
{
    "phase_id": 4,
    "phase_name": "Phase 4",
    "project_name": "membership-hub",
    "global_context_file": "{global_context_file}",
    "source_target_dir": "sources/",
    "days": [
        {
            "day": 1,
            "context_file": "{project_phase_context_file}",
            "context_section": "DAY 1",
            "sub_tasks": [
                {
                    "id": "T1",
                    "agent": "DevOps",
                    "desc": "Provision and configure the testing environment, including creation of test directories (src/test/java, __tests__) and installation of required frameworks (JUnit, Jest).",
                    "components": []
                },
                {
                    "id": "T2",
                    "agent": "Coder",
                    "desc": "Write unit test cases for backend components using JUnit.",
                    "components": []
                },
                {
                    "id": "T3",
                    "agent": "Tester",
                    "desc": "Execute all backend unit tests and record results.",
                    "components": []
                },
                {
                    "id": "T4",
                    "agent": "Coder",
                    "desc": "Fix bugs identified by unit test failures.",
                    "components": []
                },
                {
                    "id": "T5",
                    "agent": "Tester",
                    "desc": "Re‑run unit tests to verify bug fixes.",
                    "components": []
                },
                {
                    "id": "T6",
                    "agent": "Coder",
                    "desc": "Develop integration test suites for interconnected components.",
                    "components": []
                },
                {
                    "id": "T7",
                    "agent": "Tester",
                    "desc": "Run integration tests and capture any failures.",
                    "components": []
                },
                {
                    "id": "T8",
                    "agent": "Coder",
                    "desc": "Resolve integration test failures.",
                    "components": []
                },
                {
                    "id": "T9",
                    "agent": "Tester",
                    "desc": "Validate integration fixes by re‑executing integration tests.",
                    "components": []
                },
                {
                    "id": "T10",
                    "agent": "Coder",
                    "desc": "Create UI test scripts using Jest for frontend components.",
                    "components": []
                },
                {
                    "id": "T11",
                    "agent": "Tester",
                    "desc": "Run UI tests and log any UI bugs or regressions.",
                    "components": []
                },
                {
                    "id": "T12",
                    "agent": "Coder",
                    "desc": "Patch UI issues discovered during UI testing.",
                    "components": []
                },
                {
                    "id": "T13",
                    "agent": "Tester",
                    "desc": "Re‑run UI tests to confirm UI bug resolutions.",
                    "components": []
                },
                {
                    "id": "T14",
                    "agent": "Tester",
                    "desc": "Perform security testing with OWASP ZAP against all API endpoints.",
                    "components": []
                },
                {
                    "id": "T15",
                    "agent": "Coder",
                    "desc": "Address security vulnerabilities reported by OWASP ZAP.",
                    "components": []
                },
                {
                    "id": "T16",
                    "agent": "Tester",
                    "desc": "Retest secured endpoints to ensure vulnerabilities are mitigated.",
                    "components": []
                },
                {
                    "id": "T17",
                    "agent": "Tester",
                    "desc": "Execute performance load tests to evaluate scalability and efficiency.",
                    "components": []
                },
                {
                    "id": "T18",
                    "agent": "Coder",
                    "desc": "Optimize code paths identified as performance bottlenecks.",
                    "components": []
                },
                {
                    "id": "T19",
                    "agent": "Tester",
                    "desc": "Re‑run performance tests to verify improvements.",
                    "components": []
                },
                {
                    "id": "T20",
                    "agent": "Reviewer",
                    "desc": "Conduct comprehensive code reviews of test code and bug‑fix commits.",
                    "components": []
                },
                {
                    "id": "T21",
                    "agent": "DevOps",
                    "desc": "Deploy the latest build to the staging environment for final validation.",
                    "components": []
                },
                {
                    "id": "T22",
                    "agent": "Manager",
                    "desc": "Generate a consolidated test report summarizing all test results, bug fixes, and remaining issues.",
                    "components": []
                }
            ]
        }
    ]
}
```

# Phase 5 STEPS - Prompt:

Analyze the attached Phase 5 Context Markdown content.


Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.


## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
#### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

## AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
#### 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
#### 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
#### 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

## CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:


#### 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
#### 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.

#### 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
#### 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
#### 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
#### 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.
#### 7. CHRONOLOGICAL TIMELINE RESET MANDATE (ABSOLUTE):
Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7" or "Day 4 to Day 7"), you MUST reset the timeline timeline sequence internally for this JSON output so that it strictly starts from integer 1.
   - The first operational day processed inside this Phase MUST always be gaged as "day": 1.
   - Sequential days must progress logically as 2, 3, 4, etc.
   - Example Transformation: Map "Day 4" to "day": 1, "Day 5" to "day": 2, "Day 6" to "day": 3, and "Day 7" to "day": 4.
   - Adjust the 'context_section' field accordingly to match this localized reset format (e.g., set to "DAY 1", "DAY 2", etc.).

You MUST conform strictly to your required JSON Schema layout design structure:
{
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        },
        "components": {
          "description": "Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved.",
          "items": {
            "type": "string"
          },
          "title": "Components",
          "type": "array"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

--- PHASE 5 CONTEXT MARKDOWN ---
## PHASE 5 CONTEXT BLUEPRINT: membership-hub
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 5 is to deploy the membership-hub application on Google Cloud Platform (GCP) while ensuring scalability, security, and high availability. This phase involves setting up the production environment, configuring Docker and Kubernetes, and deploying the application. Additionally, this phase will focus on planning for post-deployment maintenance and updates.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 5 includes:
- Deploying the application on GCP using Docker and Kubernetes
- Configuring load balancing, autoscaling, and monitoring
- Setting up security measures such as encryption, firewalls, and access controls
- Creating a backup and disaster recovery plan
- Defining API endpoints for the production environment
- Updating the documentation to reflect the production deployment

Allowed directories and files include:
- `docker-compose.yml` for defining Docker services
- `kubernetes/deployment.yaml` for defining Kubernetes deployments
- `kubernetes/service.yaml` for defining Kubernetes services
- `gcp/deployment.py` for automating GCP deployment
- `config/prod.env` for production environment configuration

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
- **Coder**: Focus on creating automated deployment scripts for GCP, updating the Docker configuration, and implementing security measures.
- **Tester**: Conduct thorough testing of the application in the production environment, including load testing, security testing, and functionality testing.
- **Reviewer**: Review the deployment scripts, Docker configuration, and security measures to ensure they meet the project's standards and best practices.
- **DevOps**: Set up the production environment on GCP, configure Kubernetes, and deploy the application. Additionally, focus on monitoring, logging, and backup strategies.
- **Manager**: Oversee the deployment process, ensure that the application is deployed on time, and coordinate with the team to resolve any issues that arise during deployment.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 5 includes:
- The application is successfully deployed on GCP.
- The application is scalable, secure, and highly available.
- Load balancing, autoscaling, and monitoring are configured.
- Security measures such as encryption, firewalls, and access controls are in place.
- A backup and disaster recovery plan is created and tested.
- API endpoints are defined and documented for the production environment.
- The documentation is updated to reflect the production deployment.
- Thorough testing has been conducted, and any issues have been resolved.
- The team has reviewed and approved the deployment configuration and security measures.
------------------------------------------

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
```json
{
  "phase_id": 5,
  "phase_name": "Phase 5",
  "project_name": "membership-hub",
  "global_context_file": "{global_context_file}",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": "{project_phase_context_file}",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1-1",
          "agent": "DevOps",
          "desc": "Create GCP project, configure IAM, networking, and service accounts",
          "components": []
        },
        {
          "id": "1-2",
          "agent": "DevOps",
          "desc": "Provision Kubernetes cluster on GCP using gcloud commands",
          "components": []
        },
        {
          "id": "1-3",
          "agent": "Coder",
          "desc": "Develop automated deployment script gcp/deployment.py to orchestrate GCP resources",
          "components": [
            "gcp/deployment.py"
          ]
        }
      ]
    },
    {
      "day": 2,
      "context_file": "{project_phase_context_file}",
      "context_section": "DAY 2",
      "sub_tasks": [
        {
          "id": "2-1",
          "agent": "Coder",
          "desc": "Update docker-compose.yml with production image tags and resource limits",
          "components": [
            "docker-compose.yml"
          ]
        },
        {
          "id": "2-2",
          "agent": "Coder",
          "desc": "Add security configurations (encryption settings, environment secrets) to config/prod.env and deployment script",
          "components": [
            "config/prod.env",
            "gcp/deployment.py"
          ]
        },
        {
          "id": "2-3",
          "agent": "DevOps",
          "desc": "Apply GCP firewall rules and IAM policies for secure access",
          "components": []
        }
      ]
    },
    {
      "day": 3,
      "context_file": "{project_phase_context_file}",
      "context_section": "DAY 3",
      "sub_tasks": [
        {
          "id": "3-1",
          "agent": "DevOps",
          "desc": "Deploy Kubernetes manifests (deployment.yaml, service.yaml) to the cluster",
          "components": [
            "kubernetes/deployment.yaml",
            "kubernetes/service.yaml"
          ]
        },
        {
          "id": "3-2",
          "agent": "DevOps",
          "desc": "Configure GCP load balancer and enable Horizontal Pod Autoscaling",
          "components": []
        },
        {
          "id": "3-3",
          "agent": "DevOps",
          "desc": "Set up Stackdriver monitoring, logging, and alerting for the application",
          "components": []
        }
      ]
    },
    {
      "day": 4,
      "context_file": "{project_phase_context_file}",
      "context_section": "DAY 4",
      "sub_tasks": [
        {
          "id": "4-1",
          "agent": "Tester",
          "desc": "Execute functional tests against production endpoints",
          "components": []
        },
        {
          "id": "4-2",
          "agent": "Tester",
          "desc": "Perform load testing to validate autoscaling behavior",
          "components": []
        },
        {
          "id": "4-3",
          "agent": "Tester",
          "desc": "Run security scans and verify firewall and encryption settings",
          "components": []
        },
        {
          "id": "4-4",
          "agent": "Reviewer",
          "desc": "Review deployment scripts, Docker configuration, and Kubernetes manifests for compliance",
          "components": [
            "gcp/deployment.py",
            "docker-compose.yml",
            "kubernetes/deployment.yaml",
            "kubernetes/service.yaml"
          ]
        },
        {
          "id": "4-5",
          "agent": "Coder",
          "desc": "Update project documentation to reflect production deployment steps and endpoints",
          "components": []
        }
      ]
    }
  ]
}
```
```

