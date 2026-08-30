/* ===== Lien Tran — Tư vấn Bảo hiểm | main.js ===== */
(function () {
  'use strict';

  /* ---------- Mega menu ---------- */
  document.querySelectorAll('.nav-item.has-mega').forEach(function (item) {
    var link = item.querySelector('.nav-link');
    var close;
    function open() { clearTimeout(close); document.querySelectorAll('.nav-item.open').forEach(function(o){if(o!==item)o.classList.remove('open')}); item.classList.add('open'); }
    function shut() { close = setTimeout(function () { item.classList.remove('open'); }, 180); }
    item.addEventListener('mouseenter', open);
    item.addEventListener('mouseleave', shut);
    link.addEventListener('click', function (e) { e.preventDefault(); item.classList.toggle('open'); });
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.nav-item')) document.querySelectorAll('.nav-item.open').forEach(function (o) { o.classList.remove('open'); });
  });

  /* ---------- Mobile nav ---------- */
  var burger = document.getElementById('burger');
  var mnav = document.getElementById('mobileNav');
  if (burger && mnav) {
    burger.addEventListener('click', function () {
      mnav.classList.toggle('open');
      document.body.style.overflow = mnav.classList.contains('open') ? 'hidden' : '';
    });
  }

  /* ---------- Accordion ---------- */
  document.querySelectorAll('.acc-q').forEach(function (q) {
    q.addEventListener('click', function () { q.parentElement.classList.toggle('open'); });
  });

  /* ---------- Product filter pills ---------- */
  document.querySelectorAll('[data-filter-group]').forEach(function (group) {
    var pills = group.querySelectorAll('.pill');
    var targetSel = group.getAttribute('data-filter-group');
    pills.forEach(function (pill) {
      pill.addEventListener('click', function () {
        pills.forEach(function (p) { p.classList.remove('active'); });
        pill.classList.add('active');
        var cat = pill.getAttribute('data-cat');
        document.querySelectorAll(targetSel + ' [data-cat]').forEach(function (card) {
          card.classList.toggle('hide', cat !== 'all' && card.getAttribute('data-cat') !== cat);
        });
      });
    });
  });

  /* ---------- Helpers ---------- */
  function vnd(n) { return new Intl.NumberFormat('vi-VN').format(Math.round(n)) + 'đ'; }
  function tr(n) { return (n / 1e6).toFixed(1).replace('.0', '') + ' triệu'; }

  /* ---------- Máy tính chi phí sinh con ---------- */
  // Khoảng chi phí tham khảo (đồng) — nguồn: bảng giá dịch vụ bệnh viện công bố 2026.
  var HOSPITALS = {
    tudu:      { name: 'BV Từ Dũ (TP.HCM)',              thuong: [15e6, 25e6], mo: [25e6, 45e6], bhyt_thuong: [3e6, 5e6],   bhyt_mo: [6e6, 10e6] },
    hungvuong: { name: 'BV Hùng Vương (TP.HCM)',         thuong: [13e6, 22e6], mo: [22e6, 40e6], bhyt_thuong: [3e6, 5e6],   bhyt_mo: [6e6, 10e6] },
    phusan:    { name: 'BV Phụ sản Quốc tế / tư nhân',   thuong: [35e6, 60e6], mo: [55e6, 95e6], bhyt_thuong: [4e6, 6e6],   bhyt_mo: [7e6, 11e6] },
    vinmec:    { name: 'Vinmec / BV quốc tế cao cấp',    thuong: [70e6, 110e6], mo: [95e6, 160e6], bhyt_thuong: [0, 0],     bhyt_mo: [0, 0] },
    tinh:      { name: 'BV Sản Nhi tuyến tỉnh',          thuong: [8e6, 15e6],  mo: [15e6, 28e6], bhyt_thuong: [2.5e6, 4e6], bhyt_mo: [5e6, 9e6] },
    phusanhn:  { name: 'BV Phụ sản Hà Nội',               thuong: [12e6, 22e6], mo: [22e6, 40e6], bhyt_thuong: [3e6, 5e6],   bhyt_mo: [6e6, 10e6] },
    phusantw:  { name: 'BV Phụ sản Trung ương (Hà Nội)',  thuong: [14e6, 25e6], mo: [24e6, 45e6], bhyt_thuong: [3e6, 5e6],   bhyt_mo: [6e6, 10e6] },
    bachmai:   { name: 'BV Bạch Mai — khoa Sản (Hà Nội)', thuong: [12e6, 22e6], mo: [22e6, 42e6], bhyt_thuong: [3e6, 5e6],   bhyt_mo: [6e6, 10e6] },
    thanhnhan: { name: 'BV Thanh Nhàn (Hà Nội)',          thuong: [9e6, 17e6],  mo: [17e6, 32e6], bhyt_thuong: [2.5e6, 4e6], bhyt_mo: [5e6, 9e6] },
    hongngoc:  { name: 'BV Hồng Ngọc / BV tư Hà Nội',     thuong: [35e6, 65e6], mo: [55e6, 95e6], bhyt_thuong: [4e6, 6e6],   bhyt_mo: [7e6, 11e6] },
    vinmechn:  { name: 'Vinmec Times City (Hà Nội)',      thuong: [70e6, 115e6], mo: [95e6, 165e6], bhyt_thuong: [0, 0],     bhyt_mo: [0, 0] }
  };
  var EXTRAS = { gayte: [1.2e6, 2e6], bacsi: [2e6, 5e6], sanglọc: [0.5e6, 3e6] };

  var birthForm = document.getElementById('birthCalc');
  if (birthForm) {
    var out = document.getElementById('birthResult');
    function calcBirth() {
      var h = HOSPITALS[birthForm.hospital.value];
      var mode = birthForm.mode.value; // thuong | mo | unsure
      var hasBhyt = birthForm.bhyt.value === 'yes';
      var lo, hi, bLo, bHi;
      if (mode === 'unsure') {
        lo = Math.round(h.thuong[0] * 0.6 + h.mo[0] * 0.4);
        hi = Math.round(h.thuong[1] * 0.6 + h.mo[1] * 0.4);
        bLo = Math.round(h.bhyt_thuong[0] * 0.6 + h.bhyt_mo[0] * 0.4);
        bHi = Math.round(h.bhyt_thuong[1] * 0.6 + h.bhyt_mo[1] * 0.4);
      } else {
        lo = h[mode][0]; hi = h[mode][1];
        bLo = h[mode === 'thuong' ? 'bhyt_thuong' : 'bhyt_mo'][0];
        bHi = h[mode === 'thuong' ? 'bhyt_thuong' : 'bhyt_mo'][1];
      }
      var exLo = 0, exHi = 0;
      birthForm.querySelectorAll('input[name="extra"]:checked').forEach(function (c) {
        var e = EXTRAS[c.value]; if (e) { exLo += e[0]; exHi += e[1]; }
      });
      var totLo = lo + exLo, totHi = hi + exHi;
      var covLo = hasBhyt ? bLo : 0, covHi = hasBhyt ? bHi : 0;
      var gapLo = Math.max(0, totLo - covHi), gapHi = Math.max(0, totHi - covLo);

      out.innerHTML =
        '<div class="res-row"><span>Bệnh viện</span><b>' + h.name + '</b></div>' +
        '<div class="res-row"><span>Tổng chi phí dự kiến</span><b>' + tr(totLo) + ' – ' + tr(totHi) + '</b></div>' +
        '<div class="res-row"><span>BHYT chi trả ước tính</span><b>' + (hasBhyt ? tr(covLo) + ' – ' + tr(covHi) : 'Không áp dụng') + '</b></div>' +
        '<div style="margin-top:18px;padding-top:16px;border-top:2px solid var(--red-soft2)">' +
        '<div style="font-size:.86rem;color:var(--grey-600);margin-bottom:4px;font-weight:600">PHẦN GIA ĐÌNH TỰ TRẢ</div>' +
        '<div class="res-big">' + tr(gapLo) + ' – ' + tr(gapHi) + '</div></div>' +
        '<p class="res-note">Đây là khoảng chi phí tham khảo dựa trên bảng giá dịch vụ công bố, chưa gồm phát sinh ngoài dự kiến ' +
        '(sinh non, nằm phòng chăm sóc đặc biệt cho bé, biến chứng thai kỳ) — những khoản này mới là phần khiến ngân sách vỡ nhiều nhất. ' +
        'Muốn chúng tôi tính riêng cho trường hợp của bạn, bấm nút bên dưới.</p>';
      out.classList.add('hot');
    }
    birthForm.addEventListener('input', calcBirth);
    birthForm.addEventListener('change', calcBirth);
    calcBirth();
  }

  /* ---------- Đếm ngược thời gian chờ thai sản ---------- */
  var waitForm = document.getElementById('waitCalc');
  if (waitForm) {
    var wOut = document.getElementById('waitResult');
    function calcWait() {
      var dueStr = waitForm.due.value;
      if (!dueStr) { wOut.innerHTML = '<p class="res-note" style="margin:0">Chọn thời điểm bạn dự định sinh để xem hạn chót cần hoàn tất hồ sơ (300 ngày trước ngày sinh).</p>'; return; }
      var wait = waitForm.wait ? parseInt(waitForm.wait.value, 10) : 270;
      if (!wait) wait = 270;
      var BUFFER = 30;                 // đệm trước khi thả bầu, để thẩm định hồ sơ
      var total = wait + BUFFER;       // 270 + 30 = 300 ngày
      var due = new Date(dueStr + '-15T00:00:00');
      var today = new Date(); today.setHours(0, 0, 0, 0);
      var deadline = new Date(due.getTime() - total * 86400000);
      var daysLeft = Math.round((deadline - today) / 86400000);
      var dl = deadline.toLocaleDateString('vi-VN', { day: '2-digit', month: '2-digit', year: 'numeric' });
      var pill, msg;
      var SAFE = 'Công thức: <b>300 ngày = 270 ngày chờ + 30 ngày đệm trước khi thả bầu</b>. Thời gian chờ 270 ngày gần bằng đúng một thai kỳ đủ tháng, nên nếu chốt hợp đồng đúng lúc bắt đầu thả thì chỉ cần bé sinh sớm vài ngày là quyền lợi thai sản chưa kịp có hiệu lực. Ba mươi ngày đệm đó là để thẩm định hồ sơ và phòng đúng tình huống sinh non &mdash; <b>cần chốt mua trước khi thả bầu</b>.';
      if (daysLeft > 60) {
        pill = '<span class="status-pill status-ok">✓ Bạn vẫn còn thời gian</span>';
        msg = 'Bạn còn <b>' + daysLeft + ' ngày</b> để hoàn tất hồ sơ. Đây là khoảng thời gian thoải mái — nên tận dụng để so sánh kỹ và thẩm định sức khoẻ không bị gấp.<br><br>' + SAFE;
      } else if (daysLeft > 0) {
        pill = '<span class="status-pill status-warn">⚠ Sắp tới hạn</span>';
        msg = 'Chỉ còn <b>' + daysLeft + ' ngày</b>. Hồ sơ cần thời gian thẩm định, nên thực tế bạn nên bắt đầu ngay tuần này.<br><br>' + SAFE;
      } else {
        pill = '<span class="status-pill status-bad">✕ Đã qua hạn cho lần sinh này</span>';
        msg = 'Hạn chót đã qua <b>' + Math.abs(daysLeft) + ' ngày</b>. Với mốc dự sinh này, quyền lợi thai sản sẽ không kịp hiệu lực. Nhưng bạn vẫn nên xem gói sức khoẻ và nội trú để bảo vệ phần biến chứng — và chuẩn bị sớm cho lần sinh sau.';
      }
      var d = Math.max(0, daysLeft);
      wOut.innerHTML = pill +
        '<div class="res-row"><span>Thời gian chờ áp dụng</span><b>' + wait + ' ngày</b></div>' +
        '<div class="res-row"><span>Đệm trước khi thả bầu</span><b>' + BUFFER + ' ngày</b></div>' +
        '<div class="res-row"><span>Tổng cần chuẩn bị trước ngày sinh</span><b>' + total + ' ngày</b></div>' +
        '<div class="res-row"><span>Hạn chót hoàn tất hồ sơ</span><b style="color:var(--red)">' + dl + '</b></div>' +
        '<div class="cd-grid">' +
        '<div class="cd-box"><b>' + Math.floor(d / 30) + '</b><span>tháng</span></div>' +
        '<div class="cd-box"><b>' + Math.floor((d % 30) / 7) + '</b><span>tuần</span></div>' +
        '<div class="cd-box"><b>' + d + '</b><span>tổng số ngày</span></div>' +
        '</div><p class="res-note">' + msg + '</p>';
      wOut.classList.add('hot');
    }
    waitForm.addEventListener('input', calcWait);
    waitForm.addEventListener('change', calcWait);
    calcWait();
  }

  /* ---------- Máy tính ngân sách bảo vệ ---------- */
  var needForm = document.getElementById('needCalc');
  if (needForm) {
    var nOut = document.getElementById('needResult');
    function calcNeed() {
      var income = parseFloat(needForm.income.value) * 1e6 || 0;
      var debt = parseFloat(needForm.debt.value) * 1e6 || 0;
      var deps = parseInt(needForm.deps.value, 10) || 0;
      var years = deps > 0 ? 10 + deps * 2 : 5;
      var hs = income * 12 * (years / 2);
      var cover = hs + debt;
      var budgetLo = income * 0.05, budgetHi = income * 0.10;
      var vnFull = function (n) { return Math.round(n).toLocaleString('vi-VN') + ' đồng'; };
      nOut.innerHTML =
        '<div class="res-row"><span>Số năm thu nhập cần thay thế (đề xuất)</span><b>' + years + ' năm</b></div>' +
        '<div class="res-row"><span>Phần thay thế thu nhập</span><b>' + tr(hs) + '</b></div>' +
        '<div class="res-row"><span>Khoản nợ cần xoá</span><b>' + tr(debt) + '</b></div>' +
        '<div style="margin-top:18px;padding-top:16px;border-top:2px solid var(--red-soft2)">' +
        '<div style="font-size:.86rem;color:var(--grey-600);margin-bottom:4px;font-weight:600">SỐ TIỀN BẢO VỆ GỢI Ý</div>' +
        '<div class="res-big">' + tr(cover) + '</div>' +
        '<div style="font-size:.95rem;color:var(--grey-600);margin-top:4px">= <b>' + vnFull(cover) + '</b></div></div>' +
        '<div class="res-row" style="margin-top:14px"><span>Ngân sách phí hợp lý (5–10% thu nhập)</span><b>' + vnd(budgetLo) + ' – ' + vnd(budgetHi) + '/tháng</b></div>' +
        '<p class="res-note">Đây là ước tính theo nguyên tắc chung, chưa trừ đi tài sản có thể dùng ngay, bảo hiểm công ty đang có và kế hoạch riêng của gia đình bạn — những khoản đó thường kéo con số thật xuống. Con số chính xác cần một buổi ngồi tính cụ thể.</p>';
      nOut.classList.add('hot');
    }
    needForm.addEventListener('input', calcNeed);
    calcNeed();
  }

  /* ---------- Forms → lưu vào Google Sheet + chuyển sang Zalo ---------- */
  var LEAD_ENDPOINT = window.TVBHS_LEAD_ENDPOINT || '';

  function sendLead(payload) {
    if (!LEAD_ENDPOINT) return;
    try {
      var body = JSON.stringify(payload);
      if (navigator.sendBeacon) {
        navigator.sendBeacon(LEAD_ENDPOINT, new Blob([body], { type: 'text/plain;charset=utf-8' }));
      } else {
        fetch(LEAD_ENDPOINT, {
          method: 'POST', mode: 'no-cors', keepalive: true,
          headers: { 'Content-Type': 'text/plain;charset=utf-8' },
          body: body
        });
      }
    } catch (err) {}
  }

  document.querySelectorAll('form[data-lead]').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = f.querySelector('.form-ok');
      var data = new FormData(f);
      var payload = {};
      data.forEach(function (v, k) { if (k !== 'consent') payload[k] = v; });
      payload.trang = location.pathname + location.search;
      try { payload.kenh = localStorage.getItem('tvbhs_track') || ''; } catch (er) { payload.kenh = ''; }
      payload.nguon = document.referrer || 'Truy cập trực tiếp';
      sendLead(payload);
      if (ok) {
        ok.classList.add('show');
        ok.innerHTML = '✓ Đã ghi nhận. Chúng tôi sẽ liên hệ lại trong giờ hành chính.<br>' +
          '<span style="font-weight:500;font-size:.9rem">Muốn nhanh hơn, bạn nhắn thẳng Zalo <b>0777 991 852</b> — chúng tôi trả lời trong 15 phút.</span>';
      }
      window.open('https://zalo.me/0777991852', '_blank');
      f.reset();
    });
  });

  /* ---------- Năm hiện tại ---------- */
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();

