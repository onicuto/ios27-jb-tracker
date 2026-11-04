# Отчет о фактчекинге (Измерение 03): Является ли джейлбрейк Calif iOS 27.0.1 «первым перезагружаемым (untethered) со времен iOS 9»

[Русский](ios_jb_audit_dim03.md) | [中文版](ios_jb_audit_dim03-zh.md)

- **Дата проверки**: 2026-10-17
- **Метод проверки**: 17 независимых веб-поисков + постраничный сбор первоисточников
- **Проверяемое утверждение**: В отчете утверждается, что продемонстрированный 2026-10-16 компанией Calif на Hexacon джейлбрейк iOS 27.0.1 является «первым перезагружаемым (untethered) джейлбрейком со времен iOS 9».

---

## 1. Главный вердикт

**Вердикт: Опровергнуто (при буквальном прочтении) / Частично подтверждено (при расширительном толковании). Достоверность: Высокая (~90%).**

- Буквальная формулировка утверждения (заимствованная из формулировки heise "first reboot-proof jailbreak since iOS 9") **несостоятельна**: проект **Fugu14** (автор Linus Henze, публичный открытый исходный код от 2021-10-24, iOS 14.3–14.5.1, arm64e включая iPhone 12) был общедоступным непривязанным (untethered) джейлбрейком, сохраняющимся после перезагрузки. Сам Linus Henze и организаторы конференции POC официально охарактеризовали его как «первый общедоступный untethered-джейлбрейк со времен iOS 9»[^14^][^15^]. Таким образом, сценическое демо iOS 27.0.1 может претендовать максимум на статус «первого untethered-джейлбрейка **со времен Fugu14 (2021 год, iOS 14)** (притом оставаясь лишь демонстрацией без выпуска инструмента)».
- При предельно мягкой трактовке («untethered-демонстрация на актуальном флагманском оборудовании и свежайшей релизной прошивке») утверждение близко к правде, однако это расходится с формулировкой в исходном отчете.
- Пересказ в отчете **точно следовал словам heise** (GBHackers прямо сослались: "Heise reports..."). Проблема в том, что первоначальное суждение самого издания heise было ошибочным и нестрогим, а отчет скопировал его без перекрестной проверки.

---

## 2. Проверка самого события (2026-10-16, Hexacon, Париж)

Материалы независимых СМИ полностью согласуются, базовые факты подтверждены:

1. **Факт демонстрации**: 2026-10-16 компания Calif (Calif.io) на конференции Hexacon 2026 в Париже (конференция по offensive security, организованная Synacktiv, 16–17 октября) на сцене показала untethered-джейлбрейк iPhone 18 Pro (iPhone19,2 / чип T8160) на iOS 27.0.1 (сборка 24A446): после перезагрузки окружение джейлбрейка автоматически восстановилось, вход по SSH (порт 2222) выполнен от root (uid=0), neofetch показал 67 пакетов dpkg и аптайм около 2 минут[^1^][^2^].
2. **Личности докладчиков**: Открывающий доклад вели Bruce Dang и Thai Duong (XorNinja); Billy Ellis опубликовал видеозапись из зала в X[^3^][^4^].
3. **Отсутствие публичного инструмента**: Уязвимости не раскрыты, номеров CVE нет, инструмент не опубликован; представитель Calif заявил, что материалы "will be released in due time"[^2^][^3^].
4. **Роль ИИ**: heise написали, что ИИ помог выстроить цепочку уязвимостей; в бюллетене безопасности iOS 27 от 14 сентября Apple благодарила "Calif.io in collaboration with Claude and Anthropic Research" (за два баба падения, не связанных с данным джейлбрейком)[^3^][^5^].

**Итог**: Само событие абсолютно достоверно; спор касается исключительно исторического позиционирования («первый в своем роде»).

---

## 3. Сравнение исходных формулировок в СМИ

### 3.1 heise (первоисточник)

- Заголовок на немецком: «Dank KI: Rebootfester Jailbreak für iOS 27.0.1 bis zum iPhone 18 Pro, untethered» (2026-10-16)[^6^]
- Лид немецкой версии:
  > "Das Team Calif.io hat den ersten rebootfesten Jailbreak seit iOS 9 entwickelt. Er läuft bis zur jüngsten Version und auch auf den neuesten iPhones. KI half."[^7^]
