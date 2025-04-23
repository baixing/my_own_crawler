#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名: constants.py
# 功能: 存储所有常量配置
RESULT_FILE = 'new_result.xlsx'

# 一级类目列表
LEVEL1_CATEGORIES = [
    'ershou',
    'chongwu',
    'cheliang',
    'huodong',
    'fang',
    'gongzuo',
    'jiaoyupeixun',
    'fuwu',
    'jianzhi'
]

# 旧类目列表
OLD_CATEGORIES = [
    'shouji', 'shoujipeijian', 'dianqi', 'shumachanpin', 'zhaoxiangji',
    'diannao', 'pingbandiannao', 'bijiben', 'riyongpin', 'bangongyongpin',
    'jiaju', 'bangongjiaju', 'qitazhuanrang', 'yinger', 'nongchanpin',
    'yundongqicai', 'yueqi', 'xuniwupin', 'menpiao', 'shoucang',
    'qishipenjing', 'fushi', 'chongwupeizhong', 'chongwujiaoyi',
    'chongwumao', 'qitachongwu', 'chongwulingyang', 'chongwuyongpin',
    'zhaochongwu', 'gongchengche', 'ershougongchengche', 'tuolaji',
    'ershouqiche', 'cheyongpeijian', 'qicheyongpin', 'ershoumotuoche',
    'ershoukache', 'ershoudiandongche', 'ershouzixingche', 'qitacheliang',
    'shiguchejiqita', 'xincheyouhui', 'xiaxianche', 'cheliangqiugou',
    'shangpaiyanche', 'qichebaoyang', 'pinchesfc', 'daikuangouche',
    'daolujiuyuan', 'qichejiuyuan', 'zhenghun', 'nanzhaonv', 'qitajiaoyou',
    'juhui', 'jinengjiaohuan', 'jiaoyouqun', 'ershoufang', 'xinfangchushou',
    'shoufang', 'shangpuchushou', 'shangpuzhuanrang', 'jingyingzhuanrang',
    'zhengzu', 'zhaoshiyou', 'duanzu', 'shangpu', 'changfang', 'mote',
    'qitajianzhi', 'jiajiao', 'kuaijijianzhi', 'chongchang', 'yanyuan',
    'fanyijianzhi', 'shejijianzhi', 'wangzhan', 'sheyingjianzhi',
    'kefujianzhi', 'cuxiaojianzhi', 'xueshengjianzhi', 'wenjuanjianzhi',
    'cantingjianzhi', 'caiyilaoshi', 'paifa', 'qun', 'wangluojianzhi',
    'zhanhuijianzhi', 'zhongdiangongjianzhi', 'shenghuopeisongyuan',
    'wenjuandiaocha', 'xiaoyuandaili', 'daoyoujianzhi', 'huazhuangshi',
    'liyijianzhi', 'hugong', 'jianshenjiaolian', 'youxidailian',
    'tupianchuli', 'wenmi', 'renshi', 'gongren', 'xiaoshou', 'siji',
    'chushi', 'fuwuyuan', 'baoan', 'daoyou', 'bangyong', 'songhuoyuan',
    'dianyuan', 'kefu', 'kuaiji', 'fangdichan', 'laoshi', 'qichemeirong',
    'meigong', 'meirongshi', 'wangluozhibo', 'yinshiyule', 'baoxianzhaopin',
    'jinrong', 'chengxuyuan', 'yisheng', 'shichang', 'qitazhaopin',
    'chuguolaowu', 'taobaojob', 'shengchan', 'falv', 'nonglinmuyu',
    'caigou', 'ktvjiuba', 'jixie', 'dianzi', 'jianshen', 'fanyi',
    'xuelipeixun', 'shejipeixun', 'diannaopeixun', 'jinengpeixun',
    'qitajiaoyupeixun', 'wentipeixun', 'waiyupeixun', 'diannaoweixiu',
    'shumaweixiu', 'shoujiweixiu', 'jiadianweixiu', 'jiajuweixiu',
    'fangwuweixiu', 'weixiu', 'jianzhuweixiu', 'zhongbiaoweixiu',
    'kaisuo', 'bangongweixiu', 'zulin', 'zixun', 'lvshifuwu',
    'daibanzhuce', 'kuaijifuwu', 'baojieqingxi', 'baomu', 'gongyeshebei',
    'kuaidi', 'banjia', 'chaijiu', 'jiancaizhuangshi', 'zhuangxiu',
    'jiatingzhuangxiu', 'ruanzhuang', 'siyi', 'binzang', 'gerenzuche',
    'peijiafuwu', 'jiaxiaofuwu', 'peijiapeilian', 'lvxingshe',
    'jipiaofuwu', 'jiudianfuwu', 'qianzhengfuwu', 'wangzhanjianshe',
    'wangluobuxian', 'jinrongfuwu', 'licaifuwu', 'baoxianfuwu',
    'zhanlanzhanhui', 'sheji', 'qingdian', 'guanggaomeiti',
    'penhuizhaopai', 'yinshuapenghui', 'daiyunyingtg', 'jiameng',
    'quanxinshangjia', 'wupinhuishou', 'wupinpifa', 'canyin',
    'canyinmeishi', 'yule', 'qitafuwu', 'fanyifuwu', 'sheyingfuwu',
    'kuaidifuwu', 'yiminfuwu', 'meirongfuwu', 'xianhualipin',
    'lipinfuwu', 'yundongjianshen', 'gongyijianding', 'nongye',
    'suji', 'xiyihuli'
]

