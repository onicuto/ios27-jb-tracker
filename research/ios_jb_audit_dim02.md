# Отчет о фактчекинге: Демонстрация Calif джейлбрейка iOS 27.0.1 на Hexacon 2026 (iPhone 18 Pro)

[Русский](ios_jb_audit_dim02.md) | [中文版](ios_jb_audit_dim02-zh.md)

- Дата проверки: 2026-10-17
- Метод проверки: Поиск в англоязычных источниках (19 независимых запросов); приоритет отдан первоисточникам (heise online, Decrypt, CyberSecurityNews, Cyberpress, посты Billy Ellis / calif_io в X, ONE Jailbreak) с перекрестной сверкой по техническим базам данных (EveryMac, AppleDB, The Apple Wiki, обзоры Geekbench, реальные логи паники ядра от пользователей).
- Предыстория: 2026-10-16 компания Calif.io на сцене конференции Hexacon 2026 в Париже (организована Synacktiv, 16–17 октября) продемонстрировала непривязанный (untethered) джейлбрейк iPhone 18 Pro на iOS 27.0.1. Событие освещено независимыми изданиями heise, Decrypt, CyberSecurityNews, Cyberpress, ONE Jailbreak и подтверждено видеозаписью зрителя в зале (Billy Ellis). **Факт проведения демонстрации не вызывает сомнений**; ниже приведена проверка конкретных технических утверждений.

---

## Попунктный вердикт

### Утверждение 1: Модель в демонстрации — iPhone 18 Pro, внутренний идентификатор iPhone19,2, чип T8160, сборка iOS 27.0.1 build 24A446, Darwin Kernel 27.0.0 / XNU 13432.2.10

**Вердикт: Подтверждено (Достоверность: Высокая)**

- Покадровая фиксация экрана демонстрации CyberSecurityNews (первичный технический источник):
  > "The uname output showed Darwin Kernel 27.0.0 built on XNU 13432.2.10 for the T8160 chip, with the model listed as iPhone19,2. The sw_vers command confirmed iOS 27.0.1, build 24A446" [^1^] (2026-10-16)
- Cyberpress независимо подтверждает ту же комбинацию параметров:
  > "The `uname` output identified Darwin Kernel 27.0.0, built on XNU 13432.2.10 for the T8160 chip, alongside the device identifier iPhone19,2. The `sw_vers` command reported iOS 27.0.1, build 24A446." [^2^] (2026-10-16)
- Косвенные подтверждения (полное соответствие номенклатуре Apple и реальным данным):
  - **iPhone19,2 = iPhone 18 Pro**: В спецификациях EveryMac четко указано "Identifiers: iPhone 18 Pro - ... iPhone19,2" [^3^]; в AppleDB аналогично [^4^]; в бенчмарках Geekbench iPhone 18 Pro также фигурирует как iPhone19,2 [^5^].
  - **T8160 = CPID чипа A20 Pro**: CPID процессоров серии A19/A19 Pro — T8150 [^6^]; в базах чипов A20 Pro обозначен как "A20 Pro (Borneo, T8160)" [^7^], таблица кодовых имен The Apple Wiki относит T8160 к поколению A20 (Banda/Borneo) [^8^]. Полное соответствие логике нумерации чипов Apple T-серии.
  - **build 24A446 = iOS 27.0.1**: В таблице версий iOS 27 в Википедии: "Latest version: 27.0.1 | 24A446 | September 28, 2026" [^9^]; фид релизов Apple подтверждает 27.0.1 как сборку 24A446 [^10^].
  - **XNU 13432.2.10 — подлинное ядро iOS 27.0.1**: Независимый лог паники пользователя iPhone 15 (iPhone15,4) показывает `"os_version":"iPhone OS 27.0.1 (24A446)"` и ядро `Darwin Kernel Version 27.0.0: Thu Aug 13 21:41:29 PDT 2026; root:xnu-13432.2.10~2/RELEASE_ARM64_T8120` [^11^]; лог пользователя iPhone 13 Pro (T8110) также указывает xnu-13432.2.10 [^12^]. База The Apple Wiki подтверждает, что ветка iOS 27.0 работает на Darwin 27.0.0 и xnu-13432.x [^13^]. Версия ядра в uname на демо совпадает с реальной прошивкой до единого символа — это мощнейшее доказательство подлинности (фальсификаторы практически никогда не попадают в реальные номера сборок ядра).
  - Примечание: В iOS 27 мажорный номер Darwin выровнен с версией iOS (Darwin 27.0.0), что подтверждено The Apple Wiki и отражает внутреннюю нумерацию Apple [^13^].

