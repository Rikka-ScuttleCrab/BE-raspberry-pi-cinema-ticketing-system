Drop Database cinemamanagement;



Use cinemamanagement;


-- Add Roles --
INSERT INTO roles(id, role_name) VALUES
("2cc63a77ad4bfc1ba55bef4828818d9787371a757e994e870f3e37f3f93417ea","admin"),
("e7979195f68cc0da6872e2a24c77866713e780053815853b52c99923fd04f834","user"),
("6b5fa69952b506f4d3c77932c83f6607b75b36f129ae49373e10ba238d7f90e0","notrole");


-- Add Users --
INSERT INTO users(day_create, role_id, username, email, password_hash, working) VALUES
("2026-04-25","2cc63a77ad4bfc1ba55bef4828818d9787371a757e994e870f3e37f3f93417ea","admin01","admin@gmail.com","240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9", 1),
("2026-04-25","e7979195f68cc0da6872e2a24c77866713e780053815853b52c99923fd04f834","user01","user@gmail.com","e606e38b0d8c19b24cf0ee3808183162ea7cd63ff7912dbb22b5e803286b4446", 1);


-- Add Time_Slots --
INSERT INTO time_slots(id, start_time) VALUES
(800,'08:00'),(815,'08:15'),(830,'08:30'),(845,'08:45'),
(900,'09:00'),(915,'09:15'),(930,'09:30'),(945,'09:45'),
(1000,'10:00'),(1015,'10:15'),(1030,'10:30'),(1045,'10:45'),
(1100,'11:00'),(1115,'11:15'),(1130,'11:30'),(1145,'11:45'),
(1200,'12:00'),(1215,'12:15'),(1230,'12:30'),(1245,'12:45'),
(1300,'13:00'),(1315,'13:15'),(1330,'13:30'),(1345,'13:45'),
(1400,'14:00'),(1415,'14:15'),(1430,'14:30'),(1445,'14:45'),
(1500,'15:00'),(1515,'15:15'),(1530,'15:30'),(1545,'15:45'),
(1600,'16:00'),(1615,'16:15'),(1630,'16:30'),(1645,'16:45'),
(1700,'17:00'),(1715,'17:15'),(1730,'17:30'),(1745,'17:45'),
(1800,'18:00'),(1815,'18:15'),(1830,'18:30'),(1845,'18:45'),
(1900,'19:00'),(1915,'19:15'),(1930,'19:30'),(1945,'19:45'),
(2000,'20:00'),(2015,'20:15'),(2030,'20:30'),(2045,'20:45'),
(2100,'21:00'),(2115,'21:15'),(2130,'21:30'),(2145,'21:45'),
(2200,'22:00'),(2215,'22:15'),(2230,'22:30'),(2245,'22:45'),
(2300,'23:00'),(2315,'23:15'),(2330,'23:30'),(2345,'23:45'),
(2400,'00:00'),(0015,'00:15'),(0030,'00:30'),(0045,'00:45');


-- Add Voucher --
INSERT INTO vouchers(voucher_code, voucher_value, voucher_exp) VALUES
("GENZU100","10000","2026-12-31"),
("GIOTOHUNGVUONG","36000","2026-05-01"),
("VIPTOP20","20%","2026-12-31"),
("LETO","1000","2026-12-31"),
("CINEMA100k", "100%", "2026-01-01"),
("2587dfd0704eebff8ae75cfe281ea01bf5129c5e734165099256d29831ceae7d","99%","2036-12-31");

-- Add Ticket_Types --
INSERT INTO ticket_types(name, base_price) VALUES 
("2D Phụ Đề", 75000), ("2D Lồng Tiếng", 75000),
("3D Phụ Đề", 150000), ("3D Lồng Tiếng", 150000),
("IMAX 2D Phụ Đề", 195000), ("IMAX 2D Lồng Tiếng", 195000),
("IMAX 3D Phụ Đề", 250000), ("IMAX 3D Lồng Tiếng", 250000);


-- Add Theater_Rooms --
INSERT INTO theater_rooms(name, seat_capacity) VALUES 
("A",72), ("B", 64), ("C", 100), ("D", 144),
("IMAX01", 144), ("IMAX02", 144);


