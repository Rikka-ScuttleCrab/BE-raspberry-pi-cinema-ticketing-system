Use cinemamanagement;

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

-- Add Ticket_Types --
INSERT INTO ticket_types(name, base_price) VALUES 
("2D Phụ Đề", 100000), ("2D Lồng Tiếng", 120000), 
("3D Phụ Đề", 150000), ("3D Lồng Tiếng", 180000),
("IMAX 2D Phụ Đề", 200000), ("IMAX 2D Lồng Tiếng", 250000),
("IMAX 3D Phụ Đề", 300000), ("IMAX 3D Lồng Tiếng", 350000);

-- Add Theater_Rooms --
INSERT INTO theater_rooms(name, seat_capacity) VALUES 
("A",72), ("B", 64), ("C", 100), ("D", 144),
("IMAX01", 144), ("IMAX02", 144);

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

-- Add Movie Đang chiếu --
INSERT INTO movies (title, age_rating, duration_min, description, release_date, end_date)
VALUES
('Tội Phạm 101', 'T18', 110, 'Phim hành động hình sự về thế giới tội phạm nguy hiểm.', '2026-03-13', '2026-05-13'),

('Quỷ Nhập Tràng 2', 'T18', 126, 'Phần tiếp theo của phim kinh dị về hiện tượng nhập tràng và các nghi lễ tâm linh.', '2026-03-06', '2026-05-06'),

('Hoppers: Cú Nhảy Kỳ Diệu', 'T13', 105, 'Phim hoạt hình phiêu lưu về cuộc hành trình kỳ diệu của một sinh vật nhỏ.', '2026-03-13', '2026-05-13'),

('Greenland 2: Đại Di Cư', 'T13', 98, 'Bom tấn thảm họa khi nhân loại phải rời bỏ nơi trú ẩn để sinh tồn sau thiên thạch.', '2026-03-13', '2026-05-13'),

('Cô Dâu!', 'T18', 130, 'Phim kinh dị pha hài kể về một cô dâu với quá khứ bí ẩn.', '2026-03-13', '2026-05-13'),

('Không Còn Chúng Ta', 'T13', 115, 'Phim tình cảm về những mối quan hệ và ký ức đã mất.', '2026-03-06', '2026-05-06'),

('Lời Nguyền Thư Viện Mikura', 'T13', 110, 'Phim hoạt hình kỳ ảo về lời nguyền bí ẩn trong thư viện cổ.', '2026-03-06', '2026-05-06'),

('Quốc Bảo', 'T16', 120, 'Phim lịch sử – chính kịch xoay quanh một bảo vật quốc gia.', '2026-03-06', '2026-05-06'),

('Tài', 'T16', 115, 'Phim Việt Nam xoay quanh cuộc đời của Tài và những biến cố trong gia đình và xã hội.', '2026-03-06', '2026-05-06'),

('Cảm Ơn Người Đã Thức Cùng Tôi', 'K', 105, 'Phim tình cảm – âm nhạc về tình bạn và những người luôn đồng hành trong cuộc sống.', '2026-02-27', '2026-04-27'),

('Thỏ Ơi!!', 'T18', 110, 'Phim hài – hành động với câu chuyện về những nhân vật bí ẩn trong một bữa tiệc đầy hỗn loạn.', '2026-02-10', '2026-04-10');

-- Add Movie Sắp Chiếu --
INSERT INTO movies (title, age_rating, duration_min, description, release_date, end_date)
VALUES
('Đêm Ngày Xa Mẹ','T13',105,'Phim gia đình cảm động về mối quan hệ mẹ và con.','2026-06-20','2026-07-20'),

('Căn Nhà Ký Ức','T13',110,'Phim tâm lý về những ký ức bị lãng quên trong một gia đình.','2026-06-20','2026-07-20'),

('Omukade: Con Rết Người','T18',108,'Phim kinh dị Nhật Bản dựa trên truyền thuyết quái vật cổ đại.','2026-06-20','2026-07-20'),

('Bus – Chuyến Xe Một Chiều','T16',115,'Phim kinh dị về chuyến xe định mệnh không có đường quay lại.','2026-06-20','2026-07-20'),

