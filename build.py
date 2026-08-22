# -*- coding: utf-8 -*-
"""Static site generator — Liên Trần | Tư vấn Bảo hiểm"""
import os, html, json

ROOT = os.path.dirname(os.path.abspath(__file__))
PHONE      = "0777991852"
PHONE_FMT  = "0777 991 852"
PHONE_TEL  = "+84777991852"
ZALO       = "https://zalo.me/0777991852"
FB         = "https://www.facebook.com/lientran.baohiem/"
BRAND      = "Tư Vấn Bảo Hiểm Số"
BRAND_UP   = "BẢO HIỂM SỐ"
DOMAIN     = "tuvanbaohiemso.com"
ROLE       = "Tư vấn minh bạch &middot; Quyết định bằng con số"
SITE       = "https://tuvanbaohiemso.com"

# ---------------------------------------------------------------- icons
I = {
"shield":'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
"heart":'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8l1.1 1L12 21l7.7-7.6 1.1-1a5.5 5.5 0 0 0 0-7.8z"/></svg>',
"piggy":'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a7 7 0 0 1 7-7h4a7 7 0 0 1 6.7 5H22v4h-1.5A7 7 0 0 1 17 18v2h-3v-1h-4v1H7v-2.3A7 7 0 0 1 3 12z"/><circle cx="16" cy="11" r="1"/></svg>',
"hospital":'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M4 21V7a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v14"/><path d="M2 21h20M12 8v6M9 11h6"/></svg>',
"bandage":'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="2.5" y="8" width="19" height="8" rx="4" transform="rotate(-45 12 12)"/><path d="M10 10l.01 0M14 14l.01 0M14 10l.01 0M10 14l.01 0"/></svg>',
"bank":'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M3 10l9-6 9 6"/><path d="M5 10v9M19 10v9M9 10v9M15 10v9M2 21h20"/></svg>',
"grid":'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg>',
"baby":'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="9" r="6"/><path d="M9 8h.01M15 8h.01M10 12c1.3 1 2.7 1 4 0"/><path d="M6 20c1.5-2 3.7-3 6-3s4.5 1 6 3"/></svg>',
"calc":'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2.5"/><path d="M8 6h8M8 11h.01M12 11h.01M16 11h.01M8 15h.01M12 15h.01M16 15h.01M8 19h4"/></svg>',
"clock":'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/></svg>',
"doc":'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H7a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V7z"/><path d="M14 2v5h5M9 13h6M9 17h4"/></svg>',
"chart":'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><path d="M7 15l4-5 3 3 5-7"/></svg>',
"users":'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 5.2a3.5 3.5 0 0 1 0 5.6M18 20a6.4 6.4 0 0 0-2-4.6"/></svg>',
"check":'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>',
"arrow":'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
"chev":'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M9 6l6 6-6 6"/></svg>',
"caret":'<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg>',
"search":'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>',
"menu":'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M3 6h18M3 12h18M3 18h18"/></svg>',
"phone":'<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.58 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.4 11.4 0 0 0 .58 3.6 1 1 0 0 1-.25 1z"/></svg>',
"zalo":'<svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.5 2 2 5.9 2 10.7c0 2.7 1.4 5.1 3.7 6.7-.1.9-.6 2.3-1.4 3.3-.2.3 0 .7.4.6 2-.4 3.5-1.2 4.4-1.8 1 .2 1.9.3 2.9.3 5.5 0 10-3.9 10-8.7S17.5 2 12 2z"/></svg>',
"fb":'<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.4v7A10 10 0 0 0 22 12z"/></svg>',
"mail":'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="2.5" y="4.5" width="19" height="15" rx="2.5"/><path d="M3 7l9 6 9-6"/></svg>',
"pin":'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s7-6.3 7-12a7 7 0 1 0-14 0c0 5.7 7 12 7 12z"/><circle cx="12" cy="10" r="2.6"/></svg>',
"plus":'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></svg>',
"warn":'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/></svg>',
"star":'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.5l2.9 5.9 6.6.9-4.8 4.6 1.2 6.5L12 17.3l-5.9 3.1 1.2-6.5L2.5 9.3l6.6-.9z"/></svg>',
}

# ---------------------------------------------------------------- shell
def head(title, desc, path_prefix="", canon="", extra="", body_attr=""):
    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="{BRAND}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:locale" content="vi_VN">
<link rel="canonical" href="{SITE}/{canon}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='24' fill='%23D31145'/%3E%3Ctext x='50' y='68' font-family='Arial' font-size='48' font-weight='bold' fill='white' text-anchor='middle'%3ELT%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{path_prefix}assets/css/style.css">
{extra}
</head>
<body{body_attr}>"""

MEGA = f"""
<div class="mega">
  <div class="mega-grid">
    <div>
      <p style="font-size:.72rem;letter-spacing:.13em;text-transform:uppercase;color:#8E959F;font-weight:700;margin:0 12px 8px">Theo nhu cầu của bạn</p>
      <a class="mega-link" href="{{P}}thai-san.html">
        <span class="mega-icon">{I['baby']}</span>
        <span><span class="mega-title">Chuẩn bị sinh con</span><span class="mega-desc">Thai sản rời &middot; thời gian chờ 270 ngày</span></span>
        <span class="mega-arrow">{I['chev']}</span></a>
      <a class="mega-link" href="{{P}}suc-khoe.html">
        <span class="mega-icon">{I['hospital']}</span>
        <span><span class="mega-title">Sức khoẻ &amp; viện phí gia đình</span><span class="mega-desc">Nội trú, phẫu thuật, bệnh hiểm nghèo</span></span>
        <span class="mega-arrow">{I['chev']}</span></a>
      <a class="mega-link" href="{{P}}bao-ve-thu-nhap.html">
        <span class="mega-icon">{I['shield']}</span>
        <span><span class="mega-title">Bảo vệ thu nhập gia đình</span><span class="mega-desc">Dành cho người trụ cột có người phụ thuộc</span></span>
        <span class="mega-arrow">{I['chev']}</span></a>
      <a class="mega-link" href="{{P}}cong-cu.html#doc-hop-dong">
        <span class="mega-icon">{I['doc']}</span>
        <span><span class="mega-title">Đã có hợp đồng, muốn kiểm tra lại</span><span class="mega-desc">Đọc lại hợp đồng miễn phí trong 30 phút</span></span>
        <span class="mega-arrow">{I['chev']}</span></a>
    </div>
    <div class="mega-divider"></div>
    <div>
      <p style="font-size:.72rem;letter-spacing:.13em;text-transform:uppercase;color:#8E959F;font-weight:700;margin:0 12px 8px">Theo nhóm sản phẩm</p>
      <a class="mega-link" href="{{P}}san-pham.html#bao-ve">
        <span class="mega-icon">{I['shield']}</span>
        <span><span class="mega-title">Bảo vệ cuộc sống</span></span>
        <span class="mega-arrow">{I['chev']}</span></a>
      <a class="mega-link" href="{{P}}san-pham.html#tiet-kiem">
        <span class="mega-icon">{I['piggy']}</span>
        <span><span class="mega-title">Bảo vệ cuộc sống &amp; tiết kiệm</span></span>
        <span class="mega-arrow">{I['chev']}</span></a>
      <a class="mega-link" href="{{P}}san-pham.html#suc-khoe">
        <span class="mega-icon">{I['hospital']}</span>
        <span><span class="mega-title">Chăm sóc sức khoẻ &amp; nằm viện</span></span>
        <span class="mega-arrow">{I['chev']}</span></a>
      <a class="mega-link" href="{{P}}san-pham.html#tai-nan">
        <span class="mega-icon">{I['bandage']}</span>
        <span><span class="mega-title">Bảo hiểm tai nạn</span></span>
        <span class="mega-arrow">{I['chev']}</span></a>
      <a class="mega-link" href="{{P}}san-pham.html">
        <span class="mega-icon">{I['grid']}</span>
        <span><span class="mega-title">Tất cả sản phẩm</span></span>
        <span class="mega-arrow">{I['chev']}</span></a>
    </div>
  </div>
  <div class="mega-foot">
    <a href="{{P}}cong-cu.html#chi-phi-sinh">{I['calc']} Tính chi phí sinh con</a>
    <a href="{{P}}cong-cu.html#ngan-sach">{I['chart']} Tính ngân sách bảo vệ</a>
    <a href="{{P}}cong-cu.html#doc-hop-dong">{I['doc']} Đọc lại hợp đồng miễn phí</a>
  </div>
</div>"""

LOGO = """<span class="brand-mark"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 11.5l2 2 4-4.5"/></svg></span>"""

GATE = f"""
<div class="gate" id="needGate" role="dialog" aria-modal="true" aria-label="Chọn nhu cầu">
  <div class="gate-card">
    <div class="gate-head">
      <div class="brand">{{LOGO}}<span class="brand-text"><span class="brand-name">{BRAND_UP}</span><span class="brand-role">{DOMAIN}</span></span></div>
      <h2>Bạn đang quan tâm điều gì nhất?</h2>
      <p>Chọn một mục để chúng tôi hiển thị đúng thông tin bạn cần &mdash; thay vì bắt bạn đọc hết mọi thứ.</p>
    </div>
    <div class="gate-body">
      <button class="gate-opt" data-track-pick="thaisan" data-go="{{P}}thai-san.html">
        <span class="g-ico">{I['baby']}</span>
        <span><b>Chuẩn bị sinh con</b><span>Chi phí sinh, bảo hiểm thai sản, thời gian chờ</span></span>
        <span class="g-arrow">{I['chev']}</span></button>
      <button class="gate-opt" data-track-pick="suckhoe" data-go="{{P}}suc-khoe.html">
        <span class="g-ico">{I['hospital']}</span>
        <span><b>Sức khoẻ &amp; viện phí cho gia đình</b><span>Nội trú, phẫu thuật, bệnh hiểm nghèo, bảo lãnh viện phí</span></span>
        <span class="g-arrow">{I['chev']}</span></button>
      <button class="gate-opt" data-track-pick="nhantho" data-go="{{P}}bao-ve-thu-nhap.html">
        <span class="g-ico">{I['shield']}</span>
        <span><b>Bảo vệ thu nhập &amp; tài chính dài hạn</b><span>Dành cho người trụ cột, có khoản vay hoặc người phụ thuộc</span></span>
        <span class="g-arrow">{I['chev']}</span></button>
      <button class="gate-opt" data-track-pick="hopdong" data-go="{{P}}cong-cu.html#doc-hop-dong">
        <span class="g-ico">{I['doc']}</span>
        <span><b>Đã có hợp đồng, muốn kiểm tra lại</b><span>Đọc lại hợp đồng đang có, miễn phí, không chào bán</span></span>
        <span class="g-arrow">{I['chev']}</span></button>
    </div>
    <div class="gate-foot"><button class="gate-skip" type="button">Bỏ qua, xem toàn bộ nội dung</button></div>
  </div>
</div>"""


def header(active="", P=""):
    def cls(k):
        return " active" if active == k else ""
    return f"""
<div style="background:#16181D;color:#B8BEC7;font-size:.8rem;padding:8px 0">
  <div class="wrap" style="display:flex;justify-content:space-between;gap:14px;flex-wrap:wrap;align-items:center">
    <span>Tư vấn miễn phí &middot; Không thu phí dịch vụ &middot; Không chào bán trong buổi đầu</span>
    <span style="display:flex;gap:18px;align-items:center">
      <a href="tel:{PHONE_TEL}" style="color:#fff;font-weight:600">Hotline: {PHONE_FMT}</a>
      <span style="color:#5A616B">Thứ 2 &ndash; Thứ 7 &middot; 8:00 &ndash; 21:00</span>
    </span>
  </div>
</div>
<header class="header">
  <div class="header-inner">
    <a class="brand" href="{P}index.html">
      {LOGO}
      <span class="brand-text"><span class="brand-name">{BRAND_UP}</span><span class="brand-role">{DOMAIN}</span></span>
    </a>
    <nav class="nav">
      <div class="nav-item has-mega">
        <a class="nav-link{cls('sp')}" href="{P}san-pham.html">Sản phẩm &amp; nhu cầu {I['caret']}</a>
        {MEGA.replace('{P}', P)}
      </div>
      <a class="nav-link{cls('cc')}" href="{P}cong-cu.html">Công cụ</a>
      <a class="nav-link{cls('kt')}" href="{P}kien-thuc/index.html">Kiến thức</a>
      <a class="nav-link{cls('vt')}" href="{P}ve-chung-toi.html">Về chúng tôi</a>
    </nav>
    <div class="header-actions">
      <a class="btn btn-outline btn-sm" href="tel:{PHONE_TEL}">{I['phone']} {PHONE_FMT}</a>
      <a class="btn btn-primary btn-sm" href="{P}lien-he.html">Nhận tư vấn</a>
      <button class="icon-btn burger" id="burger" aria-label="Menu">{I['menu']}</button>
    </div>
  </div>
</header>
<div class="track-band" id="trackBand">
  <div class="wrap">
    <span class="track-label"><span class="track-dot"></span>Đang xem nội dung dành cho: <b id="trackName"></b></span>
    <button class="track-change" data-open-gate="{P}index.html" type="button">Đổi nhu cầu khác</button>
  </div>
</div>
{GATE.replace('{P}', P).replace('{LOGO}', LOGO)}
<div class="mobile-nav" id="mobileNav">
  <div class="grp">Theo nhu cầu</div>
  <div class="sub">
    <a href="{P}thai-san.html">Chuẩn bị sinh con &middot; Thai sản</a>
    <a href="{P}suc-khoe.html">Sức khoẻ &amp; viện phí gia đình</a>
    <a href="{P}bao-ve-thu-nhap.html">Bảo vệ thu nhập gia đình</a>
    <a href="{P}cong-cu.html#doc-hop-dong">Đã có hợp đồng, kiểm tra lại</a>
  </div>
  <div class="grp">Theo nhóm sản phẩm</div>
  <div class="sub">
    <a href="{P}san-pham.html#bao-ve">Bảo vệ cuộc sống</a>
    <a href="{P}san-pham.html#tiet-kiem">Bảo vệ cuộc sống &amp; tiết kiệm</a>
    <a href="{P}san-pham.html#suc-khoe">Chăm sóc sức khoẻ &amp; nằm viện</a>
    <a href="{P}san-pham.html#tai-nan">Bảo hiểm tai nạn</a>
    <a href="{P}san-pham.html">Tất cả sản phẩm</a>
  </div>
  <div class="grp">Khác</div>
  <a href="{P}cong-cu.html">Công cụ tính toán</a>
  <a href="{P}kien-thuc/index.html">Kiến thức</a>
  <a href="{P}ve-chung-toi.html">Về chúng tôi</a>
  <a href="{P}lien-he.html">Liên hệ</a>
  <div style="margin-top:24px" class="btn-row">
    <a class="btn btn-primary" href="tel:{PHONE_TEL}">Gọi hotline {PHONE_FMT}</a>
    <a class="btn btn-outline" href="{ZALO}" target="_blank" rel="noopener">Nhắn Zalo</a>
  </div>
</div>"""


def footer(P=""):
    return f"""
<footer class="footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="brand" href="{P}index.html" style="margin-bottom:16px">
          {LOGO}
          <span class="brand-text"><span class="brand-name">{BRAND_UP}</span><span class="brand-role">{DOMAIN}</span></span>
        </a>
        <p style="max-width:30em">Dịch vụ tư vấn bảo hiểm độc lập. Chúng tôi giúp các gia đình tính đúng số tiền cần chuẩn bị trước khi rủi ro xảy ra &mdash; bằng con số, không bằng lời hứa.</p>
        <div class="btn-row" style="margin-top:18px;max-width:280px">
          <a class="btn btn-primary btn-sm" href="tel:{PHONE_TEL}">{I['phone']} {PHONE_FMT}</a>
        </div>
        <div class="soc">
          <a href="{FB}" target="_blank" rel="noopener" aria-label="Fanpage">{I['fb']}</a>
          <a href="{ZALO}" target="_blank" rel="noopener" aria-label="Zalo">{I['zalo']}</a>
          <a href="tel:{PHONE_TEL}" aria-label="Hotline">{I['phone']}</a>
        </div>
      </div>
      <div>
        <h4>Theo nhu cầu</h4>
        <ul>
          <li><a href="{P}thai-san.html">Chuẩn bị sinh con</a></li>
          <li><a href="{P}suc-khoe.html">Sức khoẻ &amp; viện phí</a></li>
          <li><a href="{P}bao-ve-thu-nhap.html">Bảo vệ thu nhập</a></li>
          <li><a href="{P}cong-cu.html#doc-hop-dong">Kiểm tra hợp đồng đang có</a></li>
        </ul>
      </div>
      <div>
        <h4>Công cụ &amp; kiến thức</h4>
        <ul>
          <li><a href="{P}cong-cu.html#chi-phi-sinh">Tính chi phí sinh con</a></li>
          <li><a href="{P}cong-cu.html#thoi-gian-cho">Đếm ngược thời gian chờ</a></li>
          <li><a href="{P}cong-cu.html#ngan-sach">Tính ngân sách bảo vệ</a></li>
          <li><a href="{P}kien-thuc/index.html">Bài viết kiến thức</a></li>
          <li><a href="{P}san-pham.html">Danh mục sản phẩm</a></li>
        </ul>
      </div>
      <div>
        <h4>Liên hệ</h4>
        <ul>
          <li><a href="tel:{PHONE_TEL}">Hotline: {PHONE_FMT}</a></li>
          <li><a href="{ZALO}" target="_blank" rel="noopener">Zalo: {PHONE_FMT}</a></li>
          <li><a href="{FB}" target="_blank" rel="noopener">Fanpage Facebook</a></li>
          <li>Khu vực: TP. Hồ Chí Minh &amp; toàn quốc (tư vấn từ xa)</li>
          <li>Thứ 2 &ndash; Thứ 7, 8:00 &ndash; 21:00</li>
        </ul>
      </div>
    </div>
    <div class="footnote">
      {DOMAIN} là dịch vụ tư vấn bảo hiểm độc lập, không phải doanh nghiệp bảo hiểm. Quyền lợi, mức phí và điều khoản loại trừ áp dụng theo Quy tắc &amp; Điều khoản của sản phẩm do doanh nghiệp bảo hiểm phát hành.
    </div>
    <div class="footer-bottom">
      <span>&copy; <span data-year></span> {DOMAIN}</span>
      <span>Hotline tư vấn: <a href="tel:{PHONE_TEL}" style="color:#fff">{PHONE_FMT}</a></span>
    </div>
  </div>
</footer>
<div class="fab">
  <a class="f-phone fab-pulse" href="tel:{PHONE_TEL}" aria-label="Gọi hotline">{I['phone']}</a>
  <a class="f-zalo" href="{ZALO}" target="_blank" rel="noopener" aria-label="Chat Zalo">{I['zalo']}</a>
  <a class="f-mess" href="{FB}" target="_blank" rel="noopener" aria-label="Fanpage">{I['fb']}</a>
</div>
<script src="{P}assets/js/main.js"></script>
</body>
</html>"""


def page(fname, title, desc, body, active="", P="", canon="", extra="", body_attr=""):
    out = head(title, desc, P, canon, extra, body_attr) + header(active, P) + body + footer(P)
    full = os.path.join(ROOT, fname)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(out)
    print("  ✓", fname, f"({len(out)//1024} KB)")



# ---------------------------------------------------------------- helpers
def card_prod(cat, title, desc, bullets, href, tag=None, cat_attr=None):
    lis = "".join("<li>%s</li>" % b for b in bullets)
    tg = '<span class="card-tag">%s</span>' % tag if tag else ''
    attr = ' data-cat="%s"' % cat_attr if cat_attr else ''
    return ('<article class="card prod"%s>%s'
            '<div class="prod-top"><div class="prod-cat">%s</div><h3>%s</h3></div>'
            '<div class="prod-body"><p>%s</p><ul>%s</ul>'
            '<a class="card-link" href="%s">Tìm hiểu thêm %s</a></div></article>'
            ) % (attr, tg, cat, title, desc, lis, href, I['arrow'])


