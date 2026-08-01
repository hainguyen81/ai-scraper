# EcoMonitor - Nền tảng theo dõi và tối ưu hóa năng lượng cho doanh nghiệp nhỏ

- **Lĩnh vực:** Công nghệ năng lượng tái tạo
- **Tình trạng:** Các doanh nghiệp nhỏ thiếu công cụ giám sát và phân tích tiêu thụ năng lượng một cách trực quan, dẫn đến lãng phí và chi phí cao.
- **Giải pháp & Quy trình:** Nền tảng cung cấp bảng điều khiển trực quan tích hợp với cảm biến điện và API đo lường năng lượng, tự động thu thập, hiển thị dữ liệu theo thời gian thực, đưa ra đề xuất tiết kiệm và xuất báo cáo.
- **Đối tượng mục tiêu:** Các chủ doanh nghiệp nhỏ, cửa hàng bán lẻ và cơ sở dịch vụ có nhu cầu quản lý chi phí năng lượng.
- **Ưu điểm bán hàng độc đáo (USP):** Bảng điều khiển đơn giản, tích hợp sẵn với các thiết bị đo điện phổ biến, triển khai trong 2 tuần với chi phí thấp, giúp tiết kiệm 10-15% chi phí điện ngay lập tức.

##### **Hợp đồng yêu cầu thực hiện nhanh và tinh gọn:**
* **[REQ-001]** Xây dựng API endpoint GET /api/energy-data để nhận dữ liệu công suất từ thiết bị đo điện, lưu vào cơ sở dữ liệu; mã nguồn tại ./sources/api/energy_controller.js.
* **[REQ-002]** Triển khai job cron hàng phút để trích xuất dữ liệu từ cảm biến và tính toán mức tiêu thụ trung bình; mã nguồn tại ./sources/jobs/consumption_aggregator.js.
* **[DAT-001]** Tạo bảng năng_lượng (energy_readings) với các cột: id, device_id, timestamp, power_kwh, location; mã nguồn tại ./sources/models/energy_reading.js.
* **[EXC-001]** Xử lý trường hợp thiết bị không phản hồi bằng cách ghi log cảnh báo và gửi email đến quản trị viên; mã nguồn tại ./sources/handlers/device_timeout.js.