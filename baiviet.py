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

# =====================================================================
{
 "slug": "chi-phi-dieu-tri-ung-thu",
 "cum": "D",
 "ngay_dang": "2026-09-04",
 "tag": "Chi phí thật",
 "doc": "9 phút đọc",
 "title": "Điều trị ung thư ở Việt Nam tốn bao nhiêu: vì sao không ai trả lời được, và con số đã đo được",
 "h1": "Chi phí điều trị ung thư ở Việt Nam",
 "desc": "Từ 01/01/2025 không còn bảng giá viện phí chung toàn quốc, mỗi bệnh viện tự định giá. Nhưng nghiên cứu bình duyệt đã đo được phần gia đình tự trả và tỷ lệ hộ kiệt quệ tài chính.",
 "tom_tat": "Có một nghiên cứu bình duyệt theo dõi 1.141 bệnh nhân ung thư suốt 12 tháng ở Bạch Mai, Bệnh viện K và Bệnh viện Ung Bướu TP.HCM. Tiền túi mỗi gia đình bỏ ra trung bình 43,8 triệu đồng một năm, <b>82,6%</b> hộ rơi vào chi phí thảm hoạ. Dữ liệu thu thập giai đoạn 2011&ndash;2013, nên con số tuyệt đối đã cũ, phần còn dùng được là tỷ lệ. Còn câu hỏi một ca hoá trị hết bao nhiêu thì hiện không ai trả lời chung được, vì từ 01/01/2025 mỗi bệnh viện tự định giá.",
 "canh_bao": "Bài này không có bảng giá hoá trị, xạ trị hay phẫu thuật, vì không tồn tại một bảng giá chung hiện hành để dẫn. Thông tư 22/2023/TT-BYT từng quy định giá dịch vụ khám chữa bệnh BHYT toàn quốc đã <b>hết hiệu lực ngày 31/12/2024</b>. Từ 01/01/2025, mỗi bệnh viện tự xây giá theo phương pháp tại Thông tư 21/2024/TT-BYT. Chúng tôi đăng phần đo được và nói rõ phần không có.",

 "bang": [
   {"ten": "Gánh nặng tài chính, đo trên 1.141 bệnh nhân trong 12 tháng",
    "kiem_chung": "chinh-thuc",
    "nguon": "Hoang Van Minh và cộng sự, 2017, <i>BioMed Research International</i>, DOI 10.1155/2017/9350147. Nghiên cứu theo dõi dọc tại Bệnh viện Bạch Mai, Bệnh viện K và Bệnh viện Ung Bướu TP.HCM. Dữ liệu thu thập giai đoạn 2011&ndash;2013.",
    "cot": ["Chỉ số", "Kết quả"],
    "hang": [
      ["Chi tiền túi trung bình trong 12 tháng", "<b>43,8 triệu đồng</b>"],
      ["Chi tiền túi trung vị", "33,4 triệu đồng"],
      ["Hộ rơi vào chi phí thảm hoạ (ngưỡng 20% thu nhập hộ)", "<b>82,6%</b>"],
      ["Hộ rơi vào chi phí thảm hoạ (ngưỡng 50% thu nhập hộ)", "56,9%"],
      ["Hộ bị đẩy xuống dưới chuẩn nghèo", "<b>37,4%</b>"],
    ]},
   {"ten": "Giá ngày giường và khám bệnh theo khung BHYT cũ",
    "kiem_chung": "chinh-thuc",
    "nguon": "Thông tư 22/2023/TT-BYT, Bộ Y tế, ban hành 17/11/2023. <b>Đã hết hiệu lực ngày 31/12/2024.</b> Đăng ở đây làm mốc tham chiếu, không phải giá hiện hành.",
    "cot": ["Dịch vụ", "Mức BHYT theo khung cũ"],
    "hang": [
      ["Khám bệnh, bệnh viện hạng đặc biệt và hạng I", "42.100đ"],
      ["Khám bệnh, hạng II", "37.500đ"],
      ["Khám bệnh, hạng III / hạng IV", "33.200đ / 30.100đ"],
      ["Ngày giường hồi sức tích cực, hạng đặc biệt và hạng I", "<b>867.500đ/ngày</b>"],
      ["Ngày giường hồi sức tích cực, hạng II", "786.300đ/ngày"],
      ["Ngày giường hồi sức tích cực, hạng III", "673.900đ/ngày"],
      ["Ngày giường hồi sức cấp cứu", "279.400 &ndash; 509.400đ/ngày"],
      ["Ngày giường nội trú loại 1", "176.900 &ndash; 273.100đ/ngày"],
    ]},
   {"ten": "Cách tính ngày giường theo khung cũ, chỗ dễ hiểu nhầm nhất khi quyết toán",
    "kiem_chung": "chinh-thuc",
    "nguon": "Thông tư 22/2023/TT-BYT, phần quy định chung về thanh toán ngày giường. <b>Đã hết hiệu lực ngày 31/12/2024.</b> Cách tính này chỉ còn là mốc tham chiếu, phải hỏi lại quy định hiện hành của bệnh viện.",
    "cot": ["Tình huống", "Cách tính"],
    "hang": [
      ["Số ngày giường", "ngày ra viện trừ ngày vào viện, <b>cộng thêm 1</b>"],
      ["Nằm ghép 2 người một giường", "thanh toán <b>50%</b> giá ngày giường"],
      ["Nằm ghép từ 3 người trở lên", "thanh toán <b>33%</b>"],
      ["Khám chuyên khoa thứ hai trở đi trong cùng ngày", "tính <b>30%</b> giá khám, tối đa 2 lần"],
    ]},
   {"ten": "Số liệu khu vực Đông Nam Á &mdash; không tách riêng được Việt Nam",
    "kiem_chung": "thu-cap",
    "nguon": "ACTION Study Group, 2015, <i>BMC Medicine</i>, DOI 10.1186/s12916-015-0433-1. Nghiên cứu 8 nước Đông Nam Á, 9.513 bệnh nhân. Bài gốc không bóc tách riêng số của Việt Nam, nên đây là số toàn vùng.",
    "cot": ["Sau 12 tháng kể từ chẩn đoán", "Tỷ lệ toàn vùng"],
    "hang": [
      ["Tử vong", "29%"],
      ["Người còn sống rơi vào chi phí thảm hoạ", "48%"],
      ["Hoặc tử vong, hoặc kiệt quệ tài chính", "<b>hơn 75%</b>"],
      ["Định nghĩa chi phí thảm hoạ dùng trong nghiên cứu", "chi tiền túi y tế vượt 30% thu nhập hộ trong năm"],
    ]},
 ],

 "y_chinh": [
   ("Vì sao không có bảng giá điều trị ung thư toàn quốc",
    "Trước đây Thông tư 22/2023/TT-BYT quy định một khung giá dịch vụ khám chữa bệnh BHYT áp chung. Thông tư đó hết hiệu lực ngày 31/12/2024. Từ 01/01/2025, mỗi bệnh viện tự xây giá dịch vụ của mình theo phương pháp định giá tại Thông tư 21/2024/TT-BYT. Nghĩa là giá một ca xạ trị ở Bệnh viện K và ở Bệnh viện Ung Bướu TP.HCM có thể khác nhau, và cả hai đều đúng luật. Ai đưa cho bạn một con số &ldquo;giá xạ trị ở Việt Nam năm 2026&rdquo; mà không nói bệnh viện nào thì con số đó không có nghĩa."),
   ("Con số 43,8 triệu là tiền túi, không phải tổng viện phí",
    "Đây là phần gia đình tự bỏ ra sau khi bảo hiểm y tế đã chi trả, cộng cả chi phí y tế lẫn chi phí phi y tế như đi lại, ăn ở của người nhà, thu nhập mất đi. Tổng viện phí lớn hơn con số này. Nhưng với người lập ngân sách, phần tiền túi mới là phần phải lo."),
   ("Vì sao 82,6% là con số cần chú ý hơn 43,8 triệu",
    "Chi phí thảm hoạ là khoản chi y tế vượt quá một tỷ lệ nhất định trong thu nhập hộ gia đình, ở đây lấy mốc 20%. Tỷ lệ 82,6% có nghĩa là với phần lớn hộ có người mắc ung thư, khoản chi này nằm ngoài khả năng chi trả thông thường. Trung bình 43,8 triệu nghe còn xoay được. Nhưng 37,4% hộ bị đẩy xuống dưới chuẩn nghèo thì cho thấy đa số không xoay nổi."),
   ("Dữ liệu đã cũ, và điều đó cần nói ra",
    "Nghiên cứu công bố năm 2017 nhưng dữ liệu thu thập giai đoạn 2011 đến 2013. Từ đó tới nay chi phí y tế đã tăng, phác đồ điều trị đã đổi, danh mục thuốc BHYT đã mở rộng. Con số tuyệt đối 43,8 triệu chắc chắn không còn đúng cho năm 2026. Cái còn giá trị là tỷ lệ và cấu trúc: phần lớn hộ gia đình rơi vào chi phí thảm hoạ, và hơn một phần ba bị đẩy xuống dưới chuẩn nghèo."),
   ("Thuốc đích và thuốc miễn dịch là khoản chúng tôi chưa xác minh được",
    "Đây thường là khoản đắt nhất trong điều trị ung thư hiện đại, và cũng là khoản hay bị hiểu nhầm nhất. Cơ chế thì rõ: danh mục thuốc BHYT có cột tỷ lệ thanh toán, tức có thuốc BHYT trả 100%, có thuốc chỉ trả một phần. Nhưng từng hoạt chất cụ thể được trả bao nhiêu thì nằm trong phụ lục danh mục thuốc, và chúng tôi chưa đọc được bản đầy đủ. Vì vậy bài này không đưa con số nào cho nhóm thuốc đó."),
   ("Điều nên hỏi bệnh viện trước khi bắt đầu phác đồ",
    "Một: phác đồ dự kiến gồm bao nhiêu chu kỳ, mỗi chu kỳ chi phí ước tính bao nhiêu tại chính bệnh viện này. Hai: thuốc trong phác đồ có nằm trong danh mục BHYT không, tỷ lệ thanh toán bao nhiêu phần trăm. Ba: nếu phải nằm hồi sức tích cực thì giá ngày giường ở đây là bao nhiêu. Ba câu này quyết định phần lớn ngân sách, và chỉ bệnh viện điều trị mới trả lời được."),
 ],

 "khong_ro": [
   "Giá hoá trị, xạ trị và phẫu thuật khối u. Các mã này nằm ở phụ lục của thông tư và ở bảng giá riêng từng bệnh viện. Bản HTML của thông tư không hiển thị phụ lục. Website Bệnh viện K chặn ở tầng chứng chỉ nên không mở được; bốn file bảng giá của Bệnh viện Ung Bướu TP.HCM đặt trên Google Drive và bị chặn tải.",
   "Tỷ lệ BHYT chi trả cho từng thuốc đích và thuốc miễn dịch. Chúng tôi xác nhận được cơ chế tỷ lệ thanh toán tồn tại trong quy định, nhưng chưa đọc được phụ lục danh mục để biết từng hoạt chất được trả bao nhiêu.",
   "Giá dịch vụ ung bướu hiện hành của từng bệnh viện sau ngày 01/01/2025. Mỗi bệnh viện tự công bố, chúng tôi chưa mở được bảng nào.",
   "Số liệu Việt Nam tách riêng trong nghiên cứu ACTION 2015. Bài gốc chỉ báo cáo số toàn vùng tám nước.",
   "Chi phí điều trị theo từng loại ung thư và từng giai đoạn. Nghiên cứu 2017 báo cáo số gộp, không tách theo bệnh.",
 ],

 "faq": [
   ("Điều trị ung thư ở Việt Nam hết bao nhiêu tiền?",
    "Không có con số chung. Từ 01/01/2025 mỗi bệnh viện tự định giá dịch vụ theo Thông tư 21/2024/TT-BYT, nên không tồn tại bảng giá toàn quốc. Cái đo được là phần tiền túi gia đình bỏ ra: trung bình 43,8 triệu đồng trong 12 tháng, theo nghiên cứu trên 1.141 bệnh nhân tại Bạch Mai, Bệnh viện K và Bệnh viện Ung Bướu TP.HCM. Dữ liệu thu thập giai đoạn 2011 đến 2013 nên con số tuyệt đối này không còn đúng cho năm 2026, chỉ dùng để thấy quy mô."),
   ("Bảo hiểm y tế chi trả bao nhiêu khi điều trị ung thư?",
    "Tuỳ dịch vụ và tuỳ thuốc. Với dịch vụ kỹ thuật, BHYT thanh toán theo mức hưởng của thẻ và theo giá bệnh viện công bố. Với thuốc, danh mục BHYT có cột tỷ lệ thanh toán, có thuốc trả đủ, có thuốc chỉ trả một phần. Chúng tôi chưa đọc được phụ lục danh mục nên không đưa tỷ lệ cụ thể cho từng thuốc."),
   ("Chi phí thảm hoạ nghĩa là gì?",
    "Là khoản chi y tế tiền túi vượt quá một tỷ lệ nhất định trong thu nhập hộ gia đình trong năm. Nghiên cứu năm 2017 dùng hai ngưỡng 20% và 50%, cho kết quả 82,6% và 56,9%. Nghiên cứu ACTION dùng ngưỡng 30% thu nhập năm."),
   ("Ngày giường hồi sức tích cực bao nhiêu một ngày?",
    "Theo khung BHYT cũ tại Thông tư 22/2023/TT-BYT: 867.500đ mỗi ngày ở bệnh viện hạng đặc biệt và hạng I, 786.300đ ở hạng II, 673.900đ ở hạng III. Khung này đã hết hiệu lực từ 31/12/2024, nên chỉ dùng làm mốc tham chiếu, phải hỏi lại giá hiện hành của bệnh viện."),
   ("Vì sao bài này ít con số hơn các trang khác?",
    "Vì phần lớn con số đang lan truyền không dẫn được nguồn hiện hành. Khung giá chung đã hết hiệu lực gần hai năm, mà nhiều bài vẫn đăng lại như giá 2026. Chúng tôi đăng đúng phần kiểm chứng được và ghi rõ phần chưa đọc được."),
 ],
},

