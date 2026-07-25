## 1. PROJECT OVERVIEW
- **Mục tiêu sản phẩm & Giá trị cốt lõi**
   * Mục tiêu: Cung cấp cho các doanh nghiệp nhỏ một công cụ tạo showroom thực tế ảo không cần mã, có khả năng tích hợp AI chatbot, cho phép tải lên hình ảnh sản phẩm, tùy chỉnh bố cục 3D và nhúng vào website hoặc chia sẻ liên kết 360 độ trong vài phút.
   * Giá trị cốt lõi: Dễ sử dụng, tốc độ triển khai nhanh, khả năng tùy biến cao, bảo mật dữ liệu, khả năng mở rộng.

- **Đối tượng người dùng mục tiêu**
   * Chủ cửa hàng bán lẻ, công ty nội thất, nhà sản xuất hàng thủ công.
   * Vai trò: Chủ sở hữu (tạo và quản lý showroom), Quản trị viên (quản lý người dùng, thanh toán), Khách hàng (xem showroom).

- **Ma trận phân quyền (RBAC)**
   * Vai trò: **Chủ sở hữu**, **Quản trị viên**, **Người xem**, **Hỗ trợ**.
   * Quyền: Chủ sở hữu: tạo, chỉnh sửa, xóa showroom, quản lý sản phẩm, xem báo cáo. Quản trị viên: quản lý người dùng, hóa đơn, nhật ký hệ thống. Người xem: chỉ xem showroom công khai. Hỗ trợ: xem nhật ký, phản hồi người dùng.

## 2. YÊU CẦU CHỨC NĂNG

### Mô-đun 1: Quản lý tài sản (Tải lên và quản lý hình ảnh sản phẩm)
**Người dùng truyện**: Là chủ cửa hàng, tôi muốn tải lên hình ảnh sản phẩm (tối đa 10 MB mỗi ảnh, định dạng JPEG, PNG, GLB) để thêm vào danh mục sản phẩm của tôi, vì vậy tôi có thể trưng bày sản phẩm trong showroom.
**Tiêu chí chấp nhận**:
   * Given tôi đã đăng nhập với vai trò Chủ sở hữu,
   * When tôi chọn file hình ảnh và nhấn nút “Tải lên”,
   * Then tệp được tải lên thành công, được lưu trữ và hiển thị trong thư viện sản phẩm.
**Dữ liệu đầu vào & Xác thực**:
   * Trường file: bắt buộc, kích thước ≤10 MB, loại được cho phép: image/jpeg, image/png, model/gltf-binary.
   * Trường mô tả: tùy chọn, độ dài ≤500 ký tự.

### Mô-đun 2: Trình tạo bố cục 3D
**Người dùng truyện**: Là chủ cửa hàng, tôi muốn sắp xếp sản phẩm vào không gian 3D bằng cách kéo và thả, điều chỉnh góc nhìn máy ảnh và ánh sáng, vì vậy tôi có thể tạo trải nghiệm xem trực quan hấp dẫn.
**Tiêu chí chấp nhận**:
   * Given tôi đã thêm ít nhất một sản phẩm,
   * When tôi di chuyển sản phẩm vào cảnh 3D, thay đổi góc nhìn và điều chỉnh cường độ ánh sáng,
   * Then cảnh được cập nhật theo thời gian thực và có thể lưu dưới dạng bản thiết kế showroom.
**Xác thực**:
   * Tọa độ sản phẩm: phải nằm trong vùng giới hạn (‑100,‑100,‑100) đến (100,100,100).
   * Cường độ ánh sáng: từ 0.0 đến 1.0.

### Mô-đun 3: Tích hợp chatbot AI hỗ trợ sản phẩm
**Người dùng truyện**: Là khách hàng, tôi muốn hỏi chatbot về tính năng sản phẩm và nhận gợi ý, vì vậy tôi có thể nhận được hỗ trợ tức thì khi xem showroom.
**Tiêu chí chấp nhận**:
   * Given showroom có kích hoạt chatbot,
   * When tôi gửi câu hỏi “Có sản phẩm nào màu đỏ không?”,
   * Then chatbot trả về danh sách sản phẩm phù hợp trong vòng 2 giây.
**Xác thực đầu vào**:
   * Trường văn bản câu hỏi: không được rỗng, độ dài ≤200 ký tự.

### Mô-đun 4: Nhúng và chia sẻ
**Người dùng truyện**: Là chủ cửa hàng, tôi muốn nhúng showroom vào trang web hoặc chia sẻ liên kết 360 độ với khách hàng, vì vậy tôi có thể trưng bày sản phẩm trên nhiều kênh.
**Tiêu chí chấp nhận**:
   * Given tôi đã xuất bản một showroom,
   * When tôi nhấp vào “Tạo liên kết chia sẻ”,
   * Then một URL duy nhất được tạo và có thể được dán vào bất kỳ trang web nào.