-- Add Seats --
INSERT INTO seats(theater_room_id, seat_row, seat_number) VALUES 
-- Room A
(1,"A",1),(1,"A",2),(1,"A",3),(1,"A",4),(1,"A",5),(1,"A",6),(1,"A",7),(1,"A",8),
(1,"B",1),(1,"B",2),(1,"B",3),(1,"B",4),(1,"B",5),(1,"B",6),(1,"B",7),(1,"B",8),
(1,"C",1),(1,"C",2),(1,"C",3),(1,"C",4),(1,"C",5),(1,"C",6),(1,"C",7),(1,"C",8),
(1,"D",1),(1,"D",2),(1,"D",3),(1,"D",4),(1,"D",5),(1,"D",6),(1,"D",7),(1,"D",8),
(1,"E",1),(1,"E",2),(1,"E",3),(1,"E",4),(1,"E",5),(1,"E",6),(1,"E",7),(1,"E",8),
(1,"F",1),(1,"F",2),(1,"F",3),(1,"F",4),(1,"F",5),(1,"F",6),(1,"F",7),(1,"F",8),
(1,"G",1),(1,"G",2),(1,"G",3),(1,"G",4),(1,"G",5),(1,"G",6),(1,"G",7),(1,"G",8),
(1,"H",1),(1,"H",2),(1,"H",3),(1,"H",4),(1,"H",5),(1,"H",6),(1,"H",7),(1,"H",8),
(1,"J",1),(1,"J",2),(1,"J",3),(1,"J",4),(1,"J",5),(1,"J",6),(1,"J",7),(1,"J",8),

-- Room B
(2,"A",1),(2,"A",2),(2,"A",3),(2,"A",4),(2,"A",5),(2,"A",6),(2,"A",7),(2,"A",8),
(2,"B",1),(2,"B",2),(2,"B",3),(2,"B",4),(2,"B",5),(2,"B",6),(2,"B",7),(2,"B",8),
(2,"C",1),(2,"C",2),(2,"C",3),(2,"C",4),(2,"C",5),(2,"C",6),(2,"C",7),(2,"C",8),
(2,"D",1),(2,"D",2),(2,"D",3),(2,"D",4),(2,"D",5),(2,"D",6),(2,"D",7),(2,"D",8),
(2,"E",1),(2,"E",2),(2,"E",3),(2,"E",4),(2,"E",5),(2,"E",6),(2,"E",7),(2,"E",8),
(2,"F",1),(2,"F",2),(2,"F",3),(2,"F",4),(2,"F",5),(2,"F",6),(2,"F",7),(2,"F",8),
(2,"G",1),(2,"G",2),(2,"G",3),(2,"G",4),(2,"G",5),(2,"G",6),(2,"G",7),(2,"G",8),
(2,"H",1),(2,"H",2),(2,"H",3),(2,"H",4),(2,"H",5),(2,"H",6),(2,"H",7),(2,"H",8),

-- Room C --
(3,"A",1),(3,"A",2),(3,"A",3),(3,"A",4),(3,"A",5),(3,"A",6),(3,"A",7),(3,"A",8),(3,"A",9),(3,"A",10),
(3,"B",1),(3,"B",2),(3,"B",3),(3,"B",4),(3,"B",5),(3,"B",6),(3,"B",7),(3,"B",8),(3,"B",9),(3,"B",10),
(3,"C",1),(3,"C",2),(3,"C",3),(3,"C",4),(3,"C",5),(3,"C",6),(3,"C",7),(3,"C",8),(3,"C",9),(3,"C",10),
(3,"D",1),(3,"D",2),(3,"D",3),(3,"D",4),(3,"D",5),(3,"D",6),(3,"D",7),(3,"D",8),(3,"D",9),(3,"D",10),
(3,"E",1),(3,"E",2),(3,"E",3),(3,"E",4),(3,"E",5),(3,"E",6),(3,"E",7),(3,"E",8),(3,"E",9),(3,"E",10),
(3,"F",1),(3,"F",2),(3,"F",3),(3,"F",4),(3,"F",5),(3,"F",6),(3,"F",7),(3,"F",8),(3,"F",9),(3,"F",10),
(3,"G",1),(3,"G",2),(3,"G",3),(3,"G",4),(3,"G",5),(3,"G",6),(3,"G",7),(3,"G",8),(3,"G",9),(3,"G",10),
(3,"H",1),(3,"H",2),(3,"H",3),(3,"H",4),(3,"H",5),(3,"H",6),(3,"H",7),(3,"H",8),(3,"H",9),(3,"H",10),
(3,"J",1),(3,"J",2),(3,"J",3),(3,"J",4),(3,"J",5),(3,"J",6),(3,"J",7),(3,"J",8),(3,"J",9),(3,"J",10),
(3,"K",1),(3,"K",2),(3,"K",3),(3,"K",4),(3,"K",5),(3,"K",6),(3,"K",7),(3,"K",8),(3,"K",9),(3,"K",10);

