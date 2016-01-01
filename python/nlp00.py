def text_reverse(text):
    chr_list = list(text)
    chr_list.reverse()
    return "".join(chr_list)

print(text_reverse("stressed"))
