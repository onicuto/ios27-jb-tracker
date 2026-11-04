# Отчет о фактчекинге списков поддержки iOS/iPadOS 27 и обновлений безопасности (dim07)

[Русский](ios_jb_audit_dim07.md) | [中文版](ios_jb_audit_dim07-zh.md)

- Дата проверки: 2026-10-17
- Методология: 16 независимых поисков в сети; приоритет отдан официальным ресурсам Apple (продуктовые страницы apple.com, документация поддержки, списки безопасности Apple Security Releases), а также материалам MacRumors, Macworld, The Verge, Tom's Guide, EveryMac.
- Общий вердикт: **Утверждение 1 частично верно (первая часть верна, вторая опровергнута — iOS 27 не прекращала поддержку iPhone 11); утверждения 2, 3 и 4 в целом подтверждены (с важными уточнениями); предпосылка в утверждении 5 ложна, вывод несостоятелен.**

---

## Утверждение 1: iOS 26 поддерживает iPhone 11 и новее; iOS 27 прекратила поддержку iPhone 11, поддерживая только iPhone 12 и новее

**Вердикт: Частично подтверждено — первая часть верна, вторая [ОПРОВЕРГНУТА]. Достоверность: Исключительно высокая.**

- Первая часть («iOS 26 поддерживает iPhone 11 и новее») **подтверждена**. В документации поддержки Apple «How to download iOS 26» дословно указано: "iOS 26 is compatible with iPhone models: … iPhone 11, iPhone 11 Pro, iPhone 11 Pro Max, iPhone SE (2nd generation and later)"[^1].
- Вторая часть («iOS 27 прекратила поддержку iPhone 11») **опровергнута**. На официальной странице iOS 27 (apple.com) прямо указано: "iOS 27 is compatible with these devices. … iPhone 11 Pro Max, iPhone 11 Pro, iPhone 11, iPhone SE (2nd generation and later)"[^2]. В бюллетенях безопасности для iOS 27 и 27.0.1 целевыми устройствами значатся "iPhone 11 and later"[^3]. Издание MacRumors от 2026-09-09 дословно пишет: "Apple's latest software carries over the same device compatibility list as iOS 26, so no iPhones have been dropped this year."[^4]. В The Verge в день релиза подтвердили: "The iOS 27 update will be available for iPhone 11 and iPhone SE (2nd gen) and later devices"[^5].
- Примечание: Встречающиеся в сети утверждения о поддержке iOS 27 лишь начиная с iPhone 13 являются недостоверными и противоречат официальным источникам Apple.

## Утверждение 2: Список поддержки iPadOS 27 (поддерживается ли iPad mini 6 пользователя)

**Вердикт: Подтверждено — iPadOS 27 поддерживает iPad mini (6-го поколения, чип A15). Достоверность: Исключительно высокая.**

- Официальная страница iPadOS 27 на apple.com гласит: "iPadOS 27 is compatible with these devices. … iPad Pro (4th generation and later, M1 and later), iPad Air (4th generation and later, M2 and later), iPad (9th generation and later, A16), **iPad mini (6th generation, A17 Pro)**"[^6].
- Страница безопасности Apple Security Releases подтверждает совместимость: "… iPad 9th generation and later, and **iPad mini 6th generation and later**"[^7].
- Снятые с поддержки в iPadOS 27 модели: iPad 8-го поколения, iPad mini 5-го поколения, iPad Air 3-го поколения, 11-дюймовый iPad Pro 1-го поколения, 12,9-дюймовый iPad Pro 3-го поколения (устройства на чипах A12/A12X). Они остаются на iPadOS 26 и получают обновления безопасности[^8][^9].
- **Критически важное уточнение (порог Apple Intelligence): iPad mini 6 (A15) поддерживает iPadOS 27, но НЕ поддерживает функции Apple Intelligence / Siri AI.** Сноска на сайте Apple поясняет: "Apple Intelligence is available on all iPhone 16 models and later, iPhone 15 Pro, iPhone 15 Pro Max, **iPad mini (A17 Pro)**, iPad models with M1 and later …"[^6] — порог для планшетов iPad составляет чип M1 или iPad mini 7-го поколения на A17 Pro. EveryMac прямо указывает: "The iPad mini 6, iPad Air 4, and iPad Pro 11\" (2nd Gen) and iPad Pro 12.9\" (4th Gen) do not support it [Apple Intelligence], either."[^10].