POSTS = [
    dict(slug="chi-phi-sinh-con.html",
         title="Chi phí sinh con 2026: bóc tách từng khoản, và phần BHYT không trả",
         desc="Sinh thường dịch vụ, sinh mổ dịch vụ, bệnh viện công và bệnh viện tư — con số thật và khoảng chênh gia đình phải tự gánh.",
         date="20/08/2026", read="8 phút đọc", thumb="thumb-1.svg", tag="Chi phí thật"),
    dict(slug="thoi-gian-cho-thai-san.html",
         title="Thời gian chờ bảo hiểm thai sản: vì sao que thử hai vạch là đã trễ",
         desc="270 hay 365 ngày, tính từ lúc nào, và cách xác định hạn chót của riêng bạn bằng một phép tính ngược đơn giản.",
         date="20/08/2026", read="6 phút đọc", thumb="thumb-2.svg", tag="Đồng hồ đang chạy"),
    dict(slug="ke-khai-suc-khoe.html",
         title="Phần lớn vụ từ chối bồi thường đến từ đúng một ô trong tờ khai",
         desc="Kê khai tình trạng sức khoẻ — thứ ai cũng ký nhanh nhất và là thứ quyết định hợp đồng của bạn có giá trị hay không.",
         date="20/08/2026", read="7 phút đọc", thumb="thumb-3.svg", tag="Bồi thường"),
]


def post_cards(P, limit=3, exclude=None):
    out = []
    for p in POSTS:
        if exclude and p["slug"] == exclude:
            continue
        out.append(
            '<a class="card post" href="%skien-thuc/%s">'
            '<div class="post-img"><img src="%sassets/img/%s" alt="%s" loading="lazy"></div>'
            '<div class="post-body"><div class="post-meta"><span>%s</span><span class="dot"></span><span>%s</span></div>'
            '<h3>%s</h3><p>%s</p><span class="card-link">Đọc bài %s</span></div></a>'
            % (P, p["slug"], P, p["thumb"], p["title"], p["tag"], p["read"],
               p["title"], p["desc"], I['arrow']))
        if len(out) >= limit:
            break
    return "".join(out)


def faq(items):
    out = []
    for q, a in items:
        out.append('<div class="acc"><button class="acc-q">%s<span class="pm">%s</span></button>'
                   '<div class="acc-a"><div class="acc-a-inner">%s</div></div></div>'
                   % (q, I['plus'], a))
    return "".join(out)


def feat(icon, title, body):
    return ('<div class="feat"><span class="feat-ico">%s</span>'
            '<div><h4>%s</h4><p>%s</p></div></div>') % (I[icon], title, body)


def rows(data):
    return "".join("<tr>" + "".join("<td>%s</td>" % c for c in r) + "</tr>" for r in data)


def tbl(headers, data):
    th = "".join("<th>%s</th>" % h for h in headers)
    return ('<div class="tbl-wrap"><table class="tbl"><thead><tr>%s</tr></thead>'
            '<tbody>%s</tbody></table></div>') % (th, rows(data))


def cta(P="", title="Bạn muốn tính cho trường hợp cụ thể của mình?",
        body="Nhắn cho chúng tôi tình huống của bạn — dự định sinh khi nào, đang có bảo hiểm gì, ngân sách khoảng bao nhiêu. Chúng tôi trả lời trong 15 phút giờ hành chính, và trả lời bằng con số."):
    return ('<section class="section"><div class="wrap"><div class="cta-band">'
            '<h2>%s</h2><p>%s</p><div class="btn-row">'
            '<a class="btn btn-white btn-lg" href="%s" target="_blank" rel="noopener">%s Nhắn Zalo %s</a>'
            '<a class="btn btn-lg" style="background:rgba(255,255,255,.14);color:#fff;border-color:rgba(255,255,255,.4)" href="%slien-he.html">Gửi câu hỏi qua form</a>'
            '</div></div></div></section>') % (title, body, ZALO, I['zalo'], PHONE_FMT, P)


def page_head(crumb, title, desc, P=""):
    return ('<section class="page-head"><div class="wrap">'
            '<div class="crumb"><a href="%sindex.html">Trang chủ</a> / %s</div>'
            '<h1>%s</h1><p>%s</p></div></section>') % (P, crumb, title, desc)


HOME_FAQ = [
    ("Chúng tôi đã có bảo hiểm y tế rồi, còn cần bảo hiểm thai sản không?",
     "BHYT rất quan trọng và bạn nên giữ. Nhưng con số thực tế thế này: một ca sinh mổ dịch vụ tại bệnh viện công lớn ở TP.HCM vào khoảng 25–45 triệu, trong khi BHYT chi trả phần tương ứng khoảng 6–10 triệu khi đi đúng tuyến. Phần chênh còn lại là khoản gia đình tự lo. Câu hỏi không phải &ldquo;có cần không&rdquo;, mà là &ldquo;phần chênh đó mình chuẩn bị bằng cách nào&rdquo;."),
    ("Thời gian chờ 270 ngày nghĩa là gì?",
     "Là khoảng thời gian từ lúc hợp đồng có hiệu lực đến lúc quyền lợi thai sản bắt đầu được chi trả. Nếu bạn sinh trước khi hết thời gian chờ, quyền lợi thai sản của lần sinh đó sẽ không được chi trả. Nói cách khác: lúc que thử hai vạch mới đi mua thì đã trễ khoảng một năm. Đây là lý do chúng tôi làm hẳn một công cụ đếm ngược trên trang này."),
    ("Mua bảo hiểm có phải là lỗ không? Nghe nói 5 năm đầu âm vốn.",
     "Bạn nói đúng, và chúng tôi không phủ nhận. Giá trị hoàn lại trong 5–7 năm đầu thường âm, do cấu trúc chi phí ban đầu của hợp đồng. Vì vậy chúng tôi không tư vấn bảo hiểm như một kênh đầu tư sinh lời. Nó là công cụ chuyển giao rủi ro — bạn trả một khoản nhỏ đều đặn để không phải gánh một khoản lớn đột ngột. Nếu mục tiêu của bạn là sinh lời, có kênh khác phù hợp hơn và chúng tôi sẽ nói thẳng điều đó."),
    ("Lỡ giữa chừng chúng tôi không đóng nổi phí thì sao?",
     "Đây là câu hỏi nên hỏi TRƯỚC khi ký chứ không phải sau. Tuỳ sản phẩm, bạn có các lựa chọn: giảm số tiền bảo hiểm để giảm phí, dùng giá trị tài khoản để tự động đóng phí trong một thời gian, tạm dừng đóng phí, hoặc chấm dứt hợp đồng và nhận giá trị hoàn lại. Mỗi lựa chọn có hệ quả khác nhau — chúng tôi giải thích rõ từng cái ngay trong buổi tư vấn đầu tiên, trước khi bạn quyết định."),
    ("Vì sao có người bị từ chối bồi thường?",
     "Phần lớn trường hợp bị từ chối xuất phát từ việc kê khai tình trạng sức khoẻ không đầy đủ tại thời điểm tham gia — kể cả những lần khám bệnh mà khách hàng nghĩ là chuyện nhỏ. Cách phòng duy nhất là kê khai trung thực và đầy đủ ngay từ đầu, đồng thời giữ lại bản sao hồ sơ. Với khách của chúng tôi, chúng tôi ngồi khai cùng và giữ bản sao để đối chiếu về sau."),
    ("Buổi tư vấn đầu tiên có mất phí không? Có bị ép mua không?",
     "Không mất phí và không ép. Buổi đầu chúng tôi không mang bảng minh hoạ quyền lợi — chỉ hỏi và tính. Rất nhiều buổi kết thúc bằng việc chúng tôi nói: hợp đồng bạn đang có đã ổn, chưa cần mua thêm gì. Với chúng tôi đó cũng là một kết quả tốt."),
]


SP_FAQ = [
    ("Vì sao bạn tư vấn sản phẩm này mà không phải sản phẩm khác?",
     "Câu hỏi này buộc người tư vấn phải giải thích logic đằng sau đề xuất, thay vì chỉ đưa ra một gói. Nếu câu trả lời chỉ xoay quanh ưu điểm sản phẩm mà không nhắc gì tới tình huống cụ thể của bạn, đó là dấu hiệu người đó đang bán thứ họ muốn bán chứ không phải thứ bạn cần."),
    ("Sản phẩm này có nhược điểm gì?",
     "Mọi sản phẩm bảo hiểm đều có nhược điểm: giá trị hoàn lại thấp trong những năm đầu, điều khoản loại trừ, thời gian chờ, rủi ro thị trường với dòng liên kết đầu tư. Một người tư vấn không nêu được nhược điểm nào là người hoặc chưa đọc kỹ điều khoản, hoặc đang giấu bạn điều gì đó."),
    ("Nếu giữa chừng chúng tôi không đóng nổi phí thì có những lựa chọn nào?",
     "Đây là câu hỏi nên hỏi trước khi ký. Người tư vấn cần chỉ ra được các lựa chọn cụ thể theo điều khoản sản phẩm và hệ quả tài chính của từng lựa chọn. Nếu họ trả lời chung chung kiểu &ldquo;bạn yên tâm, không sao đâu&rdquo;, thì bạn chưa nhận được câu trả lời."),
    ("Chúng tôi có thể xem trước bộ Quy tắc và Điều khoản không?",
     "Bạn hoàn toàn có quyền yêu cầu và nên yêu cầu, đặc biệt là phần điều khoản loại trừ và bảng thời gian chờ theo từng nhóm quyền lợi. Đây là tài liệu chính thức, không phải tài liệu nội bộ."),
]

TS_COMPARE = [
    ["Điều kiện tham gia",
     "Tham gia độc lập, không cần hợp đồng nhân thọ chính",
     "Bắt buộc gắn vào một hợp đồng nhân thọ chính"],
    ["Chi phí ban đầu",
     "Thấp &mdash; chỉ trả cho phần quyền lợi mình cần",
     "Cao hơn nhiều &mdash; phí hợp đồng chính cộng phí thẻ bổ trợ"],
    ["Cam kết thời gian",
     "Ngắn hạn, tái tục theo kỳ",
     "Dài hạn, thường 15&ndash;20 năm"],
    ["Thời gian chờ thai sản",
     "270 ngày",
     "Thường 270&ndash;365 ngày tuỳ sản phẩm"],
    ["Giá trị tích luỹ",
     "Không có &mdash; đây là sản phẩm thuần bảo vệ",
     "Có, nhưng giá trị hoàn lại 5&ndash;7 năm đầu thường thấp hơn tổng phí đã đóng"],
    ["Quyền lợi bảo vệ dài hạn",
     "Không &mdash; chỉ giải quyết nhu cầu trước mắt",
     "Có &mdash; bảo vệ thu nhập, bệnh hiểm nghèo, tử vong"],
    ["Phù hợp với ai",
     "Gia đình trẻ chuẩn bị sinh con, chưa sẵn sàng cam kết dài hạn",
     "Gia đình đã ổn định, muốn một kế hoạch bảo vệ tổng thể lâu dài"],
]

TS_FAQ = [
    ("Chúng tôi đã có bảo hiểm sức khoẻ của công ty, có cần mua thêm thai sản không?",
     "Cần kiểm tra cụ thể chứ không nên mặc định theo hướng nào. Nhiều gói bảo hiểm sức khoẻ do công ty cấp không bao gồm quyền lợi thai sản, hoặc có nhưng với hạn mức rất thấp. Ngoài ra, gói của công ty chấm dứt khi bạn nghỉ việc &mdash; và giai đoạn nghỉ sinh lại là lúc nhiều người thay đổi công việc nhất. Bạn gửi chúng tôi bảng quyền lợi công ty cấp, chúng tôi đọc giúp và nói rõ bạn đang có gì."),
    ("Mua rồi mà cuối cùng không sinh nữa thì sao?",
     "Đây là bản chất của bảo hiểm: bạn trả tiền để chuyển giao rủi ro, và nếu sự kiện không xảy ra thì phí đã đóng không được hoàn lại. Cách nhìn hợp lý là xem đó như chi phí của sự yên tâm trong khoảng thời gian đó, tương tự bảo hiểm xe. Nếu bạn chưa chắc chắn về kế hoạch sinh con, chúng tôi sẽ nói thẳng là nên chờ đến khi kế hoạch rõ hơn."),
    ("Gói này có bao gồm quyền lợi cho chúng tôi bé sau sinh không?",
     "Tuỳ sản phẩm và tuỳ gói. Quyền lợi cho trẻ sơ sinh thường có điều kiện riêng về độ tuổi tối thiểu và có thể phải tham gia như một người được bảo hiểm riêng. Đây là mục chúng tôi luôn đi qua kỹ với khách vì nó hay bị hiểu nhầm."),
    ("Nếu thai kỳ có biến chứng thì được chi trả thế nào?",
     "Biến chứng thai kỳ thường thuộc nhóm quyền lợi riêng, có thể có hạn mức và điều kiện khác với quyền lợi sinh thông thường. Đây là phần quan trọng nhất của sản phẩm về mặt tài chính, vì nó xử lý đúng những kịch bản mà gia đình không tự lo được. Chúng tôi sẽ chỉ rõ mục này trong bộ điều khoản trước khi bạn quyết định."),
    ("Mức phí cụ thể là bao nhiêu?",
     "Mức phí phụ thuộc vào hạng mức quyền lợi bạn chọn, độ tuổi và kết quả thẩm định. Chúng tôi không đưa một con số chung ở đây vì nó dễ gây hiểu nhầm. Bạn nhắn cho chúng tôi độ tuổi và mốc dự sinh, chúng tôi gửi lại bảng phí chính thức đang áp dụng."),
]

ART1_TBL = [
    ["Sinh thường &mdash; dịch vụ", "15 &ndash; 25 triệu", "3 &ndash; 5 triệu", "<strong>12 &ndash; 20 triệu</strong>"],
    ["Sinh mổ &mdash; dịch vụ", "25 &ndash; 45 triệu", "6 &ndash; 10 triệu", "<strong>19 &ndash; 35 triệu</strong>"],
    ["Sinh tại BV tư / phụ sản quốc tế", "35 &ndash; 95 triệu", "4 &ndash; 11 triệu", "<strong>31 &ndash; 84 triệu</strong>"],
    ["Sinh tại BV quốc tế cao cấp", "70 &ndash; 160 triệu", "Gần như không áp dụng", "<strong>70 &ndash; 160 triệu</strong>"],
]

ART2_TBL = [
    ["Thời gian chờ thai sản là bao nhiêu ngày?",
     "Quyết định bạn còn kịp hay không. Chênh lệch giữa 270 và 365 ngày là ba tháng cửa sổ chuẩn bị."],
    ["Thời gian chờ tính từ ngày nào?",
     "Tính từ ngày hợp đồng có hiệu lực, không phải ngày nộp hồ sơ. Khoảng cách giữa hai mốc có thể là vài tuần."],
    ["Các nhóm quyền lợi khác có thời gian chờ riêng không?",
     "Có. Tai nạn, bệnh thông thường, bệnh đặc biệt và thai sản thường có thời gian chờ khác nhau trong cùng một hợp đồng."],
    ["Nếu hợp đồng mất hiệu lực rồi khôi phục thì thời gian chờ có tính lại không?",
     "Thường là có. Đây là lý do việc duy trì hợp đồng liên tục quan trọng hơn nhiều người nghĩ."],
    ["Sinh non trước khi hết thời gian chờ thì xử lý thế nào?",
     "Cần xem điều khoản cụ thể của từng sản phẩm. Đây là tình huống hiếm nhưng có thật và nên hỏi trước khi ký."],
]

ART3_TBL = [
    ["Kê khai sức khoẻ không đầy đủ",
     "Tiền sử bệnh không được khai tại thời điểm tham gia, bị phát hiện khi thẩm định hồ sơ bồi thường",
     "Tự đọc, tự khai, khai đủ mọi hồ sơ y tế đã có. Giữ bản sao."],
    ["Sự kiện xảy ra trong thời gian chờ",
     "Quyền lợi chưa có hiệu lực tại thời điểm phát sinh",
     "Nắm rõ bảng thời gian chờ theo từng nhóm quyền lợi ngay khi ký."],
    ["Thuộc điều khoản loại trừ",
     "Sự kiện nằm trong danh sách trường hợp sản phẩm không chi trả",
     "Đọc kỹ mục loại trừ trước khi ký &mdash; phần ngắn nhất nhưng quyết định nhiều nhất."],
    ["Hợp đồng mất hiệu lực do chậm đóng phí",
     "Quá thời gian gia hạn đóng phí, hợp đồng không còn hiệu lực tại thời điểm sự kiện",
     "Đặt nhắc lịch đóng phí. Với khách của chúng tôi, chúng tôi nhắc trước 7 ngày mỗi kỳ."],
    ["Hồ sơ bồi thường thiếu giấy tờ",
     "Không phải từ chối vĩnh viễn, nhưng làm kéo dài thời gian xử lý",
     "Nắm danh sách giấy tờ cần thiết ngay từ khi nhập viện, không đợi tới lúc xuất viện."],
]

