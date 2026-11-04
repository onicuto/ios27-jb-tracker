# Фактчекинг отчетов о джейлбрейке iOS 27 (Измерение 09)

[Русский](ios_jb_audit_dim09.md) | [中文版](ios_jb_audit_dim09-zh.md)

- Дата проверки: 2026-10-17
- Методология: Глубокий поиск в сети (23 независимых запроса на английском, китайском и немецком языках); перекрестный анализ блогов ИБ-вендоров, IT-медиа, официальных бюллетеней Apple и баз уязвимостей.
- Контекст: 2026-10-16 компания Calif (Calif.io) на конференции Hexacon 2026 в Париже показала работу непривязанного (untethered) джейлбрейка iPhone 18 Pro на iOS 27.0.1[^2][^4].

---

## Утверждение 1: Сайты и приложения, заявляющие о возможности джейлбрейка iOS 27, почти без исключения являются мошенничеством

**Вердикт: Подтверждено (Высокая достоверность, 90%)**, с двумя оговорками по деталям.

### Доказательства

(a) Лаборатория Corellium (в составе Cellebrite) опубликовала детальный разбор мошеннического сервиса «nekoJB Online» (заявлявшего поддержку iOS 18.7–26):

> "nekoJB Online isn't a jailbreak. It's a scam. A trap designed to harvest data and exploit trust."[^5]  
> —— Cellebrite/Corellium, 2026-06-08

Вектор атаки строится на **вредоносных профилях конфигурации**: установка профиля `.mobileconfig`, веб-клипа и корневого сертификата, что открывает возможность перехвата трафика (MITM) и кражи учетных данных:

> "Fake jailbreak scams can use .mobileconfig profiles, web clips, and root certificates to mislead users while enabling traffic interception and possible credential harvesting, according to Corellium."[^6]

(b) Cellebrite в сентябрьском обзоре по iOS 27 напрямую предупреждает:

> "Fake jailbreak tools like nekoJB are circulating and often carry malware."  
> "Tools circulating online that claim to jailbreak iOS 27 are often malware in disguise."[^1]

(c) Практика накрутки кликов и установки нежелательного софта имеет давние прецеденты (например, поддельный сайт checkrain[.]com во времена checkm8, разоблаченный Cisco Talos)[^7][^8].

(d) На момент проверки ни одного публичного инструмента джейлбрейка iOS 27 не существует в природе[^3][^36].

### Оговорки
1. «Опросы за вознаграждение (survey scam)» — классическая схема скама, но в контексте конкретно iOS 27 профильные ИБ-компании ее не фиксировали; подтверждены именно **вредоносные профили/сертификаты** и **кликовые схемы**.
2. Calif доказала техническую реализуемость джейлбрейка на iOS 27.0.1, но публичного дистрибутива нет; следовательно, любые ресурсы, предлагающие «скачать инструмент для iOS 27 прямо сейчас», гарантированно являются скамом.

---

## Утверждение 2: Cellebrite заявляла, что «джейлбрейк iOS 27 невозможен ни на одном реальном физическом устройстве» и «для версий выше iOS 18 нет надежного публичного джейлбрейка»; демонстрация Calif опровергает этот тезис

**Вердикт: Подтверждено (Высокая достоверность, 95%)**, с учетом коммерческого конфликта интересов источника.

### Доказательства

(a) Цитата из официального блога Cellebrite:

> "iOS 27 cannot be jailbroken on any current physical device and there is no reliable public jailbreak for anything above iOS 18."[^1]  
> —— Cellebrite, "Why Jailbreak Is Over with iOS 26", 2026-09-28

В блоке FAQ Cellebrite повторила: "No. There is no public jailbreak for iOS 27 on any current physical device — conservatively, nothing above iOS 18 has a reliable public jailbreak."[^1]

(b) Реакция издания GBHackers:

> "Cellebrite had written just weeks earlier that iOS 27 could not be jailbroken on any current physical device. It also said there was no reliable public jailbreak for anything above iOS 18. This demo challenges that claim."[^2]

(c) Демонстрация Calif 2026-10-16 в Париже на актуальном флагмане iPhone 18 Pro (iOS 27.0.1, build 24A446) с автоматическим восстановлением root после перезагрузки наглядно доказала обратное[^2][^4].

### Нюансы
1. **Конфликт интересов**: Статья Cellebrite носила откровенно маркетинговый характер, продвигая виртуальные инстансы Corellium ("Corellium is the only way to fully analyze and verify iOS internals")[^1].
2. Демонстрация опровергла первую часть тезиса («невозможен на физических устройствах»), тогда как вторая часть («нет надежного **публичного** джейлбрейка выше iOS 18») формально остается в силе, так как утилиты не выпускались[^2][^3].
3. Хронология: статья Cellebrite вышла 2026-09-28 — за 2,5 недели **до демонстрации** (а не до релиза iOS 27).

