from turtle import Turtle ,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
screen.title("Racing Game")
screen.bgcolor("black")
user_bet = screen.textinput(title="Make Your Bet",prompt="Which racer will win the race? Enter a color: ")
color=["orange","purple","red","blue","yellow","green","pink"]
y_position = [-90,-70,-40,-10,20,50,80]
all_racers = []
for index in range(0,7):
    t = Turtle(shape="turtle")  # type: ignore
    t.color(color[index])
    t.penup()
    t.goto(x=-230,y=y_position[index])
    all_racers.append(t)

if user_bet:
    is_race_on = True
while is_race_on:
    for racer in all_racers:
        if racer.xcor() > 230:
            is_race_on = False
            winner_color = racer.pencolor()
            if winner_color == user_bet:
                print(f"You've won! The {winner_color} turtle is the winner!")
            else:
                print(f"You've lose! The {winner_color} turtle is the winner!")
        rand_dist = random.randint(0,10)
        racer.fd(rand_dist)


screen.exitonclick()
                