# ================================================================ TRANG CHỦ
home = f"""
<section class="hero">
  <div class="hero-inner">
    <div>
      <span class="eyebrow">Dịch vụ tư vấn bảo hiểm độc lập</span>
      <h1>Chọn đúng bảo hiểm &mdash;<br><span class="hl">bằng con số</span>, không bằng lời hứa.</h1>
      <p class="hero-sub">Chúng tôi giúp bạn biết chính xác gia đình cần chuẩn bị bao nhiêu tiền, đang thiếu quyền lợi gì và nên bắt đầu từ đâu. Buổi đầu tiên miễn phí và không chào bán bất kỳ sản phẩm nào.</p>
      <div id="heroPicker">
        <p style="font-weight:600;margin-bottom:2px">Bạn đang quan tâm điều gì nhất?</p>
        <div class="entry-grid">
          <a class="entry" href="thai-san.html?q=thaisan"><span class="e-ico">{I['baby']}</span><span><b>Chuẩn bị sinh con</b><span>Chi phí sinh &middot; thai sản</span></span></a>
          <a class="entry" href="suc-khoe.html?q=suckhoe"><span class="e-ico">{I['hospital']}</span><span><b>Sức khoẻ &amp; viện phí</b><span>Nội trú &middot; bệnh hiểm nghèo</span></span></a>
          <a class="entry" href="bao-ve-thu-nhap.html?q=nhantho"><span class="e-ico">{I['shield']}</span><span><b>Bảo vệ thu nhập</b><span>Cho người trụ cột gia đình</span></span></a>
          <a class="entry" href="cong-cu.html?q=hopdong#doc-hop-dong"><span class="e-ico">{I['doc']}</span><span><b>Đã có hợp đồng</b><span>Kiểm tra lại miễn phí</span></span></a>
        </div>
      </div>
      <div class="hero-stats">
        <div class="hero-stat"><b>12+</b><span>sản phẩm trong danh mục tư vấn</span></div>
        <div class="hero-stat"><b>3</b><span>công cụ tính miễn phí, không cần để lại thông tin</span></div>
        <div class="hero-stat"><b>15 phút</b><span>thời gian phản hồi trong giờ làm việc</span></div>
      </div>
    </div>
    <div class="hero-art">
      <img src="assets/img/hero.svg" alt="Gia đình được bảo vệ bởi kế hoạch tài chính" width="800" height="620">
      <div class="hero-badge">
        <span class="hb-ico">{I['check']}</span>
        <span><b>Nói trước cả nhược điểm</b><span>Trước khi bạn đặt bút ký</span></span>
      </div>
    </div>
  </div>
</section>

<section class="trust">
  <div class="wrap" style="padding:0">
    <div class="trust-grid">
      <div class="trust-item"><div class="ti-ico">{I['calc']}</div><b>Tư vấn bằng bảng tính</b><span>Mọi đề xuất đều đi kèm con số cụ thể cho hoàn cảnh của bạn, không nói chung chung.</span></div>
      <div class="trust-item"><div class="ti-ico">{I['warn']}</div><b>Nêu rõ nhược điểm</b><span>Giá trị hoàn lại, điều khoản loại trừ, thời gian chờ &mdash; nói trước khi bạn hỏi.</span></div>
      <div class="trust-item"><div class="ti-ico">{I['doc']}</div><b>Không thu phí dịch vụ</b><span>Tư vấn, đọc lại hợp đồng và hỗ trợ hồ sơ bồi thường đều miễn phí.</span></div>
      <div class="trust-item"><div class="ti-ico">{I['users']}</div><b>Đồng hành sau khi ký</b><span>Nhắc kỳ đóng phí và hỗ trợ trực tiếp khi bạn cần làm hồ sơ bồi thường.</span></div>
    </div>
  </div>
</section>

<section class="section-sm">
  <div class="wrap">
    <div class="for-you" data-track="thaisan">
      <div class="fy-band">
        <span class="eyebrow">Dành riêng cho bạn</span>
        <h3>Bạn đang chuẩn bị sinh con</h3>
        <p>Việc quan trọng nhất lúc này là biết hai con số: chi phí ca sinh và hạn chót còn kịp tham gia bảo hiểm. Bắt đầu từ đây.</p>
        <div class="fy-links">
          <a class="fy-link" href="cong-cu.html#chi-phi-sinh"><span class="fyi">{I['calc']}</span>Tính chi phí ca sinh của bạn</a>
          <a class="fy-link" href="cong-cu.html#thoi-gian-cho"><span class="fyi">{I['clock']}</span>Bạn còn kịp bao nhiêu ngày?</a>
          <a class="fy-link" href="thai-san.html"><span class="fyi">{I['baby']}</span>Gói thai sản rời &mdash; chi tiết</a>
        </div>
      </div>
    </div>
    <div class="for-you" data-track="suckhoe">
      <div class="fy-band">
        <span class="eyebrow">Dành riêng cho bạn</span>
        <h3>Bạn đang quan tâm sức khoẻ &amp; viện phí gia đình</h3>
        <p>Đây là nhóm quyền lợi được dùng tới nhiều nhất trong thực tế, và cũng là nhóm bị thiếu nhiều nhất trong các hợp đồng chúng tôi đọc lại.</p>
        <div class="fy-links">
          <a class="fy-link" href="suc-khoe.html"><span class="fyi">{I['hospital']}</span>Khoảng trống giữa BHYT và viện phí thật</a>
          <a class="fy-link" href="san-pham.html#suc-khoe"><span class="fyi">{I['grid']}</span>Sản phẩm sức khoẻ &amp; bệnh hiểm nghèo</a>
          <a class="fy-link" href="cong-cu.html#doc-hop-dong"><span class="fyi">{I['doc']}</span>Kiểm tra hợp đồng đang có</a>
        </div>
      </div>
    </div>
    <div class="for-you" data-track="nhantho">
      <div class="fy-band">
        <span class="eyebrow">Dành riêng cho bạn</span>
        <h3>Bạn là người trụ cột thu nhập của gia đình</h3>
        <p>Câu hỏi không phải &ldquo;nếu tôi mất đi&rdquo;, mà là &ldquo;nếu tôi không đi làm được sáu tháng thì ai trả khoản vay và tiền học của con&rdquo;. Bắt đầu bằng một con số.</p>
        <div class="fy-links">
          <a class="fy-link" href="cong-cu.html#ngan-sach"><span class="fyi">{I['chart']}</span>Gia đình bạn cần bảo vệ bao nhiêu?</a>
          <a class="fy-link" href="bao-ve-thu-nhap.html"><span class="fyi">{I['shield']}</span>Bài toán thay thế thu nhập</a>
          <a class="fy-link" href="san-pham.html#bao-ve"><span class="fyi">{I['grid']}</span>Sản phẩm bảo vệ cuộc sống</a>
        </div>
      </div>
    </div>
    <div class="for-you" data-track="hopdong">
      <div class="fy-band">
        <span class="eyebrow">Dành riêng cho bạn</span>
        <h3>Bạn đã có hợp đồng và muốn kiểm tra lại</h3>
        <p>Rất nhiều người đóng phí đều đặn nhiều năm mà không biết chính xác mình đang được bảo vệ những gì. Việc này sửa được, và không mất phí.</p>
        <div class="fy-links">
          <a class="fy-link" href="cong-cu.html#doc-hop-dong"><span class="fyi">{I['doc']}</span>Đặt buổi đọc lại hợp đồng</a>
          <a class="fy-link" href="kien-thuc/ke-khai-suc-khoe.html"><span class="fyi">{I['warn']}</span>Vì sao hồ sơ bị từ chối chi trả</a>
          <a class="fy-link" href="san-pham.html"><span class="fyi">{I['grid']}</span>Đối chiếu với danh mục sản phẩm</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="center" style="max-width:52em;margin:0 auto 44px">
      <span class="eyebrow">Bắt đầu từ đâu</span>
      <h2>Bốn tình huống chúng tôi gặp nhiều nhất</h2>
      <p class="lead">Bảo hiểm không có một câu trả lời chung. Điểm khởi đầu đúng phụ thuộc vào việc bạn đang lo điều gì nhất.</p>
    </div>
    <div class="grid g4">
      <a class="card" href="thai-san.html?q=thaisan">
        <div class="card-ico">{I['baby']}</div>
        <h3>Chuẩn bị sinh con</h3>
        <p>Nhu cầu duy nhất có <b>hạn chót thật</b>: thời gian chờ 270&ndash;365 ngày. Biết muộn là mất đúng một chu kỳ.</p>
        <span class="card-link">Xem chi tiết {I['arrow']}</span>
      </a>
      <a class="card" href="suc-khoe.html?q=suckhoe">
        <div class="card-ico">{I['hospital']}</div>
        <h3>Sức khoẻ &amp; viện phí</h3>
        <p>Một lần nằm viện có thể xoá nhiều năm tiết kiệm. Đây là nhóm quyền lợi <b>dùng tới nhiều nhất</b>.</p>
        <span class="card-link">Xem chi tiết {I['arrow']}</span>
      </a>
      <a class="card" href="bao-ve-thu-nhap.html?q=nhantho">
        <div class="card-ico">{I['shield']}</div>
        <h3>Bảo vệ thu nhập</h3>
        <p>Dành cho người trụ cột có khoản vay và người phụ thuộc. Bài toán ở đây là <b>thay thế thu nhập</b>, không phải tiết kiệm.</p>
        <span class="card-link">Xem chi tiết {I['arrow']}</span>
      </a>
      <a class="card" href="cong-cu.html?q=hopdong#doc-hop-dong">
        <div class="card-ico">{I['doc']}</div>
        <h3>Đã có hợp đồng</h3>
        <p>Đóng phí vài năm, người tư vấn cũ đã nghỉ, không rõ mình có gì. <b>Rất phổ biến &mdash; và sửa được.</b></p>
        <span class="card-link">Kiểm tra miễn phí {I['arrow']}</span>
      </a>
    </div>
  </div>
</section>

<section class="section bg-grey">
  <div class="wrap">
    <div class="center" style="max-width:52em;margin:0 auto 10px">
      <span class="eyebrow">Hành trình làm việc</span>
      <h2>Từ lúc bạn đọc trang này đến lúc có một kế hoạch</h2>
      <p class="lead">Không có bước nào ép bạn quyết định. Bạn có thể dừng ở bất kỳ bước nào và vẫn mang đi được thứ có giá trị.</p>
    </div>
    <div class="journey">
      <div class="jstep"><div class="jnum">1</div><h4>Hiểu vấn đề</h4><p>Đọc bài viết hoặc xem gói phù hợp với tình huống của bạn. Không cần để lại thông tin gì.</p></div>
      <div class="jstep"><div class="jnum">2</div><h4>Thấy con số của mình</h4><p>Dùng công cụ tính trên trang để biết chi phí dự kiến và khoảng trống tài chính của riêng bạn.</p></div>
      <div class="jstep"><div class="jnum">3</div><h4>Hỏi một câu cụ thể</h4><p>Nhắn Zalo hoặc gọi hotline. Chúng tôi trả lời bằng con số, không bằng lời chào bán.</p></div>
      <div class="jstep"><div class="jnum">4</div><h4>Buổi phân tích 45 phút</h4><p>Chúng tôi hỏi, tính, và chỉ ra bạn đang thiếu gì. Kèm 2&ndash;3 phương án và nhược điểm của từng phương án.</p></div>
      <div class="jstep"><div class="jnum">5</div><h4>Bạn quyết định</h4><p>Theo nhịp của bạn. Kể cả khi kết luận là chưa cần mua thêm gì &mdash; với chúng tôi đó cũng là một kết quả tốt.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="center" style="max-width:52em;margin:0 auto 44px">
      <span class="eyebrow">Công cụ miễn phí</span>
      <h2>Ba con số nên biết trước khi nói chuyện với bất kỳ tư vấn viên nào</h2>
      <p class="lead">Dùng ngay trên trang, không cần để lại thông tin.</p>
    </div>
    <div class="grid g3">
      <div class="tool">
        <div class="card-ico">{I['calc']}</div>
        <h3>Chi phí sinh con thực tế</h3>
        <p style="color:var(--grey-600);font-size:.94rem">Chọn bệnh viện và hình thức sinh &mdash; công cụ trả về tổng chi phí dự kiến, phần BHYT chi trả, và <b>phần gia đình phải tự trả</b>.</p>
        <a class="btn btn-outline btn-sm" style="margin-top:auto;align-self:flex-start" href="cong-cu.html#chi-phi-sinh">Tính ngay {I['arrow']}</a>
      </div>
      <div class="tool">
        <div class="card-ico">{I['clock']}</div>
        <h3>Đếm ngược thời gian chờ</h3>
        <p style="color:var(--grey-600);font-size:.94rem">Nhập thời điểm dự định sinh &mdash; công cụ tính ngược ra <b>hạn chót phải hoàn tất hồ sơ</b>. Nhiều người biết con số này khi đã muộn đúng một năm.</p>
        <a class="btn btn-outline btn-sm" style="margin-top:auto;align-self:flex-start" href="cong-cu.html#thoi-gian-cho">Kiểm tra {I['arrow']}</a>
      </div>
      <div class="tool">
        <div class="card-ico">{I['chart']}</div>
        <h3>Ngân sách bảo vệ gia đình</h3>
        <p style="color:var(--grey-600);font-size:.94rem">Nhập thu nhập, khoản vay và số người phụ thuộc &mdash; công cụ ước tính <b>số tiền bảo vệ cần có</b> và mức phí hợp lý theo thu nhập.</p>
        <a class="btn btn-outline btn-sm" style="margin-top:auto;align-self:flex-start" href="cong-cu.html#ngan-sach">Tính ngay {I['arrow']}</a>
      </div>
    </div>
  </div>
</section>

<section class="section bg-grey">
  <div class="wrap">
    <div class="center" style="max-width:50em;margin:0 auto 44px">
      <span class="eyebrow">Danh mục tư vấn</span>
      <h2>Sản phẩm chúng tôi đang tư vấn</h2>
      <p class="lead">Danh mục AIA Việt Nam, cùng gói bảo hiểm thai sản rời phân phối qua Fuse &times; Techcombank. Việc của chúng tôi không phải bán gói đắt nhất, mà là tìm gói phù hợp với ngân sách và tình huống thật của gia đình bạn.</p>
    </div>
    <div class="grid g3">
      {card_prod('Bảo vệ cuộc sống','AIA &ndash; Khoẻ Trọn Vẹn','Bảo hiểm liên kết chung &mdash; bảo vệ dài hạn kết hợp tài khoản tích luỹ có lãi suất công bố định kỳ.',['Quyền lợi bảo vệ chính linh hoạt','Có thể gắn thêm thẻ sức khoẻ, bệnh hiểm nghèo','Điều chỉnh phí và số tiền bảo hiểm theo giai đoạn'],'san-pham.html#bao-ve')}
      {card_prod('Bảo vệ cuộc sống','AIA &ndash; Khoẻ An Nhiên','Giải pháp bảo vệ tập trung vào rủi ro sức khoẻ và tử vong, cấu trúc đơn giản, dễ hiểu.',['Phù hợp người muốn thuần bảo vệ','Chi phí bảo vệ tối ưu hơn dòng đầu tư','Dễ kết hợp với sản phẩm bổ trợ'],'san-pham.html#bao-ve')}
      {card_prod('Bảo vệ &amp; tiết kiệm','AIA &ndash; Vững Tương Lai','Bảo hiểm liên kết chung hướng tới mục tiêu dài hạn: học vấn cho con, quỹ hưu trí.',['Tích luỹ theo mục tiêu có thời hạn','Bảo vệ duy trì kể cả khi có biến cố','Có quyền lợi miễn đóng phí khi cần'],'san-pham.html#tiet-kiem')}
      {card_prod('Sức khoẻ &amp; nằm viện','Chăm Sóc Sức Khoẻ','Sản phẩm bổ trợ chi trả viện phí nội trú, ngoại trú, phẫu thuật theo hạn mức lựa chọn.',['Nhiều hạng mức quyền lợi để chọn','Có mạng lưới bảo lãnh viện phí','Đây là quyền lợi bị thiếu nhiều nhất'],'suc-khoe.html')}
      {card_prod('Sức khoẻ &amp; nằm viện','Bệnh Hiểm Nghèo','Chi trả một khoản tiền mặt khi được chẩn đoán bệnh hiểm nghèo thuộc danh sách bảo hiểm.',['Tiền mặt để lo chi phí ngoài viện phí','Bù đắp phần thu nhập mất đi','Quyền lợi theo giai đoạn bệnh'],'suc-khoe.html')}
      {card_prod('Fuse &times; Techcombank','Bảo hiểm thai sản rời','Gói thai sản tham gia độc lập, không bắt buộc mua kèm hợp đồng nhân thọ dài hạn.',['Thời gian chờ 270 ngày','Không phân biệt sinh thường và sinh mổ','Bảo lãnh viện phí tại nhiều bệnh viện sản lớn'],'thai-san.html', tag='Nổi bật')}
    </div>
    <div class="center" style="margin-top:38px">
      <a class="btn btn-outline btn-lg" href="san-pham.html">Xem tất cả sản phẩm {I['arrow']}</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div><img src="assets/img/art-advisor.svg" alt="Tư vấn viên" style="border-radius:22px;box-shadow:var(--shadow-lg);max-width:420px;margin:0 auto"></div>
      <div>
        <span class="eyebrow">Cách chúng tôi làm việc</span>
        <h2>Bốn điều chúng tôi cam kết với mọi khách hàng</h2>
        <p class="lead">Đây không phải khẩu hiệu. Nếu chúng tôi làm sai bất kỳ điều nào dưới đây, bạn hoàn toàn có thể nhắc lại.</p>
        <div class="feat"><span class="feat-ico">{I['chart']}</span><div><h4>Tính được, không chỉ nói được</h4><p>Mọi đề xuất đều đi kèm bảng tính cụ thể cho hoàn cảnh của bạn &mdash; kể cả phép so sánh sòng phẳng giữa bảo hiểm, tiết kiệm và các kênh khác.</p></div></div>
        <div class="feat"><span class="feat-ico">{I['warn']}</span><div><h4>Nói nhược điểm trước khi bạn hỏi</h4><p>Giá trị hoàn lại những năm đầu, điều khoản loại trừ, rủi ro của dòng liên kết đầu tư &mdash; chúng tôi nói hết ngay buổi đầu.</p></div></div>
        <div class="feat"><span class="feat-ico">{I['doc']}</span><div><h4>Kê khai sức khoẻ đầy đủ, không đi tắt</h4><p>Phần lớn vụ từ chối bồi thường đến từ kê khai thiếu. Chúng tôi khai đủ, giữ bản sao, và không bao giờ khuyên bạn bỏ qua một chi tiết y tế nào.</p></div></div>
        <div class="feat"><span class="feat-ico">{I['users']}</span><div><h4>Có mặt khi bạn cần bồi thường</h4><p>Đây là lúc bảo hiểm thực sự có hoặc không có giá trị. Chúng tôi hỗ trợ trực tiếp thay vì để bạn tự gọi tổng đài.</p></div></div>
        <a class="btn btn-primary" href="ve-chung-toi.html">Tìm hiểu thêm {I['arrow']}</a>
      </div>
    </div>
  </div>
</section>

<section class="section bg-grey">
  <div class="wrap">
    <div class="center" style="max-width:50em;margin:0 auto 44px">
      <span class="eyebrow">Kiến thức</span>
      <h2>Đọc trước khi mua bất kỳ hợp đồng nào</h2>
    </div>
    <div class="grid g3">{post_cards('')}</div>
    <div class="center" style="margin-top:38px"><a class="btn btn-outline" href="kien-thuc/index.html">Xem tất cả bài viết {I['arrow']}</a></div>
  </div>
</section>

<section class="section">
  <div class="wrap" style="max-width:840px">
    <div class="center" style="margin-bottom:38px">
      <span class="eyebrow">Câu hỏi thường gặp</span>
      <h2>Những gì khách hàng hỏi nhiều nhất</h2>
    </div>
    {faq(HOME_FAQ)}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="cta-band">
      <h2>Bạn đang có câu hỏi cụ thể?</h2>
      <p>Nhắn cho chúng tôi tình huống của bạn &mdash; đang lo điều gì, đã có bảo hiểm gì, ngân sách khoảng bao nhiêu. Chúng tôi trả lời trong 15 phút giờ làm việc, và trả lời bằng con số.</p>
      <div class="btn-row">
        <a class="btn btn-white btn-lg" href="tel:{PHONE_TEL}">{I['phone']} Gọi hotline {PHONE_FMT}</a>
        <a class="btn btn-lg" style="background:rgba(255,255,255,.14);color:#fff;border-color:rgba(255,255,255,.4)" href="{ZALO}" target="_blank" rel="noopener">Nhắn Zalo</a>
      </div>
    </div>
  </div>
</section>
"""

# ================================================================ SẢN PHẨM
def prod_section(anchor, eyebrow, title, intro, cards, bg=""):
    return f"""
<section class="section {bg}" id="{anchor}">
  <div class="wrap">
    <div style="max-width:56em;margin-bottom:36px">
      <span class="eyebrow">{eyebrow}</span>
      <h2>{title}</h2>
      <p class="lead">{intro}</p>
    </div>
    <div class="grid g3">{cards}</div>
  </div>
</section>"""

sp_body = page_head("Sản phẩm", "Danh mục sản phẩm chúng tôi đang tư vấn",
    "Toàn bộ danh mục AIA Việt Nam, cùng gói bảo hiểm thai sản rời phân phối qua Fuse &times; Techcombank. Dưới đây là mô tả bản chất từng nhóm sản phẩm — quyền lợi và mức phí cụ thể sẽ được tính riêng theo độ tuổi, tình trạng sức khoẻ và ngân sách của bạn.")

sp_body += f"""
<section class="section-sm bg-grey">
  <div class="wrap">
    <div class="grid g4">
      <a class="card" href="#bao-ve" style="padding:20px"><div class="card-ico" style="width:42px;height:42px;margin-bottom:12px">{I['shield']}</div><h3 style="font-size:1rem;margin-bottom:0">Bảo vệ cuộc sống</h3></a>
      <a class="card" href="#tiet-kiem" style="padding:20px"><div class="card-ico" style="width:42px;height:42px;margin-bottom:12px">{I['piggy']}</div><h3 style="font-size:1rem;margin-bottom:0">Bảo vệ &amp; tiết kiệm</h3></a>
      <a class="card" href="#suc-khoe" style="padding:20px"><div class="card-ico" style="width:42px;height:42px;margin-bottom:12px">{I['hospital']}</div><h3 style="font-size:1rem;margin-bottom:0">Sức khoẻ &amp; nằm viện</h3></a>
      <a class="card" href="#tai-nan" style="padding:20px"><div class="card-ico" style="width:42px;height:42px;margin-bottom:12px">{I['bandage']}</div><h3 style="font-size:1rem;margin-bottom:0">Bảo hiểm tai nạn</h3></a>
    </div>
  </div>
</section>"""

