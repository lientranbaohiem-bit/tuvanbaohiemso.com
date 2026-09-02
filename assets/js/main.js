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
  /* Khoang chi phi tham khao (dong).
     Nguyen tac: so lay tu cong bo cua benh vien khi co; benh vien nao khong
     cong bo thi ghi ro la uoc tinh. Ra soat 03/09/2026. */
  var HOSPITALS = {
    tudu:      { name: 'BV Từ Dũ (TP.HCM)', nguon: 'Từ Dũ công bố 16/09/2025 — mức có dịch vụ', chinhthuc: 1, mienphi_bacsi: 1,
                 thuong: [10e6, 15e6],  mo: [18e6, 20e6],  bhyt_thuong: [3e6, 5e6],   bhyt_mo: [5e6, 8e6] },
    hungvuong: { name: 'BV Hùng Vương (TP.HCM)', nguon: 'Hùng Vương — tạm ứng công bố 2024–2025, quyết toán theo thực tế', chinhthuc: 1, mienphi_bacsi: 1,
                 thuong: [10e6, 18e6],  mo: [12e6, 22e6],  bhyt_thuong: [3e6, 5e6],   bhyt_mo: [5e6, 8e6] },
    tamanh:    { name: 'BV Tâm Anh (TP.HCM / Hà Nội)', nguon: 'Tâm Anh công bố — gói trọn gói tiêu chuẩn', chinhthuc: 1, ngoai_goi: [5e6, 15e6],
                 thuong: [31.4e6, 43.1e6], mo: [36.9e6, 58.7e6], bhyt_thuong: [1e6, 3e6], bhyt_mo: [2e6, 4e6] },
    fv:        { name: 'BV FV (TP.HCM)', nguon: 'FV công bố, bản cập nhật 21/05/2026 — gói Bạc đến Kim Cương, phòng tiêu chuẩn. Gói Bạch Kim và các hạng phòng cao hơn lên tới 168 triệu', chinhthuc: 1, da_gom_gayte: 1,
                 thuong: [45e6, 75e6],  mo: [55e6, 85e6],  bhyt_thuong: [2e6, 8e6],   bhyt_mo: [2e6, 8e6] },
    cih:       { name: 'BV Quốc tế City (TP.HCM)', nguon: 'Quốc tế City công bố, cập nhật 27/02/2026 — gói sinh Như Ý và Cát Tường', chinhthuc: 1,
                 ngoai_goi: [4.95e6, 8.25e6],
                 ngoai_goi_note: 'Đã cộng sẵn <b>tiền phòng 3 ngày</b>, vì bệnh viện ghi rõ <b>giá gói sinh chưa bao gồm tiền phòng</b> (1,65 – 2,75 triệu mỗi ngày). Bệnh viện không công bố số ngày nằm viện, nên 3 ngày ở đây là giả định của bạn — hãy hỏi bệnh viện con số thật.',
                 thuong: [25.1e6, 31.7e6], mo: [36.18e6, 55.81e6], bhyt_thuong: [1e6, 3e6], bhyt_mo: [2e6, 4e6] },
    hanhphuc:  { name: 'BV Quốc tế Hạnh Phúc', nguon: 'Hạnh Phúc công bố, bảng giá cập nhật 12/08/2025 — ba gói An Nhiên, Cát Tường, Như Ý (đã gồm phòng đơn)', chinhthuc: 1,
                 thuong: [29.9e6, 59.9e6], mo: [39.9e6, 69.9e6], bhyt_thuong: [1e6, 3e6], bhyt_mo: [2e6, 4e6] },
    vinmec:    { name: 'Vinmec Times City / Central Park', nguon: 'Ước tính từ nguồn thứ ba — Vinmec KHÔNG công bố giá', chinhthuc: 0,
                 thuong: [37e6, 52e6],  mo: [52e6, 65e6],  bhyt_thuong: [1e6, 3e6],   bhyt_mo: [2e6, 4e6] },
    vinmectinh:{ name: 'Vinmec chi nhánh tỉnh', nguon: 'Ước tính từ nguồn thứ ba — Vinmec KHÔNG công bố giá', chinhthuc: 0,
                 thuong: [24e6, 33e6],  mo: [33.5e6, 41e6], bhyt_thuong: [1e6, 3e6],  bhyt_mo: [2e6, 4e6] },
    xuyena:    { name: 'BV Đa khoa Xuyên Á (Củ Chi, TP.HCM)', nguon: 'Xuyên Á công bố, bảng giá dịch vụ kỹ thuật cập nhật 15/05/2025 — cơ sở Củ Chi. Cột BHYT lấy đúng từ bảng giá của bệnh viện, không phải ước tính', chinhthuc: 1,
                 ngoai_goi: [0.96e6, 1.65e6],
                 ngoai_goi_note: 'Đã cộng sẵn <b>tiền giường khoa Sản 3 ngày</b>: từ 320.000đ (phòng 10 giường) đến 550.000đ (phòng 2 giường) mỗi ngày. Bệnh viện không công bố số ngày nằm viện, nên 3 ngày là giả định của bạn. Chọn phòng Tiêu chuẩn A (1.700.000đ/ngày) thì khoản này lên 5,1 triệu.',
                 thuong: [2.18e6, 3.33e6], mo: [4.36e6, 7.76e6],
                 bhyt_thuong: [0.7867e6, 1.5103e6], bhyt_mo: [2.6048e6, 3.3762e6] },
    phusanhn:  { name: 'BV Phụ sản Hà Nội', nguon: 'Phụ sản Hà Nội công bố 20/08/2026 — cận dưới là KHU THƯỜNG, cận trên là KHU DỊCH VỤ, chưa gồm phí chọn bác sĩ (5–9 triệu với ca thường, tới 13 triệu với ca phức tạp). Phần BHYT ở đây tính bằng 80–100% mức giá khung BHYT mà bệnh viện công bố, vì bệnh viện không công bố phần chi trả thực tế', chinhthuc: 1,
                 ngoai_goi: [2.1e6, 7.5e6],
                 ngoai_goi_note: 'Đã cộng sẵn <b>tiền phòng 3 ngày</b>: 700.000đ/ngày ở khu thường đến 2.500.000đ/ngày ở phòng 2 giường khu D và B4. Bệnh viện có cả phòng 1 giường khu B3 giá <b>5.000.000đ/ngày</b> — chọn hạng đó thì riêng tiền phòng 3 ngày là 15 triệu.',
                 thuong: [0.7867e6, 4.366e6],  mo: [2.6048e6, 7.672e6],
                 bhyt_thuong: [0.63e6, 0.787e6],   bhyt_mo: [2.08e6, 2.6e6] },
    phusantw:  { name: 'BV Phụ sản Trung ương (Hà Nội)', nguon: 'Ước tính theo mặt bằng bệnh viện công tuyến cuối', chinhthuc: 0,
                 thuong: [14e6, 25e6],  mo: [24e6, 45e6],  bhyt_thuong: [3e6, 5e6],   bhyt_mo: [6e6, 10e6] },
    bachmai:   { name: 'BV Bạch Mai — khoa Sản (Hà Nội)', nguon: 'Ước tính theo mặt bằng bệnh viện công tuyến cuối', chinhthuc: 0,
                 thuong: [12e6, 22e6],  mo: [22e6, 42e6],  bhyt_thuong: [3e6, 5e6],   bhyt_mo: [6e6, 10e6] },
    thanhnhan: { name: 'BV Thanh Nhàn (Hà Nội)', nguon: 'Ước tính theo mặt bằng bệnh viện tuyến thành phố', chinhthuc: 0,
                 thuong: [9e6, 17e6],   mo: [17e6, 32e6],  bhyt_thuong: [2.5e6, 4e6], bhyt_mo: [5e6, 9e6] },
    hongngoc:  { name: 'BV Hồng Ngọc / BV tư Hà Nội', nguon: 'Ước tính theo mặt bằng bệnh viện tư', chinhthuc: 0,
                 thuong: [35e6, 65e6],  mo: [55e6, 95e6],  bhyt_thuong: [1e6, 3e6],   bhyt_mo: [2e6, 4e6] },
    ansinh:    { name: 'BV An Sinh (TP.HCM)', nguon: 'An Sinh công bố — bảng giá gói sinh 2026, giá ưu đãi trọn gói, đã gồm phòng 2 giường (3 ngày với sinh thường, 4 ngày với sinh mổ). Khoảng sinh mổ ở đây là ĐƠN THAI; song thai cao hơn 2 triệu mỗi mức, tới 36 triệu ở lần mổ thứ 3', chinhthuc: 1,
                 gayte_ghi_chu: 'An Sinh bán <b>hai gói sinh thường riêng</b>: 17.600.000đ không giảm đau và 20.000.000đ có giảm đau. Khoảng giá ở trên đã bao gồm cả hai, nên khoản gây tê không được cộng thêm lần nữa. Chênh lệch giữa hai gói là <b>2.400.000đ</b>.',
                 thuong: [17.6e6, 20e6], mo: [28e6, 34e6], bhyt_thuong: [1e6, 3e6], bhyt_mo: [2e6, 4e6] },
    mekong:    { name: 'BV Phụ sản MêKông (TP.HCM)', nguon: 'MêKông công bố 03/06/2022 — đây là GIÁ THỦ THUẬT, chưa gồm tiền phòng. Bệnh viện chưa cập nhật bảng giá từ 2022', chinhthuc: 1,
                 ngoai_goi: [4.8e6, 9.6e6],
                 ngoai_goi_note: 'Đã cộng sẵn <b>tiền phòng 3 đêm</b>, vì bảng giá của bệnh viện tách riêng: phòng đôi từ 1,6 triệu, phòng đơn từ 2,5 triệu, VIP từ 3,2 triệu mỗi đêm (công bố 01/09/2022). Bệnh viện không công bố số đêm nằm viện, nên 3 đêm ở đây là giả định của bạn.',
                 gayte_gia: [2.4e6, 2.4e6],
                 gayte_gia_note: 'Gây tê ngoài màng cứng ở đây tính theo đúng mức bệnh viện công bố là <b>2.400.000đ</b> (bảng giá 03/06/2022), không dùng mức ước tính chung.',
                 thuong: [7.5e6, 8.5e6], mo: [10e6, 14.5e6], bhyt_thuong: [1e6, 3e6], bhyt_mo: [2e6, 4e6] },
    tinh:      { name: 'BV Sản Nhi tuyến tỉnh', nguon: 'Ước tính theo mặt bằng tuyến tỉnh', chinhthuc: 0,
                 thuong: [8e6, 15e6],   mo: [15e6, 28e6],  bhyt_thuong: [2.5e6, 4e6], bhyt_mo: [5e6, 9e6] }
  };
