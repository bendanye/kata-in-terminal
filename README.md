# Kata In Terminal

Practice writing commands or codes in your terminal

## Project Setup & Commands

### Prerequisites

* Python 3.6 minimum

### Installation

```shell
pip install -r requirements.txt
```

### Setup

* By default this program will look at "questions" and "solutions" folders
* Each question and solution file name must matched
* For solution file to indicate the solution place within `####`. Refer to `examples` folder for details.  

### Run the program

```shell
python main.py --folder_path <<your root path where questions and solutions folder reside>>
```

For example to run the examples in this project:

```shell
python main.py --folder_path examples
```

## Modes of running

* Interactive mode (one question at a time)
    * From all questions
    * From questions previously have incorrect answer

## Potential enhancements

- [ ] Check that code is correct even if there is new line
- [ ] Generate questions from a markdown file
- [ ] Allow to run in non-interactive mode, like exam mode
- [ ] Allow to run mode where number of questions based on day of the week
- [ ] Allow Number of questions based on day of the week
- [ ] Log time taken and output to a file

## Impetus

This idea started from when the author is taking ckad soon and does not have k8s environment on his machine and wanted to practise writing yaml file or typing command and allow verification to see if the written yaml or command is correct against "expected".