sp_body += prod_section("bao-ve", "Nhóm 1", "Bảo hiểm bảo vệ cuộc sống",
  "Đây là nhóm sản phẩm trả lời đúng một câu hỏi: nếu thu nhập của người trụ cột dừng lại, gia đình sống bằng gì? Tiền bảo hiểm ở nhóm này gần như toàn bộ dùng để mua quyền lợi bảo vệ, nên số tiền bảo vệ nhận được trên mỗi đồng phí là cao nhất.",
  card_prod("AIA Việt Nam", "Bảo hiểm Liên kết chung AIA &ndash; Khoẻ Trọn Vẹn",
    "Sản phẩm bảo hiểm liên kết chung: kết hợp quyền lợi bảo vệ dài hạn với một tài khoản tích luỹ được ghi nhận lãi suất công bố định kỳ, có mức lãi suất tối thiểu cam kết theo điều khoản.",
    ["Linh hoạt điều chỉnh số tiền bảo hiểm theo giai đoạn cuộc đời",
     "Nền tảng để gắn thêm thẻ sức khoẻ, bệnh hiểm nghèo, miễn đóng phí",
     "Phù hợp gia đình muốn một hợp đồng lo được nhiều mục tiêu"], "lien-he.html")
+ card_prod("AIA Việt Nam", "Bảo hiểm AIA &ndash; Khoẻ An Nhiên",
    "Giải pháp bảo vệ với cấu trúc gọn, tập trung vào rủi ro sức khoẻ và tử vong thay vì yếu tố tích luỹ &mdash; dễ hiểu, dễ theo dõi.",
    ["Phù hợp người muốn thuần bảo vệ, không muốn dính tới đầu tư",
     "Cấu trúc phí minh bạch, ít yếu tố biến động",
     "Kết hợp tốt với sản phẩm bổ trợ sức khoẻ"], "lien-he.html")
+ card_prod("AIA Việt Nam", "Bảo hiểm Tử kỳ Gia hạn Hàng năm",
    "Bảo hiểm tử kỳ có thời hạn ngắn, được gia hạn theo từng năm. Phí thấp nhất trong các dòng bảo vệ tính trên cùng số tiền bảo hiểm.",
    ["Chi phí thấp, số tiền bảo vệ lớn",
     "Hợp với người có khoản vay cần được che phủ trong một số năm nhất định",
     "Không có giá trị hoàn lại &mdash; đây là điểm cần hiểu rõ trước khi tham gia"], "lien-he.html")
+ card_prod("Sản phẩm bổ trợ", "Bảo hiểm Miễn thu phí &ndash; Phiên bản 3.0",
    "Quyền lợi ít được nhắc tới nhưng rất quan trọng: nếu người đóng phí gặp rủi ro thuộc phạm vi bảo hiểm, hợp đồng vẫn được duy trì mà gia đình không phải đóng phí tiếp.",
    ["Bảo vệ chính kế hoạch bảo vệ của gia đình",
     "Đặc biệt quan trọng với hợp đồng mua cho con",
     "Chi phí nhỏ so với giá trị mang lại"], "lien-he.html"))

sp_body += prod_section("tiet-kiem", "Nhóm 2", "Bảo hiểm bảo vệ cuộc sống &amp; tiết kiệm",
  "Nhóm này gắn quyền lợi bảo vệ với một mục tiêu tài chính có thời hạn: học vấn cho con, quỹ hưu trí, một khoản dự phòng dài hạn. Cần nói rõ ngay từ đầu &mdash; đây không phải kênh đầu tư sinh lời cao, và giá trị hoàn lại trong 5&ndash;7 năm đầu thường thấp hơn tổng phí đã đóng.",
  card_prod("AIA Việt Nam", "Bảo hiểm Liên kết chung AIA &ndash; Vững Tương Lai",
    "Hướng tới các mục tiêu dài hạn có mốc thời gian rõ ràng &mdash; điển hình là quỹ học vấn cho con hoặc quỹ hưu trí của cha mẹ.",
    ["Tích luỹ theo mục tiêu có thời hạn cụ thể",
     "Quyền lợi bảo vệ được duy trì trong suốt quá trình tích luỹ",
     "Có thể gắn quyền lợi miễn đóng phí để kế hoạch không đứt gánh"], "lien-he.html")
+ card_prod("AIA Việt Nam", "Bảo hiểm Liên kết chung AIA &ndash; Khoẻ Bình An",
    "Cân bằng giữa bảo vệ sức khoẻ và tích luỹ, phù hợp với gia đình muốn một hợp đồng lo cả hai phần mà không phải quản lý nhiều hợp đồng riêng lẻ.",
    ["Một hợp đồng, hai mục tiêu",
     "Dễ mở rộng quyền lợi khi thu nhập tăng",
     "Cấu trúc phù hợp với gia đình trẻ mới lập kế hoạch"], "lien-he.html")
+ card_prod("AIA Việt Nam", "Giải pháp Bảo hiểm Hoạch định Vững vàng",
    "Giải pháp hoạch định tổng thể, kết hợp nhiều quyền lợi trong một cấu trúc thống nhất cho những gia đình có nhu cầu phức tạp hơn.",
    ["Thiết kế theo bức tranh tài chính tổng thể",
     "Phù hợp gia đình có nhiều người phụ thuộc",
     "Cần một buổi phân tích kỹ trước khi chốt cấu trúc"], "lien-he.html"),
  bg="bg-grey")

sp_body += prod_section("suc-khoe", "Nhóm 3", "Chăm sóc sức khoẻ &amp; nằm viện",
  "Theo kinh nghiệm của chúng tôi, đây là nhóm quyền lợi bị thiếu nhiều nhất trong các hợp đồng mà khách hàng mang đến nhờ chúng tôi đọc lại. Rất nhiều người đóng phí nhiều năm, tưởng mình đã có bảo hiểm sức khoẻ, nhưng thực tế hợp đồng chỉ có quyền lợi tử vong.",
  card_prod("Sản phẩm bổ trợ", "Chăm sóc Sức khoẻ",
    "Chi trả chi phí y tế thực tế: nội trú, phẫu thuật, và tuỳ hạng mức có thể mở rộng sang ngoại trú, nha khoa, thai sản.",
    ["Nhiều hạng mức quyền lợi để chọn theo ngân sách",
     "Có mạng lưới bảo lãnh viện phí &mdash; không phải ứng tiền trước",
     "Đây là quyền lợi được dùng tới nhiều nhất trong thực tế"], "lien-he.html", tag="Hay bị thiếu")
+ card_prod("Sản phẩm bổ trợ", "Bệnh hiểm nghèo",
    "Chi trả một khoản tiền mặt khi được chẩn đoán mắc bệnh hiểm nghèo thuộc danh sách bảo hiểm &mdash; độc lập với chi phí điều trị thực tế.",
    ["Tiền mặt để lo phần chi phí ngoài viện phí",
     "Bù đắp thu nhập mất đi trong thời gian điều trị",
     "Nhiều sản phẩm chi trả theo giai đoạn bệnh, không chỉ giai đoạn cuối"], "lien-he.html")
+ card_prod("Fuse &times; Techcombank", "Bảo hiểm thai sản rời",
    "Gói thai sản tham gia độc lập, không bắt buộc mua kèm hợp đồng nhân thọ dài hạn. Đây là lựa chọn phù hợp với gia đình trẻ đang chuẩn bị sinh con.",
    ["Thời gian chờ 270 ngày &mdash; ngắn hơn mức 365 ngày phổ biến",
     "Không phân biệt sinh thường và sinh mổ",
     "Bảo lãnh viện phí tại nhiều bệnh viện sản lớn"], "thai-san.html", tag="Nổi bật"))

sp_body += prod_section("tai-nan", "Nhóm 4", "Các sản phẩm bảo hiểm tai nạn",
  "Nhóm có mức phí thấp nhất và điều khoản rõ ràng nhất. Đây thường là bước đầu tiên hợp lý cho người chưa sẵn sàng cam kết một hợp đồng dài hạn, hoặc là phần bổ sung cho gói sức khoẻ đã có.",
  card_prod("AIA Việt Nam", "Bảo hiểm Tử vong và Thương tật do Tai nạn",
    "Chi trả khi xảy ra tử vong hoặc thương tật vĩnh viễn do tai nạn thuộc phạm vi bảo hiểm.",
    ["Phí thấp, số tiền bảo hiểm lớn",
     "Phù hợp người thường xuyên di chuyển bằng xe máy",
     "Điều khoản đơn giản, dễ đối chiếu khi cần bồi thường"], "lien-he.html")
+ card_prod("AIA Việt Nam", "Bảo hiểm Tử vong do Tai nạn",
    "Phiên bản gọn hơn, tập trung vào rủi ro tử vong do tai nạn.",
    ["Mức phí rất thấp",
     "Thường dùng làm quyền lợi bổ sung",
     "Hợp với người mới bắt đầu tìm hiểu"], "lien-he.html")
+ card_prod("AIA Việt Nam", "Gói giải pháp AIA &ndash; Trọn Bình An",
    "Gói giải pháp đóng sẵn, gộp nhiều quyền lợi tai nạn trong một cấu trúc thống nhất.",
    ["Không phải ghép nhiều sản phẩm rời",
     "Quyền lợi rõ ràng theo gói",
     "Ra quyết định nhanh"], "lien-he.html"),
  bg="bg-grey")

sp_body += f"""
<section class="section">
  <div class="wrap">
    <div style="max-width:56em;margin-bottom:32px">
      <span class="eyebrow">Nhóm 5</span>
      <h2>Sản phẩm phân phối qua kênh đối tác</h2>
      <p class="lead">AIA Việt Nam còn phân phối sản phẩm qua các ngân hàng và tổ chức tài chính đối tác. Cấu trúc quyền lợi và điều kiện tham gia của nhóm này có thể khác với kênh đại lý, nên cần đối chiếu riêng trước khi so sánh.</p>
    </div>
    <div class="logos" style="justify-content:flex-start">
      <span class="logo-chip">VPBank</span><span class="logo-chip">Techcombank</span>
      <span class="logo-chip">NCB</span><span class="logo-chip">FIDT</span><span class="logo-chip">Public Bank Vietnam</span>
    </div>
    <div class="callout info" style="margin-top:32px">
      <h4>{I['warn']} Một lưu ý thật lòng về việc mua bảo hiểm qua ngân hàng</h4>
      <p class="mb0">Sản phẩm qua kênh ngân hàng không xấu &mdash; nhưng người bán thường là nhân viên ngân hàng, và họ có thể luân chuyển vị trí. Điều đó có nghĩa: vài năm sau, khi bạn cần làm hồ sơ bồi thường, người đã tư vấn cho bạn có thể không còn ở đó. Nếu bạn đang có một hợp đồng mua qua ngân hàng và không rõ mình có quyền lợi gì, chúng tôi sẵn sàng đọc lại cùng bạn &mdash; miễn phí và không chào bán.</p>
    </div>
  </div>
</section>

<section class="section bg-grey">
  <div class="wrap" style="max-width:900px">
    <div class="center" style="margin-bottom:36px">
      <span class="eyebrow">Trước khi chọn</span>
      <h2>Ba câu nên hỏi bất kỳ tư vấn viên nào</h2>
    </div>
    {faq(SP_FAQ)}
  </div>
</section>
"""
sp_body += cta("", "Chưa biết nên bắt đầu từ sản phẩm nào?",
  "Đó là câu hỏi đúng. Câu trả lời phụ thuộc vào việc bạn đang lo điều gì nhất, ngân sách bao nhiêu, và đã có sẵn quyền lợi gì. Nhắn cho chúng tôi tình huống của bạn, chúng tôi sẽ nói thẳng nên bắt đầu từ đâu &mdash; kể cả khi câu trả lời là chưa cần mua gì thêm.")

# ================================================================ THAI SẢN
ts_body = page_head("Bảo hiểm thai sản", "Bảo hiểm thai sản rời &mdash; Fuse &times; Techcombank",
  "Gói thai sản tham gia độc lập, không bắt buộc mua kèm hợp đồng nhân thọ dài hạn. Dưới đây là toàn bộ những gì bạn cần biết, bao gồm cả những điểm bất lợi.")

ts_body += f"""
<section class="section">
  <div class="wrap">
    <div class="split">
      <div>
        <span class="eyebrow">Vấn đề</span>
        <h2>Vì sao đa số người muốn mua thai sản lại không mua được</h2>
        <p>Phần lớn quyền lợi thai sản trên thị trường Việt Nam nằm trong <b>thẻ sức khoẻ bổ trợ</b>. Mà thẻ bổ trợ thì phải gắn vào một hợp đồng bảo hiểm nhân thọ chính. Nghĩa là để có quyền lợi thai sản trị giá vài chục triệu, bạn được yêu cầu cam kết một hợp đồng 15&ndash;20 năm với mức phí khoảng 20 triệu mỗi năm.</p>
        <p>Với một cặp vợ chồng trẻ vừa mua nhà, vừa chuẩn bị sinh con, đó là một rào cản rất lớn &mdash; và nó khiến nhiều người bỏ luôn ý định chuẩn bị.</p>
        <p><b>Gói thai sản rời giải quyết đúng điểm nghẽn này:</b> tham gia độc lập, giải quyết đúng nhu cầu trước mắt, không buộc cam kết dài hạn. Khi nào gia đình sẵn sàng cho kế hoạch dài hơi hơn thì tính tiếp &mdash; và lúc đó bạn đã có đủ dữ liệu để quyết định.</p>
        <div class="btn-row" style="margin-top:26px">
          <a class="btn btn-primary" href="cong-cu.html#thoi-gian-cho">{I['clock']} Kiểm tra chúng tôi còn kịp không</a>
          <a class="btn btn-ghost" href="{ZALO}" target="_blank" rel="noopener">Hỏi trực tiếp qua Zalo</a>
        </div>
      </div>
      <div><img src="assets/img/art-thaisan.svg" alt="Bảo hiểm thai sản rời" style="border-radius:22px;box-shadow:var(--shadow-lg)"></div>
    </div>
  </div>
</section>

<section class="section bg-grey">
  <div class="wrap">
    <div style="max-width:54em;margin-bottom:36px">
      <span class="eyebrow">Điểm mạnh</span>
      <h2>Bốn điểm khiến gói này đáng cân nhắc</h2>
    </div>
    <div class="grid g2">
      <div class="card">{feat('clock','Thời gian chờ 270 ngày','Ngắn hơn mức 365 ngày phổ biến trên thị trường. Chênh lệch 95 ngày này nghe nhỏ, nhưng với người đang lên kế hoạch sinh con thì nó là ba tháng cửa sổ chuẩn bị &mdash; đủ để không phải hoãn kế hoạch có con lại một chu kỳ.')}</div>
      <div class="card">{feat('hospital','Không phân biệt sinh thường hay sinh mổ','Điểm này quan trọng hơn nhiều người nghĩ. Rất nhiều ca dự định sinh thường cuối cùng phải chuyển mổ vì lý do y khoa &mdash; và đó chính là lúc chi phí tăng gần gấp đôi. Một sản phẩm phân biệt hai hình thức sinh sẽ bỏ rơi bạn đúng vào lúc bạn cần nhất.')}</div>
      <div class="card">{feat('check','Bảo lãnh viện phí trực tiếp','Tại nhiều bệnh viện sản lớn. Nghĩa là bạn không phải xoay tiền mặt ứng trước rồi chờ hoàn &mdash; điều rất đáng giá khi mọi thứ diễn ra gấp trong đêm.')}</div>
      <div class="card">{feat('doc','Có chi trả cho khám thai','Chi phí khám thai định kỳ suốt 9 tháng cộng lại là một khoản không nhỏ mà hầu như không ai tính vào ngân sách ban đầu.')}</div>
    </div>
    <div class="callout warn" style="margin-top:34px">
      <h4>{I['warn']} Con số cụ thể cần được xác nhận theo bộ điều khoản mới nhất</h4>
      <p class="mb0">Mức phí, hạn mức quyền lợi, danh sách bệnh viện bảo lãnh và điều khoản loại trừ có thể thay đổi theo từng đợt phát hành sản phẩm. Trước khi bạn quyết định, chúng tôi sẽ gửi bản điều khoản chính thức đang có hiệu lực và đi qua từng mục cùng bạn &mdash; đặc biệt là phần loại trừ. Đừng bao giờ mua chỉ dựa trên một bài đăng trên mạng, kể cả bài này.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div style="max-width:54em;margin-bottom:32px">
      <span class="eyebrow">So sánh</span>
      <h2>Thai sản rời so với thẻ bổ trợ gắn hợp đồng nhân thọ</h2>
      <p class="lead">Không có lựa chọn nào tốt hơn tuyệt đối &mdash; chỉ có lựa chọn phù hợp hơn với tình huống của bạn lúc này.</p>
    </div>
    {tbl(["Tiêu chí","Thai sản rời (Fuse &times; Techcombank)","Thẻ bổ trợ gắn hợp đồng nhân thọ"], TS_COMPARE)}
    <div class="callout" style="margin-top:30px">
      <h4>Lời khuyên thẳng thắn của chúng tôi</h4>
      <p class="mb0">Nếu gia đình bạn <b>đã có</b> hợp đồng nhân thọ và đang đóng phí ổn định &mdash; hãy kiểm tra xem thẻ bổ trợ hiện có đã bao gồm quyền lợi thai sản chưa trước khi mua thêm. Rất có thể bạn đã có rồi mà không biết. Nếu bạn <b>chưa có gì</b> và đang chuẩn bị sinh trong 1&ndash;2 năm tới, gói rời là điểm khởi đầu hợp lý hơn: giải quyết đúng nhu cầu, chi phí thấp, và không khoá bạn vào một cam kết mà bạn chưa chắc chắn.</p>
    </div>
  </div>
</section>

<section class="section bg-soft">
  <div class="wrap">
    <div class="split" style="align-items:start">
      <div>
        <span class="eyebrow">Lộ trình</span>
        <h2>Mua vào lúc nào thì đúng?</h2>
        <p class="lead">Đây là phần khiến nhiều người tiếc nhất, vì nó hoàn toàn có thể tránh được nếu biết sớm hơn vài tháng.</p>
        <div class="btn-row" style="margin-top:20px">
          <a class="btn btn-primary" href="cong-cu.html#thoi-gian-cho">Tính hạn chót của chúng tôi {I['arrow']}</a>
        </div>
      </div>
      <div class="steps">
        <div class="step"><h4>12&ndash;15 tháng trước khi muốn sinh</h4><p>Thời điểm lý tưởng. Hồ sơ có thời gian thẩm định thoải mái, thời gian chờ chắc chắn kết thúc trước ngày dự sinh, và bạn có thời gian so sánh nhiều lựa chọn.</p></div>
        <div class="step"><h4>10&ndash;12 tháng trước</h4><p>Vẫn kịp với thời gian chờ 270 ngày, nhưng cần bắt đầu ngay chứ không nên trì hoãn thêm. Việc thẩm định sức khoẻ có thể mất thêm vài tuần.</p></div>
        <div class="step"><h4>Dưới 9 tháng trước</h4><p>Quyền lợi thai sản sẽ không kịp hiệu lực cho lần sinh này. Nhưng đừng bỏ qua hoàn toàn &mdash; gói sức khoẻ và nội trú vẫn có giá trị cho các biến chứng thai kỳ, và bạn nên chuẩn bị sẵn cho lần sinh sau.</p></div>
        <div class="step"><h4>Đã mang thai</h4><p>Hầu hết sản phẩm sẽ từ chối quyền lợi thai sản cho lần mang thai hiện tại. Nếu có ai đó nói với bạn điều ngược lại, hãy yêu cầu họ chỉ đúng điều khoản trong hợp đồng &mdash; đây là dấu hiệu cảnh báo rõ ràng.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap" style="max-width:900px">
    <div class="center" style="margin-bottom:36px">
      <span class="eyebrow">Hỏi &amp; đáp</span>
      <h2>Câu hỏi về bảo hiểm thai sản</h2>
    </div>
    {faq(TS_FAQ)}
  </div>
</section>
"""
ts_body += cta("", "Bạn dự định sinh vào khoảng nào?",
  "Nhắn cho chúng tôi mốc thời gian dự kiến &mdash; chúng tôi sẽ tính ngược ra hạn chót của riêng bạn và nói rõ bạn còn kịp hay đã trễ. Nếu đã trễ, chúng tôi cũng nói thẳng luôn thay vì để bạn mua một thứ không dùng được.")

