CREATE (pingan:Person {name:"陈平安"}, title: ["隐官"])
CREATE (ningyao:Person {name:"宁姚"})
CREATE (pingan)-[:TAOIST_COUPLE_WITH{name: "道侣"}]->(ningyao)

CREATE (jiangshe:Person {name:"姜赦", taoistName: ["元神"], title: ["兵家初祖"]})
CREATE (wuyan:Person {name:"五言", taoistName: ["陆地仙"]})
CREATE (jiangshe)-[:TAOIST_COUPLE_WITH{name: "道侣"}]->(wuyan)

CREATE (peiqian:Person {name:"裴钱"})
CREATE (pingan)-[:IS_MASTER_OF{name: "是师傅"}]->(peiqian)

CREATE (jiangshe)-[:IS_PARENT_OF{name: "是父母"}]->(peiqian)
CREATE (wuyan)-[:IS_PARENT_OF{name: "是父母"}]->(peiqian)

CREATE (pozhen:Weapon {name:"破阵", kind:"长枪"})
CREATE (jiangshe)-[:HAS_WEAPON]->(pozhen)

CREATE (shiwu:Weapon {name:"十五", kind:"飞剑"})
CREATE (pingan)-[:HAS_WEAPON]->(shiwu)
CREATE (longzhongque:Weapon {name:"笼中雀", kind:"飞剑"})
CREATE (pingan)-[:HAS_WEAPON]->(longzhongque)

CREATE (baifatongzi:Person {name:"白发童子"}, taoistName: ["箜篌"])
CREATE (baishang:Person {name:"白裳"})
CREATE (baize:Person {name:"白泽"})

CREATE (caijinjian:Person {name:"蔡金简"})
CREATE (chengquan:Person {name:"程荃"})

CREATE (funanhua:Person {name:"苻南华"})
CREATE (gaozhen:Person {name:"高稹"})
CREATE (gucan:Person {name:"顾粲"})
CREATE (haosu:Person {name:"豪素"})
CREATE (jiangshe:Person {name:"姜赦", taoistName: ["蔡州道人"], title: ["碧霄洞主"]})
CREATE (laolonger:Person {name:"老聋儿"})
CREATE (lihuai:Person {name:"李槐"})
CREATE (linjiangxian:Person {name:"林江仙"})
CREATE (linshi:Person {name:"林师"})
CREATE (liuyangxian:Person {name:"刘阳羡"})
CREATE (liuxiang:Person {name:"刘飨"})
CREATE (liuzhimao:Person {name:"刘志茂"})
CREATE (luchen:Person {name:"陆沉"})
CREATE (lutai:Person {name:"陆台"})
CREATE (luzhenchun:Person {name:"卢正淳"})
CREATE (lvbixia:Person {name:"吕碧霞"})

CREATE (peimin:Person {name:"裴旻"})

CREATE (qijingchun:Person {name:"齐静春"})
CREATE (qitingji:Person {name:"齐廷济"})

CREATE (shixingyuan:Person {name:"师行辕"})
CREATE (songjixin:Person {name:"宋集薪"})

CREATE (tianwan:Person {name:"田婉"})

CREATE (wangjia:Person {name:"王甲", taoistName: ["虚君"]})
CREATE (wenzixi:Person {name:"温仔细"})
CREATE (wudiaosi:Person {name:"吴貂寺"})
CREATE (wumingshi:Person {name:"无名氏", race:"妖族"})
CREATE (wushuangjiang:Person {name:"吴霜降"})
CREATE (wuyue:Person {name:"吴钺"})
CREATE (wuzhou:Person {name:"吾洲"})

CREATE (xiaomili:Person {name:"小米粒"})
CREATE (xiegou:Person {name:"谢狗"})

CREATE (yaoxiaoyan:Person {name:"姚小妍"})

CREATE (zhangfenghai:Person {name:"张风海", taoistName: ["泥涂"]})
CREATE (zhaoyao:Person {name:"赵繇"})
CREATE (zhendafeng:Person {name:"郑大风"})
CREATE (zhenjuzhong:Person {name:"郑居中"})
CREATE (zhigui:Person {name:"稚圭"})
CREATE (zhoumi:Person {name:"周密"})

CREATE (lizhu:CaveHeaven {name:"骊珠洞天"})

# MATCH (pingan:Person {name:"陈平安"}), (ningyao:Person {name:"宁姚"})
# MERGE (pingan)-[hasRelationship:TAOIST_COUPLE_WITH{name: "道侣"}]->(ningyao)


# MATCH (n)
# DETACH DELETE n
