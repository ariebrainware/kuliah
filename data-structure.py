# # Dynamic List of Years

first_year = int(input("Masukkan awal tahun: "))
limit = int(input("Masukkan limit tahun: "))
list_year = []
list_year.append(first_year)
for i in range(limit):
    first_year += 1
    list_year.append(first_year)
print(list_year)

# # Dynamic 2 years with validation/filter
print("=== Silahkan pilih maksimal 2 tahun dari list tahun diatas ===")
selected_year = input("Pilih 2 tahun: ")
a = selected_year.split(",")
y = []
for x in a:
    y.append(int(x))


def checkyear(year):
    x = list_year
    if (year in x):
        return True
    else:
        return False


filtered_year = filter(checkyear, y)
res = []
for s in filtered_year:
    res.append(s)
print("Tahun yang dipilih adalah: ", res)


# Array with 10 length limit
array_input = input("Masukkan array [Maksimal 10, koma sebagai pemisah]: ")
a = array_input.split(",")
print("Anda memasukkan: ", a)


def search(keyword):
    if (keyword in a):
        print("Ada, item dengan index: ", a.index(keyword))
    else:
        print("Tidak ada")


def edit(keyword, text2):
    if (keyword in a):
        a[a.index(keyword)] = text2
        print("Berhasil mengganti item array: ", a)
    else:
        print("Maaf anda memasukkan item yang tidak terdaftar")


def delete(keyword):
    if (keyword in a):
        a.remove(keyword)
        print("Berhasil menghapus item array: ", keyword)
        print(a)
    else:
        print("Maaf anda memasukkan item yang tidak terdaftar")


print("------------------------")
search("jeruk")
print("------------------------")
edit("anggur", "lemon")
print("------------------------")
delete("mangga")