# ================================================================ CÔNG CỤ
cc_body = page_head("Công cụ", "Công cụ tính toán",
  "Ba công cụ dùng ngay trên trang, không cần để lại thông tin. Kết quả là ước tính tham khảo dựa trên bảng giá công bố &mdash; con số chính xác cho trường hợp của bạn cần một buổi ngồi tính cụ thể.")

cc_body += f"""
<section class="section" id="chi-phi-sinh">
  <div class="wrap">
    <div class="split" style="align-items:start">
      <div>
        <span class="eyebrow">Công cụ 1</span>
        <h2>Chi phí sinh con &mdash; và phần bảo hiểm y tế không trả</h2>
        <p class="lead">Hầu hết mọi người biết chi phí sinh con &ldquo;khoảng vài chục triệu&rdquo;. Rất ít người biết phần mình phải tự trả là bao nhiêu sau khi trừ bảo hiểm y tế. Đó mới là con số cần chuẩn bị.</p>
        <div class="callout">
          <h4>Vì sao con số này quan trọng</h4>
          <p class="mb0">Bảo hiểm y tế chi trả theo mức giá dịch vụ được quy định, trong khi phần lớn gia đình chọn sinh dịch vụ để được chọn bác sĩ và phòng riêng. Khoảng chênh giữa hai mức giá này chính là phần phải chuẩn bị bằng tiền mặt hoặc bằng bảo hiểm.</p>
        </div>
        <p style="font-size:.88rem;color:var(--grey-400)">Nguồn tham chiếu: bảng giá dịch vụ công bố của các bệnh viện sản khoa năm 2026. Chi phí thực tế thay đổi theo gói dịch vụ, thời gian nằm viện và tình trạng y khoa cụ thể.</p>
      </div>
      <div class="calc">
        <div class="calc-head"><h3>{I['calc']} Máy tính chi phí sinh con</h3><p>Ước tính theo bảng giá dịch vụ 2026</p></div>
        <div class="calc-body">
          <form id="birthCalc">
            <div class="field">
              <label for="hospital">Bệnh viện dự định sinh</label>
              <select id="hospital" name="hospital">
                <option value="tudu">BV Từ Dũ (TP.HCM)</option>
                <option value="hungvuong">BV Hùng Vương (TP.HCM)</option>
                <option value="tinh">BV Sản Nhi tuyến tỉnh</option>
                <option value="phusan">BV Phụ sản Quốc tế / tư nhân</option>
                <option value="vinmec">Vinmec / BV quốc tế cao cấp</option>
              </select>
            </div>
            <div class="field">
              <label>Hình thức sinh</label>
              <div class="radio-row">
                <label class="radio-chip"><input type="radio" name="mode" value="thuong" checked><span>Sinh thường</span></label>
                <label class="radio-chip"><input type="radio" name="mode" value="mo"><span>Sinh mổ</span></label>
                <label class="radio-chip"><input type="radio" name="mode" value="unsure"><span>Chưa biết</span></label>
              </div>
            </div>
            <div class="field">
              <label>Có bảo hiểm y tế đúng tuyến không?</label>
              <div class="radio-row">
                <label class="radio-chip"><input type="radio" name="bhyt" value="yes" checked><span>Có</span></label>
                <label class="radio-chip"><input type="radio" name="bhyt" value="no"><span>Không / trái tuyến</span></label>
              </div>
            </div>
            <div class="field">
              <label>Dịch vụ thêm <span class="hint">(chọn nếu có dự định)</span></label>
              <label style="display:flex;gap:10px;align-items:center;font-size:.93rem;margin-bottom:8px"><input type="checkbox" name="extra" value="gayte" style="width:auto"> Gây tê ngoài màng cứng</label>
              <label style="display:flex;gap:10px;align-items:center;font-size:.93rem;margin-bottom:8px"><input type="checkbox" name="extra" value="bacsi" style="width:auto"> Chọn bác sĩ riêng</label>
              <label style="display:flex;gap:10px;align-items:center;font-size:.93rem"><input type="checkbox" name="extra" value="sanglọc" style="width:auto"> Sàng lọc sơ sinh mở rộng</label>
            </div>
          </form>
          <div class="calc-result" id="birthResult"></div>
          <div class="btn-row" style="margin-top:20px">
            <a class="btn btn-primary" href="{ZALO}" target="_blank" rel="noopener">Nhờ tính cho trường hợp của chúng tôi</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section bg-grey" id="thoi-gian-cho">
  <div class="wrap">
    <div class="split" style="align-items:start">
      <div class="calc">
        <div class="calc-head"><h3>{I['clock']} Đếm ngược thời gian chờ</h3><p>Tính ngược ra hạn chót hoàn tất hồ sơ</p></div>
        <div class="calc-body">
          <form id="waitCalc">
            <div class="field">
              <label for="due">Bạn dự định sinh vào khoảng nào?</label>
              <input type="month" id="due" name="due" value="2027-08">
            </div>
            <div class="field">
              <label>Thời gian chờ của sản phẩm</label>
              <div class="radio-row">
                <label class="radio-chip"><input type="radio" name="wait" value="270" checked><span>270 ngày</span></label>
                <label class="radio-chip"><input type="radio" name="wait" value="365"><span>365 ngày</span></label>
              </div>
            </div>
          </form>
          <div class="calc-result" id="waitResult"></div>
          <div class="btn-row" style="margin-top:20px">
            <a class="btn btn-primary" href="{ZALO}" target="_blank" rel="noopener">Nhắn Zalo hỏi cụ thể</a>
          </div>
        </div>
      </div>
      <div>
        <span class="eyebrow">Công cụ 2</span>
        <h2>Bạn còn bao nhiêu ngày để kịp?</h2>
        <p class="lead">Thời gian chờ là khoảng thời gian từ khi hợp đồng có hiệu lực đến khi quyền lợi thai sản bắt đầu được chi trả. Sinh trước mốc đó thì lần sinh ấy không được chi trả.</p>
        <p>Công cụ này lấy mốc dự sinh của bạn trừ ngược lại thời gian chờ, ra hạn chót phải hoàn tất hồ sơ. Con số thường làm nhiều người bất ngờ &mdash; theo hướng họ có ít thời gian hơn mình tưởng.</p>
        <div class="callout warn">
          <h4>{I['warn']} Nhớ trừ thêm thời gian thẩm định</h4>
          <p class="mb0">Hạn chót công cụ đưa ra là ngày hợp đồng cần <b>có hiệu lực</b>, chứ không phải ngày nộp hồ sơ. Quá trình thẩm định sức khoẻ có thể mất thêm 1&ndash;4 tuần, lâu hơn nếu cần bổ sung giấy tờ y tế. Nên cộng thêm một tháng đệm cho an toàn.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="ngan-sach">
  <div class="wrap">
    <div class="split" style="align-items:start">
      <div>
        <span class="eyebrow">Công cụ 3</span>
        <h2>Gia đình bạn cần được bảo vệ bao nhiêu?</h2>
        <p class="lead">Câu hỏi không phải &ldquo;nên mua gói nào&rdquo; mà là &ldquo;nếu thu nhập của chúng tôi dừng lại, gia đình cần bao nhiêu để đi tiếp&rdquo;. Trả lời được câu đó rồi mới chọn sản phẩm.</p>
        <p>Công cụ dùng nguyên tắc chung của ngành: số tiền bảo vệ đủ để thay thế thu nhập trong khoảng thời gian người phụ thuộc còn cần, cộng với các khoản nợ cần được xoá. Ngân sách phí hợp lý thường nằm trong khoảng 5&ndash;10% thu nhập.</p>
        <div class="callout info">
          <h4>Đây là ước tính, không phải kết luận</h4>
          <p class="mb0">Công thức chung không tính tới tài sản bạn đang có, bảo hiểm công ty đang cấp, thu nhập của người bạn đời, hay kế hoạch riêng của gia đình. Con số thật thường thấp hơn kết quả này &mdash; và chúng tôi sẽ chỉ ra vì sao trong buổi tư vấn.</p>
        </div>
      </div>
      <div class="calc">
        <div class="calc-head"><h3>{I['chart']} Máy tính ngân sách bảo vệ</h3><p>Ước tính theo nguyên tắc thay thế thu nhập</p></div>
        <div class="calc-body">
          <form id="needCalc">
            <div class="field"><label for="income">Thu nhập hằng tháng của bạn <span class="hint">(triệu đồng)</span></label>
              <input type="number" id="income" name="income" value="25" min="0" step="1"></div>
            <div class="field"><label for="debt">Tổng khoản vay còn lại <span class="hint">(triệu đồng &mdash; nhà, xe, vay khác)</span></label>
              <input type="number" id="debt" name="debt" value="500" min="0" step="10"></div>
            <div class="field"><label for="deps">Số người phụ thuộc <span class="hint">(con nhỏ, cha mẹ)</span></label>
              <select id="deps" name="deps"><option value="0">Chưa có</option><option value="1" selected>1 người</option><option value="2">2 người</option><option value="3">3 người</option><option value="4">4 người trở lên</option></select></div>
          </form>
          <div class="calc-result" id="needResult"></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section bg-soft" id="doc-hop-dong">
  <div class="wrap">
    <div class="split" style="align-items:start">
      <div>
        <span class="eyebrow">Dịch vụ miễn phí</span>
        <h2>Đọc lại hợp đồng bảo hiểm bạn đang có</h2>
        <p class="lead">Rất nhiều người đóng phí đều đặn nhiều năm mà không biết chính xác mình đang được bảo vệ những gì. Người tư vấn ban đầu đã nghỉ việc, hợp đồng thì dày và toàn thuật ngữ.</p>
        <p>Chúng tôi dành 30 phút ngồi đọc cùng bạn và trả lời bốn câu hỏi: <b>bạn đang có quyền lợi gì · đang thiếu quyền lợi gì · phần kê khai có vấn đề nào không · và mức phí đang trả có tương xứng không.</b></p>
        <div class="callout">
          <h4>Cam kết trong buổi này</h4>
          <p class="mb0">Không chào bán bất kỳ sản phẩm nào. Nếu hợp đồng bạn đang có đã ổn, chúng tôi sẽ nói đúng như vậy và buổi làm việc kết thúc ở đó. Nếu có vấn đề, chúng tôi chỉ rõ vấn đề và cách xử lý &mdash; kể cả khi cách xử lý không liên quan gì tới việc mua thêm.</p>
        </div>
        <p style="font-size:.9rem;color:var(--grey-600)">Bạn chuẩn bị giúp chúng tôi: bản hợp đồng (bản giấy hoặc file), bảng minh hoạ quyền lợi nếu còn giữ, và danh sách các sản phẩm bổ trợ đang có.</p>
      </div>
      <div class="form-card">
        <h3>Đăng ký buổi đọc hợp đồng</h3>
        <p style="color:var(--grey-600);font-size:.94rem">Điền thông tin, chúng tôi sẽ liên hệ trong giờ hành chính để hẹn khung giờ phù hợp.</p>
        <form data-lead>
          <div class="form-row">
            <div class="field"><label for="n1">Tên bạn</label><input id="n1" name="ten" required placeholder="Nguyễn Thị A"></div>
            <div class="field"><label for="p1">Số điện thoại / Zalo</label><input id="p1" name="sdt" required placeholder="09xx xxx xxx"></div>
          </div>
          <div class="field"><label for="c1">Hợp đồng bạn đang có</label>
            <select id="c1" name="hopdong">
              <option>Bảo hiểm nhân thọ (mua qua đại lý)</option>
              <option>Bảo hiểm mua qua ngân hàng</option>
              <option>Bảo hiểm sức khoẻ / thẻ bổ trợ</option>
              <option>Có nhiều hợp đồng, không rõ cái nào</option>
              <option>Chưa có hợp đồng nào &mdash; muốn tìm hiểu trước</option>
            </select></div>
          <div class="field"><label for="m1">Điều bạn băn khoăn nhất <span class="hint">(không bắt buộc)</span></label>
            <textarea id="m1" name="ghichu" rows="3" placeholder="Ví dụ: chúng tôi đóng 3 năm rồi mà không biết có được chi trả nằm viện không..."></textarea></div>
          <label style="display:flex;gap:10px;align-items:flex-start;font-size:.86rem;color:var(--grey-600);margin-bottom:18px">
            <input type="checkbox" name="consent" required style="width:auto;margin-top:4px">
            <span>Chúng tôi đồng ý để {BRAND} liên hệ tư vấn qua số điện thoại / Zalo đã cung cấp.</span></label>
          <button class="btn btn-primary btn-lg" type="submit" style="width:100%">Đăng ký buổi đọc hợp đồng</button>
          <div class="form-ok"></div>
          <p class="form-note">Thông tin của bạn chỉ dùng để liên hệ tư vấn, không chia sẻ cho bên thứ ba. Muốn nhanh hơn, bạn nhắn thẳng Zalo {PHONE_FMT}.</p>
        </form>
      </div>
    </div>
  </div>
</section>
"""

# ================================================================ VỀ TÔI
SK_TBL = [
    ["Nằm viện điều trị nội trú 5&ndash;7 ngày", "8 &ndash; 25 triệu", "Một phần theo mức quy định, thường 30&ndash;60% nếu đúng tuyến", "Có &mdash; nhóm quyền lợi dùng nhiều nhất"],
    ["Phẫu thuật có kế hoạch", "25 &ndash; 90 triệu", "Một phần, tuỳ danh mục kỹ thuật", "Có &mdash; theo hạn mức phẫu thuật"],
    ["Điều trị bệnh hiểm nghèo, kéo dài nhiều tháng", "150 triệu trở lên", "Một phần chi phí điều trị, không bù thu nhập", "Có &mdash; chi trả tiền mặt một lần khi chẩn đoán"],
    ["Chi phí ngoài viện phí (đi lại, người chăm, thu nhập mất đi)", "Không đoán trước", "Không chi trả", "Có &mdash; đây là lý do cần quyền lợi tiền mặt"],
]

SK_FAQ = [
    ("Công ty tôi đã cấp bảo hiểm sức khoẻ rồi, có cần mua riêng không?",
     "Cần kiểm tra hai điều. Thứ nhất, hạn mức: gói công ty cấp thường có hạn mức nội trú thấp hơn nhiều so với chi phí thực tế của một ca phẫu thuật. Thứ hai, và quan trọng hơn: gói đó chấm dứt khi bạn nghỉ việc hoặc đổi công ty. Nếu trong thời gian đó sức khoẻ bạn đã thay đổi, việc tham gia một gói mới sẽ khó khăn hoặc bị loại trừ. Bạn gửi chúng tôi bảng quyền lợi công ty cấp, chúng tôi đọc giúp và nói rõ bạn đang có gì."),
    ("Bảo lãnh viện phí hoạt động thế nào?",
     "Tại các cơ sở y tế trong mạng lưới liên kết, bạn xuất trình thẻ bảo hiểm và giấy tờ tuỳ thân, bệnh viện làm việc trực tiếp với đơn vị bảo hiểm thay vì buộc bạn ứng tiền trước rồi chờ hoàn. Phần vượt hạn mức hoặc không thuộc phạm vi chi trả bạn vẫn thanh toán bình thường. Danh sách bệnh viện bảo lãnh khác nhau theo từng sản phẩm, nên đây là mục cần đối chiếu trước khi chọn."),
    ("Bệnh có sẵn trước khi tham gia thì sao?",
     "Thông thường bệnh đã tồn tại trước thời điểm tham gia sẽ bị loại trừ hoặc phải chờ một thời gian dài hơn, tuỳ kết quả thẩm định. Điều quan trọng là kê khai đầy đủ ngay từ đầu &mdash; kể cả khi bạn nghĩ chuyện đó không đáng kể. Giấu để hồ sơ dễ qua là cách chắc chắn nhất khiến bồi thường bị từ chối về sau."),
    ("Nên chọn hạn mức bao nhiêu là đủ?",
     "Nguyên tắc chúng tôi dùng: hạn mức nội trú nên đủ để chi trả một ca phẫu thuật tại nhóm bệnh viện bạn thực sự sẽ đến, không phải nhóm bệnh viện rẻ nhất. Chọn hạn mức quá thấp để tiết kiệm phí thường dẫn tới việc đến lúc cần thì vẫn phải tự bỏ ra phần lớn. Chúng tôi sẽ tính con số này cùng bạn thay vì đưa một mức mặc định."),
]

BV_TBL = [
    ["Thu nhập chính của gia đình", "Người trụ cột &mdash; chiếm phần lớn thu nhập hộ", "Số tiền bảo vệ nên đủ thay thế thu nhập trong số năm người phụ thuộc còn cần"],
    ["Khoản vay đang trả", "Vay mua nhà, mua xe, vay kinh doanh", "Cộng toàn bộ dư nợ còn lại vào số tiền bảo vệ &mdash; để gia đình không phải bán tài sản"],
    ["Con nhỏ đang đi học", "Chi phí học tập tới khi con tự lập", "Mỗi người con làm số năm bảo vệ dài thêm, đây là biến số quan trọng nhất"],
    ["Cha mẹ phụ thuộc", "Chi phí sinh hoạt và y tế cho cha mẹ", "Cộng thêm phần chi phí định kỳ đang chi ra hằng tháng"],
    ["Tài sản và tiết kiệm sẵn có", "Khoản gia đình có thể dùng ngay", "Trừ ra khỏi tổng nhu cầu &mdash; đây là lý do con số thật thường thấp hơn công thức chung"],
]

BV_FAQ = [
    ("Tôi còn trẻ và khoẻ, mua bây giờ có sớm quá không?",
     "Về mặt số học thì ngược lại. Phí bảo hiểm được tính theo độ tuổi và tình trạng sức khoẻ tại thời điểm tham gia, và mức phí đó được giữ theo cấu trúc sản phẩm. Tham gia khi còn trẻ và chưa có vấn đề sức khoẻ nghĩa là bạn khoá được mức phí thấp và tránh được nguy cơ bị loại trừ quyền lợi. Điều kiện duy nhất để &ldquo;mua sớm&rdquo; là sai: khi bạn chưa có ai phụ thuộc và chưa có khoản vay nào &mdash; lúc đó thứ bạn cần là bảo hiểm sức khoẻ, không phải bảo hiểm nhân thọ."),
    ("Thà bỏ tiền đó đi đầu tư có hơn không?",
     "Nếu xét thuần lợi nhuận kỳ vọng dài hạn thì đầu tư thường cho kết quả tốt hơn, và chúng tôi không tranh cãi điều đó. Nhưng hai thứ này giải quyết hai bài toán khác nhau. Đầu tư giúp tài sản lớn lên theo thời gian &mdash; với điều kiện bạn còn thời gian. Bảo hiểm xử lý đúng kịch bản bạn không còn thời gian: biến cố xảy ra ở năm thứ hai, khi danh mục đầu tư mới chỉ tích luỹ được một phần nhỏ. Cách nhìn hợp lý là bảo hiểm bảo vệ chính kế hoạch đầu tư của bạn, chứ không cạnh tranh với nó."),
    ("Bảo hiểm liên kết đầu tư có đáng tham gia không?",
     "Tuỳ mục tiêu, và cần hiểu đúng bản chất. Phần đầu tư trong sản phẩm liên kết chịu rủi ro thị trường và không được cam kết lợi nhuận &mdash; ai nói ngược lại là đang tư vấn sai quy định. Chúng tôi luôn trình bày kịch bản lãi suất ở mức thấp trước, không phải mức cao, để bạn đánh giá sản phẩm ở tình huống bất lợi. Nếu nhu cầu của bạn thuần là bảo vệ, các dòng bảo vệ đơn thuần thường cho số tiền bảo vệ cao hơn trên mỗi đồng phí."),
    ("Số tiền bảo hiểm bao nhiêu là hợp lý?",
     "Nguyên tắc chung: đủ thay thế thu nhập cho những năm người phụ thuộc còn cần, cộng toàn bộ khoản vay, trừ đi tài sản sẵn có. Về mức phí, khoảng 5&ndash;10% thu nhập là ngưỡng đa số gia đình duy trì được lâu dài. Đóng cao hơn khả năng là nguyên nhân hàng đầu khiến hợp đồng bị huỷ giữa chừng &mdash; và huỷ giữa chừng là kịch bản tệ nhất, vì bạn vừa mất phí vừa mất luôn quyền lợi bảo vệ."),
]

