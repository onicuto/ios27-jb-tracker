# Отчет о фактчекинге: Заявления о демонстрации Calif джейлбрейка iOS 27.0.1 на Hexacon 2026

[Русский](ios_jb_audit_dim01.md) | [中文版](ios_jb_audit_dim01-zh.md)

- **Дата проверки**: 2026-10-17
- **Методология проверки**: Поиск в сети (английский / французский / немецкий / китайский языки, всего 7 раундов и 27 поисковых запросов) + прямой сбор первоисточников (hexacon.fr, calif.io, blog.calif.io, support.apple.com)
- **Объем проверки**: 6 утверждений, приведенных ниже

---

## Сводная таблица общих выводов

| № | Утверждение (кратко) | Вердикт | Достоверность |
|---|---|---|---|
| 1 | Hexacon — конференция по наступательной безопасности, организованная французской Synacktiv, 16–17 октября 2026 года в Париже (Palais Brongniart) | **Подтверждено** | Высокая |
| 2 | 2026-10-16 команда Calif (Calif.io) на сцене конференции продемонстрировала непривязанный джейлбрейк iOS 27.0.1 на iPhone 18 Pro | **Подтверждено** (факт демонстрации достоверен; технические заявления независимо не воспроизводились) | Высокая |
| 3 | Calif — «коммерческая команда, проводящая аудит безопасности для IT-гигантов», на сайте предлагает услуги AI red teaming и поиска уязвимостей с помощью ИИ | **Подтверждено** | Высокая |
| 4 | Calif ранее неоднократно находила баги с помощью ИИ (Safari в апреле / M5 в мае / Screen Sharing в августе / благодарность в бюллетене iOS 27 от 14 сентября) | **Подтверждено** (все 4 подпункта имеют первоисточники; есть нюансы в формулировках) | Высокая |
| 5 | В рассылке Calif перечислено 4 демо (включая Signal one-click и iMessage) со словами "will be released in due time" | **Подтверждено** (дословное совпадение с первоисточником) | Высокая |
| 6 | Конференция в этом году позиционирует себя в «эпохе Mythos» ("Mythos era", по имени модели Anthropic) | **Частично подтверждено** (точная фраза "Mythos era" найдена лишь в одном вторичном источнике; материалы сайта подтверждают концептуальную рамку эры ИИ с отсылкой к Mythos) | Средняя |

---

## Попунктная верификация

### Утверждение 1: Базовая информация о конференции Hexacon — Подтверждено (Достоверность: Высокая)

**Критерии верификации**: (a) Конференция реально существует и позиционируется как offensive security; (b) Организатор — французская компания Synacktiv; (c) Даты — 16–17 октября 2026; (d) Место проведения — Париж, Palais Brongniart.

**Свидетельства первоисточников**:

- На странице CFP сайта hexacon.fr дословно указано:

  > "**16th & 17th of October 2026 | Palais Brongniart, 16 Place de la Bourse, 75002 Paris**"
  > "Hexacon is a single-track security conference focused on technical offensive security talks. The conference will take place from the 16th of October 2026 to the 17th, in the heart of Paris."[^1]

- Страница команды hexacon.fr подтверждает статус Synacktiv:

  > "The support of **Synacktiv, our company**, is essential in this adventure."
  > "For more than 10 years now, Synacktiv worked hard to become the French reference among offensive security shops."[^2]

- Исторические подтверждения третьих сторон: обзор первой конференции от SonarSource (2022-10-25): "This is the first edition of this event organized by the French security firm Synacktiv"[^3]; каталог конференций CSOH: "Founded 2022. Single-track, exclusively offensive research... (Synacktiv, Quarkslab, Reverse Tactics)"[^4].

**Детали**: Юридическая формулировка на hexacon.fr называет организатором "The Hexacon team" (22 человека, 1 компания), а Synacktiv — стоящей за ней компанией; поэтому выражение «организована Synacktiv» полностью корректно. Цены билетов (€660–1320) зафиксированы в каталогах событий[^5].

---

