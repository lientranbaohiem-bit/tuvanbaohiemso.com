# tuvanbaohiemso.com

Website tĩnh, sinh ra từ **một file duy nhất: `build.py`**.

## Quy tắc quan trọng nhất

**Không bao giờ sửa trực tiếp các file `.html`** — chúng bị ghi đè mỗi lần chạy `build.py`.
Muốn đổi nội dung thì sửa trong `build.py` rồi chạy:

```bash
python3 build.py
```

## Cấu trúc

| File / thư mục | Vai trò |
|---|---|
| `build.py` | Nguồn duy nhất. Chứa toàn bộ nội dung, layout, dữ liệu bảng, FAQ |
| `assets/css/style.css` | Toàn bộ giao diện |
| `assets/js/main.js` | Menu, popup phân nhánh, 3 máy tính, form → Google Sheet + Zalo |
| `assets/img/` | Ảnh và hình minh hoạ |
| `_apps-script/Code.gs` | Code Google Apps Script nhận form, ghi vào sheet "Data web" |
| `sitemap.xml`, `robots.txt`, `CNAME` | Sinh tự động khi build |

## URL

Site chạy trên GitHub Pages, hỗ trợ sẵn URL không đuôi `.html`:

- `tuvanbaohiemso.com/thai-san` → phục vụ từ `thai-san.html`
- `tuvanbaohiemso.com/cong-cu/` → phục vụ từ `cong-cu/index.html`

Mọi link nội bộ trong HTML đều đã ở dạng tuyệt đối không đuôi (`/thai-san`, `/cong-cu/chi-phi-sinh-con`).
Việc này do hàm `clean_links()` trong `build.py` xử lý tự động lúc build.

## Trang

**Trang chính:** `/` · `/san-pham` · `/thai-san` · `/suc-khoe` · `/bao-ve-thu-nhap` · `/ve-chung-toi` · `/lien-he`

**Công cụ:** `/cong-cu/` (cả 3 công cụ) và 3 trang landing SEO riêng:
`/cong-cu/chi-phi-sinh-con` · `/cong-cu/thoi-gian-cho-thai-san` · `/cong-cu/ngan-sach-bao-ve`

**Kiến thức:** `/kien-thuc/` và 3 bài viết bên trong.

## Form khách gửi về đâu

Form (`<form data-lead>`) gửi dữ liệu tới Google Apps Script Web App, ghi vào file
**QUẢN LÝ KHÁCH HÀNG BẢO HIỂM**, sheet **Data web**, rồi mới mở Zalo.

Endpoint cấu hình ở hằng số `LEAD_ENDPOINT` trong `build.py`.
Đổi endpoint thì sửa hằng số đó rồi build lại — không sửa trong `main.js`.

Cột được ghi: Thời gian gửi · Họ tên · SĐT/Zalo · Quan tâm · Đã có hợp đồng · Dự sinh ·
Ghi chú · Trang gửi form · Kênh quan tâm (popup) · Nguồn truy cập · Trạng thái xử lý.

## Link chạy quảng cáo theo tệp

Thêm `?q=` vào cuối link để bỏ qua popup và vào thẳng nội dung đúng tệp:

- `tuvanbaohiemso.com/?q=thaisan` — tệp chuẩn bị sinh con
- `tuvanbaohiemso.com/?q=suckhoe` — tệp sức khoẻ, viện phí
- `tuvanbaohiemso.com/?q=nhantho` — tệp trụ cột, bảo vệ thu nhập
- `tuvanbaohiemso.com/?q=hopdong` — tệp đã có hợp đồng, muốn kiểm tra lại
