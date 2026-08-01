# EcoGrid - Nền tảng quản lý vi lưới năng lượng tái tạo cho tòa nhà thương mại nhỏ

- **Vấn đề:** Các tòa nhà thương mại nhỏ gặp khó khăn trong việc giám sát và tối ưu hóa sản lượng năng lượng tái tạo từ các hệ thống pin mặt trời hoặc gió vì thiếu một giải pháp đơn giản, giá thành thấp. Việc theo dõi thủ công gây lãng phí và khó đảm bảo hiệu suất.
- **Giải pháp & Quy trình:** EcoGrid cung cấp một ứng dụng SaaS cho phép chủ sở hữu nhập dữ liệu cảm biến, xem biểu đồ thời gian thực, nhận cảnh báo khi hiệu suất giảm, và thực hiện điều chỉnh tự động thông qua các thiết bị được kết nối. Quy trình: cảm biến → API → lưu trữ dữ liệu → giao diện người dùng.
- **Đối tượng mục tiêu:** Chủ sở hữu tòa nhà thương mại nhỏ (ví dụ: trung tâm thương mại, văn phòng, khách sạn) có lắp đặt hệ thống năng lượng tái tạo, không có chuyên môn về năng lượng.
- **Ưu điểm bán hàng độc đáo (USP):** Giải pháp tối giản, giá cả phải chăng, triển khai nhanh trong 2 tuần, tập trung vào việc trực quan hóa dữ liệu và tự động hóa mà không yêu cầu tích hợp hệ thống phức tạp.

##### **Lean & Rapid Execution Requirements Contracts:**
* **[REQ-001]** Xây dựng endpoint API POST /readings để ghi nhận dữ liệu sản lượng điện từ thiết bị cảm biến. Endpoint trả về 201 Created với dữ liệu đã lưu. (đường dẫn: ./sources/api/readings.ts)
* **[DAT-001]** Tạo bảng lưu trữ dữ liệu sản lượng điện: bao gồm các trường id (string), timestamp (ISO string), device_id (string), power_output (number, kW), location (string). Bảng được lưu ở ./sources/models/PowerReading.ts.
* **[EXC-001]** Xử lý lỗi khi power_output âm hoặc vượt quá ngưỡng cho phép; trả về lỗi 400 với thông báo cụ thể. Logic xử lý nằm ở ./sources/middleware/validationErrorHandler.ts.

---