- Лид английской версии:
  > "The Calif.io team has developed the first reboot-proof jailbreak since iOS 9. It works on the latest version and the newest iPhones."[^8^]

### 3.2 GBHackers (цитата по heise, 2026-10-17)

> "Heise reports it is the first reboot-proof jailbreak since iOS 9, and that AI helped find the exploit chain."[^9^]

Редакция GBHackers поступила грамотно, прямо атрибутировав заявление источнику ("Heise reports"), возложив ответственность за формулировку на heise.

### 3.3 Decrypt (2026-10-16/17)

> "Security firm Calif.io demonstrated an untethered jailbreak on an iPhone 18 Pro running iOS 27.0.1 on stage at Hexacon, the offensive security conference in Paris, on Friday. It's the first time an untethered, permanent jailbreak is successful in such devices."[^3^]

### 3.4 Сравнительный анализ точности

| Критерий | heise / пересказ GBHackers | Decrypt |
|---|---|---|
| Сила утверждения | Категоричное: «первый со времен iOS 9» | Мягкое: «впервые успешен на подобных устройствах» |
| Фальсифицируемость | Высокая (опровергается единичным контрпримером) | Низкая (размытое "such devices" можно списать на «новейшее поколение iPhone») |
| Точность | **Опровергнуто прямым контрпримером (Fugu14)** | Размыто, но труднее уличить в ошибке; хотя Fugu14 в свое время работал на тогдашнем флагмане iPhone 12 |

**Вывод**: Формулировка heise звучит конкретно и профессионально, но **фактически ошибочна**. Формулировка Decrypt более размыта, но не содержит грубой фактологической ошибки. Исходный отчет безоговорочно скопировал ошибочную формулировку heise без перекрестной проверки. Корректная формулировка должна звучать так: «heise охарактеризовала его как первый reboot-proof джейлбрейк со времен iOS 9; однако следует помнить, что Fugu14 (iOS 14.3–14.5.1), опубликованный в 2021 году, являлся полноценным untethered-джейлбрейком, поэтому утверждение применимо только с оговоркой 'на новейшем оборудовании и актуальной прошивке'».

---

## 4. История публичных джейлбрейков после iOS 9 и классификация типов

Общепринятая классификация типов джейлбрейка в сообществе[^16^]:

- **untethered (непривязанный)**: состояние джейлбрейка сохраняется после перезагрузки полностью автоматически;
- **semi-untethered (полуотвязанный)**: после перезагрузки джейлбрейк слетает, но заново активируется через приложение на устройстве без подключения к ПК;
- **semi-tethered (полупривязанный)**: устройство загружается в штатную систему, но для возврата джейлбрейка требуется подключение к ПК и перезапуск утилиты;
- **tethered (привязанный)**: при любой перезагрузке запуск возможен только с помощью ПК.

