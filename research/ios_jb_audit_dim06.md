# Аудит отчета о джейлбрейке iOS (Измерение 06): Механизмы безопасности A14/A15, причины задержки джейлбрейка и портируемость цепочки Calif iOS 27.0.1

[Русский](ios_jb_audit_dim06.md) | [中文版](ios_jb_audit_dim06-zh.md)

- Дата проверки: 2026-10-17 (UTC)
- Методология: 26 независимых поисковых запросов; перекрестное сопоставление официальной документации Apple, примечаний к релизам утилит джейлбрейка и публикаций независимых СМИ.
- Проверяемое утверждение (из исходного отчета): «Аппаратная защита меняется с каждым поколением, поэтому цепочка джейлбрейка Calif iOS 27.0.1 (показанная на iPhone 18 Pro / T8160) с высокой вероятностью не адаптирована под A14/A15».
- Контекст устройств: iPhone 12 Pro Max (A14), iPad mini 6 (A15), оба работают под управлением iOS/iPadOS 26.1.

**Общий вердикт: Частично обосновано (PARTIAL PASS).** Тезис «аппаратная защита меняется с каждым поколением» верен (высокая достоверность); утверждение «с высокой вероятностью не адаптирована под A14/A15» является **логически правдоподобным, но не подтвержденным строгими доказательствами предположением**. Пока эксплойт Calif не раскрыт, ни одна сторона не может дать категоричный ответ. Более того, исторически перенос чисто программных эксплойтов с новых чипов на старые происходит регулярно, а отсутствие на старых чипах новых защит вроде MIE в некоторых фазах атаки даже упрощает эксплуатацию. Корректная формулировка: **«Адаптируемость неизвестна; в случае публикации для переноса потребуется закрыть пробелы в виде отсутствующих обходов PPL для A14 и SPTM для A15 на iOS 27»**.

---

## 0. Базовый фактологический слой

### 0.1 Демонстрация Calif iOS 27.0.1 реальна
**Вердикт: Подтверждено. Достоверность: Высокая.**

- 2026-10-16 компания Calif (Calif.io) в рамках вступительного доклада (Bruce Dang и Thai Duong) на Hexacon 2026 в Париже (организатор Synacktiv) показала живую работу непривязанного джейлбрейка на iPhone 18 Pro: после перезагрузки root-доступ восстановился автоматически, сессия SSH на порту 2222 вернула `uid=0`. Параметры тестового устройства: **iPhone19,2 / T8160 / iOS 27.0.1 build 24A446 / Darwin 27.0.0 (XNU 13432.2.10)**[^1][^2][^3].
- CyberSecurityNews (2026-10-16): "The uname output showed Darwin Kernel 27.0.0 built on XNU 13432.2.10 for the T8160 chip, with the model listed as iPhone19,2. The sw_vers command confirmed iOS 27.0.1, build 24A446"[^1].
- Уязвимости не раскрыты, номеров CVE нет, утилит нет; в рассылке Calif сказано: "Everything will be released in due time"[^4][^5].
- heise называет это первым untethered-джейлбрейком со времен iOS 9; в поиске цепочки применялись модели ИИ (Claude / Mythos)[^2][^6].

### 0.2 Временные маркеры
- iOS 27: релиз 2026-09-14, закрыто свыше 120 уязвимостей (включая 20 багов ядра)[^7][^1].
- iOS 27.0.1 (сборка 24A446): релиз 2026-09-28; iOS 27.1 находится в бета-тестировании[^8][^5].
- T8160 = A20 Pro (процессор iPhone 18 Pro / Pro Max / Duo, техпроцесс TSMC N2, архитектура ARMv9.3-A)[^9].

---

## Вопрос 1: Различия в механизмах безопасности A14/A15 (PAC / PPL / SPTM / MIE)

### 1.1 PAC (Pointer Authentication Codes)
**Вердикт: Дебютировал в A12, присутствует и на A14, и на A15. Достоверность: Высокая.**

- Анализ 8ksec: "In 2018, Apple shipped the **A12 Bionic** chip with Pointer Authentication Code (PAC). This made them the first in the industry to deploy this protection at scale."[^10]
- Соответственно, и на iPhone 12 Pro Max (A14), и на iPad mini 6 (A15) защита PAC включена; любая цепочка требует байпаса PAC или способов его обхода.