('La Tiểu Hắc Chiến Ký 2','T13',100,'Phim hoạt hình phiêu lưu tiếp nối câu chuyện của La Tiểu Hắc.','2026-06-20','2026-07-20'),

('Tiếng Thét 7','T18',112,'Phần tiếp theo của series kinh dị nổi tiếng Scream.','2026-06-20','2026-07-20'),

('Bẫy Tiền','T16',110,'Phim hành động về những phi vụ lừa đảo nguy hiểm.','2026-06-21','2026-07-21'),

('Thoát Khỏi Tận Thế','T13',120,'Phim khoa học viễn tưởng về hành trình sinh tồn của nhân loại.','2026-03-19','2026-05-19'),

('Kung Fu Quái Chưởng','T13',105,'Phim hành động võ thuật hài đến từ Đài Loan.','2026-06-27','2026-07-27'),

('Project Y: Gái Ngoan Đổi Đời','T16',108,'Phim hành động – tội phạm về cuộc đời hai cô gái.','2026-06-27','2026-07-27'),

('Tứ Hổ Đại Náo','T13',110,'Phim hành động hài với nhóm nhân vật gây náo loạn.','2026-06-27','2026-07-27'),

('Chúng Sẽ Đoạt Mạng','T18',109,'Phim kinh dị về một thế lực bí ẩn truy sát con người.','2026-06-27','2026-07-27'),

('Mario Thiên Hà','P',98,'Phim hoạt hình phiêu lưu của Mario trong vũ trụ mới.','2026-06-01','2026-07-01'),

('Hẹn Em Ngày Nhất Thức','T13',105,'Phim tình cảm về những cuộc gặp gỡ định mệnh.','2026-06-03','2026-07-03'),

('Song Hỷ Lâm Nguy','T13',108,'Phim hài – gia đình xoay quanh một đám cưới rắc rối.','2026-06-03','2026-07-03'),

('The Conjuring: Xác Ướp','T18',115,'Phim kinh dị thuộc vũ trụ The Conjuring.','2026-06-17','2026-07-17'),

('Trùm Sò','T13',104,'Phim hài về những tình huống dở khóc dở cười trong kinh doanh.','2026-06-24','2026-07-24'),

('Anh Hùng','T13',112,'Phim hành động về một người đàn ông bình thường trở thành anh hùng.','2026-06-24','2026-07-24'),

('Đại Tiệc Trăng Máu 8','T16',115,'Phần mới của series hài đen nổi tiếng.','2026-06-30','2026-07-30'),

('Michael','T13',130,'Phim tiểu sử về huyền thoại âm nhạc Michael Jackson.','2026-06-26','2026-07-26'),

('Mortal Kombat 2','T16',120,'Phần tiếp theo của loạt phim hành động dựa trên game Mortal Kombat.','2026-06-15','2026-07-15'),

('Thời Khắc Công Bố','T13',105,'Phim tâm lý về bí mật được tiết lộ vào phút cuối.','2026-06-20','2026-07-20'),

('Madam Thanh Lạc','T13',110,'Phim cổ trang Việt Nam xoay quanh hai người phụ nữ quyền lực.','2026-06-06','2026-08-06'),

('Supergirl','T13',125,'Bom tấn siêu anh hùng DC về Supergirl.','2026-06-26','2026-08-26');

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


-- Add Showtimes --
INSERT INTO showtimes(movie_id,theater_room_id,type_ticket_id,time_slot_id,dayshow) VALUES

-- 16/03
(1,1,1,900,'2026-03-16'),
(2,2,1,1115,'2026-03-16'),
(3,3,1,1330,'2026-03-16'),
(3,2,2,1545,'2026-03-16'),
(4,1,1,1800,'2026-03-16'),
(6,3,1,2015,'2026-03-16'),
(7,1,1,2230,'2026-03-16'),
(7,2,2,900,'2026-03-16'),
(8,3,1,1115,'2026-03-16'),
(9,1,1,1330,'2026-03-16'),
(10,2,1,1545,'2026-03-16'),
(10,3,2,1800,'2026-03-16'),
(11,1,1,2015,'2026-03-16'),
(5,5,5,2030,'2026-03-16'), -- IMAX
(5,6,5,2230,'2026-03-16'), -- IMAX