**Xác thực**:
   * URL: phải tuân theo RFC 3986.
   * Quyền truy cập: có thể đặt thành “Công khai” hoặc “Riêng tư”.

### Mô-đun 5: Quản lý người dùng và đăng ký
**Người dùng truyện**: Là chủ cửa hàng mới, tôi muốn đăng ký tài khoản bằng email và mật khẩu, xác nhận qua email, sau đó đăng nhập để bắt đầu tạo showroom.
**Tiêu chí chấp nhận**:
   * Given tôi truy cập trang đăng ký,
   * When tôi nhập email, tạo mật khẩu và nhấn “Đăng ký”,
   * Then một email xác nhận được gửi và tài khoản được kích hoạt trong vòng 5 phút.
**Xác thực**:
   * Email: định dạng hợp lệ, duy nhất.
   * Mật khẩu: ít nhất 8 ký tự, bao gồm chữ hoa, chữ thường, số, ký tự đặc biệt.

### Mô-đun 6: Thanh toán và gói đăng ký
**Người dùng truyện**: Là chủ cửa hàng, tôi muốn mua gói đăng ký (Miễn phí, Cơ bản, Cao cấp) để có giới hạn số lượng sản phẩm và tính năng, thanh toán qua thẻ tín dụng.
**Tiêu chí chấp nhận**:
   * Given tôi chọn gói “Cao cấp”,
   * When tôi nhập thông tin thẻ và xác nhận thanh toán,
   * Then gói được kích hoạt và tôi có thể thêm tối đa 200 sản phẩm.
**Xác thực**:
   * Số thẻ: 13‑19 chữ số, tuân theo Luhn algorithm.
   * Hạn sử dụng: phải lớn hơn ngày hiện tại.

### Mô-đun 7: Phân tích và nhật ký kiểm toán
**Người dùng truyện**: Là quản trị viên, tôi muốn xem nhật ký kiểm toán về các thao tác tải lên, chỉnh sửa và đăng nhập người dùng, vì vậy tôi có thể giám sát hệ thống.
**Tiêu chí chấp nhận**:
   * Given tôi có vai trò Quản trị viên,
   * When tôi điều hướng đến tab “Nhật ký”,
   * Then một bảng hiển thị các sự kiện theo thời gian thực với các trường: người dùng, hành động, thời gian, địa chỉ IP.
**Xác thực**:
   * Trường thời gian: ISO 8601.

## 3. LUỒNG NGOẠI LỆ & TRƯỜNG HỢP ĐẶC BIỆT

- **Mất kết nối mạng**: Hệ thống phát hiện mất mạng và hiển thị thông báo “Bạn đang xem chế độ ngoại tuyến”. Khi kết nối được khôi phục, đồng bộ hóa tự động các thay đổi chưa được lưu.
- **Đầu vào không hợp lệ**: Nếu định dạng tệp không supported hoặc kích thước vượt quá, hệ thống hiển thị thông báo lỗi chi tiết và cho phép tải lên lại.
- **Xung đột đồng thời**: Hai chủ sở hữu cố gắng chỉnh sửa cùng một showroom; hệ thống sử dụng khóa lạc quan và hiển thị cảnh báo “Đã có người khác chỉnh sửa”; người dùng cuối cùng thành công, những người khác được nhắc tải lại.
- **Khôi phục hệ thống**: Sau khi khởi động lại, hệ thống khôi phục trạng thái gần nhất từ bản sao lưu (cách đây 30 phút) và thông báo “Hệ thống đã được khôi phục, các thay đổi chưa được đồng bộ hóa có thể bị mất”.
- **Thông báo lỗi**: Tất cả các lỗi hiển thị dưới dạng toast thông báo với mã lỗi và nút “Chi tiết” để hiển thị mô tả lỗi.

## 4. YÊU CẦU PHI CHỨC NĂNG

- **Hiệu suất**:
   * Thời gian tải trang chủ < 2 giây.
   * Thời gian phản hồi API < 500 ms.
   * Giới hạn tải lên hình ảnh đồng thời ≤ 5 MB/s.
   * Hỗ trợ 5.000 người dùng đồng thời.

- **Bảo mật**:
   * Mã hóa dữ liệu ở trạng thái nghỉ bằng AES‑256.
   * Mã hóa dữ liệu truyền tải bằng TLS 1.3.
   * Xác thực bằng JWT; mỗi phiên có thời gian sống 15 phút, có thể gia hạn.
   * Tích hợp OAuth2 với Google, Microsoft để đăng nhập.
   * Tuân thủ các biện pháp kiểm soát OWASP Top 10 (SQL injection, XSS, CSRF, v.v.).
   * Tích hợp MFA tùy chọn cho Chủ sở hữu và Quản trị viên.

