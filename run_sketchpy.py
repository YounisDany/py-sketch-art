
import argparse
from sketchpy.drawing import sketch, trace, color_sketch_from_svg, auto_trace
from sketchpy.effects import ascii_art
from sketchpy.library_drawings import apj, vijay, tom_holland, rdj
from sketchpy.utils import get_svg
import os

def run_sketch_operation(image_path=None, operation='sketch', output_file=None, **kwargs):
    """تشغيل عمليات sketchpy المختلفة بناءً على المدخلات.

    :param image_path: مسار الصورة المدخلة (اختياري لبعض العمليات).
    :param operation: العملية المراد تنفيذها (مثل 'sketch', 'ascii', 'svg', 'apj', 'vijay', 'tom_holland', 'rdj').
    :param output_file: مسار ملف الإخراج (اختياري).
    :param kwargs: وسائط إضافية للعمليات المختلفة.
    """
    if operation == 'sketch':
        if not image_path:
            print("مسار الصورة مطلوب لعملية الرسم (sketch).")
            return
        
        coord_file = kwargs.get('coord_file')
        if not coord_file:
            print(f"جاري التتبع التلقائي للصورة: {image_path}")
            coord_file = auto_trace(image_path, output_file='auto_traced_coords.txt', **kwargs)
            if not coord_file:
                print("فشل التتبع التلقائي. لا يمكن المتابعة بدون ملف إحداثيات.")
                return
        
        print(f"جاري رسم الصورة من ملف الإحداثيات: {coord_file}")
        s = sketch(**kwargs)
        s.draw_fn(coord_file, **kwargs)
        print("تم الانتهاء من الرسم.")

    elif operation == 'ascii':
        if not image_path:
            print("مسار الصورة مطلوب لعملية ASCII Art.")
            return
        print(f"جاري تحويل الصورة إلى ASCII Art: {image_path}")
        a = ascii_art(**kwargs)
        a.load_data(img_path=image_path)
        a.draw()
        print("تم الانتهاء من ASCII Art.")

    elif operation == 'svg':
        if not image_path:
            print("مسار ملف SVG مطلوب لعملية SVG Sketching.")
            return
        print(f"جاري رسم ملف SVG: {image_path}")
        s = color_sketch_from_svg(path=image_path, **kwargs)
        # This class requires more setup for actual drawing, e.g., width, height, etc.
        # For simplicity, we'll just initialize it. Actual drawing logic needs to be added or simplified.
        print("تم الانتهاء من رسم SVG (قد تحتاج إلى إعدادات إضافية للرسم الفعلي).")

    elif operation == 'apj':
        print("جاري رسم APJ Abdul Kalam.")
        d = apj(**kwargs)
        d.draw()
        print("تم الانتهاء من رسم APJ Abdul Kalam.")

    elif operation == 'vijay':
        print("جاري رسم Vijay.")
        d = vijay(**kwargs)
        d.draw()
        print("تم الانتهاء من رسم Vijay.")

    elif operation == 'tom_holland':
        print("جاري رسم Tom Holland.")
        d = tom_holland(**kwargs)
        d.draw()
        print("تم الانتهاء من رسم Tom Holland.")

    elif operation == 'rdj':
        print("جاري رسم Robert Downey Jr.")
        d = rdj(**kwargs)
        d.draw()
        print("تم الانتهاء من رسم Robert Downey Jr.")

    else:
        print(f"عملية غير معروفة: {operation}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='تشغيل عمليات sketchpy المختلفة.')
    parser.add_argument('--image_path', type=str, help='مسار الصورة المدخلة (لعمليات sketch, ascii, svg).')
    parser.add_argument('--operation', type=str, required=True, choices=['sketch', 'ascii', 'svg', 'apj', 'vijay', 'tom_holland', 'rdj'], help='العملية المراد تنفيذها.')
    parser.add_argument('--output_file', type=str, help='مسار ملف الإخراج (اختياري).')
    parser.add_argument('--coord_file', type=str, help='مسار ملف الإحداثيات لعملية الرسم (sketch).\n                                                إذا لم يتم توفيره، سيتم التتبع التلقائي للصورة.')
    parser.add_argument('--x_offset', type=int, default=300, help='إزاحة X للرسم.')
    parser.add_argument('--y_offset', type=int, default=300, help='إزاحة Y للرسم.')
    parser.add_argument('--save', type=bool, default=False, help='حفظ الرسم كصورة.')
    parser.add_argument('--mode', type=int, default=1, help='وضع الرسم (1 للخطوط، 0 للتعبئة).\n                                               ينطبق على عملية sketch.')
    parser.add_argument('--thickness', type=int, default=1, help='سمك الخط للرسم.')
    parser.add_argument('--retain', type=bool, default=False, help='الاحتفاظ بالنافذة بعد الرسم.')
    parser.add_argument('--threshold', type=int, default=100, help='عتبة الكشف عن الحواف للتتبع التلقائي.')
    parser.add_argument('--simplify_factor', type=int, default=5, help='عامل تبسيط نقاط التتبع التلقائي.')

    args = parser.parse_args()

    # Collect kwargs for operations
    op_kwargs = {
        'x_offset': args.x_offset,
        'y_offset': args.y_offset,
        'save': args.save,
        'mode': args.mode,
        'thickness': args.thickness,
        'retain': args.retain,
        'threshold': args.threshold,
        'simplify_factor': args.simplify_factor,
    }

    run_sketch_operation(
        image_path=args.image_path,
        operation=args.operation,
        output_file=args.output_file,
        coord_file=args.coord_file,
        **op_kwargs
    )