# =====================================================================
{
 "slug": "ly-do-ho-so-bi-tu-choi-boi-thuong",
 "cum": "C",
 "ngay_dang": "2026-09-04",
 "tag": "Bồi thường",
 "doc": "10 phút đọc",
 "title": "Hồ sơ bảo hiểm bị từ chối bồi thường: mười ba lý do, và điều luật tương ứng cho từng lý do",
 "h1": "Vì sao hồ sơ bị từ chối bồi thường",
 "desc": "Mỗi lý do từ chối đều gắn với một điều trong Luật Kinh doanh bảo hiểm 2022. Biết điều luật nào áp cho trường hợp của mình là bước đầu tiên để biết mình có cãi được không.",
 "tom_tat": "Doanh nghiệp bảo hiểm không được từ chối tuỳ ý. Mỗi lý do từ chối hợp lệ đều phải dựa vào một điều cụ thể trong <b>Luật Kinh doanh bảo hiểm số 08/2022/QH15</b>, hiệu lực từ 01/01/2023. Bài này liệt kê mười ba lý do thường gặp, kèm điều luật và trích nguyên văn. Vài trường hợp trong đó, luật đứng về phía người mua rõ hơn nhiều người vẫn nghĩ.",

 "bang": [
   {"ten": "Mười ba lý do từ chối và điều luật tương ứng",
    "kiem_chung": "chinh-thuc",
    "nguon": "Luật Kinh doanh bảo hiểm số 08/2022/QH15, Quốc hội thông qua 16/06/2022, hiệu lực 01/01/2023. Trích rút gọn, giữ nguyên từ ngữ của luật.",
    "cot": ["Tình huống", "Điều luật", "Nội dung luật"],
    "hang": [
      ["Khai không trung thực khi ký hợp đồng", "Điều 22 khoản 2",
       "Áp dụng khi bên mua <b>cố ý</b> cung cấp thông tin sai <b>nhằm giao kết hợp đồng để được bồi thường</b>. Doanh nghiệp có quyền huỷ hợp đồng và phải hoàn lại phí sau khi trừ chi phí hợp lý."],
      ["Rơi vào điều khoản loại trừ", "Điều 20 khoản 1 điểm d",
       "Được từ chối nếu không thuộc phạm vi trách nhiệm bảo hiểm hoặc thuộc trường hợp loại trừ <b>theo thoả thuận trong hợp đồng</b>."],
      ["Hãng chưa từng giải thích điều khoản loại trừ", "Điều 19 khoản 2",
       "Doanh nghiệp phải giải thích rõ ràng, đầy đủ và <b>có bằng chứng xác nhận</b> bên mua đã được giải thích và hiểu rõ khi giao kết."],
      ["Lấy lý do bạn báo chậm", "Điều 19 khoản 3",
       "Nếu có bất khả kháng hoặc trở ngại khách quan thì <b>không được áp dụng</b> điều khoản loại trừ về việc chậm thông báo."],
      ["Điều khoản mập mờ, hai bên hiểu khác nhau", "Điều 24",
       "Điều khoản không rõ ràng dẫn đến cách hiểu khác nhau thì được giải thích <b>theo hướng có lợi cho bên mua bảo hiểm</b>."],
      ["Hợp đồng bị tuyên vô hiệu", "Điều 25 khoản 1",
       "Có 11 trường hợp, trong đó có: không có quyền lợi có thể được bảo hiểm; bên mua <b>biết sự kiện bảo hiểm đã xảy ra</b>; giả tạo; lừa dối; đe doạ, cưỡng ép. Hậu quả là hai bên hoàn trả cho nhau những gì đã nhận."],
      ["Hãng đơn phương chấm dứt hợp đồng", "Điều 26",
       "Danh sách <b>đóng</b>, chỉ 4 trường hợp: không đóng đủ phí sau thời gian gia hạn; không chấp nhận thay đổi mức độ rủi ro; không bảo đảm an toàn; không đồng ý chuyển giao danh mục."],
      ["Nợ phí nhưng sự kiện đã xảy ra trước khi chấm dứt", "Điều 27 khoản 1 điểm b",
       "Doanh nghiệp <b>vẫn có trách nhiệm trả tiền bảo hiểm</b> nếu sự kiện xảy ra trước thời điểm đơn phương chấm dứt, và được khấu trừ phí còn thiếu."],
      ["Nộp hồ sơ quá hạn", "Điều 30 khoản 1 và 2",
       "Thời hạn nộp yêu cầu bồi thường là <b>01 năm</b> kể từ ngày xảy ra sự kiện. Thời gian bất khả kháng hoặc trở ngại khách quan không tính vào. Khoản 2 tính từ ngày bên mua <b>biết</b> sự kiện."],
      ["Hãng kéo dài, không trả lời", "Điều 31",
       "Không có thoả thuận khác thì phải trả trong <b>15 ngày</b> kể từ ngày nhận đủ hồ sơ hợp lệ. Chậm thì <b>phải trả lãi</b> trên số tiền chậm trả."],
      ["Từ chối miệng, không nêu lý do", "Điều 20 khoản 2 điểm e",
       "Doanh nghiệp có nghĩa vụ <b>giải thích bằng văn bản</b> lý do từ chối bồi thường."],
      ["Đổ lỗi cho nhà tái bảo hiểm", "Điều 29 khoản 1",
       "Doanh nghiệp chịu trách nhiệm <b>duy nhất</b> với bên mua, <b>không được từ chối hoặc trì hoãn</b> kể cả khi bên nhận tái bảo hiểm không thực hiện nghĩa vụ."],
      ["Muốn rút trong thời gian cân nhắc", "Điều 35",
       "Với hợp đồng thời hạn <b>trên 01 năm</b>, trong <b>21 ngày kể từ ngày nhận được hợp đồng</b>, bên mua có quyền từ chối tiếp tục tham gia."],
    ]},
   {"ten": "Hai mốc thời gian rất hay bị lẫn",
    "kiem_chung": "chinh-thuc",
    "nguon": "Luật Kinh doanh bảo hiểm 2022 và Bộ luật Dân sự 2015",
    "cot": ["Việc cần làm", "Thời hạn", "Căn cứ"],
    "hang": [
      ["Nộp hồ sơ yêu cầu bồi thường cho doanh nghiệp bảo hiểm", "<b>01 năm</b> kể từ ngày xảy ra sự kiện", "Điều 30 Luật Kinh doanh bảo hiểm 2022"],
      ["Khởi kiện ra toà về hợp đồng bảo hiểm", "<b>03 năm</b>", "Điều 429 Bộ luật Dân sự 2015"],
      ["Doanh nghiệp phải trả tiền sau khi nhận đủ hồ sơ", "15 ngày", "Điều 31 Luật Kinh doanh bảo hiểm 2022"],
      ["Từ chối tiếp tục tham gia hợp đồng trên 1 năm", "21 ngày từ ngày nhận hợp đồng", "Điều 35 Luật Kinh doanh bảo hiểm 2022"],
    ]},
 ],

 "y_chinh": [
   ("Chữ quan trọng nhất trong Điều 22 là chữ &ldquo;cố ý&rdquo;",
    "Điều 22 khoản 2 chỉ cho phép huỷ hợp đồng khi bên mua <b>cố ý</b> cung cấp thông tin sai <b>nhằm mục đích được bồi thường</b>. Quên một lần khám cách đây nhiều năm, hoặc không biết mình có bệnh, về mặt câu chữ không phải là cố ý nhằm trục lợi. Ranh giới này là chỗ tranh chấp nhiều nhất trong thực tế, và cũng là lý do hồ sơ bệnh án cũ quan trọng đến thế."),
   ("Nghĩa vụ chứng minh đã giải thích thuộc về doanh nghiệp",
    "Điều 19 khoản 2 không chỉ yêu cầu doanh nghiệp giải thích, mà yêu cầu <b>có bằng chứng xác nhận</b> bên mua đã hiểu rõ điều khoản loại trừ. Nếu bạn bị từ chối vì một điều khoản loại trừ mà chưa từng được giải thích, câu hỏi ngược lại là bằng chứng đó đâu."),
   ("Điều 24 là điều nhiều người không biết mình có",
    "Khi một điều khoản có thể hiểu theo hai cách, luật buộc phải hiểu theo hướng có lợi cho bên mua. Đây không phải thiện chí của doanh nghiệp mà là quy định. Trong tranh chấp về từ ngữ hợp đồng, đây thường là căn cứ mạnh nhất của người mua."),
   ("Danh sách được đơn phương chấm dứt là danh sách đóng",
    "Điều 26 liệt kê đúng bốn trường hợp. Ngoài bốn trường hợp đó, doanh nghiệp không có quyền đơn phương chấm dứt hợp đồng. Nếu nhận được thông báo chấm dứt, việc đầu tiên nên làm là đối chiếu lý do trong thông báo với bốn trường hợp này."),
   ("Nợ phí không xoá trách nhiệm với sự kiện đã xảy ra trước đó",
    "Điều 27 khoản 1 điểm b nói rõ: sự kiện bảo hiểm xảy ra trước thời điểm đơn phương chấm dứt thì doanh nghiệp vẫn phải trả tiền, và chỉ được khấu trừ phần phí còn thiếu. Đây là tình huống hay bị hiểu ngược."),
   ("Từ chối phải bằng văn bản, và phải nêu lý do",
    "Điều 20 khoản 2 điểm e đặt đây là nghĩa vụ của doanh nghiệp. Một cuộc gọi báo &ldquo;hồ sơ không được duyệt&rdquo; không phải là từ chối hợp lệ. Hãy yêu cầu văn bản, vì văn bản đó là thứ bạn cần khi khiếu nại hoặc khởi kiện."),
   ("Đừng lẫn một năm với ba năm",
    "Một năm là thời hạn nộp hồ sơ cho doanh nghiệp bảo hiểm, theo Điều 30. Ba năm là thời hiệu khởi kiện ra toà, theo Điều 429 Bộ luật Dân sự 2015. Luật Kinh doanh bảo hiểm 2022 không có điều riêng về thời hiệu khởi kiện, nên nhiều bài viết dẫn nhầm sang điều của luật cũ năm 2000 đã hết hiệu lực."),
 ],

 "khong_ro": [
   "Thế nào là hồ sơ hợp lệ. Mốc 15 ngày ở Điều 31 tính từ ngày nhận đủ hồ sơ hợp lệ, nhưng luật không định nghĩa hợp lệ gồm những gì.",
   "Số lần và thời hạn yêu cầu bổ sung hồ sơ. Luật không giới hạn, nên việc yêu cầu bổ sung nhiều lần có thể kéo dài mà vẫn đúng luật.",
   "Thời hạn tối đa cho việc thẩm định và xác minh hồ sơ.",
   "Nội dung tối thiểu của văn bản từ chối. Luật buộc phải giải thích bằng văn bản nhưng không quy định văn bản đó phải dẫn điều khoản nào và phải gửi trong bao lâu.",
   "Mức trần của &ldquo;chi phí hợp lý&rdquo; được trừ khi hoàn phí, ở Điều 22 và Điều 35. Luật để hợp đồng tự thoả thuận.",
   "Mức lãi suất chậm trả ở Điều 31 khoản 2. Luật chỉ dẫn sang Bộ luật Dân sự, không ấn định con số.",
   "Loại bằng chứng nào được chấp nhận để chứng minh khách hàng đã hiểu điều khoản loại trừ.",
   "Không có cơ quan tài phán chuyên trách cho tranh chấp bảo hiểm, cũng không có thủ tục khiếu nại bắt buộc trước khi khởi kiện.",
   "Số liệu về tỷ lệ từ chối bồi thường trên thị trường. Chúng tôi không tìm thấy thống kê công khai chính thức nào. Vì vậy bài này không đưa ra bất kỳ con số phần trăm nào về chuyện đó.",
 ],

 "faq": [
   ("Bị từ chối bồi thường thì làm gì đầu tiên?",
    "Yêu cầu văn bản nêu rõ lý do từ chối. Điều 20 khoản 2 điểm e của Luật Kinh doanh bảo hiểm 2022 quy định doanh nghiệp phải giải thích bằng văn bản. Có văn bản rồi mới đối chiếu được lý do đó với điều khoản trong hợp đồng và với luật."),
   ("Khai thiếu bệnh cũ thì chắc chắn mất quyền lợi?",
    "Không chắc chắn. Điều 22 khoản 2 chỉ áp dụng khi bên mua cố ý cung cấp thông tin sai nhằm mục đích được bồi thường. Quên hoặc không biết là tình huống khác về mặt câu chữ của luật, và trên thực tế đây là chỗ tranh chấp nhiều nhất."),
   ("Nộp hồ sơ trễ bao lâu thì mất quyền?",
    "Thời hạn là 01 năm kể từ ngày xảy ra sự kiện bảo hiểm, theo Điều 30. Thời gian xảy ra bất khả kháng hoặc trở ngại khách quan không tính vào thời hạn này. Riêng thời hiệu khởi kiện ra toà là 03 năm, theo Điều 429 Bộ luật Dân sự 2015."),
   ("Hãng bảo chờ tái bảo hiểm duyệt thì sao?",
    "Điều 29 khoản 1 quy định doanh nghiệp bảo hiểm chịu trách nhiệm duy nhất với bên mua và không được từ chối hoặc trì hoãn, kể cả khi bên nhận tái bảo hiểm không thực hiện nghĩa vụ. Quan hệ giữa doanh nghiệp và nhà tái bảo hiểm không phải việc của người mua."),
   ("Hợp đồng đã ký rồi có rút được không?",
    "Với hợp đồng thời hạn trên 01 năm, Điều 35 cho quyền từ chối tiếp tục tham gia trong 21 ngày kể từ ngày nhận được hợp đồng. Doanh nghiệp hoàn lại phí sau khi trừ chi phí hợp lý. Lưu ý mốc 21 ngày tính từ ngày nhận hợp đồng, không phải ngày ký đơn yêu cầu."),
   ("Bài này có nói hãng nào hay từ chối hơn hãng nào không?",
    "Không. Chúng tôi không tìm thấy thống kê công khai chính thức về tỷ lệ từ chối theo từng doanh nghiệp, nên mọi so sánh kiểu đó đều không có căn cứ. Bài này nói về luật, áp dụng như nhau cho mọi doanh nghiệp bảo hiểm."),
 ],
},

