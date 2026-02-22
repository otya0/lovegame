# game/script.rpy

define p = Character("主人公")
define g1 = Character("さくら")
define g2 = Character("みお")
define g3 = Character("れいな")
define g4 = Character("あかり")

define police = Character("警察")
default talked_count = 0
default dating = False
default girlfriend_name = ""
default remaining_girls = [1, 2, 3, 4]
default choco_cnt = 0
image school = "images/school.png"
image girl1 = "images/g1.PNG"
image girl2 = "images/g2.PNG"
image girl3 = "images/g3.PNG"
image girl4 = "images/g4.PNG"
# 今話している相手（1〜4）
default current_girl = 0

init python:
    import random
    def success90():
        return random.random() < 0.90
    def success30():
        return random.random() < 0.30
    def success15():
        return random.random() < 0.15
    def confession_from_choco():
        return random.random() < 0.15


label start:
    p "今日はバレンタイン当日。友達みたいな距離感の女子に話かけて見るか"
    jump hub


label hub:
    if dating:
        jump bad_end_cold_eyes

    if len(remaining_girls) == 0:
        menu:
            "もう4人に話しかけた。どうする？"
            "帰る":
                if choco_cnt == 0:
                    jump normal_end
                else:
                    jump choco_get_end
            "さらに女子に話しかける（危険）":
                jump bad_end_police
    show school
    menu:
        "どうする？"
        "女子に話しかける":
            jump talk_girl
        "帰る":
            jump normal_end


label talk_girl:
    $ girl = random.choice(remaining_girls)
    $ remaining_girls.remove(girl)
    $ current_girl = girl

    if girl == 1:
        jump scene_g1
    elif girl == 2:
        jump scene_g2
    elif girl == 3:
        jump scene_g3
    else:
        jump scene_g4


# ---- 各女子の説明 ----

label scene_g1:
    show girl1
    p "あ、あれはさくらさん。！？"
    p "クラスでも有名な優等生。いつも落ち着いてて、笑うとちょっとだけ破壊力がある。"
    p "でも近づくと、意外と距離感がシビアらしい…"
    voice "audio/g1/8-13.wav"
    g1 "あ、どうしたの？"
    jump choice_menu_common

label scene_g2:
    show girl2
    p "あ、あれはみおさん。！？"
    p "明るくて誰とでも話せるタイプ。友達は多いけど、恋愛面は謎が多い。"
    p "噂だと、押しに弱いようで押しに強い…（どっちだよ）"
    voice "audio/g2/6.wav"
    g2 "どうしたの？"
    jump choice_menu_common

label scene_g3:
    show girl3
    p "あ、あれはれいなさん。！？"
    p "無表情がちでクール。だけど話すとちゃんと優しいらしい。"
    p "ただし、変なこと言うと一瞬で心を閉ざす…って聞いた"
    voice "audio/g3/10.wav"
    g3 "あ、どうしたの？"
    jump choice_menu_common

label scene_g4:
    show girl4
    p "あ、あれはあかりさん。！？"
    p "いつも眠そうで、ぼーっとしてる。けど成績は意外と良いらしい。"
    p "バレンタインのチョコは…すごいって聞いたことがある"
    voice "audio/g4/46.wav"
    g4 "あ、どうしたの？"
    jump choice_menu_common


# ---- 共通の選択肢 ----
label choice_menu_common:
    menu:
        "何て言う？"
        "チョコをください":
            jump ask_choco
        "僕と付き合ってください":
            jump ask_date


# ====== ここから「今の相手」によって喋るキャラを分岐させる ======


label ask_choco:
    p "チョコをください！"

    if confession_from_choco():
        if current_girl == 1:
            voice "audio/g1/8.wav"
            g1 "……その、"
            voice "audio/g1/8-2.wav"
            g1 "義理チョコというより本命なんだけど"
            voice "audio/g1/8-3.wav"
            g1 "私と付き合ってくれますか？"
        elif current_girl == 2:
            voice "audio/g2/6-2.wav"
            g2 "……ねえ。"
            voice "audio/g2/6-3.wav"
            g2 "私と付き合ってみない？"
        elif current_girl == 3:
            g3 "……。"
            voice "audio/g3/10-2.wav"
            g3 "私と付き合って"
        else:
            voice "audio/g4/46-2.wav"
            g4 "チョコより先に、私と付き合ってください。"

        jump girl_confession

    if success30():
        if current_girl == 1:
            voice "audio/g1/8-4.wav"
            g1 "ふふ、いいよ。はい、チョコ。"
            python:
                choco_cnt += 1
        elif current_girl == 2:
            voice "audio/g2/6-4.wav"
            g2 "はいっ、チョコ！"
            python:
                choco_cnt += 1
        elif current_girl == 3:
            voice "audio/g3/10-3.wav"
            g3 "はい、あげる..."
            python:
                choco_cnt += 1
        else:
            voice "audio/g4/46-3.wav"
            g4 "がめついね。あげる。"
            python:
                choco_cnt += 1
        p "やった、ありがとう！"
        if current_girl == 1:
            hide girl1
        elif current_girl == 2:
            hide girl2
        elif current_girl == 3:
            hide girl3
        else:
            hide girl4
    else:
        if current_girl == 1:
            voice "audio/g1/g1.mp3"
            g1 "チョコ用意してないよ？クラスメイト以上友達未満じゃん。"
        elif current_girl == 2:
            voice "audio/g2/6-5.wav"
            g2 "ごめんね、嫌いとかじゃないよ！準備してないだけで"
        elif current_girl == 3:
            voice "audio/g3/10-4.wav"
            g3 "もっと仲良くなってからね。"
        else:
            voice "audio/g4/46-4.wav"
            g4 "ごめん、そういうのはちょっと.."
        p "うっ…心が折れそうだ…"
        if current_girl == 1:
            hide girl1
        elif current_girl == 2:
            hide girl2
        elif current_girl == 3:
            hide girl3
        else:
            hide girl4

    jump hub


