
🧠 Deskripsi Proyek
Proyek ini menggunakan model YOLOv8n dari pustaka ultralytics untuk melakukan deteksi objek pada gambar. Tujuannya adalah mengidentifikasi objek dalam folder input dan menyimpan hasil deteksi ke folder output.

🛠️ Teknologi yang Digunakan
- Python 3.12
- Ultralytics YOLOv8
- Visual Studio Code
- OS: Windows 11

📁 Struktur Folder

project/
│
├── input_images/       # Folder berisi gambar mentah
├── output_images/      # Folder hasil deteksi
├── yolov8n.pt          # Model YOLOv8 ringan
└── detect.py           # Skrip utama

- Pastikan kamu sudah install modul dengan:
pip install ultralytics
- Cek environment Python di VS Code: pastikan kamu pakai interpreter yang sesuai.
- Bisa juga jalankan which python atau where python untuk memastikan path-nya benar.

✅ Cara Menjalankan
- Masukkan gambar ke folder input_images.
- Jalankan skrip:
python detect.py
- Hasil deteksi akan muncul di folder output_images.