### Утверждение 2: 2026-10-16 Calif демонстрирует непривязанный джейлбрейк iOS 27.0.1 — Подтверждено (Достоверность: Высокая)

**Критерии верификации**: (a) 2026-10-16 демонстрация состоялась на сцене Hexacon; (b) Демонстрацию провела Calif (Calif.io); (c) Целевое устройство — iPhone 18 Pro / iOS 27.0.1; (d) Заявлен как untethered (сохраняется после перезагрузки).

**Первичные и непосредственные свидетельства**:

- Официальный аккаунт Hexacon в сети X (2026-10-16):

  > "A brand new iPhone jailbreak has just been unveiled on stage at Hexacon by the @calif_io team."[^6]

- Видеозапись выступления от Billy Ellis (@bellis1000) (2026-10-16):

  > "At #hexacon - Calif.io demos iOS 27.0.1 untethered jailbreak on iPhone 18 Pro"[^7]

- Программа конференции Hexacon: День 1 (пятница, 16 октября) 10:15 **Opening Keynote — Bruce Dang, Thai Duong** (у обоих местом работы указана Calif.io)[^8].

**Перекрестное подтверждение независимыми СМИ** (все публикации от 16–17 октября 2026):

- heise online (англоязычная версия, 2026-10-16): "The jailbreak is also said to be untethered, meaning it survives reboots without requiring a reset."[^9]
- Decrypt (2026-10-16/17): "Security firm Calif.io demonstrated an untethered jailbreak on an iPhone 18 Pro running iOS 27.0.1 on stage at Hexacon, the offensive security conference in Paris, on Friday."[^10]
- CyberSecurityNews (2026-10-16): подробно осветили технические параметры (iPhone19,2, T8160, Darwin 27.0.0, сборка 24A446, SSH на порту 2222 с uid=0, neofetch показывает 67 пакетов dpkg, uptime 2 минуты)[^11].
- Cyberpress[^12], GBHackers[^13], Yahoo Tech[^14] содержат согласованные сведения.

**Обязательные технические оговорки**:

1. Использованные уязвимости не раскрыты, номеров CVE нет, публичный инструмент отсутствует; заявление о непривязанном характере (untethered) **опирается исключительно на сценическое демо и видео очевидцев, независимого воспроизведения не проводилось**. Decrypt со ссылкой на heise отмечает: "it's not yet clear which vulnerabilities Calif.io exploited."[^10]
2. В ходе демонстрации устройство **разблокировалось стандартным паролем экрана блокировки**, что не является свидетельством «обхода экрана блокировки» или «удаленной атаки без клика» (Cyberpress прямо подчеркивает этот факт)[^12].
3. «2 минуты» — это время работы устройства (uptime), выведенное утилитой neofetch с момента перезагрузки, а не длительность выполнения эксплойта[^15].

---

### Утверждение 3: Профиль компании Calif и услуги на официальном сайте — Подтверждено (Достоверность: Высокая)

**Критерии верификации**: (a) Calif действительно существует и является коммерческой ИБ-компанией; (b) Выполняет оценки безопасности для технологических корпораций; (c) На официальном сайте предлагает услуги red teaming ИИ-моделей/агентов и исследования уязвимостей с помощью ИИ.

**Прямые свидетельства с официального сайта** (calif.io, главная страница)[^16]:

> "We're the hacker team that industry titans call first. Even security companies lean on us."
> "Calif secures the AI you use every day. Red teaming and security engineering from the hackers trusted by OpenAI, Anthropic, Google, Cursor and xAI."
> "### AI red teaming — We attack models, agents, and the systems wired around them: jailbreaks, prompt injection, tool abuse, and data exfiltration. Since 2023."
> "### AI-driven vulnerability research — We deploy and tune the pipelines that discover, exploit, and patch bugs at machine speed, then hand them over running inside your own environment."
> "### Security assessments — Red teaming, infrastructure and product reviews..."

В блоке отзывов клиентов на сайте представлены отзывы от инженеров Google: "Our team at Google has engaged with Calif on various security assessments, during which they identified weaknesses and helped us harden our mitigations."[^16]

