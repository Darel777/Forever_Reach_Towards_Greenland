label chapter15Start:
    play music "../audio/chapter15-1.mp3"
    "我答应了半夏的请求。虽然我另一面向白芷保证自己肯定还是会回去的。"
    scene bg qinhuai river
    with dissolve
    "期末考试后，我又在学校附近闲逛了几天，领略了金陵独特的美，这是我在以前未曾体验的。"
    scene bg street
    with dissolve
    m1 "终于到了出发的时候了！得赶紧收拾收拾行李！"
    "我带上了三套适合当地天气的衣服，一套休闲，一套正式。还有一套，是我应急的时候穿的。提着行李到了楼下，我离得老远就看到半夏在朝他招手。"
    m1 "早上好啊！祝你旅途有个好心情啊！"
    show banxia far bright
    f2 "早上好！给这是你的票！"
    "坐飞机去一个地方支教，真是一个不错的体验。我接过了半夏手中的票，不过我却发现是一张时长将近四十个小时的火车票。"
    menu:
        "没关系，出发吧！":
            m1 "咱们走吧！现在就出发！"
            $ val2 += 10
        "咦？怎么是火车票？":
            m1 "诶！不对啊？你不是说学校包来回的飞机吗？"
            $ val2 += 5
            f2 "啊，学校在协商的时候出了一些问题，最后只有火车票了。"
        "你怎么骗人啊？":
            m1 "你怎么骗人？这不是火车票吗？"
            $ val2 += 0
            f2 "对，对不起，我不是故意的！"
    "其实学校怎么可能报销来回的飞机票呢，那个地方附近根本就没有飞机场。"
    "就连这张票，都是半夏为了林枫自己掏钱买的。至于为什么是慢车票，看过前面的人都知道，她家已经快拿不出钱了。"
    stop music fadeout 1.0
    play music "../audio/chapter15-2.mp3"
    scene bg train day
    "一番折腾过后，两个人终于上了火车。汽笛声响起，一个新的篇章开始了。"
    "旅客朋友们你们好，欢迎乘坐K137次列车，本次列车自南通站出发，终点车站昆明。旅途风光优美，旅客在旅途困顿之余，可以欣赏沿途的美景~"
    stop music fadeout 1.0
    "在火车上总要找点事情做。半夏提到了她们地区盛行的一种卡牌游戏。"
    play music "../audio/poker.mp3"
    show banxia near calm
    f2 "你听过“干瞪眼”吗？"
    m1 "没听过，是新游戏哦？"
    show banxia near happy
    f2 "什么新游戏，比游戏还刺激！还可以教你打扑克哦！"
    m1 "你说的那么神秘干嘛？不就是一种扑克玩法吗？我学！"
    f2 "干瞪眼按照正规的方法来说。。。。"
    hide banxia
    show poker
    "接下来半夏便给我讲解了这种扑克牌的玩法，两个人打了好长一段时间。"
    "时间过得很快。经过夜间短暂的休息之后，火车已经到了新余一带。"
    hide poker
    "这里的风景，是长期在黑龙江居住的我梦中的景象。这里绿水青山依傍，空气质量也比我常年的印象要好得多。"
    "这趟车在很多站都会停下，我拍了好多好多照片，记录自己在旅程中的回忆。"
    "美中不足的是，自己提前购买的两万毫安时的充电宝，现在只剩下差不多一半的剩余电量了。自己在剩下旅途中的手机使用还是需要注意一下。"
    "火车走走停停，我的心也随之摇曳起来。不过半夏倒没有什么，她直接倒在座位上睡着了。"
    m1 "看来这种长途的火车迁徙对他来说已经成了一种习惯了呢。"
    "从前，车马很慢，书信很远，一生只够爱一个人。在K137次列车上的我，觉得自己正在站在现代与过去的分界线上。"
    "能够有这样的一种旅途，何尝不是一块人生中的新拼图呢？"
    "火车到了怀化、凯里、贵阳、六盘水。火车在黑夜中无休止的穿梭，向着另一个黎明发起冲刺。新的一天来到了。用自己的导航软件查询，昆明就在一指远处。这场旅程终于到了终点，不过属于二人的旅程还在继续……"
    stop music fadeout 1.0
    jump chapter15End