---

## Утверждение 3: Производители коммерческого spyware скупают подобные эксплойт-цепочки; у Calif нет мотивации отдавать их бесплатно в сообщество

**Вердикт: Исходные данные достоверны, вывод является логически обоснованным предположением (Достоверность предпосылок 95%, вывода 75%)**, с оговоркой о встречных заявлениях.

### Анализ рынка эксплойтов
(a) Публичные расценки брокеров уязвимостей на полные цепочки под iOS:
- Zerodium: до $2 000 000 за zero-click цепочку с персистентностью[^13].
- Crowdfense: от $5 000 000 до $7 000 000 за цепочки под iOS, и до $9 000 000 за zero-click через SMS/MMS[^14][^15][^16].

(b) Данные Google TAG: производители коммерческого шпионского ПО (NSO Group, Intellexa и др.) стоят за 55% всех обнаруженных в мире 0-day эксплойтов для iOS и Safari[^16][^17].

### Поведение Calif на рынке
Calif — коммерческая компания из Пало-Альто, предлагающая услуги red teaming и аудита безопасности[^39]. Историческая модель ее поведения:
- В мае 2026 года при взломе MIE на чипе M5 компания **не выпускала эксплойт**, а передала 55-страничный отчет лично в штаб-квартиру Apple в Купертино[^11][^12].
- При обнаружении CVE-2026-86950 в сентябре 2026 года Calif после выхода патча выложила лишь **crash-only PoC** без боевого пейлоада[^18][^19][^34].

Отсутствие финансовых причин отдавать многомиллионную цепочку бесплатно вполне очевидно.

### Встречное свидетельство
Billy Ellis и портал ONE Jailbreak отметили, что ведущие со сцены упомянули фразу "will be released in due time"[^3][^10]. Однако GBHackers подчеркивает: "That is a secondary claim, not a Calif statement"[^2]. Даже если публикация состоится, по опыту Calif это будет аналитический отчет или узкий PoC после выхода официального патча Apple, а не утилита для пользователей.

---

## Утверждение 4: Ожидается, что Apple исправит уязвимости в «следующем 27.0.x или 27.1»

**Вердикт: Частично подтверждено (Вектор реакции верен, но указание версий ошибочно) (Достоверность: 80%).**

### Историческая скорость закрытия дыр
- Кейс iOS 12.4.1 (2019): баг SockPuppet закрыт Apple через **8 дней** после релиза unc0ver[^20][^21].
- Кейс iOS 16.5.1 (2023, операция Triangulation): ядро закрыто за 20 дней после раскрытия[^22].
- В 2026 году серверный баг подписи TSS был закрыт за несколько дней без обновления прошивки[^3].

### Ошибка в номерах версий
Версия **iOS 27.1 является эксклюзивной для складного iPhone Duo**; для обычных iPhone эта версия пропускается:

> "since the iOS 27.1 build is made with iPhone Duo elements in mind, that version is being skipped for the non-foldable iPhone models."[^25]

Следующим окном обновлений для стандартных iPhone является **27.0.2** либо **iOS 27.2** (которая тестируется в beta 4 build 24B5110a)[^23][^26]. Поскольку уязвимости Calif не раскрыты публично, Apple потребуется время на локализацию, и моментальный фикс не гарантирован.

---

## Утверждение 5: Риски сидения на старой версии: чего лишена iOS 26.1 по сравнению с 27.0.1

**Вердикт: Общий вывод верен, но тезис «в релиз iOS 27 вошли исправления 0-day из KEV» неточен (Достоверность: 85%).**

### Масштаб исправлений в iOS 27
В iOS 27 от 14 сентября закрыто **126 уникальных уязвимостей** (включая около 20 в ядре)[^9][^28].

### Оговорка по 0-day in-the-wild
При релизе iOS 27 Apple **не заявляла** об активной эксплуатации закрытых багов в реальных атаках[^28][^29]. Уязвимость нулевого дня CVE-2026-86950 (в CoreGraphics), эксплуатировавшаяся в targeted-атаках, была закрыта в обновлении **iOS 26.7.1**, а не в базовом релизе 27.0[^30][^31][^32].

### Реальные риски версии 26.1
Пользователь, остающийся на iOS 26.1 (вышедшей в начале ноября 2025 года), не получил:
1. Все обновления безопасности от **iOS 26.2 до 26.7.1** (свыше 100 исправлений).
2. Исправления двух подтвержденных атак нулевого дня 2026 года: CVE-2026-20700 (dyld) и CVE-2026-86950 (CoreGraphics)[^30][^37].
3. Уникальные исправления ядра и подсистем iOS 27.

Вывод отчета верен: сидеть на 26.1 небезопасно. При этом демонстрация Calif проводилась на 27.0.1, так что для пользователей 26.1 надежд на релиз джейлбрейка нет вдвойне.

