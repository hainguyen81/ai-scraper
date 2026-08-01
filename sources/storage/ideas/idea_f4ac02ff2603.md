# AI Design Assistant cho Marketing Không Chuyên

- **Lĩnh vực:** AI Thiết Kế Hình Ảnh cho Marketing
- **Problem Statement:** Nhiều chủ doanh nghiệp nhỏ và người sáng tạo nội dung không có kỹ năng thiết kế nhưng vẫn cần hình ảnh quảng cáo chuyên nghiệp, dẫn đến chi phí thuê designer cao và mất thời gian.
- **Solution & Workflow:** Một ứng dụng web cung cấp giao diện kéo-thả đơn giản, cho phép người dùng nhập mô tả văn bản và công cụ AI sẽ tạo ra hình ảnh trong vài giây, hỗ trợ tải xuống, chỉnh sửa cơ bản và tích hợp thanh toán.
- **Target Audience:** Chủ doanh nghiệp nhỏ, người làm marketing độc lập, người sáng tạo nội dung trên mạng xã hội.
- **Unique Selling Proposition (USP):** Không yêu cầu kỹ năng thiết kế, giá thành thấp, tích hợp API AI nhanh, có sẵn template và hỗ trợ tải ảnh ngay lập tức.

##### **Yêu cầu Thực hiện Nhanh & Tối giản:**

* **[REQ-001]** Controller xử lý yêu cầu tạo hình ảnh từ văn bản người dùng, gọi API AI, lưu kết quả vào ./sources/controllers/image_generation_controller.py.
* **[REQ-002]** Dịch vụ lưu trữ file hình ảnh được tạo, cung cấp URL tải xuống, cleanup file cũ, triển khai tại ./sources/services/image_storage_service.py.
* **[REQ-003]** Giao diện người dùng kéo-thả với preview thời gian thực, nút tạo ảnh, tích hợp thanh toán, mã nguồn tại ./sources/views/image_builder_ui.py.
* **[DAT-001]** Bảng lưu trữ hình ảnh (id, user_id, image_url, created_at, usage_count) định nghĩa trong ./sources/models/image_asset.py.
* **[DAT-002]** Bảng thông tin người dùng (id, email, plan_type, creation_date) định nghĩa trong ./sources/models/user_account.py.
* **[EXC-001]** Xử lý lỗi khi API AI không khả dụng, trả về thông báo lỗi cho người dùng và ghi log tại ./sources/exceptions/ai_service_unavailable_exception.py.
* **[EXC-002]** Giới hạn rate request cho gói miễn phí, trả về lỗi 429 với hướng dẫn nâng cấp tại ./sources/exceptions/rate_limit_exception.py.