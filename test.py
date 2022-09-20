import xlrd

# data = []
# readexcel = xlrd.open_workbook(r'./allpaper/words.xls', encoding_override='utf-8')
# sheet = readexcel.sheet_by_name('Sheet1')
# for i in range(0,20):
#     print('第', i+1, '行数据', sheet.row_values(i), sheet.row_values(i)[0])
#     data.append(sheet.row_values(i)[0])
# print(data)

import execjs

ctx = execjs.compile("""
        function add(x, y) {
                 alert("x + y");
           }
""")
res = ctx.call('add', 1, 2)
print(res)