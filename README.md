link aplikasi PWS: https://fidan-khalil-footballshop.pbp.cs.ui.ac.id/

Langkah-langkah implementasi:
    1. Membuat sebuah proyek Django baru
        - Membuat direktori baru bernama football-shop dan membuat serta mengaktifkan env pada terminal dengan menjalankan python -m venv env dan env\Scripts\activate

        -  Membuat dan menginstall requirements.txt, lalu membuat proyek Django bernama football_shop

        - Membuat file .env untuk menggunakan database SQLite dan file .env.prod untuk menggunakan database PostgreSQL

        - Memodifikasi file settings.py untuk meng-import environment variables dari file .env, menambahkan host lokal ke list host yang diizinkan untuk mengakses web, menambahkan konfigurasi PRODUCTION, dan mengubah konfigurasi DATABASES

        - Menghubungkan ke github dan pws

    2. Membuat aplikasi dengan nama main pada proyek:
        - Menjalankan perintah python manage.py startapp main

    3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main:
        - Menambahkan aplikasi main pada list aplikasi 

    4. Membuat model pada aplikasi main:
        - Mengisi file models.py dengan membuat class Product dan berisi atribut name bertipe Charfield, price bertipe IntegerField, description bertipe TextField, thumbnail bertipe URLField, category bertipe CharField, dan is_featured bertipe BooleanField

    5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML:
        - Membuat sebuah fungsi bernama show_main dengan parameter request. Lalu membuat context yang berisi NPM, nama, dan kelas yang berguna untuk dikirimkan ke template. Lalu fungsi me-return fungsi render

        - Mengubah main.html menjadi struktur Django, agar dapat menampilkan data yang diambil dari model tanpa menulis manual

    6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py:
        - Membuat file urls.py di dalam direktori main dan mengisinya dengan path ke main.views

        - Menghubungkan urls.py pada direktori main ke urls.py pada direktori proyek football-shop

    7. Melakukan deployment ke PWS:
        - Membuat projek baru pada PWS dan menyimpan username dan password

        - Mengubah isi pada tab environs dengan copy paste isi file .env.prod

        - Menambahkan list host yang diizinkan untuk mengakses web dengan link deployment PWS

        - Menjalankan git remote add pws, git branch -M master, git push pws master pada terminal

        -Mengisi username dan password Git Credential Manager dengan username dan password yang tadi sudah disimpan



Bagan Request:
    request -> urls.py -> views.py -> models.py -> views.py -> template -> response

    browser akan melakukan request dan urls.py memetakan URL ke view tertentu. Lalu views.py akan mengambil data dari models.py dan memproses datanya. Data tersebut akan dikirim ke template dan mengubah berkas html. Barulah response akan muncul pada browser



Peran settings.py:
    1. Menentukan penggunaan SQLite atau PostgreSQL atau yang lain
    2. Menentukan siapa saja host yang diizinkan untuk mengakses web
    3. Mendaftarkan aplikasi yang digunakan pada proyek
    4. Middleware



Cara kerja migrasi database di Django:
    1. Membuat berkas migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam basis data
    2. Setelah menjalankan perintah migrate, perubahan yang terjadi akan diimplementasikan ke basis data



Alasan framework Django dijadikan permulaan pembelajaran pengembangan perangkata lunak:
    1. Framework Django memiliki struktur yang jelas, karena menggunakan pola MVT (Model-View-Template) yang memungkinkan untuk memisah logika model, logika view, dan logika tampilan sejak awal
    2. Django sudah menyediakan perlindungan terhadap serangan umum seperti SQL Injection, XSS, CSRF, dan lain-lain secara otomatis
    3. Django menjadi jembatan ke konsep lanjutan seperti REST API, deployment, dan framework lain.
    4. Django banyak digunakan di industri, seperti Instagram dan Pinterest