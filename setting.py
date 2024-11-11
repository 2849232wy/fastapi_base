TORTOISE_ORM = {
    "connections": {
        "default": "mysql://root:123456@localhost:3306/testdatabase"
    },
    "apps": {
        "models": {
            "models": ["Student.models", "aerich.models"],
            "default_connection": "default"  # 确保这是一个字符串
        }
    }
}