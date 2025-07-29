<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Python Öğrenme Alıştırmaları</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #fafafa;
            margin: 30px;
            line-height: 1.6;
        }
        h1 {
            color: #2c3e50;
        }
        h2 {
            color: #34495e;
        }
        code {
            background-color: #eee;
            padding: 2px 4px;
            border-radius: 4px;
            font-family: monospace;
        }
        ul {
            padding-left: 20px;
        }
    </style>
</head>
<body>
    <h1>🐍 Python Öğrenme Alıştırmaları</h1>
    <p>Bu sayfa, Python programlama dili üzerine yaptığım temel alıştırmaları ve veri analizi pratiklerini içermektedir. Kodlar, hem temel konuları pekiştirmek hem de pandas gibi kütüphanelerle analiz becerisi kazanmak amacıyla hazırlanmıştır.</p>

    <h2>📁 İçerik</h2>
    <ul>
        <li><strong>temel_pratikler.py</strong><br>
            - Sayı ve string veri tipleri<br>
            - Listeler, koşullar, döngüler<br>
            - Fonksiyon yazımı
        </li>
        <li><strong>veri_analizi.py</strong><br>
            - pandas ile veri analizi<br>
            - Filtreleme: <code>df[df["price"] > 15000]</code><br>
            - Gruplama ve ortalama: <code>df.groupby("cut")["price"].mean()</code><br>
            - Çoklu gruplama: <code>df.groupby(["cut", "clarity"])["price"].mean()</code>
        </li>
    </ul>

    <h2>🎯 Amaç</h2>
    <p>Python temellerini kavramak ve küçük veri setleri üzerinde uygulama yaparak analiz becerilerimi geliştirmek.</p>
</body>
</html>
