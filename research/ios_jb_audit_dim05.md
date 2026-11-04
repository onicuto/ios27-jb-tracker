# Отчет о фактчекинге Измерения 05: Текущий статус джейлбрейка iOS/iPadOS 26 и диапазон поддержки Dopamine 3.0

[Русский](ios_jb_audit_dim05.md) | [中文版](ios_jb_audit_dim05-zh.md)

**Дата проверки**: 2026-10-17  
**Проверяющий**: Фактчекер экосистемы джейлбрейка iOS  
**Исходные данные пользователя**: iPhone 12 Pro Max (чип A14) + iPad mini 6 (чип A15), оба на iOS/iPadOS 26.1; пользователь исходит из посылки, что «старую 26.0.1 уже можно джейлбрейкнуть»  
**Методология**: 17 независимых веб-поисков + прямое извлечение данных с сайта Dopamine (ellekit.space), бюллетеней Apple (support.apple.com/125632, 100100), theapplewiki.com, ipsw.me  

---

## Главный вывод (суть вкратце)

| Вопрос | Вердикт |
|---|---|
| Возможен ли джейлбрейк iPhone 12 Pro Max (A14) на **любой** версии iOS 26? | **Нет.** Поддержка iOS 26 в Dopamine ограничена только чипами A12/A13; верхний предел для A14 в Dopamine — iOS 17.3.1 |
| Возможен ли джейлбрейк iPad mini 6 (A15) на **любой** версии iPadOS 26? | **Нет.** В официальной таблице theapplewiki для iPad mini 6 в графе 26.0/26.0.1 прямо указано "No", а начиная с 26.1 вся строка — "No Tool Available" |
| Существуют ли инструменты джейлбрейка для релизной iOS 26.1 и новее (для любых чипов)? | **Нет** (только тестовые сборки 26.1 beta 1–3 поддерживались в Dopamine 3.0.5 на A12/A13; для релизной 26.1 инструментов нет) |
| Реален ли откат на 26.0.1? | **Нереален.** Apple закрыла окно подписи iOS 26.0.1 (еще в ноябре 2025 года вскоре после выхода 26.1); на 2026-10-17 для всех моделей подписывается только iOS 27.0.1. И даже при возможности даунгрейда на 26.0.1 для A14/A15 джейлбрейка все равно нет |
| Исходная посылка пользователя: «старую 26.0.1 уже можно джейлбрейкнуть» | **Правда лишь наполовину и неприменима к устройствам пользователя.** Джейлбрейк 26.0/26.0.1 реален только для процессоров A12/A13 (iPhone 11 / SE2, iPad 8/9, mini 5, Air 3), куда чипы пользователя A14/A15 не входят |

**Достоверность: Высокая.** Выводы независимо подтверждены из 5 источников: GitHub/сайт Dopamine, бюллетени Apple, theapplewiki, iClarified, MacRumors.

---

## Попунктный вердикт

### Утверждение 1: Dopamine 3.0 вышел в августе 2026 года с поддержкой iOS 26.0/26.0.1 только для A12/A13

**Вердикт: В целом подтверждено (с уточнением списка моделей). Достоверность: Высокая.**

