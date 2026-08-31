# -*- coding: utf-8 -*-
"""
Du lieu chi phi sinh con theo tung benh vien.

NGUYEN TAC BIEN TAP - doc truoc khi sua file nay:
  1. Moi con so PHAI co nguon va ngay cong bo. Khong co nguon -> khong dang.
  2. Khong bao gio ghi "gia 2026" neu benh vien chua cong bo bang gia 2026.
  3. Neu benh vien khong cong bo gia (vi du Vinmec) -> noi thang la khong cong bo,
     va ghi ro so tham khao lay tu dau. Khong bia.
  4. Truong "kiem_chung" cua moi bang: "chinh-thuc" | "thu-cap" | "chua-xac-minh"
"""

CAP_NHAT = "31/08/2026"   # ngay ra soat noi dung gan nhat

BV_DATA = [

# =====================================================================
{
 "slug": "tu-du",
 "ten": "Bệnh viện Từ Dũ",
 "tinh": "TP. Hồ Chí Minh",
 "loai": "Bệnh viện công tuyến cuối",
 "calc_key": "tudu",
 "nguon_ngay": "16/09/2025",
 "nguon_nhan": "Bản hướng dẫn chi phí bệnh viện công bố gần nhất mà chúng tôi truy cập được là <b>ngày 16/09/2025</b>; một số dòng giá chi tiết là bản 2022&ndash;2023 và được ghi rõ trong từng bảng. Từ Dũ chưa công bố bảng giá 2026.",
 "nguon_url": "https://www.tudu.com.vn/vn/huong-dan-dich-vu/dich-vu-sanh-mo/huong-dan-di-sanh-tai-benh-vien-tu-du/",
 "title": "Chi phí sinh con ở Bệnh viện Từ Dũ: bảng giá bệnh viện công bố và phần BHYT không trả",
 "desc": "Sinh thường và sinh mổ ở Từ Dũ hết bao nhiêu, tiền phòng dịch vụ mỗi ngày, giá gây tê ngoài màng cứng, và ba khoản BHYT không chi trả. Số liệu dẫn nguồn từ bệnh viện, ghi rõ ngày công bố.",
 "tom_tat": "Sinh thường không dịch vụ ở Từ Dũ khoảng <b>3&ndash;5 triệu</b>, có dịch vụ <b>10&ndash;15 triệu</b>. Sinh mổ không dịch vụ <b>7&ndash;10 triệu</b>, có dịch vụ <b>18&ndash;20 triệu</b>. Đó là tổng hoá đơn trước khi trừ bảo hiểm y tế. Phần khiến ngân sách vỡ không nằm ở đây &mdash; mà ở tiền phòng dịch vụ, khoản BHYT không trả một đồng nào.",

 "bang": [
   {"ten": "Chi phí sinh thường",
    "kiem_chung": "chinh-thuc",
    "nguon": "tudu.com.vn, công bố 16/09/2025",
    "cot": ["Hình thức", "Tổng chi phí (chưa trừ BHYT)", "Số ngày nằm viện"],
    "hang": [
      ["Sanh <b>không</b> dịch vụ", "3.000.000 &ndash; 5.000.000đ", "khoảng 3 ngày"],
      ["Sanh <b>có</b> dịch vụ", "10.000.000 &ndash; 15.000.000đ", "khoảng 3 ngày"],
      ["Tạm ứng khi nhập viện (có dịch vụ)", "từ 10.000.000đ", "&mdash;"],
      ["Tạm ứng khi nhập viện (không dịch vụ)", "5.000.000đ", "&mdash;"],
    ]},
   {"ten": "Chi phí sinh mổ",
    "kiem_chung": "chinh-thuc",
    "nguon": "tudu.com.vn, công bố 16/09/2025 (riêng tiền công mổ: bản 02/02/2023)",
    "cot": ["Hình thức", "Số tiền", "Ghi chú"],
    "hang": [
      ["Tổng, <b>không</b> dịch vụ", "7.000.000 &ndash; 10.000.000đ", "nằm viện khoảng 5 ngày"],
      ["Tổng, <b>có</b> dịch vụ", "18.000.000 &ndash; 20.000.000đ", "nằm viện khoảng 5 ngày"],
      ["Tiền công mổ lần đầu", "2.604.000đ", "số niêm yết bản 2023"],
      ["Tiền công mổ lần 2 trở lên", "3.376.200đ", "số niêm yết bản 2023"],
      ["Mổ dịch vụ theo yêu cầu", "4.000.000 &ndash; 4.500.000đ", "số niêm yết bản 2023"],
      ["Phụ phí mổ gia đình", "cộng thêm 1.000.000đ", "số niêm yết bản 2023"],
    ]},
   {"ten": "Tiền phòng và các khoản cộng thêm",
    "kiem_chung": "chinh-thuc",
    "nguon": "tudu.com.vn, các bản công bố 2022&ndash;2023",
    "cot": ["Khoản mục", "Giá", "BHYT có trả không"],
    "hang": [
      ["Phòng hậu sản dịch vụ (khu N, M, H, B)", "600.000 &ndash; 4.000.000đ / ngày", "<b>Không</b> &mdash; tự trả 100%"],
      ["Ngày giường điều trị nội trú", "203.600đ / ngày", "Có, trong phạm vi BHYT"],
      ["Giảm đau sản khoa (gây tê ngoài màng cứng)", "1.849.000đ", "Tuỳ chỉ định"],
      ["Chọn bác sĩ đỡ sinh", "<b>0đ &mdash; không thu thêm phí</b>", "Không phát sinh"],
      ["Bộ khăn phẫu thuật (dùng 1 lần)", "586.000đ", "Không"],
    ]},
 ],

 "khong_cong_bo": [
   "<b>Giá NICU / chăm sóc đặc biệt sơ sinh hiện hành.</b> Bảng giá duy nhất Từ Dũ từng công bố là bản năm 2015 &mdash; đã hơn 10 năm, chắc chắn không còn đúng. Chúng tôi không đăng lại con số đó. Điểm quan trọng vẫn còn giá trị: bệnh viện xác nhận các khoản điều trị cho trẻ sơ sinh <b>được BHYT thanh toán</b> khi nộp đủ giấy tờ; gia đình chủ yếu tự trả sữa, tã và thuốc Surfactant từ lọ thứ ba trở đi.",
   "<b>Giá sàng lọc sơ sinh mở rộng.</b> Không tìm thấy công bố công khai.",
   "<b>Bảng giá từng dòng theo loại phòng.</b> Từ Dũ đăng dưới dạng file ảnh trên website, không tra cứu được bằng máy. Muốn biết chính xác phòng nào bao nhiêu, phải hỏi trực tiếp lúc nhập viện.",
 ],

 "luu_y": [
   ("Không cần đăng ký sinh trước",
    "Bệnh viện nói rõ: tất cả trường hợp nhập viện sinh tại Từ Dũ đều không cần đăng ký trước. Bạn chọn hình thức dịch vụ ngay lúc làm thủ tục nhập viện, tại cổng số 1 &mdash; 284 Cống Quỳnh."),
   ("Chọn bác sĩ không mất thêm tiền",
    "Rất nhiều người tưởng phải &ldquo;lót tay&rdquo; để được bác sĩ mình muốn. Từ Dũ công bố rõ: khi đã đăng ký sinh dịch vụ, sản phụ được quyền yêu cầu bác sĩ mà không thu thêm phí."),
   ("Có BHYT thì được tính như đúng tuyến, kể cả không có giấy chuyển tuyến",
    "Đây là thay đổi nhiều người chưa cập nhật. Sản phụ có thẻ BHYT sinh tại Từ Dũ được hưởng đúng tuyến 100% chi phí nội trú trong phạm vi BHYT, kể cả khi thẻ đăng ký ở tỉnh khác và không có giấy chuyển tuyến."),
   ("Có cả BHYT và bảo hiểm dịch vụ thì chỉ được chọn một",
    "Điểm này hay bị hiểu sai nhất. Tại bệnh viện, bạn chỉ được chọn một loại để hưởng &mdash; không cộng dồn. Loại còn lại phải tự làm hồ sơ đòi bồi thường sau."),
   ("Bệnh viện phát sẵn túi tiện ích",
    "Chăn, khăn, quần lót giấy, băng vệ sinh, bàn chải, kem đánh răng, bình nước, hộp trữ cuống rốn đều có sẵn. Mẹ không cần mang vác nhiều như các danh sách trên mạng khuyên."),
 ],

 "faq": [
   ("Sinh ở Bệnh viện Từ Dũ hết bao nhiêu tiền?",
    "Theo hướng dẫn bệnh viện công bố ngày 16/09/2025: sinh thường không dịch vụ khoảng 3&ndash;5 triệu, có dịch vụ 10&ndash;15 triệu, nằm viện khoảng 3 ngày. Sinh mổ không dịch vụ 7&ndash;10 triệu, có dịch vụ 18&ndash;20 triệu, nằm viện khoảng 5 ngày. Đây là tổng chi phí trước khi trừ bảo hiểm y tế."),
   ("Tiền phòng dịch vụ ở Từ Dũ bao nhiêu một ngày?",
    "Phòng hậu sản dịch vụ dao động 600.000 đến 4.000.000đ mỗi ngày tuỳ khu và loại phòng. Đây là khoản bảo hiểm y tế <b>không chi trả</b> đồng nào, và cũng là khoản khiến ngân sách vỡ nhiều nhất vì nhân với số ngày nằm viện."),
   ("Có bảo hiểm y tế thì sinh ở Từ Dũ được hưởng bao nhiêu?",
    "Sản phụ có thẻ BHYT được tính hưởng đúng tuyến 100% chi phí nội trú trong phạm vi BHYT, kể cả khi không có giấy chuyển tuyến. Nhưng phần vượt phạm vi BHYT &mdash; đặc biệt là tiền phòng dịch vụ &mdash; vẫn phải tự thanh toán toàn bộ."),
   ("Đẻ không đau ở Từ Dũ giá bao nhiêu?",
    "Bệnh viện niêm yết giảm đau sản khoa (gây tê ngoài màng cứng) là 1.849.000đ, theo bản công bố ngày 29/08/2022. Nên gọi xác nhận lại trước khi sinh vì đây là số của năm 2022."),
   ("Chọn bác sĩ đỡ sinh ở Từ Dũ có phải trả thêm tiền không?",
    "Không. Bệnh viện công bố rõ: khi đã đăng ký sinh dịch vụ, sản phụ được quyền chỉ định bác sĩ mà không thu thêm phí."),
   ("Có cần đăng ký sinh ở Từ Dũ trước không?",
    "Không cần. Bệnh viện xác nhận mọi trường hợp nhập viện sinh đều không cần đăng ký trước; chọn hình thức dịch vụ ngay khi làm thủ tục nhập viện. Tạm ứng từ 10 triệu nếu chọn dịch vụ, 5 triệu nếu không."),
   ("Nên chuẩn bị sẵn bao nhiêu tiền mặt khi đi sinh ở Từ Dũ?",
    "Tối thiểu bằng mức tạm ứng (5 hoặc 10 triệu). Nhưng nếu tính cả kịch bản chuyển từ sinh thường sang sinh mổ và nằm phòng dịch vụ thêm vài ngày, con số an toàn nên gấp đôi mức bạn dự tính ban đầu."),
 ],
},

# =====================================================================
{
 "slug": "hung-vuong",
 "ten": "Bệnh viện Hùng Vương",
 "tinh": "TP. Hồ Chí Minh",
 "loai": "Bệnh viện công tuyến cuối",
 "calc_key": "hungvuong",
 "nguon_ngay": "23/09/2025",
 "nguon_nhan": "Câu trả lời chính thức gần nhất của bệnh viện là <b>ngày 23/09/2025</b>. Hùng Vương phát hành bảng giá qua file Google Sheets và file này hiện khoá quyền truy cập, nên không ai tra cứu trước được.",
 "nguon_url": "https://bvhungvuong.vn/hoi-dap/goi-sinh-va-chi-phi-sinh-cua-benh-vien",
 "title": "Chi phí sinh con ở Bệnh viện Hùng Vương: tạm ứng bao nhiêu, tiền phòng bao nhiêu một ngày",
 "desc": "Hùng Vương không bán gói trọn gói, thanh toán theo thực tế. Mức tạm ứng sinh thường và sinh mổ, giá phòng một giường, chọn bác sĩ có mất phí không, và mức BHYT thực tế được hưởng.",
 "tom_tat": "Hùng Vương <b>không bán gói sinh trọn gói</b> &mdash; bệnh viện khẳng định chi phí thanh toán theo thực tế sử dụng từng trường hợp. Bạn đóng tạm ứng lúc nhập viện: <b>6&ndash;7 triệu</b> diện nhà nước, <b>10&ndash;18 triệu</b> diện dịch vụ. Dư thì hoàn lại, thiếu thì đóng thêm. Khoản đắt nhất và ít ai tính trước là tiền phòng một giường: <b>3&ndash;3,7 triệu mỗi ngày</b>.",

 "bang": [
   {"ten": "Mức tạm ứng khi nhập viện sinh",
    "kiem_chung": "chinh-thuc",
    "nguon": "bvhungvuong.vn, mục Hỏi&ndash;Đáp do bệnh viện trả lời, 15/06/2024 và 23/09/2025",
    "cot": ["Hình thức", "Tạm ứng", "Ghi chú"],
    "hang": [
      ["Sinh thường &mdash; diện nhà nước", "6.000.000 &ndash; 7.000.000đ", "quyết toán theo thực tế"],
      ["Sinh thường &mdash; diện dịch vụ", "10.000.000 &ndash; 18.000.000đ", "quyết toán theo thực tế"],
      ["Sinh mổ &mdash; diện dịch vụ", "10.000.000 &ndash; 18.000.000đ", "quyết toán theo thực tế"],
    ]},
   {"ten": "Tiền công mổ &mdash; con số niêm yết duy nhất bệnh viện công bố",
    "kiem_chung": "chinh-thuc",
    "nguon": "bvhungvuong.vn, Hỏi&ndash;Đáp 12/04/2024",
    "cot": ["Khoản mục", "Số tiền", "Ai trả"],
    "hang": [
      ["Tiền công mổ (trường hợp mổ lần 3)", "7.193.000đ", "tổng"],
      ["&mdash; phần BHYT chi trả", "3.102.000đ", "bảo hiểm y tế"],
      ["&mdash; phần gia đình tự trả", "khoảng 4.091.000đ", "<b>gia đình</b>"],
    ]},
   {"ten": "Tiền phòng và dịch vụ cộng thêm",
    "kiem_chung": "chinh-thuc",
    "nguon": "bvhungvuong.vn, Hỏi&ndash;Đáp 09/04/2024 và 23/08/2023",
    "cot": ["Khoản mục", "Giá", "Ghi chú"],
    "hang": [
      ["Phòng 1 giường tiêu chuẩn", "3.000.000 &ndash; 3.700.000đ / ngày", "khoản đắt nhất, BHYT không trả"],
      ["Phòng nằm sau mổ", "3.500.000 &ndash; 3.700.000đ / ngày", "nhân với 4&ndash;5 ngày"],
      ["Chọn bác sĩ mổ / đỡ sinh", "<b>0đ &mdash; không thu thêm phí</b>", "khi đã chọn sinh dịch vụ"],
      ["Massage thư giãn cho bé", "250.000đ", "dịch vụ tự chọn"],
      ["Cắt rốn kèm chụp hình", "500.000đ", "dịch vụ tự chọn"],
      ["Tắm sơ sinh", "30.000đ", "dịch vụ tự chọn"],
    ]},
   {"ten": "Khám thai dịch vụ",
    "kiem_chung": "chinh-thuc",
    "nguon": "bvhungvuong.vn, Hỏi&ndash;Đáp 09/07/2023",
    "cot": ["Loại khám", "Tạm ứng", "Ghi chú"],
    "hang": [
      ["Khám thai dịch vụ", "500.000 &ndash; 1.600.000đ", "trừ dần vào thẻ khám"],
      ["Khám thai chuyên gia", "1.500.000 &ndash; 3.000.000đ", "trừ dần vào thẻ khám"],
    ]},
 ],

 "khong_cong_bo": [
   "<b>Bảng giá viện phí đầy đủ.</b> Hùng Vương phát hành bảng giá qua file Google Sheets, và file này hiện <b>khoá quyền truy cập</b> với người ngoài. Nghĩa là không ai tra cứu trước được &mdash; phải gọi tổng đài (028) 3855 8532.",
   "<b>Giá NICU / chăm sóc đặc biệt sơ sinh.</b> Không có bất kỳ công bố nào. Chúng tôi <b>không mượn số của bệnh viện khác</b> để lấp chỗ trống này.",
   "<b>Số ngày nằm viện chuẩn.</b> Bệnh viện không công bố. Không suy từ Từ Dũ sang được.",
   "<b>Giá gói khám thai trọn gói.</b> Bệnh viện xác nhận có triển khai dịch vụ này tại Phòng khám Chuyên gia &mdash; nhưng trang giá không truy cập được.",
 ],

 "luu_y": [
   ("Không có gói trọn gói &mdash; đây là khác biệt lớn nhất so với bệnh viện tư",
    "Bệnh viện nói rõ ngày 23/09/2025: không áp dụng gói sinh trọn gói, chi phí thanh toán theo thực tế sử dụng mỗi trường hợp. Ưu điểm: không trả cho thứ mình không dùng. Nhược điểm: bạn không biết trước con số cuối cùng."),
   ("Thẻ BHYT ở tỉnh khác vẫn được hưởng như đúng tuyến",
    "Bệnh viện xác nhận (04/2024): nhập viện sinh thì dù thẻ đăng ký ở tỉnh khác vẫn hưởng như đúng tuyến, mức 80% trong danh mục BHYT, không cần giấy chuyển tuyến."),
   ("Đừng tin con số &ldquo;trái tuyến chỉ 48%&rdquo; còn trôi nổi trên mạng",
    "Đó là câu trả lời của bệnh viện từ năm 2019 và <b>đã bị chính bệnh viện thay thế</b> bằng hướng dẫn 2024 ở trên. Nhiều bài viết vẫn chép lại con số cũ này và làm người đọc tính sai ngân sách."),
   ("Sanh VIP và sanh gia đình khác nhau ở thời điểm người nhà được vào",
    "Phòng sanh VIP cho người nhà vào từ lúc nhập sanh. Box sanh gia đình chỉ cho vào sau khi đã chuyển lên khoa sanh. Nếu điều quan trọng với bạn là có chồng bên cạnh suốt quá trình, đây là điểm cần hỏi kỹ."),
   ("Không gây tê ngoài màng cứng thì vẫn phải chích tê tại chỗ",
    "Khi rạch và khâu tầng sinh môn, tê tại chỗ là bắt buộc. Đây không phải khoản tuỳ chọn."),
 ],

 "faq": [
   ("Sinh ở Bệnh viện Hùng Vương hết bao nhiêu tiền?",
    "Bệnh viện không bán gói trọn gói mà thu tạm ứng rồi quyết toán theo thực tế. Tạm ứng sinh thường diện nhà nước 6&ndash;7 triệu, diện dịch vụ 10&ndash;18 triệu; sinh mổ dịch vụ cũng 10&ndash;18 triệu. Dư được hoàn lại khi xuất viện."),
   ("Bệnh viện Hùng Vương có gói sinh trọn gói không?",
    "Không. Bệnh viện khẳng định ngày 23/09/2025 rằng không áp dụng gói sinh trọn gói, chi phí sẽ thanh toán theo thực tế sử dụng của mỗi trường hợp."),
   ("Tiền phòng một giường ở Hùng Vương bao nhiêu?",
    "Từ 3.000.000 đến 3.700.000đ mỗi ngày theo công bố tháng 4/2024. Đây là khoản đắt nhất trong hoá đơn nếu bạn nằm 4&ndash;5 ngày sau mổ, và bảo hiểm y tế không chi trả phần này."),
   ("Thẻ BHYT ở tỉnh khác sinh ở Hùng Vương có được hưởng không?",
    "Có. Bệnh viện xác nhận khi nhập viện sinh, dù thẻ đăng ký ở tỉnh khác vẫn được hưởng như đúng tuyến, mức 80% trong danh mục BHYT và không cần giấy chuyển tuyến."),
   ("Chọn bác sĩ mổ ở Hùng Vương có tốn thêm phí không?",
    "Không. Bệnh viện trả lời rõ: chọn sinh dịch vụ thì được quyền yêu cầu bác sĩ mổ sinh mà không đóng thêm phí."),
   ("Gây tê ngoài màng cứng ở Hùng Vương giá bao nhiêu?",
    "Con số bệnh viện từng trả lời là 1.200.000đ, nhưng đó là năm 2018 &mdash; đã tám năm. Chúng tôi không đăng con số này như giá hiện hành. Gọi (028) 3855 8532 để xác nhận."),
   ("Sinh ở Từ Dũ hay Hùng Vương rẻ hơn?",
    "Ở mức không dịch vụ, Từ Dũ nhỉnh hơn về giá (3&ndash;5 triệu so với tạm ứng 6&ndash;7 triệu). Nhưng ở mức dịch vụ hai bên gần tương đương. Khác biệt thật nằm ở tiền phòng: phòng một giường Hùng Vương 3&ndash;3,7 triệu/ngày, còn Từ Dũ có dải rộng hơn từ 600.000đ. Nếu ngân sách chặt, dải phòng của Từ Dũ cho bạn nhiều lựa chọn hơn."),
 ],
},

# =====================================================================
{
 "slug": "tam-anh",
 "ten": "Bệnh viện Đa khoa Tâm Anh",
 "tinh": "TP.HCM và Hà Nội",
 "loai": "Bệnh viện tư",
 "calc_key": "tamanh",
 "nguon_ngay": "31/08/2026",
 "nguon_nhan": "Bảng giá dưới đây là bảng <b>đang hiển thị trên website bệnh viện</b>, chúng tôi truy cập ngày 31/08/2026. Tâm Anh không ghi ngày hiệu lực trên trang giá.",
 "nguon_url": "https://tamanhhospital.vn/sinh-con-tron-goi/",
 "title": "Chi phí sinh con ở Bệnh viện Tâm Anh: bảng giá gói trọn gói và khoản 10 triệu phát sinh ngoài gói",
 "desc": "Bảng giá gói thai sản Tâm Anh TP.HCM và Hà Nội theo từng tuần đăng ký. Kèm số liệu nghiên cứu bình duyệt: trung bình mỗi ca phát sinh thêm 10,2 triệu ngoài gói.",
 "tom_tat": "Tâm Anh là bệnh viện <b>minh bạch giá nhất</b> trong nhóm bệnh viện tư &mdash; đăng bảng giá chi tiết từng gói, từng loại sinh ngay trên website. Gói TP.HCM từ <b>31,4 triệu</b> đến <b>71,1 triệu</b>. Nhưng có một con số quan trọng hơn cả bảng giá, và nó không nằm trên website bệnh viện: một nghiên cứu khoa học bình duyệt năm 2024 đo được mỗi ca sinh <b>phát sinh thêm trung bình 10,2 triệu ngoài gói</b>.",

 "bang": [
   {"ten": "Gói TIÊU CHUẨN &mdash; Tâm Anh TP.HCM, đơn thai",
    "kiem_chung": "chinh-thuc",
    "nguon": "tamanhhospital.vn/sinh-con-tron-goi/",
    "cot": ["Đăng ký từ tuần", "Sinh thường", "Sinh thường + giảm đau", "Sinh mổ lần 1", "Sinh mổ lần 2"],
    "hang": [
      ["Tuần 12", "41.010.000đ", "44.670.000đ", "46.520.000đ", "48.920.000đ"],
      ["Tuần 22", "35.110.000đ", "38.770.000đ", "40.620.000đ", "43.020.000đ"],
      ["Tuần 32", "32.870.000đ", "36.520.000đ", "38.370.000đ", "40.780.000đ"],
      ["Tuần 36", "31.430.000đ", "35.080.000đ", "36.930.000đ", "39.340.000đ"],
    ]},
   {"ten": "Gói VIP &mdash; Tâm Anh TP.HCM, đơn thai",
    "kiem_chung": "chinh-thuc",
    "nguon": "tamanhhospital.vn/sinh-con-tron-goi/",
    "cot": ["Đăng ký từ tuần", "Sinh thường", "Sinh thường + giảm đau", "Sinh mổ lần 1", "Sinh mổ lần 2"],
    "hang": [
      ["Tuần 12", "59.280.000đ", "62.600.000đ", "68.870.000đ", "71.060.000đ"],
      ["Tuần 22", "49.140.000đ", "52.460.000đ", "58.730.000đ", "60.920.000đ"],
      ["Tuần 32", "44.640.000đ", "47.960.000đ", "54.240.000đ", "56.420.000đ"],
      ["Tuần 36", "41.510.000đ", "44.840.000đ", "51.110.000đ", "53.290.000đ"],
    ]},
   {"ten": "Tâm Anh Hà Nội &mdash; cấu trúc giá khác TP.HCM",
    "kiem_chung": "chinh-thuc",
    "nguon": "tamanhhospital.vn/cham-soc-thai-san-tron-goi/",
    "cot": ["Gói", "Loại", "Phòng 1 giường", "Phòng 2 giường"],
    "hang": [
      ["Tuần 12", "Đơn thai, sinh thường", "43.080.000đ", "38.140.000đ"],
      ["Tuần 12", "Đơn thai, mổ lần 1", "58.740.000đ", "53.090.000đ"],
      ["Tuần 12", "Song thai, sinh thường", "54.670.000đ", "48.570.000đ"],
      ["Tuần 12", "Ba thai, sinh thường", "64.870.000đ", "57.750.000đ"],
      ["Tuần 36", "Đơn thai, sinh thường", "&mdash;", "28.340.000đ"],
      ["VIP tuần 12", "Đơn thai, sinh thường", "67.240.000đ", "&mdash;"],
    ]},
   {"ten": "Song thai &mdash; Tâm Anh TP.HCM",
    "kiem_chung": "chinh-thuc",
    "nguon": "tamanhhospital.vn/sinh-con-tron-goi/",
    "cot": ["Gói / tuần", "Sinh thường", "Sinh thường + giảm đau", "Sinh mổ lần 1", "Sinh mổ lần 2"],
    "hang": [
      ["Tiêu chuẩn &mdash; tuần 32", "35.940.000đ", "39.600.000đ", "41.570.000đ", "44.150.000đ"],
      ["Tiêu chuẩn &mdash; tuần 34", "33.910.000đ", "37.560.000đ", "39.530.000đ", "42.110.000đ"],
      ["VIP &mdash; tuần 32", "49.830.000đ", "53.160.000đ", "59.540.000đ", "61.890.000đ"],
      ["VIP &mdash; tuần 34", "45.620.000đ", "48.940.000đ", "55.320.000đ", "57.670.000đ"],
    ]},
 ],

 "diem_nhan": {
   "tieu_de": "Con số quan trọng nhất trên trang này không nằm trong bảng giá",
   "noi_dung": "Có một nghiên cứu khoa học bình duyệt đo đúng câu hỏi &ldquo;mua gói rồi thì còn phải trả thêm bao nhiêu&rdquo;. Nghiên cứu mô tả cắt ngang trên các sản phụ mua gói trọn gói tại Tâm Anh từ tháng 12/2023 đến tháng 5/2024, đăng trên Tạp chí Y học Cộng đồng năm 2024.",
   "so": [
     ("Tổng chi phí trung bình mỗi ca sinh", "45.532.846đ", "độ lệch chuẩn 14,3 triệu"),
     ("Phần nằm trong gói", "35.293.286đ", "độ lệch chuẩn 8,5 triệu"),
     ("<b>Phần phát sinh ngoài gói</b>", "<b>10.239.560đ</b>", "<b>độ lệch chuẩn 12,1 triệu</b>"),
   ],
   "ket": "Hãy nhìn kỹ dòng cuối: độ lệch chuẩn 12,1 triệu <b>lớn hơn cả giá trị trung bình 10,2 triệu</b>. Về mặt thống kê, điều đó nghĩa là khoản phát sinh này <b>không dự đoán được</b>. Nhiều gia đình gần như không phát sinh gì; một số phát sinh vài chục triệu. Nếu bạn lập ngân sách bằng đúng giá gói, xác suất vỡ kế hoạch là rất cao. Nguồn: An, P.T., An, N.T.B., Cần, M.N. (2024), Tạp chí Y học Cộng đồng 65(6), DOI 10.52163/yhc.v65i6.1707.",
 },

 "khong_bao_gom": [
   "Khám cấp cứu ngoài giờ hành chính khi <b>chưa</b> chuyển dạ thực sự &mdash; rất hay xảy ra với con so.",
   "<b>Mổ lấy thai theo yêu cầu, không có chỉ định y khoa</b> &mdash; phụ thu thêm.",
   "Khám chuyên khoa cho bệnh lý không liên quan đến sinh nở.",
   "<b>Giảm đau đẻ tại TP.HCM là mức giá riêng</b>, cộng thêm khoảng 3,3&ndash;3,7 triệu. Đây là lỗi so sánh giá phổ biến nhất khi người ta đặt giá Tâm Anh cạnh giá bệnh viện khác.",
   "Chi phí vượt ngoài phác đồ chuẩn.",
   "Khám tặng sau sinh chỉ có hiệu lực trong 30 ngày.",
 ],

 "khong_cong_bo": [
   "<b>Giá NICU / chăm sóc đặc biệt sơ sinh.</b> Không công bố đơn giá theo ngày. Đây là rủi ro tài chính lớn nhất và không ước tính trước được.",
   "<b>Giá ngày giường theo hạng phòng.</b> File PDF bảng giá trên website hiện lỗi 404.",
   "<b>Giá sinh lẻ trọn ca</b> nếu không mua gói.",
 ],

 "luu_y": [
   ("Bảo hiểm y tế bù lại rất ít, đừng trông chờ",
    "Tâm Anh nhận mọi thẻ BHYT, mức hưởng 70/80/100% tuỳ đối tượng. Nhưng mức hưởng được tính <b>theo khung giá bệnh viện công</b>. Với hoá đơn 40&ndash;70 triệu ở bệnh viện tư, phần BHYT bù lại chỉ là một tỷ lệ nhỏ."),
   ("Có bảo lãnh viện phí trực tiếp với khoảng 18 công ty bảo hiểm",
    "Gồm Bảo Việt, Pacific Cross, Generali, Dai-ichi Life, Bảo Minh, GIC, BIC, Papaya, MIC, PTI, <b>AIA</b>, VBI, PJICO, InSmart, Fullerton, ATACC và một số đơn vị khác."),
   ("PVI đã dừng bảo lãnh tại cơ sở TP.HCM từ 01/11/2024",
    "Nếu bạn cầm thẻ PVI, phải tự thanh toán rồi lấy chứng từ đòi lại sau. Đây là thay đổi nhiều người không biết cho tới lúc đứng ở quầy thu ngân."),
   ("Khám thai định kỳ thường không được bảo hiểm tư nhân chi trả",
    "Danh mục loại trừ của hầu hết hợp đồng có mục &ldquo;khám thai sản định kỳ&rdquo;. Ca sinh có thể được chi trả, nhưng phần khám thai trong gói thì thường không."),
   ("Đăng ký sớm đắt hơn, nhưng không hẳn là đắt hơn",
    "Gói tuần 36 rẻ hơn gói tuần 12 khoảng 9,6 triệu ở TP.HCM. Nhưng gói tuần 12 đã bao gồm toàn bộ khám thai từ tuần 12 trở đi. Mua gói muộn thì bạn vẫn phải trả riêng các lần khám thai đó. Hãy so tổng chi, đừng so giá gói."),
 ],

 "faq": [
   ("Sinh ở Bệnh viện Tâm Anh hết bao nhiêu tiền?",
    "Gói trọn gói TP.HCM từ 31,43 triệu (tuần 36, sinh thường, tiêu chuẩn) đến 71,06 triệu (tuần 12, mổ lần 2, VIP). Hà Nội từ 28,34 triệu đến khoảng 118,78 triệu cho gói VIP đa thai. Nhưng nghiên cứu năm 2024 cho thấy tổng thực chi trung bình khoảng 45,5 triệu mỗi ca."),
   ("Mua gói thai sản Tâm Anh sớm hay muộn thì rẻ hơn?",
    "Về giá niêm yết, gói tuần 36 rẻ hơn gói tuần 12 khoảng 9,6 triệu tại TP.HCM. Nhưng gói tuần 12 bao gồm toàn bộ các lần khám thai từ tuần 12 đến khi sinh. Nếu mua gói muộn, bạn vẫn phải trả riêng những lần khám đó, nên tổng chi có thể không rẻ hơn."),
   ("Giá gói đã bao gồm đẻ không đau chưa?",
    "Tại TP.HCM là chưa. Giảm đau đẻ được tính thành một mức giá riêng, chênh khoảng 3.320.000 đến 3.660.000đ. Đây là chỗ hay bị so sánh sai khi đặt giá Tâm Anh cạnh bệnh viện khác."),
   ("Mua gói rồi thì còn phải trả thêm gì nữa không?",
    "Có, và khoản này lớn. Nghiên cứu bình duyệt năm 2024 đo được trung bình mỗi ca phát sinh thêm 10.239.560đ ngoài gói, với độ lệch chuẩn 12,1 triệu. Các khoản chính gồm: mổ theo yêu cầu không có chỉ định y khoa, khám cấp cứu ngoài giờ khi chưa chuyển dạ thực sự, nằm viện dài hơn dự kiến, bệnh lý ngoài sản khoa, và chăm sóc đặc biệt cho bé."),
   ("Sinh mổ ở Tâm Anh đắt hơn sinh thường bao nhiêu?",
    "Tại TP.HCM, gói tiêu chuẩn tuần 12: sinh thường 41,01 triệu, mổ lần 1 46,52 triệu &mdash; chênh khoảng 5,5 triệu. Tại Hà Nội cùng mốc tuần 12 phòng một giường: 43,08 lên 58,74 triệu &mdash; chênh tới 15,7 triệu."),
   ("Bảo hiểm y tế dùng được ở Tâm Anh không?",
    "Được, Tâm Anh nhận thẻ BHYT đăng ký ban đầu ở bất kỳ cơ sở nào, mức hưởng 70/80/100% tuỳ đối tượng. Nhưng mức hưởng tính theo khung giá bệnh viện công, nên với hoá đơn vài chục triệu, phần bù lại chiếm tỷ lệ nhỏ."),
   ("Bảo hiểm tư nhân có bảo lãnh viện phí trực tiếp ở Tâm Anh không?",
    "Có, với khoảng 18 công ty gồm Bảo Việt, AIA, Generali, Dai-ichi, Bảo Minh, PTI, MIC, Pacific Cross và một số đơn vị khác. Lưu ý PVI đã tạm dừng bảo lãnh tại cơ sở TP.HCM từ 01/11/2024."),
 ],
},

# =====================================================================
{
 "slug": "vinmec",
 "ten": "Bệnh viện Vinmec",
 "tinh": "Toàn quốc",
 "loai": "Bệnh viện tư quốc tế",
 "calc_key": "vinmec",
 "nguon_ngay": "31/08/2026",
 "nguon_nhan": "Chúng tôi truy cập website Vinmec ngày 31/08/2026 và <b>không tìm thấy bất kỳ con số giá nào</b>. Bệnh viện chỉ ghi &ldquo;áp dụng bảng giá mới từ 14/10/2025&rdquo; mà không đăng bảng.",
 "nguon_url": "https://www.vinmec.com/vie/di-sinh-tai-vinmec-dich-vu-thai-san-toan-dien/",
 "title": "Chi phí sinh con ở Vinmec: vì sao không tìm được bảng giá, và những gì kiểm chứng được",
 "desc": "Vinmec không công bố giá gói thai sản trên website. Trang này tách rõ phần bệnh viện xác nhận chính thức và phần chỉ là ước tính từ bên thứ ba, thay vì đưa một bảng giá không rõ nguồn.",
 "tom_tat": "Nếu bạn đã tìm mỏi mắt mà không thấy bảng giá thai sản Vinmec, thì không phải bạn tìm kém. <b>Vinmec không công bố giá công khai.</b> Trang &ldquo;Bảng giá dịch vụ thai sản trọn gói tại Vinmec&rdquo; trên website chính thức có tiêu đề nhưng không có con số nào. Mọi bảng giá Vinmec bạn thấy trên internet đều là do bên thứ ba tổng hợp &mdash; và chúng <b>mâu thuẫn nhau tới hai, ba lần</b>.",
 "canh_bao": "Chúng tôi quyết định không đăng một bảng giá Vinmec như thể đó là số chắc chắn. Thay vào đó, trang này tách làm hai phần rõ ràng: phần Vinmec xác nhận chính thức, và phần chỉ là tham khảo. Bạn tự quyết định tin đến đâu.",

 "bang": [
   {"ten": "Phần Vinmec XÁC NHẬN CHÍNH THỨC",
    "kiem_chung": "chinh-thuc",
    "nguon": "vinmec.com",
    "cot": ["Nội dung", "Xác nhận"],
    "hang": [
      ["Các mốc gói thai sản", "Tuần 12, 22, 27, 36 &mdash; và gói chuyển dạ"],
      ["Gói chuyển dạ dành cho ai", "Mẹ chưa từng đăng ký gói thai sản trước đó (tương đương &ldquo;sinh lẻ&rdquo;)"],
      ["Phạm vi áp dụng", "Toàn hệ thống Vinmec"],
      ["Ưu đãi", "<b>Giảm 10%</b> khi mua gói 12/22/27/36 tuần và gói chuyển dạ"],
      ["Ưu đãi combo", "Thai sản + vaccine + biobank: giảm thêm 1&ndash;2 triệu"],
      ["Gói bao gồm", "Khám thai, xét nghiệm, siêu âm, lớp học tiền sản, quà mẹ &amp; bé, suất ăn cho mẹ, sữa công thức cho bé"],
      ["Bảng giá mới Times City &amp; Central Park", "Hiệu lực từ 14/10/2025 &mdash; nhưng <b>không đăng số</b>"],
      ["Số đối tác bảo lãnh viện phí", "<b>35 công ty</b> &mdash; rộng hơn hầu hết bệnh viện khác"],
    ]},
   {"ten": "Phần THAM KHẢO &mdash; số từ bên thứ ba, Vinmec chưa xác nhận",
    "kiem_chung": "thu-cap",
    "nguon": "Tổng hợp từ các trang thứ ba, đối chiếu chéo giữa nhiều nguồn. KHÔNG phải số chính thức của Vinmec.",
    "cot": ["Loại sinh (Times City / Central Park, đơn thai)", "Dải giá tham khảo (tuần 36 &rarr; tuần 12)"],
    "hang": [
      ["Sinh thường", "khoảng 37.200.000 &ndash; 52.000.000đ"],
      ["Sinh mổ lần 1", "khoảng 52.000.000 &ndash; 65.000.000đ"],
      ["Sinh mổ lần 2", "khoảng 56.000.000 &ndash; 68.000.000đ"],
      ["Sinh mổ lần 3 trở lên", "khoảng 60.500.000 &ndash; 72.000.000đ"],
      ["Chi nhánh tỉnh (Hải Phòng, Nha Trang, Đà Nẵng, Hạ Long, Phú Quốc)", "thấp hơn đáng kể: sinh thường khoảng 24&ndash;33 triệu"],
    ]},
 ],

 "khong_cong_bo": [
   "<b>Toàn bộ bảng giá gói thai sản.</b> Vinmec yêu cầu gọi hotline để biết giá. Tổng đài 024 3975 6789, Times City 024 3974 3556.",
   "<b>Giá gói chuyển dạ</b> (trường hợp đến viện khi đã chuyển dạ mà chưa mua gói).",
   "<b>Giá ngày giường theo hạng phòng.</b>",
   "<b>Giá NICU / chăm sóc đặc biệt sơ sinh.</b> Chỉ xác nhận được rằng NICU nằm ngoài gói.",
   "<b>Số ngày nằm viện chính thức theo gói.</b> Nguồn thứ cấp ghi sinh thường 1&ndash;2 đêm, sinh mổ 3&ndash;4 đêm.",
 ],

 "luu_y": [
   ("Vì sao chúng tôi không đưa một bảng giá Vinmec đẹp đẽ như các trang khác",
    "Vì chúng tôi đã kiểm tra và các bảng giá đó mâu thuẫn nhau nghiêm trọng. Một trang ghi sinh thường 15&ndash;25 triệu, trang khác ghi 50&ndash;70 triệu &mdash; chênh nhau ba lần cho cùng một dịch vụ, cùng một bệnh viện. Đăng lại con số nào cũng là đánh cược bằng ngân sách của bạn."),
   ("Điểm mạnh thật của Vinmec nằm ở danh sách bảo lãnh",
    "35 đối tác bảo lãnh viện phí trực tiếp, gồm cả PVI (mà Tâm Anh TP.HCM đã dừng), International SOS, Allianz Partners, Liberty, Pacific Cross, AIA, Bảo Việt, Generali, Dai-ichi. Nếu thẻ bảo hiểm của bạn nằm trong danh sách này, phần bạn thực trả có thể thấp hơn nhiều so với giá niêm yết."),
   ("Chi nhánh tỉnh rẻ hơn đáng kể",
    "Theo nguồn tham khảo, Vinmec ở Hải Phòng, Nha Trang, Đà Nẵng, Hạ Long, Phú Quốc có giá thấp hơn Times City và Central Park khoảng 30&ndash;40%. Nếu bạn linh hoạt được về địa điểm, đây là khoản tiết kiệm lớn."),
   ("Bảo hiểm y tế: hưởng theo khung giá bệnh viện công",
    "Vinmec có hợp đồng BHYT tại Times City, Central Park, Smart City, Đà Nẵng, Nha Trang, Hải Phòng, Hạ Long, Phú Quốc, Cần Thơ. Nhưng như mọi bệnh viện tư, bạn tự trả phần chênh giữa giá Vinmec và mức BHYT chi trả &mdash; phần chênh này là phần lớn."),
 ],

 "faq": [
   ("Sinh ở Vinmec hết bao nhiêu tiền?",
    "Vinmec không công bố giá công khai nên không có câu trả lời chắc chắn. Theo các nguồn tham khảo bên thứ ba (chưa được Vinmec xác nhận), sinh thường tại Times City hoặc Central Park khoảng 37&ndash;52 triệu, sinh mổ lần 1 khoảng 52&ndash;65 triệu, tuỳ tuần đăng ký gói. Chi nhánh tỉnh thấp hơn nhiều. Bắt buộc gọi hotline 024 3975 6789 để có giá chính xác."),
   ("Vì sao không tìm thấy bảng giá thai sản Vinmec ở đâu cả?",
    "Vì Vinmec không đăng số lên website. Trang &ldquo;Bảng giá dịch vụ thai sản trọn gói tại Vinmec&rdquo; chỉ có tiêu đề và hướng dẫn liên hệ. Các trang bảng giá cơ sở cũng chỉ ghi &ldquo;áp dụng bảng giá mới từ 14/10/2025&rdquo; mà không có con số nào."),
   ("Các bảng giá Vinmec trên mạng có tin được không?",
    "Nên rất thận trọng. Chúng tôi đã đối chiếu nhiều nguồn và thấy chúng chênh nhau tới hai, ba lần cho cùng một dịch vụ &mdash; có trang ghi sinh thường 15&ndash;25 triệu, trang khác ghi 50&ndash;70 triệu. Không nguồn nào trong số đó dẫn được bảng giá gốc của Vinmec."),
   ("Vinmec có giảm giá gói thai sản không?",
    "Có, và đây là thông tin chính thức từ Vinmec: giảm 10% cho gói 12, 22, 27, 36 tuần và gói chuyển dạ. Mua combo thai sản kết hợp vaccine và biobank được giảm thêm 1&ndash;2 triệu."),
   ("Đến viện lúc đã chuyển dạ mà chưa mua gói thì sao?",
    "Vinmec có &ldquo;gói chuyển dạ&rdquo; dành riêng cho trường hợp này &mdash; đây là thông tin bệnh viện xác nhận chính thức. Giá thì không công bố."),
   ("Bảo hiểm của tôi có bảo lãnh viện phí ở Vinmec không?",
    "Vinmec có 35 đối tác bảo lãnh, gồm hầu hết công ty lớn: Bảo Việt, PVI, Bảo Minh, AIA, Dai-ichi, Generali, PTI, PJICO, MIC, BIC, VBI, Pacific Cross, Liberty, International SOS, Allianz Partners. Đây là danh sách rộng hơn phần lớn bệnh viện khác."),
   ("Sinh ở Vinmec hay Tâm Anh đắt hơn?",
    "Với dữ liệu hiện có, Tâm Anh rẻ hơn khoảng 15&ndash;30% ở cùng mốc tuần đăng ký, rõ nhất ở sinh mổ tại TP.HCM. Nhưng phải nói thẳng: so sánh này lệch về chất lượng nguồn &mdash; số Tâm Anh là số chính thức bệnh viện đăng, còn số Vinmec chỉ là ước tính từ bên thứ ba."),
 ],
},

]