-- 17/03
(1,2,1,900,'2026-03-17'),
(2,3,1,1115,'2026-03-17'),
(3,1,1,1330,'2026-03-17'),
(3,2,2,1545,'2026-03-17'),
(4,3,1,1800,'2026-03-17'),
(6,1,1,2015,'2026-03-17'),
(7,2,1,2230,'2026-03-17'),
(7,3,2,900,'2026-03-17'),
(8,1,1,1115,'2026-03-17'),
(9,2,1,1330,'2026-03-17'),
(10,3,1,1545,'2026-03-17'),
(10,1,2,1800,'2026-03-17'),
(11,2,1,2015,'2026-03-17'),

-- 18/03
(1,3,1,900,'2026-03-18'),
(2,1,1,1115,'2026-03-18'),
(3,2,1,1330,'2026-03-18'),
(3,3,2,1545,'2026-03-18'),
(4,1,1,1800,'2026-03-18'),
(6,2,1,2015,'2026-03-18'),
(7,3,1,2230,'2026-03-18'),
(7,1,2,900,'2026-03-18'),
(8,2,1,1115,'2026-03-18'),
(9,3,1,1330,'2026-03-18'),
(10,1,1,1545,'2026-03-18'),
(10,2,2,1800,'2026-03-18'),
(11,3,1,2015,'2026-03-18'),

-- 19/03
(1,1,1,900,'2026-03-19'),
(2,2,1,1115,'2026-03-19'),
(3,3,1,1330,'2026-03-19'),
(3,1,2,1545,'2026-03-19'),
(4,2,1,1800,'2026-03-19'),
(6,3,1,2015,'2026-03-19'),
(7,1,1,2230,'2026-03-19'),
(7,2,2,900,'2026-03-19'),
(8,3,1,1115,'2026-03-19'),
(9,1,1,1330,'2026-03-19'),
(10,2,1,1545,'2026-03-19'),
(10,3,2,1800,'2026-03-19'),
(11,1,1,2015,'2026-03-19'),

-- 20/03
(1,2,1,900,'2026-03-20'),
(2,3,1,1115,'2026-03-20'),
(3,1,1,1330,'2026-03-20'),
(3,2,2,1545,'2026-03-20'),
(4,3,1,1800,'2026-03-20'),
(6,1,1,2015,'2026-03-20'),
(7,2,1,2230,'2026-03-20'),
(7,3,2,900,'2026-03-20'),
(8,1,1,1115,'2026-03-20'),
(9,2,1,1330,'2026-03-20'),
(10,3,1,1545,'2026-03-20'),
(10,1,2,1800,'2026-03-20'),
(11,2,1,2015,'2026-03-20'),

-- 21/03
(1,3,1,900,'2026-03-21'),
(2,1,1,1115,'2026-03-21'),
(3,2,1,1330,'2026-03-21'),
(3,3,2,1545,'2026-03-21'),
(4,1,1,1800,'2026-03-21'),
(6,2,1,2015,'2026-03-21'),
(7,3,1,2230,'2026-03-21'),
(7,1,2,900,'2026-03-21'),
(8,2,1,1115,'2026-03-21'),
(9,3,1,1330,'2026-03-21'),
(10,1,1,1545,'2026-03-21'),
(10,2,2,1800,'2026-03-21'),
(11,3,1,2015,'2026-03-21'),

-- 22/03
(1,1,1,900,'2026-03-22'),
(2,2,1,1115,'2026-03-22'),
(3,3,1,1330,'2026-03-22'),
(3,1,2,1545,'2026-03-22'),
(4,2,1,1800,'2026-03-22'),
(6,3,1,2015,'2026-03-22'),
(7,1,1,2230,'2026-03-22'),
(7,2,2,900,'2026-03-22'),
(8,3,1,1115,'2026-03-22'),
(9,1,1,1330,'2026-03-22'),
(10,2,1,1545,'2026-03-22'),
(10,3,2,1800,'2026-03-22'),
(11,1,1,2015,'2026-03-22'),

-- IMAX suất cuối
(5,5,5,1800,'2026-03-22'); 