### Утверждение 2: Сценарий демонстрации: Перезагрузка → Логотип Apple → Экран блокировки → Обычный ввод пароля → SSH на порту 2222 от имени root (uid=0) → neofetch показывает 67 пакетов dpkg и аптайм около 2 минут

**Вердикт: Подтверждено (Достоверность: Высокая)**

- CyberSecurityNews:
  > "It booted to the Apple logo, reached the lock screen, and was unlocked with the passcode. ... the team connected to the phone over SSH on port 2222 and logged in as root. The id command returned uid=0 ... neofetch listed 67 packages installed through dpkg with an uptime of only two minutes." [^1^]
- Cyberpress дословно подтверждает:
  > "they subsequently connected to the device through SSH on port 2222 and authenticated as root. Running the `id` command returned `uid=0` ... `neofetch` displayed 67 packages installed through `dpkg` and an uptime of approximately two minutes, consistent with the recent reboot." [^2^]
- Описание видеозаписи Billy Ellis в материале Decrypt подтверждает цепочку «перезагрузка — разблокировка паролем — root SSH»:
  > "Video from the stage, posted by jailbreak researcher Billy Ellis, shows the team rebooting the phone, unlocking it with the regular passcode and opening an SSH session as root ... The terminal output listed iOS 27.0.1 and an uptime of about two minutes." [^14^] (2026-10-16)
- Первичный твит Billy Ellis (@bellis1000):
  > "At #hexacon - Calif.io demos iOS 27.0.1 untethered jailbreak on iPhone 18 Pro" [^15^]
- Примечание: Использование порта 2222 является стандартом джейлбрейк-сообщества (утилита iproxy перенаправляет порт 2222 на SSH-порт устройства).

### Утверждение 3: «Две минуты» — это время работы после перезагрузки (uptime), а не время срабатывания эксплойта (ошибочно интерпретированное в соцсетях)

**Вердикт: Подтверждено (Достоверность: Высокая)**

- Пример искажения (первоисточник ошибки): Пост International Cyber Digest в сети X:
  > "Its Hexacon demo shows the phone on iOS 27.0.1, Apple's latest, giving up a root shell within 2 minutes of boot." [^16^] (2026-10-16)
- ONE Jailbreak также повторил эту формулировку: "Reports from people in the room said the phone gave up a root shell roughly two minutes after boot." [^17^]
- Разъяснение: pasqualepillitteri прямо указал:
  > "The two minutes circulating in social media posts are the uptime neofetch reported at the moment of the session. They measure how long the phone had been on after the reboot, not how long the exploit takes to run, which remains unknown." [^16^]
- В оригинальных отчетах Decrypt и CyberSecurityNews везде сказано лишь "uptime of about/only two minutes", без каких-либо утверждений о скорости выполнения эксплойта [^1^][^14^]. GBHackers также отметили, что формулировка "root shell within two minutes of boot" — ошибка вторичного пересказа [^18^].

### Утверждение 4: Демонстрация проводилась на «разблокированном» смартфоне, не затрагивает обход экрана блокировки и не доказывает возможность взлома заблокированного iPhone посторонним