- Дата релиза — **7 августа 2026 года** (в ряде азиатских СМИ указано 8 августа из-за часовых поясов). В theapplewiki зафиксировано: "Dopamine 3.0 released on 7 August 2026 … Support for iOS 16.6-18.7.1 and iOS 26.0-26.0.1 was unexpectedly added for A12/A13 devices, thanks to the release of Momentarius."[^1^]
- MacRumors (2026-08-07): "Lars Fröder, better known as opa334, today released Dopamine 3.0, which adds support for a number of newer firmware versions, including iOS 26.0 and iOS 26.0.1 on devices with A12 or A13 chips."[^2^]
- Описание официального репозитория Dopamine на GitHub: "A rootless semi-untethered jailbreak for iOS 15.0 - 17.3.1 (arm64e), iOS 15.0 - 18.7.1, 26.0 - 26.0.1 (A12/A13) and iOS 15.0 - 18.7.1 (arm64)."[^3^]
- Официальный сайт Dopamine (ellekit.space): "Supported on iOS 15.0 - 17.3.1 (A14 - A17 / M1 - M2) / Supported on iOS 15.0 - 18.7.1 and 26.0 - 26.0.1 (A8 - A13)."[^4^]
- **Точные границы поддерживаемых устройств**: На уровне чипов это **A12 / A12X / A12Z / A13**. Однако формулировка в отчетах о «линейках iPhone XS/XR/11, SE2» вводит в заблуждение: **iPhone XS/XR (чип A12) физически не поддерживают iOS 26** — официальный список Apple для iOS 26 начинается с iPhone 11[^5^]. Таким образом, среди iPhone поддержка iOS 26 есть только на **A13**: iPhone 11 / 11 Pro / 11 Pro Max и iPhone SE (2-го поколения). Поддержка A12 фактически касается только iPad (iPad 8-го поколения, iPad Air 3, iPad mini 5 могут работать на iPadOS 26)[^6^][^7^].
- Матрица iClarified: "iPhone 11 lineup / SE (2nd Gen) | A13 | iOS 26.0.1 (Dopamine)", "iPhone 12 lineup | A14 | iOS 17.3.1 (Dopamine)", "iPhone 13 lineup / SE (3rd Gen) | A15 | iOS 17.3.1 (Dopamine)". "iPhone 16 / 17 lineups | A18 / A19 families | No public jailbreak"[^8^].

### Утверждение 2: Для iOS 26.1 и новее нет инструментов джейлбрейка (theapplewiki указывает для 26.1 "No Tool Available")

**Вердикт: Подтверждено (с важным исключением для бета-версий). Достоверность: Высокая.**

- В таблицах theapplewiki по ветке 26.x для iPadOS: "26.0 Dopamine 3.0.11 … / 26.0.1 Dopamine 3.0.11 … / **26.1 No Tool Available** / 26.2 No Tool Available / 26.2.1 No Tool Available"; для iOS аналогично статус 26.1 — "No Tool Available"[^7^][^9^].
- **Исключение для бета-сборок**: В ченджлоге Dopamine 3.0.5 от 2026-08-13 указано: "**Actually** enable support for iOS 26.1 beta 1 - 3 (A12/A13)"[^10^]. То есть джейлбрейк был возможен только на бета-сборках 26.1 beta 1–3 на A12/A13. Для релизной 26.1 от 2025-11-03 и всех последующих версий (26.2–26.6.2 и релизной iOS 27) публичных инструментов нет[^5^][^11^].
- Исторический обзор TechEngage: "There is no public jailbreak for iOS 26.1 or later, or for iPhone 12 and newer models on any iOS 26 build."[^6^]

### Утверждение 3 (Критическое): Существует ли джейлбрейк для A14 (iPhone 12) и A15 (iPad mini 6, iPhone 13, SE3) на iOS/iPadOS 26.x?

**Вердикт: Публичных инструментов нет вообще. Утверждение iClarified о том, что для A14–A17 верхний предел — iOS 17.3.1, подтверждено. Достоверность: Высокая.**

- На сайте Dopamine прямо указано: "Supported on iOS 15.0 - 17.3.1 (A14 - A17 / M1 - M2)" — планка для A14/A15 заканчивается на 17.3.1, не затрагивая ни iOS 18, ни iOS 26[^4^].
- Статья в The Apple Wiki о Dopamine: "...for arm64 devices running iOS 15.0 - 18.7.1, A12/A13 devices running 15.0-18.7.1 and 26.0-26.0.1 as well as **A14- A17 Pro, M1 & M2 devices running iOS 15.0 - 17.3.1**"[^1^].
- Для iPad mini 6 в графах iPadOS 26.0 и 26.0.1 в таблице The Apple Wiki стоит однозначное "No"[^7^].
- В таблицах совместимости ONE Jailbreak поддержка iOS 26 для линеек на A14/A15 полностью отсутствует[^12^].

### Утверждение 4: Почему Dopamine 3.0 поддерживает iOS 26 только на A12/A13? Связано ли это с usbliter8?

**Вердикт: Это никак не связано с usbliter8. Причина кроется в чисто программной связке: обход PPL momentarius (работающий только на A12/A13) + эксплойт ядра ClearSword/DarkSword. На чипах A14+ в iOS 17.4+ защита PPL заменена на SPTM, а публичных обходов SPTM для версий ≥17.4 не существует. Достоверность: Высокая.**

