This is the app that runs the 289 The Peak Websites

IMPORTANT:
Pushing to Heroku is a fucking pain in the ass. First, you will need Git CLI and Heroku CLI installed. Then, make sure you have runtime.txt, requirements.txt, and Procfile (no extension, it will be a dick if you accidentally save it as 'Procfile.txt'). Make sure the formatting in the files is correct. One misplaced space or character and you're fucked. ALL of them must be encoded in ANSI or Heroku will bitch at you. Also, make sure the version of Python you have listed in runtime.txt is supported on the Heroku stack, otherwise Heroku will shit the bed. If you have all of this stuff correct and the planets align in rising Jupiter, you can run 'git push heroku master' and bada boom, it should work.

Make sure that any time you add a new package/dependency, you run 'pip freeze > requirements.txt' and double check that it's encoded in ANSI, otherwise Heroku will shid and fard and cry.