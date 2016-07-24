from ghost import Ghost
ghost = Ghost()
page, resources = ghost.open('https://www.hackerrank.com/raj61')
result, resources = ghost.evaluate(
    "document.getElementsById('hacker-contest-score');")
