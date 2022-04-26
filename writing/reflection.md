# Text Analysis

Make sure that your GitHub repository contains the following text files:

- `generated_one.txt`: generated text from the `aitextgen` program provided as a part of this project
- `generated_two.txt`: generated text from the `aitextgen` program provided as a part of this project
- `input_one.txt`: human-written text provided as part of this project
- `input_two.txt`: human-written text that you excerpt from an external source or write yourself


Make sure that your GitHub repository contains the following graphics files:

- `set-visualization-generated.png`: visualization created by `textanalysis` for the file `generated_one.txt`
- `set-visualization-input.png`: visualization created by `textanalysis` for the file `input_one.txt`

You must use a command like `git add` to ensure that certain files exist in the repository.

## Evelyn Griffith

## Program Input and Output

### What is the output from running the following command?

`poetry run textanalysis --input-file text/input_one.txt --analyze`

```✨ Let's characterize the file and its words!

        The input file contains 23 lines, including blank lines!
        The input file contains 19 lines, not including blank lines!
        The input file contains 5 paragraphs!
        The input file contains 118 unique words across all sets!
        The words that are found across all sets are: {'Make', 'to'}

🖌 Saving the visualization in graphics/set-visualization.png

🔬 Get ready, here is the analysis of the sets!

{
    frozenset({0, 4}): {'how', 'package'},
    frozenset({1, 2}): {'changed', 'source', 'on', 'files', 'It'},
    frozenset({4}): {
        'control',
        'want',
        'worth',
        'use',
        'do',
        'down',
        'often',
        'while',
        'installing',
        'enough',
        'make',
        'building',
        'deinstalling',
        'You',
        'anything',
        'generate',
        'writing',
        'else',
        'tags',
        'tables'
    },
    frozenset({0}): {
        'without',
        'build',
        'done',
        'these',
        'supply',
        'because',
        'recorded',
        'are',
        'user',
        'end',
        'knowing',
        'details',
        'install',
        'enables'
    },
    frozenset({1}): {
        'have',
        'another',
        'one',
        'figures',
        'needs',
        'automatically',
        'determines',
        'which',
        'based',
        'depends',
        'out',
        'case',
        'updating',
        'order',
        'proper'
    },
    frozenset({0, 2}): {'that', 'your', 'of', 'and'},
    frozenset({3}): {
        'shell',
        'commands',
        'an',
        'linker',
        'library',
        'specifies',
        'produce',
        'language',
        'any',
        'object',
        'ar',
        'These',
        'compute',
        'format',
        'Makeinfo',
        'For',
        'TeX',
        'documentation',
        'executable',
        'particular',
        'each',
        'compiler'
    },
    frozenset({0, 1, 2, 3, 4}): {'Make', 'to'},
    frozenset({0, 2, 4}): {'you'},
    frozenset({3, 4}): {'can', 'limited'},
    frozenset({2, 3, 4}): {'a', 'not', 'or'},
    frozenset({2}): {
        'updates',
        'those',
        'depend',
        'As',
        'if',
        'then',
        'change',
        'result',
        'directly',
        'few',
        'does',
        'indirectly',
        'need',
        'only',
        'recompile',
        'all'
    },
    frozenset({0, 3, 4}): {'is'},
    frozenset({1, 3}): {'update', 'file'},
    frozenset({1, 2, 3, 4}): {'it'},
    frozenset({0, 3}): {'makefile'},
    frozenset({0, 1, 2, 3}): {'the'},
    frozenset({2, 3}): {'program', 'run'},
    frozenset({1, 4}): {'also', 'for'},
    frozenset({1, 2, 3}): {'non-source'},
    frozenset({0, 1, 3}): {'in'}
}
```

### What is the output from running the following command?

`poetry run textanalysis --input-file text/generated_one.txt --analyze`

