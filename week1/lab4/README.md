# Lab 4 – Command Line and Bash

## Goal

Get comfortable in the shell and write your first useful script.
---

## Problem Statement

The objective of this lab is to gain hands-on experience with Linux command-line tools and Bash scripting. The task involves downloading a plain-text file using `curl`, analyzing the text to find the most frequent words using a pipeline of shell commands (`tr`, `sort`, `uniq -c`, `sort -nr`, and `head`), counting lines, words, and characters using `wc`, and creating a reusable Bash script (`top_words.sh`) that accepts a filename and an optional count to display the most frequent words. The script should be executable and work correctly on different text files.


---

# Step 1: Download a Text File

Download a public text file from Project Gutenberg using `curl`.

### Command

```bash
curl -o alice.txt https://www.gutenberg.org/files/11/11-0.txt
```

### Explanation

- `curl` downloads a file from a URL.
- `-o` specifies the output filename.

### Screenshot

**Add Screenshot:** `screenshots/download.png`

---

### Step 2: Print the Top 10 Most Frequent Words

The following shell pipeline was used to extract all words from the text file, convert them to lowercase, count the occurrences of each word, sort them in descending order of frequency, and display the top 10 most frequent words.

```bash
tr -cs '[:alpha:]' '\n' < alice.txt | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -nr | head
```

**Explanation:**
- `tr -cs '[:alpha:]' '\n'` – Replaces non-alphabetic characters with newlines, producing one word per line.
- `tr '[:upper:]' '[:lower:]'` – Converts all words to lowercase.
- `sort` – Sorts the words alphabetically.
- `uniq -c` – Counts the occurrences of each unique word.
- `sort -nr` – Sorts the word counts in descending numerical order.
- `head` – Displays the top 10 most frequent words.

### Screenshot

**Add Screenshot:** `screenshots/pipeline.png`

---

# Step 3: Count Lines, Words and Characters

### Command

```bash
wc alice.txt
```

### Sample Output

```
3734 27462 144696 alice.txt
```

### Meaning

- Lines
- Words
- Characters
- Filename

### Screenshot

**Add Screenshot:** `screenshots/wc.png`

---

# Step 4: Create the Bash Script

Create a reusable Bash script named `top_words.sh`.

### Script

```bash
#!/bin/bash

if [ $# -lt 1 ]; then
    echo "Usage: $0 <filename> [count]"
    exit 1
fi

file=$1
count=${2:-10}

tr -cs '[:alpha:]' '\n' < "$file" \
| tr '[:upper:]' '[:lower:]' \
| sort \
| uniq -c \
| sort -nr \
| head -n "$count"
```

### Features

- Accepts a filename as input.
- Accepts an optional count.
- Default count is **10**.

### Screenshot

**Add Screenshot:** `screenshots/script.png`

---

# Step 5: Make the Script Executable

### Command

```bash
chmod +x top_words.sh
```

### Explanation

`chmod +x` gives execute permission to the script.

---

# Step 6: Execute the Script

### Display Top 10 Words

```bash
./top_words.sh alice.txt
```

### Display Top 15 Words

```bash
./top_words.sh alice.txt 15
```

### Screenshot

**Add Screenshot:** `screenshots/top_words_alice.png`

---

# Step 7: Test with Another File

Download another book.

```bash
curl -o sherlock.txt https://www.gutenberg.org/files/1661/1661-0.txt
```

Run the script.

```bash
./top_words.sh sherlock.txt
```

or

```bash
./top_words.sh sherlock.txt 8
```

### Screenshot

**Add Screenshot:** `screenshots/top_words_sherlock.png`

---

# 💻 Commands Used

- curl
- cat
- tr
- sort
- uniq
- head
- wc
- chmod
- nano

---

# 📖 Learning Outcomes

After completing this lab, I learned how to:

- Navigate the Linux shell.
- Download files from the internet using `curl`.
- Process text using command pipelines.
- Count lines, words, and characters with `wc`.
- Write reusable Bash scripts.
- Use command-line arguments and default values.
- Execute shell scripts using Linux permissions.

---

# ✅ Conclusion

This lab provided hands-on experience with essential Linux command-line tools and Bash scripting. By creating a reusable script (`top_words.sh`), I learned how to automate text analysis tasks and make scripts flexible using command-line arguments. These concepts form the foundation for shell scripting and Linux-based automation.