### 1.2 PPL (Page Protection Layer)
**Вердикт: Внедрен в 2017 году; процессор A14 по-прежнему защищен PPL (механизм APRR). Достоверность: Высокая.**

- Исследование arXiv:2510.09272: "Introduced in 2017, Apple designed PPL to deny user-space code modification after successful code signature verification… This PPL-trampoline is the only entry point to PPL"[^11].
- В том же источнике: "**SPTM has replaced the PPL mitigation on A15 / M2 or newer SoCs**" — то есть **A14 не поддерживает SPTM и остается в лагере PPL**[^11].

### 1.3 SPTM / TXM (Secure Page Table Monitor / Trusted Execution Monitor)
**Вердикт: Аппаратно поддерживается только на чипах A15/M2 и новее, придя на смену PPL; программно внедрен начиная с iOS 17.0b1. Достоверность: Высокая (официальная документация Apple).**

- Руководство Apple Platform Security: "Secure Page Table Monitor (SPTM) is supported in the **A15 or later and M2 or later** SOCs and **replaces Page Protection Layer** on supported platforms."[^12]
- Официальное пояснение: "In the A15 or later and M2 or later SOCs, SPTM (in combination with TXM) replaces the PPL, providing a smaller attack surface that doesn't rely on trust of the kernel, even during early boot. SPTM relies on new silicon primitives that are an evolution of the Fast Permission Restrictions that PPL utilizes, and are available only on the processors listed"[^13].
- Хронология: "SPTM was first introduced in iOS 17.0b1, and has gradually replaced PPL on more and more devices… if you look e.g. at A15 on iOS 15 or 16, you will see PPL, whereas in 17 or later, you will see SPTM." (Nicolás Alvarez)[^14].

**Ключевой вывод**: В отчете A14 и A15 объединены, но на уровне защиты страниц они принадлежат к разным эпохам:
- iPhone 12 Pro Max (A14) = PAC + **PPL** (нет аппаратного модуля SPTM);
- iPad mini 6 (A15) = PAC + **SPTM/TXM** (начиная с iOS 17).
Для переноса эксплойта на эти устройства требуются принципиально разные типы байпасов.

### 1.4 MIE (Memory Integrity Enforcement)
**Вердикт: Тезис отчета требует исправления: MIE появился только в чипах A19/A19 Pro (iOS 26) и M5 (macOS 26), а не «начиная с A17/M-серии»; на A14/A15 защита MIE отсутствует. Достоверность: Высокая.**

- Блог Apple Security Research (2025-09-09): "Memory Integrity Enforcement (MIE) is the culmination of an unprecedented design and engineering effort… the most significant upgrade to memory safety in the history of consumer operating systems."[^15]
- TidBITS Talk: "MIE is currently available **only in the A19 and A19 Pro chips** used in the iPhone 17 and iPhone Air."[^16]
- sigreturn.com: "Memory Integrity Enforcement… ships on the **A19 and A19 Pro from iOS 26** and on the **M5 from macOS 26**."[^17]
- Архитектура MIE объединяет аллокатор kalloc_type / xzone malloc, синхронный аппаратный режим EMTE и контроль Tag Confidentiality, вызывая аппаратную панику при выходе за границы или Use-After-Free[^10].
- Чипы A17 Pro, A18, M1–M4 защиты MIE не имеют. В процессорах A20 Pro / T8160 она гарантированно сохранена и развита[^18][^19].

---

## Вопрос 2: Причины задержки джейлбрейка на A14+ — феномен «на A12/A13 проще»

### 2.1 Подтверждение факта
**Вердикт: Подтверждено. Достоверность: Высокая.**

- Сайт Dopamine: "Supported on iOS 15.0 - 17.3.1 (A14 - A17 / M1 - M2) · Supported on iOS 15.0 - 18.7.1 and 26.0 - 26.0.1 (A8 - A13)"[^20].
- Примечания к Dopamine 3.0 (2026-08-07):
  - "Add Titan PPL/SPTM bypass by @alfiecg24, introduces support for all devices running 16.5.1 - 17.3.1"
  - "Add momentarius PPL bypass by @staturnzz and @TheRealClarity, introduces support for **A12/A13** devices running **16.6 - 18.7.1, 26.0 - 26.0.1**"
  - "obviously only works up to 17.3.1 on real devices **due to lack of an SPTM bypass on >=17.4**"[^21].
