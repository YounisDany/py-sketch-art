# SketchPy - مكتبة رسم وتحويل الصور

![SketchPy Logo](https://raw.githubusercontent.com/MRMYSTERY003/sketchpy/main/assets/logo.png)

Py-Sketch-Art هي مكتبة بايثون قوية وممتعة تتيح لك تحويل الصور إلى رسومات فنية باستخدام خوارزميات الرسم بالقلم الرصاص (pencil sketch) أو تحويلها إلى فن ASCII. تم تطوير هذه المكتبة لتكون سهلة الاستخدام، مع إمكانية التخصيص الكامل للتحكم في عملية الرسم والتأثيرات.

## الميزات الرئيسية

*   **الرسم بالقلم الرصاص:** حول أي صورة إلى رسم فني واقعي بالقلم الرصاص.
*   **فن ASCII:** قم بتحويل الصور إلى فن ASCII باستخدام الأحرف النصية.
*   **رسومات جاهزة:** تتضمن المكتبة رسومات جاهزة لشخصيات مشهورة مثل APJ Abdul Kalam و Tom Holland و Robert Downey Jr. و Vijay.
*   **واجهة سطر الأوامر (CLI):** تشغيل العمليات بسهولة من خلال سطر الأوامر.
*   **تتبع تلقائي:** وظيفة تتبع تلقائية للصور لتبسيط عملية الرسم.

## التثبيت

يمكنك تثبيت `SketchPy` بسهولة باستخدام `pip`:

```bash
pip install sketchpy
```

## الاستخدام

### من خلال سطر الأوامر (CLI)

يمكنك استخدام الملف `run_sketchpy.py` لتشغيل العمليات المختلفة:

*   **لرسم صورة بالقلم الرصاص:**
    ```bash
    python run_sketchpy.py --operation sketch --image_path path/to/your/image.jpg --save True --retain False
    ```
    (سيتم إنشاء ملف إحداثيات مؤقت تلقائيًا إذا لم يكن موجودًا.)

*   **لتحويل صورة إلى ASCII Art:**
    ```bash
    python run_sketchpy.py --operation ascii --image_path path/to/your/image.png --save True
    ```

*   **لرسم شخصية جاهزة (مثال: APJ Abdul Kalam):**
    ```bash
    python run_sketchpy.py --operation apj --retain False
    ```

*   **لرؤية جميع الخيارات المتاحة:**
    ```bash
    python run_sketchpy.py --help
    ```

### كجزء من مشروع بايثون الخاص بك

يمكنك استيراد الوحدات واستخدامها مباشرة في كود بايثون الخاص بك:

```python
from sketchpy import sketch
from sketchpy import effects
from sketchpy import library_drawings

# مثال على رسم صورة بالقلم الرصاص
obj = sketch.sketch_from_image('path/to/your/image.jpg')
obj.draw(threshold=120) # يمكنك تعديل قيمة threshold للتحكم في تفاصيل الرسم

# مثال على تحويل صورة إلى ASCII Art
eff = effects.ascii_art('path/to/your/image.png')
eff.draw()

# مثال على رسم شخصية جاهزة
drawing = library_drawings.apj()
drawing.draw()

# مثال على رسم Tom Holland
drawing = library_drawings.tom_holland()
drawing.draw()

# مثال على رسم Robert Downey Jr.
drawing = library_drawings.rdj()
drawing.draw()

# مثال على رسم Vijay
drawing = library_drawings.vijay()
drawing.draw()
```

## المساهمة

نرحب بالمساهمات في تطوير هذه المكتبة! إذا كان لديك أي اقتراحات أو تحسينات، فلا تتردد في فتح مشكلة (issue) أو إرسال طلب سحب (pull request) على مستودع GitHub.

## الترخيص

هذه المكتبة مرخصة تحت ترخيص MIT. انظر ملف `LICENSE` لمزيد من التفاصيل.

## شكر وتقدير

شكر خاص للمطور الأصلي للمكتبة [MRMYSTERY003](https://github.com/MRMYSTERY003/sketchpy) على عمله الأساسي.