- Из ченджлога Dopamine 3.0: "Add Titan PPL/SPTM bypass by @alfiecg24, introduces support for all devices running 16.5.1 - 17.3.1", "Add momentarius PPL bypass by @staturnzz and @TheRealClarity, introduces support for A12/A13 devices running 16.6 - 18.7.1, 26.0 - 26.0.1", "obviously only works up to 17.3.1 on real devices due to lack of an SPTM bypass on >=17.4", "Add ClearSword exploit by @TheRealClarity, cleaner alternative to DarkSword"[^1^][^13^].
- Разбор в сообществе r/jailbreak (u/Yeth3): "26.0.1 is only supported on A12/A13 because they have a new PPL bypass and the darksword kernel exploit. A15+ on 17.0+ replaces PPL with SPTM, and darksword is patched on 26.1"[^14^].
- **Роль usbliter8**: Это аппаратный эксплойт SecureROM для A12/A13, требующий физического подключения платы в DFU. Он **не входит** в состав Dopamine и не используется им (Dopamine — программный джейлбрейк)[^15^][^16^].
- Архитектурная причина: На более новых процессорах A15+ внедрен монитор SPTM (Secure Page Table Monitor), который не позволяет модифицировать таблицы страниц через ядро без отдельного обхода SPTM. Эксплойт Titan умел обходить SPTM только до iOS 17.3.1 включительно[^1^][^13^].

### Утверждение 5: Какие уязвимости закрыла Apple в iOS 26.1?

**Вердикт: В iOS 26.1 (2025-11-03) закрыто множество критических багов ядра, песочницы и WebKit; сообщество связывает релиз 26.1 с закрытием ядра DarkSword, но Apple прямо не указывает, какой именно CVE соответствует эксплойту джейлбрейка. Достоверность: Выше средней.**

Бюллетень безопасности Apple для iOS 26.1 фиксирует ключевые исправления[^18^]:
- Ядро: CVE-2025-43447, CVE-2025-43462 (повреждение памяти ядра), CVE-2025-43520 (запись в память ядра), CVE-2025-43398.
- Песочница: CVE-2025-43407, CVE-2025-43448 (побег из песочницы).
- WebKit: свыше 10 уязвимостей (Use-After-Free CVE-2025-43438, переполнение буфера CVE-2025-43429).

Официально Apple не подтверждает конкретный номер CVE для эксплойта DarkSword/ClearSword, поэтому категорично связывать конкретный CVE с джейлбрейком в отчетах не следует.

### Утверждение 6: Поддержка iOS 26 инструментами checkm8 (palera1n)

**Вердикт: Инструменты checkm8 в принципе неприменимы к iOS 26 — ни одно уязвимое к checkm8 устройство не поддерживает iOS 26. Достоверность: Высокая.**

- Эксплойт checkm8 затрагивает процессоры от A5 до A11 (от iPhone 4S до iPhone X). Потолок обновлений для iPhone X/8 — iOS 16.7.x, для самого свежего iPad на checkm8 (iPad 7 на A10) — iPadOS 18.x. Устройств на checkm8 с поддержкой iOS 26 в природе не существует[^6^].
- Поддержка ветки 26 в palera1n относится исключительно к **tvOS и bridgeOS** (tvOS 26.0 / bridgeOS 10.0 на Apple TV и чипах T2 в Mac)[^20^][^21^]. Утверждения SEO-статей о «джейлбрейке iOS 26 через palera1n» являются дезинформацией.

---

## Прямые ответы на вопросы пользователя

1. **iPhone 12 Pro Max (A14, iOS 26.1)**: На текущий момент джейлбрейк невозможен ни на 26.1, ни на 26.0, ни на 26.0.1. Потолок для чипа A14 — iOS 17.3.1[^4^][^8^].
2. **iPad mini 6 (A15, iPadOS 26.1)**: Джейлбрейк также невозможен ни на одной версии 26.x[^7^].
3. **Откат на 26.0.1**: Невозможен физически (подпись закрыта в ноябре 2025 года, подписывается только 27.0.1) и бессмысленен практически (на 26.0.1 для A14/A15 все равно нет джейлбрейка)[^22^][^23^].
4. **Коррекция ожиданий**: Фраза «26.0.1 уже можно взломать» верна строго для процессоров A12/A13. Для чипов пользователя A14/A15 на любых версиях iOS 26.x и 27.x публичных путей джейлбрейка не существует.

