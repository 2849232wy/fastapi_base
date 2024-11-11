from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `course` ADD `major_id` INT NOT NULL;
        ALTER TABLE `course` ADD `add` VARCHAR(50) NOT NULL  DEFAULT '';
        CREATE TABLE IF NOT EXISTS `major` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL
) CHARACTER SET utf8mb4;
        ALTER TABLE `course` ADD CONSTRAINT `fk_course_major_3f338be8` FOREIGN KEY (`major_id`) REFERENCES `major` (`id`) ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `course` DROP FOREIGN KEY `fk_course_major_3f338be8`;
        ALTER TABLE `course` DROP COLUMN `major_id`;
        ALTER TABLE `course` DROP COLUMN `add`;
        DROP TABLE IF EXISTS `major`;"""
