## OSINT Wordlist Generator

<h5>Do you have a file of OSINT data on someone? Including but not limited to: </h1>
<ul>
    <li>Names</li>
    <li>Birthdays</li>
    <li>Pets names</li>
    <li>Favorite sports teams</li>
</ul>

If the answer is yes, then this simple tool might be the one for you.

Create a text file with these values on newlines, and feed it to the program

`python3 main.py --infile yourfilehere.txt --outfile whereitsgoing.txt`

You can also set the depth by using the `--depth` flag. The default is 2 layers.

And <b> BOOM</b>. You have a fully custom password list that might be better suited for  
your cracking needs than a standard wordlist *cough cough* <b>rockyou.txt</b> *cough cough*.

You can also set the depth by using the `--depth` flag. The default is 2 layers.

### Installation Guide (Linux)

Clone the repo, then I recommend sticking it into your `/bin` directory so you can access
it anywhere.

You'll also probably want to rename the file before you stick it in `/bin`

`cp main.py; mv main.py yourfilename.py; chmod +x yourfilename.py`

Then a simple `sudo mv yourfilename.py /bin` and *voila* you're all set to run this bad
boy wherever you want.