-- Room D --
INSERT INTO seats(theater_room_id, seat_row, seat_number)
SELECT 4, r.seat_row, n.seat_number
FROM (
    SELECT 'A' AS seat_row UNION SELECT 'B' UNION SELECT 'C' UNION SELECT 'D'
    UNION SELECT 'E' UNION SELECT 'F' UNION SELECT 'G' UNION SELECT 'H'
    UNION SELECT 'J' UNION SELECT 'K' UNION SELECT 'L' UNION SELECT 'M'
) r
CROSS JOIN (
    SELECT 1 AS seat_number UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5
    UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9 UNION SELECT 10
    UNION SELECT 11 UNION SELECT 12
) n;

-- Room IMAX01 --
INSERT INTO seats(theater_room_id, seat_row, seat_number)
SELECT 5, r.seat_row, n.seat_number
FROM (
    SELECT 'A' AS seat_row UNION SELECT 'B' UNION SELECT 'C' UNION SELECT 'D'
    UNION SELECT 'E' UNION SELECT 'F' UNION SELECT 'G' UNION SELECT 'H'
    UNION SELECT 'J' UNION SELECT 'K' UNION SELECT 'L' UNION SELECT 'M'
) r
CROSS JOIN (
    SELECT 1 AS seat_number UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5
    UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9 UNION SELECT 10
    UNION SELECT 11 UNION SELECT 12
) n;

-- Room IMAX02 --
INSERT INTO seats(theater_room_id, seat_row, seat_number)
SELECT 6, r.seat_row, n.seat_number
FROM (
    SELECT 'A' AS seat_row UNION SELECT 'B' UNION SELECT 'C' UNION SELECT 'D'
    UNION SELECT 'E' UNION SELECT 'F' UNION SELECT 'G' UNION SELECT 'H'
    UNION SELECT 'J' UNION SELECT 'K' UNION SELECT 'L' UNION SELECT 'M'
) r
CROSS JOIN (
    SELECT 1 AS seat_number UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5
    UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9 UNION SELECT 10
    UNION SELECT 11 UNION SELECT 12
) n;


-- Add Theater_Room_Ticket_Type --
INSERT INTO theater_room_ticket_type(theater_room_id, ticket_type_id) VALUES
(1,1),(1,2),(2,1),(2,2),(3,1),(3,2),(4,3),(4,4),
(5,5),(5,6),(5,7),(5,8),(6,5),(6,6),(6,7),(6,8);


-- Add Category --
INSERT INTO categories (name) VALUE ("Giật Gân");
INSERT INTO categories (name) VALUE ("Kinh Dị");
INSERT INTO categories (name) VALUE ("Hoạt Hình");
INSERT INTO categories (name) VALUE ("Phiêu Lưu");
INSERT INTO categories (name) VALUE ("Hài");
INSERT INTO categories (name) VALUE ("Hành Động");
INSERT INTO categories (name) VALUE ("Lãng Mạn");
INSERT INTO categories (name) VALUE ("Tâm Lý");
INSERT INTO categories (name) VALUE ("Tình Cảm");
INSERT INTO categories (name) VALUE ("Gia Đình");
INSERT INTO categories (name) VALUE ("Ca Nhạc");
INSERT INTO categories (name) VALUE ("Giả Tưởng");
INSERT INTO categories (name) VALUE ("Lịch Sử");
INSERT INTO categories (name) VALUE ("Ly Kì");
ALTER TABLE categories
ADD CONSTRAINT unique_category_name UNIQUE (name);

