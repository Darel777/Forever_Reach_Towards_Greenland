label chapter22Start:
    m1 "半夏，有时间吗？等到放暑假之后，咱们去上海玩啊！反正闲着也是闲着。"
    show banxia jk happy
    f2 "可以的，正好我也没什么事！你想哪一天出发？"
    m1 "就明天吧！你如果同意了我就去买票！"
    show banxia jk bright
    f2 "明天不行！你再给我两天时间吧！我还有些急事要处理！"
    m1 "好，都听你的。"
    hide banxia

    scene bg market
    show banxia far happy
    "半夏这两天还真没有什么事。自从上次回家乡宣讲之后，自己对林枫的好感愈发强烈了起来。她在想，这次旅行，是不是她此生仅有的向心上人吐露真心的机会。"
    "她听说我最近在写环境论文的时候遇到了一点问题，便想买点礼物来让我的心情好一点。可是买什么呢？？这个问题白芷想了好几天，也没有答案。而我的邀约又近在眼前了，已经不能继续拖下去了。"
    "半夏造访了南京的许多商场，但是还是没有买到自己喜欢的东西。就在她灰心丧气之际，附近展台上的吊坠吸引了她的目光。"
    "这个吊坠并不是真金白银或奇石珍宝做成的。相反，和那些吊坠相比，它显得非常简约优雅。一片叶子镶嵌在吊坠中间的水晶中，呈现一种静谧的美。"
    "工作人员" "您真有眼光！这是我们相应国家号召精心打造的环保限定吊坠！每一片叶子，都像是一艘小船，承载着情侣之间的爱！七夕马上就要到了，如果您给你的男朋友买一份，一定是不错的选择！"
    f2 "这不正和林枫未来的职业相配吗？本来她还有些犹豫，但是当工作人员说出“男朋友”三个字的时候，她的内心便不再犹豫了。"
    f2 "说得真好！我这就买！帮我包装一下，谢谢。"

    scene bg shanghai
    "2017年7月19日"
    "魔都上海，被誉为中国继曹县之后的第二大都市。虽然和曹县还是有一些差距，但是这里高楼林立的美景，还是迷倒了一大片人。"
    "上海外滩，人头攒动，其中不乏一对对的手挽手走着的情侣。我们两人也开始在长江边上漫步。"
    "夜上海，夜上海，你是个不夜城~"
    "两个人一起在上海的街头漫步，在南京路步行街领略了最繁华商业街的美景。"
    "旅行的第二站是迪士尼，这也是半夏主动提出要去的地方。两人在去迪士尼之前决定现在上海市区住一个晚上。"
    "我们来到了一家旅店。看到双人间的价格只比单人间贵了20\%，我开始犹豫起来。这次旅行的费用是由我买单的，而得知要去迪士尼的我，心中不能保证预算一定是够的。订哪个呢？"
    show banxia far happy
    f2 "您好，订一间双人间。"
    hide banxia
    m1 "等等！我还没同意呢！让我再想想！"
    menu:
        "选择单人间":
            jump chapter23Mid
        "选择双人间":
            "两个人最终开了一间房间。我小心地走进浴室，将透明的玻璃用手边的一切东西挡好，这才松了一口气，开始洗澡。"
            "他听到了浴室外面的敲门声。"
    m1 "你别进来啊！我跟你说，咱们还不是那种关系，咱们是出来玩的！"
    show banxia far happy
    f2 "瞧给你吓得。不过你这么一说，我还挺激动的。有时候，理智会让我们做出一些正确的事情，可感情却偏偏逆道而行。让我们今天把该做的事情都做完吧~"
    m1 "不要！"
    hide banxia
    jump chapter22End