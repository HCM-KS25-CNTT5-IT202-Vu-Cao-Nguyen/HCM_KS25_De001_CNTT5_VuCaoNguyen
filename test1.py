def input_staff_id():
    while True:
        st_id = input("Nhập id của nhân viên: ").strip()

        if st_id:
            return st_id
        print("Không được để trống ID")

input_staff_id()