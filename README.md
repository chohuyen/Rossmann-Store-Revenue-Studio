# Store Revenue Forecast & Planning Studio

Dự án phân tích và dự báo doanh thu cửa hàng bán lẻ, thử nghiệm kịch bản khuyến mãi (What-if analysis) và hỗ trợ lập kế hoạch nguồn lực kinh doanh. (Đồ án áp dụng trên bộ dữ liệu Rossmann Store Sales).

---

## Thành viên nhóm
| MSSV | Họ và tên | Vai trò / Phụ trách chính |
| :--- | :--- | :--- |
| K244060717 | Lê Trần Ngọc Huyên | Project Coordinator (Điều phối, chốt bản chính, Chương 5-6) |
| K244030343 | Nguyễn Gia Bảo | Research & Problem Definition (Bài toán, Chương 1-2, Kiểm thử) |
| K244060714 | Bùi Thi Khánh Hà | Data & EDA (Dữ liệu, Phân tích khám phá, Pipeline, Chương 4) |
| K244161824 | Lê Vy | ML Modeling & Evaluation (Baseline, Mô hình, Đánh giá, Chương 3) |
| K244060724 | K Thị Lụa | Web & Model Integration (Giao diện Web, API, Tích hợp, Demo) |
| K244161782 | Nguyễn Phan Bảo Hân | Report, QA & Presentation (Tài liệu tham khảo, QA, Slide) |

---

## 📂 Cấu trúc Thư mục Dự án
```text
Rossmann-Store-Revenue-Studio/
│
├── data/                  # Chứa dữ liệu thô và đã xử lý (train.csv, store.csv)
├── notebooks/             # Các file Jupyter Notebook chạy thử nghiệm (EDA, Model Training)
├── src/                   # Mã nguồn Python xử lý dữ liệu và mô hình
├── models/                # Lưu file mô hình đã huấn luyện (.pkl / .json)
├── web/                   # Mã nguồn ứng dụng Web / API (Flask / Streamlit)
├── requirements.txt       # Danh sách các thư viện Python cần thiết
└── README.md              # Tài liệu giới thiệu dự án