| Утилита | Дата релиза | Поддерживаемые версии / чипы | Тип |
|---|---|---|---|
| Pangu 9.0–9.0.2 | 2015-10 | Все устройства на iOS 9.0–9.0.2 | **untethered**[^10^] |
| Pangu 9.1 | 2016-03 | iOS 9.1 (64-бит) | **untethered**[^11^] |
| Pangu 9.2–9.3.3 | 2016-07-24 | iOS 9.2–9.3.3 (64-бит) | semi-untethered[^11^][^12^] |
| Phoenix 9.3.5/9.3.6 | 2017 | 32-бит iOS 9.3.5/9.3.6 | semi-untethered[^12^] |
| p0laris | 2022-04-20 | 32-бит iOS 9.3.5/9.3.6 | semi-untethered (untether был заброшен)[^13^] |
| Yalu / yalu+mach_portal / yalu102 | 2016-12 ~ 2017-01 | iOS 10.0–10.2 | semi-untethered[^12^][^17^] |
| extra_recipe+yaluX | 2017-05 | iOS 10.0–10.1.1 (iPhone 7/7+) | semi-untethered[^17^] |
| doubleH3lix / Meridian / g0blin / Saïgon / h3lix | 2017-2018 | iOS 10.x | semi-untethered (h3lix для 32-бит)[^12^] |
| Electra | 2018 | iOS 11.0–11.4.1 | semi-untethered[^16^] |
| unc0ver (ранний) | 2018-2019 | iOS 11–12.1.2 | semi-untethered[^16^] |
| Chimera | 2019-04-30 | iOS 12.0–12.5.x (A7–A12) | semi-untethered[^18^] |
| **checkra1n (checkm8)** | 2019-11 | A5–A11, iOS 12–14.8.1 | **semi-tethered**[^19^][^20^] |
| unc0ver 5.x (iOS 13) / 6.x–8.x (iOS 14) | 2020-2021 | iOS 13.0–13.5 / 14.0–14.8 | semi-untethered[^16^] |
| Odyssey | 2020 | iOS 13.0–13.7 | semi-untethered[^16^] |
| Taurine | 2021-04-01 | iOS 14.0–14.3 | semi-untethered[^21^] |
| **Fugu14 (+ интеграция в unc0ver v7)** | **2021-10-24** | **iOS 14.3–14.5.1, arm64e (A12–A14)** | **untethered (для разработчиков, компиляция через Mac+Xcode)**[^14^][^15^][^22^] |
| palera1n (checkm8) | 2022-10 | A8–A11, iOS 15–16.x (и iPadOS 17/18) | semi-tethered[^16^][^20^] |
| Fugu15 | 2022-10-31 | iOS 15.0–15.4.1 (arm64e) | **semi-untethered** (perma-signed через CoreTrust, не untethered)[^23^][^24^] |
| XinaA15 | 2022-12-07 | iOS 15.0–15.4.1 (A12–A15/M1) | semi-untethered[^25^] |
| Dopamine (экс-Fugu15 Max) 1.x/2.x | 2023–2025 | iOS 15.0–16.6.1 (A8–A16, M1–M2) | semi-untethered[^16^][^26^] |
| meowbrek2 | 2024-01 | iOS 15.0–15.8.6 (A8–A11) | semi-untethered[^27^] |
| Dopamine 2.5 Beta (DarkSword) | 2026-05 | Расширение на iOS 16.7–16.7.16, iOS 17–18.7.1 (A9–A11) | semi-untethered (экспериментальный)[^28^] |
| **Демо Calif iOS 27.0.1** | 2026-10-16 | iPhone 18 Pro, iOS 27.0.1 | **untethered (только демонстрация, инструмента нет)**[^1^][^3^] |

**Вывод из таблицы**: После июля 2016 года (Pangu 9.2–9.3.3) практически все публичные джейлбрейки относились к semi-untethered или semi-tethered. **Единственным исключением стал открытый Fugu14 от 2021-10-24 (полноценный untethered)**.

---

## 5. Ключевой контрпример: Fugu14 как опровержение тезиса

1. **Fugu14 был открытым публичным untethered-джейлбрейком**: The Apple Wiki прямо пишет: "Fugu14 is an incomplete untethered jailbreak for iOS 14.3 to 14.5.1. It released on 24 October 2021."[^14^]
2. **Официальное признание автором и организаторами конференции** (биография докладчика POC 2022):
   > "...as well as the developer of Fugu (iOS 13 checkm8 based jailbreak), **Fugu14 (iOS 14 untethered jailbreak - the first publicly available untethered jailbreak since iOS 9)** and Fugu15 (iOS 15 permasigned jailbreak)..."[^15^]
   То есть именно Fugu14 официально признан «первым общедоступным untethered-джейлбрейком со времен iOS 9».
3. **Практическая доступность**: unc0ver v7.0.0 (2021-10-24) интегрировал Fugu14, обеспечив устройствам A12–A14 (включая iPhone 12) на iOS 14.4–14.5.1 сохранение джейлбрейка после перезагрузки; утилита AltStore v1.4.8 поддерживала установку в один клик[^22^][^29^]. Немецкая Википедия отмечает: "Fugu14, der bis dato letzte untethered Jailbreak für iOS-Geräte" (Fugu14 на тот момент — последний untethered-джейлбрейк)[^30^].
4. **Попытка защиты позиции heise и ее пределы**: Fugu14 назывался "incomplete" (неполным: требовал компиляции, не имел встроенного внедрения твиков). Если heise имело в виду «первый законченный пользовательский untethered», это ближе к правде — но на словах этого сказано не было. К тому же Calif показала лишь сценическое демо без исходников, и по критерию доступности Fugu14 был неизмеримо более открытым.

