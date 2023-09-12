Nama: Steven Faustin Orginata <br>
Kelas: PBP C <br>
NPM: 2206030855

Tugas 2 PBP Ganjil 2023/2024

=================================================

iStock adalah sebuah aplikasi untuk mengukur/mengecek stok pada toko.
<br>
Link: [Adaptable](https://istock.adaptable.app/)

=================================================

Step:
* Membuat sebuah proyek Django baru.
* Membuat aplikasi dengan nama main pada proyek tersebut.
* Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
* Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
 - name sebagai nama item dengan tipe CharField.
 - amount sebagai jumlah item dengan tipe IntegerField.
 - description sebagai deskripsi item dengan tipe TextField.
* Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
* Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
* Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

=================================================

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
<br>
Dalam membuat proyek Django, saya pertama membuat direktori di komputer saya. Kemudian, saya jalankan git init untuk membuat direktori bisa menjalankan git. Selanjutnya, saya membuat file requirements.txt dimana isinya adalah module yang digunakan untuk membuat project. Setelah itu, saya jalankan command django-admin startproject "nama project". Setelah itu, saya membuat file .gitignore agar file yang tidak seharusnya di upload ke git tidak ter-upload.

Untuk membuat proyek dengan nama main, maka saya menjalankan command django-admin startproject main. 

Setelah membuat project Django, hal pertama yang saya lakukan adalah mengubah ALLOWED HOSTS di file settings.py menjadi "*" dimana maksudnya adalah all. Saya juga menambahkan nama folder project, yaitu main, ke INSTALLED_APPS. Selain itu, saya menambahkan routing di file urls.py dimana pathnya akan mengarah ke main.

Untuk membuat model, saya membuat file models.py di dalam folder project. Kemudian, saya membuat class Item (nama bebas) dengan param models(import django).Model. Di dalam class tersebut saya isi dengan atribut yang diinginkan. Misal, name = models.CharField() amount = models.IntegerField(), dst.

Fungsi yang dibuat bernama show_main dengan param request. Isi dari function ini adalah context yang berisi nilai dari model yang ingin dibuat. Kemudian, di akhir akan di return request, nama file html, context.

Routing dapat ditambahkan di urls.py dengan menambahkan line path(main, include main.urls) dimana isi urls.py di folder main adalah mendeklarasikan nama app, yaitu main, dan membuat path yang menerima func show_main pada views.py

Step-step dalam melakukan deploy sama dengan tutorial yaitu, connect ke github repo, pilih python template, pilih postgreSQL database, pilih python ver dan jangan lupa masukkan start command, terakhir nyalakan port listener

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![image](https://github.com/steven-fo/iStock/assets/119484321/b95efc89-f909-442f-abc0-7507e982e501)
<br>
Pada saat client me-request website di browser, browser akan jalan ke urls.py untuk melakukan url routing. Kemudian, dari urls akan jalan ke views.py karena ada func show_main yang berfungsi untuk menampilkan data. Dari views akan masuk ke models untuk melihat jenis data yang akan ditampilkan. Setelah itu, akan masuk ke database untuk mengambil data yang ingin ditampilkan. Dari database akan masuk ke models.py kemudian ke views.py untuk menyiapkan data yang akan ditampilkan. Terakhir, data tersebut akan dipass ke file template yaitu index.html dimana data akan ditampilkan disini. Index.html kemudian di pass ke browser yang akhirnya user dapat melihat data yang di-request.


4. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
<br>
Menurut saya, virtual environment berguna untuk menjalankan program/aplikasi web. Mengapa? karena terdapat beberapa depedensi setiap modul yang di-install. Modul-modul tersebut hanya bisa diakses dengan virtual environment
<br>
<br>
5. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
<br>
MVC = Model-View-Controller
<br>
MVT = Model-View-Template
<br>
MVVM = Model-View-ViewModel
<br>

MVC berfokus pada menerima data yang diinput oleh user. Model dan view akan berubah mengikuti input user
MVT berfokus pada menampilkan data. Ia tidak bisa menerima data/input dari user.
MVVM berfokus pada menampilkan dan menerima data.

<hr>
