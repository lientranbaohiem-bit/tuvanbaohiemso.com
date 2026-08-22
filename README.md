# tuvanbaohiemso.com — Website tư vấn bảo hiểm

Website thương hiệu "Tư Vấn Bảo Hiểm Số" (tuvanbaohiemso.com).
Tĩnh hoàn toàn (HTML/CSS/JS thuần), không cần backend, chạy được trên GitHub Pages.

## Cấu trúc

```
index.html              Trang chủ (trung tính + popup phân nhánh nhu cầu)
san-pham.html           Danh mục sản phẩm (AIA + thai sản rời)
thai-san.html           Nhánh 1 — Chuẩn bị sinh con
suc-khoe.html           Nhánh 2 — Sức khoẻ & viện phí gia đình
bao-ve-thu-nhap.html    Nhánh 3 — Bảo vệ thu nhập (tệp trụ cột)
cong-cu.html            Nhánh 4 + 3 công cụ tính + form đọc hợp đồng
ve-chung-toi.html       Giới thiệu, minh bạch hoa hồng, cam kết, tuân thủ
lien-he.html            Liên hệ + form
kien-thuc/              Blog SEO (3 bài)
_preview.py             Dựng file xem trước gộp 12 trang vào 1 file
assets/css/style.css    Design system (tone đỏ/trắng)
assets/js/main.js       Mega menu, accordion, 3 máy tính, popup phân nhánh, form
assets/img/*.svg        Minh hoạ vector tự vẽ
build.py                Trình tạo trang tĩnh — SỬA NỘI DUNG Ở ĐÂY
sitemap.xml, robots.txt SEO
```

## Sửa nội dung

Toàn bộ HTML được sinh ra từ `build.py`. **Đừng sửa trực tiếp file .html** — sửa xong chạy lại
`python3 build.py` là mọi trang được dựng lại (header, footer, menu đồng bộ tự động).

Thông tin liên hệ nằm ở đầu `build.py`:

```python
BRAND     = "Tư Vấn Bảo Hiểm Số"
PHONE     = "0777991852"
ZALO      = "https://zalo.me/0777991852"
FB        = "https://www.facebook.com/lientran.baohiem/"
SITE      = "https://tuvanbaohiemso.com"
```

Bảng chi phí bệnh viện dùng cho máy tính nằm trong `assets/js/main.js`, biến `HOSPITALS`.

## Chạy thử ở máy

```bash
python3 -m http.server 8000
# mở http://localhost:8000
```

## Deploy lên GitHub Pages

```bash
export GITHUB_TOKEN=ghp_xxx        # Personal Access Token, scope: repo
export GITHUB_USER=<username>
./deploy.sh
```

Script sẽ tạo repo, push code, bật GitHub Pages và in ra địa chỉ web.

## Việc cần làm trước khi chạy quảng cáo

1. Đọc quy chế truyền thông / mạng xã hội của hãng bảo hiểm đang hợp tác — nhiều hãng
   yêu cầu duyệt trước nội dung công khai có nhắc tới sản phẩm.
2. Đối chiếu lại số liệu sản phẩm (thời gian chờ, quyền lợi, mức phí, danh sách bệnh viện
   bảo lãnh) với bộ Quy tắc & Điều khoản mới nhất đang có hiệu lực.
3. Cập nhật lại bảng chi phí bệnh viện trong `main.js` theo bảng giá mới nhất.


## Popup phân nhánh nhu cầu

Lần đầu vào trang chủ, khách được hỏi đang quan tâm điều gì (4 nhánh: thai sản / sức khoẻ /
bảo vệ thu nhập / đã có hợp đồng). Lựa chọn được lưu vào `localStorage` với khoá `tvbhs_track`
và dùng để:

- Điều hướng ngay tới trang nhánh tương ứng
- Hiện thanh "Đang xem nội dung dành cho: ..." ở đầu mọi trang
- Hiện khối "Dành riêng cho bạn" đúng nhánh trên trang chủ

Có thể ép nhánh qua URL để dùng cho quảng cáo, ví dụ:

```
https://tuvanbaohiemso.com/?q=nhantho
https://tuvanbaohiemso.com/thai-san.html?q=thaisan
```

Dùng cách này để mỗi nhóm quảng cáo dẫn về đúng nhánh nội dung — người bấm quảng cáo
thai sản sẽ không phải xem nội dung nhân thọ và ngược lại.

## Tên miền riêng

File `CNAME` đã có sẵn nội dung `tuvanbaohiemso.com`. Sau khi deploy, trỏ DNS tại nhà cung cấp
tên miền:

| Loại  | Tên | Giá trị |
|-------|-----|---------|
| A     | @   | 185.199.108.153 |
| A     | @   | 185.199.109.153 |
| A     | @   | 185.199.110.153 |
| A     | @   | 185.199.111.153 |
| CNAME | www | `<username>.github.io` |

Sau đó vào repo → Settings → Pages → bật "Enforce HTTPS".