# 添加类目到一级类目的映射字典
CATEGORY_TO_LEVEL1 = {
    'shouji': 'ershou', 'shoujipeijian': 'ershou', 'dianqi': 'ershou', 'shumachanpin': 'ershou',
    'zhaoxiangji': 'ershou', 'diannao': 'ershou', 'pingbandiannao': 'ershou', 'bijiben': 'ershou',
    'riyongpin': 'ershou', 'bangongyongpin': 'ershou', 'jiaju': 'ershou', 'bangongjiaju': 'ershou',
    'qitazhuanrang': 'ershou', 'yinger': 'ershou', 'nongchanpin': 'ershou', 'yundongqicai': 'ershou', 'yueqi': 'ershou',
    'xuniwupin': 'ershou', 'menpiao': 'ershou', 'shoucang': 'ershou', 'qishipenjing': 'ershou', 'fushi': 'ershou',
    'chongwupeizhong': 'chongwu', 'chongwujiaoyi': 'chongwu', 'chongwumao': 'chongwu', 'qitachongwu': 'chongwu',
    'chongwulingyang': 'chongwu', 'chongwuyongpin': 'chongwu', 'zhaochongwu': 'chongwu', 'gongchengche': 'cheliang',
    'ershougongchengche': 'cheliang', 'tuolaji': 'cheliang', 'ershouqiche': 'cheliang', 'cheyongpeijian': 'cheliang',
    'qicheyongpin': 'cheliang', 'ershoumotuoche': 'cheliang', 'ershoukache': 'cheliang',
    'ershoudiandongche': 'cheliang', 'ershouzixingche': 'cheliang', 'qitacheliang': 'cheliang',
    'shiguchejiqita': 'cheliang', 'xincheyouhui': 'cheliang', 'xiaxianche': 'cheliang', 'cheliangqiugou': 'cheliang',
    'shangpaiyanche': 'cheliang', 'qichebaoyang': 'cheliang', 'pinchesfc': 'cheliang', 'daikuangouche': 'cheliang',
    'daolujiuyuan': 'cheliang', 'qichejiuyuan': 'cheliang', 'zhenghun': 'huodong', 'nanzhaonv': 'huodong',
    'qitajiaoyou': 'huodong', 'juhui': 'huodong', 'jinengjiaohuan': 'huodong', 'jiaoyouqun': 'huodong',
    'ershoufang': 'fang', 'xinfangchushou': 'fang', 'shoufang': 'fang', 'shangpuchushou': 'fang',
    'shangpuzhuanrang': 'fang', 'qitafangwu': 'fang', 'jingyingzhuanrang': 'fang', 'zhengzu': 'fang',
    'zhaoshiyou': 'fang', 'duanzu': 'fang', 'shangpu': 'fang', 'changfang': 'fang', 'mote': 'gongzuo',
    'qitajianzhi': 'gongzuo', 'jiajiao': 'gongzuo', 'kuaijijianzhi': 'gongzuo', 'chongchang': 'gongzuo',
    'yanyuan': 'gongzuo', 'fanyijianzhi': 'gongzuo', 'shejijianzhi': 'gongzuo', 'wangzhan': 'gongzuo',
    'sheyingjianzhi': 'gongzuo', 'kefujianzhi': 'gongzuo', 'cuxiaojianzhi': 'gongzuo', 'xueshengjianzhi': 'gongzuo',
    'wenjuanjianzhi': 'gongzuo', 'cantingjianzhi': 'gongzuo', 'caiyilaoshi': 'gongzuo', 'paifa': 'gongzuo',
    'qun': 'gongzuo', 'wangluojianzhi': 'gongzuo', 'zhanhuijianzhi': 'gongzuo', 'zhongdiangongjianzhi': 'gongzuo',
    'shenghuopeisongyuan': 'gongzuo', 'wenjuandiaocha': 'gongzuo', 'xiaoyuandaili': 'gongzuo',
    'daoyoujianzhi': 'gongzuo', 'huazhuangshi': 'gongzuo', 'liyijianzhi': 'gongzuo', 'hugong': 'gongzuo',
    'jianshenjiaolian': 'gongzuo', 'youxidailian': 'gongzuo', 'tupianchuli': 'gongzuo', 'wenmi': 'gongzuo',
    'renshi': 'gongzuo', 'gongren': 'gongzuo', 'xiaoshou': 'gongzuo', 'siji': 'gongzuo', 'chushi': 'gongzuo',
    'fuwuyuan': 'gongzuo', 'baoan': 'gongzuo', 'daoyou': 'gongzuo', 'bangyong': 'gongzuo', 'songhuoyuan': 'gongzuo',
    'dianyuan': 'gongzuo', 'kefu': 'gongzuo', 'kuaiji': 'gongzuo', 'fangdichan': 'gongzuo', 'laoshi': 'gongzuo',
    'qichemeirong': 'gongzuo', 'meigong': 'gongzuo', 'meirongshi': 'gongzuo', 'wangluozhibo': 'gongzuo',
    'yinshiyule': 'gongzuo', 'baoxianzhaopin': 'gongzuo', 'jinrong': 'gongzuo', 'chengxuyuan': 'gongzuo',
    'yisheng': 'gongzuo', 'shichang': 'gongzuo', 'qitazhaopin': 'gongzuo', 'chuguolaowu': 'gongzuo',
    'taobaojob': 'gongzuo', 'shengchan': 'gongzuo', 'falv': 'gongzuo', 'nonglinmuyu': 'gongzuo', 'caigou': 'gongzuo',
    'ktvjiuba': 'gongzuo', 'jixie': 'gongzuo', 'dianzi': 'gongzuo', 'jianshen': 'gongzuo', 'fanyi': 'gongzuo',
    'xuelipeixun': 'jiaoyupeixun', 'shejipeixun': 'jiaoyupeixun', 'diannaopeixun': 'jiaoyupeixun',
    'jinengpeixun': 'jiaoyupeixun', 'qitajiaoyupeixun': 'jiaoyupeixun', 'wentipeixun': 'jiaoyupeixun',
    'waiyupeixun': 'jiaoyupeixun', 'diannaoweixiu': 'fuwu', 'shumaweixiu': 'fuwu', 'shoujiweixiu': 'fuwu',
    'jiadianweixiu': 'fuwu', 'jiajuweixiu': 'fuwu', 'fangwuweixiu': 'fuwu', 'weixiu': 'fuwu', 'jianzhuweixiu': 'fuwu',
    'zhongbiaoweixiu': 'fuwu', 'kaisuo': 'fuwu', 'bangongweixiu': 'fuwu', 'zulin': 'fuwu', 'zixun': 'fuwu',
    'lvshifuwu': 'fuwu', 'daibanzhuce': 'fuwu', 'kuaijifuwu': 'fuwu', 'baojieqingxi': 'fuwu', 'baomu': 'fuwu',
    'gongyeshebei': 'fuwu', 'kuaidi': 'fuwu', 'banjia': 'fuwu', 'chaijiu': 'fuwu', 'jiancaizhuangshi': 'fuwu',
    'zhuangxiu': 'fuwu', 'jiatingzhuangxiu': 'fuwu', 'ruanzhuang': 'fuwu', 'siyi': 'fuwu', 'binzang': 'fuwu',
    'gerenzuche': 'fuwu', 'peijiafuwu': 'fuwu', 'jiaxiaofuwu': 'fuwu', 'peijiapeilian': 'fuwu', 'lvxingshe': 'fuwu',
    'jipiaofuwu': 'fuwu', 'jiudianfuwu': 'fuwu', 'qianzhengfuwu': 'fuwu', 'wangzhanjianshe': 'fuwu',
    'wangluobuxian': 'fuwu', 'jinrongfuwu': 'fuwu', 'licaifuwu': 'fuwu', 'baoxianfuwu': 'fuwu',
    'zhanlanzhanhui': 'fuwu', 'sheji': 'fuwu', 'qingdian': 'fuwu', 'guanggaomeiti': 'fuwu', 'penhuizhaopai': 'fuwu',
    'yinshuapenghui': 'fuwu', 'daiyunyingtg': 'fuwu', 'jiameng': 'fuwu', 'quanxinshangjia': 'fuwu',
    'wupinhuishou': 'fuwu', 'wupinpifa': 'fuwu', 'canyin': 'fuwu', 'canyinmeishi': 'fuwu', 'yule': 'fuwu',
    'qitafuwu': 'fuwu', 'fanyifuwu': 'fuwu', 'sheyingfuwu': 'fuwu', 'kuaidifuwu': 'fuwu', 'yiminfuwu': 'fuwu',
    'meirongfuwu': 'fuwu', 'xianhualipin': 'fuwu', 'lipinfuwu': 'fuwu', 'yundongjianshen': 'fuwu',
    'gongyijianding': 'fuwu', 'nongye': 'fuwu', 'suji': 'fuwu', 'xiyihuli': 'fuwu'

}