label ask_date:
    p "僕と付き合ってください！"

    if success15():
        if current_girl == 1:
            voice "audio/g1/8-7.wav"
            g1 "真面目にいってる？"
            voice "audio/g1/8-8.wav"
            g1 "……ふふ。"
            voice "audio/g1/8-9.wav"
            g1 "いいよ。"
            $ girlfriend_name = "さくら"
        elif current_girl == 2:
            voice "audio/g2/6-7.wav"
            g2 "えっ、急だね！？。"
            voice "audio/g2/6-8.wav"
            g2 "……でも、嫌じゃないから、デートしてそこで決めてあげる！"
            $ girlfriend_name = "みお"
        elif current_girl == 3:
            voice "audio/g3/10-5.wav"
            g3 "……いいよ。"
            voice "audio/g3/10-6.wav"
            g3 "これからよろしくね？"
            $ girlfriend_name = "れいな"
        else:
            voice "audio/g4/g4.mp3"
            g4 "…うん。いいよ"
            $ girlfriend_name = "あかり"

        $ dating = True
        jump good_end
    else:
        if current_girl == 1:
            voice "audio/g1/8-10.wav"
            g1 "えっ…ごめん。私はあなたのことしらないから"
            p "俺はさくらさんに認知されていなかったのか..."
        elif current_girl == 2:
            voice "audio/g2/6-9.wav"
            g2 "それはびっくり！"
            voice "audio/g2/6-10.wav"
            g2 "ごめん、今はそういう気分じゃないからな"
            p "断り方が優しいなと思った。この頃の自分に感謝"
        elif current_girl == 3:
            voice "audio/g3/10-7.wav"
            g3 "セクハラですよね？"
            p "最近は告白しただけで書類送検される時代だってことを忘れていたよ"
        else:
            voice "audio/g4/g4-1.mp3"
            g4 "えっ…ごめん。恋愛する体力がないから無理"
            p "いっそのこと生理的に無理ですと断ってくれ！"
            
        p "そ、そっか…！"
        if current_girl == 1:
            hide girl1
        elif current_girl == 2:
            hide girl2
        elif current_girl == 3:
            hide girl3
        else:
            hide girl4
        jump hub


label girl_confession:
    p "えっ…！？"
    p "（逆告白！？）"

    if success90():
        if current_girl == 1:
            voice "audio/g1/8-11.wav"
            g1 "決まりだね。これからよろしく。"
            $ girlfriend_name = "さくら"
            hide girl1
        elif current_girl == 2:
            voice "audio/g2/g2.mp3"
            g2 "決まりだね。これからよろしく。"
            $ girlfriend_name = "みお"
            hide girl2
        elif current_girl == 3:
            voice "audio/g3/g3.mp3"
            g3 "決まりだね。これからよろしく。"
            $ girlfriend_name = "れいな"
            hide girl3
        else:
            voice "audio/g4/46-5.wav"
            g4 "決まりだね。これからよろしく。"
            $ girlfriend_name = "あかり"
            hide girl4

        $ dating = True
        jump good_end
    else:
        if current_girl == 1:
            voice "audio/g1/8-12.wav"
            g1 "……冗談。"
            p "冗談だってさ、はは、、"
            hide girl1
        elif current_girl == 2:
            voice "audio/g2/6-11.wav"
            g2 "……冗談。びっくりした？"
            p "うーん、勢いが足りなかったか？"
            hide girl2
        elif current_girl == 3:
            voice "audio/g3/10-8.wav"
            g3 "冗談なの。びっくりさせようと思って、怒った？"
            p "悪い子猫ちゃんだぜ。全く。"
            hide girl3
        else:
            voice "audio/g4/46-6.wav"
            g4 "私たちってそんなに仲良くないでしょ。"
            p "意識が喪失しそうだった。けどなんとか意識を保った自分を褒めたい"
            hide girl4

        p "心臓に悪い！！"
        jump hub


# ---- エンディング ----
label good_end:
    p "信じられない…本当に付き合うことになった。"
    p "[girlfriend_name]さんと手をつないで、帰り道がやけに明るく見えた。"
    return

label normal_end:
    p "今日はここまでにしておこう。"
    p "バレンタインは…来年もある。"
    p "きっと多分。"
    return
label choco_get_end:
    p "チョコを{choco_cnt}個もらったぞ。"
    p "やっぱり持つべきものは友達だな。"
    return
label bad_end_police:
    p "……さらに声をかけようとした、その瞬間。"
    police "ちょっと君、話を聞こうか"
    p "BAD END：職質"
    return

label bad_end_cold_eyes:
    p "（もう恋人いるのに、また話しかけるのは…）"
    p "周りの視線が冷たい。"
    p "BAD END：信頼崩壊"
    return
