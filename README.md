# Extending-jieba-dict

1.先用 grep --color=auto 'title' wiki_aftercc >> titles
  →我是從轉換繁簡後的資料找有關title的字
  titles長這樣↓
     <doc id="2804006" url="https://zh.wikipedia.org/wiki?curid=2804006" title="九老車輛基地">
     <doc id="2804009" url="https://zh.wikipedia.org/wiki?curid=2804009" title="紋首矮長頜魚">
     <doc id="2804015" url="https://zh.wikipedia.org/wiki?curid=2804015" title="餅店車輛基地">
     <doc id="2804016" url="https://zh.wikipedia.org/wiki?curid=2804016" title="司徒夢巖">
     <doc id="2804017" url="https://zh.wikipedia.org/wiki?curid=2804017" title="伊氏矮長頜魚">
     <doc id="2804024" url="https://zh.wikipedia.org/wiki?curid=2804024" title="峯上巡檢司城">
2.再用creatitle.py將title後的字截出來
  extra_dict長這樣↓
    洛思加圖斯 nz
    米爾皮塔斯 nz
    蒙堤聖利諾 nz
    王冠 nz
    藪中三十二 nz
    許敦仁 nz
    林霆 nz
    獨指花鮨 nz
    凌源市實驗中學 nz
3.最後在TermPOSTokenizer.py 加入
   jieba.load_userdict("extra_dict.txt")