```
✨ Let's characterize the file and its words!

        The input file contains 15 lines, including blank lines!
        The input file contains 8 lines, not including blank lines!
        The input file contains 8 paragraphs!
        The input file contains 110 unique words across all sets!
        The words that are found across all sets are: {}

🖌 Saving the visualization in graphics/set-visualization.png

🔬 Get ready, here is the analysis of the sets!

{
    frozenset({0, 2, 3, 7}): {'that'},
    frozenset({2}): {
        'but',
        'told',
        'Guardian',
        'photo',
        'God',
        'help',
        'never',
        'issue',
        'my',
        '2016',
        'According',
        'reported',
        'taken',
        'feel',
        'health',
        "couldn't",
        'June',
        'what',
        '"I',
        '27',
        "'Oh",
        'miracle!\'"'
    },
    frozenset({0}): {
        'someone',
        'scandal',
        'been',
        'take',
        'hard',
        "It's",
        'lead',
        'have',
        'like',
        'kind',
        'this',
        'Ryan',
        'would',
        'water-related',
        'such',
        'did',
        'serious',
        'incident',
        'believe',
        'position'
    },
    frozenset({1}): {
        '"',
        'carried',
        '"Oceans',
        'called',
        'bottle',
        'and',
        'claimed',
        'March',
        'from',
        'out',
        'private',
        'it',
        'contained',
        'water'
    },
    frozenset({3}): {'But', 'authentic', 'court', 'ruled', 'problem'},
    frozenset({1, 3, 5}): {'family'},
    frozenset({5}): {'then', 'long', "didn't", 'which', 'October', '1', 'last'},
    frozenset({0, 1}): {'of', 'in'},
    frozenset({0, 1, 2, 3, 5, 6, 7}): {'the'},
    frozenset({7}): {'tell', 'way', 'talking', 'about', 'Unfortunately', 'is', 'no', 'means'},
    frozenset({0, 1, 2, 6, 7}): {'to'},
    frozenset({1, 3}): {'photograph', 'with'},
    frozenset({6}): {'years', 'took', 'two', 'nearly'},
    frozenset({0, 1, 2, 3, 5}): {'a'},
    frozenset({1, 2, 3, 4, 5}): {'was', 'The'},
    frozenset({1, 2, 4, 5}): {'on'},
    frozenset({3, 5}): {'against', 'defamation', 'filed'},
    frozenset({2, 3}): {'had'},
    frozenset({3, 5, 6}): {'for'},
    frozenset({4}): {'September', '25th'},
    frozenset({1, 2, 5, 6}): {'It'},
    frozenset({1, 7}): {'hoax'},
    frozenset({0, 3}): {'not'},
    frozenset({3, 7}): {'there'},
    frozenset({4, 5, 6}): {'dismissed'},
    frozenset({0, 7}): {'who'},
    frozenset({3, 4, 5, 6}): {'lawsuit'},
    frozenset({0, 1, 2, 3, 5, 7}): {'Lochte'},
    frozenset({1, 2, 3, 5}): {'website'},
    frozenset({1, 6}): {'be'},
    frozenset({4, 5}): {'2017'}
}
```

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

```It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.

However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.

"My dear Mr. Bennet," said his lady to him one day, "have you heard that Netherfield Park is let at last?"

Mr. Bennet replied that he had not.

"But it is," returned she; "for Mrs. Long has just been here, and she told me all about it."

Mr. Bennet made no answer.

"Do not you want to know who has taken it?" cried his wife impatiently.

"You want to tell me, and I have no objection to hearing it."

This was invitation enough.
```

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

The analysis described in this reflection file only requires you to study
the output of `textanalysis` when run with the files called `input_one.txt` and
`input_two.txt`. With that said, you should make sure that the program also
works correctly when it is run with other input files!

### According to the output of your program, what words does `input_one.txt` have in common across all paragraphs? How did you know?

The words that are the same across all paragraphs are `Make` and `to`.  I know this because when looking at the functions in the extract.py file there is a function called `extract_common_words` and this function is going to take the list of sets of strings and pick out which words are in each set of strings within the set of strings.

### Using the console output and visualization for the `input_one.txt`, what trends do you see? Interpret these trends.

I think the biggest trend that I see in this file is that there is a column that has all colors and this column is the 6th one from the left side. This is interesting because it means that this is a value that all sets have.

### Using the console output and visualization for the `generated_one.txt`, what trends do you see? Interpret these trends.

In this file a trend that I see is that sets 2,3,5,1, and 4 have a lot of similar words, whereas the other sets are more on their own and sporadic.

## Professional Development

### What are the similarities and differences between `set`, `FrozenSet`, and `FiniteSet`?

The biggest differences between sets FrozenSets and FiniteSets is actually in the titles. A FiniteSet is going to have a fixed number of elements in it and it is always going to have a fixed size. It is going to offer some operations as built-in sets and add additional set-theoretic operations. Another nice thing about FiniteSets is that they are immutable while regular sets are not. A regular set is going to be mutable and therefore unhashable whereas a FiniteSet will be hashable. A FrozenSet however is a little bit different than both of these things. It is going to be an immutable version of a python set, just like a FiniteSet but it is going to act more like a key in a dictionary than an actual Set.

### How is the `set` discrete structure similar to and different from the `list` and the `tuple`?

A set is different than a list and a tuple because a Set has no order in the way that the data is stored. It is also going to be immutable which means they are hashable whereas the other two are unhashable and mutable. A list and tuple are also ordered data containers which means that we can do a lot of different things like indexing whereas sets are not ordered at all and can contain any type of data mixed together whereas lists and tuples need to have the same types within.

### At your own option, do you have any other insights to share about this assignment?