- До версии 2026-10-17 устройства **A14/A15 не имеют публичного джейлбрейка ни на одном релизном билде iOS 26**, тогда как A12/A13 поддерживают 26.0.1[^7].

### 2.2 Анализ причин
**(a) Отсутствие обхода SPTM для версий ≥17.4 — непреодолимый барьер для A15+ (подтверждено).**  
Все устройства с чипом A15+ упираются в потолок 17.3.1, так как публичного обхода SPTM для более новых версий нет[^21][^23].

**(b) Эксплойт momentarius — это обход PPL, реализованный только для A12/A13 (подтверждено).**  
Почему он не поддерживает A14 (также использующий PPL), разработчики не уточняли. Анализ коммитов XNU показывает, что между iOS 17.0 и 17.5.1 Apple скрыто ужесточила PPL (добавив подсистему `pmap_cs_runtime` и проверки трапов PPL), что закрыло вектор эксплуатации именно на A14[^24].

**(c) Уязвимость SecureROM usbliter8 существует только на A12/A13 (подтверждено).**  
- Документация usbliter8-fun: "There's a SecureROM bug… **It only supports A12 and A13**"[^25].
- Журнал Infosecurity: "**A14 and later chips appear to configure DART correctly in SecureROM, making the same route unexploitable.**"[^26].
- Начиная с A14 Apple корректно настроила IOMMU DART в коде SecureROM, закрыв DMA-переполнение. На iPhone 11 Pro (A13) благодаря usbliter8 энтузиасты смогли запустить привязанный джейлбрейк iOS 27.0 beta 2, что еще сильнее закрепило отрыв старых чипов[^28][^29].

**(d) Сравнение с историческими моделями.** Ситуация «A12/A13 опережают A14/A15» — временный аномальный феномен, вызванный совпадением двух факторов: доступностью PPL-байпаса momentarius строго под A12/A13 и появлением аппаратного бага usbliter8 только на этих чипах[^30].

---

## Вопрос 3: Прецеденты портирования с новых флагманов на старые устройства

**Вердикт: Перенос чисто программных цепочек между поколениями процессоров — историческая норма. Предположение отчета «демонстрация на новом чипе означает несовместимость со старыми» противоречит истории джейлбрейка.**

Примеры успешного портирования:
- Fugu14 (2021 год, untethered-цепочка iOS 14.3–14.5.1): изначально поддерживал все arm64e-устройства (iPhone XS и новее), охватывая A12, A13 и A14 единым кодом[^31].
- Fugu15 (2022 год): стартовал на iOS 15.4.1 для чипов A12+, успешно покрыв линейки iPhone XS, 11, 12, 12 Pro Max и 13[^32][^33].
- Dopamine 2.0 охватил устройства от A8 до A16 и M2, а эксплойт kfd успешно применялся на всей линейке вплоть до iPhone 14 Pro[^21][^34].
- Атака Operation Triangulation была специально спроектирована для охвата как старых, так и новых моделей iPhone с байпасом PAC[^35].

Непереносимы только аппаратные уязвимости (BootROM): checkm8 (A5–A11), usbliter8 (A12/A13)[^26][^36].

Аналитический вывод: **Перенос «с нового на старое» обычно проще, чем «со старого на новое»**, поскольку на старых чипах меньше защитных механизмов. В нашем случае на A14/A15 нет MIE; если цепочка Calif на A20 Pro преодолевает аппаратный монитор памяти MIE, то на A14/A15 эта стадия вовсе не потребуется, что повышает надежность эксплойта[^10][^16].

---

## Вопрос 4: Объем работ для портирования цепочки Calif на A14/A15

### 4.1 Известное и неизвестное
- Неизвестно: точный список уязвимостей, номера CVE, начальный вектор, механизмы персистентности и обхода SPTM/PAC[^1][^4].
- Авторитетный комментарий heise: «Сможет ли эта цепочка работать на старых чипах — неизвестно, **поскольку аппаратная защита меняется с каждым поколением**»[^19] — именно эта фраза послужила основой для тезиса исходного отчета.