---

## Итоговая таблица

| № | Утверждение | Вердикт | Достоверность |
|---|-------------|---------|---------------|
| 1 | Фейковые джейлбрейки iOS 27 — скам | Подтверждено (схемы через профили и сертификаты доказаны) | 90% |
| 2 | Заявление Cellebrite и опровержение показом Calif | Подтверждено (с учетом маркетинговой цели Cellebrite; формулировка «до показа») | 95% |
| 3 | Спрос со стороны spyware и отсутствие мотивов у Calif | Подтверждено (рынок многомиллионный, Calif придерживается ответственного раскрытия) | 75–95% |
| 4 | Apple закроет баги в «27.0.x или 27.1» | Частично подтверждено (скорость верна; но 27.1 — только для Duo, обычным смартфонам выйдет 27.0.2 / 27.2) | 80% |
| 5 | Риски безопасности при сохранении iOS 26.1 | Подтверждено (дыра в безопасности огромна; уточнен статус 0-day в 26.7.1) | 85% |

---

## Источники информации

[^1]: Cellebrite, "Why Jailbreak Is Over with iOS 26", 2026-09-28. https://cellebrite.com/en/blog/ios-risk-for-mobile-app-developers-and-security-teams/
[^2]: GBHackers, "Researchers Demonstrate iOS 27.0.1 Untethered Jailbreak on iPhone 18 Pro", 2026-10-16. https://gbhackers.com/ios-27-0-1-untethered-jailbreak/
[^3]: ONE Jailbreak, "Calif Demos Untethered iOS 27.0.1 Jailbreak on iPhone 18 Pro", 2026-10-16. https://onejailbreak.com/blog/calif-demos-untethered-ios-27-0-1-jailbreak-on-iphone-18-pro/
[^4]: Cyber Security News, "iOS 27.0.1 Untethered Jailbreak Demonstrated on iPhone 18 Pro", 2026-10-16. https://cybersecuritynews.com/ios-27-0-1-jailbreak-demonstrated/
[^5]: Cellebrite / Corellium, "nekoJB Jailbreak Scam? Investigating the iOS 18.7 Fake Jailbreak Trap", 2026-06-08. https://cellebrite.com/en/blog/nekojb-jailbreak-scam/
[^6]: NHI Mgmt Group, "Fake iOS jailbreak scams are turning profiles into credential traps", 2026-08-18. https://nhimg.org/articles/fake-ios-jailbreak-scams-are-turning-profiles-into-credential-traps/
[^7]: PCMag, "Scammer Uses Fake iPhone Jailbreak for Fraud Scheme", 2019-10-15. https://www.pcmag.com/news/scammer-uses-fake-iphone-jailbreak-for-fraud-scheme
[^8]: CyberScoop, "Scammers are dangling an iOS jailbreak to trick victims into downloading a malicious app", 2019-10-15. https://cyberscoop.com/ios-jailbreak-checkm8-app-fraud/
[^9]: Mallory, "Calif Demonstrates Reboot-Persistent iOS 27.0.1 Jailbreak on iPhone 18 Pro", 2026-10-16. https://mallory.ai/stories/01a144a5-33e9-786d-9d6a-311be6bd2189
[^10]: explainx, "Calif.io Jailbreaks iOS 27.0.1 on iPhone 18 Pro: What Is Claimed vs. Verified", 2026-10-16. https://explainx.ai/blog/calif-io-ios-27-0-1-untethered-jailbreak-iphone-18-pro-hexacon-ai-claimed-vs-verified-2026
[^11]: Digit, "Anthropic Mythos helped researchers break Apple M5 shield on macOS: Report", 2026-05-15. https://www.digit.in/news/general/anthropic-mythos-helped-researchers-break-apple-m5-shield-on-macos-report.html
[^12]: 163.com, "Взлом систем безопасности Apple с помощью Mythos", 2026-05-15. https://www.163.com/dy/article/KSVN9AT30511BLFD.html
[^13]: CERT-EU Threat Memo, "Android exploits commanding higher price than ever before". https://cert.europa.eu/publications/threat-intelligence/threat-memo-190910-1/pdf
[^14]: mapshock, "Zero-Day Market Dynamics: Broker Pricing, Government Procurement, and Disclosure Norms", 2026-08-22. https://mapshock.com/briefings/zero-day-market-dynamics-broker-pricing-government
[^15]: BrightDefense, "80+ Zero-Day Exploit Statistics", 2026-09-02. https://www.brightdefense.com/resources/zero-day-exploit-statistics/
[^16]: cybersecurity-help.cz, "Exploit broker offers millions of dollars for iOS, Android zero-day exploits". https://www.cybersecurity-help.cz/blog/3916.html
[^17]: SecurityWeek, "Google Catches Russian APT Reusing Exploits From Spyware Merchants", 2024-08-29. https://www.securityweek.com/google-catches-russian-apt-re-using-exploits-from-spyware-merchants-nso-group-intellexa/
[^18]: Cyber Kendra, "CVE-2026-86950: The CoreGraphics Glyph Bug That Hit iPhones", 2026-10-01. https://www.cyberkendra.com/2026/10/cve-2026-86950-the-coregraphics-glyph-bug-that-hit-iphones.html
[^19]: GajShield KB, "CVE-2026-86950 PoC Shows How a Malicious PDF Font Can Corrupt Apple Memory", 2026-10-01. https://kb.gajshield.com/a/1534/
[^20]: SecureMac, "The Great iOS Jailbreak of 2019—and why you should update to 12.4.1 right now!", 2019-08-26. https://www.securemac.com/news/the-great-ios-jailbreak-of-2019-and-why-you-should-update-to-12-4-1-right-now
[^21]: TheAppleWiki, "Unc0ver" (v3.5.0, 2019-08-18). https://theapplewiki.com/wiki/Unc0ver
[^22]: SentinelOne Vulnerability Database, "CVE-2023-32434". https://www.sentinelone.com/vulnerability-database/cve-2023-32434/
[^23]: Wikipedia, "iOS 27" (история версий). https://en.wikipedia.org/wiki/IOS_27
[^24]: blakecrosley.com, "Xcode 27.1 Beta: Your App in the iPhone Duo Simulator", 2026-10-11. https://blakecrosley.com/blog/xcode-27-1-beta-iphone-duo-simulator
[^25]: macsonly.com, "macOS 27.2 Beta 1 is Out... 27.1 Skipped for the iPhone Duo", 2026-09-21. https://macsonly.com/article/2026/macos-27-2-beta-1-is-out
[^26]: Zeera Wireless, "Apple Released iOS 27.2 Beta Before iOS 27.1", 2026-09-17. https://zeerawireless.com/blogs/news/ios-27-2-beta-features-why-before-ios-27-1
[^27]: 9to5Mac, "iOS 27.1 release date: Here's when to expect the new iPhone update", 2026-09-11. https://9to5mac.com/2026/09/11/ios-27-1-release-date-heres-when-to-expect-the-new-iphone-update/
[^28]: GBHackers, "Apple Releases iOS 27 Security Update to Fix Over 120 Vulnerabilities", 2026-09-16. https://gbhackers.com/apple-releases-ios-27-security-update/
[^29]: SecurityWeek, "Apple Patches 200 Vulnerabilities With New iOS 27, macOS Golden Gate 27 Releases", 2026-09-15. https://www.securityweek.com/apple-patches-200-vulnerabilities-with-new-ios-27-macos-golden-gate-27-releases/
[^30]: BleepingComputer, "Apple patches CoreGraphics zero-day flaw exploited in attacks", 2026-09-29. https://www.bleepingcomputer.com/news/security/apple-patches-coregraphics-zero-day-flaw-exploited-in-attacks/
[^31]: The Register, "Apple patches CoreGraphics zero-day already exploited in targeted attacks", 2026-09-29. https://www.theregister.com/security/2026/09/29/apple-patches-coregraphics-zero-day-already-exploited-in-targeted-attacks/5299721
[^32]: Apple, "Apple security releases". https://support.apple.com/en-us/100100
[^33]: blakecrosley.com, "iOS 27.0 Release Notes", 2026-10-01. https://blakecrosley.com/blog/ios-27-release-notes
[^34]: zerohour.day, "CVE-2026-86950". https://zerohour.day/cves/CVE-2026-86950
[^35]: MacRumors Forums, "iOS 27 and iOS 26.7 Fix More Than 100 Security Bugs", 2026-09-14. https://forums.macrumors.com/threads/2489301/
[^36]: 4uKey (Tenorshare), "Jailbreak iOS 27: Latest Status, Tools & Safer Options", 2026-08-28. https://www.4ukey.com/unlock-iphone/ios-27-jailbreak.html
[^37]: SOC Prime, "CVE-2026-20700: Apple Patches Zero-Day Exploited in Sophisticated Cyber Attacks", 2026-02-12. https://socprime.com/blog/cve-2026-20700-vulnerability/
[^38]: HEAL Security, "New usbliter8 SecureROM Exploit Enables iOS 27 Jailbreak on iPhone 11 Pro", 2026-07-27. https://healsecurity.com/new-usbliter8-securerom-exploit-enables-ios-27-jailbreak-on-iphone-11-pro/
[^39]: Pasquale Pillitteri, "Calif Unveils iPhone 18 Pro Jailbreak on iOS 27.0.1 at Hexacon", 2026-10-16. https://pasqualepillitteri.it/en/news/24540/jailbreak-iphone-18-pro-ios-27-calif-hexacon