# =====================================================================
{
 "slug": "chi-phi-dieu-tri-dot-quy",
 "cum": "D",
 "ngay_dang": "2026-09-06",
 "tag": "Chi phí thật",
 "doc": "8 phút đọc",
 "title": "Chi phí điều trị đột quỵ ở Việt Nam: số đo được tại từng bệnh viện, và phần chưa ai đo",
 "h1": "Chi phí điều trị đột quỵ ở Việt Nam",
 "desc": "Không có bảng giá điều trị đột quỵ chung toàn quốc từ 01/01/2025. Đây là số thật đo tại Bạch Mai năm 2021 và Thống Nhất Đồng Nai năm 2024, kèm phần chúng tôi chưa tìm được số đáng tin.",
 "tom_tat": "Trung tâm Thần kinh Bệnh viện Bạch Mai có một nghiên cứu trên 500 bệnh nhân nhồi máu não, dữ liệu thu nửa cuối năm 2021. Chi phí trực tiếp một đợt nội trú trung bình <b>10,5 triệu đồng</b>, nhưng dao động từ 3,3 đến 39,8 triệu. Riêng thuốc tiêu sợi huyết, ở nhóm phải dùng, trung bình 17,2 triệu, tức là một mình nó đã đắt hơn cả đợt nằm viện trung bình.",
 "canh_bao": "Bài này không có bảng giá điều trị đột quỵ áp chung toàn quốc, vì từ 01/01/2025 không còn thứ đó. Thông tư 22/2023/TT-BYT từng quy định khung giá dịch vụ khám chữa bệnh BHYT toàn quốc đã hết hiệu lực ngày 31/12/2024; từ 01/01/2025 mỗi bệnh viện tự xây giá theo Thông tư 21/2024/TT-BYT. Số trong bài là số đo tại từng bệnh viện cụ thể, kèm năm thu dữ liệu. Đọc kèm cả hai thông tin đó, đừng tách con số ra khỏi bệnh viện và năm.",

 "bang": [
   {"ten": "Chi phí trực tiếp một đợt nội trú, đo trên 500 bệnh nhân nhồi máu não",
    "kiem_chung": "chinh-thuc",
    "nguon": "Nghiên cứu tại Trung tâm Thần kinh, Bệnh viện Bạch Mai, đăng trên Tạp chí Y học Việt Nam. Dữ liệu thu từ 01/07 đến 31/12/2021, cỡ mẫu 500 bệnh nhân. Đơn vị gốc của nghiên cứu là nghìn đồng, chúng tôi quy về triệu đồng để dễ đọc. Bốn khoản mục dưới đây là các khoản nghiên cứu tách riêng, cộng lại chưa bằng tổng chi phí trực tiếp.",
    "cot": ["Khoản mục", "Trung bình một đợt nội trú"],
    "hang": [
      ["Tổng chi phí trực tiếp", "<b>10,5 triệu đồng</b> (độ lệch chuẩn 7,3 triệu)"],
      ["Khoảng dao động", "3,3 &ndash; 39,8 triệu đồng"],
      ["Tiền giường", "3,64 triệu (lệch chuẩn 2,98 triệu)"],
      ["Thuốc", "2,84 triệu (lệch chuẩn 3,04 triệu)"],
      ["Chẩn đoán hình ảnh", "1,50 triệu (lệch chuẩn 1,22 triệu)"],
      ["Vật tư y tế", "0,118 triệu (lệch chuẩn 0,077 triệu)"],
    ]},
   {"ten": "Thuốc tiêu sợi huyết, khoản đắt nhất khi phải dùng",
    "kiem_chung": "chinh-thuc",
    "nguon": "Cùng nghiên cứu Bạch Mai, dữ liệu 2021. Đây là chi phí riêng của thuốc tiêu sợi huyết ở nhóm bệnh nhân được chỉ định, không phải mọi bệnh nhân đều dùng.",
    "cot": ["Khoản mục", "Trung bình"],
    "hang": [
      ["Thuốc tiêu sợi huyết", "17,2 triệu đồng (độ lệch chuẩn 5,96 triệu)"],
      ["So với tổng một đợt nội trú trung bình", "cao hơn khoảng 6,7 triệu"],
    ]},
   {"ten": "Chi phí ngoại trú và tỷ lệ BHYT chi trả",
    "kiem_chung": "chinh-thuc",
    "nguon": "Nghiên cứu tại Bệnh viện Đa khoa Thống Nhất, Đồng Nai, đăng trên Tạp chí Y học Việt Nam. Dữ liệu năm 2024, cỡ mẫu 1.903 bệnh nhân với 9.051 lượt khám.",
    "cot": ["Chỉ số", "Kết quả"],
    "hang": [
      ["Chi phí y tế trực tiếp mỗi đợt ngoại trú", "470.627đ (khoảng tin cậy 95%: 456.949 &ndash; 484.305đ)"],
      ["Phần BHYT chi trả", "89,5%"],
      ["Phần người bệnh tự trả", "<b>10,5%</b>"],
    ]},
   {"ten": "Quy mô đột quỵ ở Việt Nam",
    "kiem_chung": "thu-cap",
    "nguon": "Phát biểu của Thứ trưởng Bộ Y tế Trần Văn Thuấn tại hội nghị đột quỵ ngày 24/07/2025, VnExpress đưa tin cùng ngày. Đây là số nêu trong phát biểu, không kèm công bố nghiên cứu, nên chúng tôi gắn nhãn thứ cấp.",
    "cot": ["Chỉ số", "Con số nêu trong phát biểu"],
    "hang": [
      ["Tỷ lệ hiện mắc", "1.541 trên 100.000 dân"],
      ["Mới mắc mỗi năm", "khoảng 222 trên 100.000 dân"],
      ["Mất khả năng lao động sau điều trị", "<b>71%</b>"],
      ["Số cơ sở điều trị đột quỵ", "12 cơ sở năm 2016, hơn 150 cơ sở năm 2025"],
    ]},
 ],

 "y_chinh": [
   ("Vì sao không có bảng giá điều trị đột quỵ cho năm 2026",
    "Thông tư 22/2023/TT-BYT từng đặt một khung giá dịch vụ khám chữa bệnh BHYT áp chung cả nước. Thông tư đó hết hiệu lực ngày 31/12/2024. Từ 01/01/2025, mỗi bệnh viện tự xây giá dịch vụ theo phương pháp định giá tại Thông tư 21/2024/TT-BYT. Nghĩa là cùng một ca can thiệp, giá ở Bạch Mai và ở một bệnh viện tỉnh có thể khác nhau, và cả hai đều đúng luật. Trang nào đưa cho bạn một con số giá điều trị đột quỵ ở Việt Nam năm 2026 mà không nói bệnh viện nào thì con số đó không kiểm chứng được."),
   ("Con số 10,5 triệu là chi phí trực tiếp, không phải toàn bộ gánh nặng",
    "Nghiên cứu Bạch Mai với dữ liệu nửa cuối năm 2021 đo chi phí trực tiếp của đợt điều trị nội trú, gồm giường, thuốc, chẩn đoán hình ảnh, vật tư và các khoản khác. Nó không tính tiền đi lại, ăn ở của người nhà, thu nhập mất đi trong thời gian nằm viện, và cũng không tính phục hồi chức năng sau khi ra viện. Vì vậy đừng đọc 10,5 triệu như tổng số tiền một gia đình phải bỏ ra."),
   ("Khoản đắt nhất là thứ bạn không chọn được",
    "Thuốc tiêu sợi huyết trung bình 17,2 triệu theo dữ liệu Bạch Mai năm 2021, đắt hơn cả một đợt nội trú trung bình. Có dùng hay không thì phụ thuộc bệnh nhân tới viện lúc nào và bác sĩ chỉ định thế nào, gia đình không quyết được. Vì vậy chi phí đột quỵ khó dự trù hơn nhiều loại bệnh khác. Hai người cùng chẩn đoán vẫn có thể chênh nhau hơn mười lần, từ 3,3 triệu tới 39,8 triệu, đúng bằng khoảng dao động nghiên cứu ghi nhận."),
   ("Tỷ lệ BHYT chi trả 89,5% là số của ngoại trú, tại một bệnh viện",
    "Con số này lấy từ nghiên cứu ở Bệnh viện Đa khoa Thống Nhất, Đồng Nai, năm 2024, và chỉ đo phần khám chữa ngoại trú. Đừng suy ra rằng nội trú cũng được trả 89,5%, và đừng suy ra rằng bệnh viện khác cũng vậy. Mức hưởng còn phụ thuộc loại thẻ, nơi đăng ký khám ban đầu và dịch vụ cụ thể."),
   ("Phần khiến bảo hiểm trở thành câu chuyện là hậu quả, không phải viện phí",
    "Theo phát biểu tại hội nghị đột quỵ tháng 07/2025, 71% người bệnh mất khả năng lao động sau điều trị. Nếu con số này gần đúng thì chi phí y tế của đợt cấp không phải phần nặng nhất. Phần nặng hơn là thu nhập dừng lại trong khi chi phí chăm sóc kéo dài. Đó là lý do các sản phẩm bảo vệ thu nhập và bệnh hiểm nghèo tồn tại, và cũng là phần chúng tôi không có số liệu Việt Nam để định lượng."),
   ("Ba câu nên hỏi bệnh viện khi người nhà bị đột quỵ",
    "Một: bệnh nhân có nằm trong cửa sổ điều trị để dùng tiêu sợi huyết hoặc can thiệp lấy huyết khối không, và nếu có thì chi phí tại chính bệnh viện này là bao nhiêu. Hai: thẻ BHYT của bệnh nhân được hưởng bao nhiêu phần trăm ở đây, khoản nào ngoài danh mục. Ba: sau giai đoạn cấp thì phục hồi chức năng ở đâu, kéo dài bao lâu, chi phí mỗi đợt bao nhiêu."),
 ],

 "khong_ro": [
   "Chi phí tiền túi của hộ gia đình có người bị đột quỵ. Không tìm được nghiên cứu Việt Nam nào đo riêng khoản này cho đột quỵ. Các nghiên cứu về chi tiêu y tế thảm hoạ ở Việt Nam đều đo y tế nói chung, không tách riêng đột quỵ, nên chúng tôi không mượn số của chúng.",
   "Chi phí phục hồi chức năng dài hạn tại Việt Nam. Có một nghiên cứu quốc tế đưa con số tổng khoảng 3.310 USD, nhưng chúng tôi chưa xác minh được nghiên cứu đó thực hiện tại Việt Nam nên không đăng.",
   "Cửa sổ giờ vàng theo hướng dẫn hiện hành. Nguồn Việt Nam chúng tôi mở được là bài từ năm 2017, nêu mốc 3 đến 6 giờ, đã lệch so với thực hành hiện nay. Chúng tôi không đăng mốc giờ vì đưa sai con số này nguy hiểm hơn là không đưa. Hãy hỏi trực tiếp cơ sở đột quỵ gần nhất.",
   "Tỷ lệ tàn tật sau đột quỵ có cỡ mẫu và phương pháp. Con số 71% đến từ một phát biểu tại hội nghị, không kèm công bố nghiên cứu.",
   "Chi phí điều trị đột quỵ hiện hành của từng bệnh viện sau ngày 01/01/2025. Mỗi bệnh viện tự công bố, chúng tôi chưa mở được bảng nào.",
   "Số liệu phân biệt nhồi máu não và xuất huyết não. Nghiên cứu Bạch Mai chúng tôi dùng chỉ đo nhóm nhồi máu não.",
 ],

 "faq": [
   ("Điều trị đột quỵ ở Việt Nam hết bao nhiêu tiền?",
    "Không có con số chung, vì từ 01/01/2025 mỗi bệnh viện tự định giá dịch vụ theo Thông tư 21/2024/TT-BYT. Số đo được cụ thể: tại Trung tâm Thần kinh Bệnh viện Bạch Mai, chi phí trực tiếp một đợt nội trú của bệnh nhân nhồi máu não trung bình 10,5 triệu đồng, dao động 3,3 đến 39,8 triệu, theo dữ liệu thu nửa cuối năm 2021 trên 500 bệnh nhân."),
   ("Vì sao chi phí đột quỵ chênh nhau tới hơn mười lần?",
    "Vì phụ thuộc bệnh nhân có phải dùng thuốc tiêu sợi huyết hay không, nằm viện bao lâu, và có phải vào hồi sức hay không. Riêng thuốc tiêu sợi huyết đã trung bình 17,2 triệu, cao hơn cả một đợt nội trú trung bình. Đây là số của nghiên cứu Bạch Mai với dữ liệu năm 2021."),
   ("Bảo hiểm y tế chi trả bao nhiêu khi điều trị đột quỵ?",
    "Tuỳ loại thẻ, nơi đăng ký khám ban đầu và dịch vụ cụ thể. Số đo được: tại Bệnh viện Đa khoa Thống Nhất Đồng Nai năm 2024, phần khám chữa ngoại trú được BHYT chi trả 89,5%, người bệnh tự trả 10,5%. Đây là số của riêng bệnh viện đó và riêng phần ngoại trú, không suy ra được cho nội trú hay bệnh viện khác."),
   ("Đột quỵ có để lại di chứng lâu dài không?",
    "Theo phát biểu của Thứ trưởng Bộ Y tế tại hội nghị đột quỵ ngày 24/07/2025, 71% người bệnh mất khả năng lao động sau điều trị. Đây là con số nêu trong phát biểu, không kèm công bố nghiên cứu, nên đọc như một chỉ dấu về quy mô chứ không phải số liệu đã bình duyệt."),
   ("Vì sao bài này không có bảng giá chi tiết như các trang khác?",
    "Vì bảng giá chung toàn quốc đã hết hiệu lực gần hai năm mà nhiều trang vẫn đăng lại như giá hiện hành. Chúng tôi chỉ đăng số đo được tại bệnh viện cụ thể, kèm năm thu dữ liệu, và ghi rõ những chỗ chưa tìm được số đáng tin."),
 ],
 "lien_quan": ["chi-phi-dieu-tri-ung-thu"],
},

