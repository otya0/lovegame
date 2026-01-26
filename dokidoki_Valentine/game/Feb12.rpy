define m = Character("紅葉", color="#d4bd9f")
define k = Character("九条", color="#9fbdc4")
define did_talk_Horror = False
label Feb12_Start:
    "講義が終わった。"
    menu:
        "どうする？"
        "映画サークルに行く":
            "よし、映画サークルに行くか。"
            jump Feb12_Circle_Arrive
        "自宅に帰る":
            "今日はもう疲れたし、家に帰ろう。"
            "こうして、あなたは８０年間自宅で過ごしましたとさ、おしまい。"
            return
        "図書館に行く":
            "図書館に行って本を借りるか。"
            jump Feb12_Library_Arrive
    jump Feb13_Start

label Feb12_Circle_Arrive:
    "部室に入った。小さい部室だ。"
    "映画サークルのメンバーは今日も二人だけだ。"
    k "あ、来たの？今日は早いね。"
    m "今日はそういう気分だったんだよ。"
    k "ふーん、そうなんだ。"
    m "で、今日は何を観るの？"
    k "うーん、どうしようか？ 見たい映画ある？"
    jump Feb12_Movie_Choice

label Feb12_Movie_Choice:
    menu:       
        "ホラー映画を提案する。" if not did_talk_Horror:
            m "ホラー映画はどう？最近いいのが出たらしいよ。"
            k "うーん、ホラーは夏がいいのよね。"
            m "そうなの？じゃあ、他のにしようか。"
            k "うん、お願い。"
            $ did_talk_Horror = True
            jump Feb12_Movie_Choice

        "コメディ映画を提案する。":
            m "コメディ映画は？最近面白いのが出たらしいよ。"
            k "いいね！それにしよう！"
            m "よし、じゃあそれに決まりだね。"
    return
label Feb12_Library_Arrive:
    return