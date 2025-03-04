#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名: constants.py
# 功能: 存储所有常量配置
RESULT_FILE = '03_04_20_result.xlsx'

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
'shouji':'ershou','shoujipeijian':'ershou','dianqi':'ershou','shumachanpin':'ershou','zhaoxiangji':'ershou','diannao':'ershou','pingbandiannao':'ershou','bijiben':'ershou','riyongpin':'ershou','bangongyongpin':'ershou','jiaju':'ershou','bangongjiaju':'ershou','qitazhuanrang':'ershou','yinger':'ershou','nongchanpin':'ershou','yundongqicai':'ershou','yueqi':'ershou','xuniwupin':'ershou','menpiao':'ershou','shoucang':'ershou','qishipenjing':'ershou','fushi':'ershou','chongwupeizhong':'chongwu','chongwujiaoyi':'chongwu','chongwumao':'chongwu','qitachongwu':'chongwu','chongwulingyang':'chongwu','chongwuyongpin':'chongwu','zhaochongwu':'chongwu','gongchengche':'cheliang','ershougongchengche':'cheliang','tuolaji':'cheliang','ershouqiche':'cheliang','cheyongpeijian':'cheliang','qicheyongpin':'cheliang','ershoumotuoche':'cheliang','ershoukache':'cheliang','ershoudiandongche':'cheliang','ershouzixingche':'cheliang','qitacheliang':'cheliang','shiguchejiqita':'cheliang','xincheyouhui':'cheliang','xiaxianche':'cheliang','cheliangqiugou':'cheliang','shangpaiyanche':'cheliang','qichebaoyang':'cheliang','pinchesfc':'cheliang','daikuangouche':'cheliang','daolujiuyuan':'cheliang','qichejiuyuan':'cheliang','zhenghun':'huodong','nanzhaonv':'huodong','qitajiaoyou':'huodong','juhui':'huodong','jinengjiaohuan':'huodong','jiaoyouqun':'huodong','ershoufang':'fang','xinfangchushou':'fang','shoufang':'fang','shangpuchushou':'fang','shangpuzhuanrang':'fang','qitafangwu':'fang','jingyingzhuanrang':'fang','zhengzu':'fang','zhaoshiyou':'fang','duanzu':'fang','shangpu':'fang','changfang':'fang','mote':'gongzuo','qitajianzhi':'gongzuo','jiajiao':'gongzuo','kuaijijianzhi':'gongzuo','chongchang':'gongzuo','yanyuan':'gongzuo','fanyijianzhi':'gongzuo','shejijianzhi':'gongzuo','wangzhan':'gongzuo','sheyingjianzhi':'gongzuo','kefujianzhi':'gongzuo','cuxiaojianzhi':'gongzuo','xueshengjianzhi':'gongzuo','wenjuanjianzhi':'gongzuo','cantingjianzhi':'gongzuo','caiyilaoshi':'gongzuo','paifa':'gongzuo','qun':'gongzuo','wangluojianzhi':'gongzuo','zhanhuijianzhi':'gongzuo','zhongdiangongjianzhi':'gongzuo','shenghuopeisongyuan':'gongzuo','wenjuandiaocha':'gongzuo','xiaoyuandaili':'gongzuo','daoyoujianzhi':'gongzuo','huazhuangshi':'gongzuo','liyijianzhi':'gongzuo','hugong':'gongzuo','jianshenjiaolian':'gongzuo','youxidailian':'gongzuo','tupianchuli':'gongzuo','wenmi':'gongzuo','renshi':'gongzuo','gongren':'gongzuo','xiaoshou':'gongzuo','siji':'gongzuo','chushi':'gongzuo','fuwuyuan':'gongzuo','baoan':'gongzuo','daoyou':'gongzuo','bangyong':'gongzuo','songhuoyuan':'gongzuo','dianyuan':'gongzuo','kefu':'gongzuo','kuaiji':'gongzuo','fangdichan':'gongzuo','laoshi':'gongzuo','qichemeirong':'gongzuo','meigong':'gongzuo','meirongshi':'gongzuo','wangluozhibo':'gongzuo','yinshiyule':'gongzuo','baoxianzhaopin':'gongzuo','jinrong':'gongzuo','chengxuyuan':'gongzuo','yisheng':'gongzuo','shichang':'gongzuo','qitazhaopin':'gongzuo','chuguolaowu':'gongzuo','taobaojob':'gongzuo','shengchan':'gongzuo','falv':'gongzuo','nonglinmuyu':'gongzuo','caigou':'gongzuo','ktvjiuba':'gongzuo','jixie':'gongzuo','dianzi':'gongzuo','jianshen':'gongzuo','fanyi':'gongzuo','xuelipeixun':'jiaoyupeixun','shejipeixun':'jiaoyupeixun','diannaopeixun':'jiaoyupeixun','jinengpeixun':'jiaoyupeixun','qitajiaoyupeixun':'jiaoyupeixun','wentipeixun':'jiaoyupeixun','waiyupeixun':'jiaoyupeixun','diannaoweixiu':'fuwu','shumaweixiu':'fuwu','shoujiweixiu':'fuwu','jiadianweixiu':'fuwu','jiajuweixiu':'fuwu','fangwuweixiu':'fuwu','weixiu':'fuwu','jianzhuweixiu':'fuwu','zhongbiaoweixiu':'fuwu','kaisuo':'fuwu','bangongweixiu':'fuwu','zulin':'fuwu','zixun':'fuwu','lvshifuwu':'fuwu','daibanzhuce':'fuwu','kuaijifuwu':'fuwu','baojieqingxi':'fuwu','baomu':'fuwu','gongyeshebei':'fuwu','kuaidi':'fuwu','banjia':'fuwu','chaijiu':'fuwu','jiancaizhuangshi':'fuwu','zhuangxiu':'fuwu','jiatingzhuangxiu':'fuwu','ruanzhuang':'fuwu','siyi':'fuwu','binzang':'fuwu','gerenzuche':'fuwu','peijiafuwu':'fuwu','jiaxiaofuwu':'fuwu','peijiapeilian':'fuwu','lvxingshe':'fuwu','jipiaofuwu':'fuwu','jiudianfuwu':'fuwu','qianzhengfuwu':'fuwu','wangzhanjianshe':'fuwu','wangluobuxian':'fuwu','jinrongfuwu':'fuwu','licaifuwu':'fuwu','baoxianfuwu':'fuwu','zhanlanzhanhui':'fuwu','sheji':'fuwu','qingdian':'fuwu','guanggaomeiti':'fuwu','penhuizhaopai':'fuwu','yinshuapenghui':'fuwu','daiyunyingtg':'fuwu','jiameng':'fuwu','quanxinshangjia':'fuwu','wupinhuishou':'fuwu','wupinpifa':'fuwu','canyin':'fuwu','canyinmeishi':'fuwu','yule':'fuwu','qitafuwu':'fuwu','fanyifuwu':'fuwu','sheyingfuwu':'fuwu','kuaidifuwu':'fuwu','yiminfuwu':'fuwu','meirongfuwu':'fuwu','xianhualipin':'fuwu','lipinfuwu':'fuwu','yundongjianshen':'fuwu','gongyijianding':'fuwu','nongye':'fuwu','suji':'fuwu','xiyihuli':'fuwu'
}