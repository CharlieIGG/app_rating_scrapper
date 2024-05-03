# Define a list of app_names and app_ids
app_list = [
    {"app_name": "rodauapp", "app_id": 1128735481},
    {"app_name": "löwenbündel", "app_id": 1555115158},
    {"app_name": "typisch-sylt", "app_id": 1014930650},
    {"app_name": "mark-e", "app_id": 1613757282},
    {"app_name": "stadtwerke-lüdenscheid", "app_id": 1618049828},
    {"app_name": "meine-enni", "app_id": 1047155954},
    {"app_name": "wetzlarapp", "app_id": 1245573216},
    {"app_name": "my-mkg", "app_id": 6466412785},
    {"app_name": "bad-tabarz2go", "app_id": 1458634996},
    {"app_name": "igudd", "app_id": 1586767337},
    {"app_name": "mainova", "app_id": 1590992330},
    {"app_name": "meine-mvv", "app_id": 935183881},
    {"app_name": "naturenergie-netze-app", "app_id": 1572647918},
    {"app_name": "naturenergie-netze-app", "app_id": 1572647918},
    # https://apps.apple.com/de/app/netzinfobb/id1146814709
    {"app_name": "netzinfo", "app_id": 1146814709},
    # https://apps.apple.com/tr/app/dreiheit/id1623868205
    {"app_name": "dreiheit", "app_id": 1623868205},
    # https://apps.apple.com/de/app/meine-svb/id6444028433
    {"app_name": "meine-svb", "app_id": 6444028433},
    # https://apps.apple.com/de/app/meinheidelberg/id525396199
    {"app_name": "meinheidelberg", "app_id": 525396199},
    # https://apps.apple.com/us/app/meine-werke/id1618928592
    {"app_name": "meine-werke", "app_id": 1618928592},
    # https://apps.apple.com/de/app/i-love-alz/id1613787135
    {"app_name": "i-love-alz", "app_id": 1613787135},
    # https://apps.apple.com/de/app/3-2-1-app/id979841785
    {"app_name": "3-2-1-app", "app_id": 979841785},
    # https://apps.apple.com/de/app/stadtwerke-br%C3%BChl/id6476326018
    {"app_name": "stadtwerke-brühl", "app_id": 6476326018},
    # https://apps.apple.com/us/app/buxtuell-schlau-wer-sie-hat/id1169036500
    {"app_name": "buxtuell", "app_id": 1169036500},
    # https://apps.apple.com/de/app/mein-crailsheim/id1324604599
    {"app_name": "mein-crailsheim", "app_id": 1324604599},
    # https://apps.apple.com/de/app/swapp/id1377206688
    {"app_name": "swapp", "app_id": 1377206688},
    # https://apps.apple.com/de/app/meine-swd/id1671154951
    {"app_name": "meine-swd", "app_id": 1671154951},
    # https://apps.apple.com/de/app/sw-app/id6446178181
    {"app_name": "sw-app", "app_id": 6446178181},
    # https://apps.apple.com/de/app/gt-fair-netzt/id1107687404
    {"app_name": "gt-fair-netzt", "app_id": 1107687404},
    # https://apps.apple.com/de/app/hamm/id1499349216
    {"app_name": "hamm", "app_id": 1499349216},
    # https://apps.apple.com/de/app/f%C3%BCr-dich-stadtwerke-heidelberg/id1157634583
    {"app_name": "für-dich-stadtwerke-heidelberg", "app_id": 1157634583},
    # https://apps.apple.com/de/app/herborn-erleben/id6452756176
    {"app_name": "herborn-erleben", "app_id": 6452756176},
    # https://apps.apple.com/de/app/iz4you/id1268554672
    {"app_name": "iz4you", "app_id": 1268554672},
    # https://apps.apple.com/de/app/swk-app/id1160799695
    {"app_name": "swk-app", "app_id": 1160799695},
    # https://apps.apple.com/de/app/stadtwerke-karlsruhe/id946029381?platform=iphone
    {"app_name": "stadtwerke-karlsruhe", "app_id": 946029381},
    # https://apps.apple.com/de/app/mein-konstanz/id1227695672
    {"app_name": "mein-konstanz", "app_id": 1227695672},
    # https://apps.apple.com/de/app/meinl%C3%BCbeck/id1066411856
    {"app_name": "meinlübeck", "app_id": 1066411856},
    # https://apps.apple.com/de/app/meine-sle/id6460013862
    {"app_name": "meine-sle", "app_id": 6460013862},
    # https://apps.apple.com/de/app/momend/id975736670
    {"app_name": "momend", "app_id": 975736670},
    # https://apps.apple.com/de/app/enzjoy/id1554453311
    {"app_name": "enzjoy", "app_id": 1554453311},
    # https://apps.apple.com/de/app/unsernms/id1221244758
    {"app_name": "unsernms", "app_id": 1221244758},
    # https://apps.apple.com/us/app/ruppin2go/id1281900103
    {"app_name": "ruppin2go", "app_id": 1281900103},
    # https://apps.apple.com/de/app/taunaapp-oberursel/id1102934206
    {"app_name": "taunaapp-oberursel", "app_id": 1102934206},
    # https://apps.apple.com/us/app/swp2go/id1671158926
    {"app_name": "swp2go", "app_id": 1671158926},
    # https://apps.apple.com/de/app/mein-plauen/id1613923753
    {"app_name": "mein-plauen", "app_id": 1613923753},
    # https://apps.apple.com/de/app/echt-potsdam/id1122410415
    {"app_name": "echt-potsdam", "app_id": 1122410415},
    # https://apps.apple.com/de/app/mein-row/id1636309124
    {"app_name": "mein-row", "app_id": 1636309124},
    # https://apps.apple.com/de/app/mein-schkeuditz/id1238298599?l=en
    {"app_name": "mein-schkeuditz", "app_id": 1238298599},
    # https://apps.apple.com/de/app/schwerte-app/id986529992
    {"app_name": "schwerte-app", "app_id": 986529992},
    # https://apps.apple.com/de/app/stadtwerke-soltau/id6464325158
    {"app_name": "stadtwerke-soltau", "app_id": 6464325158},
    # https://apps.apple.com/de/app/mein-speyer/id1380285642
    {"app_name": "mein-speyer", "app_id": 1380285642},
    # https://apps.apple.com/de/app/tro4me/id1265140309
    {"app_name": "tro4me", "app_id": 1265140309},
    #  https://apps.apple.com/us/app/wappfels/id1313206941
    {"app_name": "wappfels", "app_id": 1313206941},
    # https://apps.apple.com/de/app/wei%C3%9Fwass-er-leben/id1439434938
    {"app_name": "weißwasser-leben", "app_id": 1439434938},
    # https://apps.apple.com/de/app/winsen4you/id1459517017
    {"app_name": "winsen4you", "app_id": 1459517017},
    # https://apps.apple.com/de/app/meine-wvv/id957820409
    {"app_name": "meine-wvv", "app_id": 957820409},
    # https://apps.apple.com/de/app/moin-f%C3%B6hr/id1195126387
    {"app_name": "moin-föhr", "app_id": 1195126387},
    # https://apps.apple.com/de/app/coburg-erleben/id1640514919
    {"app_name": "coburg-erleben", "app_id": 1640514919},
    # https://apps.apple.com/de/app/travenetz/id1523794537
    {"app_name": "travenetz", "app_id": 1523794537},
    # https://apps.apple.com/de/app/mein-zbl/id6468662564
    {"app_name": "mein-zbl", "app_id": 6468662564},
]