-- Add Movie Đang chiếu --
INSERT INTO movies (title, age_rating, duration_min, description, release_date, end_date)
VALUES
('Tội Phạm 101', 'T18', 110, 'Lấy bối cảnh thành phố Los Angeles đầy nắng và bụi đường, Tội Phạm 101 kể về một tên trộm nữ trang bí ẩn (Chris Hemsworth) với hàng loạt phi vụ táo bạo khiến cảnh sát phải đau đầu. Trong lúc chuẩn bị cho phi vụ lớn nhất của mình, hắn gặp gỡ một nữ nhân viên bảo hiểm (Halle Berry), người cũng đang vật lộn với những lựa chọn trong đời mình. Trong khi đó, một thanh tra (Mark Ruffalo) đã tìm ra quy luật trong chuỗi các vụ án và đang ráo riết truy đuổi tên trộm, khiến cuộc chơi trở nên căng thẳng hơn bao giờ hết. Khi phi vụ định mệnh đến gần, ranh giới giữa kẻ săn đuổi và con mồi dần trở nên mờ nhạt và cả ba buộc phải đối mặt với những lựa chọn khó khăn và không còn cơ hội để quay đầu lại. Bộ phim được chuyển thể từ tiểu thuyết ngắn nổi tiếng cùng tên của Don Winslow, do Bart Layton (tác giả của American Animals, The Imposter) viết kịch bản và đạo diễn. Dàn diễn viên có sự tham gia của Barry Keoghan, Monica Barbaro, Corey Hawkins, Jennifer Jason Leigh và Nick Nolte.', '2026-03-13', '2027-05-13'),

('Quỷ Nhập Tràng 2', 'T18', 126, 'Quỷ Nhập Tràng 2 là tiền truyện của nhân vật Minh Như, trở về xưởng nhuộm gia đình sau nhiều năm bị xua đuổi. Tại đây, cô phải đối mặt với những hiện tượng ma quái cùng sự thật tàn khốc về cái chết của mẹ và giao ước đẫm máu năm xưa. Ác giả ác báo, liệu Minh Như có thoát khỏi vòng vây của quỷ dữ?', '2026-03-06', '2027-05-06'),

('Hoppers: Cú Nhảy Kỳ Diệu', 'T13', 105, 'Hoppers xoay quanh Mabel, một cô gái yêu động vật, vô tình tiếp cận công nghệ cho phép chuyển ý thức con người vào cơ thể robot động vật. Nhờ đó, Mabel “nhảy” vào thế giới tự nhiên dưới hình dạng một con hải ly và có thể giao tiếp trực tiếp với các loài khác. Trong hành trình này, cô dần khám phá cách động vật nhìn nhận con người, đồng thời phát hiện những mối nguy đang đe dọa môi trường sống của chúng. Tận dụng công nghệ Nhảy, Mabel đã trở thành cầu nối, mang lại cuộc sống cân bằng cho cả con người và động vật.', '2026-03-13', '2027-05-13'),

('Greenland 2: Đại Di Cư', 'T13', 98, 'Bom tấn thảm họa thiên thạch trở lại! 5 năm sau cú va chạm tuyệt diệt, nhân loại một lần nữa đứng trước bờ vực bị xóa sổ. Buộc phải rời khỏi hầm trú ẩn, gia đình Garrity bắt đầu cuộc đại di cư khẩn thiết đầy khắc nghiệt. Một hành trình không đường lui, nơi mỗi bước chân đều là cuộc chiến giành lấy cơ hội tồn tại trong một thế giới đã lụi tàn.', '2026-03-13', '2027-05-13'),

('Cô Dâu!', 'T18', 130, 'Một cách tiếp cận táo bạo, phá vỡ mọi khuôn mẫu đối với một trong những câu chuyện hấp dẫn nhất thế giới. Bộ phim theo chân Frankenstein cô đơn (do Chrisitian Bale thủ vai) lên đường đến Chicago những năm 1930 để tìm đến nhà khoa học Dr. Euphronious (Annette Bening – 5 lần đề cử Oscar thủ vai), với hy vọng bà có thể tạo ra một người bạn đồng hành cho mình. Cả hai hồi sinh một cô gái trẻ đã bị sát hại, và Cô Dâu (Buckley thủ vai) đã ra đời. Những gì xảy ra sau đó đã vượt xa mọi tưởng tượng của họ: những vụ giết người, sự chiếm hữu, một phong trào văn hóa hoang dại và cấp tiến cũng như mối tình ngoài vòng pháp luật đầy cuồng nhiệt và bùng nổ!', '2026-03-13', '2027-05-13'),

