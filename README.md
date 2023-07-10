# Twenty Questions

This repository is an implementation of the game Twenty Questions where an Azure OpenAI model attempts to guess the object that the user is thinking about.

## Example Game

This example game uses only 5 questions.

```txt
Welcome to 20 Questions!

        1. Think of an object.
        2. Answer a series of 5 yes/no questions.
        3. Once all 5 questions have been answered, the bot will try to guess what you are thinking of.

Question 1 of 5: Is the object typically found indoors?
Yes (y) or no (n)? y

Question 2 of 5: Is the object used for entertainment?
Yes (y) or no (n)? y

Question 3 of 5: Is the object electronic?
Yes (y) or no (n)? n

Question 4 of 5: Is the object typically used in a group setting?
Yes (y) or no (n)? n

Question 5 of 5: Is the object typically used for physical activity?
Yes (y) or no (n)? y

Are you thinking of a jump rope? (y/n): y

I gazed intently at you, trying to read your thoughts and figure out what object you were thinking of.
I could feel my heart racing as the seconds ticked by, the pressure mounting with every passing moment.
I knew that this was my chance to prove myself - to show that I had what it takes to read minds and guess correctly.

Suddenly, I saw a flicker of recognition in your eyes, and I knew that I was on the right track.
With a surge of inspiration, I blurted out the name of the object that had been on your mind all along - and to my great relief, I was right!
A warm glow of triumph swelled within me as I basked in the glow of your approval, knowing that I had earned my place as a true master of the art of guesswork.
```

## Setup

1. Install python and requirements `pip install -r requirements`
1. Copy [`example.env`](./example.env) to `.env`
1. Run the game: `python twenty-questions.py`