var EXTRAS = { gayte: [1.2e6, 1.9e6], bacsi: [2e6, 5e6], 'sanglọc': [0.5e6, 3e6] };

  var birthForm = document.getElementById('birthCalc');
  if (birthForm) {
    /* Tren trang tung benh vien: tu chon dung benh vien do */
    try {
      var box = birthForm.closest('.calc');
      var bvKey = box && box.getAttribute('data-bv');
      if (bvKey && HOSPITALS[bvKey]) birthForm.hospital.value = bvKey;
    } catch (e) {}
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
      var exLo = 0, exHi = 0, ghiChu = [];
      birthForm.querySelectorAll('input[name="extra"]:checked').forEach(function (c) {
        if (c.value === 'bacsi' && h.mienphi_bacsi) {
          ghiChu.push('Bệnh viện này công bố <b>không thu thêm phí</b> khi bạn chọn bác sĩ đỡ sinh, nên khoản đó không được cộng vào.');
          return;
        }
        if (c.value === 'gayte' && (h.da_gom_gayte || h.gayte_ghi_chu)) {
          ghiChu.push(h.gayte_ghi_chu || 'Bệnh viện này ghi rõ <b>gây tê ngoài màng cứng đã nằm trong giá gói</b>, nên khoản đó không được cộng thêm.');
          return;
        }
        if (c.value === 'gayte' && h.gayte_gia) {
          exLo += h.gayte_gia[0]; exHi += h.gayte_gia[1];
          if (h.gayte_gia_note) ghiChu.push(h.gayte_gia_note);
          return;
        }
        var e = EXTRAS[c.value]; if (e) { exLo += e[0]; exHi += e[1]; }
      });
      if (h.ngoai_goi) {
        exLo += h.ngoai_goi[0]; exHi += h.ngoai_goi[1];
        ghiChu.push(h.ngoai_goi_note || 'Đã cộng sẵn khoản <b>phát sinh ngoài gói</b>. Nghiên cứu bình duyệt năm 2024 đo được mỗi ca sinh trọn gói tại đây phát sinh thêm trung bình <b>10,2 triệu</b> ngoài giá gói.');
      }
      if (!h.chinhthuc) {
        ghiChu.push('⚠️ Bệnh viện này <b>không công bố bảng giá công khai</b>. Con số trên là ước tính từ nguồn thứ ba, cần gọi bệnh viện xác nhận.');
      }
      var totLo = lo + exLo, totHi = hi + exHi;
      var covLo = hasBhyt ? bLo : 0, covHi = hasBhyt ? bHi : 0;
      /* Ghep dung canh: kich ban re di voi phan BHYT tra it, kich ban dat di voi
         phan BHYT tra nhieu. Ghep cheo (totLo - covHi) tao ra khoang rong vo ly
         va hay cho ra can duoi bang 0. */
      var gapLo = Math.max(0, totLo - covLo), gapHi = Math.max(0, totHi - covHi);
      if (gapHi < gapLo) { var _t = gapLo; gapLo = gapHi; gapHi = _t; }

      out.innerHTML =
        '<div class="res-row"><span>Bệnh viện</span><b>' + h.name + '</b></div>' +
        '<div class="res-row"><span>Tổng chi phí dự kiến</span><b>' + tr(totLo) + ' – ' + tr(totHi) + '</b></div>' +
        '<div class="res-row"><span>BHYT chi trả ước tính</span><b>' + (hasBhyt ? tr(covLo) + ' – ' + tr(covHi) : 'Không áp dụng') + '</b></div>' +
        '<div style="margin-top:18px;padding-top:16px;border-top:2px solid var(--red-soft2)">' +
        '<div style="font-size:.86rem;color:var(--grey-600);margin-bottom:4px;font-weight:600">PHẦN GIA ĐÌNH TỰ TRẢ</div>' +
        '<div class="res-big">' + tr(gapLo) + ' – ' + tr(gapHi) + '</div></div>' +
        '<p class="res-note"><b>Nguồn số liệu:</b> ' + h.nguon + '.</p>' +
        (ghiChu.length ? '<p class="res-note">' + ghiChu.join('<br>') + '</p>' : '') +
        '<p class="res-note">Khoảng này chưa gồm phát sinh ngoài dự kiến — sinh non, bé nằm phòng chăm sóc đặc biệt, biến chứng thai kỳ. ' +
        'Không bệnh viện nào trong danh sách công bố giá phòng chăm sóc đặc biệt sơ sinh, nên đây là khoản không ai ước tính trước được, ' +
        'và cũng là khoản khiến ngân sách vỡ nhiều nhất. Muốn chúng tôi tính riêng cho trường hợp của bạn, bấm nút bên dưới.</p>';
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
    var daGui = false;
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = f.querySelector('.form-ok');
      /* Chan gui trung: mot form chi ghi nhan mot lead moi lan tai trang.
         Khong co doan nay thi bam Gui hai lan se tao hai dong CRM va hai su kien generate_lead. */
      if (daGui) {
        if (ok) {
          ok.classList.add('show');
          ok.innerHTML = '✓ Thông tin của bạn đã được ghi nhận rồi.<br>' +
            '<span style="font-weight:500;font-size:.9rem">Cần gấp thì nhắn Zalo <b>0777 991 852</b>, chúng tôi trả lời trong 15 phút.</span>';
        }
        return;
      }
      daGui = true;
      var data = new FormData(f);
      var payload = {};
      data.forEach(function (v, k) { if (k !== 'consent') payload[k] = v; });
      payload.trang = location.pathname + location.search;
      try { payload.kenh = localStorage.getItem('tvbhs_track') || ''; } catch (er) { payload.kenh = ''; }
      payload.nguon = document.referrer || 'Truy cập trực tiếp';
      try {
        var u = JSON.parse(localStorage.getItem('tvbhs_utm') || '{}');
        var bits = [];
        ['utm_source','utm_medium','utm_campaign','utm_content'].forEach(function (k) {
          if (u[k]) bits.push(k.replace('utm_', '') + '=' + u[k]);
        });
        if (u.fbclid) bits.push('fbclid');
        if (u.gclid) bits.push('gclid');
        if (bits.length) payload.chien_dich = bits.join(' | ');
      } catch (er) {}
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

  /* ---------- Hanh trinh: nho trang VA vi tri khach dang doc ---------- */
  (function () {
    var KEY = 'tvbhs_journey';   // trang nhu cau gan nhat + cho khach dang doc
    var RET = 'tvbhs_return';    // co hieu: lan tai trang sau day la "quay lai"
    var isTool = function (p) { return p.indexOf('/cong-cu/') === 0; };
    var here = location.pathname;

    function read(k) {
      try { return JSON.parse(sessionStorage.getItem(k) || 'null'); } catch (e) { return null; }
    }
    function write(k, v) {
      try { sessionStorage.setItem(k, JSON.stringify(v)); } catch (e) {}
    }
    function drop(k) { try { sessionStorage.removeItem(k); } catch (e) {} }

    // Moi lien ket dan sang trang cong cu, theo dung thu tu xuat hien trong trang.
    // Thu tu nay on dinh giua hai lan tai vi HTML khong doi.
    function toolLinks() {
      var out = [], all = document.querySelectorAll('a[href]');
      for (var k = 0; k < all.length; k++) {
        try {
          if (isTool(new URL(all[k].href, location.href).pathname)) out.push(all[k]);
        } catch (e) {}
      }
      return out;
    }

    function scrollY() {
      return window.pageYOffset || document.documentElement.scrollTop || 0;
    }

    /* ============ A. Trang nhu cau / kien thuc ============ */
    if (!isTool(here)) {
      var links = toolLinks();

      // A1. Quay lai tu trang cong cu: dua khach ve dung cho vua bam
      var ret = read(RET);
      if (ret && ret.p === here) {
        drop(RET);
        var target = (ret.i >= 0 && links[ret.i]) ? links[ret.i] : null;
        var restore = function () {
          if (target) target.scrollIntoView({ block: 'center' });
          else if (ret.y) window.scrollTo(0, ret.y);
        };
        restore();
        // anh tai xong co the lam xe dich bo cuc — chinh lai
        window.addEventListener('load', restore);
        setTimeout(restore, 300);
        if (target) {
          setTimeout(function () {
            target.classList.add('ns-returned');
            setTimeout(function () { target.classList.remove('ns-returned'); }, 2000);
          }, 350);
        }
      }

      // A2. Ghi lai trang nay lam diem quay ve
      var label = document.body.getAttribute('data-jn') || '';
      write(KEY, { p: here, n: label, y: 0, i: -1 });

      // A3. Bam sang cong cu thi ghi them vi tri dang doc
      for (var a = 0; a < links.length; a++) {
        (function (el, idx) {
          el.addEventListener('click', function () {
            write(KEY, { p: here, n: label, y: scrollY(), i: idx });
          });
        })(links[a], a);
      }
      return;
    }

    /* ============ B. Trang cong cu ============ */
    var back = read(KEY);
    if (!back || !back.p) {
      try {
        if (document.referrer) {
          var u = new URL(document.referrer);
          if (u.origin === location.origin && !isTool(u.pathname)) {
            back = { p: u.pathname, n: '', y: 0, i: -1 };
          }
        }
      } catch (e) {}
    }
    if (!back || !back.p) return;

    var btns = document.querySelectorAll('.js-back');
    for (var b = 0; b < btns.length; b++) {
      btns[b].setAttribute('href', back.p);
      var nm = btns[b].querySelector('.js-back-name');
      if (nm && back.n) nm.textContent = back.n;
      btns[b].hidden = false;
      btns[b].addEventListener('click', function () { write(RET, back); });
    }
  })();

})();