- **Khả năng mở rộng & Tính khả dụng**:
   * Kiến trúc vi dịch vụ với Kubernetes auto‑scaling.
   * Cân bằng tải qua NGINX, lưu cache tĩnh qua CDN.
   * SLA 99.9% thời gian hoạt động, giám sát qua Prometheus + Grafana.
   * Các khu vực sẵn sàng: US‑East, EU‑West.

## 5. TỪ ĐIỂN DỮ LIỆU (Bảng thực thể)

### Bảng: Users
| Tên trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
|-----------|-----------|-----------|-------------|
| user_id | UUID | PK, không null | Định danh duy nhất |
| email | VARCHAR(255) | không null, unique | Địa chỉ email đăng nhập |
| password_hash | VARCHAR(512) | không null | Hash mật khẩu (bcrypt) |
| full_name | VARCHAR(100) | tùy chọn | Tên hiển thị |
| role | ENUM('owner','admin','viewer','support') | không null | Vai trò người dùng |
| organization_id | UUID | không null, FK | Tổ chức thuộc về |
| is_email_verified | BOOLEAN | mặc định false | Trạng thái xác minh email |
| created_at | TIMESTAMP | mặc định now | Thời điểm tạo |
| updated_at | TIMESTAMP | mặc định now | Thời điểm cập nhật |

### Bảng: Organizations
| Tên trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
|-----------|-----------|-----------|-------------|
| organization_id | UUID | PK, không null | Định danh duy nhất |
| name | VARCHAR(150) | không null | Tên công ty |
| subscription_tier | ENUM('free','basic','premium') | mặc định 'free' | Gói hiện tại |
| max_products | INT | nullable | Số sản phẩm tối đa được phép |
| created_at | TIMESTAMP | mặc định now | Thời điểm tạo |

### Bảng: Showrooms
| Tên trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
|-----------|-----------|-----------|-------------|
| showroom_id | UUID | PK, không null | Định danh duy nhất |
| organization_id | UUID | không null, FK | Tổ chức sở hữu |
| name | VARCHAR(100) | không null | Tên showroom |
| slug | VARCHAR(100) | unique, không null | URL thân thiện |
| scene_data | JSON | không null | Bố cục 3D và vị trí sản phẩm |
| is_published | BOOLEAN | mặc định false | Trạng thái công khai |
| created_at | TIMESTAMP | mặc định now | Thời điểm tạo |
| updated_at | TIMESTAMP | mặc định now | Thời điểm cập nhật |

### Bảng: Products
| Tên trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
|-----------|-----------|-----------|-------------|
| product_id | UUID | PK, không null | Định danh duy nhất |
| showroom_id | UUID | không null, FK | Showroom chứa sản phẩm |
| name | VARCHAR(150) | không null | Tên sản phẩm |
| description | TEXT | tùy chọn | Mô tả sản phẩm |
| image_url | VARCHAR(500) | không null | Đường dẫn hình ảnh chính |
| glb_url | VARCHAR(500) | tùy chọn | Đường dẫn mô hình 3D |
| position_x | FLOAT | không null | Tọa độ X trong không gian |
| position_y | FLOAT | không null | Tọa độ Y |
| position_z | FLOAT | không null | Tọa độ Z |
| scale | FLOAT | mặc định 1.0 | Tỷ lệ hiển thị |

### Bảng: Chatbots
| Tên trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
|-----------|-----------|-----------|-------------|
| chatbot_id | UUID | PK, không null | Định danh duy nhất |
| showroom_id | UUID | không null, FK | Showroom liên kết |
| knowledge_base | JSON | không null | Dữ liệu sản phẩm để tham chiếu |
| api_endpoint | VARCHAR(200) | không null | URL dịch vụ AI |
| created_at | TIMESTAMP | mặc định now | Thời điểm tạo |

### Bảng: Sessions
| Tên trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
|-----------|-----------|-----------|-------------|
| session_id | UUID | PK, không null | Định danh phiên |
| user_id | UUID | không null, FK | Người dùng |
| token | VARCHAR(500) | unique, không null | JWT token |
| expires_at | TIMESTAMP | không null | Hết hạn |
| ip_address | VARCHAR(45) | tùy chọn | Địa chỉ IP |
| user_agent | TEXT | tùy chọn | Thông tin trình duyệt |

### Bảng: AuditLogs
| Tên trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
|-----------|-----------|-----------|-------------|
| log_id | UUID | PK, không null | Định danh duy nhất |
| user_id | UUID | tùy chọn, FK | Người dùng thực hiện |
| action | VARCHAR(100) | không null | Thao tác (tải lên, chỉnh sửa, v.v.) |
| entity_type | VARCHAR(50) | không null | Loại thực thể (User, Showroom, Product) |
| entity_id | UUID | không null | ID của thực thể |
| timestamp | TIMESTAMP | mặc định now | Thời điểm xảy ra |
| details | JSON | tùy chọn | Thông tin chi tiết |
| ip_address | VARCHAR(45) | tùy chọn | Địa chỉ IP |

... có thể tiếp tục nhưng đủ.
