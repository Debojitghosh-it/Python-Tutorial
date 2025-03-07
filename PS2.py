letter = '''Dear <|Name|>,
            you are selected!
            <|Date|>'''

letter = letter.replace("<|Name|>", "Debojit")
letter = letter.replace("<|Date|>", "7 Mar 2025")

print(letter)
