token = "671154971:AAHQGK_JSs2n2rT_aCbRuZ3Z5ZUIT6sh0Sg"

start_mes = "Mystery House"

about = "Mystery House-приключенческая игра, выпущенная компанией On-Line Systems в 1980 году. Она была разработана, " \
        "написана и проиллюстрирована Робертой Уильямс и запрограммирована Кеном Уильямсом для Apple II. Mystery " \
        "House-первая графическая приключенческая игра и первая игра, выпущенная компанией On-Line Systems, " \
        "которая развивалась в Sierra On-Line. Это одна из самых ранних видеоигр в жанре ужасов "

error_mes = "⚠️ Бот был перезапущен ⚠️\nК сожалению произошел перезапуск бота, и вы продолжите " \
            "игру с последней контрольной точки"

repeated_marks = [[["👁 Исследовать", "explore 2"], ["📜 Читать записку", "note 1"], ["⬆️ Вперед", "candle"],
                   ["⬅️ Влево", "kitchen"], ["➡️ Вправо", "library"], ["↗️ Подняться по лестнице", "stairs on 2 floor"]],
                  [["➡️ Обратно в холл", "hall 1"],
                   ["🚰 Осмотреть раковину", "knife"], ["Осмотреть холодильник", "pitcher"]],
                  [["🖼 Взглянуть на картину", "picture"], ["🛁 В ванную", "towel"],
                   ["⬆️ Назад", "stairs on attic"]]]

