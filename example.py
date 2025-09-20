
import os

# تأكد من وجود صورة للاختبار
# يمكنك استبدال هذا بمسار صورة حقيقية لديك
# For demonstration, let's assume a dummy image path or create one if needed.
# In a real scenario, the user would provide their own image.
# For now, we'll just use a placeholder and note that a real image is needed.

# Example 1: Sketching an image (requires an actual image file)
print("\n--- Example 1: Sketching an image ---")
image_for_sketch = "path/to/your/image.jpg" # <--- استبدل هذا بمسار صورتك الحقيقية
if os.path.exists(image_for_sketch):
    print(f"تشغيل عملية الرسم على الصورة: {image_for_sketch}")
    os.system(f"python run_sketchpy.py --operation sketch --image_path {image_for_sketch} --save True --retain False")
else:
    print(f"تنبيه: الصورة {image_for_sketch} غير موجودة. تخطي مثال الرسم.")
    print("يرجى توفير مسار صورة صالح لتشغيل هذا المثال.")

# Example 2: Generating ASCII Art (requires an actual image file)
print("\n--- Example 2: Generating ASCII Art ---")
image_for_ascii = "path/to/your/image.png" # <--- استبدل هذا بمسار صورتك الحقيقية
if os.path.exists(image_for_ascii):
    print(f"تشغيل عملية ASCII Art على الصورة: {image_for_ascii}")
    os.system(f"python run_sketchpy.py --operation ascii --image_path {image_for_ascii} --save True")
else:
    print(f"تنبيه: الصورة {image_for_ascii} غير موجودة. تخطي مثال ASCII Art.")
    print("يرجى توفير مسار صورة صالح لتشغيل هذا المثال.")

# Example 3: Drawing APJ Abdul Kalam
print("\n--- Example 3: Drawing APJ Abdul Kalam ---")
os.system("python run_sketchpy.py --operation apj --retain False")

# Example 4: Drawing Tom Holland
print("\n--- Example 4: Drawing Tom Holland ---")
os.system("python run_sketchpy.py --operation tom_holland --retain False")

# Example 5: Drawing Robert Downey Jr.
print("\n--- Example 5: Drawing Robert Downey Jr. ---")
os.system("python run_sketchpy.py --operation rdj --retain False")

# Example 6: Drawing Vijay
print("\n--- Example 6: Drawing Vijay ---")
os.system("python run_sketchpy.py --operation vijay --retain False")

print("\n--- انتهت الأمثلة. يرجى مراجعة المخرجات. ---")

