import sqlite3
g='Аудит,Бизнес-планирование,История искусств,Декоративно-прикладное искусство и народные промыслы,Практика производственная (преддипломная),Графический дизайн,Организация обслуживания,Биология,Иностранный язык,Правовое обеспечение профессиональной деятельности,Анатомия,Экономика отрасли,Ландшафтный дизайн,Физическая культура,Литература,Введение в специальность,включая информатику,Администрирование сетевых операционных систем,Информационное общество (включая информатику и обществознание),Информационные технологии в профессиональной деятельности,Метрология и стандартизация,Организация и ведение процессов приготовления,оформления и подготовки к реализации полуфабрикатов для блюд,кулинарных изделий сложного ассортимента,Технология сложных хлебобулочных,мучных кондитерских изделий,Информационное общество (обществознание),Психология общения,Основы анализа бухгалтерской отчётности,Компьютерная графика,География,Астрономия,Кавказская и кубанская кухня,Введение в специальность (информатика),Безопасность жизнедеятельности,Дополнительная работа под руководством преподавателя,Зарубежная кухня,Технология приготовления сложной горячей кулинарной продукции,Основы спортивной тренировки,Организация физкультурно-спортивной работы,Организация расчетов с бюджетом и внебюджетными фондами,Дискретная математика,Контроль качества продукции,1С: Бухгалтерия,Основы банковского дела,Самостоятельная работа,Практические основы бухгалтерского учета имущества организации,Бухгалтерский учет и отчетность в бюджетных организациях,История мировой культуры,Производственная практика,Дизайн в сфере применения,Практика учебная,Цветоводство и декоративное древоводство,Гигиенические основы физической культуры и спорта,Менеджмент ФК и спорта,Основы флористики,Базовые и новые физкультурно-спортивные виды деятельности с методикой оздоровительной тренировки,Русский язык,Избранный вид спорта с методикой тренировки и руководства соревновательной деятельностью спортсменов,История,Инженерная,компьютерная графика,Безопасность функционирования информационных систем,Операционные системы и среды,Правовые основы профессиональной деятельности,Приготовление,оформление и подготовка к реализации хлебобулочных,мучных кондитерских изделий разнообразного ассортимента,Технология приготовления простой и основной кулинарной продукции,Этика профессиональной деятельности,Основы бухгалтерского учета,Художественное проектирование изделий декоративно-прикладного и народного искусства,Менеджмент,Декоративная дендрология,Технология приготовления коктейлей,Родной язык,Основы безопасности жизнедеятельности,Композиция,оформление и подготовка к реализации холодных и горячих сладких блюд,десертов,напитков разнообразного ассортимента,Оборудование предприятий общественного питания,Технология физкультурно-спортивной деятельности,Налоги и налогообложение,Математика,Математическое и имитационное моделирование,Практика производственная,Иностранный язык в профессиональной деятельности,Методы расчёта основных технико-экономических показателей дзайна,Основы менеджмента  и маркетинга,Основы философии,Рисунок,Дизайн и рекламные технологии,Естествознание,Фитодизайн,Русский язык и культура речи,Основы биомеханики,История дизайна,Основы конструкторско-технологического обеспечения дизайна,Информатика,Операционные системы,Организация и контроль текущей деятельности подчиненного персонала,Приготовление и подготовка к реализации полуфабрикатов для блюд,кулинарных изделий разнообразного ассортимента,Теоретические и прикладные аспекты методической работы педагога по физической культуре и спорту,Основы проектной и компьютерной графики,Основы экономики,Защита растений,Живопись,Организация хранения и контроль запасов сырья,Информационное обеспечение профессиональной деятельности,Основы исполнительского мастерства (художественное стекло,бисер),Охрана труда,Техническое оснащение и организация рабочего места,Физика,Математика и информатика,Основы программирования,Практические основы бухгалтерского учета источников формирования имущества организации,Экономика организации,Рисунок с основами перспективы,Дизайн-проектирование (композиция,макетирование,современные концепции в искусстве),Региональные кухни,Лечебная физическая культура и массаж,Обществознание,Основы проектирования объектов садово-паркового строительства,Компьютерные сети,Проектирование предприятий общественного питания,Управление структурным подразделением организации,Перспектива,менеджмента и маркетинга,Выполнение работ по профессии Цветовод,Живопись с основами цветоведения,Физиология питания,Информационное общество (информатика),Первичная обработка продукции,Техническое оснащение организаций питания,Численные методы,Прикладная математика,Финансы,денежное обращение и кредит,Бухгалтерская технология проведения и оформления инвентаризации,Экономика,Основы врачебного контроля,Обществознание (включая Право),Организация администрирования компьютерных систем,Технология приготовления хлебобулочных изделий и хлеба,Эстетика и дизайн в оформлении кулинарных и кондитерских изделий,Педагогика,Экологические основы природопользования,Садово-парковое строительство и хозяйство,Колористика,оформление и подготовка к реализации горячих блюд,кулинарных изделий,закусок разнообразного ассортимента,Элементы высшей математики,Химия,Основы стандартизации,сертификации и метрологии,Материаловедение,Спортивная физиология,Технологии физического уровня передачи данных,Управление структурным подразделением,Маркетинг ландшафтных услуг,Учебная практика (изучение памятников искусства в других городах),Технология приготовления блюд и кулинарных изделий для диетического,лечебно-профилактического питания,Элементы математической логики,Химия с элементами биологии,Основы управления качеством,Основы информационного и библиографического поиска,Физиология с основами биохимии,Экономические и правовые основы профессиональной деятельности,Цветовод (цветоводство в благоустройстве),Технология исполнения изделий декоративно-прикладного и народного искусства (художественная роспись по дереву),Учебная практика,Выполнение работ по профессии Кассир,Шрифты и основы шрифтовой композиции (с присвоением квалификации исполнитель художественно-оформительских работ),Физическая и коллоидная химия почасовая,Системное программирование,Практические основы бухгалтерского учёта активов организации,Технология составления бухгалтерской отчётности,Химия с элементами физики,Основы бухгалтерского учета в общественном питании,Статистика,'
#print(','.join('"'+h.strip().__str__()+'"' for h in g.split(',')))
GROUPS=["ЧИПфд-01-21","ЧИПфд-02-21","ЧСАфд-01-21","ЧСАфд-02-21","ЧИПфд-01-20","ЧСАфд-01-20","ЧПКфд-01-20","ЧПКфд-02-20","ЧИПфд-01-19","ЧСАфд-01-19","ЧПКфд-01-19","ЧИПфд-01-18","ЧСАфд-01-18","ЧПКфд-01-18","ЧЭБфд-01-21","ЧЭБфд-02-21","ЧЭБфд-01-20","ЧЭБфд-02-20","ЧЭБфд-01-19","ЧФУфд-01-21","ЧФУфд-02-21","ЧФУфд-01-20","ЧФУфд-02-20","ЧФУфд-01-19","ЧФУфд-02-19","ЧФУфд-01-18","ЧФУфд-02-18","ЧСЛфд-01-21","ЧСЛфд-01-20","ЧСЛфд-01-19","ЧСЛфд-01-18","ЧНПфд-01-21","ЧДЗфд-01-21","ЧНПфд-01-20","ЧДЗфд-01-20","ЧНПфд-01-19","ЧДЗфд-01-19","ЧДЗфд-01-18","ЧПВфд-01-21","ЧПВфд-02-21","ЧРРфд-01-21","ЧППфд-01-20","ЧПВфд-01-20","ЧРРфд-01-20","ЧППфд-01-19","ЧПВфд-01-19","ЧРРрд-01-19","ЧППфд-01-18","ЧПВфд-01-18","ЧРРфд-01-18"]
PREPODS=['Андросова П.К.',
'Аникина Г.Ю.',
'Антонова Е.И.',
'Бараш Л.А.',
'Белоусова И.А.',
'Великанов Е.Э.',
'Вершинина Н.П.',
'Габуния А.Я.',
'Горнушкина О.Н.',
'Горохова А.А.',
'Григорьева О.А.',
'Догадов Д.И.',
'Дымов Е.В.',
'Жук Л.И.',
'Зорова О.В.',
'Игошев М.В.',
'Иджиян Т.Ю.',
'Исаева В.В.',
'Истягина И.В.',
'Казакова Н.А.',
'Казарова Л.Р.',
'Караманян М.И.',
'Карпов А.И.',
'Каспарян К.И.',
'Кислова М.Е.',
'Корниенко Н.Я.',
'Кузнецова О.О.',
'Лежнева О.Д.',
'Ливенцова Т.Д.',
'Макарова К.Б.',
'Мелентьева А.Д.',
'Миносян Р.Х.',
'Муллакова А. М.',
'Муллакова А.М.',
'Нагорняя М.В.',
'Нубарян В.А.',
'Огаркова Л.А.',
'Панова Н.А.',
'Пересунько-Гончарова Т.В.',
'Подгорнова Т.П.',
'Родионова И.А.',
'Сарахатунова И.В.',
'Сигова Е.В.',
'Силаев А.И.',
'Слюсаренко Л.Э.',
'Соболева Н.Л.',
'Суркова Ю.А.',
'Сущенко С.С.',
'Талантова Е.А.',
'Цатурян С.А.',
'Цымбалова Ю.С.',
'Чайкина М.Л.',
'Чехова Т.М.',
'Юргина Л.А.',
'Яворский В.Н.',
'Жук Л.И./Иджиян Т.Ю.']
AUDITORIES=['1-5',
'1-6',
'1-7',
'1-8',
'1-9',
'1-11',
'1-13',
'1-15',
'1-16',
'1-17',
'1-18',
'1-Лаб',
'1-УТЦ',
'3-30',
'3-30а',
'3-34',
'3-Лаб',
'4-26',
'4-27',
'4-29',
'4-31',
'4-32',
'4-33',
'1-стадион',
'2-стадион',
'3-стадион',
'1-ЭИОС',
'1-13/1-15',
'1-5/1-15',
'1-5/1-6',]
lessons=["Аудит","Бизнес-планирование","История искусств","Декоративно-прикладное искусство и народные промыслы","Практика производственная (преддипломная)","Графический дизайн","Организация обслуживания","Биология","Иностранный язык","Правовое обеспечение профессиональной деятельности","Анатомия","Экономика отрасли","Ландшафтный дизайн","Физическая культура","Литература","Введение в специальность","включая информатику","Администрирование сетевых операционных систем","Информационное общество (включая информатику и обществознание)","Информационные технологии в профессиональной деятельности","Метрология и стандартизация","Организация и ведение процессов приготовления","оформления и подготовки к реализации полуфабрикатов для блюд","кулинарных изделий сложного ассортимента","Технология сложных хлебобулочных","мучных кондитерских изделий","Информационное общество (обществознание)","Психология общения","Основы анализа бухгалтерской отчётности","Компьютерная графика","География","Астрономия","Кавказская и кубанская кухня","Введение в специальность (информатика)","Безопасность жизнедеятельности","Дополнительная работа под руководством преподавателя","Зарубежная кухня","Технология приготовления сложной горячей кулинарной продукции","Основы спортивной тренировки","Организация физкультурно-спортивной работы","Организация расчетов с бюджетом и внебюджетными фондами","Дискретная математика","Контроль качества продукции","1С Бухгалтерия","Основы банковского дела","Самостоятельная работа","Практические основы бухгалтерского учета имущества организации","Бухгалтерский учет и отчетность в бюджетных организациях","История мировой культуры","Производственная практика","Дизайн в сфере применения","Практика учебная","Цветоводство и декоративное древоводство","Гигиенические основы физической культуры и спорта","Менеджмент ФК и спорта","Основы флористики","Базовые и новые физкультурно-спортивные виды деятельности с методикой оздоровительной тренировки","Русский язык","Избранный вид спорта с методикой тренировки и руководства соревновательной деятельностью спортсменов","История","Инженерная","компьютерная графика","Безопасность функционирования информационных систем","Операционные системы и среды","Правовые основы профессиональной деятельности","Приготовление","оформление и подготовка к реализации хлебобулочных","мучных кондитерских изделий разнообразного ассортимента","Технология приготовления простой и основной кулинарной продукции","Этика профессиональной деятельности","Основы бухгалтерского учета","Художественное проектирование изделий декоративно-прикладного и народного искусства","Менеджмент","Декоративная дендрология","Технология приготовления коктейлей","Родной язык","Основы безопасности жизнедеятельности","Композиция","оформление и подготовка к реализации холодных и горячих сладких блюд","десертов","напитков разнообразного ассортимента","Оборудование предприятий общественного питания","Технология физкультурно-спортивной деятельности","Налоги и налогообложение","Математика","Математическое и имитационное моделирование","Практика производственная","Иностранный язык в профессиональной деятельности","Методы расчёта основных технико-экономических показателей дзайна","Основы менеджмента  и маркетинга","Основы философии","Рисунок","Дизайн и рекламные технологии","Естествознание","Фитодизайн","Русский язык и культура речи","Основы биомеханики","История дизайна","Основы конструкторско-технологического обеспечения дизайна","Информатика","Операционные системы","Организация и контроль текущей деятельности подчиненного персонала","Приготовление и подготовка к реализации полуфабрикатов для блюд","кулинарных изделий разнообразного ассортимента","Теоретические и прикладные аспекты методической работы педагога по физической культуре и спорту","Основы проектной и компьютерной графики","Основы экономики","Защита растений","Живопись","Организация хранения и контроль запасов сырья","Информационное обеспечение профессиональной деятельности","Основы исполнительского мастерства (художественное стекло","бисер)","Охрана труда","Техническое оснащение и организация рабочего места","Физика","Математика и информатика","Основы программирования","Практические основы бухгалтерского учета источников формирования имущества организации","Экономика организации","Рисунок с основами перспективы","Дизайн-проектирование (композиция","макетирование","современные концепции в искусстве)","Региональные кухни","Лечебная физическая культура и массаж","Обществознание","Основы проектирования объектов садово-паркового строительства","Компьютерные сети","Проектирование предприятий общественного питания","Управление структурным подразделением организации","Перспектива","менеджмента и маркетинга","Выполнение работ по профессии Цветовод","Живопись с основами цветоведения","Физиология питания","Информационное общество (информатика)","Первичная обработка продукции","Техническое оснащение организаций питания","Численные методы","Прикладная математика","Финансы","денежное обращение и кредит","Бухгалтерская технология проведения и оформления инвентаризации","Экономика","Основы врачебного контроля","Обществознание (включая Право)","Организация администрирования компьютерных систем","Технология приготовления хлебобулочных изделий и хлеба","Эстетика и дизайн в оформлении кулинарных и кондитерских изделий","Педагогика","Экологические основы природопользования","Садово-парковое строительство и хозяйство","Колористика","оформление и подготовка к реализации горячих блюд","кулинарных изделий","закусок разнообразного ассортимента","Элементы высшей математики","Химия","Основы стандартизации","сертификации и метрологии","Материаловедение","Спортивная физиология","Технологии физического уровня передачи данных","Управление структурным подразделением","Маркетинг ландшафтных услуг","Учебная практика (изучение памятников искусства в других городах)","Технология приготовления блюд и кулинарных изделий для диетического","лечебно-профилактического питания","Элементы математической логики","Химия с элементами биологии","Основы управления качеством","Основы информационного и библиографического поиска","Физиология с основами биохимии","Экономические и правовые основы профессиональной деятельности","Цветовод (цветоводство в благоустройстве)","Технология исполнения изделий декоративно-прикладного и народного искусства (художественная роспись по дереву)","Учебная практика","Выполнение работ по профессии Кассир","Шрифты и основы шрифтовой композиции (с присвоением квалификации исполнитель художественно-оформительских работ)","Физическая и коллоидная химия почасовая","Системное программирование","Практические основы бухгалтерского учёта активов организации","Технология составления бухгалтерской отчётности","Химия с элементами физики","Основы бухгалтерского учета в общественном питании","Статистика"]
highles = [
('Scientific writing',17),
('Writing in the Sciences',18),
('Адвокатура',19),
('Административное право',20),
('Административный процесс',21),
('Акушерство и гинекология',22),
('Анализ данных',23),
('Анатомия животных',24),
('Английский язык .',25),
('Аннотирование и реферирование (первый иностранный язык)',26),
('Антикризисное управление',27),
('Арбитражный процесс',28),
('Археология',29),
('Архитектура информационных систем',30),
('Аудит',31),
('Базы данных',32),
('Банковский надзор',33),
('Банковское дело',34),
('Безопасность жизнедеятельности',35),
('Биологическая физика',36),
('Биологическая химия',37),
('Биология',38),
('Биология клетки: Биофизика',39),
('Биология клетки: Биохимия',40),
('Биология клетки: Цитология',41),
('Биофизика',42),
('Болезни рыб, птиц, зоопарковых и диких животных',43),
('Бухгалтерский учет и анализ',44),
('Бюджетная система РФ',45),
('Введение в литературоведение',46),
('Введение в прикладную информатику',47),
('Введение в профессиональную деятельность',48),
('Введение в специальность',49),
('Ведение переговоров и деловое общение',50),
('Ветеринарная вирусология',51),
('Ветеринарная микробиология и микология',52),
('Ветеринарная радиобиология',53),
('Ветеринарная санитария',54),
('Ветеринарная фармакология',55),
('Ветеринарно-санитарная экспертиза',56),
('Ветеринарно-санитарные меры и оформление документов',57),
('Ветеринарно-санитарный контроль',58),
('Ветеринарно-санитарный контроль качества сырья и продуктов животного и растительного происхождения',59),
('Ветеринарное законодательство',60),
('Вирусология и биотехнология',61),
('Внутренние незаразные болезни',62),
('Возрастная физиология',63),
('Вредные и опасные вещества в промышленности',64),
('Выпуск учебных СМИ',65),
('ГИС в экологии и природопользовании',66),
('Гематология',67),
('География',68),
('Геология',69),
('Геохимия окружающей среды',70),
('Геоэкология',71),
('Государственно-частное партнерство в развитии экономики регионов',72),
('Гражданский процесс',73),
('Гражданское право',74),
('Гражданское право зарубежных стран',75),
('Деловая коммуникация в сфере юриспруденции (иностранный язык, дополнительные разделы)',76),
('Делопроизводство и подготовка юридических документов',77),
('Деньги, кредит, банки',78),
('Диалектология страны изучаемого языка (первый иностранный язык)',79),
('Дискретная математика',80),
('Древнерусская литература',81),
('Жилищное право',82),
('Земельное право',83),
('Зоология',84),
('Зоопсихология',85),
('Иммунология',86),
('Инвестиционный менеджмент и маркетинг',87),
('Инновационный менеджмент',88),
('Иностранный язык',89),
('Иностранный язык (делового общения)',90),
('Иностранный язык (дополнительные разделы',91),
('Иностранный язык (дополнительные разделы)',92),
('Иностранный язык (продвинутый уровень)',93),
('Иностранный язык .',94),
('Иностранный язык / Русский язык для иностранных студентов',95),
('Иностранный язык в профессиональной деятельности',96),
('Иностранный язык в профессиональной сфере',97),
('Иностранный язык в сфере юриспруденции',98),
('Иностранный язык/русский язык в сфере юриспруденции',99),
('Инструментальные методы диагностики',100),
('Интеллектуальные системы',101),
('Интернет-программирование',102),
('Информатика',103),
('Информационная безопасность',104),
('Информационное право',105),
('Информационные системы в экономике',106),
('Информационные системы и технологии',107),
('Информационные технологии в профессиональной деятельности',108),
('Информационные технологии в юриспруденции',109),
('Информационный бизнес',110),
('История',111),
('История Азии и Африки',112),
('История Америки',113),
('История Большого Сочи',114),
('История Древнего мира',115),
('История Новейшего времени',116),
('История Нового времени',117),
('История России XVII-XVIII в.',118),
('История России ХIX в.',119),
('История России ХХ в.',120),
('История Средних веков',121),
('История античной литературы',122),
('История государства и права России',123),
('История зарубежной журналистики',124),
('История зарубежной литературы XIX в.',125),
('История зарубежной литературы XVII- XVIII веков',126),
('История зарубежной литературы ХХ века',127),
('История и культура стран изучаемого языка (первый иностранный язык)',128),
('История исторической науки',129),
('История мировой и отечественной культуры',130),
('История отечественной журналистики',131),
('История первобытного общества',132),
('История русского литературного языка',133),
('История русской литературы XIX в.',134),
('История русской литературы XIX века',135),
('История средневековой России',136),
('История экономических учений',137),
('Клиническая биохимия',138),
('Клиническая диагностика',139),
('Компьютерная графика',140),
('Компьютерные технологии и статистические методы в экологии природопользовании',141),
('Конституционное право России',142),
('Конституционное право зарубежных стран',143),
('Концепции современного естествознания',144),
('Кормление животных с основами кормопроизводства',145),
('Корпоративные финансы',146),
('Корпоративные финансы (продвинутый курс)',147),
('Криминалистика',148),
('Лёгкая атлетика',149),
('Латинский язык',150),
('Легкая атлетика',151),
('Лексикология',152),
('Лингвистическое комментирование художественного текста (второй иностранный язык)',153),
('Лингвистическое комментирование художественного текста (первый иностранный язык)',154),
('Лингвокультурологический анализ текста',155),
('Литература стран изучаемого языка (первый иностранный язык)',156),
('Литература стран третьего иностранного языка',157),
('Литература эпохи Возрождения',158),
('Логика',159),
('Макроэкономика',160),
('Макроэкономика (продвинутый курс)',161),
('Макроэкономическое планирование и прогнозирование',162),
('Маркетинг',163),
('Математика',164),
('Математический анализ',165),
('Международная торговля',166),
('Международное право',167),
('Международные стандарты финансовой отчетности',168),
('Международный коммерческий арбитраж',169),
('Менеджмент',170),
('Методика обучения иностранным языкам',171),
('Методика преподавания истории',172),
('Методика преподавания обществознания',173),
('Методика преподавания русского языка в средней школе',174),
('Методика преподавания русского языка как иностранного',175),
('Методология экономических исследований',176),
('Методы контроля состояния окружающей среды',177),
('Методы определения и оценки эколого-экономического ущерба от загрязнения окружающей среды',178),
('Методы оптимальных решений',179),
('Методы химико-токсикологический экспертизы',180),
('Микробиология',181),
('Микроэкономика',182),
('Микроэкономика (продвинутый курс)',183),
('Мировая экономика и международные экономические отношения',184),
('Мировые информационные ресурсы',185),
('Миф о Петре I в русской исторической памяти',186),
('Моделирование бизнес-процессов',187),
('Морфология',188),
('Назначение наказаний',189),
('Налоги и налогообложение',190),
('Налоговое администрирование',191),
('Налоговое право',192),
('Наследственное право РФ и зарубежных стран',193),
('Науки о Земле: Геология',194),
('Науки о земле: География',195),
('Национальная экономика',196),
('Немецкий язык .',197),
('Неорганическая и аналитическая химия',198),
('Неорганическая химия',199),
('Нормирование и снижение загрязнения окружающей среды',200),
('Нотариат',201),
('Общая биология',202),
('Общая и частная хирургия',203),
('Общая психология',204),
('Общая теория перевода',205),
('Общая экология',206),
('Общее языкознание',207),
('Объектно-ориентированное программирование',208),
('Организация PR-кампаний',209),
('Органическая и физколлоидная химия',210),
('Органическая химия',211),
('Основы государства и права / История государства и права зарубежных стран',212),
('Основы журналистской деятельности',213),
('Основы зоотехнии',214),
('Основы инженерной экологии',215),
('Основы информационного и библиографического поиска',216),
('Основы научных исследований в экономике',217),
('Основы риторики',218),
('Основы риторики и коммуникации',219),
('Основы теории литературы',220),
('Основы теории межкультурной коммуникации',221),
('Основы теории публицистики',222),
('Основы физиологии',223),
('Основы филологии',224),
('Основы экономики и менеджмента',225),
('Охрана окружающей среды',226),
('Оценка воздействия на окружающую среду',227),
('Паразитарные болезни',228),
('Паразитология и инвазионные болезни',229),
('Патологическая анатомия животных',230),
('Патологическая анатомия и судебно-ветеринарная экспертиза',231),
('Патологическая физиология',232),
('Педагогика',233),
('Политология',234),
('Право интеллектуальной собственности',235),
('Право социального обеспечения',236),
('Правоведение',237),
('Правовые основы природопользования и охраны окружающей среды',238),
('Правоохранительные органы',239),
('Практикум  по орфографии',240),
('Практикум общественно-политической речи (первый иностранный язык)',241),
('Практикум по культуре речевого общения (второй иностранный язык)',242),
('Практикум по культуре речевого общения (первый иностранный язык)',243),
('Практикум по лингвистическому анализу текста',244),
('Практикум по межкультурной коммуникации',245),
('Практикум по методике грамматического разбора',246),
('Практикум по стилистике русского языка',247),
('Практическая риторика',248),
('Практический курс иностранного языка (второй иностранный язык)',249),
('Практический курс иностранного языка (первый иностранный язык)',250),
('Преддипломная практика/Преддипломная практика',251),
('Предпринимательское право',252),
('Проблемы фальсификации истории',253),
('Программная инженерия',254),
('Проектирование информационных систем',255),
('Проектное финансирование и анализ',256),
('Проектный практикум',257),
('Производные финансовые инструменты',258),
('Производственная практика/Ветеринарно-санитарная практика',259),
('Производственная практика/Врачебно-производственная практика',260),
('Производственная практика/Научно-исследовательская работа',261),
('Производственная практика/Научно-исследовательская работа (по теме выпускной квалификационной работы)',262),
('Производственная практика/Педагогическая',263),
('Производственная практика/Педагогическая (в общеобразовательной школе)',264),
('Производственная практика/Технологическая (проектно-технологическая)',265),
('Прокурорский надзор',266),
('Профессиональная этика филолога',267),
('Профессиональная этика юриста',268),
('Профессиональный иностранный язык (английский)',269),
('Психология',270),
('Психология и педагогика',271),
('Работа журналиста в газете',272),
('Радиоэкологическая безопасность территорий',273),
('Радиоэкология',274),
('Разведение с основами частной зоотехнии',275),
('Разработка приложений для мобильных устройств',276),
('Региональная история',277),
('Редактирование научных и официально-деловых текстов',278),
('Ресурсосбережение и использование малоотходных технологий',279),
('Римское право',280),
('Русский язык для иностранных студентов',281),
('Русский язык для иностранных студентов (дополнительные разделы)',282),
('Русский язык и культура речи',283),
('Рынок ценных бумаг',284),
('Селекция и генетика',285),
('Системный анализ и менеджмент рисков',286),
('Современные проблемы экологии и природопользования',287),
('Сопоставительно-типологическое языкознание',288),
('Социальная экология',289),
('Социально-экономическая статистика',290),
('Социология',291),
('Сравнительно-историческое  языкознание',292),
('Старославянский язык',293),
('Стратегическое планирование',294),
('Страхование',295),
('Судебная ветеринарно-санитарная экспертиза',296),
('Судебная медицина и вскрытие животных',297),
('Таможенное право',298),
('Теория вероятностей и математическая статистика',299),
('Теория второго иностранного языка',300),
('Теория государства и права',301),
('Теория и методология истории',302),
('Теория литературы',303),
('Теория первого иностранного языка',304),
('Теория систем и системный анализ',305),
('Теория статистики',306),
('Техника и технология СМИ',307),
('Техногенные системы и экологический риск',308),
('Токсикология с основами фармакологии',309),
('Токсикология. Экологическая эпидемиология',310),
('Торговое дело',311),
('Трудовое право',312),
('Уголовно-исполнительное право',313),
('Уголовное право',314),
('Уголовное право зарубежных стран',315),
('Уголовный процесс',316),
('Управление информационными системами',317),
('Управление персоналом',318),
('Управление проектами',319),
('Устойчивое развитие',320),
('Учебная практика/Ознакомительная',321),
('Учебная практика/Ознакомительная, преп 1',322),
('Учебная практика/Ознакомительная, преп 3',323),
('Учебная практика/Практика по получению первичных профессиональных умений и навыков, преп 1',324),
('Учебная практика/Практика по получению первичных профессиональных умений и навыков, преп 2',325),
('Учение и биосфере',326),
('Фармакология',327),
('Фармацевтическая химия',328),
('Фауна Кавказа',329),
('Физика',330),
('Физиология и этология животных',331),
('Физиология: Иммунология',332),
('Физиология: Физиология высшей нервной деятельности',333),
('Физическая культура и спорт',334),
('Философия',335),
('Философия научного знания',336),
('Финансовая статистика',337),
('Финансовое право',338),
('Финансовые рынки, институты и инструменты',339),
('Финансовые системы зарубежных стран',340),
('Финансовый контроль и аудит',341),
('Финансовый менеджмент',342),
('Финансы',343),
('Флора Кавказа',344),
('Фонетика',345),
('Фразеология',346),
('Французский язык .',347),
('Цитология, гистология и эмбриология',348),
('Цифровая экономика',349),
('Человек западноевропейского Средневековья в своем мире',350),
('Человек и его здоровье',351),
('Экологическая экспертиза и оценка воздействия на окружающую среду',352),
('Экологические аудит, менеджмент и экспертиза',353),
('Экологические основы гигиены',354),
('Экологические технологии утилизации отходов',355),
('Экологический аудит и экологический менеджмент',356),
('Экологический мониторинг',357),
('Экологический мониторинг в геоэкологической оценке территорий',358),
('Экологическое право',359),
('Экология и рациональное природопользование',360),
('Эконометрика',361),
('Эконометрика (продвинутый курс)',362),
('Экономика',363),
('Экономика и организация бизнеса',364),
('Экономика труда',365),
('Экономика фирмы',366),
('Экономико-математические методы и модели',367),
('Экономическая безопасность',368),
('Экономическая информатика',369),
('Экономическая теория',370),
('Экспертиза мяса и мясопродуктов',371),
('Экспрессивно-стилистические основы перевода (первый иностранный язык)',372),
('Эпидемиология. Экология эндемических растений',373),
('Эпизоотология и инфекционные болезни',374),
('Этика специалиста',375),
('Этимология современного русского языка',376),
('Легкая атлетика.',377),
('Биохимия человека',378),
('Консультация. Математический анализ',379),
('Древние языки и культуры',380),
('Основы рекламы и PR',381),
('Математические методы в исторических исследованиях',382),
('Роль личности в истории',383),
('Этнология и социальная антропология',384),
('Введение в теорию перевода',385),
('Культура научного исследования',386),
('История зарубежной литературы Средних веков и эпохи Возрождения',387),
('Устное народное творчество',388),
('Методика преподавания литературы',389),
('История русской литературы XX века',390),
('Работа по развитию речи на уроках русского языка',391),
('Вспомогательные исторические дисциплины',392),
('Источниковедение',393),
('Основы теории журналистики',394),
('Стилистика и литературное редактирование',395),
('Тележурналистика',396),
('Язык СМИ',397),
('Практикум по орфографии и пунктуации',398),
('Научно-исследовательская работа (получение первичных навыков научно-исследовательской работы)',399),
('Экономическая политика и финансы российских регионов',400),
('Проведение деловых и научных презентаций',401),
('Введение в журналистику',402),
('Введение в языкознание',403),
('Баскетбол',404),
('Ботаника',405),
('Математика и информатика',406),
('Анатомия человека',407),
('Прикладная физическая культура и спорт',408),
('Основы научных исследований в зкологии и природопользовании',409),
('Методика преподавания экологии и географии',410),
('Биология клетеи: Гистология',411),
('Биология клетки: Гистология',412),
('Основы научных исследований в биологии',413),
('Методика преподавания экологии и биологии',414),
('Основы экологии и природопользования на туристских территориях',415),
('Экология и природопользование на ООПТ',416),
('Химия окружающей среды',417),
('Экологическая физиология',418),
('Метрология,стандартизация и сертификация',419),
('Экология и природопользование на особо охраняемых природных территориях',420),
]
conn = sqlite3.connect("exl1.db")

cursor = conn.cursor()

spam = list(range(1, 187))
res = [tuple(spam[i:i + 1]) for i in range(0, len(spam), 1)]

#c = cursor.execute('SELECT * FROM GROUPS')
#c = cursor.execute('SELECT  * FROM AUDITORIES')
#for i in range(len(AUDITORIES)):
#   cursor.execute('INSERT INTO AUDITORIES VALUES(?);',(AUDITORIES[i],))

#cursor.executemany('INSERT INTO LESSONS(NameLesson,IdLesson) VALUES (?,?)',highles)
#conn.commit()


#c = cursor.executemany('INSERT INTO AUDITORIES(Auditories,id) VALUES (?,null)',res)
#conn.commit()