('Không Còn Chúng Ta', 'T13', 115, 'Jeong-won và Eun-ho yêu nhau chân thành và sâu đậm bằng những tất cả những gì họ có ở khoảng thời gian đẹp nhất của thanh xuân. Nhưng tình yêu của tuổi trẻ không tránh khỏi sự non nớt, bồng bột để rồi họ chọn rời xa nhau. Nhiều năm sau gặp lại, họ nhận ra: chính những tháng năm đã yêu và đã đau ấy đã giúp họ trưởng thành hơn, hiểu được tình yêu và biết cách yêu thương hơn. Chỉ tiếc rằng khi ấy, yêu thương này họ không dành cho nhau được nữa…', '2026-03-06', '2027-05-06'),

('Lời Nguyền Thư Viện Mikura', 'T13', 110, 'Mikura Mifuyu rất ghét đọc sách lại là con gái của "gia tộc" nhiều đời quản lý một thư viện khổng lồ. Khi những cuốn sách bị đánh cắp, cô bị nuốt chửng vào thế giới của những câu chuyện. Mifuyu buộc phải truy tìm kẻ trộm sách, tìm hiểu về "lời nguyền" cũng như "gia tộc" mà ngay cả cô cũng không hề hay biết. Hành trình phiêu lưu qua "Thế giới sách" chính thức bắt đầu!', '2026-03-06', '2027-05-06'),

