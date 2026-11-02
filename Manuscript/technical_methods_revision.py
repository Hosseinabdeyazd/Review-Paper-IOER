from pathlib import Path
import json,csv,re,html
B=Path(__file__).resolve().parent
en='''## 3.6.1. Transition-level evidence and continuity distribution (D01)

The adjacent-boundary set is B={B12,B23,B34,B45}, corresponding to S1→S2, S2→S3, S3→S4 and S4→S5. O5 (other inputs→S5) is retained outside this set. A paper with S5 outputs is not automatically assigned B45: its upstream recovery input must be documented. The existing analysis unit is a unique publication–context pair a=(p,b), not an independent study or a physical material flow. Scenario variants within that pair are not counted again. A future scenario-level extraction would require a new unit and denominator.

The archived continuity codebook assigns one primary status c(a): Q, discussion/review; N, downstream transfer not demonstrated; R, inputs prepared for propagation; S, sensitivity/representation comparison; P, partial or incompletely documented transfer; E, quantified outputs for selected uncertain inputs. These are evidence categories, not an ordinal maturity scale. In particular, E does not establish transport of every upstream uncertainty or dependency. The R code here is distinct from the reported-function R code used for DT features.

D01 is computed as n(b,c)=sum over a of 1[b(a)=b and c(a)=c]. Its margins satisfy N(b)=sum_c n(b,c) and sum_b N(b)=|A|. Ribbon width is proportional to n(b,c); it encodes the distribution of assessments into evidence states, not the magnitude of uncertainty transferred. All four adjacent boundaries remain in the exported table, including zero cells. A zero for B34 means no counted assessment in this selected extraction, not absence of relevant research. Multiple pairs from one publication remain dependent. No downstream continuity is inferred by joining different publications into a synthetic S1–S5 trajectory.

To adjudicate an actual transition, extraction must identify the upstream uncertain variable X, its representation U(X), the documented mapping Y=f(X,theta), and the downstream use of U(Y). For stochastic propagation, samples, joint distributions or an equivalent dependence treatment must be traceable through f; a sensitivity plot alone is not such evidence. Updating is separately recorded when new observations change the inferred state or parameter distribution. The notation describes what is inspected in the papers; this review does not itself simulate material stocks or perform Bayesian updating. An interval on Y without a documented connection to upstream X supports output-UQ evidence but not necessarily end-to-end continuity [I25,I33].

## 3.6.2. Stage–function incidence network (D02)

For each publication p, stage s and function f, x(p,s,f)=1 only when the source coding contains a reported-function state R. C denotes conceptual/proposed/review support and NR denotes no positive recorded feature. R is not independent validation or proof of an operational whole-system twin. The weighted bipartite network has w(s,f)=sum_p x(p,s,f); stage-node counts are the distinct union of supporting publications across functions, and function-node counts are the corresponding union across stages. Repeated tags within a publication–stage–function cell must be collapsed before aggregation.

Only S1–S5 cells enter the network; X-coded adjacent construction, scheduling or cost functions remain outside it. Edge width is proportional to w. In the archived plotting implementation, stage-node area is 220+55N(s) points squared and function-node area is 170+45N(f), so node size is an affine visual encoding, not a strictly proportional area encoding. The network is an incidence map without inter-stage direction. Even if the same paper supports S2 and S3, a transition is counted only after its input–mapping–output connection is separately evidenced. D02 supplies candidate functions for the transition join; it does not substitute for that join.

## 3.6.3. Exact positive-code configurations (D03)

For the non-review DT–U subset, each publication is represented by z(p)=(z1,...,z7), where zk=1 for a reported R-coded mechanism and 0 otherwise. The seven dimensions are probabilistic representation, Bayesian state/parameter inference, explicit dependency transport, residual/shift diagnostics, online adaptation, interval-coverage assessment and uncertainty-linked alerts/actions. The original C and NR states are preserved separately: zero in this projection does not establish absence. Publications assigned to the review/reference-architecture family are omitted from this configuration analysis.

For each observed binary pattern v, its exact-intersection frequency is h(v)=sum_p 1[z(p)=v]. Each publication contributes to exactly one pattern, and sum_v h(v)=N. Marginal mechanism frequency is m(k)=sum_v v(k)h(v). Columns are sorted by decreasing h, then number of positive codes, with a deterministic binary-pattern tie-break. This is an UpSet-style exact-set display, not clustering, a maturity ranking or an inferred causal sequence. Identical positive-code patterns do not establish identical implementations; implementations may differ in context and in their C/NR states.

## 3.6.4. Source–method associations within the same transition context (D04)

Source and method labels are joined on the compound key (publication_id, context), never on publication alone. Let A(q) be the set of counted pairs carrying source q and A(m) those carrying method m. The cell count is n(q,m)=|A(q) intersection A(m)| and the row denominator is N(q)=|A(q)|. Colour encodes P(m|q)=100 n(q,m)/N(q), while bubble area is 150 n(q,m) points squared. Empty source rows have an undefined percentage, not zero. Rows and columns are ordered by their assessment frequencies, with codebook order resolving ties.

Because labels are multilabel, percentages within a row need not sum to 100%. The join establishes co-occurrence within one assessed context, not that the method was specifically applied to that source. For example, a context containing two sources and two methods yields four co-occurrence cells; a source-specific treatment claim requires an additional explicit evidence relation. Source labels are not automatically mapped to epistemic or aleatory uncertainty. Prediction-error diagnostics and scenario comparison are not automatically probabilistic propagation.

## 3.6.5. Joining the four outputs into transition-based architectural evidence

D01 establishes the recorded continuity state of a boundary; D04 identifies accompanying sources and methods; D02 locates reported domain functions; D03 provides general-DT mechanism configurations. The architectural join uses the boundary record as its anchor and stores: boundary_id, material variable and unit, uncertainty source/representation, continuity state, method, DT function, update trigger, spatial/temporal validity, evidence locator and support class. Within-publication links are distinguished from compatible cross-study synthesis and proposed additions. General DT configurations are not relabelled S1–S5 implementations.

For each boundary, the results will report the assessed publication count, context count, distribution of continuity states, documented variable transformations, candidate DT functions and the evidential status of each proposed connection. A transition diagram can therefore show what is preserved, transformed, newly introduced or insufficiently reported without interpreting a stage–function edge as uncertainty transport. Missing B34 coverage remains visible. A conceptual missing link is not filled by reallocating O5 assessments to B45 or by treating a review as an independent experiment.

## 3.6.6. Verification and limits of the current analytical inputs

The aggregation audit independently reconstructs D01 cells from context records, D02 weights from R-coded cells, D03 exact memberships from mechanism codes and D04 intersections from source/method assignments. It checks unique keys, ID sets, marginal conservation, row denominators and source-file hashes. The current snapshot reproduces 23 contexts from 20 publications, 16 positive stage–function edges, nine exact configurations across ten non-review records, and 46 positive cells in the 100-cell source–method matrix. These are analysis-subset counts, not PRISMA included-study totals.

This arithmetic check does not reread or validate the semantic interpretation of every paper. Some archived extraction anchors refer to earlier coding tables rather than page-specific primary evidence. Such cases require evidence-locator completion and compatibility checks against the current eligibility ledger before submission. The figures are therefore reproducible from the archived coding, but are not certified as a newly completed full-text synthesis. No statistical independence, inter-reviewer agreement or significance test is inferred from successful reproduction.

'''
fa='''## ۳.۶.۱. شواهد انتقال و توزیع وضعیت پیوستگی: D01

مجموعهٔ مرزهای مجاور B={B12,B23,B34,B45} به‌ترتیب متناظر با S1→S2، S2→S3، S3→S4 و S4→S5 است. O5، یعنی سایر ورودی‌ها به S5، خارج از این مجموعه نگه داشته می‌شود. مقالهٔ دارای خروجی S5 خودکار به B45 نسبت داده نمی‌شود؛ ورودی بازیابیِ بالادست باید مستند باشد. واحد تحلیل موجود، زوج یکتای مقاله–زمینه a=(p,b) است، نه مطالعهٔ مستقل یا جریان فیزیکی مصالح. سناریوهای مختلف همان زوج دوباره شمرده نمی‌شوند. استخراج سناریومحور به واحد و مخرج جدید نیاز دارد.

در فرهنگ کدگذاری آرشیوشده، هر ارزیابی یک وضعیت اصلی c(a) دارد: Q، بحث یا مرور؛ N، انتقال پایین‌دست نشان داده نشده؛ R، ورودی آمادهٔ انتشار؛ S، مقایسهٔ حساسیت یا بازنمایی؛ P، انتقال جزئی یا ناقص مستندشده؛ و E، خروجی کمّی برای ورودی‌های نامطمئن منتخب. این دسته‌ها رتبهٔ بلوغ نیستند. به‌ویژه E انتقال همهٔ عدم قطعیت‌ها و وابستگی‌های بالادست را ثابت نمی‌کند. کد R این جدول با R مربوط به قابلیت گزارش‌شدهٔ DT متفاوت است.

در D01، مقدار n(b,c) برابر تعداد ارزیابی‌هایی است که هم مرز b و هم وضعیت c دارند. مجموع وضعیت‌های هر مرز برابر N(b) و مجموع مرزها برابر تعداد کل زوج‌های مقاله–زمینه است. پهنای نوار متناسب با n(b,c) است و توزیع ارزیابی‌ها را نشان می‌دهد، نه مقدار عدم قطعیت منتقل‌شده. هر چهار مرز، حتی با مقدار صفر، در جدول خروجی باقی می‌مانند. صفر B34 یعنی در این استخراج منتخب ارزیابی شمارش‌شده‌ای وجود ندارد؛ نه اینکه پژوهش مرتبط وجود ندارد. چند زمینهٔ یک مقاله مشاهدات مستقل نیستند و اتصال مقاله‌های مختلف، مسیر سرتاسری S1–S5 را اثبات نمی‌کند.

برای داوری انتقال واقعی باید متغیر نامطمئن بالادست X، بازنمایی U(X)، نگاشت مستند Y=f(X,theta) و استفادهٔ پایین‌دست از U(Y) شناسایی شوند. در انتشار تصادفی، نمونه‌ها، توزیع مشترک یا روش معادل برخورد با وابستگی باید در عبور از f قابل ردیابی باشند؛ نمودار حساسیت به‌تنهایی چنین شاهدی نیست. به‌روزرسانی زمانی جدا ثبت می‌شود که مشاهدهٔ جدید، توزیع وضعیت یا پارامتر استنباط‌شده را تغییر دهد. این نمادگذاری بیانگر چیزی است که در مقاله‌ها بررسی می‌کنیم؛ مرور حاضر شبیه‌سازی موجودی یا به‌روزرسانی بیزی جدید اجرا نمی‌کند. بازهٔ Y بدون اتصال مستند به X، شاهد کمّی‌سازی عدم قطعیت خروجی است، اما لزوماً پیوستگی سرتاسری نیست [I25,I33].

## ۳.۶.۲. شبکهٔ حضور قابلیت در مرحله: D02

برای مقاله p، مرحله s و قابلیت f، مقدار x(p,s,f) فقط زمانی یک است که کد منبع، وضعیت R یا قابلیت گزارش‌شده داشته باشد. C پشتوانهٔ مفهومی، پیشنهادی یا مروری و NR نبود کد مثبت ثبت‌شده است. R اعتبارسنجی مستقل یا عملیاتی‌بودن کل دوقلو را ثابت نمی‌کند. وزن یال شبکهٔ دوبخشی w(s,f) مجموع x در مقاله‌هاست. تعداد گره مرحله از اجتماع یکتای مقاله‌های پشتیبان قابلیت‌ها و تعداد گره قابلیت از اجتماع مقاله‌های پشتیبان آن در مراحل محاسبه می‌شود. برچسب تکراری در سلول مقاله–مرحله–قابلیت باید پیش از شمارش ادغام شود.

فقط S1–S5 وارد شبکه می‌شوند؛ کارکردهای مجاور هزینه، زمان‌بندی و ساخت با کد X بیرون می‌مانند. ضخامت یال متناسب با w است. در کد رسم آرشیوشده، مساحت گره مرحله 220+55N(s) و مساحت گره قابلیت 170+45N(f) پوینت مربع است؛ بنابراین اندازهٔ گره رابطهٔ خطی دارای عرض از مبدأ دارد و تناسب مستقیم مساحت نیست. این شبکه، حضور قابلیت را بدون جهت بین‌مرحله‌ای نشان می‌دهد. حتی اگر مقاله هم S2 و هم S3 داشته باشد، انتقال فقط پس از مستندشدن اتصال ورودی–نگاشت–خروجی ثبت می‌شود. D02 قابلیت‌های نامزد برای بررسی رابط را فراهم می‌کند و جایگزین تحلیل انتقال نیست.

## ۳.۶.۳. ترکیب‌های دقیق کدهای مثبت: D03

در زیرمجموعهٔ غیرمروری DT–U، هر مقاله با بردار z(p)=(z1,...,z7) نمایش داده می‌شود؛ zk برای سازوکار دارای کد R برابر یک و در غیر این صورت صفر است. هفت بُعد شامل بازنمایی احتمالاتی، استنباط بیزی وضعیت یا پارامتر، انتقال صریح وابستگی، تشخیص باقیمانده یا تغییر توزیع، انطباق برخط، بررسی پوشش بازه و هشدار یا اقدام مرتبط با عدم قطعیت هستند. وضعیت اصلی C و NR جدا حفظ می‌شود؛ صفر در این تصویر دودویی به معنای نبود قابلیت نیست. خانوادهٔ مرور و معماری مرجع از این تحلیل ترکیب کنار گذاشته می‌شود.

برای هر الگوی مشاهده‌شده v، فراوانی تقاطع دقیق h(v) برابر تعداد مقاله‌هایی است که z(p)=v دارند. هر مقاله دقیقاً وارد یک الگو می‌شود و مجموع فراوانی الگوها برابر N است. فراوانی حاشیه‌ای سازوکار k از مجموع v(k)h(v) به دست می‌آید. ستون‌ها بر اساس فراوانی، سپس تعداد کد مثبت و در حالت تساوی با ترتیب ثابت الگوی دودویی مرتب می‌شوند. این نمایش تقاطع دقیق به سبک UpSet است؛ نه خوشه‌بندی، رتبهٔ بلوغ یا توالی علّی. یکسانی الگوی مثبت، یکسانی پیاده‌سازی را اثبات نمی‌کند؛ زمینه و وضعیت‌های C و NR می‌توانند متفاوت باشند.

## ۳.۶.۴. هم‌وقوعی منبع و روش در زمینهٔ یکسان انتقال: D04

برچسب منبع و روش با کلید مرکب شناسهٔ مقاله و زمینه متصل می‌شوند؛ نه فقط شناسهٔ مقاله. اگر A(q) مجموعهٔ زوج‌های دارای منبع q و A(m) مجموعهٔ زوج‌های دارای روش m باشد، شمار خانه n(q,m)=|A(q)∩A(m)| و مخرج ردیف N(q)=|A(q)| است. رنگ، درصد 100n(q,m)/N(q) و مساحت حباب، 150n(q,m) پوینت مربع را نشان می‌دهد. درصد برای ردیف فاقد منبع تعریف‌نشده است، نه صفر. ترتیب ردیف و ستون بر اساس فراوانی ارزیابی و در تساوی بر اساس ترتیب فرهنگ کدگذاری است.

چون کدگذاری چندبرچسبی است، مجموع درصد ردیف الزاماً ۱۰۰ نیست. این اتصال هم‌وقوعی در زمینهٔ ارزیابی یکسان را نشان می‌دهد، نه اینکه روش مشخصاً روی همان منبع اعمال شده است. برای مثال، زمینه‌ای با دو منبع و دو روش، چهار خانهٔ هم‌وقوعی ایجاد می‌کند؛ ادعای بررسی اختصاصی یک منبع با یک روش، رابطهٔ مستند اضافی می‌خواهد. برچسب‌های منبع خودکار معرفتی یا تصادفی تلقی نمی‌شوند. تشخیص خطای پیش‌بینی و مقایسهٔ سناریو نیز خودکار انتشار احتمالاتی نیستند.

## ۳.۶.۵. اتصال چهار خروجی به شواهد معماری مبتنی بر انتقال

D01 وضعیت ثبت‌شدهٔ پیوستگی مرز را مشخص می‌کند؛ D04 منابع و روش‌های همراه آن را نشان می‌دهد؛ D02 جایگاه قابلیت‌های حوزه را مشخص می‌کند؛ و D03 ترکیب سازوکارهای DT عمومی را فراهم می‌کند. اتصال معماری بر رکورد مرز استوار است و شناسهٔ مرز، متغیر مصالح و واحد آن، منبع و بازنمایی عدم قطعیت، وضعیت پیوستگی، روش، قابلیت DT، محرک به‌روزرسانی، اعتبار مکانی و زمانی، محل شاهد و نوع پشتوانه را نگه می‌دارد. اتصال درون مقاله از سنتز مطالعات سازگار و پیشنهاد جدید جدا می‌شود. ترکیب‌های DT عمومی به‌عنوان پیاده‌سازی S1–S5 بازنام‌گذاری نمی‌شوند.

برای هر مرز، نتایج تعداد مقاله و زمینهٔ ارزیابی‌شده، توزیع وضعیت پیوستگی، تبدیل متغیرهای مستند، قابلیت‌های نامزد DT و وضعیت شاهد هر اتصال پیشنهادی را گزارش می‌کند. بنابراین نمودار انتقال می‌تواند حفظ، تبدیل، ورود عدم قطعیت جدید یا گزارش ناکافی را نشان دهد، بدون تفسیر یال مرحله–قابلیت به‌عنوان انتقال عدم قطعیت. پوشش خالی B34 قابل مشاهده می‌ماند و با انتقال ارزیابی O5 به B45 یا شمردن مرور به‌عنوان آزمایش مستقل پر نمی‌شود.

## ۳.۶.۶. کنترل محاسبات و حدود داده‌های تحلیلی موجود

ممیزی تجمیع، خانه‌های D01 را از رکورد زمینه، وزن‌های D02 را از سلول‌های دارای R، عضویت‌های D03 را از کد سازوکار و تقاطع‌های D04 را از برچسب منبع و روش مستقلاً بازسازی می‌کند. یکتایی کلید، مجموعهٔ شناسه، توازن مجموع‌ها، مخرج ردیف و هش فایل منبع کنترل می‌شوند. نسخهٔ موجود، ۲۳ زمینه از ۲۰ مقاله، ۱۶ یال مثبت مرحله–قابلیت، ۹ ترکیب دقیق در ۱۰ رکورد غیرمروری و ۴۶ خانهٔ مثبت در ماتریس ۱۰۰خانه‌ای منبع–روش را بازتولید می‌کند. این‌ها شمار زیرمجموعهٔ تحلیل هستند، نه تعداد مطالعات Included در PRISMA.

این کنترل محاسباتی، بازخوانی یا تأیید تفسیر معنایی همهٔ مقاله‌ها نیست. بعضی محل‌های شاهد در استخراج آرشیوی به جدول کدگذاری قبلی اشاره دارند و هنوز ارجاع صفحه‌ای به متن اصلی ندارند. این موارد پیش از ارسال مقاله به تکمیل محل شاهد و تطبیق با دفتر صلاحیت فعلی نیاز دارند. پس شکل‌ها از کدگذاری آرشیوی بازتولیدپذیرند، اما به‌عنوان سنتز متن کاملِ تازه و نهایی تأیید نشده‌اند. موفقیت بازتولید نیز استقلال آماری، توافق ارزیابان یا معناداری را ثابت نمی‌کند.

'''
for lang,body in [('en',en),('fa',fa)]:
 p=B/f'sections/03_methods_{lang}.txt';s=p.read_text(encoding='utf8')
 marker='## 3.7.' if lang=='en' else '## ۳.۷.'
 start='## 3.6.1.' if lang=='en' else '## ۳.۶.۱.'
 if start in s:s=s[:s.index(start)]+s[s.index(marker):]
 s=s.replace(marker,body+marker);p.write_text(s,encoding='utf8')
print('Technical D01-D04 methods inserted in both languages.')