NO_IMPORTANT_PATH = ['_next', '/a/', '/oz/', 'showImg', 'root', 'search', '53kf',
                     '/v/', '/w/', '/ra/', 'help', 'bind',
                     'credit', 'PublicReview', '/weishop',
                     'fabu','arch','/user/','/c/'
                     ]

FOUR_XX_PATH = ['/cart','/info/']

CITIES = ['shanghai','tianjin','chongqing','nanjing','changshu','kunshan','lianyungang','nantong','suzhou','tz','wuxi','suqian','xuzhou','yangzhou','zhangjiagang','shaoxing','jinhua','quzhou','lishui','taizhou','fuzhou','xiamen','quanzhou','putian','zhangzhou','longyan','nanping','ningde','sanming','jinan','qingdao','yantai','weihai','weifang','binzhou','dezhou','dongying','heze','jining','laiwu','liaocheng','linyi','rizhao','taian','zaozhuang','zibo','nanchang','jiujiang','ganzhou','fz','jian','jingdezhen','pingxiang','shangrao','xinyu','yc','yingtan','hefei','anqing','bengbu','bozhou','chaohu','chizhou','chuzhou','fuyang','huaibei','huainan','huangshan','luan','maanshan','tongling','wuhu','sz','xuancheng','guangzhou','shenzhen','dongguan','foshan','zhuhai','zhongshan','huizhou','chaozhou','heyuan','jiangmen','jieyang','maoming','meizhou','qingyuan','shantou','shanwei','shaoguan','yangjiang','yunfu','zhanjiang','zhaoqing','haikou','sanya','baisha','baoting','changjiang','chengmai','danzhou','dingan','dongfang','ledong','lingao','lingshui','qionghai','qiongzhong','sansha','tunchang','wanning','wenchang','wuzhishan','nanning','guilin','liuzhou','bose','beihai','chongzuo','fangchenggang','guigang','hechi','hezhou','laibin','qinzhou','wuzhou','yl','wuhan','yichang','xiangfan','ezhou','enshi','huanggang','huangshi','jingmen','jingzhou','qianjiang','shennongjia','shiyan','suizhou','tianmen','xiantao','xianning','xiaogan','changsha','zhuzhou','xiangtan','changde','chenzhou','hengyang','huaihua','loudi','shaoyang','xiangxi','yiyang','yongzhou','yueyang','zhangjiajie','zhengzhou','luoyang','kaifeng','anyang','hebi','jiyuan','jiaozuo','luohe','nanyang','pingdingshan','puyang','sanmenxia','shangqiu','xinxiang','xinyang','xuchang','zhoukou','zhumadian','huhehaote','baotou','eerduosi','alashan','bayannaoer','chifeng','hulunbeier','tongliao','wuhai','wulanchabu','xilinguole','xingan','shijiazhuang','baoding','tangshan','cangzhou','chengde','handan','hengshui','langfang','qinhuangdao','xingtai','zhangjiakou','taiyuan','datong','yuncheng','jincheng','jinzhong','linfen','lvliang','shuozhou','xinzhou','yangquan','changzhi','shenyang','dalian','anshan','benxi','chaoyang','dandong','fushun','fuxin','huludao','jinzhou','liaoyang','panjin','tieling','yingkou','changchun','jilin','yanbian','baicheng','baishan','liaoyuan','siping','songyuan','tonghua','haerbin','daqing','qiqihaer','daxinganling','hegang','heihe','jixi','jiamusi','mudanjiang','qitaihe','shuangyashan','suihua','yichun','chengdu','mianyang','leshan','aba','bazhong','dazhou','deyang','ganzi','guangan','guangyuan','liangshan','luzhou','meishan','nanchong','neijiang','panzhihua','suining','yaan','yibin','ziyang','zigong','lasa','rikaze','ali','changdu','linzhi','naqu','shannan','kunming','dali','lijiang','baoshan','chuxiong','dehong','diqing','honghe','lincang','nujiang','puer','qujing','wenshan','xishuangbanna','yuxi','zhaotong','guiyang','zunyi','liupanshui','anshun','bijie','qiandongnan','qiannan','qianxinan','tongren','xian','baoji','xianyang','ankang','hanzhong','shangluo','tongchuan','weinan','yanan','yulin','wulumuqi','kelamayi','akesu','alaer','aletai','bayinguoleng','boertala','changji','hami','hetian','kashi','kezilesu','shihezi','tacheng','tumushuke','tulufan','wujiaqu','yili','xining','guoluo','haibei','haidong','hainan','haixi','huangnan','yushu','yinchuan','shizuishan','guyuan','wuzhong','zhongwei','lanzhou','baiyin','dingxi','gannan','jiayuguan','jinchang','jiuquan','linxia','longnan','pingliang','qingyang','tianshui','wuwei','zhangye']

