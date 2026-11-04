# Отчет о фактчекинге заявлений по usbliter8 (dim04)

[Русский](ios_jb_audit_dim04.md) | [中文版](ios_jb_audit_dim04-zh.md)

- Дата проверки: 2026-10-17
- Метод проверки: Поиск в англоязычных источниках (16 независимых поисков + постраничный сбор данных), перекрестное сопоставление ≥15 независимых источников.
- Первоначальное раскрытие: Публикация Paradigm Shift «Introducing usbliter8: An A12/A13 SecureROM Exploit» от 2026-06-18 по адресу `https://ps.tc/pages/blog-usbliter8.html`; оригинальный репозиторий PoC: `github.com/prdgmshift/usbliter8`. **Оба ресурса были удалены 2026-07-23 по решению федерального суда США** (подробности в разделе «Важный фоновый контекст» ниже); оригинал доступен через архивы Wayback Machine (снимок от 2026-06-18)[^1^][^2^][^3^].

---

## 1. Попунктный вердикт

### Утверждение 1: usbliter8 — это аппаратная уязвимость BootROM (SecureROM) в чипах A12/A13, которую Apple не может устранить системным обновлением

**Вердикт: Подтверждено (Достоверность: Высокая)**

- Название статьи при публикации: *"Introducing usbliter8: An A12/A13 SecureROM Exploit"*, Paradigm Shift опубликовала подробный write-up и рабочий PoC 2026-06-18[^1^][^2^].
- Причина уязвимости — переполнение вниз (pointer underflow) DMA-указателя в USB-контроллере Synopsys DesignWare DWC2 (при получении 4-го Setup-пакета адрес DMA фиксированно откатывается назад на 24 байта, тогда как короткий пакет инкрементирует счетчик лишь на фактическую длину, порождая underflow на 12 байт), в сочетании с тем, что в SecureROM на чипах A12/A13 блок USB DART настроен в режиме bypass. Прошивка SecureROM высечена в кремниевой маске ПЗУ кристалла: «никакое обновление iOS никогда ее не закроет»[^4^][^5^].
- Цитата Paradigm Shift: *"As these vulnerabilities remain in unmodified code, affected users should know that upgrading to more modern hardware remains the most effective way to mitigate the risks."*[^6^]
- Точные границы уязвимости: Публичный PoC поддерживает **A12, A13, S4, S5**; чипы **A12X/A12Z теоретически уязвимы, но в PoC поддержка не реализована** (по состоянию на октябрь 2026 года). По данным The Apple Wiki затрагиваются версии SecureROM 3865.0.0.4.7 – 4479.0.0.100.4, закрыто в 5281.0.0.100.45[^2^][^7^][^8^].
- Примечание: Раскрытие координировалось с Apple Product Security[^4^].

### Утверждение 2: Требует физического доступа (DFU + USB + микроконтроллер вроде RP2350), публичных инструментов джейлбрейка нет

**Вердикт: Частично подтверждено — первая часть верна, утверждение «нет публичных инструментов» устарело / частично опровергнуто (Достоверность: Высокая)**

- Условие физического доступа достоверно и подтверждено всеми источниками: требуется физическое владение аппаратом, ручной ввод в режим DFU и подключение микроконтроллера по USB, время срабатывания < 2 секунд[^4^][^7^][^9^]. Уточнение: в основном используется **RP2350** (Raspberry Pi Pico 2 / Waveshare RP2350 USB-A); **RP2040 также может применяться, но процент успеха существенно ниже**[^2^][^10^].
- Однако фраза «нет публичных инструментов джейлбрейка» на октябрь 2026 года **не соответствует действительности**:
  - Около 2026-07-25 проект сообщества **usbliter8-fun** (github.com/34306/usbliter8-fun на базе ранних наработок wh1te4ever и патчей Huy Nguyen) публично реализовал **привязанный root-джейлбрейк iOS 27.0 beta 2 на iPhone 11 Pro** с патчами ядра/DeviceTree, внедрением SSH и установкой Sileo[^11^][^12^].
  - Компания Elcomsoft 2026-07-15 выпустила **форк ipwndfu** на базе usbliter8 (примитивы R/W/X + патчи сигнатур BootROM) для интеграции в iOS Forensic Toolkit[^10^].
  - Появились подробные руководства по сборке SSH ramdisk и платы аппаратного взлома (например, "SUNSHINE RP2354A Pico DFU" по цене ~$10)[^13^][^14^].