vt_body = page_head("Về chúng tôi", "Về " + BRAND,
  "Dịch vụ tư vấn bảo hiểm độc lập. Dưới đây là cách chúng tôi làm việc, cách chúng tôi kiếm thu nhập, và những việc chúng tôi không làm.")

vt_body += f"""
<section class="section">
  <div class="wrap">
    <div class="split">
      <div><img src="assets/img/art-advisor.svg" alt="Tư vấn bảo hiểm" style="border-radius:22px;box-shadow:var(--shadow-lg);max-width:420px"></div>
      <div>
        <span class="eyebrow">Chúng tôi là ai</span>
        <h2>Một dịch vụ tư vấn, không phải một quầy bán hàng</h2>
        <p>{DOMAIN} là dịch vụ tư vấn bảo hiểm hoạt động với tư cách đại lý được uỷ quyền của doanh nghiệp bảo hiểm. Chúng tôi không phải doanh nghiệp bảo hiểm và không phát hành hợp đồng &mdash; hợp đồng luôn do doanh nghiệp bảo hiểm phát hành và chịu trách nhiệm chi trả.</p>
        <p>Chúng tôi lập ra trang này vì một quan sát đơn giản: phần lớn người Việt không thiếu nhu cầu bảo hiểm và cũng không thiếu nhận thức &mdash; họ thiếu một chỗ để hiểu vấn đề bằng con số trước khi phải nói chuyện với người bán hàng.</p>
        <p>Nên toàn bộ công cụ tính trên trang này đều <b>miễn phí và không yêu cầu để lại thông tin</b>. Bạn có thể dùng, tự rút ra kết luận, và không bao giờ liên hệ với chúng tôi. Điều đó hoàn toàn ổn.</p>
      </div>
    </div>
  </div>
</section>

<section class="section bg-grey">
  <div class="wrap">
    <div style="max-width:54em;margin-bottom:36px">
      <span class="eyebrow">Minh bạch</span>
      <h2>Chúng tôi kiếm thu nhập bằng cách nào</h2>
      <p class="lead">Đây là câu ít ai nói ra, nhưng bạn có quyền biết &mdash; vì nó ảnh hưởng tới lời khuyên bạn đang nhận.</p>
    </div>
    <div class="grid g2">
      <div class="card">
        <div class="card-ico">{I['check']}</div>
        <h3>Khách hàng không trả phí cho chúng tôi</h3>
        <p>Tư vấn, tính toán, đọc lại hợp đồng cũ và hỗ trợ hồ sơ bồi thường đều miễn phí. Bạn không trả thêm đồng nào so với việc mua trực tiếp.</p>
      </div>
      <div class="card">
        <div class="card-ico">{I['warn']}</div>
        <h3>Chúng tôi nhận hoa hồng từ doanh nghiệp bảo hiểm</h3>
        <p>Theo cơ chế chung của ngành, hoa hồng tập trung nhiều vào những năm đầu hợp đồng. Cơ chế này tạo ra một xung đột lợi ích có thật: nó thưởng cho việc bán được hợp đồng mới hơn là giữ khách hàng lâu dài.</p>
      </div>
      <div class="card">
        <div class="card-ico">{I['users']}</div>
        <h3>Vì sao chúng tôi vẫn làm ngược lại</h3>
        <p>Vì phần lớn khách hàng mới của chúng tôi đến từ giới thiệu của khách hàng cũ. Một hợp đồng bán ẩu có thể được vài tháng hoa hồng, nhưng nó cắt đứt nguồn khách của nhiều năm sau.</p>
      </div>
      <div class="card">
        <div class="card-ico">{I['doc']}</div>
        <h3>Bạn có thể kiểm chứng điều này</h3>
        <p>Hãy hỏi chúng tôi &mdash; hoặc bất kỳ tư vấn viên nào &mdash; hai câu: &ldquo;Sản phẩm này có nhược điểm gì?&rdquo; và &ldquo;Nếu tôi không đóng nổi phí giữa chừng thì sao?&rdquo;. Câu trả lời cho bạn biết mình đang nói chuyện với ai.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div style="max-width:54em;margin-bottom:36px">
      <span class="eyebrow">Nguyên tắc</span>
      <h2>Bốn điều chúng tôi cam kết</h2>
    </div>
    <div class="grid g2">
      <div class="card">{feat('warn','Nói nhược điểm trước','Giá trị hoàn lại những năm đầu thấp hơn tổng phí đã đóng. Sản phẩm liên kết đầu tư có rủi ro thị trường. Có những trường hợp bảo hiểm không chi trả. Chúng tôi nói hết những điều này trong buổi đầu tiên, không đợi bạn hỏi.')}</div>
      <div class="card">{feat('doc','Kê khai đầy đủ, không đi tắt','Phần lớn vụ từ chối bồi thường bắt nguồn từ kê khai sức khoẻ thiếu. Chúng tôi khai đủ, giữ bản sao, và không bao giờ khuyên bạn bỏ qua một chi tiết y tế nào để hồ sơ dễ qua.')}</div>
      <div class="card">{feat('users','Có mặt khi bạn cần bồi thường','Đây là lúc bảo hiểm thực sự có hoặc không có giá trị. Chúng tôi hỗ trợ chuẩn bị và theo dõi hồ sơ thay vì để bạn tự gọi tổng đài.')}</div>
      <div class="card">{feat('clock','Phản hồi trong 15 phút','Trong giờ làm việc, qua Zalo hoặc hotline. Nếu đang bận, chúng tôi nhắn báo và hẹn giờ gọi lại cụ thể chứ không để tin nhắn của bạn treo cả ngày.')}</div>
    </div>
  </div>
</section>

<section class="section bg-grey">
  <div class="wrap" style="max-width:960px">
    <div class="center" style="margin-bottom:34px"><span class="eyebrow">Ranh giới</span><h2>Ba điều chúng tôi không làm</h2></div>
    <div class="grid g3">
      <div class="card"><h3 style="color:var(--red)">Không gửi bảng minh hoạ ở buổi đầu</h3><p>Bảng minh hoạ toàn con số phí, khiến người ta hoảng trước khi kịp hiểu mình cần gì. Buổi đầu chỉ có câu hỏi và một bảng tính nhu cầu.</p></div>
      <div class="card"><h3 style="color:var(--red)">Không tạo cấp bách giả</h3><p>Không có &ldquo;chỉ còn 3 suất&rdquo; hay &ldquo;ưu đãi hết hạn hôm nay&rdquo;. Bảo hiểm không có khuyến mãi thật. Thứ cấp bách duy nhất là những thứ có thật: thời gian chờ, tuổi tăng thì phí tăng, sức khoẻ thay đổi thì khó tham gia hơn.</p></div>
      <div class="card"><h3 style="color:var(--red)">Không nhắn thúc</h3><p>Không có tin nhắn &ldquo;bạn xem tin chưa ạ&rdquo;. Nếu bạn cần thời gian, chúng tôi chốt một mốc gọi lại và giữ đúng mốc đó.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap" style="max-width:860px">
    <div class="center" style="margin-bottom:32px"><span class="eyebrow">Tuân thủ</span><h2>Khung pháp lý chúng tôi hoạt động</h2></div>
    <div class="card">
      <p>Hoạt động tư vấn bảo hiểm tại Việt Nam chịu điều chỉnh của Luật Kinh doanh bảo hiểm 2022 và các văn bản hướng dẫn, trong đó có Thông tư 67/2023/TT-BTC. Một số nguyên tắc chúng tôi tuân thủ nghiêm ngặt:</p>
      <ul style="color:var(--grey-800);padding-left:1.2em">
        <li style="margin-bottom:8px">Không cam kết hay gợi ý về mức lợi nhuận chắc chắn đối với sản phẩm bảo hiểm liên kết đầu tư.</li>
        <li style="margin-bottom:8px">Không cung cấp thông tin sai lệch về quyền lợi, điều kiện bảo hiểm hoặc về doanh nghiệp bảo hiểm.</li>
        <li style="margin-bottom:8px">Không dùng tên, hình ảnh cơ quan nhà nước để gợi ý sự bảo trợ cho sản phẩm.</li>
        <li style="margin-bottom:8px">Mọi nội dung trên trang mang tính kiến thức tham khảo, không thay thế Quy tắc và Điều khoản sản phẩm do doanh nghiệp bảo hiểm phát hành.</li>
      </ul>
      <p class="mb0" style="font-size:.92rem;color:var(--grey-600)">Nếu bạn thấy bất kỳ nội dung nào trên trang này chưa chính xác hoặc gây hiểu nhầm, hãy báo cho chúng tôi qua hotline {PHONE_FMT} &mdash; chúng tôi sẽ sửa.</p>
    </div>
  </div>
</section>
"""
vt_body += cta("", "Bạn muốn nói chuyện thử 15 phút?",
  "Không cần chuẩn bị gì. Bạn kể tình huống của mình, chúng tôi hỏi vài câu và nói thẳng bạn đang thiếu gì &mdash; hoặc không thiếu gì cả.")

# ================================================================ SỨC KHOẺ
sk_body = page_head("Sức khoẻ", "Sức khoẻ &amp; viện phí cho gia đình",
  "Một lần nằm viện có thể xoá đi nhiều năm tiết kiệm. Đây là nhóm quyền lợi được dùng tới nhiều nhất trong thực tế &mdash; và cũng là nhóm bị thiếu nhiều nhất trong các hợp đồng chúng tôi đọc lại.")

sk_body += f"""
<section class="section">
  <div class="wrap">
    <div class="split">
      <div>
        <span class="eyebrow">Vấn đề</span>
        <h2>Khoảng trống giữa bảo hiểm y tế và viện phí thật</h2>
        <p>Bảo hiểm y tế chi trả theo mức giá và danh mục kỹ thuật được quy định. Trong khi đó, phần lớn gia đình khi có người nằm viện đều chọn dịch vụ tốt hơn mức cơ bản: phòng riêng, bác sĩ theo yêu cầu, thuốc ngoài danh mục, hoặc chuyển thẳng lên tuyến trên mà không kịp làm thủ tục chuyển tuyến.</p>
        <p>Khoảng chênh giữa hai mức đó chính là phần gia đình phải tự trả &mdash; và nó xuất hiện đúng vào lúc không ai muốn ngồi tính toán.</p>
        <div class="callout">
          <h4>Điều ít người để ý</h4>
          <p class="mb0">Chi phí điều trị chỉ là một nửa vấn đề. Nửa còn lại là <b>phần thu nhập mất đi</b> trong thời gian nghỉ việc để điều trị hoặc để chăm người bệnh, cộng với chi phí đi lại và người chăm nuôi. Bảo hiểm y tế không xử lý phần này. Đây là lý do quyền lợi chi trả tiền mặt tồn tại.</p>
        </div>
      </div>
      <div><img src="assets/img/art-thaisan.svg" alt="Sức khoẻ và viện phí" style="border-radius:22px;box-shadow:var(--shadow-lg)"></div>
    </div>
  </div>
</section>

<section class="section bg-grey">
  <div class="wrap">
    <div style="max-width:56em;margin-bottom:32px">
      <span class="eyebrow">Bốn kịch bản</span>
      <h2>Chuyện gì thực sự xảy ra khi có người nằm viện</h2>
      <p class="lead">Bảng dưới là khoảng chi phí tham khảo, thay đổi nhiều theo cơ sở y tế và tình trạng bệnh. Cột cuối cho biết loại quyền lợi nào xử lý được kịch bản đó.</p>
    </div>
    {tbl(["Kịch bản","Chi phí tham khảo","BHYT xử lý được phần nào","Bảo hiểm thương mại"], SK_TBL)}
    <p style="font-size:.86rem;color:var(--grey-400);margin-top:14px">Con số mang tính tham khảo từ nguồn công khai, không phải cam kết. Mức chi trả thực tế theo Quy tắc &amp; Điều khoản sản phẩm.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div style="max-width:54em;margin-bottom:36px">
      <span class="eyebrow">Giải pháp</span>
      <h2>Ba lớp quyền lợi, theo thứ tự ưu tiên</h2>
      <p class="lead">Chúng tôi luôn tư vấn theo thứ tự này, kể cả khi ngân sách chỉ đủ cho lớp đầu tiên.</p>
    </div>
    <div class="grid g3">
      <div class="card"><span class="card-tag">Ưu tiên 1</span>
        <div class="card-ico">{I['hospital']}</div>
        <h3>Nội trú &amp; phẫu thuật</h3>
        <p>Lớp nền. Chi trả chi phí y tế thực tế khi nằm viện và phẫu thuật, theo hạn mức lựa chọn. Có mạng lưới bảo lãnh viện phí nên không phải ứng tiền trước.</p>
        <p style="font-size:.88rem"><b>Nguyên tắc chọn hạn mức:</b> đủ chi trả một ca phẫu thuật tại nhóm bệnh viện bạn thực sự sẽ đến, không phải nhóm rẻ nhất.</p>
      </div>
      <div class="card"><span class="card-tag">Ưu tiên 2</span>
        <div class="card-ico">{I['heart']}</div>
        <h3>Bệnh hiểm nghèo</h3>
        <p>Chi trả một khoản <b>tiền mặt</b> khi được chẩn đoán bệnh thuộc danh sách bảo hiểm &mdash; độc lập với chi phí điều trị thực tế.</p>
        <p style="font-size:.88rem">Khoản này dùng để lo phần bảo hiểm y tế không bao giờ chi: thu nhập mất đi, chi phí đi lại, người chăm nuôi, và thời gian phục hồi.</p>
      </div>
      <div class="card"><span class="card-tag">Ưu tiên 3</span>
        <div class="card-ico">{I['doc']}</div>
        <h3>Ngoại trú &amp; khám chữa định kỳ</h3>
        <p>Chi trả khám bệnh, xét nghiệm, thuốc không cần nhập viện. Tần suất dùng cao nhưng giá trị mỗi lần nhỏ.</p>
        <p style="font-size:.88rem">Chúng tôi xếp lớp này cuối cùng vì nó làm phí tăng đáng kể trong khi rủi ro tài chính nó xử lý lại là rủi ro bạn tự lo được.</p>
      </div>
    </div>
    <div class="callout warn" style="margin-top:32px">
      <h4>{I['warn']} Sai lầm phổ biến nhất mà chúng tôi gặp</h4>
      <p class="mb0">Rất nhiều người mua hợp đồng bảo hiểm nhân thọ và tin rằng mình &ldquo;đã có bảo hiểm sức khoẻ&rdquo;. Thực tế hợp đồng đó có thể chỉ có quyền lợi tử vong, không có quyền lợi nội trú. Chỉ đến lúc nằm viện họ mới phát hiện ra. Nếu bạn không chắc chắn hợp đồng của mình có gì, <a href="cong-cu.html#doc-hop-dong" style="color:var(--red-darker);font-weight:600">gửi cho chúng tôi đọc lại miễn phí</a> &mdash; mất 30 phút và không có chào bán trong buổi đó.</p>
    </div>
  </div>
</section>

<section class="section bg-soft">
  <div class="wrap" style="max-width:900px">
    <div class="center" style="margin-bottom:34px"><span class="eyebrow">Hỏi &amp; đáp</span><h2>Câu hỏi về bảo hiểm sức khoẻ</h2></div>
    {faq(SK_FAQ)}
  </div>
</section>
"""
sk_body += cta("", "Muốn biết gia đình bạn đang thiếu quyền lợi nào?",
  "Gửi chúng tôi bảng quyền lợi hiện có &mdash; của công ty cấp hoặc của hợp đồng riêng. Chúng tôi đọc và chỉ ra khoảng trống cụ thể, miễn phí và không chào bán.")

# ================================================================ BẢO VỆ THU NHẬP
bv_body = page_head("Bảo vệ thu nhập", "Bảo vệ thu nhập &amp; tài chính gia đình",
  "Dành cho người trụ cột: có người phụ thuộc, có khoản vay, và thu nhập của gia đình phụ thuộc phần lớn vào khả năng lao động của bạn.")

