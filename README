# Convert & Haplogrep Tool

## 📌 Giới thiệu
Tool này giúp chuyển đổi file JSON sang định dạng HSD và chạy **Haplogrep** để phân tích dữ liệu di truyền.

## 🚀 Cách sử dụng
### 1️⃣ **Chuẩn bị môi trường**
Đảm bảo bạn đã cài đặt Python và Haplogrep

### 2️⃣ **Cấu trúc thư mục**
```
.
├── input/                 # Thư mục chứa file JSON đầu vào
│   ├── 250396.json        # Ví dụ file đầu vào
├── output_hsd/            # Thư mục chứa file HSD sau khi chuyển đổi
├── output_haplogrep/      # Thư mục chứa kết quả Haplogrep
├── convert.py             # Script chuyển đổi JSON -> HSD
├── haplogrep.py           # Script chạy Haplogrep
├── script.sh              # Script chạy toàn bộ quy trình
├── README.md              # Hướng dẫn sử dụng
```

### 3️⃣ **Chạy Tool**
Bạn có thể chạy script bằng Python hoặc Shell Script:
```bash
./run.sh <input_file> + <output_name>
```

## 🛠 Cách hoạt động
### **1. Convert JSON sang HSD**
File `convert.py` sẽ đọc file JSON đầu vào và chuyển đổi thành file HSD:
```bash
python3 convert.py ./input/250396.json 250396
```
### **2. Chạy Haplogrep**
Sau khi có file HSD, script `haplogrep.py` sẽ chạy phân tích:
```bash
python3 haplogrep.py ./output_hsd/250396.hsd ./output_haplogrep/250396
```

---
🛠 **Tác giả**: Hien
📅 **Cập nhật lần cuối**: Tháng 2/2025