# CITIES = ['beijing','shanghai','tianjin','chongqing','nanjing','changshu','changzhou','huaian','kunshan','lianyungang','nantong','suzhou','taicang','tz','wuxi','suqian','xuzhou','yancheng','yangzhou','zhangjiagang','zhenjiang','hangzhou','ningbo','wenzhou','jiaxing','huzhou','shaoxing','jinhua','quzhou','lishui','taizhou','zhoushan','fuzhou','xiamen','quanzhou','putian','zhangzhou','longyan','nanping','ningde','sanming','jinan','qingdao','yantai','weihai','weifang','binzhou','dezhou','dongying','heze','jining','laiwu','liaocheng','linyi','rizhao','taian','zaozhuang','zibo','nanchang','jiujiang','ganzhou','fz','jian','jingdezhen','pingxiang','shangrao','xinyu','yc','yingtan','hefei','anqing','bengbu','bozhou','chaohu','chizhou','chuzhou','fuyang','huaibei','huainan','huangshan','luan','maanshan','tongling','wuhu','sz','xuancheng','guangzhou','shenzhen','dongguan','foshan','zhuhai','zhongshan','huizhou','chaozhou','heyuan','jiangmen','jieyang','maoming','meizhou','qingyuan','shantou','shanwei','shaoguan','yangjiang','yunfu','zhanjiang','zhaoqing','haikou','sanya','baisha','baoting','changjiang','chengmai','danzhou','dingan','dongfang','ledong','lingao','lingshui','qionghai','qiongzhong','sansha','tunchang','wanning','wenchang','wuzhishan','nanning','guilin','liuzhou','bose','beihai','chongzuo','fangchenggang','guigang','hechi','hezhou','laibin','qinzhou','wuzhou','yl','wuhan','yichang','xiangfan','ezhou','enshi','huanggang','huangshi','jingmen','jingzhou','qianjiang','shennongjia','shiyan','suizhou','tianmen','xiantao','xianning','xiaogan','changsha','zhuzhou','xiangtan','changde','chenzhou','hengyang','huaihua','loudi','shaoyang','xiangxi','yiyang','yongzhou','yueyang','zhangjiajie','zhengzhou','luoyang','kaifeng','anyang','hebi','jiyuan','jiaozuo','luohe','nanyang','pingdingshan','puyang','sanmenxia','shangqiu','xinxiang','xinyang','xuchang','zhoukou','zhumadian','huhehaote','baotou','eerduosi','alashan','bayannaoer','chifeng','hulunbeier','tongliao','wuhai','wulanchabu','xilinguole','xingan','shijiazhuang','baoding','tangshan','cangzhou','chengde','handan','hengshui','langfang','qinhuangdao','xingtai','zhangjiakou','taiyuan','datong','yuncheng','jincheng','jinzhong','linfen','lvliang','shuozhou','xinzhou','yangquan','changzhi','shenyang','dalian','anshan','benxi','chaoyang','dandong','fushun','fuxin','huludao','jinzhou','liaoyang','panjin','tieling','yingkou','changchun','jilin','yanbian','baicheng','baishan','liaoyuan','siping','songyuan','tonghua','haerbin','daqing','qiqihaer','daxinganling','hegang','heihe','jixi','jiamusi','mudanjiang','qitaihe','shuangyashan','suihua','yichun','chengdu','mianyang','leshan','aba','bazhong','dazhou','deyang','ganzi','guangan','guangyuan','liangshan','luzhou','meishan','nanchong','neijiang','panzhihua','suining','yaan','yibin','ziyang','zigong','lasa','rikaze','ali','changdu','linzhi','naqu','shannan','kunming','dali','lijiang','baoshan','chuxiong','dehong','diqing','honghe','lincang','nujiang','puer','qujing','wenshan','xishuangbanna','yuxi','zhaotong','guiyang','zunyi','liupanshui','anshun','bijie','qiandongnan','qiannan','qianxinan','tongren','xian','baoji','xianyang','ankang','hanzhong','shangluo','tongchuan','weinan','yanan','yulin','wulumuqi','kelamayi','akesu','alaer','aletai','bayinguoleng','boertala','changji','hami','hetian','kashi','kezilesu','shihezi','tacheng','tumushuke','tulufan','wujiaqu','yili','xining','guoluo','haibei','haidong','hainan','haixi','huangnan','yushu','yinchuan','shizuishan','guyuan','wuzhong','zhongwei','lanzhou','baiyin','dingxi','gannan','jiayuguan','jinchang','jiuquan','linxia','longnan','pingliang','qingyang','tianshui','wuwei','zhangye']

