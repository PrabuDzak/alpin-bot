alpin-bot

```
$ sudo apt-get install python-pip
$ pip install -r requirements.txt
```

# Plan for alpin-bot behaviour

## pin \<command\> pin:

#### koran
headline koran lampu hijau

#### istighfar
"Astaghfirullah"

#### jadwal kuliah
jadwal kuliah hari itu dan ruangan

#### jancok
kata kata mutiara / peribahasa

#### kucing
http://thecatapi.com/api/images/get?size=med


#### asu
http://i.imgur.com/1MCV5s7.jpg

# Lesson learned

- use Flask handler. its easier
- to app.run() you need to define host ```0.0.0.0``` and port ``` os.environ.get('PORT') ```