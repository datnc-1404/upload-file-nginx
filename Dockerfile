# Sử dụng Python base image
FROM python:3.9-slim

# Đặt thư mục làm việc trong container
WORKDIR /app

# Sao chép file yêu cầu và cài đặt dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn vào container
COPY . .

# Thiết lập biến môi trường Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=1205

# Mở cổng 1205
EXPOSE 1205

# Chạy ứng dụng Flask
CMD ["flask", "run"]
