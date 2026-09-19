
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    roll_no VARCHAR(30) NOT NULL UNIQUE,
    student_name VARCHAR(100) NOT NULL,
    department VARCHAR(50)
);
INSERT INTO students (roll_no, student_name, department)
VALUES
('101', 'Rahul Kumar', 'CSE'),
('102', 'Priya Sharma', 'CSE'),
('103', 'Amit Kumar', 'CSE'),
('104', 'Neha Singh', 'IT'),
('105', 'Rohan Gupta', 'IT'),
('106', 'Anjali Verma', 'AI'),
('107', 'Karan Singh', 'AI');

CREATE TABLE IF NOT EXISTS attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    attendance_date DATE NOT NULL,
    status ENUM('Present', 'Absent') NOT NULL,

    FOREIGN KEY (student_id)
        REFERENCES students(student_id)
        ON DELETE CASCADE,

    UNIQUE(student_id, attendance_date)
);
select*
from attendance;

# for login purposes
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('Admin', 'Teacher') NOT NULL,
    full_name VARCHAR(100) NOT NULL
);


INSERT INTO users (username, password, role, full_name) 
VALUES ('admin', 'admin123', 'Admin', 'HOD')
ON DUPLICATE KEY UPDATE username=username;


INSERT INTO users (username, password, role, full_name) 
VALUES ('teacher1', 'teacher123', 'Teacher', 'Adarsh Mishra')
ON DUPLICATE KEY UPDATE username=username;