---

## Источники информации

[^1^]: The Apple Wiki — Dopamine (обновление от 2026-10-12): https://theapplewiki.com/wiki/Dopamine
[^2^]: MacRumors — "iOS 26 Gets First Jailbreak Thanks to Dopamine" (2026-08-07): https://www.macrumors.com/2026/08/07/ios-26-dopamine-jailbreak/
[^3^]: GitHub — opa334/Dopamine: https://github.com/opa334/dopamine
[^4^]: Официальный сайт Dopamine: https://ellekit.space/dopamine/
[^5^]: Apple Security Releases (iOS 26.1 and iPadOS 26.1, 03 Nov 2025): https://support.apple.com/en-us/100100
[^6^]: TechEngage — "iOS Jailbreak History: Every Major Tool From 2007 to 2026" (2026-09-14): https://techengage.com/ios-jailbreaking-complete-history/
[^7^]: The Apple Wiki — Jailbreak/26.x (таблица iPadOS): https://theapplewiki.com/wiki/Jailbreak/26.x
[^8^]: iClarified — Руководство по джейлбрейку iPhone (2026-08-07): https://www.iclarified.com/jailbreak
[^9^]: The Apple Wiki — Jailbreak/26.x (снимок 2026-09-28): https://theapplewiki.com/wiki/Jailbreak/26.x
[^10^]: GitHub — opa334/Dopamine Releases v3.0.5 (2026-08-13): https://github.com/opa334/Dopamine/releases
[^11^]: ipsw.me — Релизы iOS (Signed IPSW): https://ipsw.me/iOS/
[^12^]: ONE Jailbreak — "Dopamine Jailbreak IPA Download & Install iOS 15.0-26.0.1": https://onejailbreak.com/blog/dopamine-jailbreak/
[^13^]: ONE Jailbreak — "Dopamine 3.0 Jailbreak Out With iOS 26 Support" (2026-08-07): https://onejailbreak.com/blog/dopamine-3-0-jailbreak-out-with-ios-26-support/
[^14^]: ComputerBase — "Dopamine Jailbreak: iOS 26 geknackt" (2026-08-08): https://www.computerbase.de/news/smartphones/dopamine-jailbreak-ios-26-wurde-nach-326-tagen-geknackt.98764/
[^15^]: SecurityAffairs — "usbliter8 Brings Unpatchable BootROM Exploit", 2026-06-22: https://securityaffairs.com/193965/hacking/usbliter8-brings-unpatchable-bootrom-exploit-to-apple-a12-and-a13-devices.html
[^16^]: GitHub — prdgmshift/usbliter8: https://github.com/prdgmshift/usbliter8
[^17^]: usbliter8.info — "Can usbliter8 be used for Untethered A12/A13 jailbreak?": https://www.usbliter8.info/can-usbliter8-be-used-for-untethered-a12-and-a13-jailbreak/
[^18^]: Apple — About the security content of iOS 26.1 and iPadOS 26.1: https://support.apple.com/en-us/125632
[^19^]: PK Sharma Security Briefing (2026-09-16): https://www.pk-sharma.com/briefing/packagist-removed-thirteen-fourteenth-still-there
[^20^]: palera1n GitHub (зеркало): https://blog.csdn.net/gitblog_00621/article/details/155635983
[^21^]: The Apple Wiki — Palera1n релизы: https://theapplewiki.com/wiki/Palera1n
[^22^]: ipsw.me — IPSW для iPhone 12: https://ipsw.me/iPhone13,2/
[^23^]: ipsw.me — Статус подписи iPhone 12 Pro Max: https://ipsw.me/iPhone12,5
[^24^]: OSTORE — "Apple закрыла возможность отката с iOS 26.1 на iOS 26.0.1", ноябрь 2025: https://ostore.ru/blog/obzory-tovarov-i-novosti/apple-zakryla-vozmozhnost-otkata-s-ios-26-1-na-ios-26-0-1/