/* ============================================================
   Do luong: GA4 + Meta Pixel + su kien tuy chinh
   Tat ca deu an toan khi chua gan ID (gtag/fbq chua ton tai).
   ============================================================ */
(function () {
  'use strict';

  function track(name, params, pixelName) {
    params = params || {};
    try { if (window.gtag) window.gtag('event', name, params); } catch (e) {}
    try {
      if (window.fbq) {
        var std = ['Lead','Contact','ViewContent','CompleteRegistration','Search','InitiateCheckout'];
        if (pixelName && std.indexOf(pixelName) > -1) window.fbq('track', pixelName, params);
        else if (pixelName) window.fbq('trackCustom', pixelName, params);
      }
    } catch (e) {}
    if (window.TVBHS_DEBUG) console.log('[track]', name, pixelName || '', params);
  }
  window.tvbhsTrack = track;

  function nhanh() {
    try { return localStorage.getItem('tvbhs_track') || 'chua-chon'; } catch (e) { return 'chua-chon'; }
  }
  function trang() { return location.pathname || '/'; }

  /* ---- 1. Gui form thu lead (su kien quan trong nhat) ---- */
  document.querySelectorAll('form[data-lead]').forEach(function (f) {
    var daBan = false;
    f.addEventListener('submit', function () {
      if (daBan) return;      /* mot form chi ban generate_lead mot lan moi lan tai trang */
      daBan = true;
      var qt = '';
      try {
        var el = f.querySelector('[name="quan_tam"],[name="nhu_cau"],select');
        if (el) qt = el.value || '';
      } catch (e) {}
      track('generate_lead', {
        method: 'form_web', trang: trang(), nhanh_nhu_cau: nhanh(),
        quan_tam: qt, value: 1, currency: 'VND'
      }, 'Lead');
    });
  });

  /* ---- 2. Nhap Zalo / goi hotline ---- */
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var h = a.getAttribute('href') || '';
    if (h.indexOf('zalo.me') > -1) {
      track('lien_he_zalo', { trang: trang(), nhanh_nhu_cau: nhanh(), vi_tri: a.className || '' }, 'Contact');
    } else if (h.indexOf('tel:') === 0) {
      track('goi_hotline', { trang: trang(), nhanh_nhu_cau: nhanh() }, 'Contact');
    } else if (h.indexOf('facebook.com') > -1 || h.indexOf('tiktok.com') > -1) {
      track('click_mang_xa_hoi', { trang: trang(), dich: h }, null);
    }
  }, true);

  /* ---- 3. Dung cong cu tinh toan (chi ban 1 lan / cong cu / phien xem) ---- */
  (function () {
    var daBan = {};
    [['#birthCalc', 'chi_phi_sinh_con'], ['#waitForm', 'thoi_gian_cho'],
     ['#needForm', 'ngan_sach_bao_ve']].forEach(function (pair) {
      var form = document.querySelector(pair[0]);
      if (!form) return;
      var key = pair[1], t = null;
      function ban() {
        if (daBan[key]) return;
        daBan[key] = 1;
        track('dung_cong_cu', { cong_cu: key, trang: trang(), nhanh_nhu_cau: nhanh() }, 'ViewContent');
      }
      form.addEventListener('change', function () { clearTimeout(t); t = setTimeout(ban, 900); });
      form.addEventListener('input',  function () { clearTimeout(t); t = setTimeout(ban, 1800); });
    });
  })();

  /* ---- 4. Do sau cuon: 25 / 50 / 75 / 90% ---- */
  (function () {
    var moc = [25, 50, 75, 90], daBan = {}, cho = false;
    function do_() {
      cho = false;
      var d = document.documentElement, b = document.body;
      var cao = Math.max(b.scrollHeight, d.scrollHeight) - window.innerHeight;
      if (cao <= 0) return;
      var pct = (window.pageYOffset || d.scrollTop) / cao * 100;
      moc.forEach(function (m) {
        if (pct >= m && !daBan[m]) {
          daBan[m] = 1;
          track('cuon_trang', { phan_tram: m, trang: trang() }, m >= 75 ? 'DocSau' : null);
        }
      });
    }
    window.addEventListener('scroll', function () {
      if (!cho) { cho = true; requestAnimationFrame(do_); }
    }, { passive: true });
  })();

  /* ---- 5. Thoi gian doc co y nghia: o lai qua 30 giay ---- */
  setTimeout(function () {
    track('doc_lau_30s', { trang: trang(), nhanh_nhu_cau: nhanh() }, null);
  }, 30000);

  /* ---- 6. Chon nhanh nhu cau o popup ---- */
  document.addEventListener('click', function (e) {
    var b = e.target.closest && e.target.closest('[data-track-pick]');
    if (!b) return;
    track('chon_nhu_cau', { nhanh: b.getAttribute('data-track-pick'), trang: trang() }, 'Search');
  }, true);

  /* ---- 7. Mo cau hoi thuong gap (tin hieu y dinh) ---- */
  document.querySelectorAll('.acc-q').forEach(function (q) {
    q.addEventListener('click', function () {
      if (q.parentElement.classList.contains('open')) return; // dang dong lai
      track('mo_faq', { cau_hoi: (q.textContent || '').trim().slice(0, 80), trang: trang() }, null);
    });
  });

  /* ---- 8. Nguon truy cap: nho lai utm de gan vao lead ---- */
  (function () {
    try {
      var q = new URLSearchParams(location.search), got = {};
      ['utm_source','utm_medium','utm_campaign','utm_content','fbclid','gclid'].forEach(function (k) {
        if (q.get(k)) got[k] = q.get(k);
      });
      if (Object.keys(got).length) {
        got._t = Date.now();
        localStorage.setItem('tvbhs_utm', JSON.stringify(got));
      }
    } catch (e) {}
  })();
})();