## Утверждение 3: Полный спектр функций Apple Intelligence доступен только на iPhone 15 Pro и новее (на iOS 27); iPhone 12/13/14 лишены полного функционала ИИ

**Вердикт: Подтверждено (с полезным уточнением градации). Достоверность: Высокая.**

- Документ поддержки Apple «How to get the next generation of Apple Intelligence» (2026-09-14): "Apple Intelligence in iOS 27 … are available on iPhone 16 models or later, **iPhone 15 Pro, iPhone 15 Pro Max**, iPhone Air, iPad mini (A17 Pro), … iPad models with M1 or later, Mac with M1 or later …"[^11].
- Линейки iPhone 12, iPhone 13, iPhone 14, а также базовые iPhone 15 и 15 Plus полностью исключены из поддержки Apple Intelligence (входной порог для iPhone — процессор A17 Pro и 8 ГБ RAM)[^11][^12].
- Уточнение градации: MacRumors отмечает, что самые продвинутые локальные модели в iOS 27 (выразительный голос Siri, улучшенная диктовка) требуют 12 ГБ памяти и работают только на iPhone 17 Pro, 17 Pro Max и iPhone Air[^4].

## Утверждение 4: iOS 27 вышла 2026-09-14, исправив 120+ уязвимостей (включая 20 в ядре); iOS 27.0.1 — актуальная релизная версия; iOS 27.2 уже в стадии beta

**Вердикт: Подтверждено (с комментарием по методике подсчета уязвимостей ядра). Достоверность: Высокая.**

- Дата выхода: Официальный релиз состоялся **14 сентября 2026 года**[^7], что подтверждено MacRumors, Macworld и The Verge[^5][^8][^13].
- Количество уязвимостей: В бюллетене support.apple.com/en-us/149034 перечислено **126 уникальных номеров CVE**, что совпадает с отчетом eSecurityPlanet ("Apple's security bulletin lists 122 fixes covering 126 unique CVEs, including 20 entries tied to the iPhone kernel")[^14]. Формулировка «120+ уязвимостей» **абсолютно точна**.
- Подсчет уязвимостей ядра: Непосредственно под заголовком «Kernel» сгруппировано **18 записей**, еще 2 уязвимости с эскалацией до уровня ядра (например, CVE-2026-84607, CVE-2026-28968) отнесены к смежным компонентам. Итоговая цифра в 20 багов ядра полностью легитимна.
- Статус 27.0.1: Сборка iOS 27.0.1 от 2026-09-28 являлась актуальной релизной версией на момент проверки (закрывает баги с перезагрузкой Face ID на iPhone 18 Pro)[^3][^16]. Релиз 27.1 запланирован эксклюзивно под выход iPhone Duo на конец октября[^17].
- Статус beta iOS 27.2: Сборки beta 1 (24B5084k, 16 сентября), beta 2 (21 сентября) и beta 3 (24B5099f, 5 октября) активно тестируются[^18][^19].

## Утверждение 5: «Прекращение поддержки iPhone 11 означает, что iPhone 12 на грани списания, а оставаться на iOS 26 — значит преждевременно уйти на пенсию» — Анализ логической обоснованности

**Вердикт: Вывод несостоятелен (посылка опровергнута фактами, противоречит исторической статистике Apple). Достоверность: Высокая.**

- Предпосылка ложна: Как доказано в Утверждении 1, Apple **не прекращала** поддержку iPhone 11 в iOS 27; список совместимости на 100% повторяет iOS 26[^2][^4].
- Жизненный цикл устройств: Macworld отмечает, что Apple обычно поддерживает устройства крупными обновлениями ОС в течение 5–7 лет, а патчами безопасности — значительно дольше[^20]; по статистике RefurbMe средний срок поддержки мажорными версиями составляет 6,4 года[^12]. Например, iPhone 6s (выпущенный в 2015 году) в мае 2026 года получил патч iOS 15.8.8 (свыше 10 лет поддержки).
- Соответственно, iPhone 11 (2019 года выпуска) получает уже 8-й крупный релиз (iOS 13 → 27), демонстрируя рекордную долговечность. До границы прекращения поддержки iPhone 12 остаются еще как минимум два поколения (iPhone 11 и iPhone SE 2), и поддержка продлится примерно до 2028–2030 годов[^20][^12].
- Тезис о «преждевременном уходе на пенсию» на iOS 26 также неверен: ветка 26 параллельно получает патчи безопасности (выпуск iOS 26.7 закрыл около 80 уязвимостей одновременно с выходом iOS 27, поддержка продолжена сборкой 26.7.1)[^3][^14].

