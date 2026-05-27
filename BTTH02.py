""" 
    phân tích và thiết kế giải pháp:
        + Input:
            + giá trị nhập lựa chọn menu 
            + Chức năng 1:
                + Nhập tên bài hát nếu chức năng 1 
                + Nhập thêm cả chỉ số nếu chức năng 2
            + Chức năng 3:
                + nhập tên bài hát nếu chức năng 1
                + nhập số thứ tự nếu là chức năng 2
            
        + Output:
            + Chức năng 1: 
                + thông báo đã thêm phần tử thành công
            + Chức năng 2: 
                + Hiển thị danh sách đã được định dạng và căn lề 
            + Chức năng 3:
                + Thông báo đã xóa thành công !
            + Chức năng 4:
                + Thông báo sắp xếp thành công và hiển thị danh sách đó
                
        + Đề xuất giải pháp:
            + Ở phần menu ta sử dụng vòng while với điều kiện True
            + NẾU NGƯỜI DÙNG NHẬP CHỮ CÁI HOẶC NHẬP NGOÀI CHỨC NĂNG 
            => BÁO LỖI CHO CHƯƠNG TRÌNH VÀ CHO NHẬP LẠI 
            + Chức năng 1:
                + chức năng 1.1
                    + cho người dùng nhập tên bài hát mà người dùng muốn thêm
                + Chức năng 1.2
                    + Cho người dùng nhập vị trí mà người dùng muốn thêm cũng như tên bài hát sau khi vị trí hợp lệ
            + Chức năng 2:
                + Cho người dùng thấy được danh sách phát nhạc
            + Chức năng 3:
                Cho người dùng hiện menu xóa
                    + Chức năng 3.1
                        + cho người dùng nhập tên bài muốn xóa
                    + Chức năng 3.2
                        + Cho người dùng nhập vị trí mà muốn xóa
            + Chức năng 4: Cho người dùng nhập 2 chức năng
                + Chức năng 4.1:
                    + Sắp xếp được danh sách nhạc
                + Chức năng 2:
                    + lấy 3 nhạc đầu tiên
            + Chức năng 5: Bye
            
        + Thiết kế thuật toán :
            + Khi vừa vào mình sẽ in ra menu cho người dùng 
                + với mỗi chức năng mình ấn thì mình sẽ thực hiện chức năng tương ứng với 
                người dùng
                + sau khi sử dụng chức năng đó thì cho người dùng quay lại menu 
                và nhập lại đến khi nhập chức năng thoát thì kết thức chương trình
        + BẪY
            + BẪY 1: NẾU NGƯỜI DÙNG CHỌN CHỨC NĂNG 2 , 3 , 4 KHI DANH SÁCH ĐANG KHÔNG CÓ BÀI HÁT NÀO
            => THÔNG BÁO DANH SÁCH TRỐNG VÀ QUAY VỀ MENU
            + BÂY 2: NẾU NGƯỜI DÙNG XÓA TÊN BÀI HÁT KHÔNG CÓ TRONG DANH SÁCH PHÂN BIỆT HOA THƯỜNG
            =>  THÔNG BÁO KHÔNG TÌM THẤY BÀI HÁT TRONG DANH SÁCH
            + BẪY 3: NẾU NGƯỜI DÙNG CHÈN HOẶC XÓA BÀI HÁT KTHEO SỐ THỰ TỰ SAI THÌ TA 
            => VỊ TRÍ LỚN HƠN ĐỘ DÀI DANH SÁCH VÀ LÀ SỐ ÂM => CHO NGƯỜI DÙNG NHẬP LẠI
            + BẪY 3: NẾU NGƯỜI DÙNG NHẬP SAI CHỨC NĂNG NGOÀI VÙNG CÙNG NHƯ NHẬP CHỮ CÁI
            => THÔNG BÁO PHẢI THUỘC TỪ 1- > 5  
            
"""
disk_items = ["Shape of you", "Blinding Lights", "Perfect", "Cỏ May", "23:40", "Một Nửa Sự Thật", "Nội Dung Nhạy Cảm"]
LINE = "="*60
import time 
while True:
    try: 
        choose = int(input(
        f"{LINE}\n"
        f"{"MENU QUẢN LÝ DANH SÁCH PHÁT".center(60, " ")} \n"
        f"{LINE}\n"
        f"{"[1]. Thêm bài hát vào danh sách phát".ljust(60, " ")} \n"
        f"{"[2]. Xem danh sách phát".ljust(60, " ")} \n"
        f"{"[3]. Xóa bài hát khỏi danh sách".ljust(60, " ")} \n"
        f"{"[4]. Sắp xếp và trích xuất danh sách".ljust(60, " ")} \n"
        f"{"[5]. Thoát chương trình".ljust(60, " ")} \n"
        f"{LINE}\n"
        f"> Lựa chọn chức năng: "        
        ))
    except:
        print("Lỗi nhập không khớp với dữ liệu")
        continue 
    match choose:
        case 1:
            if(len(disk_items) <= 0):
                print("Danh sách rỗng")
            else:
                print()
                while True:
                    try: 
                        choose2 = int(input(
                        f"{LINE}\n"
                        f"{"THÊM BÀI HÁT".center(60, " ")} \n"
                        f"{LINE}\n"
                        f"{"[1]. Thêm vào cuối danh sách".ljust(60, " ")} \n"
                        f"{"[2]. Chèn vào vị trí cụ thể".ljust(60, " ")} \n"
                        f"{"[3]. Thoát khỏi chức năng này".ljust(60, " ")} \n"
                        f"{LINE}\n"
                        f"> Lựa chọn chức năng: "        
                        ))
                    except:
                        print("Lỗi nhập không khớp với dữ liệu")
                        continue
                    match choose2:
                        case 1:
                            print()
                            while True:
                                new_song = input("Vui lòng nhập bài hát mới: ")
                                if(not new_song.strip()):
                                    print("Tên bài hát không được để trống !")
                                    continue 
                                break
                            disk_items.append(new_song)
                            print(f"Thêm bài hát {new_song} thành công !")
                            print()
                        case 2 :
                            while True:
                                try:
                                    index_wanna_insert = int(input(f"Vui lòng nhập vị trí từ (0 -> {(len(disk_items))-1}): "))
                                except:
                                    print("Giá trị không khớp với dữ liệu")
                                    continue
                                if(index_wanna_insert < 0 or index_wanna_insert > len(disk_items)-1):
                                    print("Vị trí chèn không hợp lệ !")
                                    continue 
                                break 
                            while True:
                                new_song = input("Vui lòng nhập bài hát mới: ")
                                if(not new_song.strip()):
                                    print("Tên bài hát không được để trống !")
                                    continue 
                                break
                            disk_items.insert(index_wanna_insert, new_song)
                            print(f"Thêm bài hát {new_song} thành công !")
                        case 3:
                            break
                        case _:
                            print("Chức năng lựa chọn không phù hợp !")
                print()
        case 2:
            print()
            print(f"{"DANH SÁCH PHÁT".center(63, "-")}")
            if(len(disk_items) <= 0):
                print("Danh sách rỗng")
            else:
                print(f"{"STT":<10} | {"Tên bài hát":<50}")
                print("-".center(63, "-"))
                for index, value in enumerate(disk_items):
                    print(f"{(index + 1):<10} | {value:<50}")
                
            print("-".center(63,"-"))
            print()
        case 3:
            print()
            if(len(disk_items) <= 0):
                print("Danh sách rỗng")
            else:
                while True:
                    try: 
                        choose2 = int(input(
                        f"{LINE}\n"
                        f"{"XÓA BÀI HÁT".center(60, " ")} \n"
                        f"{LINE}\n"
                        f"{"[1]. Xóa theo tên bài hát".ljust(60, " ")} \n"
                        f"{"[2]. Xóa theo số thứ tự".ljust(60, " ")} \n"
                        f"{"[3]. Thoát khỏi chức năng này".ljust(60, " ")} \n"
                        f"{LINE}\n"
                        f"> Lựa chọn chức năng: "        
                        ))
                    except:
                        print("Lỗi nhập không khớp với dữ liệu")
                        continue
                    match choose2:
                        case 1:
                            hasdel = False 
                            print()
                            while True:
                                dell_song = input("Vui lòng nhập bài hát cần xóa: ")
                                if(not dell_song.strip()):
                                    print("Tên bài hát không được để trống !")
                                    continue 
                                break
                            
                            try:
                                disk_items.remove(dell_song)
                            except:
                                hasdel = True
                            if not hasdel:
                                print(f"Xóa bài hát {dell_song} khỏi danh sách")
                            else:
                                print(f"Không có tên bài hát {dell_song} trong danh sách")
                            print()
                        case 2 :
                            while True:
                                try:
                                    index_wanna_delete = int(input(f"Vui lòng nhập vị trí từ (1 -> {len(disk_items)}) muốn xóa: "))
                                except:
                                    print("Giá trị không khớp với dữ liệu")
                                    continue
                                if(index_wanna_delete < 1 or index_wanna_delete > len(disk_items)):
                                    print("Vị trí xóa không hợp lệ !")
                                    continue 
                                break 
                            current_song = disk_items.pop(index_wanna_delete -1)
                            print(f"xóa bài hát {current_song} thành công !")
                        case 3:
                            break
                        case _:
                            print("Chức năng lựa chọn không phù hợp !")
                print()
        case 4:
            if(len(disk_items) <= 0):
                print("Danh sách rỗng")
            else:
                print()
                while True:
                    try: 
                        choose3 = int(input(
                        f"{LINE}\n"
                        f"{"SẮP XẾP VÀ TRÍCH XUẤT DANH SÁCH".center(60, " ")} \n"
                        f"{LINE}\n"
                        f"{"[1]. Sắp xếp danh sách pháp theo bảng chữ cái A-Z".ljust(60, " ")} \n"
                        f"{"[2]. Hiển thị 3 bài hát đầu tiên".ljust(60, " ")} \n"
                        f"{"[3]. Thoát khỏi chức năng này".ljust(60, " ")} \n"
                        f"{LINE}\n"
                        f"> Lựa chọn chức năng: "        
                        ))
                    except:
                        print("Lỗi nhập không khớp với dữ liệu")
                        continue
                    match choose3:
                        case 1:
                            print()
                            new_sort = sorted(disk_items)
                            print("sắp xếp thành công ")
                            print()
                            print(f"{"DANH SÁCH PHÁT ĐÃ ĐƯỢC SẮP XẾP".center(63, "-")}")
                            if(len(new_sort) <= 0):
                                print("Danh sách rỗng")
                            else:
                                print(f"{"STT":<10} | {"Tên bài hát":<50}")
                                print("-".center(63, "-"))
                                for index, value in enumerate(new_sort):
                                    print(f"{(index + 1):<10} | {value:<50}")
                                
                            print("-".center(63,"-"))
                            print()
                        case 2 :
                            print()
                            print(f"{"TRÍCH XUẤT 3 BÀI HÁT ĐÀU TIÊN".center(63, "-")}")
                            if(len(disk_items) <= 0):
                                print("Danh sách rỗng")
                            else:
                                print(f"{"STT":<10} | {"Tên bài hát":<50}")
                                print("-".center(63, "-"))
                                for index, value in enumerate(disk_items):
                                    if(index == 3):
                                        break
                                    print(f"{(index + 1):<10} | {value:<50}")
                                
                            print("-".center(63,"-"))
                            print()
                        case 3:
                            break
                        case _:
                            print("Chức năng lựa chọn không phù hợp !")
                print()
        case 5:
            print()
            message = "Tạm biệt, Chương trình sẽ hủy ngay sau: "
            for letter in message:
                print(letter, end = "", flush=True)
                time.sleep(0.09)
            count = 5
            print()
            time.sleep(0.05)
            while count > 0:
                print(count, end = "\r")
                time.sleep(1)
                count -= 1
            print("BYE :>")
            break
        case _:
            print("Không có chức năng này !")