**Итоговые тезисы**:
- Утверждение «со времен iOS 9 не было публичных untethered-джейлбрейков» — **неверно** (Fugu14 — задокументированное исключение);
- Утверждение «после 2021 года (Fugu14) до настоящего времени не было untethered-джейлбрейков» — **верно**.

---

## 6. Почему джейлбрейки семейства checkm8 (checkra1n / palera1n) не являются untethered

- checkm8 — аппаратная уязвимость в BootROM процессоров A5–A11, которую Apple не может устранить патчем. Однако она **эксплуатируется исключительно в момент старта устройства в режиме DFU**; после обычной перезагрузки устройство возвращается в заводское немодифицированное состояние[^20^].
- По этой причине checkra1n и palera1n классифицируются как **semi-tethered**: телефон может штатно загружаться, но для повторной активации джейлбрейка его необходимо подключить к компьютеру, перевести в DFU и запустить утилиту заново[^19^][^20^].
- Термин «неустранимый (unpatchable)» описывает **невозможность пропатчить "железо"**, а не сохранение состояния джейлбрейка после перезагрузки. Эти понятия часто путают.

---

## 7. Резюме по задачам проверки

1. **Хронология джейлбрейков**: отражена в таблице раздела 4; ключевой факт: с июля 2016 по октябрь 2021 года все инструменты были полупривязанными; Fugu14 в октябре 2021 стал публичным исключением; после него до октября 2026 года публичных untethered-инструментов не появлялось.
2. **Точность тезиса**: Буквально опровергнуто существованием Fugu14. Кроме того, важно отличать открытый релиз от закрытого демо: у Calif это закрытый показ.
3. **Формулировки СМИ**: heise высказалась конкретно, но допустила фактическую ошибку; Decrypt высказалась осторожнее. Отчет скопировал ошибку heise без проверки.
4. **checkm8**: не является untethered, поскольку эксплойт BootROM работает только в DFU при старте и слетает при перезагрузке (semi-tethered).

---

## Источники информации

