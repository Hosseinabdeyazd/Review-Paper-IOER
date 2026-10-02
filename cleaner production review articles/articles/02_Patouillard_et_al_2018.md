# JCP-02 — Patouillard et al. (2018)

[بازگشت به فهرست](../README.md) · [درس‌ها و اقدام‌ها](../LESSONS_AND_ACTIONS.md) · [ساختار پیشنهادی مقاله خودمان](../PROPOSED_MANUSCRIPT_STRUCTURE.md)

## 1. مشخصات و حدود بررسی

| مشخصه | مقدار |
|---|---|
| عنوان | Critical review and practical recommendations to integrate the spatial dimension into life cycle assessment |
| نویسندگان | Laure Patouillard; Cecile Bulle; Cecile Querleu; Dominique Maxime; Philippe Osset; Manuele Margni |
| ژورنال | Journal of Cleaner Production |
| سال، جلد، صفحات | 2018; 177; 398–412 |
| DOI | [10.1016/j.jclepro.2017.12.192](https://doi.org/10.1016/j.jclepro.2017.12.192) |
| نوع | Review؛ در عنوان: critical review |
| منبع بررسی | PDF ارائه‌شده توسط کاربر: `1-s2.0-S0959652617331827-main.pdf`، 15 صفحه |
| تاریخ یادداشت | 2026-10-02 |
| وضعیت | متن کامل بررسی شد؛ درس‌ها ثبت شده‌اند؛ پیشنهادهای جدید هنوز در فایل‌های اصلی پروژه اعمال نشده‌اند |
| نقش برای پروژه | منبع مستقیم برای spatial LCA، GIS، spatial scale، spatial variability، regionalization/spatialization و پیوند آن‌ها با uncertainty |

شماره صفحات زیر، صفحات چاپی ژورنال 398–412 هستند.

## 2. چیزی که باید به خاطر بسپاریم

این مقاله فقط یک فهرست از روش‌های GIS/LCA نیست. منطق اصلی آن این است:

**زبان مشترک بساز → مسئله‌های مکانی را به سؤال‌های مشخص بشکن → رویکردهای موجود را برای هر سؤال طبقه‌بندی کن → آن‌ها را با معیارهای روشن ارزیابی کن → توصیه‌های کوتاه‌مدت و بلندمدت بساز → در پایان یک منطق تصمیم‌گیری عملی ارائه کن.**

برای مرور خودمان، مهم‌ترین درس این است که «مقیاس مکانی» نباید فقط یک ستون توصیفی باشد. باید بررسی کنیم هنگام انتقال اطلاعات بین مراحل و مقیاس‌ها، چه چیزی از مکان، تفکیک مکانی و عدم‌قطعیت حفظ، تجمیع، تغییر یا حذف می‌شود.

## 3. ساختار واقعی مقاله

| بخش | کارکرد |
|---|---|
| 1. Introduction | توضیح می‌دهد چرا LCA site-generic می‌تواند گمراه‌کننده باشد؛ spatial variability را از uncertainty جدا می‌کند؛ خلأ زبان مشترک و چارچوب را معرفی می‌کند؛ سه هدف روشن می‌سازد. |
| 2. Methods | سه کار را جدا می‌کند: مرور ادبیات و تعریف اصطلاحات؛ ارزیابی انتقادی رویکردها؛ تولید توصیه‌های عملی. |
| 2.1 Literature review | ابتدا terminology، سپس recommendations، سپس approaches را استخراج می‌کند. |
| 2.2 Critical analysis | هر approach را با سه معیار relevance، level of development و level of operationalization ارزیابی می‌کند. |
| 2.3 Practical recommendations | توصیه‌ها را برای stakeholderهای مختلف و در دو افق short-term و long-term می‌سازد. |
| 3. Results and discussion | 75 منبع، 33 recommendation و 37 approach را گزارش می‌کند؛ سپس تحلیل را حول مسائل مشخص مکانی در مراحل LCA سازمان می‌دهد. |
| 3.2 | هفت مسئله: G&S، inventory regionalization، inventory spatialization، regionalized impact calculation، impact regionalization، interpretation، software. |
| 3.3 | توصیه‌های عملی و یک decision-support diagram تکرارشونده برای regionalization/spatialization ارائه می‌کند. |
| 4. Conclusion | بر زبان مشترک، موانع، توصیه‌ها و نیاز به ابزارهای uncertainty-contribution برای آینده تأکید می‌کند. |

**درس ساختاری:** Results به‌جای اینکه بر اساس مقاله‌ها یا فناوری‌ها چیده شود، بر اساس «سؤال‌هایی که کاربر/مدل باید حل کند» سازمان یافته است.

## 4. دفتر شواهد مقاله

### E10 — spatial variability و uncertainty یک چیز نیستند

**شاهد مقاله:** در مقدمه، variability به تغییرات واقعی موجود در جهان اشاره می‌کند، در حالی که uncertainty به کمبود شناخت درباره واقعیت مربوط است. مقاله استدلال می‌کند که توصیف مکانی نماینده‌تر می‌تواند uncertainty ناشی از کمبود اطلاعات درباره مکان را کاهش دهد. [§1، ص. 399]

**برداشت ما:** در پروژه خودمان نباید هر تفاوت مکانی بین ساختمان‌ها، محله‌ها یا مناطق را «عدم‌قطعیت» بنامیم. تغییرپذیری واقعی می‌تواند منبعی باشد که اگر در مدل تجمیع یا ناشناخته شود، عدم‌قطعیت در برآورد ایجاد کند.

### E11 — regionalization و spatialization دو عملیات متفاوت‌اند

**شاهد مقاله:**  
- Inventory regionalization = بهبود geographic representativeness داده‌های inventory برای یک منطقه.  
- Inventory spatialization = نسبت‌دادن موقعیت مکانی به elementary flow تا بتوان آن را با characterization factor منطقه‌ای تطبیق داد. [§2.1.1، ص. 400]

**برداشت ما:** در زنجیره خودمان نیز «دقیق‌ترکردن ویژگی یک ساختمان/آرکی‌تایپ برای یک منطقه» با «دادن مختصات یا واحد مکانی به یک خروجی» یکسان نیست. این دو باید جدا کدگذاری شوند.

### E12 — سطح تفکیک inventory و impact لزوماً نباید یکی باشد

**شاهد مقاله:** نویسندگان تأکید می‌کنند سطح regionalization در inventory به variability در technosphere مربوط است، در حالی که سطح regionalization impact به variability در ecosphere مربوط است؛ بنابراین یکسان‌کردن اجباری این دو سطح می‌تواند نامناسب باشد. [§3.2.2.4، ص. 403]

**برداشت ما:** در پروژه ما نیز grain مناسب برای GeoAI، material stock، stock dynamics و LCA ممکن است متفاوت باشد. «همه چیز در بالاترین resolution» الزاماً بهترین طراحی نیست.

### E13 — افزایش aggregation می‌تواند uncertainty مکانی را بیشتر کند

**شاهد مقاله:** برای regionalized characterization factors، دو منبع از هم جدا می‌شوند: basic uncertainty در native resolution و uncertainty ناشی از spatial variability هنگام aggregation. مقاله می‌گوید هرچه CF بیشتر aggregate شود، uncertainty ناشی از spatial variability بیشتر می‌شود. [§3.2.5.2، ص. 405]

**برداشت ما:** گذار building → block → neighbourhood → city نباید صرفاً تغییر مقیاس توصیفی تلقی شود. باید ثبت کنیم aggregation چه اطلاعاتی را فشرده می‌کند و آیا اثر آن بر uncertainty ارزیابی شده است.

### E14 — impact hotspot با uncertainty hotspot یکی نیست

**شاهد مقاله:** در بحث توصیه‌ها، نویسندگان صریحاً می‌گویند بزرگ‌ترین contributors به impact الزاماً بزرگ‌ترین contributors به uncertainty نیستند. در بلندمدت، اولویت regionalization/spatialization باید بر uncertainty contribution analysis تکیه کند، نه صرفاً impact contribution analysis. [§3.3.3، ص. 410]

**برداشت ما:** برای پروژه خودمان، مرحله یا پارامتری که بیشترین اثر محیط‌زیستی را دارد لزوماً همان جایی نیست که بیشترین عدم‌قطعیت تصمیم از آن می‌آید.

### E15 — GIS فقط ابزار نمایش نیست؛ بخشی از محاسبه و matching است

**شاهد مقاله:** GIS می‌تواند برای نسبت‌دادن موقعیت به elementary flows، overlap بین مناطق inventory و مناطق characterization factor، و محاسبه regionalized impacts استفاده شود. [§§3.2.3–3.2.5، صص. 404–406]

**برداشت ما:** اگر در ادبیات GeoAI/GIS فقط map visualization وجود داشته باشد، آن را با spatially explicit propagation یا spatial matching یکی نگیریم.

### E16 — mismatched spatial resolutions خود یک مسئله روش‌شناختی است

**شاهد مقاله:** مقاله به‌طور مکرر بر اختلاف resolution بین inventory و LCIA تأکید می‌کند و روش‌هایی برای matching آن‌ها معرفی می‌کند. برخی روش‌ها از surface-weighted overlap استفاده می‌کنند، که خود بر فرض توزیع یکنواخت فعالیت در ناحیه overlap تکیه دارد. [§3.2.4، صص. 404–405]

**برداشت ما:** در استخراج داده، باید هم source resolution و هم target resolution و هم روش تبدیل بین آن‌ها را ثبت کنیم. تغییر مقیاس بدون بیان قاعده تبدیل، یک link ناقص است.

### E17 — «فاین‌تر» همیشه بهتر نیست؛ resolution باید تابع هدف باشد

**شاهد مقاله:** سطح جزئیات مناسب به impact category، هدف مطالعه، زمان، داده و منابع بستگی دارد. native resolution هر impact category نیز متفاوت است. [§§3.2.5، 3.3، صص. 405–409]

**برداشت ما:** در پروژه ما بهتر است به‌جای فرض «higher resolution = better»، سؤال کنیم چه resolutionای برای کدام تصمیم و کدام مرحله کافی است و چه شواهدی برای آن وجود دارد.

### E18 — review از سؤال‌ها به توصیه‌ها می‌رسد

**شاهد مقاله:** 37 approach براساس main question دسته‌بندی و سپس با relevance، development و operationalization ارزیابی می‌شوند. بعد توصیه‌های short-term و long-term برای practitioner، database developer، LCIA method developer، software developer و researcher استخراج می‌شود. [§§2.2–2.3، ص. 400]

**برداشت ما:** برای Discussion خودمان نیز می‌توان recommendationها را بر اساس «چه کسی باید چه تغییری بدهد» و «الان قابل‌اجراست یا نیازمند توسعه آینده است» تفکیک کرد.

### E19 — تصمیم‌گیری iterative و مبتنی بر uncertainty

**شاهد مقاله:** Figure 1 یک فرایند iterative پیشنهاد می‌کند: ابتدا بررسی شود spatial uncertainty در سطح قابل‌قبول است یا نه؛ سپس regionalization و spatialization انجام شوند و فرایند دوباره تکرار شود تا uncertainty به حد قابل‌قبول برسد یا داده/منابع اجازه بهبود بیشتر ندهند. [§3.3.2 و Fig. 1، صص. 406–410]

**برداشت ما:** برای چارچوب پیشنهادی خودمان، می‌توان به‌جای یک pipeline یک‌طرفه، منطق بازخوردی «آیا uncertainty برای تصمیم قابل‌قبول است؟ اگر نه، کدام مرحله باید بهبود یابد؟» را بررسی کرد. این فعلاً پیشنهاد مفهومی است، نه نتیجه‌ای اثبات‌شده برای زنجیره ما.

## 5. اصلاح مهم در تعریف uncertainty خودمان

این مقاله یک نکته مهم برای توضیح قبلی ما دارد:

**Spatial variability ≠ uncertainty.**

مثلاً اگر دو ساختمان واقعاً ترکیب مصالح متفاوتی دارند، این تفاوت واقعی یک variability است. اگر ما ندانیم ساختمان موردنظر دقیقاً چه ترکیبی دارد، یا variability واقعی را با یک میانگین کلی پنهان کنیم، uncertainty وارد برآورد می‌شود.

بنابراین در codebook بهتر است حداقل سه لایه از هم جدا شوند:

1. **Variability:** تفاوت واقعی در سیستم، مانند تفاوت مکانی یا زمانی.
2. **Uncertainty:** کمبود شناخت، داده، نمایندگی، انتخاب یا ساختار مدل.
3. **Representation/aggregation:** عملیاتی که ممکن است variability را صریح نگه دارد یا آن را فشرده و به uncertainty نتیجه تبدیل کند.

این تفکیک با تصمیم A02–A03 سازگار است و آن را دقیق‌تر می‌کند. با این حال، مقاله JCP-03 اصطلاح parameter uncertainty را به‌صورت گسترده‌تری به‌کار می‌برد و variability را نیز در آن می‌گنجاند. بنابراین در مرور خودمان باید **اصطلاح اصلی هر منبع را حفظ کنیم و harmonization را جدا انجام دهیم**؛ نباید وانمود کنیم ادبیات یک تعریف واحد دارد.

## 6. پیشنهاد برای فرم استخراج

این موارد پیشنهاد ما هستند، نه فیلدهای مقاله Patouillard:

| فیلد پیشنهادی | پرسش |
|---|---|
| `spatial_phenomenon` | variability واقعی است، uncertainty شناختی است یا هر دو مطرح‌اند؟ |
| `spatial_operation` | regionalization، spatialization، aggregation، disaggregation، matching یا none؟ |
| `source_spatial_grain` | grain/واحد مکانی ورودی چیست؟ |
| `target_spatial_grain` | خروجی در چه grainی استفاده می‌شود؟ |
| `spatial_coverage` | extent یا geographic validity چیست؟ |
| `native_resolution` | اگر وجود دارد، resolution طبیعی/اصلی روش چیست؟ |
| `scale_transition_rule` | aggregation/interpolation/overlap/archetype/other چگونه انجام شده؟ |
| `spatial_information_loss` | آیا از دست‌رفتن اطلاعات مکانی گزارش یا قابل‌استنتاج مستقیم است؟ |
| `spatial_uncertainty_assessed` | آیا uncertainty ناشی از مکان/aggregation سنجیده شده؟ |
| `uncertainty_contribution` | آیا سهم این منبع در uncertainty خروجی ارزیابی شده؟ |
| `impact_contribution` | آیا فقط سهم در impact بررسی شده؟ |
| `decision_use` | آیا resolution/uncertainty به تصمیم یا اولویت جمع‌آوری داده مرتبط شده؟ |

**احتیاط:** نبود تحلیل uncertainty contribution را نباید با صفر بودن سهم عدم‌قطعیت یکی دانست.

## 7. چه چیزی برای ساختار مقاله خودمان تغییر می‌دهد؟

### 7.1 بخش Methods
یک glossary کوتاه و عملیاتی برای اصطلاحات spatial لازم است: grain، extent/coverage، regionalization، spatialization، aggregation/disaggregation و scale transition.

### 7.2 بخش Evidence Landscape
فقط «سطح مطالعه: building/city» کافی نیست. باید source grain، target grain و نوع تبدیل بین آن‌ها استخراج شود.

### 7.3 بخش Uncertainty Across Links and Scales
این بخش باید حداقل سه زیرموضوع داشته باشد:
- انتقال اطلاعات بین مراحل؛
- گذار مقیاس و aggregation/disaggregation؛
- spatial variability و uncertainty ناشی از representation/location.

### 7.4 بخش Discussion
یک تفاوت مهم باید حفظ شود:
**impact importance ≠ uncertainty importance.**
بنابراین research gaps و اولویت‌های بهبود داده باید، هرجا شواهد اجازه می‌دهد، براساس uncertainty contribution بحث شوند.

### 7.5 چارچوب پیشنهادی آینده
منطق iterative این مقاله می‌تواند برای چارچوب ما الهام‌بخش باشد:
**Decision requirement → current uncertainty → identify dominant source/link → improve data/model only where needed → re-evaluate.**

این adaptation باید به‌عنوان پیشنهاد ما معرفی شود و نباید به‌عنوان framework آزموده‌شده برای GeoAI-material-stock chain به مقاله Patouillard نسبت داده شود.

## 8. چه چیزهایی را کپی نکنیم؟

- سیستم امتیازدهی +/− مقاله را بدون rubric و آزمون reliability خودمان کپی نکنیم.
- ادعاهای مربوط به availability یا maturity ابزارهای 2018 را به وضعیت امروز تعمیم ندهیم.
- «regionalization reduces uncertainty» را به قانون عمومی تبدیل نکنیم؛ مقاله خود نیز trade-off داده/هزینه/هدف را برجسته می‌کند.
- fine resolution را خودکار برابر با accuracy بیشتر فرض نکنیم.
- spatial variability را با uncertainty مترادف نکنیم.
- GIS visualization را با spatially explicit calculation یا uncertainty propagation یکی نگیریم.
- نبود approach در مرور 2018 را بدون جست‌وجوی امروز به‌عنوان شکاف فعلی گزارش نکنیم.

## 9. اقدام‌های پیشنهادی برای پروژه

| شناسه | اقدام | وضعیت اولیه |
|---|---|---|
| A13 | variability واقعی را از uncertainty شناختی/مدلی در codebook جدا کنیم، در حالی که اصطلاح اصلی هر مطالعه حفظ شود | Proposed |
| A14 | regionalization، spatialization، aggregation/disaggregation و spatial matching را به‌صورت عملیات جداگانه استخراج کنیم | Proposed |
| A15 | برای هر link، source grain، target grain، spatial coverage و rule گذار مقیاس را ثبت کنیم | Proposed |
| A16 | impact contribution را از uncertainty contribution جدا کنیم و از اولی، دومی را استنباط نکنیم | Proposed |
| A17 | اثر aggregation/resolution change بر uncertainty را فقط با شواهد و مبنای مقایسه ثبت کنیم | Proposed |
| A18 | در بخش cross-link synthesis، زیرتحلیل مستقل برای scale transition و spatial information loss ایجاد کنیم | Proposed |
| A19 | در Discussion، توصیه‌ها را در صورت کفایت شواهد بر اساس stakeholder و short-term/long-term تفکیک کنیم | Proposed |
| A20 | منطق iterative «uncertainty acceptable? → improve dominant link → re-evaluate» را به‌عنوان گزینه framework آینده بررسی کنیم | Proposed |

## 10. مقایسه با JCP-03

دو مقاله مکمل‌اند:

- **JCP-03** می‌پرسد منابع عدم‌قطعیت چیستند و چگونه میان مدل‌های متصل propagate می‌شوند.
- **JCP-02** نشان می‌دهد وقتی موضوع مکانی است، باید بین variability، representativeness، location، resolution و aggregation تمایز بگذاریم.

مهم‌ترین نتیجه ترکیبی برای ما این است:

**در هر link فقط نباید بپرسیم uncertainty منتقل شد یا نه؛ باید بپرسیم اطلاعات مکانی در چه grain و coverageی منتقل شد، چه transformationی روی آن انجام شد، و آیا این transformation عدم‌قطعیت نتیجه را تغییر داد یا فقط شکل نمایش اطلاعات را عوض کرد.**

## 11. وضعیت تصمیم‌ها

A13–A20 در این مرحله فقط `Proposed` هستند. ثبت آن‌ها در این پوشه به معنی اعمال‌شدن در README اصلی، queryها، codebook یا manuscript نیست.

**کار بعدی پیشنهادی:** مقاله بعدی spatial/GIS-LCA را بخوانیم تا ببینیم این درس‌ها در یک منبع مستقل تکرار، تکمیل یا نقض می‌شوند.
