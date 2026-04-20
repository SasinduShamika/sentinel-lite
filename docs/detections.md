# Detection Rules

## Reverse Shell Detection

Detects common reverse shell patterns such as:

* bash interactive shells
* /dev/tcp usage

---

## Temporary Execution

Flags binaries executed from `/tmp`.

---

## Process Tree Analysis

Detects suspicious parent-child relationships such as:

* sshd spawning unexpected processes