**Сведения сторонних реестров и СМИ**:

- Crunchbase: Calif, основатели — **An Trinh, Thai Duong**, "provides security services including red teaming, security engineering, and cryptography consulting"[^17].
- WSJ (цитаты по 9to5Mac/iClarified, 2026-05-14): "The researchers with **Calif, a Palo Alto-based security research company**..."[^18]
- NYT (цитаты по Quartz/Anadolu, 2026-09): "Calif, a security company based in **Palo Alto, California**... Calif chief executive **Thai Duong**"[^19]
- Вакансии (Remotive/Jobgether): "Calif is a fast growing tech startup founded by world-class experts from Google. Our client portfolio includes **AWS, Google, SnapChat, Anthropic, and Let's Encrypt**" с указанием зарплат, опционов и бенефитов (явный признак коммерческой компании)[^20].
- Страница компании в LinkedIn насчитывает около 3 439 подписчиков[^21]; персональная страница Thai Duong указывает "Chief at Calif", его биография (также на странице докладчиков hexacon.fr): 12 лет опыта в сфере безопасности и криптографии в Google, соавтор атак BEAST, CRIME, POODLE, лауреат премии Pwnie[^8].

**Нюансы для протокола**:
- В отдельных низкоавторитетных источниках компанию называют "Vietnam-based" (atlas21, gncrypto) или приводят расчетные данные вроде "Саннивейл, основана в 2020 году, выручка $515 151" (prospeo)[^22]. Авторитетные первоисточники (WSJ, NYT, Crunchbase, собственный сайт) единогласно указывают **штаб-квартиру в Пало-Альто, Калифорния**; сооснователь Thai Duong родом из Сайгона, что могло вызвать путаницу. Прямые выписки из корпоративных реестров Делавэра или Калифорнии в открытом доступе не запрашивались.
- Формулировка «выполняет аудиты безопасности для ИТ-гигантов» полностью соответствует списку клиентов (OpenAI, Anthropic, Google, Cursor, xAI, AWS, SnapChat, Let's Encrypt) и отзывам.

---

### Утверждение 4: Предыдущие подтвержденные находки Calif с помощью ИИ — Подтверждено (Достоверность: Высокая)

Разбор каждого подпункта:

**(a) В апреле 2026 года Thai Duong заявил, что Claude помог проанализировать эксплойт Safari для iOS — Подтверждено**

Первоисточник: рассылка Calif Newsletter (blog.calif.io, 2026-04-13/15):

> "**Learning to Jailbreak an iPhone with Claude (Part 1)** — Claude helped me take apart an iOS Safari exploit, and retune it for my Mac. It even wrote its own variant." (Опубликовано 2026-04-13)[^23]
> "The vehicle is **Coruna**, a commercial spyware kit that leaked in full recently: a complete Safari-to-kernel chain for iOS 17... Part 1 is the first stage: CVE-2024-23222..."[^24]

⚠️ Нюанс формулировки: работа заключалась в **деконструкции и модификации утекшей цепочки коммерческого шпионского ПО Coruna** (включая адаптацию эксплойта под macOS), а не в обнаружении новой уязвимости нулевого дня в Safari. Слова «помог проанализировать» точны. Издание Decrypt также зафиксировало этот факт[^10].

**(b) В мае 2026 года эксплойт ядра macOS на процессоре M5 — Подтверждено**

Первоисточник (blog.calif.io, 2026-05-14):

> "The exploit is a data-only kernel local privilege escalation chain targeting macOS 26.4.1 (25E253). It starts from an unprivileged local user, uses only normal system calls, and ends with a root shell... targeting bare-metal M5 hardware with kernel MIE enabled."
> "Bruce Dang found the bugs on April 25th. Dion Blazakis joined Calif on April 27th. Josh Maine built the tooling, and by May 1st we had a working exploit."[^25]

Независимое подтверждение: репортаж WSJ (2026-05-14)[^18]; Apple в бюллетене безопасности macOS Tahoe 26.5 закрыла **CVE-2026-28952** (Kernel) с дословной благодарностью: "Calif.io in collaboration with Claude and Anthropic Research"[^26]; издания TechRadar, Tom's Hardware, SC Media, heise выпустили независимые материалы[^27].

**(c) В августе 2026 года уязвимость в Screen Sharing — Подтверждено**

Первоисточник (calif.io/research/password-fiction, 2026-08-10):

> "**Two pre-auth macOS remote root exploits in four hours.** On Thursday August 6, Apple shipped an emergency macOS update. It fixed exactly one vulnerability, **CVE-2026-65400**, in a feature called Screen Sharing... We started reverse engineering the emergency update and had a working exploit for the bug they fixed about four hours later"[^28]

Фоновое подтверждение: Malwarebytes (2026-08-17) подтвердила, что CVE-2026-65400 представляла собой обход аутентификации в Screen Sharing на macOS и эксплуатировалась in the wild (для установки майнера Monero), Apple выпустила экстренный внеплановый патч 6 августа[^29].
⚠️ Деталь: по своей сути это был **N-day реверс-инжиниринг патча Apple и воссоздание эксплойта**; формулировка об «использовании ИИ» в основном исходит от heise ("used artificial intelligence to derive an exploit from Apple's fix for a serious screen-sharing vulnerability")[^30], в тексте самой Calif роль ИИ прямо не расписана.

**(d) Бюллетень безопасности iOS 27 от 2026-09-14 выражает благодарность Calif.io + Claude + Anthropic Research — Подтверждено (официально подтверждено на сайте Apple)**

В официальном документе Apple "About the security content of iOS 27 and iPadOS 27" (support.apple.com/en-us/149034, 2026-09-14) содержатся две дословные благодарности[^31]:

> "Impact: An app may be able to cause a denial of service ... **CVE-2026-65409: Bruce Dang of Calif.io in collaboration with Claude and Anthropic Research**"
> "Impact: An app may be able to cause unexpected system termination ... **CVE-2026-65410: Calif.io in collaboration with Claude and Anthropic Research**"

Кроме того, по уязвимости **CVE-2026-28968** (out-of-bounds write в ядре) благодарность объявлена исследователю "Josh Maine of Calif.io". Описание Decrypt ("two bugs that let an app cause a denial of service or a system crash. Nothing in the notes ties either bug to the jailbreak") полностью соответствует тексту Apple[^10].

---

### Утверждение 5: 4 демо в рассылке Calif и слова "released in due time" — Подтверждено (Достоверность: Высокая)

Первоисточник: статья в рассылке Calif Newsletter под заголовком "Today, we hacked what we'd set out to hack: the iPhone." (blog.calif.io/p/iphone, 2026-10-16), дословный фрагмент[^32]:

> "Below is a series of demos we revealed at Hexacon in Paris today. **Everything will be released in due time.**
> 1/ Signal 1-click
> 2/ But who cares about a third-party app when everyone uses iMessage, right?
> 3/ Can your iPhone do this?
> 4/ APT stands for Apple Persistent Threat"

Тот же контент опубликован в официальном аккаунте Calif в X (@calif_io) серией из четырех постов (2026-10-16)[^33]. Цитата Decrypt: "Its newsletter post from the conference lists four demos, including a Signal one-click and an iMessage demo, and says everything 'will be released in due time.'"[^10] полностью идентична оригиналу.
⚠️ Деталь: утверждение о наличии демо Signal в один клик и демо iMessage абсолютно точно (пункт 2 оформлен риторическим вопросом об iMessage). Слухи из соцсетей о том, что «в демо iMessage использовался вредоносный PDF», издание Glitchwire пометило как **не поддающиеся независимой проверке**[^34].

---

### Утверждение 6: Позиционирование конференции в «эпоху Mythos» — Частично подтверждено (Достоверность: Средняя)

**Результаты проверки**:

- **Фактологическая основа**: «Mythos» — реальное название семейства моделей Anthropic (Claude Mythos / Mythos Preview, запущенное в апреле 2026 года в рамках Project Glasswing для доверенных партнеров; релиз моделей Mythos 5 и Fable 5 в июне с экспортными ограничениями подтвержден многими СМИ)[^35]; термин «Mythos era» активно используется в индустрии кибербезопасности в 2026 году (Bitsight, Holm Security, Chainguard, HCL и др.) как обозначение эпохи ИИ-поиска уязвимостей[^36].
- **Прямые свидетельства первоисточников конференции**: Аннотация вступительного доклада (Bruce Dang & Thai Duong из Calif) на hexacon.fr дословно гласит:

  > "2026 has been the year of AI for vulnerability research. Within a period of a few months, **frontier models such like Mythos** and the likes have changed the entire research community and its experts' outlook on computer security."[^8]

- **Недостающие звенья**: Дословная формулировка «конференция в этом году позиционирует себя как действующая в 'Mythos era'» обнаружена лишь в одной вторичной публикации explainx.ai (2026-10-16, авторитетность B): "The conference positions itself this year as operating in the 'Mythos era,' a reference to the AI cyber-capable models..."[^37]. На сайте hexacon.fr дословная фраза "Mythos era" не встречается; самое близкое название тренинга звучит как "Attacking Instant Messaging Applications in the **LLM Era**".

**Обоснование вердикта**: Утверждение о том, что именно сама конференция официально объявила себя наступившей «эпохой Mythos», не подтверждено первоисточниками организаторов. Однако ключевой доклад Hexacon открыто признает модель Mythos символом наступления новой эры в анализе уязвимостей 2026 года. Поэтому вердикт — частично подтверждено (концептуально верно, но формулировка «официальное самоназвание конференции» не подтверждена).

---

## Дополнительные согласованные факты контекста

- iOS 27.0.1 (сборка 24A446) — минорное обновление Apple от 2026-09-28 без открытых номеров CVE; сама iOS 27 вышла 2026-09-14[^31][^38].
- Издание heise охарактеризовало это как «первый джейлбрейк, сохраняющийся после перезагрузки, со времен iOS 9» (цитируется по GBHackers)[^13].
- В сентябре 2026 года Calif также раскрыла сетевого червя для WeChat под названием «WeWorm», созданного с помощью ИИ (освещено NYT), после чего Tencent закрыла уязвимость[^19], что подтверждает репутацию компании как передовой ИИ-лаборатории offensive security.

## Честное обозначение не верифицированных аспектов

1. **Техническая подлинность джейлбрейка** (архитектура цепочки, универсальность непривязанного механизма): нет технического отчета, нет CVE, нет независимого воспроизведения, свидетельства ограничены живым показом на сцене и видеозаписью.
2. **Первоисточник фразы "Mythos era"** как официального слогана конференции (возможно, содержалась в рассылке для участников или печатных буклетах, не сохранившихся на веб-страницах).
3. **Юридическая регистрация компании Calif** (штат инкорпорации, точное наименование юридического лица) в открытых базах данных напрямую не локализована.
4. Конкретная техническая роль ИИ в эксплойте Screen Sharing в августе (Calif не раскрывала деталей роли ИИ, авторство приписано heise).

---

## Источники информации

[^1]: Официальный сайт Hexacon — Call for Papers, https://www.hexacon.fr/conference/call-for-papers/ (проверено 2026-10-17)
[^2]: Официальный сайт Hexacon — Team, https://www.hexacon.fr/about/team/ (проверено 2026-10-17)
[^3]: SonarSource Blog — "Bits from Hexacon 2022", 2022-10-25, https://www.sonarsource.com/blog/bits-from-hexacon-2022/
[^4]: CSOH — Security & Hacker Conferences, https://csoh.org/conferences.html (отметка страницы 2026-04-29)
[^5]: Luminik — "Hexacon 2026, Paris: dates and venue", https://www.luminik.io/events/hexacon/
[^6]: X (@hexacon_fr), 2026-10-16, https://x.com/hexacon_fr/status/2111030563020669055
[^7]: Видео Billy Ellis (@bellis1000), 2026-10-16, https://x.com/bellis1000/status/2111028042495824337/video/2
[^8]: Hexacon Agenda / Speakers, https://www.hexacon.fr/conference/speakers/ ; https://www.hexacon.fr/conference/agenda/ (проверено 2026-10-17)
[^9]: heise online — "Works on iPhone 18 Pro: AI helps create untethered jailbreak for iOS 27.0.1", 2026-10-16, https://www.heise.de/en/news/Works-on-iPhone-18-Pro-AI-helps-create-untethered-jailbreak-for-iOS-27-0-1-11490907.html
[^10]: Decrypt — "Hackers Jailbreak iPhone 18 Pro on Stage, and It Survives a Reboot", 2026-10-16/17, https://decrypt.co/381177/hackers-jailbreak-iphone-18-pro-survives-reboot
[^11]: CyberSecurityNews — "iOS 27.0.1 Untethered Jailbreak Demonstrated on iPhone 18 Pro", 2026-10-16, https://cybersecuritynews.com/ios-27-0-1-jailbreak-demonstrated/
[^12]: Cyberpress — "iOS 27.0.1 Jailbreak Survives Reboot and Restores Root Access on iPhone 18 Pro", 2026-10-16, https://cyberpress.org/ios-27-0-1-jailbreak-survives-reboot/
[^13]: GBHackers — "Researchers Demonstrate iOS 27.0.1 Untethered Jailbreak on iPhone 18 Pro", 2026-10-16, https://gbhackers.com/ios-27-0-1-untethered-jailbreak/
[^14]: Yahoo Tech — "Hackers Jailbreak iPhone 18 Pro on Stage, and It Survives a Reboot", 2026-10-16, https://tech.yahoo.com/cybersecurity/articles/hackers-jailbreak-iphone-18-pro-193604534.html
[^15]: Pasquale Pillitteri — "Calif Unveils iPhone 18 Pro Jailbreak on iOS 27.0.1 at Hexacon", 2026-10-16, https://pasqualepillitteri.it/en/news/24540/jailbreak-iphone-18-pro-ios-27-calif-hexacon
[^16]: Главная страница сайта Calif, https://calif.io/ (проверено 2026-10-17)
[^17]: Crunchbase — Профиль компании Calif, https://www.crunchbase.com/organization/calif-837d
[^18]: 9to5Mac (со ссылкой на WSJ / Robert McMillan) — "New macOS vulnerabilities were exposed by Anthropic's Mythos: report", 2026-05-14, https://9to5mac.com/2026/05/14/new-macos-vulnerabilities-were-exposed-by-anthropics-mythos-report/ ; iClarified https://www.iclarified.com/100859/
[^19]: Quartz (со ссылкой на NYT) — "Calif security firm built AI-powered WeChat worm WeWorm", 2026-09-08, https://tech.yahoo.com/cybersecurity/articles/calif-security-firm-built-ai-141643566.html ; Anadolu Agency, 2026-09-09, https://www.aa.com.tr/en/asia-pacific/ai-hacking-tool-builds-worm-that-can-infect-chinas-wechat-accounts-with-call-report/4052290
[^20]: Remotive — "Offensive Security Engineer @Calif", 2026-08-14, https://remotive.com/remote/jobs/all-others/offensive-security-engineer-5547165 ; Jobgether https://jobgether.com/offer/6ac5bd388a27695aea358bb3-offensive-security-engineer
[^21]: LinkedIn Mirror — "Calif | 3,439 followers", https://app.icebreaker.xyz/companies/www.linkedin.com%2Fcompany%2Fcalifio
[^22]: Агрегатор Prospeo, https://prospeo.io/c/calif ; Atlas21, 2026-05-15, https://atlas21.com/claude-mythos-ai-exploit-on-apple-m5-developed-in-less-than-a-week/
[^23]: Calif Newsletter — список статей, https://blog.calif.io/p/mad-bugs-month-of-ai-discovered-bugs (2026-04-16)
[^24]: Calif Newsletter — "Learning to Jailbreak an iPhone with Claude (Part 1)", 2026-04-15, https://blog.calif.io/p/learning-to-jailbreak-an-iphone-with
[^25]: Calif Blog — "First public macOS kernel memory corruption exploit on Apple M5", 2026-05-14, https://blog.calif.io/p/first-public-kernel-memory-corruption
[^26]: LLM-Hacking — "Apple's May 2026 bulletin formally credits Claude on two macOS CVEs", 2026-05-27, https://www.llm-hacking.com/hacks/apple-may-2026-claude-credited-cves.md/ ; ByteIota, 2026-05-26, https://byteiota.com/apple-m5-mie-kernel-exploit-update-to-macos-26-5-now/
[^27]: TechRadar/Yahoo, 2026-05-15, https://tech.yahoo.com/ai/claude/articles/anthropic-mythos-helped-build-working-181500559.html ; heise, 2026-05-15, https://www.heise.de/en/news/Security-Firm-Claude-Mythos-Discovers-macOS-Exploit-11295068.html
[^28]: Calif Research — "Password Fiction", 2026-08-10, https://calif.io/research/password-fiction
[^29]: Malwarebytes — "Update your Mac: Screen Sharing vulnerability exploited in the wild", 2026-08-17, https://www.malwarebytes.com/blog/bugs/2026/08/update-your-mac-screen-sharing-vulnerability-exploited-in-the-wild
[^30]: Хроника Mallory (ссылка на heise online), 2026-10-16/17, https://mallory.ai/stories/01a144a5-33e9-786d-9d6a-311be6bd2189
[^31]: Apple Support — "About the security content of iOS 27 and iPadOS 27", 2026-09-14, https://support.apple.com/en-us/149034
[^32]: Calif Newsletter — "iPhone" ("Today, we hacked what we'd set out to hack: the iPhone."), 2026-10-16, https://blog.calif.io/p/iphone
[^33]: Серия твитов X (@calif_io), 2026-10-16, https://x.com/calif_io/status/2111080247944745106
[^34]: Glitchwire — "Calif Demonstrates Untethered iOS 27.0.1 Jailbreak at Hexacon, Hints at Signal and iMessage Exploits", 2026-10-16, https://glitchwire.com/news/calif-demonstrates-untethered-ios-2701-jailbreak-at-hexacon-hints-at-signal-and/
[^35]: CNET — "Anthropic Pulls Claude Fable and Mythos AI Models After Feds Claim Jailbreak", 2026-06-15, https://www.cnet.com/tech/services-and-software/anthropic-claude-fable-mythos-us-export-controls/ ; Holm Security — "Vulnerability Management in the Claude Mythos Era", 2026-04-28, https://www.holmsecurity.com/blog/claude-mythos-vulnerability-management
[^36]: Bitsight — "The CISO's 90-Day AI (i.e. Claude Mythos) Threat Response Playbook", 2026-05-20, https://www.bitsight.com/guides/the-cisos-90-day-ai-claude-mythos-threat-response-playbook ; Chainguard webinar, 2026-09-15, https://www.chainguard.dev/events/board-ready-security-metrics-for-the-mythos-era
[^37]: explainx.ai — "Calif.io Jailbreaks iOS 27.0.1 on iPhone 18 Pro: What Is Claimed vs. Verified", 2026-10-16, https://explainx.ai/blog/calif-io-ios-27-0-1-untethered-jailbreak-iphone-18-pro-hexacon-ai-claimed-vs-verified-2026
[^38]: ONE Jailbreak — "Calif Demos Untethered iOS 27.0.1 Jailbreak on iPhone 18 Pro", 2026-10-16, https://onejailbreak.com/blog/calif-demos-untethered-ios-27-0-1-jailbreak-on-iphone-18-pro/ ; NightSquawk, 2026-10-10, https://nightsquawk.tech/blog/exploited-flaws-apple-fortimail/
