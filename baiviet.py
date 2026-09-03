# -*- coding: utf-8 -*-
"""
Bai viet cum C (hop dong & boi thuong) va cum D (suc khoe & bao ve thu nhap).
Song song voi benhvien.py, dung chung bo render trong build.py.

NGUYEN TAC BIEN TAP - doc truoc khi sua file nay:
  1. Moi con so PHAI co nguon va ngay. Khong co nguon -> khong dang.
  2. KHONG SO SANH AIA VOI CAC HANG KHAC. Khong nêu ten hang de xep hang,
     cham diem, hay noi hang nao tot hon. Lien la dai ly AIA.
     Duoc phep: trich nguyen van danh sach doi tac bao lanh vien phi do BENH VIEN
     cong bo (do la dữ kiện cua benh vien, khong phai danh gia cua minh).
  3. Dan luat thi dan dung so dieu, so van ban, ngay ban hanh.
  4. Truong "kiem_chung" cua moi bang: "chinh-thuc" | "thu-cap" | "chua-xac-minh"

CUM:
  "C" -> hop dong & boi thuong   -> tru cot /san-pham.html
  "D" -> suc khoe & benh nang    -> tru cot /suc-khoe.html
  "E" -> bao ve thu nhap         -> tru cot /bao-ve-thu-nhap.html

MOI ENTRY:
{
 "slug": "bay-ly-do-tu-choi-boi-thuong",   # -> /kien-thuc/<slug>.html
 "cum": "C",
 "ngay_dang": "2026-09-04",
 "tag": "Bồi thường",              # nhan ngan hien tren the bai viet
 "doc": "7 phút đọc",
 "title": "...",                   # the <title>, co the dai
 "h1": "...",                      # tieu de tren trang, ngan hon title
 "desc": "...",                    # meta description
 "tom_tat": "...",                 # doan mo dau, HTML cho phep
 "canh_bao": "",                   # tuy chon, hien trong callout warn
 "bang": [ {"ten":..., "kiem_chung":..., "nguon":..., "cot":[...], "hang":[[...]]} ],
 "y_chinh": [ ("Tiêu đề", "Nội dung") ],   # cac muc noi dung chinh
 "khong_ro": [ "..." ],            # nhung gi chua co du lieu chac chan - tuy chon
 "faq": [ ("Hỏi", "Đáp") ],
 "lien_quan": ["slug-khac"],       # tuy chon, link noi bo them
}
"""

BAI_VIET = [
]