ALL_CITIES = ['beijing','shanghai','tianjin','chongqing','nanjing','changshu','changzhou','huaian','kunshan','lianyungang','nantong','suzhou','taicang','tz','wuxi','suqian','xuzhou','yancheng','yangzhou','zhangjiagang','zhenjiang','hangzhou','ningbo','wenzhou','jiaxing','huzhou','shaoxing','jinhua','quzhou','lishui','taizhou','zhoushan','fuzhou','xiamen','quanzhou','putian','zhangzhou','longyan','nanping','ningde','sanming','jinan','qingdao','yantai','weihai','weifang','binzhou','dezhou','dongying','heze','jining','laiwu','liaocheng','linyi','rizhao','taian','zaozhuang','zibo','nanchang','jiujiang','ganzhou','fz','jian','jingdezhen','pingxiang','shangrao','xinyu','yc','yingtan','hefei','anqing','bengbu','bozhou','chaohu','chizhou','chuzhou','fuyang','huaibei','huainan','huangshan','luan','maanshan','tongling','wuhu','sz','xuancheng','guangzhou','shenzhen','dongguan','foshan','zhuhai','zhongshan','huizhou','chaozhou','heyuan','jiangmen','jieyang','maoming','meizhou','qingyuan','shantou','shanwei','shaoguan','yangjiang','yunfu','zhanjiang','zhaoqing','haikou','sanya','baisha','baoting','changjiang','chengmai','danzhou','dingan','dongfang','ledong','lingao','lingshui','qionghai','qiongzhong','sansha','tunchang','wanning','wenchang','wuzhishan','nanning','guilin','liuzhou','bose','beihai','chongzuo','fangchenggang','guigang','hechi','hezhou','laibin','qinzhou','wuzhou','yl','wuhan','yichang','xiangfan','ezhou','enshi','huanggang','huangshi','jingmen','jingzhou','qianjiang','shennongjia','shiyan','suizhou','tianmen','xiantao','xianning','xiaogan','changsha','zhuzhou','xiangtan','changde','chenzhou','hengyang','huaihua','loudi','shaoyang','xiangxi','yiyang','yongzhou','yueyang','zhangjiajie','zhengzhou','luoyang','kaifeng','anyang','hebi','jiyuan','jiaozuo','luohe','nanyang','pingdingshan','puyang','sanmenxia','shangqiu','xinxiang','xinyang','xuchang','zhoukou','zhumadian','huhehaote','baotou','eerduosi','alashan','bayannaoer','chifeng','hulunbeier','tongliao','wuhai','wulanchabu','xilinguole','xingan','shijiazhuang','baoding','tangshan','cangzhou','chengde','handan','hengshui','langfang','qinhuangdao','xingtai','zhangjiakou','taiyuan','datong','yuncheng','jincheng','jinzhong','linfen','lvliang','shuozhou','xinzhou','yangquan','changzhi','shenyang','dalian','anshan','benxi','chaoyang','dandong','fushun','fuxin','huludao','jinzhou','liaoyang','panjin','tieling','yingkou','changchun','jilin','yanbian','baicheng','baishan','liaoyuan','siping','songyuan','tonghua','haerbin','daqing','qiqihaer','daxinganling','hegang','heihe','jixi','jiamusi','mudanjiang','qitaihe','shuangyashan','suihua','yichun','chengdu','mianyang','leshan','aba','bazhong','dazhou','deyang','ganzi','guangan','guangyuan','liangshan','luzhou','meishan','nanchong','neijiang','panzhihua','suining','yaan','yibin','ziyang','zigong','lasa','rikaze','ali','changdu','linzhi','naqu','shannan','kunming','dali','lijiang','baoshan','chuxiong','dehong','diqing','honghe','lincang','nujiang','puer','qujing','wenshan','xishuangbanna','yuxi','zhaotong','guiyang','zunyi','liupanshui','anshun','bijie','qiandongnan','qiannan','qianxinan','tongren','xian','baoji','xianyang','ankang','hanzhong','shangluo','tongchuan','weinan','yanan','yulin','wulumuqi','kelamayi','akesu','alaer','aletai','bayinguoleng','boertala','changji','hami','hetian','kashi','kezilesu','shihezi','tacheng','tumushuke','tulufan','wujiaqu','yili','xining','guoluo','haibei','haidong','hainan','haixi','huangnan','yushu','yinchuan','shizuishan','guyuan','wuzhong','zhongwei','lanzhou','baiyin','dingxi','gannan','jiayuguan','jinchang','jiuquan','linxia','longnan','pingliang','qingyang','tianshui','wuwei','zhangye']

