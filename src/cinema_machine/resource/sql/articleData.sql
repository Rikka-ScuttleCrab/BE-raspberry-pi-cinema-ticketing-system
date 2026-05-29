Drop Database managerapplication;


Use managerapplication;

INSERT INTO roles(role_name, description) VALUES
("Reader", "Người đọc"),
("Editor", "Biên tập viên"),
("Author", "Tác giả"),
("Admin", "Quản trị viên"),
("Staff", "Nhân viên");

-- INSERT INTO categories(category_name) VALUES
-- ("Game"),
-- ("Công Nghệ"),
-- ("Thể Thao");


INSERT INTO users(username, password_hash, gender, email, nickname) VALUES
("karin","$2a$10$M6xvmoyqQbncTzZP9aFUsOPSDMa2M1Hi6RbozRGWk6UizvG.UwARG", "FEMALE","ekari@gmail.com", "Corin"),
("endmin","$2a$10$e67bYaspGN2kDjS66GCtP.M71usrhrjyMx.vY/Nv7i2ffHFa4AxKK", "FEMALE","endmin@gmail.com", "Endministrator"),
("reader01","$2a$10$3WiTGGLOuicmtMwsqWLW7.qXP/9YnTNzZC7YW8wGJcEBpSeJtGv.a", "MALE","reader01@gmail.com", "reader01"),
("reader02","$2a$10$XhM5KtVrcvu7Dm417pfRIOkaSL2DLErmiLhZ8RRL8NAxisjR8QM0W", "MALE","reader02@gmail.com", "reader02"),
("reader03","$2a$10$vjnWdNhPEqj/mbkYP5UFRenAOUMQRXPEeZR7w.kUdhTdF0.G/8Thi", "FEMALE","reader03@gmail.com", "reader03"),
("author01","$2a$10$NoR5of4ty4GVHnhv78E/6.T.tcVAYBfqDPDIyddvIbTN4kRjWrJCG", "FEMALE","author01@gmail.com", "author01"),
("author02","$2a$10$1tD8xrBX24Aoxc7y67x.i.Bl3TRudhoqCAElnvBpT69e999LM9AXi", "MALE","author02@gmail.com", "author02"),
("editor01","$2a$10$glK8RDp0psvqe1xfh9bCKeZO2bvFT32z8OVMXfWJ9jnkD19fPGiw6", "MALE","editor01@gmail.com", "editor01"),
("editor02","$2a$10$XSK2P2ZTvFpJjX49sv29Gu/6VJ2X3ty4YVeHVuqxogIZGYD2IMKbG", "FEMALE","editor02@gmail.com", "editor02");


INSERT INTO permissions(permission_name, permission_action, permissionDescription, description) VALUES 

-- author permissions --
("post-news", "VIEW", "Trang đăng báo", "Quyền truy cập và xem trang đăng báo"),
("post-news", "UPDATE", "Trang đăng báo", "Quyền chỉnh sửa trang đăng báo"),
("articles", "CREATE", "Báo", "Quyền tạo và đăng báo mới"),
("articles", "UPDATE", "Báo", "Quyền chỉnh sửa báo cũ"),

-- editor permissions --
("approve", "VIEW", "Trang duyệt báo", "Quyền truy cập và xem trang quản lý duyệt báo"),
("approve", "UPDATE", "Trang duyệt báo", "Quyền chỉnh sửa trang quản lý duyệt báo"),
("articles", "DELETE", "Báo", "Quyền xoá báo cũ"),
("articles", "APPROVE", "Báo", "Quyền phê duyệt báo"),

-- admin dashboard --
("admin", "VIEW", "Trang Admin Dashboard", "Quyền truy cập và xem trang quản lý hệ thống"),
("admin", "UPDATE", "Trang Admin Dashboard", "Quyền chỉnh sửa trang quản lý hệ thống"),


-- admin user management
("users", "GET", "Trang quản lý người dùng", "Quyền lấy thông tin toàn bộ người dùng"),
("users", "VIEW", "Trang quản lý người dùng", "Quyền truy cập và xem thông tin toàn bộ người dùng"),
("users", "CREATE", "Trang quản lý người dùng", "Quyền thêm người dùng mới"),
("users", "UPDATE", "Trang quản lý người dùng", "Quyền thay đổi thông tin người dùng khác"),
("users", "ACTIVE", "Trang quản lý người dùng", "Quyền vô hiệu hoá/ kích hoạt tài khoản người dùng"),
("users", "ROLE", "Trang quản lý người dùng", "Quyền phân nhóm cho người dùng"),

-- admin role management
("roles", "GET", "Trang quản lý nhóm người dùng", "Quyền lấy thông tin các nhóm người dùng"),
("roles", "VIEW", "Trang quản lý nhóm người dùng", "Quyền truy cập và xem thông tin các nhóm người dùng"),
("roles", "CREATE", "Trang quản lý nhóm người dùng", "Quyền tạo nhóm người dùng mới"),
("roles", "UPDATE", "Trang quản lý nhóm người dùng", "Quyền thay đổi thông tin nhóm người dùng"),
("roles", "DELETE", "Trang quản lý nhóm người dùng", "Quyền xoá nhóm người dùng"),

-- admin user management
("permissions", "GET", "Trang phân quyền nhóm người dùng", "Quyền lấy thông tin các quyền"),
("permissions", "VIEW", "Trang phân quyền nhóm người dùng", "Quyền xem thông tin của các quyền"),
("permissions", "CREATE", "Trang phân quyền nhóm người dùng", "Quyền tạo các quyền mới"),
("permissions", "UPDATE", "Trang phân quyền nhóm người dùng", "Quyền thay đổi thông tin quyền");


INSERT INTO user_role (role_id, user_id)
SELECT 1, id
FROM users;

INSERT INTO user_role (role_id, user_id) VALUES 
(4, 1), (4, 2),
(3, 6), (3, 7),
(2, 8), (2, 9);




INSERT INTO permission_role(role_id, permission_id) VALUES 
(3, 1), (3, 2), (3, 3), (3, 4),
(2, 5), (2, 6), (2, 7), (2, 8);

INSERT INTO permission_role(role_id, permission_id)
SELECT 4, id
FROM permissions
WHERE id BETWEEN 9 AND 25;






















DELIMITER $$

CREATE PROCEDURE generate_users()
BEGIN
    DECLARE i INT DEFAULT 1;

    WHILE i <= 100 DO

        INSERT INTO users(
            username,
            password_hash,
            gender,
            email,
            nickname
        )
        VALUES (
            CONCAT('user', LPAD(i, 3, '0')),
            '$2a$10$M6xvmoyqQbncTzZP9aFUsOPSDMa2M1Hi6RbozRGWk6UizvG.UwARG',
            IF(MOD(i, 2) = 0, 'FEMALE', 'MALE'),
            CONCAT('user', LPAD(i, 3, '0'), '@gmail.com'),
            CONCAT('User', LPAD(i, 3, '0'))
        );

        SET i = i + 1;

    END WHILE;
END$$

DELIMITER ;

CALL generate_users();







