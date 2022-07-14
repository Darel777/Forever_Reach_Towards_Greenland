label chapter17Start:
    play music "../audio/chapter17.mp3"
    scene bg village
    "我和半夏，两个人开始在双柏县穿梭。两个人从汽车客运站出发，一路向北。"
    "一路上，我都没有说话。我在丈量着双柏的每一寸土地。在这里，我看到了自己的城市十几年前的影子。那个留存于记忆中的城市，小而温暖，自己和朋友外出游玩的时候不会感觉到任何的劳累。"
    "我虽然没有来到过这里，但是却找到了家的感觉。"
    show banxia far happy
    "两个人继续这样走着，穿过一片六层楼的居民区，来到了一片彩钢房附近。半夏脸上的疲惫瞬间消散，她看到他的父母正站在其中一个彩钢房门口，焦急地等待着她的到来。"
    f2 "欢迎欢迎，这里就是我的家了！"
    "我没有感到一丝的惊讶，甚至开始心疼起自己旁边的这个小姑娘。从南京到双柏的票，即使是半价，也需要五百多块钱。这对于一个住在这种房屋的家庭来说，也是一笔不小的数目。"
    "从这样偏僻的地方来，到这么远的地方上学，也是一种勇气。"
    hide banxia
    m1 "叔叔阿姨好！"
    "半夏父亲" "孩子！欢迎你！一路上颠簸了这么久，饿了吧！我给你们做好饭了，快进来吃！"
    "我摸了摸自己的肚子。我的胃自从晕车后就始终是空的。经历了初到双柏短暂的激动之后，确实是饿了。"
    m1 "谢谢款待！那我就不客气了！"
    "我和半夏走进屋子，开始享用美餐。"
    "蝉鸣，风声，闲聊之声，声声入耳。"
    "水车，树木，孩童之景，景景动心。"
    scene bg black
    "到了晚上了，我在半夏家为自己准备的屋子里面休息。今天已经疲惫地不想再动弹。美中不足的是，长年的阴间作息让他现在根本睡不着。"
    m1 "无聊。去哪里呢，我查一下。。。什么，双柏县竟然有电影院！我去看场电影吧！听说最近郑爽的那部片子不错。。。"
    "从床上爬起来，穿好衣服，准备出门。不过我察觉到了一丝不对劲。"
    "门边似乎有什么响动。不会遇到小偷了吧？可是这个点还不是很晚啊，小偷不会选择这个时间出动，怎么办？"
    menu:
        "不开门":
            "唔，不开门了，锁好门回去睡觉。"
        "开门":
            "打开门与门外的人正面对峙！"
            $ val2 += 10
            show banxia front curious
            "打开门一看，半夏正倚在门口，好像在听着什么。这下倒好，半夏重心不稳，直接倒在了屋子内侧的位置。"
            "我赶快很快把半夏扶了起来。"
            m1 "你怎么在这？我正要去找你呢？"
            show banxia front embarrassed
            f2 "我，我路过！想看看你能不能适应，睡着没有！你刚才不是说找我吗！正好！咱们走吧！"
            m1 "可是我还没有说去哪啊！"
            f2 "对哦。"
            m1 "我刚才看到市中心那边有一家电影院。咱们去看电影啊！我请客！"
            f2 "好啊！"
            hide banxia
            scene bg cinema
            "我们在街头走着。虽然时间才九点出头，但是街上的行人已经十分稀少了。"
            "两人来到电影院，买了票后便开始等待。"
            show banxia front curious
            "电影开始了，与其说是买票，倒不如说是包场。偌大的剧场里面，只有我们两个人。我紧张地偷偷瞄了她一眼，正看见她也在偷瞄我。"
            "电影开始了。这真是一部好电影。剧情的安排，音乐的穿插都十分的到位。唯一美中不足的一点，就是感觉女主和配音怎么都对不上，感觉女主像是一个混子。"
            m1 "一定是我才疏学浅了！这应该是一种新的演绎方式！通过口型和配音的不一致来引发观众的思考！"
            "“我愿意跟在你身后，像影子追着光梦游。。。”"
            show banxia front cry
            "电影至最动人处，歌曲追光者轻轻地响了起来。半夏哭了，眼泪啪嗒啪嗒地往下掉。"
            "我拿出自己随身准备的纸，开始为半夏擦眼泪。"
            "半夏见到此番场景，更加慌乱了。她干脆直接躲在我的怀里，哭了起来。"
            m1 "诶，你干什么！啊 好吧！真是服了你了！也不知道你什么时候能长大！"
            "半夏比我要成熟的多，可她毕竟是个女孩。在自己喜欢的人面前，仍然会展露自己真实的一面。"
            scene black
            "夜深了，我们回到家中。我进了自己的屋子，拉开窗帘，在萤火虫的陪伴中入眠。"
    stop music fadeout 1.0
    jump chapter17End