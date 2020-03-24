import xlrd

class Read_Ex():
    def read_excel(self,filepath):
        #打开excel表，填写路径
        book = xlrd.open_workbook(filepath)
        # book = xlrd.open_workbook(r"E:\hugewarts\web_auto\comment\sheel.xls")
        #找到sheet页
        table = book.sheet_by_name("Sheet1")
        #获取总行数总列数
        row_Num = table.nrows
        col_Num = table.ncols

        s =[]
        key =table.row_values(0)# 这是第一行数据，作为字典的key值

        if row_Num <= 1:
            print("没数据")
        else:
            j = 1
            for i in range(row_Num-1):
                d ={}
                values = table.row_values(j)
                for x in range(col_Num):
                    # 把key值对应的value赋值给key，每行循环
                    d[key[x]]=values[x]
                j+=1
                # 把字典加到列表中
                s.append(d)
            return s





if __name__ == '__main__':
    r = Read_Ex()
    filepath = r"E:\hugewarts\web_auto\comment\sheel.xls"
    s=r.read_excel(filepath)
    print(s)
    list = [i for i in s]
    print(list)
    for i in s:
        print(i)
    print(s)









#
# import xlrd
# import xlwt
#
#
# class xlsUtil:
#     def read(self, path):
#         '''
#         :param path: string 文件路径
#         '''
#         workbook = xlrd.open_workbook(path)
#         data_sheet = workbook.sheets()[0]
#         row_num = data_sheet.nrows
#         col_num = data_sheet.ncols
#         data = []
#         for i in range(row_num):
#             row_data = []
#             for j in range(col_num):
#                 if (i == 0):
#                     continue
#                 row_data.append(data_sheet.cell_value(i, j))
#             data.append(row_data)
#         print(data)
#         return data
#
#     def write(self, data, header, out_path):
#         '''
#         :param data: array 表格数据
#         :param header: array 表头数据
#         :param out_path: string 输出路径
#         '''
#         wbk = xlwt.Workbook()
#         sheet = wbk.add_sheet('Sheet1', cell_overwrite_ok=True)
#         for i in range(len(header)):
#             sheet.write(0, i, header[i])
#         for row in range(len(data)):
#             for col in range(len(data[row])):
#                 sheet.write(row + 1, col, data[row][col])
#         print(out_path)
#         wbk.save(out_path)
#
#
# # test read and write
# if __name__ == '__main__':
#     xls_util = xlsUtil()
#     xls_util.read(r'E:\hugewarts\web_auto\comment\sheel.xls')
#     xls_util.write(
#                     [[1.0, '海底世界', '1.mp4', '1.png',
#                      'animal:动物,coral:珊瑚,crab:蟹,dolphin:海豚,jellyfish:水母,near:靠近,ocean:海洋,plant:植物,soft:软的,tail:尾巴',
#                      '神秘的海底世界，色彩斑斓，有好多好多的动物，海龟、海豚、海豹、水母…… 鲸是怎么跳得那么高的呢，一起去看看吧~', '免费'], [2.0, '沙滩上的一天', '2.mp4', '2.png',
#                                                                                         'brown:棕色的,cute:可爱,desk:书桌,great:美好的,late:晚的,seashell:贝壳,sky:天空,put:放,small:小的,star:星星',
#                                                                                         '沙滩，阳光，贝壳。我们会在沙滩上看到些什么呢？这一天的旅行是怎么度过呢？让我们一起度过这美好的一天吧。',
#                                                                                         '免费'], [
#                         3.0, '沙滩，我来了！', '3.mp4', '3.png',
#                         'beach:海滩,sea:海,shorts:短裤,summertime:夏日,swimsuit:泳衣,wave:波浪,wear:穿,sunscreen:防晒霜,tank top:背心,sunglasses:太阳眼镜',
#                         '炎炎夏日，最好的去处当然是沙滩啦。为了我们的沙滩旅行，我们需要准备些什么呢？在沙滩上，我们又会做些什么游戏呢？', '会员'],
#                     [4.0, '在度假中', '4.mp4', '4.png',
#                      'beach:海滩,having a picnic:吃野餐,hungry:饿的,sand:沙子,sea:海,looking at:看着,sitting on:坐在…上,looking for:寻找着,together:一起,yard:院子',
#                      '度假时间到了，让我们一去去逛逛，沙滩，花园，大海，让我们一起去看看我们小伙伴的度假时光吧。', '会员']],
#                    ['编号', '名称', '视频文件', '封面文件', '单词', '简介', '权限'], r'E:\hugewarts\web_auto\comment\sheel2.xls')
