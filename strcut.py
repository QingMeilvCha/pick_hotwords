import jieba

seg_list = jieba.cut("子曰食无求饱，居无求安，敏于事而慎于言，就有道而正焉，可谓好学也已。", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("子曰食无求饱，居无求安，敏于事而慎于言，就有道而正焉，可谓好学也已。", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

# seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
# print(", ".join(seg_list))

# seg_list = jieba.cut_for_search("RNG上单Aj打的真菜")  # 搜索引擎模式
# print("/ ".join(seg_list))