# =====================================================================
{
 "slug": "benh-co-san-duoc-hieu-the-nao",
 "cum": "C",
 "ngay_dang": "2026-09-06",
 "tag": "Hợp đồng",
 "doc": "9 phút đọc",
 "title": "Bệnh có sẵn được hiểu thế nào: định nghĩa nằm ở Thông tư 67, không nằm ở Luật",
 "h1": "Bệnh có sẵn được hiểu thế nào",
 "desc": "Luật Kinh doanh bảo hiểm 2022 không có cụm từ bệnh có sẵn. Định nghĩa nằm ở Thông tư 67/2023/TT-BTC Điều 12, kèm bốn mốc thời gian doanh nghiệp không được vượt: 36 tháng, 90 ngày, 1 năm và 270 ngày.",
 "tom_tat": "Nhiều bài trên mạng nói định nghĩa bệnh có sẵn do từng công ty bảo hiểm tự đặt. Chỗ này đúng một nửa. Luật Kinh doanh bảo hiểm số 08/2022/QH15 không có cụm từ này, nhưng Thông tư 67/2023/TT-BTC thì có, ở Điều 12 khoản 3. Doanh nghiệp vẫn tự soạn quy tắc điều khoản, chỉ là phải nằm trong khung đó. Và khung đó đặt bốn mốc cứng: <b>36 tháng</b>, <b>90 ngày</b>, <b>1 năm</b>, <b>270 ngày</b>.",
 "canh_bao": "Bài này trích nguyên văn điều khoản và ghi rõ số điều, số khoản để bạn tự đối chiếu. Chúng tôi không đưa ra tư vấn pháp lý cho trường hợp cụ thể, và không so sánh sản phẩm của các công ty bảo hiểm.",

 "bang": [
   {"ten": "Các mốc thời gian Thông tư 67 đặt ra, doanh nghiệp không được vượt",
    "kiem_chung": "chinh-thuc",
    "nguon": "Thông tư 67/2023/TT-BTC, Điều 12 khoản 2 và khoản 3, Bộ Tài chính. Các mốc dưới đây là mức tối đa, hợp đồng có thể quy định ngắn hơn.",
    "cot": ["Mốc", "Con số", "Nằm ở đâu"],
    "hang": [
      ["Truy ngược dấu hiệu, triệu chứng để coi là bệnh có sẵn", "tối đa <b>36 tháng</b> trước ngày hiệu lực", "Điều 12 khoản 3 điểm a"],
      ["Thời gian chờ với các trường hợp bệnh", "tối đa <b>90 ngày</b>", "Điều 12 khoản 2 điểm c"],
      ["Thời gian chờ khi doanh nghiệp chấp thuận bảo hiểm cho bệnh có sẵn", "tối đa <b>1 năm</b>", "Điều 12 khoản 2 điểm c"],
      ["Thời gian chờ quyền lợi thai sản", "tối đa 270 ngày", "Điều 12 khoản 2 điểm d"],
      ["Thời gian chờ với trường hợp tai nạn", "không được áp dụng", "Điều 12 khoản 2 điểm b"],
    ]},
   {"ten": "Ba yếu tố trong câu chữ Điều 22 khoản 2",
    "kiem_chung": "chinh-thuc",
    "nguon": "Luật Kinh doanh bảo hiểm số 08/2022/QH15, Điều 22 khoản 2. Ba điều kiện dưới đây là phần bóc tách câu chữ của chính khoản đó.",
    "cot": ["Điều kiện", "Nguyên văn trong luật"],
    "hang": [
      ["Ý chí", "&ldquo;cố ý&rdquo;"],
      ["Hành vi", "&ldquo;cung cấp không đầy đủ thông tin hoặc cung cấp thông tin sai sự thật&rdquo;"],
      ["Mục đích", "&ldquo;nhằm giao kết hợp đồng bảo hiểm để được bồi thường, trả tiền bảo hiểm&rdquo;"],
    ]},
   {"ten": "Bệnh có sẵn trong bảo hiểm thương mại và trong BHYT là hai chuyện khác nhau",
    "kiem_chung": "chinh-thuc",
    "nguon": "Luật Bảo hiểm y tế, văn bản hợp nhất số 47/VBHN-VPQH năm 2023, các Điều 2, 3 và 23 (danh sách các trường hợp không được hưởng). Luật số 51/2024/QH15 ngày 27/11/2024 có sửa đổi khoản 7 và khoản 8 của Điều 23. Đối chiếu với Thông tư 67/2023/TT-BTC Điều 12.",
    "cot": ["Tiêu chí", "Bảo hiểm thương mại", "Bảo hiểm y tế"],
    "hang": [
      ["Có khái niệm bệnh có sẵn không", "có, tại Thông tư 67 Điều 12 khoản 3", "Điều 23 không liệt kê bệnh có sẵn trong các trường hợp không được hưởng"],
      ["Được từ chối vì tiền sử bệnh không", "có thể, nếu quy tắc điều khoản quy định", "Điều 23 không có trường hợp loại trừ nào theo tiền sử bệnh"],
      ["Cách xác định mức hưởng", "theo hợp đồng", "theo mức độ bệnh tật và thời gian tham gia, không theo tình trạng sức khoẻ khi tham gia"],
      ["Tính chất", "tự nguyện, có lợi nhuận", "bắt buộc, không vì mục đích lợi nhuận"],
    ]},
 ],

 "y_chinh": [
   ("Định nghĩa chính thức, nguyên văn",
    "Thông tư 67/2023/TT-BTC, Điều 12 khoản 3 điểm a: &ldquo;Bệnh có sẵn là tình trạng bệnh tật hoặc thương tật của người được bảo hiểm đã được bác sỹ chẩn đoán hoặc điều trị trước ngày hiệu lực hoặc ngày khôi phục hiệu lực (gần nhất) của hợp đồng bảo hiểm.&rdquo; Điểm đáng chú ý nhất nằm ở chỗ định nghĩa gốc bám vào một hành vi y tế đã xảy ra, tức đã được chẩn đoán hoặc đã điều trị, chứ không bám vào việc trong người đã có mầm bệnh hay chưa."),
   ("Doanh nghiệp được mở rộng định nghĩa, nhưng bị chặn ở mốc 36 tháng",
    "Cũng tại điểm a, thông tư cho phép doanh nghiệp bổ sung các dấu hiệu, triệu chứng đặc thù, nhưng &ldquo;chỉ được xem xét đến các dấu hiệu, triệu chứng khởi phát trong vòng 36 tháng trước ngày hiệu lực hoặc ngày khôi phục hiệu lực (gần nhất) của hợp đồng bảo hiểm&rdquo;. Nghĩa là một triệu chứng xuất hiện cách đây bốn năm, chưa từng được chẩn đoán, thì nằm ngoài khung này."),
   ("Căn cứ để xác định bệnh có sẵn là một danh sách đóng",
    "Điều 12 khoản 3 điểm b liệt kê ba nguồn: hồ sơ y tế lưu tại bệnh viện hoặc cơ sở y tế được thành lập hợp pháp; tài liệu y khoa do Bộ Y tế và cơ quan có thẩm quyền ban hành; và thông tin do chính bên mua hoặc người được bảo hiểm tự kê khai. Đây là lý do hồ sơ bệnh án cũ trở thành thứ quan trọng nhất khi có tranh chấp."),
   ("Chữ quan trọng nhất trong Điều 22 vẫn là chữ cố ý",
    "Luật Kinh doanh bảo hiểm 2022, Điều 22 khoản 2, cho doanh nghiệp quyền huỷ bỏ hợp đồng khi bên mua &ldquo;cố ý cung cấp không đầy đủ thông tin hoặc cung cấp thông tin sai sự thật nhằm giao kết hợp đồng bảo hiểm để được bồi thường, trả tiền bảo hiểm&rdquo;. Ba yếu tố phải cùng có mặt: cố ý, hành vi kê khai sai, và mục đích để được bồi thường. Quên một lần khám nhiều năm trước, hoặc không biết mình có bệnh, về mặt câu chữ không thoả mãn cả ba."),
   ("Luật buộc doanh nghiệp phải chứng minh đã giải thích, không phải ngược lại",
    "Điều 19 khoản 2 quy định khi có điều khoản loại trừ trách nhiệm, doanh nghiệp &ldquo;phải quy định rõ trong hợp đồng bảo hiểm, phải giải thích rõ ràng, đầy đủ và có bằng chứng xác nhận việc bên mua bảo hiểm đã được doanh nghiệp bảo hiểm... giải thích đầy đủ và hiểu rõ nội dung này khi giao kết hợp đồng bảo hiểm&rdquo;. Nghĩa vụ chứng minh nằm ở phía doanh nghiệp."),
   ("Bệnh có sẵn không phải điều luật cấm bảo hiểm",
    "Điều 12 khoản 2 điểm c của Thông tư 67 viết: &ldquo;Đối với trường hợp doanh nghiệp bảo hiểm chấp thuận bảo hiểm cho các bệnh có sẵn, thời gian chờ tối đa là 1 năm.&rdquo; Câu này chỉ tồn tại nếu pháp luật dự liệu việc doanh nghiệp có thể nhận bảo hiểm cho bệnh có sẵn. Nhận hay không là quyền của doanh nghiệp, không phải nghĩa vụ, nhưng việc nhận là hợp pháp và có khung thời gian chờ riêng."),
   ("Không có quy tắc hai năm trong luật Việt Nam",
    "Một số nước có điều khoản gọi là incontestability: qua một số năm thì doanh nghiệp hết quyền huỷ hợp đồng vì kê khai sai. Luật Kinh doanh bảo hiểm 2022 không có quy định đó. Điều 22 khoản 2 không gắn thời hạn nào cho quyền huỷ bỏ này. Con số hai năm hay bị viện dẫn nằm ở Điều 40 khoản 1 điểm a, và điều đó nói về một trường hợp khác hẳn, không liên quan tới kê khai sai. Hai thứ này hay bị nhầm với nhau."),
   ("BHYT không có khái niệm bệnh có sẵn",
    "Điều 2 Luật Bảo hiểm y tế định nghĩa BHYT là hình thức bảo hiểm bắt buộc, không vì mục đích lợi nhuận, do Nhà nước tổ chức thực hiện. Điều 3 nêu nguyên tắc: mức hưởng xác định theo mức độ bệnh tật và thời gian tham gia, không theo tình trạng sức khoẻ lúc tham gia. Điều 23 liệt kê các trường hợp không được hưởng, và trong danh sách đó không có bệnh có sẵn, không có bệnh mắc trước khi tham gia, không có loại trừ nào theo tiền sử. Người đã có bệnh vẫn tham gia và vẫn hưởng BHYT bình thường."),
 ],

 "khong_ro": [
   "Danh mục bệnh nào được coi là bệnh có sẵn. Không có văn bản nhà nước nào liệt kê. Doanh nghiệp tự xác định trong quy tắc điều khoản, trong khung Điều 12 khoản 3 của Thông tư 67.",
   "Mức tăng phí hoặc loại trừ riêng phần khi người mua có bệnh có sẵn. Cả Luật Kinh doanh bảo hiểm 2022 lẫn Thông tư 67/2023/TT-BTC đều không quy định, để hợp đồng tự thoả thuận.",
   "Quy trình khiếu nại riêng cho tranh chấp về bệnh có sẵn. Không có, dùng chung đường khiếu nại và khởi kiện như mọi tranh chấp hợp đồng bảo hiểm.",
   "Tiêu chí y khoa riêng để xác định bệnh có sẵn. Bộ Y tế không ban hành bộ tiêu chí riêng; Thông tư 67 chỉ dẫn chiếu tới tài liệu y khoa nói chung.",
   "Nghị định 46/2023/NĐ-CP có nhắc tới bệnh có sẵn hay không. Chúng tôi chưa đọc hết nghị định này nên không khẳng định.",
 ],

 "faq": [
   ("Luật Việt Nam có định nghĩa bệnh có sẵn không?",
    "Luật Kinh doanh bảo hiểm số 08/2022/QH15 không có cụm từ này. Nhưng Thông tư 67/2023/TT-BTC, Điều 12 khoản 3 điểm a, thì có định nghĩa: bệnh có sẵn là tình trạng bệnh tật hoặc thương tật đã được bác sỹ chẩn đoán hoặc điều trị trước ngày hiệu lực hoặc ngày khôi phục hiệu lực gần nhất của hợp đồng."),
   ("Công ty bảo hiểm có được tự đặt định nghĩa bệnh có sẵn không?",
    "Doanh nghiệp soạn quy tắc điều khoản của mình, nhưng phải nằm trong khung Điều 12 Thông tư 67. Nếu bổ sung dấu hiệu, triệu chứng đặc thù thì chỉ được xem xét những dấu hiệu khởi phát trong vòng 36 tháng trước ngày hiệu lực hợp đồng."),
   ("Có bệnh có sẵn thì có mua được bảo hiểm không?",
    "Được, nếu doanh nghiệp chấp thuận. Thông tư 67 Điều 12 khoản 2 điểm c nêu rõ trường hợp doanh nghiệp chấp thuận bảo hiểm cho bệnh có sẵn thì thời gian chờ tối đa là 1 năm. Nhưng chấp thuận là quyền của doanh nghiệp, không phải nghĩa vụ, nên từ chối cũng không trái luật."),
   ("Quên khai một lần khám cũ thì có bị huỷ hợp đồng không?",
    "Điều 22 khoản 2 chỉ cho huỷ hợp đồng khi bên mua cố ý cung cấp thông tin sai nhằm mục đích được bồi thường. Ba yếu tố cố ý, kê khai sai và mục đích phải cùng có mặt. Quên hoặc không biết mình có bệnh thì về câu chữ không thoả mãn điều kiện đó. Trên thực tế đây là chỗ tranh chấp nhiều nhất, và hồ sơ bệnh án cũ là thứ quyết định. Kết quả từng vụ phụ thuộc hồ sơ thực tế, bài này không kết luận thay cho trường hợp của bạn."),
   ("Sau bao nhiêu năm thì công ty bảo hiểm không được huỷ hợp đồng vì kê khai sai nữa?",
    "Luật Kinh doanh bảo hiểm 2022 không quy định thời hạn nào cho quyền này. Điều 22 khoản 2 trao quyền huỷ bỏ mà không gắn thời hiệu. Con số hai năm hay xuất hiện trên mạng là nhầm với Điều 40 khoản 1 điểm a, một trường hợp hoàn toàn khác, không liên quan tới kê khai sai."),
   ("Bảo hiểm y tế có từ chối vì bệnh có sẵn không?",
    "Không. Điều 23 Luật Bảo hiểm y tế liệt kê các trường hợp không được hưởng, và trong đó không có loại trừ nào theo tiền sử bệnh. Mức hưởng xác định theo mức độ bệnh tật và thời gian tham gia, theo nguyên tắc tại Điều 3."),
 ],
 "lien_quan": ["ly-do-ho-so-bi-tu-choi-boi-thuong"],
},

]