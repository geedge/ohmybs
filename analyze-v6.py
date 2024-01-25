import pandas as pd
from rich.progress import Progress

from analyzer import node

data = []
with Progress() as p:
    # inputdata = "./openIPv6dns.txt"
    inputdata="./recurisivev6dns.txt"
    print(len(open(inputdata).readlines()))
    task = p.add_task("[blue]Working...", total=sum(1 for _ in open(inputdata)))
    # exclist=["中国台湾","中国香港"]
    with open(inputdata, "r") as f:
        while True:
            l = f.readline()
            if l == "":
                break
            ip6 = l.splitlines()[0]
            n = node(ip6)
            p.update(task, advance=1, refresh=True)
            # if n.prov=="UnKnown":
            if n.isp=="UnKnown":
                continue
            # if n.cou=="中国" and n.prov not in exclist and "澳" not in n.isp:
            data.append({"ip": n.ip,
                        "owner": n.owner,
                        "isp": n.isp,
                        "area": n.prov,
                        "asn": n.AS,
                        "lat": n.lat,
                        "lng": n.lng,
                        "coucode":n.couCode,
                        "cou":n.cou})
d = pd.DataFrame(data)
import pygal 
# 地图可视化
#创建一个字典
print(d.shape[0])
cc = d['isp'].value_counts().to_dict()
# cc = d['area'].value_counts().to_dict()
# from pygal_maps_world.i18n import COUNTRIES
# def get_cc(ccname):
#     #根据指定的国家，返回Pygal使用的两个字母的国别码
#     for code,name in COUNTRIES.items():
#         if ccname in name :
#             return code
#     # 如果没有找到指定的国家，就返回None
#     return None

# cc_stats={}
# for pop_dic,pop_v in cc.items() :
#     country_name= pop_dic
#     code =  get_cc(country_name)
#     if code :
#         cc_stats[code] =  pop_v
# import pygal.maps.world#创建了一个Worldmap实例，并设置了该地图的的title属性
# wm = pygal.maps.world.World(print_values=True)
# wm.title = '全球递归IPv6 DNS解析器分布'
# wm.add('IPv6 DNS数量', cc_stats)
# wm.render_to_file('world_v6Rdns.svg')

# 柱状图
bar_chart = pygal.Bar(print_values=True, print_values_position='top')
# bar_chart.title = '国内各服务商开放IPv6 DNS解析器数量'
i=0
x=[]
for k,v in cc.items():
    bar_chart.add(k,v)
    i+=1
    if i==20:
        break
bar_chart.render_to_file("isp_v6dns.svg")