ID2CITY = {'m373':'akesu','m177415':'alaer','m146':'alashan','m333':'aletai','m328':'ali','m340':'ankang','m177':'anqing','m108':'anshan','m301':'anshun','m90':'anyang','m124':'baicheng','m177418':'baisha','m127':'baishan','m354':'baiyin','m68':'baoding','m342':'baoji','m313':'baoshan','m177420':'baoting','m137':'baotou','m143':'bayannaoer','m372':'bayinguoleng','m288':'bazhong','m270':'beihai','m28':'beijing','m173':'bengbu','m110':'benxi','m305':'bijie','m169':'binzhou','m334':'boertala','m267':'bose','m179':'bozhou','m73':'cangzhou','m119':'changchun','m237':'changde','m326':'changdu','m370':'changji','m177421':'changjiang','m232':'changsha','m6015':'changshu','m83':'changzhi','m156':'changzhou','m185':'chaohu','m116':'chaoyang','m259':'chaozhou','m70':'chengde','m36':'chengdu','m177422':'chengmai','m236':'chenzhou','m141':'chifeng','m186':'chizhou','m32':'chongqing','m50':'chongzuo','m316':'chuxiong','m43':'chuzhou','m310':'dali','m107':'dalian','m111':'dandong','m59':'danzhou','m134':'daqing','m80':'datong','m177413':'daxinganling','m285':'dazhou','m216':'dehong','m297':'deyang','m163':'dezhou','m177423':'dingan','m346':'dingxi','m320':'diqing','m60':'dongfang','m260':'dongguan','m170':'dongying','m142':'eerduosi','m229':'enshi','m219':'ezhou','m261':'fangchenggang','m252':'foshan','m109':'fushun','m114':'fuxin','m171':'fuyang','m198':'fuzhou','m275':'fz','m353':'gannan','m278':'ganzhou','m295':'ganzi','m287':'guangan','m298':'guangyuan','m29':'guangzhou','m266':'guigang','m264':'guilin','m299':'guiyang','m363':'guoluo','m358':'guyuan','m128':'haerbin','m359':'haibei','m361':'haidong','m329':'haikou','m366':'hainan','m365':'haixi','m331':'hami','m66':'handan','m188':'hangzhou','m341':'hanzhong','m99':'hebi','m269':'hechi','m172':'hefei','m40':'hegang','m132':'heihe','m74':'hengshui','m235':'hengyang','m332':'hetian','m256':'heyuan','m159':'heze','m49':'hezhou','m311':'honghe','m154':'huaian','m181':'huaibei','m243':'huaihua','m175':'huainan','m221':'huanggang','m362':'huangnan','m180':'huangshan','m222':'huangshi','m136':'huhehaote','m247':'huizhou','m118':'huludao','m135':'hulunbeier','m189':'huzhou','m131':'jiamusi','m277':'jian','m245':'jiangmen','m98':'jiaozuo','m190':'jiaxing','m48':'jiayuguan','m213':'jieyang','m120':'jilin','m160':'jinan','m349':'jinchang','m84':'jincheng','m279':'jingdezhen','m228':'jingmen','m224':'jingzhou','m196':'jinhua','m166':'jining','m82':'jinzhong','m112':'jinzhou','m273':'jiujiang','m351':'jiuquan','m38':'jixi','m105':'jiyuan','m96':'kaifeng','m374':'kashi','m367':'kelamayi','m177414':'kezilesu','m296':'kimi','m309':'kunming','m6016':'kunshan','m44':'laibin','m209':'laiwu','m72':'langfang','m345':'lanzhou','m322':'lasa','m177424':'ledong','m292':'leshan','m293':'liangshan','m155':'lianyungang','m210':'liaocheng','m115':'liaoyang','m125':'liaoyuan','m321':'lijiang','m318':'lincang','m85':'linfen','m177425':'lingao','m177426':'lingshui','m344':'linxia','m168':'linyi','m325':'linzhi','m195':'lishui','m306':'liupanshui','m263':'liuzhou','m46':'longnan','m204':'longyan','m239':'loudi','m184':'luan','m102':'luohe','m97':'luoyang','m289':'luzhou','m86':'lvliang','m176':'maanshan','m214':'maoming','m45':'meishan','m248':'meizhou','m283':'mianyang','m130':'mudanjiang','m272':'nanchang','m284':'nanchong','m34':'nanjing','m262':'nanning','m206':'nanping','m150':'nantong','m95':'nanyang','m327':'naqu','m291':'neijiang','m191':'ningbo','m200':'ningde','m319':'nujiang','m117':'panjin','m281':'panzhihua','m93':'pingdingshan','m347':'pingliang','m280':'pingxiang','m317':'puer','m201':'putian','m100':'puyang','m303':'qiandongnan','m58':'qianjiang','m302':'qiannan','m307':'qianxinan','m161':'qingdao','m348':'qingyang','m257':'qingyuan','m76':'qinhuangdao','m268':'qinzhou','m62':'qionghai','m177427':'qiongzhong','m129':'qiqihaer','m39':'qitaihe','m202':'quanzhou','m312':'qujing','m187':'quzhou','m323':'rikaze','m208':'rizhao','m104':'sanmenxia','m205':'sanming','m177419':'sansha','m55':'sanya','m30':'shanghai','m339':'shangluo','m88':'shangqiu','m274':'shangrao','m324':'shannan','m249':'shantou','m211':'shanwei','m246':'shaoguan','m192':'shaoxing','m240':'shaoyang','m230':'shennongjia','m33':'shenyang','m250':'shenzhen','m369':'shihezi','m67':'shijiazhuang','m226':'shiyan','m356':'shizuishan','m41':'shuangyashan','m77':'shuozhou','m122':'siping','m126':'songyuan','m133':'suihua','m286':'suining','m227':'suizhou','m158':'suqian','m149':'suzhou','m178':'sz','m330':'tacheng','m42':'taian','m6014':'taicang','m79':'taiyuan','m193':'taizhou','m71':'tangshan','m31':'tianjin','m57':'tianmen','m352':'tianshui','m106':'tieling','m343':'tongchuan','m123':'tonghua','m140':'tongliao','m182':'tongling','m304':'tongren','m371':'tulufan','m177417':'tumushuke','m177428':'tunchang','m157':'tz','m64':'wanning','m165':'weifang','m167':'weihai','m338':'weinan','m61':'wenchang','m314':'wenshan','m194':'wenzhou','m138':'wuhai','m35':'wuhan','m174':'wuhu','m177416':'wujiaqu','m139':'wulanchabu','m368':'wulumuqi','m47':'wuwei','m147':'wuxi','m63':'wuzhishan','m357':'wuzhong','m265':'wuzhou','m199':'xiamen','m37':'xian','m218':'xiangfan','m233':'xiangtan','m241':'xiangxi','m223':'xianning','m56':'xiantao','m335':'xianyang','m220':'xiaogan','m144':'xilinguole','m145':'xingan','m75':'xingtai','m360':'xining','m91':'xinxiang','m94':'xinyang','m271':'xinyu','m78':'xinzhou','m215':'xishuangbanna','m183':'xuancheng','m92':'xuchang','m153':'xuzhou','m294':'yaan','m336':'yanan','m121':'yanbian','m152':'yancheng','m212':'yangjiang','m81':'yangquan','m151':'yangzhou','m164':'yantai','m276':'yc','m290':'yibin','m225':'yichang','m51':'yichun','m52':'yili','m355':'yinchuan','m113':'yingkou','m217':'yingtan','m238':'yiyang','m65':'yl','m244':'yongzhou','m231':'yueyang','m337':'yulin','m87':'yuncheng','m258':'yunfu','m364':'yushu','m315':'yuxi','m207':'zaozhuang','m6013':'zhangjiagang','m242':'zhangjiajie','m69':'zhangjiakou','m350':'zhangye','m203':'zhangzhou','m254':'zhanjiang','m253':'zhaoqing','m308':'zhaotong','m89':'zhengzhou','m148':'zhenjiang','m255':'zhongshan','m54':'zhongwei','m101':'zhoukou','m197':'zhoushan','m251':'zhuhai','m103':'zhumadian','m234':'zhuzhou','m162':'zibo','m282':'zigong','m53':'ziyang','m300':'zunyi'}