[^1^]: Cyber Security News, "iOS 27.0.1 Untethered Jailbreak Demonstrated on iPhone 18 Pro", 2026-10-16. https://cybersecuritynews.com/ios-27-0-1-jailbreak-demonstrated/
[^2^]: CyberPress, "iOS 27.0.1 Jailbreak Survives Reboot and Restores Root Access on iPhone 18 Pro", 2026-10-16. https://cyberpress.org/ios-27-0-1-jailbreak-survives-reboot/
[^3^]: Decrypt, "Hackers Jailbreak iPhone 18 Pro on Stage, and It Survives a Reboot", 2026-10-16/17. https://decrypt.co/381177/hackers-jailbreak-iphone-18-pro-survives-reboot
[^4^]: Твит Billy Ellis (@bellis1000) в X, 2026-10-16. https://x.com/bellis1000/status/2111028042495824337
[^5^]: explainX, "Calif.io Jailbreaks iOS 27.0.1 on iPhone 18 Pro: What Is Claimed vs. Verified", 2026-10-16. https://explainx.ai/blog/calif-io-ios-27-0-1-untethered-jailbreak-iphone-18-pro-hexacon-ai-claimed-vs-verified-2026
[^6^]: heise online, "Dank KI: Rebootfester Jailbreak für iOS 27.0.1 bis zum iPhone 18 Pro, untethered", 2026-10-16. https://www.heise.de/news/
[^7^]: aimbit.de (зеркало heise с цитатой лида), 2026-10-16. https://aimbit.de/news
[^8^]: heise online (English), "AI helps create untethered jailbreak for iOS 27.0.1", 2026-10-16. https://www.heise.de/en/news/Works-on-iPhone-18-Pro-AI-helps-create-untethered-jailbreak-for-iOS-27-0-1-11490907.html
[^9^]: GBHackers, "Researchers Demonstrate iOS 27.0.1 Untethered Jailbreak on iPhone 18 Pro", 2026-10-17. https://gbhackers.com/ios-27-0-1-untethered-jailbreak/
[^10^]: TechCrunch, "Apple's iOS 9.1 Shuts Down The Pangu Hacking Team's Jailbreak", 2015-10-21. https://techcrunch.com/2015/10/21/apples-ios-9-1-shuts-down-the-pangu-hacking-teams-jailbreak/
[^11^]: The Apple Wiki, "Pangu9". https://theapplewiki.com/wiki/Pangu9
[^12^]: iDownloadBlog, "Properly rebooting your iOS 9.2-10.2 device after jailbreaking with Pangu or Yalu", 2016-07-24. https://www.idownloadblog.com/2016/07/24/properly-rebooting-your-ios-9-3-3-device-after-jailbreaking-with-pangu/
[^13^]: iDownloadBlog, "New p0laris jailbreak for legacy iOS 9.x firmware released", 2022-04-20; The Apple Wiki, "P0laris". https://www.idownloadblog.com/2022/04/20/p0laris-ios-9-jailbreak/ ; https://theapplewiki.com/wiki/P0laris
[^14^]: The Apple Wiki, "Fugu14". https://theapplewiki.com/wiki/Fugu14
[^15^]: Страница докладчиков POC 2022 (биография Linus Henze). https://powerofcommunity.net/2022/
[^16^]: iOSJailbreak.pro, "Untethered Jailbreak Explained: Does One Exist in 2026?", 2026-06-13; iClarified Jailbreak History. https://iosjailbreak.pro/untethered-jailbreak-explained-2026.html ; https://www.iclarified.com/jailbreak
[^17^]: The Apple Wiki, "Yalu". https://theapplewiki.com/wiki/Yalu
[^18^]: The Apple Wiki, "Chimera". https://theapplewiki.com/wiki/Chimera
[^19^]: TechAcrobat, "checkra1n Linux Guide", 2026-10-04. https://www.techacrobat.com/checkra1n-linux-jailbreak/
[^20^]: TechAcrobat, "Checkm8 BootROM Exploit", 2026-09-29. https://www.techacrobat.com/checkm8-jailbreak-exploit/
[^21^]: IPAOMTK, "Taurine Jailbreak iOS 14". https://ipaomtk.com/taurine-jailbreak/
[^22^]: iOSHacker, "Fugu14 Untethered Jailbreak Released, unc0ver Updated With Preliminary Support", 2021-10-25; iphonetweak.fr, "Unc0ver 7.0 : le jailbreak iOS 14.5.1 est désormais untethered avec fugu14", 2021-10-25. https://ioshacker.com/news/fugu14-untethered-jailbreak-released-unc0ver-updated-with-preliminary-support
[^23^]: The Apple Wiki, "Fugu15". https://theapplewiki.com/wiki/Fugu15
[^24^]: iDownloadBlog, "Linus Henze releases Fugu15 jailbreak for iOS 15", 2022-10-31. https://www.idownloadblog.com/2022/10/31/linus-henze-releases-fugu15-jailbreak-ios-15/
[^25^]: The Apple Wiki, "XinaA15". https://theapplewiki.com/wiki/XinaA15
[^26^]: The Apple Wiki, "Open Source Jailbreaking Tools". https://theapplewiki.com/wiki/Open_Source_Jailbreaking_Tools
[^27^]: The Apple Wiki, "Meowbrek2". https://theapplewiki.com/wiki/Meowbrek2
[^28^]: UltFone, "Jailbreak iOS 27 Beta: Best Tools", 2026-06-04. https://www.ultfone.com/ios-27/jailbreak-ios-27.html
[^29^]: iDownloadBlog, "Linus Henze updates Fugu14 untether for reliability", 2021-10-28. https://www.idownloadblog.com/tag/ios-14-5-1/
[^30^]: Немецкая Википедия, "Jailbreak (iOS)". https://de.wikipedia.org/wiki/Jailbreak_(iOS)