bv_body += f"""
<section class="section">
  <div class="wrap">
    <div class="split">
      <div>
        <span class="eyebrow">Câu hỏi thật</span>
        <h2>Nếu thu nhập của bạn dừng lại sáu tháng, ai trả khoản vay và tiền học của con?</h2>
        <p class="lead">Đây mới là câu hỏi của bảo hiểm nhân thọ &mdash; không phải &ldquo;nếu tôi mất đi&rdquo;. Rủi ro phổ biến hơn nhiều so với tử vong là <b>mất khả năng tạo thu nhập trong một khoảng thời gian dài</b>: một ca phẫu thuật lớn, một đợt điều trị kéo dài, một tai nạn cần nhiều tháng phục hồi.</p>
        <p>Trong khoảng thời gian đó, chi phí gia đình không giảm đi. Tiền học vẫn đóng, khoản vay vẫn đến hạn, và thường còn phát sinh thêm chi phí y tế.</p>
        <div class="btn-row" style="margin-top:26px">
          <a class="btn btn-primary" href="cong-cu.html#ngan-sach">{I['chart']} Tính số tiền bảo vệ cần có</a>
          <a class="btn btn-ghost" href="tel:{PHONE_TEL}">Gọi hotline {PHONE_FMT}</a>
        </div>
      </div>
      <div><img src="assets/img/hero.svg" alt="Bảo vệ thu nhập gia đình" style="border-radius:22px;box-shadow:var(--shadow-lg)"></div>
    </div>
  </div>
</section>

<section class="section bg-grey">
  <div class="wrap">
    <div style="max-width:56em;margin-bottom:32px">
      <span class="eyebrow">Cách tính</span>
      <h2>Năm biến số quyết định con số của bạn</h2>
      <p class="lead">Không có mức bảo vệ chuẩn cho mọi người. Con số đúng được ghép từ năm thành phần dưới đây &mdash; và thành phần cuối cùng là lý do con số thật thường thấp hơn công thức chung mà bạn đọc trên mạng.</p>
    </div>
    {tbl(["Biến số","Nội dung","Cách đưa vào phép tính"], BV_TBL)}
    <div class="callout info" style="margin-top:30px">
      <h4>Công thức rút gọn chúng tôi dùng</h4>
      <p class="mb0"><b>Số tiền bảo vệ = (Thu nhập năm &times; Số năm người phụ thuộc còn cần) + Tổng dư nợ &minus; Tài sản có thể dùng ngay.</b><br>
      Về mức phí, khoảng 5&ndash;10% thu nhập là ngưỡng đa số gia đình duy trì được lâu dài. Đóng vượt khả năng là nguyên nhân hàng đầu khiến hợp đồng bị huỷ giữa chừng &mdash; và huỷ giữa chừng là kịch bản tệ nhất: mất phí đã đóng và mất luôn quyền lợi.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div style="max-width:54em;margin-bottom:36px">
      <span class="eyebrow">So sánh thẳng thắn</span>
      <h2>Ba cách xử lý cùng một rủi ro</h2>
      <p class="lead">Chúng tôi trình bày cả phần bất lợi của bảo hiểm, vì bạn sẽ tự phát hiện ra &mdash; và lúc đó thì đã muộn cho niềm tin.</p>
    </div>
    <div class="grid g3">
      <div class="card">
        <div class="card-ico">{I['piggy']}</div>
        <h3>Tự tiết kiệm</h3>
        <p><b>Ưu điểm:</b> toàn quyền sử dụng, không mất phí, không phụ thuộc điều khoản.</p>
        <p><b>Điểm yếu:</b> cần thời gian để tích luỹ đủ. Một biến cố ở năm thứ hai xoá sạch thành quả &mdash; và đó chính là kịch bản cần được bảo vệ.</p>
      </div>
      <div class="card">
        <div class="card-ico">{I['chart']}</div>
        <h3>Đầu tư</h3>
        <p><b>Ưu điểm:</b> lợi nhuận kỳ vọng dài hạn cao hơn, thanh khoản linh hoạt hơn.</p>
        <p><b>Điểm yếu:</b> cũng cần thời gian, và chịu rủi ro thị trường đúng lúc bạn cần rút. Đầu tư làm tài sản lớn lên; nó không tạo ra một khoản tiền lớn ngay lập tức khi biến cố xảy ra.</p>
      </div>
      <div class="card" style="border-color:var(--red-soft2)">
        <div class="card-ico">{I['shield']}</div>
        <h3>Bảo hiểm</h3>
        <p><b>Ưu điểm:</b> một khoản tiền lớn có mặt ngay khi biến cố xảy ra, kể cả ở năm đầu tiên. Đây là thứ hai cách trên không làm được.</p>
        <p><b>Điểm yếu:</b> giá trị hoàn lại 5&ndash;7 năm đầu thấp hơn tổng phí đã đóng. Nếu không có biến cố, phí đã đóng không được hoàn lại như tiết kiệm.</p>
      </div>
    </div>
    <div class="callout" style="margin-top:30px">
      <h4>Kết luận của chúng tôi</h4>
      <p class="mb0">Ba cách này không thay thế nhau. Bảo hiểm không cạnh tranh với tiết kiệm hay đầu tư &mdash; nó <b>bảo vệ chính khoản tiết kiệm và danh mục đầu tư của bạn</b> khỏi bị xoá sổ bởi một biến cố duy nhất. Nếu ai đó tư vấn bảo hiểm cho bạn như một kênh sinh lời, hãy hỏi họ về giá trị hoàn lại trong năm năm đầu.</p>
    </div>
  </div>
</section>

<section class="section bg-soft">
  <div class="wrap" style="max-width:900px">
    <div class="center" style="margin-bottom:34px"><span class="eyebrow">Hỏi &amp; đáp</span><h2>Câu hỏi thường gặp về bảo vệ thu nhập</h2></div>
    {faq(BV_FAQ)}
  </div>
</section>
"""
bv_body += cta("", "Muốn biết con số của riêng gia đình bạn?",
  "Dùng công cụ tính ngân sách bảo vệ trên trang, hoặc gọi hotline. Chúng tôi sẽ hỏi vài câu và tính cụ thể &mdash; kể cả khi kết luận là bạn chưa cần mua thêm gì.")

# ================================================================ LIÊN HỆ
lh_body = page_head("Liên hệ", "Liên hệ với chúng tôi",
  "Cách nhanh nhất là nhắn Zalo &mdash; chúng tôi trả lời trong khoảng 15 phút giờ hành chính. Hoặc để lại thông tin qua form, chúng tôi sẽ gọi lại.")

lh_body += f"""
<section class="section">
  <div class="wrap">
    <div class="split" style="align-items:start">
      <div>
        <span class="eyebrow">Kênh liên hệ</span>
        <h2>Chọn cách tiện nhất cho bạn</h2>
        <div class="grid" style="gap:16px;margin-top:26px">
          <a class="card" href="{ZALO}" target="_blank" rel="noopener" style="flex-direction:row;align-items:center;gap:18px;padding:22px">
            <span class="card-ico" style="margin:0;background:#E7F0FF;color:#0068FF">{I['zalo']}</span>
            <span><b style="display:block;font-size:1.05rem">Zalo &mdash; {PHONE_FMT}</b><span style="color:var(--grey-600);font-size:.92rem">Nhanh nhất. Phản hồi trong ~15 phút, 8:00&ndash;21:00.</span></span>
          </a>
          <a class="card" href="tel:{PHONE_TEL}" style="flex-direction:row;align-items:center;gap:18px;padding:22px">
            <span class="card-ico" style="margin:0">{I['phone']}</span>
            <span><b style="display:block;font-size:1.05rem">Gọi trực tiếp &mdash; {PHONE_FMT}</b><span style="color:var(--grey-600);font-size:.92rem">Nếu bạn cần trao đổi kỹ hoặc hồ sơ đang gấp.</span></span>
          </a>
          <a class="card" href="{FB}" target="_blank" rel="noopener" style="flex-direction:row;align-items:center;gap:18px;padding:22px">
            <span class="card-ico" style="margin:0;background:#E7F0FF;color:#0084FF">{I['fb']}</span>
            <span><b style="display:block;font-size:1.05rem">Facebook</b><span style="color:var(--grey-600);font-size:.92rem">facebook.com/lientran.baohiem &mdash; nơi chúng tôi đăng bài phân tích thường xuyên.</span></span>
          </a>
        </div>
        <div class="callout" style="margin-top:30px">
          <h4>Nhắn gì để chúng tôi trả lời nhanh nhất?</h4>
          <p class="mb0">Ba thông tin này giúp chúng tôi trả lời ngay thay vì phải hỏi lại: <b>(1)</b> bạn đang lo điều gì nhất, <b>(2)</b> dự định sinh con vào khoảng nào (nếu có), <b>(3)</b> hiện đang có bảo hiểm gì rồi. Không cần chi tiết &mdash; chỉ cần đại khái.</p>
        </div>
        <div style="margin-top:26px;color:var(--grey-600);font-size:.94rem">
          <p style="margin-bottom:6px">{I['pin']} <b>Khu vực làm việc:</b> TP. Hồ Chí Minh và lân cận. Tư vấn từ xa qua Zalo / video call cho các tỉnh khác.</p>
          <p style="margin-bottom:0">{I['clock']} <b>Giờ làm việc:</b> Thứ 2 &ndash; Thứ 7, 8:00 &ndash; 21:00. Chủ nhật chúng tôi nghỉ, tin nhắn sẽ được trả lời sáng thứ 2.</p>
        </div>
      </div>
      <div class="form-card">
        <h3>Gửi câu hỏi của bạn</h3>
        <p style="color:var(--grey-600);font-size:.94rem">Chúng tôi đọc tất cả và trả lời từng người &mdash; không phải tin nhắn tự động.</p>
        <form data-lead>
          <div class="form-row">
            <div class="field"><label for="n2">Tên bạn</label><input id="n2" name="ten" required placeholder="Nguyễn Thị A"></div>
            <div class="field"><label for="p2">Số điện thoại / Zalo</label><input id="p2" name="sdt" required placeholder="09xx xxx xxx"></div>
          </div>
          <div class="field"><label for="t2">Bạn đang quan tâm điều gì?</label>
            <select id="t2" name="quantam">
              <option>Bảo hiểm thai sản &mdash; đang lên kế hoạch sinh con</option>
              <option>Bảo hiểm sức khoẻ, viện phí, nội trú</option>
              <option>Bảo hiểm nhân thọ &mdash; bảo vệ thu nhập gia đình</option>
              <option>Đọc lại hợp đồng đang có</option>
              <option>Chưa rõ &mdash; muốn nghe tư vấn tổng quát</option>
            </select></div>
          <div class="field"><label for="d2">Dự định sinh con vào khoảng <span class="hint">(nếu có)</span></label>
            <input type="month" id="d2" name="dusinh"></div>
          <div class="field"><label for="m2">Câu hỏi của bạn <span class="hint">(không bắt buộc)</span></label>
            <textarea id="m2" name="ghichu" rows="4" placeholder="Ví dụ: vợ chồng chúng tôi định năm sau sinh, hiện chỉ có BHYT công ty, không biết cần chuẩn bị thêm gì..."></textarea></div>
          <label style="display:flex;gap:10px;align-items:flex-start;font-size:.86rem;color:var(--grey-600);margin-bottom:18px">
            <input type="checkbox" name="consent" required style="width:auto;margin-top:4px">
            <span>Chúng tôi đồng ý để {BRAND} liên hệ tư vấn qua số điện thoại / Zalo đã cung cấp.</span></label>
          <button class="btn btn-primary btn-lg" type="submit" style="width:100%">Gửi câu hỏi</button>
          <div class="form-ok"></div>
          <p class="form-note">Thông tin của bạn chỉ dùng để liên hệ tư vấn, không chia sẻ cho bên thứ ba.</p>
        </form>
      </div>
    </div>
  </div>
</section>
"""

# ================================================================ KIẾN THỨC (index)
kt_body = page_head("Kiến thức", "Kiến thức bảo hiểm", 
  "Những bài viết chúng tôi mong bạn đọc trước khi ký bất kỳ hợp đồng nào &mdash; kể cả hợp đồng của chúng tôi.", "../")

kt_body += f"""
<section class="section">
  <div class="wrap">
    <div class="grid g3">{post_cards('../', limit=9)}</div>
  </div>
</section>

<section class="section bg-grey">
  <div class="wrap" style="max-width:860px">
    <div class="center" style="margin-bottom:30px"><span class="eyebrow">Đang viết</span><h2>Chủ đề sắp có</h2></div>
    <div class="grid g2">
      <div class="card" style="padding:22px"><h3 style="font-size:1rem">Tính IRR thật của một hợp đồng 20 triệu/năm</h3><p style="margin:0;font-size:.9rem">So sánh sòng phẳng với gửi tiết kiệm, bằng bảng tính công khai.</p></div>
      <div class="card" style="padding:22px"><h3 style="font-size:1rem">Bảng minh hoạ quyền lợi: đọc dòng nào, bỏ dòng nào</h3><p style="margin:0;font-size:.9rem">Hướng dẫn đọc từng mục, kèm những chỗ dễ bị hiểu nhầm nhất.</p></div>
      <div class="card" style="padding:22px"><h3 style="font-size:1rem">Nếu giữa chừng không đóng nổi phí thì có những lựa chọn nào</h3><p style="margin:0;font-size:.9rem">Bốn phương án và hệ quả tài chính của từng phương án.</p></div>
      <div class="card" style="padding:22px"><h3 style="font-size:1rem">Điều khoản loại trừ: 5 dòng phải đọc trước khi ký</h3><p style="margin:0;font-size:.9rem">Phần ngắn nhất trong hợp đồng nhưng quyết định nhiều nhất.</p></div>
    </div>
  </div>
</section>
"""
kt_body += cta("../", "Có câu hỏi mà chưa có bài viết nào trả lời?",
  "Nhắn cho chúng tôi &mdash; nếu câu hỏi đủ nhiều người quan tâm, chúng tôi sẽ viết hẳn một bài. Còn không thì chúng tôi trả lời riêng cho bạn.")

# ================================================================ BÀI VIẾT
def article(p, toc, content, P="../"):
    tocs = "".join('<li><a href="#%s">%s</a></li>' % (a, b) for a, b in toc)
    return f"""
<section class="page-head">
  <div class="wrap">
    <div class="crumb"><a href="{P}index.html">Trang chủ</a> / <a href="{P}kien-thuc/index.html">Kiến thức</a> / {p['tag']}</div>
    <h1 style="max-width:20em">{p['title']}</h1>
    <p style="margin-top:14px;font-size:.94rem;opacity:.85">{p['date']} &nbsp;·&nbsp; {p['read']} &nbsp;·&nbsp; {BRAND}</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="article">
      <p class="lead" style="font-size:1.16rem;color:var(--grey-800)">{p['desc']}</p>
      <div class="toc"><b>Nội dung bài viết</b><ol>{tocs}</ol></div>
      {content}
      <div class="callout info" style="margin-top:44px">
        <h4>{I['doc']} Về số liệu trong bài</h4>
        <p class="mb0" style="font-size:.9rem">Các con số chi phí y tế và mức phí nêu trong bài là khoảng tham khảo tổng hợp từ bảng giá dịch vụ công bố và thông tin sản phẩm tại thời điểm viết. Chi phí thực tế thay đổi theo từng cơ sở y tế, từng gói dịch vụ và từng đợt phát hành sản phẩm. Quyền lợi, mức phí và điều khoản loại trừ áp dụng theo Quy tắc &amp; Điều khoản của hợp đồng do doanh nghiệp bảo hiểm phát hành. Cần con số cho đúng trường hợp của bạn, gọi hotline {PHONE_FMT} &mdash; miễn phí.</p>
      </div>
    </div>
  </div>
</section>
<section class="section bg-grey">
  <div class="wrap">
    <div class="center" style="margin-bottom:36px"><span class="eyebrow">Đọc tiếp</span><h2>Bài viết khác</h2></div>
    <div class="grid g2">{post_cards(P, limit=2, exclude=p['slug'])}</div>
  </div>
</section>
""" + cta(P, "Bạn muốn chúng tôi tính cho trường hợp cụ thể của mình?",
       "Nhắn cho chúng tôi mốc dự sinh, bệnh viện bạn định chọn và bảo hiểm bạn đang có. Chúng tôi gửi lại bảng tính riêng cho trường hợp của bạn trong ngày.")


ART1 = f"""
<h2 id="tong-quan">Con số ngắn gọn trước khi vào chi tiết</h2>
<p>Nếu bạn chỉ có một phút, đây là phần cần nhớ: một ca <b>sinh thường dịch vụ</b> tại bệnh viện sản công lớn ở TP.HCM rơi vào khoảng <b>15&ndash;25 triệu đồng</b>. Một ca <b>sinh mổ dịch vụ</b> vào khoảng <b>25&ndash;45 triệu đồng</b>. Khi đi đúng tuyến với bảo hiểm y tế, phần được chi trả tương ứng khoảng <b>3&ndash;5 triệu</b> và <b>6&ndash;10 triệu</b>.</p>
<p>Nghĩa là khoảng chênh mà gia đình phải tự trả nằm trong khoảng <b>12&ndash;20 triệu cho sinh thường</b> và <b>19&ndash;35 triệu cho sinh mổ</b>. Đó là con số nên có trong kế hoạch tài chính trước khi có bầu, chứ không phải sau.</p>
{tbl(["Hình thức","Bệnh viện công &mdash; dịch vụ","Có BHYT đúng tuyến","Phần tự trả (ước tính)"], ART1_TBL)}

<h2 id="boc-tach">Bóc tách từng khoản trong hoá đơn</h2>
<p>Con số tổng thường làm người ta bất ngờ vì họ chỉ hình dung &ldquo;tiền sinh&rdquo;. Thực tế hoá đơn gồm nhiều lớp:</p>
<ul>
  <li><b>Chi phí thủ thuật / phẫu thuật.</b> Phần lõi. Sinh mổ cao hơn sinh thường khoảng gấp đôi vì liên quan tới phòng mổ, ê-kíp và thuốc.</li>
  <li><b>Tiền phòng theo ngày.</b> Đây là khoản biến động mạnh nhất. Phòng thường và phòng dịch vụ một giường có thể chênh nhau nhiều lần. Sinh mổ nằm viện lâu hơn sinh thường 1&ndash;2 ngày, nên khoản này nhân lên.</li>
  <li><b>Gây tê ngoài màng cứng.</b> Khoảng 1,2&ndash;2 triệu. Phần lớn sản phụ sinh thường đều chọn, nên nên tính vào từ đầu.</li>
  <li><b>Phí chọn bác sĩ riêng.</b> Khoảng 2&ndash;5 triệu. Không bắt buộc nhưng rất nhiều gia đình chọn.</li>
  <li><b>Sàng lọc sơ sinh.</b> Từ khoảng 500 nghìn cho gói cơ bản đến 3 triệu cho gói mở rộng.</li>
  <li><b>Thuốc, vật tư, xét nghiệm phát sinh.</b> Khoản không đoán trước được.</li>
</ul>
<p>Ngoài ra, bệnh viện thường yêu cầu <b>đặt cọc 5&ndash;10 triệu</b> khi nhập viện và quyết toán lúc xuất viện. Nếu gia đình không có sẵn khoản tiền mặt này, đó là áp lực thật vào đúng thời điểm căng thẳng nhất.</p>

<h2 id="khoan-quen">Ba khoản hầu như không ai tính vào ngân sách</h2>
<p>Đây là phần chúng tôi thấy gây vỡ kế hoạch nhiều nhất, vì nó nằm ngoài kịch bản &ldquo;mọi thứ suôn sẻ&rdquo; mà ai cũng mặc định.</p>
<h3>1. Chi phí khám thai suốt 9 tháng</h3>
<p>Khám định kỳ, siêu âm, xét nghiệm sàng lọc trước sinh, tiêm phòng. Từng lần không nhiều, nhưng cộng dồn cả thai kỳ thì đây là một khoản đáng kể &mdash; và nó được chi ra rải rác nên ít ai cộng lại.</p>
<h3>2. Chuyển từ sinh thường sang sinh mổ</h3>
<p>Đây là kịch bản rất phổ biến: gia đình lên kế hoạch tài chính cho ca sinh thường, nhưng vì lý do y khoa phải chuyển mổ. Chi phí tăng gần gấp đôi, và quyết định được đưa ra trong vài giờ. Vì vậy khi lập ngân sách, nên lấy con số của <b>sinh mổ</b> làm mốc chứ không phải sinh thường &mdash; nếu cuối cùng sinh thường thì bạn dư tiền, còn ngược lại thì bạn thiếu.</p>
<h3>3. Bé phải nằm chăm sóc đặc biệt</h3>
<p>Sinh non hoặc bé cần hỗ trợ hô hấp sau sinh dẫn tới thời gian nằm phòng chăm sóc đặc biệt tính theo ngày, và đây là khoản có thể vượt xa toàn bộ chi phí ca sinh. Đây chính là rủi ro mà bảo hiểm được thiết kế để xử lý &mdash; không phải khoản 20 triệu dự đoán được, mà khoản không dự đoán được.</p>

<div class="callout warn">
<h4>Đây là điểm quan trọng nhất của cả bài viết</h4>
<p class="mb0">Một ca sinh bình thường 30 triệu là khoản gia đình có thể tự chuẩn bị bằng tiết kiệm. Bảo hiểm không tồn tại để lo khoản đó. Nó tồn tại để lo phần đuôi &mdash; những kịch bản hiếm nhưng đắt, xảy ra đúng lúc bạn không có khả năng xoay xở. Nếu ai đó bán bảo hiểm thai sản cho bạn bằng lập luận &ldquo;để được hoàn tiền sinh&rdquo;, họ đang bán sai bản chất sản phẩm.</p>
</div>

<h2 id="benh-vien">Chênh lệch giữa các nhóm bệnh viện</h2>
<p>Cùng một ca sinh, chi phí có thể chênh nhau 5&ndash;6 lần tuỳ nơi. Điều đáng nói là <b>chênh lệch này chủ yếu đến từ dịch vụ, không phải từ chất lượng chuyên môn sản khoa</b> &mdash; các bệnh viện sản công tuyến cuối tại TP.HCM có năng lực xử lý ca khó rất tốt.</p>
<ul>
  <li><b>Bệnh viện sản công (Từ Dũ, Hùng Vương):</b> chi phí thấp nhất, chuyên môn cao, nhưng đông và điều kiện phòng ốc hạn chế hơn.</li>
  <li><b>Bệnh viện tư / phụ sản quốc tế:</b> gấp khoảng 2&ndash;3 lần bệnh viện công dịch vụ, đổi lại là trải nghiệm và sự riêng tư.</li>
  <li><b>Bệnh viện quốc tế cao cấp:</b> gấp 4&ndash;6 lần. Ở nhóm này, bảo hiểm y tế gần như không đóng vai trò gì.</li>
</ul>
<p>Một điều thực tế: nhiều gia đình chọn bệnh viện <b>sau khi</b> đã có bầu, dựa trên cảm nhận khi đi khám. Nếu đến lúc đó mới tính chuyện bảo hiểm thì đã muộn &mdash; xem phần dưới.</p>

<h2 id="chuan-bi">Vậy nên chuẩn bị thế nào</h2>
<p>Chúng tôi gợi ý ba lớp, theo đúng thứ tự ưu tiên:</p>
<ol>
  <li><b>Lớp 1 &mdash; Bảo hiểm y tế đúng tuyến.</b> Rẻ nhất và nên có. Đừng bỏ qua chỉ vì mức chi trả không lớn.</li>
  <li><b>Lớp 2 &mdash; Tiền mặt dự phòng bằng chi phí một ca sinh mổ dịch vụ.</b> Lấy con số cao nhất trong kịch bản bạn chọn, đó là khoản bạn nên có sẵn.</li>
  <li><b>Lớp 3 &mdash; Bảo hiểm cho phần đuôi.</b> Quyền lợi thai sản và nội trú, để xử lý những kịch bản vượt quá khả năng tự lo. Lớp này có <b>ràng buộc thời gian</b>: thời gian chờ 270&ndash;365 ngày, nghĩa là phải chuẩn bị trước khi mang thai.</li>
</ol>
<p>Bạn có thể tự tính con số của mình bằng <a href="{{P}}cong-cu.html#chi-phi-sinh">công cụ tính chi phí sinh con</a> trên trang này, và kiểm tra mình còn kịp mua bảo hiểm không bằng <a href="{{P}}cong-cu.html#thoi-gian-cho">công cụ đếm ngược thời gian chờ</a>.</p>
"""

