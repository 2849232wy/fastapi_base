from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `clas` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `course` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `score` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `score` DOUBLE NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `teacher` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL,
    `age` INT NOT NULL,
    `email` VARCHAR(50) NOT NULL,
    `tno` VARCHAR(50) NOT NULL UNIQUE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `student` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL,
    `age` INT NOT NULL,
    `email` VARCHAR(50) NOT NULL,
    `sno` VARCHAR(50) NOT NULL UNIQUE,
    `teacher_id` INT NOT NULL,
    CONSTRAINT `fk_student_teacher_d0fc6994` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `clas_course` (
    `clas_id` INT NOT NULL,
    `course_id` INT NOT NULL,
    FOREIGN KEY (`clas_id`) REFERENCES `clas` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`course_id`) REFERENCES `course` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_clas_course_clas_id_da02a8` (`clas_id`, `course_id`)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `score_student` (
    `score_id` INT NOT NULL,
    `student_id` INT NOT NULL,
    FOREIGN KEY (`score_id`) REFERENCES `score` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`student_id`) REFERENCES `student` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_score_stude_score_i_13f62c` (`score_id`, `student_id`)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `score_course` (
    `score_id` INT NOT NULL,
    `course_id` INT NOT NULL,
    FOREIGN KEY (`score_id`) REFERENCES `score` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`course_id`) REFERENCES `course` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_score_cours_score_i_bf64e1` (`score_id`, `course_id`)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `teacher_clas` (
    `teacher_id` INT NOT NULL,
    `clas_id` INT NOT NULL,
    FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`clas_id`) REFERENCES `clas` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_teacher_cla_teacher_7bd26a` (`teacher_id`, `clas_id`)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `teacher_course` (
    `teacher_id` INT NOT NULL,
    `course_id` INT NOT NULL,
    FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`course_id`) REFERENCES `course` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_teacher_cou_teacher_a5ae8d` (`teacher_id`, `course_id`)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `student_clas` (
    `student_id` INT NOT NULL,
    `clas_id` INT NOT NULL,
    FOREIGN KEY (`student_id`) REFERENCES `student` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`clas_id`) REFERENCES `clas` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_student_cla_student_6118fa` (`student_id`, `clas_id`)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `student_course` (
    `student_id` INT NOT NULL,
    `course_id` INT NOT NULL,
    FOREIGN KEY (`student_id`) REFERENCES `student` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`course_id`) REFERENCES `course` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_student_cou_student_0d222b` (`student_id`, `course_id`)
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