**Вердикт: Подтверждено (Достоверность: Высокая)**

- pasqualepillitteri:
  > "The demo also never touched the lock screen. The phone was unlocked with the passcode the way any owner would do it, so the video does not prove that a stranger holding a locked iPhone could get in." [^16^]
  И в блоке FAQ повторно: "In the Paris demo the passcode was entered normally, so the second point was not proven." [^16^]
- Cyberpress подчеркивает отсутствие удаленного вектора:
  > "Root access alone also does not reveal the initial exploitation vector. The presentation therefore should not be interpreted as evidence of a remotely deliverable or zero-click attack." [^2^]
- Все свидетельства очевидцев подтверждают стандартный ввод PIN-кода владельца после загрузки [^1^][^14^][^17^].

### Утверждение 5: Уязвимость не раскрыта, нет CVE, нет публичного инструмента; heise заявляет о совместимости «вплоть до iOS 27.0.1 + линейка iPhone 18 Pro»; работоспособность на старых процессорах неизвестна

**Вердикт: Подтверждено (Достоверность: Высокая)**

- Не раскрыто / нет инструмента: Cyberpress: "the researchers have not disclosed the underlying vulnerabilities or released a public jailbreak tool" [^2^]; GBHackers: "No CVEs have been assigned or confirmed." [^18^]; heise (цитата по explainx): "it's not yet clear which vulnerabilities Calif.io exploited" [^19^].
- Зона совместимости по heise:
  - pasqualepillitteri: "heise online writes that the jailbreak works up to and including iOS 27.0.1 and across the iPhone 18 Pro family." [^16^]
  - explainx: "heise describes the talk as the first jailbreak for iOS 27, working on versions up to iOS 27.0.1 including the iPhone 18 Pro family." [^19^]
  - Анонс немецкой редакции heise: "Das Team Calif.io hat den ersten rebootfesten Jailbreak seit iOS 9 entwickelt. Er läuft bis zur jüngsten Version und auch auf den neuesten iPhones. KI half." [^20^]
- Работа на старых чипах неизвестна: pasqualepillitteri FAQ: "Heise mentions compatibility with the iPhone 18 Pro family and with iOS up to 27.0.1, but nobody knows whether the chain also runs on earlier chips, since hardware defenses change from one generation to the next." [^16^]

### Утверждение 6: heise заявляет, что ИИ помог найти цепочку эксплойтов, но не раскрывает деталей; «сравнение beta-версий iOS 27.2 с 27.0.1» — исключительно догадка редакции heise

**Вердикт: Подтверждено (Достоверность: Высокая)**

- explainx прямо цитирует английскую версию heise:
  > "heise: AI 'once again helped find the exploit chain.' ... speculates that the team could have done the same here by comparing iOS 27.2 betas with iOS 27.0.1. It flags that Apple has published no documentation on this and that the search 'would presumably require a lot of tokens.' That is speculation, not a finding." [^19^]
- Фрагмент из статьи heise (зафиксирован поисковым индексом): "Apple has yet to publish any documentation on this, however, so the search would presumably require a lot of tokens." [^21^]
- pasqualepillitteri независимо повторяет: "Heise reports that artificial intelligence once again helped find the exploit chain, without explaining how. The outlet speculates that the team may have compared the iOS 27.2 betas with 27.0.1 ... That is a conjecture, not a confirmed fact." [^16^]
- Хронология подтверждает: iOS 27.2 на тот момент действительно находилась в стадии тестирования (beta 4 build 24B5110a от 2026-10-13), поэтому технически диффы между сборками были доступны [^9^][^23^].

### Утверждение 7: Apple не делала никаких заявлений; ONE Jailbreak пишет, что наработки будут выпущены «in due time» (со ссылкой на слова ведущих)

**Вердикт: Частично подтверждено (Достоверность: Высокая) — основная мысль верна, но оговорка о цитате требует уточнения**