ART2 = f"""
<h2 id="la-gi">Thời gian chờ là gì</h2>
<p>Thời gian chờ là khoảng thời gian tính từ ngày hợp đồng bảo hiểm có hiệu lực đến ngày quyền lợi bắt đầu được chi trả. Trong khoảng đó, bạn vẫn đóng phí bình thường nhưng nếu sự kiện bảo hiểm xảy ra thì <b>không được chi trả</b>.</p>
<p>Với quyền lợi thai sản, thời gian chờ phổ biến trên thị trường Việt Nam là <b>270 đến 365 ngày</b> &mdash; tức 9 đến 12 tháng. Một số sản phẩm áp dụng 280 ngày.</p>
<p>Vì sao lại có quy định này? Vì nếu không, người ta sẽ chỉ mua bảo hiểm khi đã biết mình mang thai. Khi đó rủi ro không còn là rủi ro nữa mà là một khoản chi chắc chắn, và sản phẩm không thể tồn tại. Thời gian chờ là cơ chế giữ cho bảo hiểm là bảo hiểm.</p>

<div class="callout">
<h4>Hệ quả trực tiếp mà ít người nhận ra</h4>
<p class="mb0">Thai kỳ kéo dài khoảng 280 ngày. Thời gian chờ thai sản là 270&ndash;365 ngày. Hai con số này gần bằng nhau &mdash; và đó chính là lý do <b>thời điểm que thử hiện hai vạch là thời điểm đã trễ</b>. Không phải trễ vài tuần, mà trễ gần đúng một chu kỳ mang thai.</p>
</div>

<h2 id="tinh-nguoc">Cách tự tính hạn chót của bạn</h2>
<p>Phép tính rất đơn giản, chỉ ba bước:</p>
<ol>
  <li>Xác định thời điểm bạn <b>muốn sinh</b> (không phải thời điểm muốn có bầu).</li>
  <li>Trừ ngược lại số ngày chờ của sản phẩm (270 hoặc 365).</li>
  <li>Trừ tiếp <b>khoảng một tháng</b> cho quá trình thẩm định hồ sơ.</li>
</ol>
<p>Ví dụ cụ thể: bạn muốn sinh vào tháng 8/2027. Với sản phẩm thời gian chờ 270 ngày, hợp đồng cần có hiệu lực trước khoảng tháng 11/2026. Cộng thêm một tháng đệm cho thẩm định, bạn nên bắt đầu làm hồ sơ từ <b>tháng 10/2026</b>. Mà muốn sinh tháng 8/2027 thì bạn cần có bầu khoảng tháng 11/2026 &mdash; tức <b>gần như cùng lúc</b>.</p>
<p>Đó là lý do chúng tôi làm hẳn một <a href="{{P}}cong-cu.html#thoi-gian-cho">công cụ đếm ngược</a> trên trang này: bạn nhập mốc dự sinh, công cụ trả về hạn chót và số ngày còn lại.</p>

<h2 id="270-vs-365">270 ngày và 365 ngày &mdash; chênh lệch này đáng giá bao nhiêu</h2>
<p>Nghe thì chỉ là 95 ngày. Nhưng với người đang lên kế hoạch sinh con, 95 ngày là ba tháng cửa sổ. Nó có thể là khác biệt giữa &ldquo;kịp cho lần sinh này&rdquo; và &ldquo;phải hoãn kế hoạch có con lại một năm&rdquo;.</p>
<p>Vì vậy khi so sánh các sản phẩm thai sản, thời gian chờ là một trong những tiêu chí đầu tiên nên hỏi &mdash; trước cả câu hỏi về hạn mức quyền lợi. Một gói có quyền lợi cao hơn 20% nhưng thời gian chờ dài hơn 3 tháng có thể hoàn toàn vô dụng với bạn.</p>
{tbl(["Câu hỏi nên hỏi","Vì sao quan trọng"], ART2_TBL)}

<h2 id="truong-hop">Nếu đã mang thai rồi thì sao</h2>
<p>Nói thẳng: với hầu hết sản phẩm, quyền lợi thai sản sẽ <b>không áp dụng</b> cho lần mang thai hiện tại. Nếu có tư vấn viên nói với bạn điều ngược lại, hãy yêu cầu họ chỉ đúng điều khoản trong bộ quy tắc sản phẩm. Không chỉ được thì đó là dấu hiệu cảnh báo rõ ràng.</p>
<p>Nhưng điều đó không có nghĩa là bạn không nên làm gì:</p>
<ul>
  <li><b>Quyền lợi nội trú và biến chứng thai kỳ</b> ở một số sản phẩm vẫn có thể áp dụng sau thời gian chờ ngắn hơn &mdash; cần kiểm tra cụ thể theo điều khoản.</li>
  <li><b>Bảo hiểm sức khoẻ cho bé sau sinh</b> nên được chuẩn bị từ trong thai kỳ, vì có mốc tuổi tối thiểu để tham gia.</li>
  <li><b>Chuẩn bị cho lần sinh sau.</b> Nếu gia đình dự định có con thứ hai, mua ngay bây giờ là đúng thời điểm &mdash; và lần này bạn đã có kinh nghiệm về chi phí thật.</li>
</ul>

<h2 id="sai-lam">Ba sai lầm phổ biến về thời gian chờ</h2>
<h3>Tưởng thời gian chờ tính từ ngày nộp hồ sơ</h3>
<p>Không. Nó tính từ ngày hợp đồng <b>có hiệu lực</b>, tức sau khi hồ sơ được thẩm định và chấp thuận, và phí đầu tiên đã được đóng. Khoảng cách giữa nộp hồ sơ và có hiệu lực có thể từ vài ngày đến vài tuần, lâu hơn nếu cần bổ sung giấy tờ y tế.</p>
<h3>Tưởng mọi quyền lợi có cùng một thời gian chờ</h3>
<p>Không. Trong cùng một hợp đồng, quyền lợi tai nạn thường có hiệu lực gần như ngay lập tức, quyền lợi bệnh thông thường có thời gian chờ ngắn (30&ndash;90 ngày), còn thai sản và bệnh đặc biệt có thời gian chờ dài nhất. Khi đọc hợp đồng, bạn cần xem bảng thời gian chờ theo <b>từng nhóm quyền lợi</b>.</p>
<h3>Tưởng gia hạn hợp đồng sẽ reset thời gian chờ</h3>
<p>Thường là không &mdash; nếu hợp đồng được duy trì liên tục. Nhưng nếu hợp đồng bị mất hiệu lực do không đóng phí rồi khôi phục lại, thời gian chờ có thể được tính lại. Đây là lý do việc <b>không để hợp đồng đứt giữa chừng</b> quan trọng hơn nhiều người nghĩ.</p>
"""

ART3 = f"""
<h2 id="thuc-te">Sự thật ít được nói ra</h2>
<p>Nỗi sợ lớn nhất của người mua bảo hiểm tại Việt Nam là: đóng phí nhiều năm, đến lúc cần thì bị từ chối. Nỗi sợ này có cơ sở &mdash; nhưng nguyên nhân thường không nằm ở chỗ mọi người nghĩ.</p>
<p>Phần lớn các trường hợp bị từ chối chi trả không đến từ việc doanh nghiệp bảo hiểm cố tình gây khó, mà đến từ <b>phần kê khai tình trạng sức khoẻ tại thời điểm tham gia</b>. Cụ thể hơn: khách hàng không kê khai đầy đủ tiền sử bệnh, và khi hồ sơ bồi thường được thẩm định lại, hồ sơ y tế cũ hiện ra.</p>
<p>Điều trớ trêu là đa số không cố tình giấu. Họ chỉ nghĩ những chuyện đó không đáng kể.</p>

<div class="callout warn">
<h4>Nguyên tắc kê khai đơn giản nhất</h4>
<p class="mb0">Nếu bạn từng bước chân vào một cơ sở y tế và có hồ sơ ghi lại &mdash; hãy khai. Kể cả khi đó là chuyện của nhiều năm trước, kể cả khi bác sĩ nói không sao, kể cả khi bạn đã khỏi hoàn toàn. Việc quyết định điều gì đáng kể là việc của bộ phận thẩm định, không phải của bạn và cũng không phải của tư vấn viên.</p>
</div>

<h2 id="hay-bo-sot">Những gì hay bị bỏ sót nhất</h2>
<ul>
  <li><b>Khám sức khoẻ định kỳ có chỉ số bất thường.</b> Men gan cao, mỡ máu, đường huyết ranh giới &mdash; nhiều người nghĩ &ldquo;bác sĩ bảo theo dõi thêm&rdquo; nghĩa là không có gì.</li>
  <li><b>Đã từng nội soi, siêu âm phát hiện bất thường nhỏ.</b> Polyp, nang, sỏi &mdash; kể cả khi không cần điều trị.</li>
  <li><b>Thuốc đang dùng dài hạn.</b> Kể cả thuốc không kê đơn dùng thường xuyên.</li>
  <li><b>Từng nhập viện, kể cả vì tai nạn nhỏ.</b></li>
  <li><b>Tiền sử bệnh trong gia đình trực hệ.</b> Một số sản phẩm hỏi mục này.</li>
  <li><b>Thói quen sinh hoạt ảnh hưởng rủi ro.</b> Hút thuốc, uống rượu thường xuyên, nghề nghiệp hoặc sở thích có rủi ro cao.</li>
</ul>

<h2 id="ai-chiu">Nếu tư vấn viên khai hộ thì ai chịu trách nhiệm</h2>
<p>Đây là phần bạn cần đọc kỹ nhất.</p>
<p>Trên hồ sơ, <b>người ký tên vào tờ kê khai là bên chịu trách nhiệm về tính trung thực của thông tin</b> &mdash; tức là bạn, không phải tư vấn viên. Nếu tư vấn viên nói &ldquo;bạn cứ để chúng tôi điền cho nhanh&rdquo; hoặc &ldquo;cái này không cần khai đâu&rdquo;, và vài năm sau hồ sơ bồi thường bị từ chối, người gánh hậu quả tài chính là gia đình bạn. Tư vấn viên đó có thể đã không còn làm nghề.</p>
<p>Vì vậy, ba việc bạn nên làm với bất kỳ hợp đồng nào:</p>
<ol>
  <li><b>Tự đọc và tự điền phần kê khai sức khoẻ.</b> Chậm hơn vài chục phút, nhưng đây là vài chục phút quan trọng nhất của cả hợp đồng.</li>
  <li><b>Giữ một bản sao đầy đủ</b> của hồ sơ đã nộp, bao gồm phần kê khai. Chụp lại bằng điện thoại cũng được.</li>
  <li><b>Không ký vào tờ trống.</b> Không bao giờ, với bất kỳ lý do nào.</li>
</ol>

<h2 id="da-ky">Nếu đã lỡ kê khai thiếu rồi thì sao</h2>
<p>Không phải hết cách, và càng phát hiện sớm thì càng dễ xử lý. Tuỳ thời điểm và tình huống, có thể có các hướng: bổ sung thông tin cho doanh nghiệp bảo hiểm để hồ sơ được thẩm định lại, chấp nhận điều khoản loại trừ riêng cho tình trạng đó, hoặc điều chỉnh hợp đồng.</p>
<p>Điều tệ nhất là biết mình kê khai thiếu và im lặng chờ đợi &mdash; vì sự việc sẽ lộ ra đúng vào lúc gia đình cần tiền nhất.</p>
<p>Nếu bạn đang ở trong tình huống này, đây chính là loại việc chúng tôi làm trong <a href="{{P}}cong-cu.html#doc-hop-dong">buổi đọc lại hợp đồng miễn phí</a>: rà soát phần kê khai, chỉ ra rủi ro nếu có, và đề xuất hướng xử lý. Không chào bán gì trong buổi đó.</p>

<h2 id="nhung-ly-do-khac">Những lý do từ chối khác cần biết</h2>
{tbl(["Lý do","Bản chất","Cách phòng"], ART3_TBL)}
<p>Điểm chung của tất cả: chúng đều có thể phòng được <b>tại thời điểm tham gia</b>, và gần như không thể sửa <b>tại thời điểm bồi thường</b>. Đó là lý do chúng tôi luôn dành nhiều thời gian cho buổi làm hồ sơ hơn là buổi chào sản phẩm.</p>
"""

# ================================================================ RENDER
TOC1 = [("tong-quan","Con số ngắn gọn"),("boc-tach","Bóc tách từng khoản trong hoá đơn"),
        ("khoan-quen","Ba khoản hầu như không ai tính"),("benh-vien","Chênh lệch giữa các nhóm bệnh viện"),
        ("chuan-bi","Vậy nên chuẩn bị thế nào")]
TOC2 = [("la-gi","Thời gian chờ là gì"),("tinh-nguoc","Cách tự tính hạn chót của bạn"),
        ("270-vs-365","270 ngày và 365 ngày"),("truong-hop","Nếu đã mang thai rồi thì sao"),
        ("sai-lam","Ba sai lầm phổ biến")]
TOC3 = [("thuc-te","Sự thật ít được nói ra"),("hay-bo-sot","Những gì hay bị bỏ sót nhất"),
        ("ai-chiu","Nếu tư vấn viên khai hộ thì ai chịu trách nhiệm"),
        ("da-ky","Nếu đã lỡ kê khai thiếu rồi thì sao"),("nhung-ly-do-khac","Những lý do từ chối khác")]

print("Dang dung site...")

page("index.html", f"{BRAND} — Tư vấn bảo hiểm minh bạch, quyết định bằng con số",
     "Dịch vụ tư vấn bảo hiểm độc lập: công cụ tính chi phí sinh con, đếm ngược thời gian chờ thai sản, tính ngân sách bảo vệ gia đình và đọc lại hợp đồng miễn phí.",
     home, active="", P="", canon="", body_attr=" data-gate-auto")

page("san-pham.html", f"Danh mục sản phẩm bảo hiểm | {BRAND}",
     "Danh mục sản phẩm AIA Việt Nam và gói bảo hiểm thai sản rời Fuse × Techcombank — mô tả bản chất từng nhóm, kèm cả ưu và nhược điểm.",
     sp_body, active="sp", P="", canon="san-pham.html")

page("thai-san.html", f"Bảo hiểm thai sản rời — thời gian chờ 270 ngày | {BRAND}",
     "Bảo hiểm thai sản tham gia độc lập, không cần hợp đồng nhân thọ chính. Thời gian chờ 270 ngày, không phân biệt sinh thường hay sinh mổ, bảo lãnh viện phí trực tiếp.",
     ts_body, active="sp", P="", canon="thai-san.html")

page("suc-khoe.html", f"Bảo hiểm sức khoẻ & viện phí cho gia đình | {BRAND}",
     "Khoảng trống giữa bảo hiểm y tế và viện phí thật, ba lớp quyền lợi nên ưu tiên, và cách chọn hạn mức nội trú cho đúng.",
     sk_body, active="sp", P="", canon="suc-khoe.html")

page("bao-ve-thu-nhap.html", f"Bảo vệ thu nhập gia đình — bài toán cho người trụ cột | {BRAND}",
     "Nếu thu nhập của bạn dừng lại sáu tháng, ai trả khoản vay và tiền học của con? Cách tính số tiền bảo vệ cần có và so sánh thẳng thắn giữa tiết kiệm, đầu tư và bảo hiểm.",
     bv_body, active="sp", P="", canon="bao-ve-thu-nhap.html")

page("cong-cu.html", f"Công cụ tính chi phí sinh con, thời gian chờ & ngân sách bảo vệ | {BRAND}",
     "Ba công cụ miễn phí, không cần để lại thông tin: tính chi phí sinh con và phần BHYT không trả, đếm ngược thời gian chờ bảo hiểm thai sản, tính ngân sách bảo vệ gia đình.",
     cc_body, active="cc", P="", canon="cong-cu.html")

page("ve-chung-toi.html", f"Về chúng tôi | {BRAND}",
     "Dịch vụ tư vấn bảo hiểm độc lập. Cách chúng tôi làm việc, cách chúng tôi kiếm thu nhập, và ba điều chúng tôi không làm.",
     vt_body, active="vt", P="", canon="ve-chung-toi.html")

page("lien-he.html", f"Liên hệ tư vấn | {BRAND}",
     f"Hotline tư vấn {PHONE_FMT}. Tư vấn miễn phí, không thu phí dịch vụ, không chào bán trong buổi đầu. Phản hồi trong khoảng 15 phút giờ làm việc.",
     lh_body, active="", P="", canon="lien-he.html")

page("kien-thuc/index.html", f"Kiến thức bảo hiểm | {BRAND}",
     "Bài viết về chi phí sinh con, thời gian chờ bảo hiểm thai sản và kê khai sức khoẻ — những gì nên đọc trước khi ký hợp đồng.",
     kt_body, active="kt", P="../", canon="kien-thuc/")

_arts = [(POSTS[0], TOC1, ART1), (POSTS[1], TOC2, ART2), (POSTS[2], TOC3, ART3)]
for _p, _toc, _body in _arts:
    page("kien-thuc/" + _p["slug"], _p["title"] + " | " + BRAND, _p["desc"],
         article(_p, _toc, _body.replace("{P}", "../")), active="kt", P="../",
         canon="kien-thuc/" + _p["slug"])

urls = ["", "san-pham.html", "thai-san.html", "suc-khoe.html", "bao-ve-thu-nhap.html",
        "cong-cu.html", "ve-chung-toi.html", "lien-he.html", "kien-thuc/"] + \
       ["kien-thuc/" + p["slug"] for p in POSTS]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for u in urls:
    sm += "  <url><loc>%s/%s</loc><changefreq>weekly</changefreq></url>\n" % (SITE, u)
sm += "</urlset>\n"
open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(sm)
open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(
    "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE)
open(os.path.join(ROOT, "CNAME"), "w", encoding="utf-8").write("tuvanbaohiemso.com\n")
print("  sitemap.xml, robots.txt, CNAME")
print("Xong.")
