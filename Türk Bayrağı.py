import turtle

# Ayarlar
w = turtle.Screen()
w.title("Türk Bayrağı")
w.setup(width=720, height=420)
w.bgcolor("red")

# Turtle Ayarları
t = turtle.Turtle()
t.speed(10)

# Büyük Daire
t.up()
t.goto(-100, -100)
t.down()
t.color('white')
t.begin_fill()
t.circle(120)
t.end_fill()

# Küçük Daire
t.up()
t.goto(-70, -80)
t.down()
t.color('red')
t.begin_fill()
t.circle(100)
t.end_fill()

# Yıldız
t.up()
t.goto(30, 50)
t.down()
t.color('white')
t.begin_fill()
for i in range(5):
    t.forward(80)
    t.right(144)
t.end_fill()

# Yıldızın içini dolduran pentagon
t.up()
t.goto(60, 49)
t.down()
t.color('white')
t.begin_fill()
for i in range(5):
    t.forward(20)
    t.right(72)
t.end_fill()

# Yazı
t.up()
t.goto(-175, -190)
t.color("white")
t.write("ahmet.sirin.34@outlook.com", font=("Verdana", 17, "bold"))

# Bitirme
t.hideturtle()
w.exitonclick()
