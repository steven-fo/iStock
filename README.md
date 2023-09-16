# iStock

Nama: Steven Faustin Orginata <br>
Kelas: PBP C <br>
NPM: 2206030855

iStock adalah sebuah aplikasi untuk mengukur/mengecek stok pada toko.
<br>
Link: [Adaptable](https://istock.adaptable.app/)

=================================================

<h2>Tugas 2 PBP Ganjil 2023/2024</h2>

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

<hr>

<h4>1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).</h4>
Dalam membuat proyek Django, saya pertama membuat direktori di komputer saya. Kemudian, saya jalankan git init untuk membuat direktori bisa menjalankan git.

  ```
  git init
  ```
<br>
Selanjutnya, saya membuat file requirements.txt dimana isinya adalah module yang digunakan untuk membuat project.

  ```
  django
  gunicorn
  whitenoise
  psycopg2-binary
  requests
  urllib3
  ```
Setelah itu, saya jalankan command django-admin startproject "nama project". Setelah itu, saya membuat file .gitignore agar file yang tidak seharusnya di upload ke git tidak ter-upload. Untuk membuat proyek dengan nama main, maka saya menjalankan command django-admin startproject main. 
  ```
  django-admin startproject main
  ```
Struktur project akan seperti berikut
<br>
![struktur_proyek_istock](https://github.com/steven-fo/iStock/assets/119484321/0c8d521a-2231-41b9-bcd8-660124f91f0f)

Setelah membuat project Django, hal pertama yang saya lakukan adalah mengubah ALLOWED HOSTS di file settings.py menjadi "*" dimana maksudnya adalah all. 
  ```
  ...
  ALLOWED_HOSTS = ["*"]
  ...
  ```
Saya juga menambahkan nama folder project, yaitu main, ke INSTALLED_APPS. 
  ```
  INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
]
  ```
Selain itu, saya menambahkan routing di file urls.py dimana pathnya akan mengarah ke main.
  ```
  urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
  ```

Untuk membuat model, saya membuat file models.py di dalam folder project. Kemudian, saya membuat class Item (nama bebas) dengan param models(import django).Model. Di dalam class tersebut saya isi dengan atribut yang diinginkan. Misal, name = models.CharField() amount = models.IntegerField(), dst.
  ```
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
    type = models.TextField()
    description = models.TextField()

  ```

Fungsi yang dibuat bernama show_main dengan param request. Isi dari function ini adalah context yang berisi nilai dari model yang ingin dibuat. Kemudian, di akhir akan di return request, nama file html, context.
  ```
def show_main(request):
    item = Item.objects.all()
    context = {
        'name': 'Steven Faustin Orginata',
        'class': 'PBP C',
        'items': item
    }

    return render(request, "main.html", context)
  ```

Routing dapat ditambahkan di urls.py dengan menambahkan line path(main, include main.urls) dimana isi urls.py di folder main adalah mendeklarasikan nama app, yaitu main, dan membuat path yang menerima func show_main pada views.py
  ```
urlpatterns = [
    path('', show_main, name='show_main'),
]
  ```

Step-step dalam melakukan deploy sama dengan tutorial yaitu, connect ke github repo, pilih python template, pilih postgreSQL database, pilih python ver dan jangan lupa masukkan start command, terakhir nyalakan port listener

<h4>2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.</h4>

![image](https://github.com/steven-fo/iStock/assets/119484321/b95efc89-f909-442f-abc0-7507e982e501)
<br>
Pada saat client me-request website di browser, browser akan jalan ke urls.py untuk melakukan url routing. Kemudian, dari urls akan jalan ke views.py karena ada func show_main yang berfungsi untuk menampilkan data. Dari views akan masuk ke models untuk melihat jenis data yang akan ditampilkan. Setelah itu, akan masuk ke database untuk mengambil data yang ingin ditampilkan. Dari database akan masuk ke models.py kemudian ke views.py untuk menyiapkan data yang akan ditampilkan. Terakhir, data tersebut akan dipass ke file template yaitu index.html dimana data akan ditampilkan disini. Index.html kemudian di pass ke browser yang akhirnya user dapat melihat data yang di-request.

<h4>3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?</h4>
Menurut saya, virtual environment berguna untuk menjalankan program/aplikasi web. Mengapa? karena terdapat beberapa depedensi setiap modul yang di-install. Modul-modul tersebut hanya bisa diakses dengan virtual environment
<br>
<h4>4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.</h4>

  * MVC = Model-View-Controller <br>
  MVC berfokus pada menerima data yang diinput oleh user. Model dan view akan berubah mengikuti input user <br>
  * MVT = Model-View-Template <br>
  MVT berfokus pada menampilkan data. Ia tidak bisa menerima data/input dari user. <br>
  * MVVM = Model-View-ViewModel <br>
  MVVM berfokus pada menampilkan dan menerima data. <br>

<hr>

<h2>Tugas 3 PBP Ganjil 2023/2024</h2>

* Apa perbedaan antara form POST dan form GET dalam Django?
* Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
* Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
* Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

<hr>

<h4>Apa perbedaan antara form POST dan form GET dalam Django?</h4>
Query POST dan GET berbeda dari request ke server. Query POST, sesuai namanya, yaitu memasukkan data ke server. Pada saat kita mengisi form dan mengklik tombol add item, kita melakukan query POST ke server untuk menyimpan data tersebut di server. Query GET, sesuai namanya, yaitu mengambil data dari server. Pada saat kita men-display data ada berapa item, kita melakukan query GET ke server untuk mendapatkan data tersebut kemudian data tersebut di display.
<br>

<h4>Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data</h4>

* XML: menyimpan/mengirimkan data dalam urutan/hierarki root / parent dan child.
* JSON: menyimpan/mengirimkan data dalam bentuk yang lebih mudah dibaca
* HTML: bukan untuk menyimpan/mengirimkan data. HTML dipakai untuk membuat tampilan web. Data dikirimkan dalam bentuk webpage.

<h4>Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern</h4>
JSON sering digunakan karena struktur / format yang mudah dibaca. 

<h4>Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
</h4>
Sebelum membuat form, saya membuat file base.html untuk menjadi template html webpage berikut"nya.

  ```
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>

{% comment %} file ini sebagai skeleton/template untuk halaman page lainnya {% endcomment %}
  ```

Setelah membuat template, saya memasukkan template ke settings.py bagian template, DIRS

    TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [BASE_DIR / 'templates'],
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
    ]
  

Kemudian, saya menambahkan button ke form dan table untuk mendisplay data

        <h4>Kamu menyimpan {{items.count}} item pada aplikasi ini</h4>
    <table>
        <tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Type</th>
            <th>Description</th>
            <th>Date Added</th>
        </tr>

        {% for item in items %}
        <tr>
            <td>{{item.name}}</td>
            <td>{{item.amount}}</td>
            <td>{{item.type}}</td>
            <td>{{item.description}}</td>
            <td>{{item.date_added}}</td>
        </tr>
        {% endfor %}
    </table>

    <br>

    <a href="{% url 'main:create_item' %}">
        <button>
            Add New Item
        </button>
    </a>

Bisa dilihat di link button, dia akan redirect ke create_item page. Maka, saya perlu membuat create_item.html.

    {% extends 'base.html' %}

    {% block content %}
    <h1>Add New Item</h1>
    
    <form method="POST">
        {% csrf_token %}
        <table>
            {{form.as_table}}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Add Item"/>
                </td>
            </tr>
        </table>
    </form>
    
    
    {% endblock content %}

Selanjutnya, saya membuat function untuk mendisplay create_item di views.py

    def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context) 