('Quốc Bảo', 'T16', 120, 'Kikuo, con trai của một tay xã hội đen, được một diễn viên kịch Kabuki nổi tiếng nhận nuôi và trở thành một diễn viên Onnagata tài năng. Kikuo đi cùng chặng đường nhiều thập kỷ cùng Shunsuke, con ruột của người cha nuôi. Cả hai nếm trải tình huynh đệ, ganh đua và tai tiếng để khẳng định vị trí trên sân khấu Kabuki. Trong bối cảnh Nhật Bản hậu chiến đầy biến động, họ phải đối mặt áp lực gìn giữ nghệ thuật truyền thống và theo đuổi danh hiệu “Báu vật sống của quốc gia”.
', '2026-03-06', '2027-05-06'),

('Tài', 'T16', 115, 'Tài bất ngờ rơi vào vòng xoáy nguy hiểm vì một khoản nợ tiền khổng lồ. Bị dồn vào đường cùng, Tài buộc phải dấn thân vào những lựa chọn sai lầm khiến gia đình trở thành mục tiêu bị đe dọa. Đằng sau những hành động liều lĩnh ấy là nỗi ám ảnh về người mẹ mà Tài luôn muốn bảo vệ và bù đắp bằng mọi giá. Khi ranh giới giữa đúng và sai ngày càng mong manh, Tài phải đối mặt với câu hỏi lớn nhất của đời mình: liệu lòng hiếu thảo có đủ để biện minh cho con đường anh đang đi.', '2026-03-06', '2027-05-06'),

('Cảm Ơn Người Đã Thức Cùng Tôi', 'K', 105, 'Cảm Ơn Người Đã Thức Cùng Tôi là một hành trình cảm xúc của những người trẻ đi tìm đáp án cho câu hỏi “Ước mơ của bạn là gì?”, để rồi chính họ khi bước vào thế giới trưởng thành dần nhận ra câu hỏi quan trọng nhất là “Mình muốn thực hiện ước mơ đó cùng ai?”', '2026-02-27', '2027-04-27'),

('Thỏ Ơi!!', 'T18', 110, 'Phim “Thỏ ơi!!” dự kiến công chiếu trong dịp Tết 2026, thuộc thể loại hài, tâm lý sở trường của Trấn Thành, mang màu sắc trẻ trung với dàn diễn viên mới, tiếp nối tinh thần đem đến cho khán giả những điều vui vẻ, hài hước vào dịp Tết Nguyên đán.', '2026-02-10', '2027-05-10');

-- Add Movie Sắp Chiếu --
INSERT INTO movies (title, age_rating, duration_min, description, release_date, end_date)
VALUES
('Đêm Ngày Xa Mẹ','T13',105,'Phim gia đình cảm động về mối quan hệ mẹ và con.','2027-06-20','2027-07-20'),

('Căn Nhà Ký Ức','T13',110,'Phim tâm lý về những ký ức bị lãng quên trong một gia đình.','2027-06-20','2027-07-20'),

('Omukade: Con Rết Người','T18',108,'Phim kinh dị Nhật Bản dựa trên truyền thuyết quái vật cổ đại.','2027-06-20','2027-07-20'),

('Bus – Chuyến Xe Một Chiều','T16',115,'Phim kinh dị về chuyến xe định mệnh không có đường quay lại.','2027-06-20','2027-07-20'),

('La Tiểu Hắc Chiến Ký 2','T13',100,'Phim hoạt hình phiêu lưu tiếp nối câu chuyện của La Tiểu Hắc.','2027-06-20','2027-07-20'),

('Tiếng Thét 7','T18',112,'Phần tiếp theo của series kinh dị nổi tiếng Scream.','2027-06-20','2027-07-20'),

('Bẫy Tiền','T16',110,'Phim hành động về những phi vụ lừa đảo nguy hiểm.','2027-06-21','2027-07-21'),

('Thoát Khỏi Tận Thế','T13',120,'Phim khoa học viễn tưởng về hành trình sinh tồn của nhân loại.','2027-03-19','2027-05-19'),

('Kung Fu Quái Chưởng','T13',105,'Phim hành động võ thuật hài đến từ Đài Loan.','2027-06-27','2027-07-27'),

('Project Y: Gái Ngoan Đổi Đời','T16',108,'Phim hành động – tội phạm về cuộc đời hai cô gái.','2027-06-27','2027-07-27'),

('Tứ Hổ Đại Náo','T13',110,'Phim hành động hài với nhóm nhân vật gây náo loạn.','2027-06-27','2027-07-27'),

('Chúng Sẽ Đoạt Mạng','T18',109,'Phim kinh dị về một thế lực bí ẩn truy sát con người.','2027-06-27','2027-07-27'),

('Mario Thiên Hà','P',98,'Phim hoạt hình phiêu lưu của Mario trong vũ trụ mới.','2027-06-01','2027-07-01'),

('Hẹn Em Ngày Nhất Thức','T13',105,'Phim tình cảm về những cuộc gặp gỡ định mệnh.','2027-06-03','2027-07-03'),

('Song Hỷ Lâm Nguy','T13',108,'Phim hài – gia đình xoay quanh một đám cưới rắc rối.','2027-06-03','2027-07-03'),

('The Conjuring: Xác Ướp','T18',115,'Phim kinh dị thuộc vũ trụ The Conjuring.','2027-06-17','2027-07-17'),

('Trùm Sò','T13',104,'Phim hài về những tình huống dở khóc dở cười trong kinh doanh.','2027-06-24','2027-07-24'),

('Anh Hùng','T13',112,'Phim hành động về một người đàn ông bình thường trở thành anh hùng.','2027-06-24','2027-07-24'),

('Đại Tiệc Trăng Máu 8','T16',115,'Phần mới của series hài đen nổi tiếng.','2027-06-30','2027-07-30'),

('Michael','T13',130,'Phim tiểu sử về huyền thoại âm nhạc Michael Jackson.','2027-06-26','2027-07-26'),

('Mortal Kombat 2','T16',120,'Phần tiếp theo của loạt phim hành động dựa trên game Mortal Kombat.','2027-06-15','2027-07-15'),

('Thời Khắc Công Bố','T13',105,'Phim tâm lý về bí mật được tiết lộ vào phút cuối.','2027-06-20','2027-07-20'),

('Madam Thanh Lạc','T13',110,'Phim cổ trang Việt Nam xoay quanh hai người phụ nữ quyền lực.','2027-06-06','2027-08-06'),

('Supergirl','T13',125,'Bom tấn siêu anh hùng DC về Supergirl.','2027-06-26','2027-08-26');

-- Add Phim Ngưng Chiếu --
INSERT INTO movies (title, age_rating, duration_min, description, release_date, end_date)
VALUES
('The Conjuring: Last Rites', 'T18', 120,
 'Phần cuối của loạt phim kinh dị The Conjuring, tiếp tục câu chuyện điều tra siêu nhiên của vợ chồng Warren.',
 '2025-09-05', '2025-11-05'),

('Tử Chiến Trên Không', 'T16', 115,
 'Phim Việt Nam dựa trên sự kiện có thật về một vụ không tặc trong lịch sử ngành hàng không.',
 '2025-09-22', '2025-11-22'),

('Tron: Ares', 'T13', 130,
 'Phim khoa học viễn tưởng tiếp nối thương hiệu Tron với thế giới thực và thế giới kỹ thuật số giao thoa.',
 '2025-10-10', '2025-12-10'),

('Zootopia 2', 'P', 110,
 'Phần tiếp theo của phim hoạt hình nổi tiếng Zootopia với cuộc phiêu lưu mới của Judy và Nick.',
 '2025-11-26', '2026-01-26'),

('Avatar: Fire and Ash', 'T13', 192,
 'Phần tiếp theo trong loạt phim Avatar của James Cameron, giới thiệu bộ tộc Na’vi mới tại Pandora.',
 '2025-12-19', '2026-02-19');

-- Add Actors--
UPDATE movies
SET actors = CASE
    WHEN id = 1 THEN "Chris Hemsworth,Mark Ruffalo,Halle Berry,Barry Keoghan,Monica Barbaro,Nick Nolte"
    WHEN id = 2 THEN "Quang Tuấn, Khả Như, Vân Dung, Đào Anh Tuấn, Phương Bình, Doãn Quốc Đam, Thanh Hiền, Lê Thúy"
	WHEN id = 3 THEN "Jon Hamm, Piper Curda, Bobby Moynihan"
    WHEN id = 4 THEN "
Amber Rose Revah, Antonio De Lima, Beruce Khan, Gerard Butler, Gina Gangar, Gísli Örn Garðarsson, Megan Jacobs Shrivastava, Mitu Panicucci, Morena Baccarin, Peter Polycarpou, Roman Griffin Davis, Sidsel Siem Koch, Tommie Earl Jenkins, Trond Fausa Aurvåg"
    WHEN id = 5 THEN "Jessie Buckley, Christian Bale, Annette Bening, Penélope Cruz, Peter Sarsgaard"
    WHEN id = 6 THEN "Koo Kyo Hwan,Mun Ka Young,Lee Sang Yeob,Lim Jae Hyeok,Shin Jung Keun,Kang Mal Geum"
    WHEN id = 7 THEN "Kataoka Rin, Tamaki Sora"
    WHEN id = 8 THEN "Koshiyama Keitatsu, Kurokawa Soya, Mikami Ai"
    WHEN id = 9 THEN "Mai Tài Phến, Vinh Râu, Long Đẹp Trai, Hồng Ánh, Trần Kim Hải"
    WHEN id = 10 THEN "Võ Phan Kim Khánh, Trần Doãn Hoàng, Nguyễn Hùng"
    WHEN id = 11 THEN "Lyly, Pháo, Văn Mai Hương, Quốc Anh, Trấn Thành"
END
WHERE id IN (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11);


-- Add Movie_Category --
INSERT INTO movie_category(movie_id, category_id) 
VALUE 
(1,6),(1,14),(2,2),(2,14),(3,3),(3,4),(3,10),

(4,6),(4,4),(5,2),(5,14),(6,8),(6,9),

(7,3),(7,4),(8,13),(8,8),(9,5),(9,8),

(10,3),(10,4),(10,10),(11,6),(11,14),(12,5),(12,9),

(13,8),(13,9),(14,4),(14,12),(15,2),(15,14),(16,6),(16,4),

(17,3),(17,10),(18,8),(18,14),(19,6),(19,13),

(20,5),(20,8),(21,4),(21,12),(22,2),(22,14),(23,6),(23,4),

(24,3),(24,10),(25,8),(25,9),(26,13),(26,8),

(27,6),(27,14),(28,5),(28,8),(29,3),(29,4),

(30,5),(30,8),(31,11),(31,13),(32,6),(32,4),(32,12),

(33,8),(33,14),(34,13),(34,8),(35,6),(35,4),(35,12),

(36,2),(36,14),(37,6),(37,13),(38,12),(38,4),(38,6),

(39,3),(39,4),(39,10),(40,4),(40,12),(40,6);

-- Add Poster --
INSERT INTO posters(movie_id, name, path) 
VALUE 
(1, "Poster Tội Phạm 101", "https://iguov8nhvyobj.vcdn.cloud/media/catalog/product/cache/1/image/c5f0a1eff4c394a251036189ccddaacd/p/o/poster-crime.jpg"),
(2, "Poster Quỷ Nhập Tràng 2 ", "https://iguov8nhvyobj.vcdn.cloud/media/catalog/product/cache/1/image/c5f0a1eff4c394a251036189ccddaacd/4/7/470wx700h-qnt.jpg"),
(3, "Poster Hoppers: Cú Nhảy Kỳ Diệu", "https://iguov8nhvyobj.vcdn.cloud/media/catalog/product/cache/1/image/1800x/71252117777b696995f01934522c402d/h/o/hoppers_-_poster.jpg"),
(4, "Poster Greenland 2: Đại Di Cư", "https://iguov8nhvyobj.vcdn.cloud/media/catalog/product/cache/3/image/c5f0a1eff4c394a251036189ccddaacd/3/5/350x495-greenland.jpg"),
(5, "Poster Cô Dâu!", "https://iguov8nhvyobj.vcdn.cloud/media/catalog/product/cache/1/image/c5f0a1eff4c394a251036189ccddaacd/m/a/main_poster_co_dau_1_final.jpg"),
(6, "Poster Không Còn Chúng Ta", "https://iguov8nhvyobj.vcdn.cloud/media/catalog/product/cache/1/image/c5f0a1eff4c394a251036189ccddaacd/4/7/470x700-us.jpg"),
(7, "Poster Lời Nguyền Thư Viện Mikura", "https://media.lottecinemavn.com/Media/MovieFile/MovieImg/202602/12112_203_100002.jpg"),
(8, "Poster Quốc Bảo", "https://iguov8nhvyobj.vcdn.cloud/media/catalog/product/cache/3/image/1800x/71252117777b696995f01934522c402d/k/o/kokuho_470x700.jpg"),
(9, "Poster Tài", "https://iguov8nhvyobj.vcdn.cloud/media/catalog/product/cache/3/image/1800x/71252117777b696995f01934522c402d/1/2/1200wx1800h-tai.jpg"),
(10, "Poster Cảm Ơn Người Đã Thức Cùng Tôi", "https://iguov8nhvyobj.vcdn.cloud/media/catalog/product/cache/1/image/c5f0a1eff4c394a251036189ccddaacd/m/a/main_condtct_cinema_low.jpg"),
(11, "Poster Thỏ Ơi!!", "https://iguov8nhvyobj.vcdn.cloud/media/catalog/product/cache/1/image/c5f0a1eff4c394a251036189ccddaacd/t/o/to_poster_official_tiectet_3x4_fa.jpg");


INSERT INTO trailers(movie_id, name, path) 
VALUE 
(1, "Trailer Tội Phạm 101", "https://www.youtube.com/watch?v=TxY9GfEEMOI"),
(2, "Trailer Quỷ Nhập Tràng 2 ", "https://www.youtube.com/watch?v=q0UWKBzFFxQ"),
(3, "Trailer Hoppers: Cú Nhảy Kỳ Diệu", "https://www.youtube.com/watch?v=mRSpJwMp6LM"),
(4, "Trailer Greenland 2: Đại Di Cư", "https://www.youtube.com/watch?v=h-LQ-kWefX4"),
(5, "Trailer Cô Dâu!", "https://www.youtube.com/watch?v=HYIOdcSGON4"),
(6, "Trailer Không Còn Chúng Ta", "https://www.youtube.com/watch?v=DltytoKP7Rg"),
(7, "Trailer Lời Nguyền Thư Viện Mikura", "https://www.youtube.com/watch?v=rRA7t2VBvPU"),
(8, "Trailer Quốc Bảo", "https://www.youtube.com/watch?v=v619uUq9pPs"),
(9, "Trailer Tài", "https://www.youtube.com/watch?v=z8H4miEhi-4"),
(10, "Trailer Cảm Ơn Người Đã Thức Cùng Tôi", "https://www.youtube.com/watch?v=uf2oOeJ-Z3s&list=RDuf2oOeJ-Z3s&start_radio=1"),
(11, "Trailer Thỏ Ơi!!", "https://www.youtube.com/watch?v=j1aBd2_GH48");




DELIMITER $$

DROP PROCEDURE IF EXISTS RESET_SHOWTIMES $$

CREATE PROCEDURE RESET_SHOWTIMES()
BEGIN
    DELETE FROM tickets;
    ALTER TABLE tickets AUTO_INCREMENT = 260000001;

    DELETE FROM orders;
    ALTER TABLE orders AUTO_INCREMENT = 260000001;

    DELETE FROM showtimes;
    ALTER TABLE showtimes AUTO_INCREMENT = 260000001;
END $$

DELIMITER ;



SET SQL_SAFE_UPDATES = 0;
CALL RESET_SHOWTIMES;
SET SQL_SAFE_UPDATES = 1;