- Корректная формулировка: **Пока не существует удобного полупривязанного (semi-tethered) инструмента пользовательского уровня по типу checkra1n**; из-за ужесточения BPR в iOS 17 (при загрузке через DFU сопроцессор SEP отказывается расшифровывать /var, вызывая панику ядра) создание полупривязанного джейлбрейка на A12/A13 считается **невозможным**, доступен лишь полный tethered-режим[^15^][^16^]. Проект usbliter8-fun носит характер разрушающего исследовательского эксперимента, а не готового продукта.

### Утверждение 3: Первая уязвимость BootROM для процессоров новее A11 со времен checkm8 (2019 год)

**Вердикт: Подтверждено, но с обязательной оговоркой «первая публично раскрытая» (Достоверность: Высокая)**

- Elcomsoft (2026-07-15): *"It has been almost 7 years since the last major BootROM exploit called checkm8 was released, which exploits Apple chips up to A11… More recently, just last month, a new BootROM exploit called usbliter8 was published."*[^10^]
- Профильные СМИ (iRemove, Feedsta, pasqualepillitteri, xakep и др.) сходятся во мнении, что это первая публичная уязвимость BootROM для кремния поколения после A11 со времен checkm8[^4^][^7^][^17^].
- Важная оговорка: В судебном иске Magnet Forensics заявляет, что обладала закрытой возможностью эксплуатации A12/A13 SecureROM (под кодовым именем «MSG») еще в апреле–мае 2024 года и внедряла ее в коммерческие продукты форензики. Поэтому корректнее формулировать: «первая **публично раскрытая**»[^18^][^19^].

### Утверждение 4: iPhone 12 Pro Max (чип A14) и iPad mini 6 (чип A15) не входят в зону уязвимости

**Вердикт: Подтверждено (Достоверность: Высокая)**

- Первоначальное исследование и технический анализ единодушны: **A11 не уязвим** (драйвер USB вручную очищает адрес DMA перед каждой передачей); **начиная с A14 и новее блок DART корректно настроен в SecureROM**, отсекая данный вектор[^4^][^7^][^17^]. Соответственно, iPhone 12 Pro Max (A14) и iPad mini 6 (A15) защищены на аппаратном уровне.
- Слух: В китайском сообществе в сентябре распространялись слухи о том, что «ранние ревизии A14 и M1 также уязвимы». Заявление **не подтверждено**, противоречит техническим спецификациям и классифицировано как неподтвержденный слух[^20^].

---

## 2. Специальная проверка: Появился ли инструмент уровня «checkra1n для checkm8»? Эволюция сообщества

**Вывод: Инструмента уровня checkra1n нет; однако существуют открытые исследовательские цепочки и интеграции в криминалистический софт.**

Хронология открытых событий:
- **2026-06-18**: Релиз write-up и PoC от Paradigm Shift (280+ звезд на GitHub за несколько часов)[^1^].
- **2026-07-03**: Инструкция по запуску SSH ramdisk на iPhone XR ("PWND: usbliter8")[^13^].
- **2026-07-07**: Компания Magnet Forensics подает иск в суд Джорджии против бывшего инженера Del Gaudio и Paradigm Shift (дело 1:26-cv-03781), обвиняя их в краже коммерческой тайны «MSG»[^18^][^19^].
- **2026-07-15**: Elcomsoft публикует исследование патчей сигнатур A12 BootROM и форк ipwndfu[^10^].
- **2026-07-21/23**: Судья Victoria Calvert выносит предварительный судебный запрет; Paradigm Shift удаляет пост и PoC; в сообществе расходятся зеркала[^1^][^3^][^19^].
- **2026-07-25/27**: Релиз **usbliter8-fun** — прошивка кастомного образа iOS 27.0 beta 2 на iPhone 11 Pro + привязанный джейлбрейк + Sileo[^11^][^12^].
- **2026-08-20**: Серийный выпуск плат RP2354A DFU по цене $10 в Китае[^14^].
- **2026-09-17**: В сообществе usbliter8 используется как инструмент отката без SHSH (через ramdisk Spironolactone), после чего ставится Dopamine/surrealra1n; **на релизной iOS 27 готовых инструментов нет**[^20^].

