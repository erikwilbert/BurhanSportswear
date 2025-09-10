Tautan menuju aplikasi : https://erik-wilbert-burhansportswear.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
- Membuat folder proyek local, aktifkan virtual environment, susun requirements.txt, download seluruh dependence atau library yang terdapat pada requirements.txt.
- Inisialisasi git dan buat .gitignore untuk file sensitif yang tidak perlu dicommit, buatkan juga repository baru di github lalu menghubungkan git local ke github dengan menggunakan "remote add origin <link menuju repository>".
- Buatkan proyek Django dengan menggunakan "django-admin startproject <nama project>". Buatkan file .env (development) dan .env.prod (production) dan muat variabelnya di settings.py dengan menggunkan "python-dotenv".
- Buatkan aplikasi main dengan menggunakan "python manage.py startapp <nama aplikasi>" dan mendaftarkannya di settings.py dalam INSTALLED_APPS.
- Mendefinisikan model Product di models.py dengan enam atribut wajib (name, price, description, thumbnail, category, is_featured) dengan tipe field masing-masing, lalu jalankan "python manage.py makemigrations" dan "python manage.py migrate" untuk melakukan perubahan pada model basis data di Django.
- Implementasi MVT dasar dengan sebuah views yang merender template main.html (buatkan main.html di dalam folder baru bernama templates di aplikasi main) berisi html sederhana dengan nama aplikasi, nama lengkap, dan kelas, petakan rute main.html di main/urls.py dan gabungkan ke urls.py utama proyek dengan include.
- Setup PWS dengan buat proyek di PWS, amankan username dan passwordnya, copy isi env.prod ke Environs, dan tambahkan URL PWS proyek ini ke ALLOWED_HOSTS di settings.py, jalankan perintah “Project Command” awal dari PWS.
- Lakukan "git add .", "git commit -m <komentar>", dan "git push origin <main branch>", serta "git push PWS <main branch>" setiap kali melakukan perubahan.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Django MVT](./images/bagan_model_mvt.png)
Diagram ini menjelaskan alur kerja arsitektur MTV pada Django. Proses dimulai ketika server menerima sebuah HTTP Request, yang kemudian diteruskan ke urls.py untuk menentukan rute dan mengarahkannya ke View (views.py) yang sesuai. Di dalam View, logika aplikasi dijalankan, dan jika diperlukan, View akan berinteraksi dengan Model (models.py) untuk mengambil atau memodifikasi data dari database. Setelah itu, data yang diperoleh dikirim ke Template (.html) untuk dirender menjadi halaman web. Hasil render tersebut kemudian dikembalikan ke pengguna sebagai sebuah HTTP Response dalam bentuk dokumen HTML.

3. Jelaskan peran settings.py dalam proyek Django! 
settings.py adalah file konfigurasi utama dalam proyek Django. Semua pengaturan penting proyek didefinisikan di sini, mulai dari daftar aplikasi yang digunakan (INSTALLED_APPS), konfigurasi database, daftar host yang diizinkan (ALLOWED_HOSTS), hingga SECRET_KEY untuk keamanan. Selain itu, file ini juga memungkinkan pemisahan pengaturan antara lingkungan development (saat aplikasi masih dikembangkan di komputer lokal) dan production (saat aplikasi dijalankan di server).

4. Bagaimana cara kerja migrasi database di Django?
Migrasi database di Django adalah proses yang menjaga agar struktur database selalu sesuai dengan definisi model di models.py. Saat developer menambahkan atau mengubah model, Django dapat membuat file migrasi menggunakan perintah makemigrations, yang berisi instruksi tentang perubahan apa saja yang harus diterapkan pada database, seperti membuat tabel baru, menambah kolom, atau menghapus field. Setelah itu, perintah migrate dijalankan untuk mengeksekusi file migrasi tersebut dan menerapkan perubahan ke database.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak? 
Menurut saya, framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak karena Django menggunakan Model-View-Template (MVT) yang sangat jelas dan terstruktur, yang memisahkan data, logika, dan tampilan, yang membuatnya menjadi permulaan karena alur aplikasi awal yang terlihat jelas, terstruktur, dan lebih mudah dipahami.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Asisten dosen tutorial 1 cukup membantu walaupun dilaksanakan secara online, asisten dosen membantu melalui platform yang tersedia, asisten dosen mampu membantu menangani error yang membingungkan bagi kita.