### 4.2 Теоретическая декомпозиция трудозатрат
1. **Поиск смещений (offsets / patchfinding)**: тривиальная инженерная задача, решаемая автопатчерами вроде XPF в Dopamine[^21][^31].
2. **Обход PAC**: одинаков для A14 и A15 (оба поколения используют PAC)[^10].
3. **Обход SPTM для A15 (iPad mini 6)**: публичного обхода для iOS 27 нет, но чип A20 Pro также использует SPTM, следовательно, в цепочке Calif **уже есть решение для SPTM**, которое может подойти и для A15.
4. **Обход PPL для A14 (iPhone 12 Pro Max)**: требует реализации отдельного обхода PPL под iOS 27, которого в публичном доступе нет.
5. **Защита MIE**: на A14/A15 отсутствует, этот барьер преодолевать не нужно.
6. **Персистентность (untether)**: если механизм привязан к особенностям загрузчика T8160, перенос может оказаться невозможным.
7. **Версионный тупик пользователя**: устройства находятся на **iOS 26.1**, а цепочка написана под **27.0.1**. Окно подписания 27.0.1 стремительно закрывается[^37].

---

## Вопрос 5: Поддержка iOS/iPadOS 27 устройствами iPhone 12 Pro Max и iPad mini 6

**Вердикт: Оба устройства официально поддерживают iOS/iPadOS 27. Достоверность: Высокая.**

- В официальном списке поддерживаемых моделей iOS 27 значатся iPhone 12, iPhone 12 Pro и **iPhone 12 Pro Max** (минимальный порог — iPhone 11)[^41][^42][^43].
- iPadOS 27 официально поддерживает **iPad mini (6-го поколения)** (прекращена поддержка iPad 8, mini 5, Air 3)[^44][^45][^46].
- Важное напоминание: **функции Apple Intelligence на этих устройствах работать не будут** (требуется чип M1 или A17 Pro и новее)[^46][^47].

---

## Сводная таблица верификации

| Утверждение из отчета | Вердикт | Достоверность |
|---|---|---|
| Аппаратная защита меняется от поколения к поколению | ✅ Подтверждено (тезис heise + документация Apple Platform Security) | Высокая |
| Защита MIE появилась «после A17/M-серии» | ⚠️ Требует правки: MIE появилась в **A19/A19 Pro (iOS 26) и M5 (macOS 26)**; на A17/A18 и M1–M4 ее нет | Высокая |
| Джейлбрейк для A14/A15 задерживается (Dopamine ограничен 17.3.1) | ✅ Подтверждено; факт поддержки A12/A13 вплоть до 26.0.1 также верен | Высокая |
| Аномалия связана с наличием SPTM/PPL-байпасов и usbliter8 | ✅ Подтверждено официальными источниками | Высокая |
| Цепочка Calif «с высокой вероятностью не адаптирована под A14/A15» | ⚠️ **Предположение без достаточных доказательств**; корректно: статус неизвестен, при портировании понадобятся обходы PPL (для A14) и SPTM (для A15), однако отсутствие MIE облегчает задачу | Средняя (допустимо как предостережение, но не как доказанный факт) |
| iPhone 12 Pro Max и iPad mini 6 поддерживают iOS/iPadOS 27 | ✅ Подтверждено (без функций Apple Intelligence) | Высокая |

---

## Источники информации