events = {"yard": {"text": "Вы находитесь в переднем дворе большого заброшенного викторианского дома. Каменные ступени "
                           "ведут к широкому крыльцу",
                   "markup": [["👁 Исследовать", "explore 1"], ["⬆️ Вперед", "main door"]]},
          "explore 1": {"text": "Вы и еще семь человек оказались перед большим заброшенным домом по одной причине: вы "
                                "узнали что в этом доме спрятаны сокровища", "markup": [["⬆️ Вперед", "main door"]]},
          "main door": {"text": "Вы находитесь на крыльце. Перед вами дверь ведущая в дом",
                        "markup": [["🚪 Открыть дверь", "open main door"]]},
          "open main door": {"text": "Вы открыли дверь", "markup": [["⬆️ Вперед", "hall 0"]]},
          "hall 0": {"text": "Вы находитесь внутри дома. Дверь позади вас захлопнулась. Перед вами семеро других "
                             "персонажей. Также в этой комнате есть лестница на 2 этаж, двери в другие комнаты и "
                             "записка, лежащая на полу", "markup": repeated_marks[0]},
          "hall 1": {"text": "Вы в холле. Здесь есть лестница на 2 этаж и двери в другие комнаты",
                     "markup": repeated_marks[0][2:]},
          "explore 2": {"text": "Люди стоящие перед вами: Том, водопроводчик; Сэм, механик; Салли, швея; Доктор Грин, "
                                "хирург; Джо, могильщик; Билл, мясник и Дэйзи, повар", "markup": repeated_marks[0][1:]},
          "note 1": {"text": "В записке сказано, что драгоценности спрятаны в этом доме",
                     "markup": [["Бросить записку", "hall 0"]]},
          "note 2": {"text": "Неужели кто то пойдет на это ради сокровищ?", "markup": [["Бросить записку", "library"]]},
          "kitchen": {"text": "Вы находитесь на кухне. Перед вами печь, шкаф, холодильник, раковина, дверь обратно в "
                      "холл и дверь, ведущая на улицу.", "markup": repeated_marks[1]},
          "knife": {"text": "Вы заглянули в раковину. В ней лежит нож", "markup": [["🔪 Взять нож", "kitchen"]],
                    "command": "add knife"},
          "not knife": {"text": "Пустая раковина", "markup": [["↩️ Вернуться", "kitchen"]]},
          "pitcher": {"text": "Вы открыли холодильник. Он не работает. В нем кувшин с водой",
                      "markup": [["Взять кувшин", "kitchen"]], "command": "add pitcher"},
          "not pitcher": {"text": "Здесь пусто", "markup": [["↩️ Вернуться", "kitchen"]]},
          "candle": {"text": "Вы в столовой. Перед вами большой обеденный стол на котором стоит светильник.",
                     "markup": [["🕯 Взять светильник", "not candle"]], "command": "add candle"},
          "not candle": {"text": "Вы в столовой. Перед вами большой обеденный стол и выход и дверь во двор",
                         "markup": [["⬇️️ Обратно в холл", "hall 1"], ["🚪 Выйти во двор", "courtyard"]],
                         "command": "fire"},
          "fire": {"text": "Вы случайно задели свисающую с потолка паутину, та резко вспыхнула, и большой стол с "
                           "потолком вместе с ней. Перед вами в мгновение поднялся столб огня.",
                   "markup": [["🚪 Попытаться выбраться из комнаты", "end in fire"],
                              ["💦 Использовать кувшин с водой", "puddle with key"]]},
          "end in fire": {"text": "Вы живо рванули к двери, в надежде на спасение из пламени, но старые доски "
                                  "загорались быстрее. И когда вы оказались у двери, она была объята пламенем. Огонь "
                                  "был повсюду. К сожалению, когда пожар потушили, от вас остались лишь обгорелые "
                                  "кости.", "markup": [["🔄 Заново", "yard"]], "command": "end of game"},
          "puddle with key": {"text": "Вам успешно удалось погасить огонь из кувшина. В луже около стола, где раньше "
                                      "горело пламя, вы видите ключ. Видимо, раньше вы не замечали его в темноте.",
                              "markup": [["🔑 Взять ключ", "not candle"]], "command": "add key"},
          "courtyard": {"text": "Вы во дворе. Вы видите перед собой мертвое тело и дверь в дом",
                        "markup": [["☠️ Осмотреть тело", "dead 1"], ["🚪 Войти в дом", "candle"],
                                   ["️⤴️ Повернуть за угол", "courtyard corner"]]},
          "courtyard corner": {"text": "Вы во дворе.", "markup": [["⬅️ Обратно в библиотеку", "library"],
                                                                  ["⤵️ Повернуть за угол", "courtyard"]]},
          "library": {"text": "Вы находитесь в старой пыльной библиотеке. Перед вами диван, полки с книгами, камин и "
                              "стол на котором лежит записка.",
                      "markup": [["⬅️ Обратно в холл", "hall 1"], ["📜 Читать записку", "note 2"],
                                 ["🚪 Выйти во двор", "courtyard corner"]]},
          "dead 1": {"text": "Это Сэм, механик. Кто то нанес ему удар по голове тупым предметом",
                     "markup": [["🚪 Войти в дом", "candle"], ["️⤴️ Повернуть за угол", "courtyard corner"]]},
          "stairs on 2 floor": {"text": "Вы на втором этаже.",
                                "markup": [["↙️ Спуститься на первый этаж", "hall 1"], ["⬆️ Вперед", "stairs on attic"],
                                           ["⬅️ Влево", "door to nursery"], ["➡️ Вправо", "door to bedroom"]]},
          "stairs on attic": {"text": "Вы прошли вперед. перед вами лестница, ведущая на чердак. Дальше по коридору "
                                      "есть комната",
                              "markup": [["↗️ Подняться на чердак", "hammer"], ["➡️ Пройти дальше", "study"],
                                         ["⬅️ Назад", "stairs on 2 floor"]]},
          "hammer": {"text": "Вы на чердаке. Из окна видно лес. На полу вы видите кувалду.",
                     "markup": [["🔨 Взять кувалду", "not hammer"]], "command": "add hammer"},
          "not hammer": {"text": "Вы на чердаке. Около лестницы есть дверь.",
                         "markup": [["↙️ Спуститься вниз", "stairs on attic"], ["🚪 Пройти в дверь", "chest"]]},
          "chest": {"text": "Вы в кладовке. На полу расставлены коробки и старые чемоданы. У стены вы видите "
                            "сундук, он заперт",
                    "markup": [["🔐 Отпереть сундук", "not chest"], ["⬆️ Назад", "hammer"]]},
          "not chest": {"text": "Вы в кладовке. На полу расставлены коробки и старые чемоданы. У стены вы видите "
                                "открытый сундук", "markup": [["⬆️ Назад", "hammer"], ["👁 Содержимое сундука", "gun"]],
                        "command": "add chest"},
          "gun": {"text": "В сундуке лежит пистолет.", "markup": [["🔫 Взять пистолет", "not gun"]],
                  "command": "add gun"},
          "not gun": {"text": "В сундуке пусто", "markup": [["↩️ Вернуться", "chest"]]},
          "return chest": {"text": "Вам нечем открыть замок.", "markup": [["⬆️ Назад", "hammer"]]},
          "study": {"text": "Вы вошли в старый кабинет. В нем есть дверь, ведущая в ванную комнату, картина висящая "
                            "на стене, рабочий стол и стул.",
                    "markup": repeated_marks[2]},
          "picture": {"text": "Довольно неплохой пейзаж. Но кажется, за картиной что то есть...",
                      "markup": [["🔪 Использовать нож", "button"]]},
          "cant use knife": {"text": "У вас нет с собой ножа.", "markup": repeated_marks[2][1:]},
          "button": {"text": "Вы вырезали картину ножом. На стене, за картиной, оказалась кнопка",
                     "markup": [["🔘 Нажать кнопку", "not study"]], "command": "add study"},
          "not study": {"text": "Одна из стен в кабинете отодвинулась. За ней есть проход",
                        "markup": [["🛁 В ванную", "towel"], ["⬆️ Назад", "stairs on attic"],
                                   ["В проход в стене", "musty crawlspace"]]},
          "towel": {"text": "Вы в ванной комнате. На полу лежит труп.",
                    "markup": [["☠️ Осмотреть тело", "dead 2"], ["⬅️ Назад", "study"]]},
          "dead 2": {"text": "Это Билл, мясник. Его задушили парой колготок.",
                     "markup": [["Взять полотенце", "not towel"]], "command": "add towel"},
          "not towel": {"text": "Здесь ничего интересного", "markup": [["⬅️ Назад", "study"]]},
          "door to nursery": {"text": "Здесь дверь.",
                              "markup": [["🚪 Зайти в комнату", "nursery"], ["⬅️ Дальше по коридору", "west bedroom"],
                                         ["➡️ Назад", "stairs on 2 floor"]]},
          "nursery": {"text": "Вы в старой детской. На полу лежит тело",
                      "markup": [["☠️ Осмотреть тело", "dead 3"], ["⬆️ Назад", "door to nursery"]]},
          "dead 3": {"text": "Это труп доктора Грина. Его зарезали.", "markup": [["⬆️ Назад", "door to nursery"]]},
          "west bedroom": {"text": "Вы в западной спальне.",
                           "markup": [["📜 Читать записку", "note 3"], ["⬆️ Назад", "door to nursery"]]},
          "note 3": {"text": "💬 Вы никогда не найдете его. Все достанется мне",
                     "markup": [["Бросить записку", "west bedroom"]]},
          "door to bedroom": {"text": "Здесь дверь.",
                              "markup": [["🚪 Зайти в комнату", "dagger"], ["➡️ Дальше по коридору", "east bedroom"],
                                         ["⬅️ Назад", "stairs on 2 floor"]]},
          "dagger": {"text": "Заходя в комнату, вы заметили, как кто то метнул в вас кинжал из коридора. Вы чудом "
                             "успели увернуться.", "markup": [["🗡 Взять кинжал", "not dagger"]],
                     "command": "add dagger"},
          "not dagger": {"text": "Большая спальня. Здесь нет ничего интересного.",
                         "markup": [["⬆️ Назад", "door to bedroom"]]},
          "east bedroom": {"text": "Вы в восточной спальне. На полу мертвое тело.",
                           "markup": [["☠️ Осмотреть тело", "dead 4"], ["⬆️ Назад", "door to bedroom"]]},
          "dead 4": {"text": "Это Салли, швея. На ее одежде волос убийцы. Убийца блондин. Среди тех, кто был в холле "
                             "вместе с вами, светлые волосы имеют только Дейзи, Билл и Том.",
                     "markup": [["⬆️ Назад", "door to bedroom"]]},
          "push": {"text": "Вы снова на кухне.", "markup": repeated_marks[1] + [["❗️Отодвинуть шкаф", "break wall"]]},
          "not kitchen": {"text": "Вы на кухне", "markup": repeated_marks[1] + [["⬅️ Пролезть в дыру", "pantry"]]},
          "break wall": {"text": "За шкафом вы видите непрочную часть стены.",
                         "markup": [["🔨 Использовать кувалду", "not kitchen"]], "command": "add kitchen"},
          "musty crawlspace": {"text": "Вы прошли в разъем в стене. Она закрылась за вашей спиной. Теперь "
                                       "единственный путь ведет вниз по лестнице",
                               "markup": [["↙️ Спуститься вниз", "basement"]]},
          "pantry": {"text": "Вы оказались в небольшом помещении. Видимо, раньше это была кладовая для продуктов",
                     "markup": [["↙️ Спуститься вниз", "corridor"], ["➡️ Назад", "kitchen"]]},
          "not pantry": {"text": "Вы оказались в небольшом помещении. Видимо, раньше это была кладовая для продуктов",
                         "markup": [["↙️ Спуститься вниз", "corridor"]]},
          "corridor": {"text": "Коридор, ведущий в подвал.",
                       "markup": [["⬆️ Вперед", "basement"], ["↗️ Подняться", "pantry"]]},
          "basement": {"text": "Вы в затхлом подвале. На столе лежит ключ от входной двери.",
                       "markup": [["🔑 Взять ключ", "not basement"]], "command": "add basement"},
          "not basement": {"text": "Вы в затхлом подвале. Лестница наверх ведет в пустое помещение. На полу лежит труп",
                           "markup": [["☠️ Осмотреть тело", "dead 5"], ["⬆️ Назад в коридор", "corridor"],
                                      ["Пролезть в дыру", "tunnel"]]},
          "dead 5": {"text": "Это Том, водопроводчик. Его зарезали",
                     "markup": [["⬆️ Назад в коридор", "corridor"], ["Пролезть в дыру", "tunnel"]]},
          "tunnel": {"text": "Вы пролезли в туннель. Он ведет в лес",
                     "markup": [["Пролезть в дыру", "basement"], ["⬆️ Лезть по туннелю", "tree"]]},
          "tree": {"text": "Выйдя из леса, вы оказались перед большим деревом. На большой ветке стоит телескоп. "
                           "Забраться на ветку не так уж сложно",
                   "markup": [["🌲 Забраться", "telescope"], ["⬇️ Назад в туннель", "tunnel"],
                              ["🌲🌳🌲 Идти по лесу", "forest"]]},
          "forest": {"text": "Вы прошли по лесу и оказались у двери в кухню",
                     "markup": [["🌲 Обратно к дереву", "tree"], ["🚪 На кухню", "kitchen"]]},
          "telescope": {"text": "Телескоп направлен на окно чердака. На потолке над стремянкой вы видите кнопку.",
                        "markup": [["⬇️ Спуститься вниз", "tree"]], "command": "add attic"},
          "attic": {"text": "Вы на чердаке. Кнопка действительно находиться над стремянкой.",
                    "markup": [["🔘 Нажать кнопку", "tower"], ["↙️ Спуститься вниз", "stairs on attic"],
                               ["🚪 Пройти в дверь", "chest"]]},
          "tower": {"text": "На чердаке вы видите Дейзи. Она не собирается делиться сокровищами. У нее в руках записка",
                    "markup": [["😵 Избавиться от Дейзи", "not tower"]], "command": "add tower"},
          "not tower": {"text": "Вы взяли записку. В ней сказано о тайнике в подвале дома. Стоит спуститься туда "
                                "снова.", "markup": [["Дойти до подвала", "jewels"]]},
          "jewels": {"text": "Вы дошли до подвала. Как и говорилось в записке, в стене подвала есть один "
                             "выступающий кирпич, скрытый под слоем водорослей.",
                     "markup": [["Подцепить его ножом", "not jewels"]]},
          "not jewels": {"text": "Вы вытащили кирпич. За ним, в стене были спрятаны драгоценные камни. Теперь вы "
                                 "нашли сокровища, и у вас есть ключ от входной двери.",
                         "markup": [["💎 Завершить игру", "victory"]], "command": "end"},
          "victory": {"text": "🏁🏁 Поздравляем, вы завершили игру.", "markup": [["🔄 Играть еще раз", "yard"]]}
          }