Dari views ini lanjut ke urls.py untuk melakukan routing

    urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name="create_item"),
    ]

Selanjutnya, untuk membuat 5 fungsi views, saya membuat fungsi di views.py

    def show_html(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("html", data), content_type="application/html")

    def show_xml(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    
    def show_json(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    
    def show_xml_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    
    def show_json_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

Dengan langkah yang sama seperti create_item, saya membuat routing function tersebut di urls.py

    urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name="create_item"),
    path('html/', show_html, name="show_html"),
    path('xml/', show_xml, name="show_xml"),
    path('json/', show_json, name="show_json"),
    path('xml/<int:id>/', show_xml_by_id, name="show_xml_by_id"),
    path('json/<int:id>/', show_json_by_id, name="show_json_by_id"),
    ]

=================================================

<h4>Screenshoot Postman</h4>

<h5>Mengakses http://localhost:8000/json</h5>
![json](https://github.com/steven-fo/iStock/assets/119484321/de695a66-67ef-4f36-ae9c-baefe3aa9e51)

<h5>Mengakses http://localhost:8000/xml</h5>
![xml](https://github.com/steven-fo/iStock/assets/119484321/b4b9304c-0eb5-4849-81d8-d5a82f2614d1)

<h5>Mengakses http://localhost:8000/html</h5>
![HTML](https://github.com/steven-fo/iStock/assets/119484321/2a878155-e1e0-47e4-a83b-ab78a7de4284)
![html](https://github.com/steven-fo/iStock/assets/119484321/2bbd981d-f9b2-48fd-af6c-e457ce1b41d9)

<h5>Mengakses http://localhost:8000/json/1</h5>
![json_id](https://github.com/steven-fo/iStock/assets/119484321/1a772f6c-e1f0-4179-8ba8-87dab09d26dc)

<h5>Mengakses http://localhost:8000/xml/1</h5>
![xml_id](https://github.com/steven-fo/iStock/assets/119484321/2501b831-3949-40f3-8b94-e6cf123899b6)

<hr>