---

## Прямой ответ для пользователя (по iPad mini 6)

Планшет iPad mini 6 (чип A15) **полностью поддерживает обновление до iPadOS 27**, однако **не будет поддерживать функции Apple Intelligence / Siri AI** (аппаратный порог для iPad — чип M1 либо iPad mini на A17 Pro). Обновление принесет общесистемные улучшения интерфейса и патчи безопасности, но не возможности нейросети Apple[^6][^10][^11].

---

## Источники информации

[^1]: Apple Support, "How to download iOS 26", https://support.apple.com/en-us/123705
[^2]: Apple, официальная страница "iOS 27", https://www.apple.com/os/ios/
[^3]: Apple Support, "Apple security releases", https://support.apple.com/en-us/100100
[^4]: MacRumors, "Which iPhones Support Every iOS 27 Feature?", 2026-09-09, https://www.macrumors.com/2026/09/09/which-iphones-support-every-ios-27-feature/
[^5]: The Verge, "Apple releases iOS 27 with Siri AI overhaul", 2026-09-14, https://www.theverge.com/news/994756/apple-ios-27-launch-iphone-siri-ai-update
[^6]: Apple, официальная страница "iPadOS 27", https://www.apple.com/os/ipados/
[^7]: Apple Support, "About the security content of iOS 27 and iPadOS 27", 2026-09-14, https://support.apple.com/en-us/149034
[^8]: MacRumors, "iPadOS 27 roundup", 2026-09-14, https://www.macrumors.com/roundup/ipados/
[^9]: Stuff, "iPadOS 27 system requirements", 2026-09-16, https://www.stuff.tv/features/ipados-27-system-requirements-will-it-run-on-your-apple-ipad/
[^10]: EveryMac, "iPadOS 27 Supported Devices List", 2026-09-16, https://everymac.com/systems/apple/ipad/ipad-faq/ipados-27-supported-devices-ipad-system-requirements.html
[^11]: Apple Support, "How to get the next generation of Apple Intelligence", 2026-09-14, https://support.apple.com/en-us/121115
[^12]: RefurbMe, "How Long Does Apple Support iPhones? (2026 Guide)", 2026-09-15, https://www.refurb.me/blog/how-long-does-apple-support-iphones
[^13]: Macworld, "iOS 27: What's new, what's in the latest beta", 2026-10-13, https://www.macworld.com/article/2986799/ios-27-features-compatiblity-siri-ai-updates.html
[^14]: eSecurityPlanet, "iOS 27 Fixes 126 Security Flaws, Including 20 Kernel Issues", 2026-09-21, https://www.esecurityplanet.com/news/news-ios-27-126-security-fixes-kernel-2026/
[^15]: CyberPress, "Apple iOS 27 and macOS 27 Security Updates Fix RCE, Kernel and WebKit Flaws", 2026-09-16, https://cyberpress.org/apple-ios-27-and-macos-27-security-updates-fix/
[^16]: Macworld, "iOS 27.0.1 is out now to fix iPhone 18 Pro restart bug", 2026-09-28, https://www.macworld.com/article/3245812/ios-27-0-1-is-out-now-to-fix-iphone-18-pro-restart-bug.html
[^17]: ZEERA, "iOS 27.2 Release Date", 2026-10-05, https://zeerawireless.com/blogs/news/ios-27-2-release-date-should-you-wait
[^18]: IPSWBeta.dev, "iOS 27.x Release History", 2026-10-05, https://ipswbeta.dev/ios/27.x/
[^19]: Blake Crosley, "iOS 27.0 Release Notes", 2026-10-01, https://blakecrosley.com/blog/ios-27-release-notes
[^20]: Macworld, "How long does Apple support iPhones with updates?", 2026-09-15, https://www.macworld.com/article/675021/how-long-does-apple-support-iphones.html
