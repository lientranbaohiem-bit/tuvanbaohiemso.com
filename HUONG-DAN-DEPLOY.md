# Hướng dẫn đưa web lên tuvanbaohiemso.com

Có 2 cách. **Cách 1 không cần cài gì, không cần token** — nên làm cách này.

---

# CÁCH 1 — Kéo thả file lên GitHub (khuyến nghị, ~10 phút)

Không cần token, không cần cài git, làm hoàn toàn trên trình duyệt.

## Bước 1 — Giải nén file mã nguồn

Giải nén `website-tuvanbaohiemso.zip`. Bên trong sẽ có:

```
index.html
san-pham.html
thai-san.html
suc-khoe.html
bao-ve-thu-nhap.html
cong-cu.html
ve-chung-toi.html
lien-he.html
CNAME
sitemap.xml
robots.txt
assets/          (thư mục)
kien-thuc/       (thư mục)
build.py
README.md
```

## Bước 2 — Tạo repo

1. Đăng nhập github.com
2. Vào https://github.com/new
3. **Repository name:** `tuvanbaohiemso`
4. Chọn **Public** — bắt buộc, vì GitHub Pages miễn phí chỉ chạy với repo public
5. **KHÔNG** tick "Add a README file"
6. Bấm **Create repository**

## Bước 3 — Kéo thả toàn bộ file vào

1. Ở trang repo vừa tạo, bấm dòng chữ **uploading an existing file**
   (hoặc vào `https://github.com/<tên-tài-khoản>/tuvanbaohiemso/upload/main`)
2. Mở thư mục vừa giải nén
3. **Chọn tất cả file và thư mục bên trong** (Ctrl+A / Cmd+A) rồi kéo thả vào ô upload

   > ⚠️ Kéo **các file bên trong**, đừng kéo cả thư mục mẹ.
   > Nếu kéo cả thư mục mẹ thì mọi thứ nằm sâu một cấp và web sẽ không chạy.
   > Sau khi thả, danh sách phải hiện `index.html` ở ngay mức đầu tiên.

4. Đợi upload xong, kéo xuống bấm **Commit changes**

## Bước 4 — Bật GitHub Pages

1. Vào `https://github.com/<tên-tài-khoản>/tuvanbaohiemso/settings/pages`
2. **Source:** chọn **Deploy from a branch**
3. **Branch:** `main` — thư mục `/ (root)` → bấm **Save**
4. Đợi 1–3 phút. Web chạy tại `https://<tên-tài-khoản>.github.io/tuvanbaohiemso/`

Mở thử link đó xem web đã lên chưa trước khi làm bước tên miền.

---

# BƯỚC CUỐI (áp dụng cho cả 2 cách) — Gắn tên miền tuvanbaohiemso.com

## A. Trỏ DNS tại nơi mua tên miền

Vào phần quản lý DNS, thêm **5 bản ghi**:

| Loại  | Tên / Host | Giá trị                     |
|-------|------------|-----------------------------|
| A     | `@`        | `185.199.108.153`           |
| A     | `@`        | `185.199.109.153`           |
| A     | `@`        | `185.199.110.153`           |
| A     | `@`        | `185.199.111.153`           |
| CNAME | `www`      | `<tên-tài-khoản>.github.io` |

Lưu ý:
- `@` nghĩa là tên miền gốc. Một số nhà cung cấp bắt gõ `tuvanbaohiemso.com` thay cho `@`.
- Nếu ở `@` đang có sẵn bản ghi A hoặc CNAME trỏ đi chỗ khác thì **xoá đi trước**.
- DNS thường vào sau 15–60 phút, có nơi lâu hơn.

## B. Khai báo tên miền trong GitHub

1. Quay lại `Settings → Pages`
2. **Custom domain:** gõ `tuvanbaohiemso.com` → **Save**
   (file `CNAME` trong repo đã có sẵn nội dung này nên thường tự điền)
3. GitHub kiểm tra DNS. Nếu báo lỗi thì DNS chưa kịp cập nhật — đợi 15–30 phút rồi Save lại.
4. Khi kiểm tra xong, tick **Enforce HTTPS** (GitHub cần tới ~1 tiếng để cấp chứng chỉ SSL).

---

# CÁCH 2 — Dùng dòng lệnh (nếu máy đã có git)

```bash
GITHUB_USER=<tên-tài-khoản> GITHUB_TOKEN=ghp_xxx ./deploy.sh
```

Token tạo tại https://github.com/settings/tokens → **Generate new token (classic)**
→ Expiration 7 days → tick ô **`repo`** → Generate → copy chuỗi `ghp_...`

Repo vẫn phải tạo sẵn trước (Bước 2 ở trên). Sau khi push xong vẫn phải làm Bước 4 và bước
gắn tên miền trên giao diện web.

> Xong việc thì vào lại trang tokens bấm **Delete** để thu hồi token.

---

# Kiểm tra sau khi lên

- [ ] `https://tuvanbaohiemso.com` mở được, có ổ khoá HTTPS
- [ ] `https://www.tuvanbaohiemso.com` tự chuyển về địa chỉ chính
- [ ] Popup chọn nhu cầu hiện ra khi vào lần đầu
- [ ] Bấm nút hotline trên điện thoại gọi được
- [ ] Bấm nút Zalo mở đúng cửa sổ chat
- [ ] Máy tính chi phí sinh con chạy ra số
- [ ] Link chạy quảng cáo theo tệp: `tuvanbaohiemso.com/?q=nhantho`

---

# Cập nhật nội dung sau này

Sửa nội dung trong `build.py`, rồi chạy `python3 build.py` để dựng lại toàn bộ trang HTML,
sau đó upload lại (hoặc chạy `./deploy.sh`).

**Không sửa trực tiếp các file `.html`** — chúng bị ghi đè mỗi lần chạy `build.py`.