Ключевые отличия от checkra1n: требуется внешнее «железо» при каждом старте (строгий tethered-режим); защита SEP/BPR в iOS 17+ исключает semi-tethered вариант; существующий эксплойт жестко привязан к одной модели (iPhone 11 Pro) и стирает пользовательские разделы[^11^][^15^].

---

## 3. Специальная проверка: Связь usbliter8 и джейлбрейка iOS 27

- **Можно ли с помощью usbliter8 сделать джейлбрейк iOS 27?** Да, но с жесткими ограничениями: в июле проект usbliter8-fun загрузил джейлбрейк на тестовой сборке **iOS 27.0 beta 2 (build 24A5370h)** на iPhone 11 Pro (старейшее совместимое устройство в списке iOS 27)[^12^][^21^]. Кастомная прошивка патчит ядро, обходит USB Restricted Mode, песочницу /var/jb, кэш AMFI и глушит демоны coreauthd/ctkd для игнорирования паник SEP[^11^].
- **Почему только 27.0 beta 2?** Смещения в ядре и DeviceTree жестко захардкожены под конкретную сборку (build-specific). Под релизные версии 27.0 / 27.0.1 готовых цепочек нет[^11^][^12^].
- **Побочные эффекты**: Прошивка кастомного образа стирает устройство и полностью ломает **функции SEP, код-пароль, Wi-Fi, модемную связь, часть Bluetooth и сервисы Apple** (подтверждено GBHackers)[^21^].
- **Общий контекст iOS 27**: Октябрьская демонстрация Calif джейлбрейка iOS 27.0.1 на iPhone 18 Pro **никак не связана** с usbliter8 (там используется неизвестная программная уязвимость без физического вмешательства)[^22^].

---

## 4. Важный фоновый контекст: Удаление первоисточника по решению суда

Компания Magnet Forensics (разработчик комплекса GrayKey) заявила, что эксплойт usbliter8 был создан с использованием ее коммерческой тайны «MSG», к которой бывший сотрудник Del Gaudio имел доступ. 21 июля 2026 года федеральный судья удовлетворил обеспечительные меры, обязав удалить публикации и репозитории[^3^][^18^][^19^]. Теперь доступ к оригинальным материалам возможен только через архивы web.archive.org и форки сообщества.

---

## 5. Итоговая сводка

| № | Утверждение | Вердикт | Достоверность |
|---|-------------|---------|---------------|
| 1 | Аппаратный баг BootROM в A12/A13, не устранимый программно | Подтверждено (затрагивает также S4/S5; A12X/Z уязвимы в теории, но не поддержаны) | Высокая |
| 2 | Физический PoC; нет публичных инструментов | Частично подтверждено (физический PoC верен; «нет инструментов» устарело — есть исследовательские цепочки вроде usbliter8-fun, но нет стабильных утилит уровня checkra1n) | Высокая |
| 3 | Первый BootROM эксплойт для post-A11 чипов со времен checkm8 | Подтверждено (с оговоркой «первый публично раскрытый») | Высокая |
| 4 | A14 (iPhone 12 Pro Max) и A15 (iPad mini 6) не затронуты | Подтверждено (слухи об уязвимости A14/M1 отклонены как недостоверные) | Высокая |

---

## Источники информации

