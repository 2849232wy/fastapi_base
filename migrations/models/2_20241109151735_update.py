from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `student` ADD `password` VARCHAR(50) NOT NULL;
        ALTER TABLE `teacher` ADD `password` VARCHAR(50) NOT NULL;
        ALTER TABLE `student` ADD UNIQUE INDEX `uid_student_email_e7143f` (`email`);
        ALTER TABLE `teacher` ADD UNIQUE INDEX `uid_teacher_email_09e362` (`email`);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `teacher` DROP INDEX `idx_teacher_email_09e362`;
        ALTER TABLE `student` DROP INDEX `idx_student_email_e7143f`;
        ALTER TABLE `student` DROP COLUMN `password`;
        ALTER TABLE `teacher` DROP COLUMN `password`;"""
