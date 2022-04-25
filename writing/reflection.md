# Text Analysis

TODO: Make sure that your GitHub repository contains the following text files:

- `generated_one.txt`: generated text from the `aitextgen` program provided as a part of this project
- `generated_two.txt`: generated text from the `aitextgen` program provided as a part of this project
- `input_one.txt`: human-written text provided as part of this project
- `input_two.txt`: human-written text that you excerpt from an external source or write yourself


TODO: Make sure that your GitHub repository contains the following graphics files:

- `set-visualization-generated.png`: visualization created by `textanalysis` for the file `generated_one.txt`
- `set-visualization-input.png`: visualization created by `textanalysis` for the file `input_one.txt`

TODO: You must use a command like `git add` to ensure that certain files exist in the repository.

## Evelyn Griffith

## Program Input and Output

### What is the output from running the following command?

TODO: Use a fenced code block to provide the output for this command.

`poetry run textanalysis --input-file text/input_one.txt --analyze`

### What is the output from running the following command?

TODO: Use a fenced code block to provide the output for this command.

`poetry run textanalysis --input-file text/generated_one.txt --analyze`

### What is inside of the `generated_two.txt` file that `aitextgen` created?

```The Federal Reserve has been trying to figure out how much money will be available to the economy of the United States from the Federal Reserve, although the Fed is pushing back its efforts.

The Federal Reserve Board is pushing back on the idea that the U.S. economy has reached a point where it is no longer "in an economy of money," according to a report released by the Fed last week.

The report, titled "The American Economy: The Federal Reserve Is Making a Mistake," points to a few key facts.

The Fed has no plans to raise interest rates.

"In fact, the Federal Reserve expects to raise rates before the next set of economic growth rates are set and before the next monetary policy cycle begins," the report said.

The Fed didn't make any specific announcement about how much money will be available to the economy in the report, which was released just before the third quarter in which the government's unemployment rate was at its lowest level in more than a decade.

But it did say that if policymakers are willing to raise rates, "there is no reason to expect that the monetary policy rate will be substantially lower than at present."

The Fed has been trying to figure out how much money
```

### What is inside of the `input_two.txt` file that you downloaded/wrote and saved?

TODO: Use a fenced code block to provide the contents of the file.
TODO: You should download and save a short text segment written by another person.
TODO: Alternatively, you can write your own text that you want to analyze.

## Source Code

### Describe in detail how your provided source code works

#### Please explain each line of source code from the `extract` module

```python
def extract_paragraphs(input_lines: str) -> List[str]:
    """Extract all of the paragraphs from the lines of textual input."""
    # Reference:
    # https://stackoverflow.com/questions/53240763/python-how-to-separate-paragraphs-from-text
    no_newlines = input_lines.strip("\n")
    split_text = NEWLINES_RE.split(no_newlines)
    paragraphs = [p + "\n" for p in split_text if p.strip()]
    return paragraphs
```

This function is going to start, like every other function, with a function definition. This is going to name the function (in this case it will be named `extract_paragraphs`) and then it will state the input and ouput variable types. This function will take in a string called input_lines and it will produce a list of strings in this case called `paragraphs`. The main goal of this function is to extract the number of paragraphs from the file and return a list of strings called paragraphs. This function is going to create a variable called `no_newlines` which is going to take `input_lines` and strip it of its lines in between paragraphs. It will then take a variable called `split_text` and it will use the NEWLINES_RE.split() function to split up the paragraphs based on newline breaks. Then the function will take the variable paragraphs and create a lambda variable the will essentially iterate through and create a list for every paragraph that was in the file.

## Analyzing the Text

NOTE: The analysis described in this reflection file only requires you to study
the output of `textanalysis` when run with the files called `input_one.txt` and
`input_two.txt`. With that said, you should make sure that the program also
works correctly when it is run with other input files!

### According to the output of your program, what words does `input_one.txt` have in common across all paragraphs? How did you know?

TODO: Provide response to this question, demonstrating your knowledge of the use and visualization of sets.

### Using the console output and visualization for the `input_one.txt`, what trends do you see? Interpret these trends.

TODO: Provide response to this question, demonstrating your knowledge of the use and visualization of sets.

### Using the console output and visualization for the `generated_one.txt`, what trends do you see? Interpret these trends.

TODO: Provide response to this question, demonstrating your knowledge of the use and visualization of sets.

## Professional Development

### What are the similarities and differences between `set`, `FrozenSet`, and `FiniteSet`?

The biggest differences between sets FrozenSets and FiniteSets is actually in the titles. A FiniteSet is going to have a fixed number of elements in it and it is always going to have a fixed size. It is going to offer some operations as built-in sets and add additional set-theoretic operations. Another nice thing about FiniteSets is that they are immutable while regular sets are not. A regular set is going to be mutable and therefore unhashable whereas a FiniteSet will be hashable. A FrozenSet however is a little bit different than both of these things. It is going to be an immutable version of a python set, just like a FiniteSet but it is going to act more like a key in a dictionary than an actual Set.

### How is the `set` discrete structure similar to and different from the `list` and the `tuple`?

A set is different than a list and a tuple because a Set has no order in the way that it is stored. It is going to 

### At your own option, do you have any other insights to share about this assignment?

TODO: At your own option, provide further insights about this assignment!
