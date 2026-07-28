# Project Name: membership-hub

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