[^1]: CyberSecurityNews, "iOS 27.0.1 Untethered Jailbreak Demonstrated on iPhone 18 Pro", 2026-10-16. https://cybersecuritynews.com/ios-27-0-1-jailbreak-demonstrated/
[^2]: GBHackers, "Researchers Demonstrate iOS 27.0.1 Untethered Jailbreak on iPhone 18 Pro", 2026-10-16. https://gbhackers.com/ios-27-0-1-untethered-jailbreak/
[^3]: Mallory, "Calif Demonstrates Reboot-Persistent iOS 27.0.1 Jailbreak on iPhone 18 Pro", 2026-10-16. https://mallory.ai/stories/01a144a5-33e9-786d-9d6a-311be6bd2189
[^4]: explainx.ai, "Calif.io Jailbreaks iOS 27.0.1 on iPhone 18 Pro: What Is Claimed vs. Verified", 2026-10-16. https://explainx.ai/blog/calif-io-ios-27-0-1-untethered-jailbreak-iphone-18-pro-hexacon-ai-claimed-vs-verified-2026
[^5]: Glitchwire, "Calif Demonstrates Untethered iOS 27.0.1 Jailbreak at Hexacon", 2026-10-16. https://glitchwire.com/news/calif-demonstrates-untethered-ios-2701-jailbreak-at-hexacon-hints-at-signal-and/
[^6]: Yahoo Tech / Decrypt, "Hackers Jailbreak iPhone 18 Pro on Stage, and It Survives a Reboot", 2026-10-16. https://tech.yahoo.com/cybersecurity/articles/hackers-jailbreak-iphone-18-pro-193604534.html
[^7]: TechEngage, "iOS Jailbreak History: Every Major Tool From 2007 to 2026", 2026-09-14. https://techengage.com/ios-jailbreaking-complete-history/
[^8]: ONE Jailbreak, "Calif Demos Untethered iOS 27.0.1 Jailbreak on iPhone 18 Pro", 2026-10-16. https://onejailbreak.com/blog/calif-demos-untethered-ios-27-0-1-jailbreak-on-iphone-18-pro/
[^9]: namu.wiki, "Apple Silicon/A series — A20 Pro (APL1Y01-T8160)", 2026-09-18. http://en.namu.wiki/w/Apple%20Silicon/A%20%EC%8B%9C%EB%A6%AC%EC%A6%88
[^10]: 8ksec, "Memory Integrity Enforcement (MIE) on iOS Deep Dive", 2026-01-27. https://www.8ksec.io/mie-deep-dive-kernel/
[^11]: arXiv:2510.09272, "XNU Kernel Security Research: PPL and SPTM", 2025-10-10. https://arxiv.org/html/2510.09272v1
[^12]: Apple Platform Security, "Apple SoC security", 2026-01-28. https://support.apple.com/guide/security/apple-soc-security-sec87716a080/web
[^13]: Apple Platform Security, "Operating system integrity", 2026-01-28. https://support.apple.com/guide/security/operating-system-integrity-sec8b776536b/web
[^14]: Nicolás Alvarez, "SPTM Deployment Timeline", 2025-06-22. https://social.treehouse.systems/@nicolas17/114727754975559614
[^15]: Apple Security Research, "Memory Integrity Enforcement", 2025-09-09. https://security.apple.com/blog/memory-integrity-enforcement/
[^16]: TidBITS Talk, "Memory Integrity Enforcement Bolsters iPhone Security", 2025-09-12. https://talk.tidbits.com/t/memory-integrity-enforcement-bolsters-iphone-security/31894
[^17]: sigreturn.com, "Apple internals: The security stack", 2026-06-21. https://sigreturn.com/blog/apple-security-stack/
[^18]: efani, "iPhone 18 Security Changes: MIE", 2026. https://www.linkedin.com/posts/efani_iphone18-apple-wwdc-activity-7502289026482139136-mOOB
[^19]: Pasquale Pillitteri, "Calif Unveils iPhone 18 Pro Jailbreak on iOS 27.0.1 at Hexacon", 2026-10-16. https://pasqualepillitteri.it/en/news/24540/jailbreak-iphone-18-pro-ios-27-calif-hexacon
[^20]: Официальный сайт Dopamine: https://ellekit.space/dopamine/
[^21]: The Apple Wiki, "Dopamine", 2026-10-12. https://theapplewiki.com/wiki/Dopamine
[^22]: iClarified, "Dopamine 3.0 Jailbreak Released With iOS 17.3.1 Support", 2026-08-07. https://www.iclarified.com/101697/dopamine-30-jailbreak-released-with-ios-1731-support-ios-26-on-a12a13
[^23]: ONE Jailbreak, "Dopamine 3.0 Jailbreak With iOS 26 Support", 2026-08-07. https://onejailbreak.com/blog/dopamine-3-0-jailbreak-out-with-ios-26-support/
[^24]: GitHub Somisomair/xnu-vm-map-cur-max-bug, "PPL hardening diffs", 2026-03-28. https://github.com/Somisomair/xnu-vm-map-cur-max-bug
[^25]: GitHub 34306/usbliter8-fun, "README", 2026-07-08. https://github.com/34306/usbliter8-fun/blob/main/README.md
[^26]: Infosecurity Magazine, "Unpatchable BootROM Flaw Impacts Apple A12, A13 Chips", 2026-06-22. https://www.infosecurity-magazine.com/news/apple-bootrom-exploit-a12-a13/
[^27]: Аналитический обзор хронологии usbliter8, 2026-09-21. https://post.smzdm.com/p/awwzz93k/
[^28]: CyberSecurityNews, "Booted Jailbroken iOS 27 iPhone 11 Pro", 2026-07-27. https://cybersecuritynews.com/booted-jailbroken-ios-27-iphone-11-pro/
[^29]: ONE Jailbreak, "usbliter8-fun: iOS 27 Jailbreak on iPhone 11 Pro", 2026-07-25. https://onejailbreak.com/blog/usbliter8-fun-ios-27-jailbreak-on-iphone-11-pro/
[^30]: Руководство по джейлбрейку по чипам, 2026-08-26. https://blog.csdn.net/gitblog_00466/article/details/164085296
[^31]: GitHub neoncloud/Fugu14_onlinebuild, 2021-10-27. https://github.com/neoncloud/Fugu14_onlinebuild
[^32]: Objective by the Sea v5, Linus Henze "Fugu15 Slides". https://objectivebythesea.org/v5/talks/OBTS_v5_lHenze.pdf
[^33]: The Apple Wiki, "Fugu15". https://theapplewiki.com/wiki/Fugu15
[^34]: iDevice Central, "KFD Exploit Compiled for iOS 15.5 – 16.5 (A12+)", 2023-07-31. https://idevicecentral.com/jailbreak-tools/download-kfd-jailbreak-exploit-ipa/
[^35]: Kaspersky Securelist, "Operation Triangulation: The last hardware mystery", 2023-12-27. https://securelist.com/operation-triangulation-the-last-hardware-mystery/111669/
[^36]: Belkasoft, "Unc0ver: What you should know". https://belkasoft.com/what_you_should_know_about_unc0ver
[^37]: iPhoneTweak, "Dopamine 3.0 rend iOS 26 enfin jailbreakable", 2026-08-08. https://iphonetweak.fr/2026/08/08/dopamine-3-0-rend-ios-26-enfin-jailbreakable-a12-a13-only
[^38]: Reddit r/jailbreak, "Calif team presented untethered iOS 27 jailbreak at Hexacon", 2026-10-16. https://www.reddit.com/r/jailbreak/comments/1x7dwzb/calif_team_presented_untethered_ios_27_jailbreak/
[^39]: Reddit r/jailbreak, "iPhone duo jailbreak", 2026-10-17. https://www.reddit.com/r/jailbreak/comments/1x7xmp8/iphone_duo_jailbreak/
[^40]: Видео Billy Ellis (@bellis1000) в X, 2026-10-16. https://x.com/bellis1000/status/2111028042495824337
[^41]: Apple Support, "iPhone models compatible with iOS 27". https://support.apple.com/guide/iphone/iphone-models-compatible-with-ios-27-iphe3fa5df43/ios
[^42]: Macworld, "Can your iPhone run iOS 27? Compatibility list", 2026-09-14. https://www.macworld.com/article/1811287/which-version-of-ios-can-my-iphone-run.html
[^43]: everymac, "iOS 27 Supported Devices List", 2026-09-20. https://everymac.com/systems/apple/iphone/iphone-faq/iphone-ios-27-supported-devices-features.html
[^44]: Tom's Guide, "iPadOS 27 review: Compatible iPads", 2026-09-15. https://www.tomsguide.com/computing/ipads/ipados-27-review
[^45]: Stuff, "iPadOS 27 system requirements", 2026-09-16. https://www.stuff.tv/features/ipados-27-system-requirements-will-it-run-on-your-apple-ipad/
[^46]: everymac, "iPadOS 27 Supported Devices List", 2026-09-16. https://everymac.com/systems/apple/ipad/ipad-faq/ipados-27-supported-devices-ipad-system-requirements.html
[^47]: Tapsmart, "Which devices are compatible with iOS 27, iPadOS 27, and more?", 2026-09-18. https://www.tapsmart.com/tips-and-tricks/2026-device-compatibility-guide/