/* ===== Popup phân nhánh nhu cầu + cá nhân hoá ===== */
(function () {
  'use strict';
  var KEY = 'tvbhs_track';
  var LABELS = {
    thaisan:  'Chuẩn bị sinh con · Thai sản',
    suckhoe:  'Sức khoẻ & viện phí gia đình',
    nhantho:  'Bảo vệ thu nhập & tài chính dài hạn',
    hopdong:  'Đã có hợp đồng · Muốn kiểm tra lại'
  };

  function store(v) { try { v === null ? localStorage.removeItem(KEY) : localStorage.setItem(KEY, v); } catch (e) {} }
  function read() {
    try {
      var q = new URLSearchParams(location.search).get('q');
      if (q && LABELS[q]) { store(q); return q; }
      return localStorage.getItem(KEY);
    } catch (e) { return null; }
  }

  function apply(track) {
    var band = document.getElementById('trackBand');
    var name = document.getElementById('trackName');
    document.querySelectorAll('.for-you').forEach(function (el) {
      el.classList.toggle('show', el.getAttribute('data-track') === track);
    });
    if (band && name && LABELS[track]) { name.textContent = LABELS[track]; band.classList.add('show'); }
    else if (band) { band.classList.remove('show'); }
    // ẩn khối "chọn nhu cầu" trên hero nếu đã chọn
    var picker = document.getElementById('heroPicker');
    if (picker) picker.style.display = LABELS[track] ? 'none' : '';
  }

  var gate = document.getElementById('needGate');
  function openGate() { if (gate) { gate.classList.add('show'); document.body.style.overflow = 'hidden'; } }
  function closeGate() { if (gate) { gate.classList.remove('show'); document.body.style.overflow = ''; } }

  if (gate) {
    gate.querySelectorAll('[data-track-pick]').forEach(function (b) {
      b.addEventListener('click', function () {
        var t = b.getAttribute('data-track-pick');
        store(t); apply(t); closeGate();
        var go = b.getAttribute('data-go');
        if (go) { setTimeout(function () { location.href = go; }, 120); }
      });
    });
    var skip = gate.querySelector('.gate-skip');
    if (skip) skip.addEventListener('click', function () { store('all'); apply('all'); closeGate(); });
    gate.addEventListener('click', function (e) { if (e.target === gate) { store('all'); apply('all'); closeGate(); } });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && gate.classList.contains('show')) { store('all'); apply('all'); closeGate(); } });
  }

  var current = read();
  apply(current);

  // Tự mở popup ở trang chủ khi chưa từng chọn
  if (gate && !current && document.body.hasAttribute('data-gate-auto')) {
    setTimeout(openGate, 900);
  }

  // Nút đổi nhu cầu
  document.querySelectorAll('[data-open-gate]').forEach(function (b) {
    b.addEventListener('click', function (e) {
      e.preventDefault();
      if (gate) openGate();
      else location.href = b.getAttribute('data-open-gate') || 'index.html';
    });
  });
})();

/* ===== Đổ bóng header khi cuộn ===== */
(function () {
  var h = document.querySelector('.header');
  if (!h) return;
  function onScroll() { h.classList.toggle('scrolled', window.scrollY > 8); }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();
