
# Fundamentals Exercise 1: CLI

Perform the following tasks using the CLI and paste the commands and results below.

- Navigate to your home directory
cd ~

- Create a new directory called CodingNomads. We will use this folder
to house materials for the course.
mkdir CodingNomads

- Move into the CodingNomads folder
cd CodingNomads

- Create new folder cli_testing
mkdir cli_testing


- Inside of folder cli_testing,
    a. print the directory path
	pwd
    b. create 3 new .txt files all with different names (file1.txt,
    file2.txt, file3.txt)
	touch file1.txt
	touch file2.txt
	touch files3.txt

    c. list the contents of the folder
	ls
    d. rename one of the files
	mv file1.txt file4.txt

- Inside of folder cli_testing, create a new folder
	mkdir random
- Copy a file from cli_testing to the new folder
	cp file1.txt /random/
- Move a different file from cli_testing to the new folder
	mv file2txt /random/
- Demonstrate removing:
    a. A file
	rm text3.txt
    b. A folder
	rm -rf /random

## vim

- Use `$ vim` to write some text inside a file
	vim file
	i
	entered some text
esc
	:wq
- Use `$ cat` print contents of file
	cat file
- Use `$ grep` to search for a word inside file
	grep file "word"


## explore advanced CLI

- What is the difference between the two commands > and >>?
	the first overwrite , the second appends.
- Create a file hello.txt with the text "how?!", then append the text
    to another file called my_file.txt
	touch hello.txt
        echo "how?!" >> my_file.txt
	
- Overwrite the content of my_file.txt with "tell me"
	echo "tell me" > my_file.txt
