#!/usr/bin/env python
#encoding: utf-8

from third_part import pyMoeFou

def GetSongUrlByName(name):
    mf = pyMoeFou.MoeFou()
    songList = mf.GetSongByName(name)
    for s in songList:
        upList = mf.GetUpBySong(s)
        if upList:
            up = upList[-1]
            m = mf.GetMusicByID(s.parent_wiki)
            print("{} - {}: {}".format(s.title.encode("utf8"), m.title.encode("utf8"), up.url))

GetSongUrlByName("my life")
# OUT: 1-11 Words that changed my life - TVアニメ『Free!』オリジナルサウンドトラック Ever Blue Sounds: http://nyan.90g.org/6/9/a8/f24474b2d557adc459d405eb82691c4f.mp3
# OUT: Someday of my life - ラブライブ!  μ&#039;s Best Album Best Live! collection 【Blu-ray Disc付 超豪華盤】: http://nyan.90g.org/2/7/43/0811ed7dd408fe77c6f1f2ca92c3143f.mp3
# OUT: 陽ノ下葵(CV.海保絵果) - Happy my life ～Thank you for everything!!～ (Aoi in KARAOKE room Autumn Accoustic Ver.) - D.C.III~ダ・カーポIII~ドラマCDコレクション vol.3 feat.陽ノ下葵: http://nyan.90g.org/4/e/1d/22f6126f3b1fc194b24d1583c76d74be.mp3
# OUT: My life - YOU&amp;YU: http://nyan.90g.org/b/1/97/b6d2ccb137e8d470775938b2c38da62b.mp3
# OUT: My Life (Off Vocal) - Realization(初回限定盤)(DVD付): http://nyan.90g.org/e/d/34/402354764e7bedbd05eb9c105eb18404.mp3
# OUT: My Life - Realization(初回限定盤)(DVD付): http://nyan.90g.org/6/5/90/8c7edb1674720c11c8ed8c7858c79a2d.mp3
# OUT: My life - 空のコトバ: http://nyan.90g.org/7/c/c1/44d99c6236a7bc889ade64a26350e788.mp3
# OUT: A way of Life -Deep inside my mind Remix- - ペルソナ3ポータブル オリジナル・サウンドトラック: http://nyan.90g.org/e/9/dc/2907424c8adfff21d887054748613491.mp3
# OUT: Happy my life～Thank you for everything!!～ - CIRCUS 10th Collect Disc08: http://nyan.90g.org/d/4/84/bc4c0998e53d3a1109fb0812b27ce5fa.mp3
# OUT: a day of my life - a day of my life: http://nyan.90g.org/9/0/a6/5fb99453e795614ff7a3c967026832a2.mp3
# OUT: Start in my life - THE BEST OF DETECTIVE CONAN 2 ~名探偵コナン テーマ曲集2~ (通常盤): http://nyan.90g.org/2/6/b5/95239f0681d02192038e205fe9718b3d.mp3
# OUT: my hope ship life - 「シャイニング・ハーツ」Original Soundtrack: http://nyan.90g.org/0/d/d1/65ac43afdd9a3839d02f73f024699aa2.mp3
# OUT: When Will My Life Begin (Reprise) - Tangled (Soundtrack from the Motion Picture): http://nyan.90g.org/c/4/1c/c3da22a1cc22510cb8c553d2da4e4e5c.mp3
# OUT: When Will My Life Begin (Reprise) - Tangled (Soundtrack from the Motion Picture): http://nyan.90g.org/f/2/3a/4b1d18c32757626cc563c9d92668cf20.mp3
# OUT: When Will My Life Begin? - Tangled (Soundtrack from the Motion Picture): http://nyan.90g.org/8/d/9d/3d0600513f2b4649c28b091976b6d836.mp3
# OUT: Light My Life（万年置き伞にご注意を） - Silver Drive: http://nyan.90g.org/a/b/a9/276328377a0d952d60aaf47e9387adfb.mp3
# OUT: Once In My Life - Euphorise: http://nyan.90g.org/5/f/12/447402b01952c35037ad4a1917da7224.mp3
# OUT: IN MY LIFE - 銀魂BEST2: http://nyan.90g.org/5/2/d1/d45051b868628a54f4e1426cbeb76675.mp3
# OUT: my life -farewell arrange- - 噬神者 爆裂 广播剧&amp;OST: http://nyan.90g.org/7/4/f3/2f7497543122812e092d12dfbe686fab.mp3
# OUT: Drumming Shining My Life - TVアニメ「けいおん! ! 」キャラクターイメージCDシリーズ 「けいおん! ! 」イメージソング 田井中律: http://nyan.90g.org/3/7/f3/3525c568138b96a771992df30e64a3e0.mp3
# OUT: my life - 噬神者 OST: http://nyan.90g.org/4/e/09/bf5da9c9debeaab064d904b0d589c29b.mp3
# OUT: my life -シオのうた- - 噬神者 OST: http://nyan.90g.org/2/1/69/494b9225ca021c1ae356589a78e23073.mp3