- Молчание Apple: Подтверждено. Decrypt: "Apple has not publicly commented on the demo as of Friday, and says it does not confirm security issues until patches are available." [^14^]; pasqualepillitteri: "Apple, for its part, has issued no statement." [^16^]
- Источник фразы "in due time": В ONE Jailbreak это действительно пересказ: "Ellis later said the presenters mentioned that the work would be released in due time." [^17^]
- **Однако** это прямая цитата самого Calif: официальный аккаунт компании @calif_io в тот же день опубликовал пост с заголовком:
  > "Demos we presented at Hexacon in Paris today. Everything will be released in due time." [^24^] (2026-10-16)
  Издание Decrypt также цитирует рассылку Calif: "Its newsletter post from the conference lists four demos ... and says everything 'will be released in due time.'" [^14^]
- Корректировка: Фраза "in due time" действительно была передана ONE Jailbreak через вторые руки, но она слово в слово присутствует в официальных публикациях самой Calif.

---

## Дополнительные находки для контекста

1. heise называет это «первым перезагружаемым (rebootfest) джейлбрейком со времен iOS 9» [^20^].
2. В бюллетене безопасности iOS 27 от 14 сентября Apple благодарила "Calif.io in collaboration with Claude and Anthropic Research" за два бага DoS/crash, но они не связаны с показанным джейлбрейком [^14^].
3. В рассылке Calif с Hexacon перечислено четыре демонстрации (Signal 1-click, iMessage, "Can your iPhone do this?", "APT stands for Apple Persistent Threat") под общим девизом "will be released in due time" [^14^][^24^][^25^].
4. Докладчики — Bruce Dang и Thai Duong (XorNinja), бывшие исследователи безопасности Google и лауреаты Pwnie Awards [^17^][^25^].

---

## Источники информации