[^1^]: ONE Jailbreak, "usbliter8 Exploit Removed After Court Order in Magnet Suit", 2026-07-23. https://onejailbreak.com/blog/usbliter8-exploit-removed-after-court-order-in-magnet-suit/
[^2^]: The Apple Wiki, "usbliter8 Exploit", обновлено 2026-09-30. https://theapplewiki.com/wiki/Usbliter8_Exploit
[^3^]: CourtListener, Magnet Forensics, LLC v. Del Gaudio, 1:26-cv-03781 (N.D. Ga.), судебный приказ от 2026-07-21. https://www.courtlistener.com/docket/73584326/magnet-forensics-llc-v-del-gaudio/
[^4^]: Pasquale Pillitteri, "usbliter8: Unpatchable BootROM Flaw Hits iPhone XS, XR and 11", 2026-09-06. https://pasqualepillitteri.it/en/news/6725/usbliter8-unpatchable-bootrom-iphone-xs-xr-11
[^5^]: hackyboiz, "usbliter8: Apple A12/A13, S4/S5 SoC BootROM 취약점", 2026-06-27. https://hackyboiz.github.io/2026/06/27/ji9umi/usbliter8/
[^6^]: Mezha, "Paradigm Shift disclosed usbliter8 exploit that could jailbreak iPhones", 2026-06-22. https://mezha.net/eng/news/1d2041c4_paradigm_shift_disclosed/
[^7^]: iRemove Tools, "USBLiter8 BootROM Exploit Explained", 2026-07-04. https://iremove.tools/blog/usbliter8-bootrom-exploit-guide
[^8^]: TechCrunch / перевод, "Неустранимая уязвимость в чипах Apple", 2026-07-20. https://m.zhiding.cn/article/3193526.htm
[^9^]: Feedsta, "Researchers Uncover Unpatchable BootROM Exploit Targeting Apple's A12 and A13 Chips", 2026-07-19. https://feedsta.ai/blog/apple-a12-a13-bootrom-exploit-usbliter8/
[^10^]: Elcomsoft Blog, "A12 usbliter8 BootROM sigpatches", 2026-07-15. https://blog.elcomsoft.com/2026/07/a12-usbliter8-bootrom-sigpatches/
[^11^]: ONE Jailbreak, "usbliter8-fun: iOS 27 Jailbreak on iPhone 11 Pro", 2026-07-25. https://onejailbreak.com/blog/usbliter8-fun-ios-27-jailbreak-on-iphone-11-pro/
[^12^]: GitHub - 34306/usbliter8-fun, "iOS 27 jailbreak with usbliter8 exploit", 2026-07-08. https://github.com/34306/usbliter8-fun
[^13^]: usbliter8.info, "How to Boot iPhone XR SSH Ramdisk Using USBLiter8 BootROM Exploit", 2026-07-03. https://www.usbliter8.info/how-to-boot-iphone-xr-ssh-ramdisk-by-using-usbliter8-bootrom-exploit/
[^14^]: CNX Software, "Why are people suddenly adding Apple Lightning cables to Raspberry Pi Pico 2 boards?", 2026-08-20. https://www.cnx-software.com/2026/08/20/why-are-people-suddenly-adding-apple-lightning-cables-to-raspberry-pi-pico-2-boards/
[^15^]: usbliter8.info, "Can usbliter8 be used for Untethered A12 and A13 jailbreak?", 2026-07-03. https://www.usbliter8.info/can-usbliter8-be-used-for-untethered-a12-and-a13-jailbreak/
[^16^]: r/jailbreak (Telegram mirror), "usbliter8: what you need to know — The iOS 17 problem", 2026-06-19. https://t.me/s/r_jailbreak?before=56488
[^17^]: xakep.ru, «Неисправимая» уязвимость в Apple A12 и A13, 2026-06-30. https://xakep.ru/2026/06/30/meganews-327/
[^18^]: AppleInsider, "iPhone exploit fight highlights who owns security research", 2026-07-24. https://appleinsider.com/articles/26/07/24/iphone-exploit-legal-fight-is-really-about-who-owns-security-research
[^19^]: Cult of Mac / Yahoo Tech, "usbliter8 lawsuit forces 'unpatchable' iPhone hack offline", 2026-07-27. https://tech.yahoo.com/cybersecurity/articles/usbliter8-lawsuit-forces-unpatchable-iphone-140002992.html
[^20^]: Аналитический обзор, "iOS 27 и статус чипов", 2026-09-17. https://post.smzdm.com/p/a70nrpn9/
[^21^]: GBHackers, "New usbliter8 SecureROM Exploit Enables iOS 27 Jailbreak on iPhone 11 Pro", 2026-07-27. https://gbhackers.com/usbliter8-securerom-exploit-ios-27-jailbreak-on-iphone-11-pro/
[^22^]: GBHackers, "Researchers Demonstrate iOS 27.0.1 Untethered Jailbreak on iPhone 18 Pro", 2026-10-17. https://gbhackers.com/ios-27-0-1-untethered-jailbreak/
