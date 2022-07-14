label chapter12Start:
    play music "../audio/chapter12.mp3"
    scene bg blue sky
    with dissolve
    "在半梦半醒之中，我看到了家乡的天空。天空万里无云，太阳也被拉的很远，但是却十分晃眼睛。"
    "正常人看到外面的这番场景便会转过头去，可是我没有。也许我对家乡的情结不是阳光能够阻挡的。"
    "要下飞机了呢。"
    scene bg plane
    show baizhi near happy
    m1 "对于南星计划，你有什么想法吗？想在三中做什么活动呢？"
    f1 "活动的话。。。在三中。。。还是算了吧。"
    m1 "不对啊？不是你说要领我来这边进行招生宣讲的吗？那我们手里还有这么多物资怎么处理呢？"
    f1 "我是这样想的。你不是一中的学生吗？咱们就在一中做活动吧，把这些材料都给一中的同学。"
    m1 "那三中怎么办？"
    show baizhi near cry
    f1 "三中根本没人能考上南大。每年三中的最高分不过600出头。想让三中出个好苗子，很蓝的啦！"
    m1 "？？？那你不是南大的学生吗？"
    f1 "要不是我在衡水借读，在三中我也考不上的。"
    f1 "要我说，三中的一系列行政问题，真是让人焦头烂额。领导班子换了一批又一批，根本没有为我们学生做实事的。都只是想把这里当作跳板。"
    f1 "校领导得过且过，根本不思进取。改革浮于表面，流于形式。想改变现状的人遭到排挤。现在的校领导，配不上这里的学生和老师。"
    f1 "可是我又有什么办法呢？"
    m1 "害，不要再回忆那些了。那我们就在一中宣传吧。你有没有什么宣传的妙计？"
    show baizhi near happy
    f1 "我有一个好办法，不知道你会不会同意。"
    m1 "你说说看。"
    f1 "咱们两个装成情侣，模拟一下到了南大之后的幸福生活。这样学生们也愿意看。你看行吗？"
    menu:
        "演就演呗":
            m1 "嗯，你还别说，不仅他们期待，我也挺期待的。演这么一把也没什么损失。"
            $ val1 += 5
            f1 "好好好，那就这么定了！趁现在一中的学生还没放假，我们尽快准备吧！"
        "是你想看戏吧":
            m1 "我看，是你想看戏吧！我可不和你演。"
            $ val1 += 2
            show baizhi near angry
            f1 "胡说？我不还是为了招生？你怎么这样凭空污人清白？就这么定了！我就是问问你的意见，你说的不算！"
        "怎么可能？":
            m1 "没门！李在赣神魔？"
            show baizhi near angry
            $ val1 += 0
            f1 "哼，你不会以为我在征求你的意见吧，我只是告诉你一声罢了！"
    m1 "额，那好吧，都听你的。"
    scene bg airport
    with dissolve
    "下飞机后，两人在机场走过一段路程，取过行李后，我和白芷都看到了来接自己的亲人。"
    m1 "今天很开心，那就先聊到这里吧！咱们家长来了，改日再见！"
    show baizhi near calm
    f1 "嗯！"
    hide baizhi

    "一中还有一周的时间就放假了，所以两个人必须尽快做好准备。为了不耽误事，两个人在微信上又聊了起来。"
    play sound "../audio/message.mp3"
    show phone wechat
    f1 "林枫，我跟你说，我想好了，咱们到时候进学校就拿我的剧本。白芷说着传过一个word文档。"
    m1 "这是什么？让我看看？什么？对绿色我们永远向往？这不是这个galgame的废弃名吗？用它干嘛？"
    "作者" "不是我说，你怎么知道的？我让你怎么说，你就怎么说，别说这么多废话行不？"
    m1 "好的好的，作者大人，我知道错了。"
    m1 "我看看里面的内容哈。"
    "我看到了：（包括但不限于）两个人手牵着手走进每一个班级的门，在单身狗们艳羡的目光下尽情地宣传南大；让我领着白芷进教师办公室，转交南大的宣传资料，等等。"
    menu:
        "你疯了吧？":
            m1 "你是不是疯了？绝对不能这么干！我不同意，会在全校同学面前社死的！"
            $ val1 += 2
        "有点太张扬了。":
            m1 "啊这，要不咱们别这么张扬，宣传的话还是低调一些好一点，免得其它竞争学校误会"
            $ val1 += 5
    f1 "你说的好像有点道理。确实是我写得有点过了。不过后天我们就要去宣讲了，你总不能不去吧？"
    menu:
        "你又不是一中的学生":
            m1 "我寻思你也不是一中的学生啊，要不去也应该是你不去吧？"
            $ val1 += 0
        "这个剧本太离谱了":
            m1 "这可难办了。但是我还是要说，这个文档写得有点太过了！作为一个牡丹的我根本不能接受！咱们得收敛一点！"
            $ val1 += 5
    f1 "不去？怎么可能？我总不能当队长什么事情都不干吧？"
    f1 "那好吧，你说了算，那你把咱们的行动纲领修改一下！散会！"
    hide phone
    m1 "两个人微信聊天算什么散会啊？真是奇怪的人！"
    stop music fadeout 1.0
    jump chapter12End