[^1^]: CyberSecurityNews, "iOS 27.0.1 Untethered Jailbreak Demonstrated on iPhone 18 Pro", 2026-10-16. https://cybersecuritynews.com/ios-27-0-1-jailbreak-demonstrated/
[^2^]: Cyberpress, "iOS 27.0.1 Jailbreak Survives Reboot and Restores Root Access on iPhone 18 Pro", 2026-10-16. https://cyberpress.org/ios-27-0-1-jailbreak-survives-reboot/
[^3^]: EveryMac, "iPhone 18 Pro (US/A3472) Specs (... iPhone19,2)". https://everymac.com/systems/apple/iphone/specs/apple-iphone-18-pro-united-states-a3472-specs.html
[^4^]: AppleDB, "iPhone 18 Pro — Identifier iPhone19,2, iPhone19,3, iPhone19,7; SoC A20 Pro". https://appledb.dev/device/iPhone-18-Pro-series.html
[^5^]: PC Guide, "iPhone 18 Pro benchmarks ... Apple A20 Pro chip" ("The iPhone19,2 identifier refers to the iPhone 18 Pro"), 2026-09-16. https://www.pcguide.com/news/iphone-18-pro-benchmarks-reveal-impressive-scores-for-apple-a20-pro-chip-even-outperforming-desktop-cpus/
[^6^]: Wikipedia, "Apple A19" (Part Number T8150), 2025-09-09. https://en.wikipedia.org/wiki/Apple_A19
[^7^]: База чипов 果粉查询, "Параметры чипа A20 Pro (Borneo, T8160)". https://www.guofenchaxun.com/devices/silicon/chip_a/a20-pro-borneo-t8160
[^8^]: The Apple Wiki, "Codenames" (A20 generation T8160 / Banda / Borneo), 2026-10-07. http://theapplewiki.com/wiki/User:Ilikeiphone123/Playground/Codenames
[^9^]: Wikipedia, "iOS 27 — Version history" (27.0.1 = 24A446, 2026-09-28). https://en.wikipedia.org/wiki/IOS_27
[^10^]: Blake Crosley, "iOS 27.0 Release Notes" (27.0.1 build 24A446, 2026-09-28), 2026-10-01. https://blakecrosley.com/blog/ios-27-release-notes
[^11^]: Лог паники пользователя iPhone15,4 (iPhone OS 27.0.1 24A446, xnu-13432.2.10~2), 2026-10-13. https://otvet.mail.ru/question/270601050?reply
[^12^]: Reddit r/iOS27, Лог паники ядра iPhone 13 Pro (xnu-13432.2.10~2/RELEASE_ARM64_T8110). https://www.reddit.com/r/iOS27/comments/1wp5mqd/
[^13^]: The Apple Wiki, "Kernel" (iOS 27.0 Darwin 27.0.0 / xnu-13432.x), 2026-10-13. http://theapplewiki.com/wiki/Kernel
[^14^]: Decrypt, "Hackers Jailbreak iPhone 18 Pro on Stage, and It Survives a Reboot", 2026-10-16. https://decrypt.co/381177/hackers-jailbreak-iphone-18-pro-survives-reboot
[^15^]: Видео Billy Ellis (@bellis1000) в X, 2026-10-16. https://x.com/bellis1000/status/2111028042495824337
[^16^]: Pasquale Pillitteri, "Calif Unveils iPhone 18 Pro Jailbreak on iOS 27.0.1 at Hexacon", 2026-10-16. https://pasqualepillitteri.it/en/news/24540/jailbreak-iphone-18-pro-ios-27-calif-hexacon
[^17^]: ONE Jailbreak, "Calif Demos Untethered iOS 27.0.1 Jailbreak on iPhone 18 Pro", 2026-10-16. https://onejailbreak.com/blog/calif-demos-untethered-ios-27-0-1-jailbreak-on-iphone-18-pro/
[^18^]: GBHackers, "Researchers Demonstrate iOS 27.0.1 Untethered Jailbreak on iPhone 18 Pro", 2026-10-17. https://gbhackers.com/ios-27-0-1-untethered-jailbreak/
[^19^]: explainX, "Calif.io Jailbreaks iOS 27.0.1 on iPhone 18 Pro: What Is Claimed vs. Verified", 2026-10-16. https://explainx.ai/blog/calif-io-ios-27-0-1-untethered-jailbreak-iphone-18-pro-hexacon-ai-claimed-vs-verified-2026
[^20^]: heise online, "Dank KI: Rebootfester Jailbreak für iOS 27.0.1 bis zum iPhone 18 Pro, untethered", 2026-10-16. https://www.heise.de/news/Untethered-Jailbreak-fuer-iOS-27-0-1-auf-iPhone-18-Pro-der-Reboots-ueberlebt-11490726.html
[^21^]: heise online (English), "Works on iPhone 18 Pro: AI helps create untethered jailbreak for iOS 27.0.1", 2026-10-16. https://www.heise.de/en/news/Works-on-iPhone-18-Pro-AI-helps-create-untethered-jailbreak-for-iOS-27-0-1-11490907.html
[^22^]: Mallory, "Calif Demonstrates Reboot-Persistent iOS 27.0.1 Jailbreak on iPhone 18 Pro", 2026-10-16. https://mallory.ai/stories/01a144a5-33e9-786d-9d6a-311be6bd2189
[^23^]: The Apple Wiki, "List of iPhones" (iPhone 18 Pro Max, прошивка 27.2 beta 3), 2026-09-30. http://theapplewiki.com/wiki/List_of_iPhones
[^24^]: Пост Calif (@calif_io) в X, 2026-10-16. https://x.com/calif_io/status/2111080240978223545
[^25^]: Glitchwire, "Calif Demonstrates Untethered iOS 27.0.1 Jailbreak at Hexacon", 2026-10-16. https://glitchwire.com/news/calif-demonstrates-untethered-ios-2701-jailbreak-at-hexacon-hints-at-signal-and/
