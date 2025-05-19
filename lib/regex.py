import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = (
    r"^"                              # start
    r"[A-Z][a-zA-Z]*"                 # first chunk (capital + letters)
    r"(?:['-][A-Z][a-zA-Z]*)*"        # optional ‑ or ' followed by another capitalised chunk
    r"(?: "                           # OPTIONAL space‑separated second name
        r"[A-Z][a-zA-Z]*"             #   same rules …
        r"(?:['-][A-Z][a-zA-Z]*)*"    #
    r")?$"                            # end (space‑last‑name is optional)
)
name_regex = re.compile(name)

phone_number = (
    r"^" 
    r"(?:\(\d{3}\)\s?|\d{3}-?)"   # (555)  or 555  (with optional dash)
    r"\d{3}-?\d{4}$"              # 555‑5555  or 5555555
)
phone_regex = re.compile(phone_number)

email_address = (
    r"^[A-za-z]"
    r"[A-Za-z0-9]+(?:\.[A-Za-z0-9]+)*"   # local
    r"@"                                  # at
    r"[A-Za-z]+"                          # domain
    r"\.[A-Za-z]{2,}$"                    # .tld
)
email_regex = re.compile(email_address)
