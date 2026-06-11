staffs = []

def total_income_staff(basic_salary, work_day, allowance):
    return (basic_salary * work_day) + allowance


def classify_salary(total_income):
    if total_income < 9_000_000:
        return "Thấp"
    elif total_income < 15_000_000:
        return "Trung bình"
    elif total_income < 30_000_000:
        return "Khá"
    else:
        return "Cao"


def find_staff_id(st_id):
    for staff in staffs:
        if staff["ID"] == st_id:
            return st_id
    print("Không tìm thấy id nhân viên")

def display_staff():

    if not staffs:
        print("Chưa có nhân viên nào")
        return

    print(
        f"{'ID':<10}",
        f"{'Tên nhân viên':<18}",
        f"{'Lương cơ bản':<25}"
        f"{'Số ngày làm việc':<18}"
        f"{'Phụ Cấp':<10}"
        f"{'Tổng thu nhập':<15}"
        f"{'Phân loại':<10}"
    )

    for s in staffs:
        print(
            f"{s['ID']:<10}"
            f"{s['name']:<10}"
            f"{s['basic_salary']:<10}"
            f"{s['work_day']:<10}"
            f"{s['allowance']:<10}"
            f"{s['total_income']:<10}"
            f"{s['classify']:<10}"
        )

def input_staff_id():
    while True:
        st_id = input("Nhập id của nhân viên: ").strip()

        if st_id:
            return st_id
        print("Không được để trống ID")

def input_name_staff():
    while True:
        name = input("Nhập tên nhân viên: ").strip()

        if name:
            return name
        print("Tên không được để trống")

def input_basic_salary_staff():
    while True:
        try:
            basic_salary = float(input("Nhập lương cơ bản nhân viên: ").strip())

            if basic_salary >= 0:
                return basic_salary
            print("Lương cơ bản không được nhỏ hơn 0")

        except ValueError:
            print("Lương cơ bản không hợp lệ")

def input_work_day_staff():
    while True:
        try:
            work_day = int(input("Nhập số ngày làm việc của nhân viên: ").strip())

            if work_day >= 0:
                return work_day
            print("Số ngày làm việc không được nhỏ hơn 0")

        except:
            print("Số ngày làm việc không hợp lệ")

def input_allowance_staff():
    while True:
        try:
            allowance = float(input("Nhập phụ cấp của nhân viên: ").strip())

            if allowance >= 0:
                return allowance
            print("Phụ cấp phải lớn hơn 0")

        except:
            print("Phụ cấp không hợp lệ")

def add_staff(data = None):

    if data is None:
        data = staffs

    print("Nhập thông tin nhân viên")

    st_id = input_staff_id()
    name = input_name_staff()
    basic_salary = input_basic_salary_staff()
    work_day = input_work_day_staff()
    allowance = input_allowance_staff()
    total_income = total_income_staff(basic_salary, work_day, allowance)
    classify = classify_salary(total_income)

    staff = {
        "ID": st_id,
        "name": name,
        "basic_salary": basic_salary,
        "work_day": work_day,
        "allowance": allowance,
        "total_income": total_income,
        "classify": classify,
    }

    staffs.append(staff)
    print("Thêm nhân viên thành công")

def update_staff():

    if not staffs:
        print("Không có nhân viên nào")
        return


    st_id = input("Nhập id nhân viên cần sửa: ").strip()

    staff = find_staff_id(st_id)

    if not staff:
        print("Id nhân viên không hợp lệ")
        return

    print("Nhập thông tin mới")

    name = input_name_staff()
    work_day = input_work_day_staff()
    basic_salary = input_basic_salary_staff()
    allowance = input_allowance_staff()
    total_income = total_income_staff(basic_salary, work_day, allowance)
    classify = classify_salary(total_income)

    staff["name"] = name
    staff["work_day"] = work_day
    staff["basic_salary"] = basic_salary
    staff["allowance"] = allowance
    staff["total_income"] = total_income
    staff["classify"] = classify

    print("Sửa nhân viên thành công")

def delete_staff():

    if not staffs:
        print("Không có nhân viên nào")
        return

    st_id = input("Nhập id nhân viên cần sửa: ")

    staff = find_staff_id(st_id)

    if not staff:
        print("Id nhân viên không hợp lệ")
        return

    confim = input("Bạn có chắc muốn xóa nhân viên (Y / N): ").strip().lower()

    if confim == "Y":
        staffs.remove(staff)
        print("Đã xóa nhân viên thành công")
    else:
        print("Dừng xóa nhân viên")

def search_staff():

    if not staffs:
        print("Không có nhân viên nào")
        return

    print("1.Tìm nhân viên theo ID")
    print("2. Tìm nhân viên theo tên")

    choice = input("Nhập lựa chọn của bạn: ").strip()

    match choice:
        case "1":
            st_id = input("Nhập id bạn muốn tìm: ")
            staff = find_staff_id(st_id)
            if staff:
                display_staff()
            print("Không tìm thấy ID nhân viên")

        case "2":
            keyword = input("Nhập tên nhân viên cần tìm: ").strip().lower()


        case _:
            print("Lựa chọn không hợp lệ")

def classify_salary_staff():

    if not staffs:
        print("Không có nhân viên nào")
        return



    low = 0
    medium = 0
    big = 0
    very_big = 0



while True:
    print("Quản lí nhân viên")
    print("1. Hiển thị danh sách nhân viên")
    print("2. Thêm nhân viên mới")
    print("3. Cập nhập nhân viên")
    print("4. Xóa nhân viên")
    print("5. Tìm kiếm nhân viên")
    print("6. Thống kê quỹ lương")
    print("7. Phân loại nhân viên")
    print("8. Thoát")

    choice = input("Nhập lựa chọn của bạn: ").strip()

    match choice:
        case "1":
            display_staff()
        case "2":
            add_staff()
        case "3":
            update_staff()
        case "4":
            delete_staff()
        case "5":
            search_staff()
        case "6":
            classify_salary_staff()
        case "7":
            pass
        case "8":
            print("Thoát chương trình")
            break
        case _:
            print("Lựa chọn không hợp lệ")


