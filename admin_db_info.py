# Ambil value password
def get_current_mysql_password():
    with open("admin_db_info.txt") as file:
        content = file.readlines()
        current_password = content[2].split("=", 1)[1].strip().strip('"')
        
    return current_password if current_password.strip() else ""