"""Extract the paragraphs and other textual content from the paragraphs of text."""
from typing import List
from typing import Set
# Add the required imports at the top of the file
import re


NEWLINES_RE = re.compile(r"\n{2,}")


def extract_lines_including_blanks(input_lines: str) -> List[str]:
    """Extract all of the lines, including the blanks lines."""
    # extract all of the lines in the file, using splitlines
    # return input_lines.readlines()
    #     return len(lines)
    # with input_lines as fp:
    #     num_lines = len(fp.readlines())
    #     return num_lines
    # for line in input_lines:
    #     if line in input_lines:
    #         len_lines += 1
    #     print(len_lines)
    # count = 0
    # for line in input_lines:
    #     if line.strip():
    #         if line is not None:
    #             count += 1
    #     return count
    count = []
    for line in input_lines.splitlines():
        count.append(line)
        # if line:
        #     count += 1
        #     print(count)
    return count

    # return all of the extracted lines


def extract_lines_not_including_blanks(input_lines: str) -> List[str]:
    """Extract all of the lines, not including the blanks lines."""
    # extract all of the lines in the file, using splitlines
    # for line in input_lines.splitlines():
    #     if len(line) != 0:
    #         return line
    count = []
    for line in input_lines.splitlines():
        if line != "":
            count.append(line)
        # if line:
        #     count += 1
        #     print(count)
    return count
    # filter out all of the blank lines that have a length of zero
    # return the list of non-blank lines


def extract_paragraphs(input_lines: str) -> List[str]:
    """Extract all of the paragraphs from the lines of textual input."""
    # Reference:
    # https://stackoverflow.com/questions/53240763/python-how-to-separate-paragraphs-from-text
    no_newlines = input_lines.strip("\n")
    split_text = NEWLINES_RE.split(no_newlines)
    paragraphs = [p + "\n" for p in split_text if p.strip()]
    return paragraphs
    # implement a function that uses, for instance, regular expressions to
    # break up a provided text in a string as a list of strings, with each
    # string representing a paragraph
    # consult the following reference:
    # https://stackoverflow.com/questions/53240763/python-how-to-separate-paragraphs-from-text
    # you may use other online tutorials or responses in your implementation
    # of this function as long as you provide the needed references
    # remove leading and trailing newline characters


def extract_unique_words_paragraphs(paragraphs: List[str]) -> List[Set[str]]:
    """Extract all of the unique words in each one of the paragraphs."""
    # go through each of the strings inside of the list and
    # extract the unique words in each of the paragraphs
    unique_list = []

    symbols = [",", ".", "---"]
    for para in paragraphs:
        lines = para.splitlines()
        para_set = set()

        for line in lines:
            line_str = line

            for symbol in symbols:
                if symbol in line_str:
                    line_str = line_str.replace(symbol, " ")

            line_list = line_str.split()

            for word in line_list:
                if word not in para_set:
                    para_set.add(word)

        unique_list.append(para_set)

    return unique_list

    # print(new_paragraph)
    # if words in line.replace((" ".join(symbols)), ""):\
    # joined_symbols = ",".join(symbols)
    # for symb in symbols:
    # removed_paragraph = re.sub(',!@#$%^&*().?;:--+=1234567890/---[]','" "',new_paragraph)
    # new = re.escape(string.punctuation)
    # print(new)
    # return new
    # for words in para.split():
    # sentences = new_paragraph.splitlines()
    # for single_sentence in sentences:
    #     word = single_sentence.split(" ")

    # print(word)
    #     if symb == words:
    #         print(words)
    # for symb in joined_symbols:
    #     words = line.split(" ")
    #                 # if outputs is not None:
    #         unique_set.add(word)
    #         # print(unique_set)
    #     unique_list.append(unique_set)
    #     # print(unique_list)
    #         # go from list to set to list
    # return unique_list
    # collect the unique words for each paragraph in a set of strings
    # store each set of unique words in a separate index of a list
    # return a list that contains at each index a set of strings
    # such that every one of the sets contains the unique words for a paragraph


def extract_unique_words(sets: List[Set[str]]) -> Set[str]:
    """Extract all of the unique words shared across the sets in a list."""
    # create a single set of strings that includes all of the words
    # that that are unique across all of the sets for each of the paragraphs
    # new_set = sets[0].union(*sets)
    return sets[0].union(*sets)


def extract_common_words(sets: List[Set[str]]) -> Set[str]:
    """Extract all of the unique words shared in common by sets in a list."""
    # create a single set of strings that includes all of the words
    # that are found in every one of the sets for each paragraph in the text
    return sets[0].intersection(*sets)
