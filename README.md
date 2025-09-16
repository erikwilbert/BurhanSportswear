Tautan menuju aplikasi : https://erik-wilbert-burhansportswear.pbp.cs.ui.ac.id/

Tugas 2
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
- Membuat folder proyek local, aktifkan virtual environment, susun requirements.txt, download seluruh dependence atau library yang terdapat pada requirements.txt.
- Inisialisasi git dan buat .gitignore untuk file sensitif yang tidak perlu dicommit, buatkan juga repository baru di github lalu menghubungkan git local ke github dengan menggunakan "remote add origin <link menuju repository>".
- Buatkan proyek Django dengan menggunakan "django-admin startproject <nama project>". Buatkan file .env (development) dan .env.prod (production) dan muat variabelnya di settings.py dengan menggunkan "python-dotenv".
- Buatkan aplikasi main dengan menggunakan "python manage.py startapp <nama aplikasi>" dan mendaftarkannya di settings.py dalam INSTALLED_APPS.
- Mendefinisikan model Product di models.py dengan enam atribut wajib (name, price, description, thumbnail, category, is_featured) dengan tipe field masing-masing, lalu jalankan "python manage.py makemigrations" dan "python manage.py migrate" untuk melakukan perubahan pada model basis data di Django.
- Implementasi MVT dasar dengan sebuah views yang merender template main.html (buatkan main.html di dalam folder baru bernama templates di aplikasi main) berisi html sederhana dengan nama aplikasi, nama lengkap, dan kelas, petakan rute main.html di main/urls.py dan gabungkan ke urls.py utama proyek dengan include.
- Setup PWS dengan buat proyek di PWS, amankan username dan passwordnya, copy isi env.prod ke Environs, dan tambahkan URL PWS proyek ini ke ALLOWED_HOSTS di settings.py, jalankan perintah “Project Command” awal dari PWS.
- Lakukan "git add .", "git commit -m <komentar>", dan "git push origin <main branch>" serta "git push PWS <main branch>" setiap kali melakukan perubahan.

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


Tugas 3
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery diperlukan dalam pengimplementasian sebuah platform karena menjadi mekanisme utama pertukaran informasi antar komponen sistem, seperti antara frontend dan backend. Dengan adanya data delivery, aplikasi dapat menampilkan data secara dinamis, memungkinkan interaksi dua arah dengan server, serta memastikan sistem yang berbeda bisa saling berkomunikasi dengan baik. 

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON lebih unggul dibandingkan XML karena memiliki struktur yang lebih sederhana, ringan, mudah dibaca, serta lebih cepat diproses. Meskipun XML mendukung struktur data kompleks, formatnya cenderung verbose dan kurang efisien untuk kebutuhan pertukaran data modern. JSON menjadi lebih populer karena strukturnya mirip objek JavaScript, sehingga integrasi dengan aplikasi web jauh lebih mudah dan mendapat dukungan luas dari berbagai bahasa pemrograman.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() pada form Django berfungsi untuk memvalidasi data yang dikirimkan pengguna. Method ini mengecek kesesuaian data dengan tipe field, memastikan field wajib terisi, serta menjalankan aturan validasi tambahan. Jika valid, is_valid() mengembalikan nilai True dan data bersih dapat diakses melalui cleaned_data; jika tidak valid, method ini mengembalikan False sekaligus menyimpan pesan error untuk ditampilkan di template. 

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
CSRF token dibutuhkan pada form Django untuk mencegah serangan Cross-Site Request Forgery (CSRF), yaitu upaya penyerang memanfaatkan sesi login pengguna untuk menjalankan aksi berbahaya tanpa sepengetahuan mereka. Token ini berfungsi sebagai verifikasi bahwa request benar-benar berasal dari form sah milik aplikasi. Tanpa CSRF token, penyerang dapat menyisipkan form palsu atau link berbahaya yang mengirimkan request otomatis, misalnya mengubah data penting atau melakukan transaksi.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Import module HttpResponse dari django.http dan serializers dari django.core.
- Membuat 4 fungsi baru di main/views.py bernama show_xml dengan parameter "response", show_json dengan parameter "response", show_xml_by_id dengan parameter "response" dan "product_id", show_json_by_id dengan parameter "response" dan "product_id".
- Pada show_xml, mendefinisikan product_list dengan mengambil semua product yang ada, ubah queryset menjadi format XML dan membalikan data (response) ke client dalam bentuk XML.
- Pada show_json, mendefinisikan product_list dengan mengambil semua product yang ada, ubah queryset menjadi format JSON dan membalikan data (response) ke client dalam bentuk JSON.
- Pada show_xml_by_id, mendefinisikan produt_item dengan cari produk berdasarkan primary key (id) menggunakan filter, kalau ketemu, ubah ke format XML dan dikirim balik ke client.
- Pada show_json_by_id, mendefinisikan produt_item dengan cari produk berdasarkan primary key (id) menggunakan filter, kalau ketemu, ubah ke format JSON dan dikirim balik ke client.
- Menambahkan semua routing urls masing-masing views yang telah dibuat tadi fungsinya dalam main/urls.py.
- Tambahkan tombol add pada main.html untuk redirect ke form nantinya dan membuat templates create_product dan product_detail pada main/templates/ untuk digunakan nantinya dan base.html di roots/templates/ sebagai template dasar.
- Membuat halaman form dengan templates create_product dan konfigurasinya pada forms.py.
- Menambahkan tampilan produk-produk pada main.html jika terdapat produk dan halaman product_detail untuk menampilkan detail produk.
- Lakukan "git add .", "git commit -m <komentar>", dan "git push origin <main branch>" serta "git push PWS <main branch>" setiap kali melakukan perubahan.

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Selama tutorial 2 masih aman dan baik.