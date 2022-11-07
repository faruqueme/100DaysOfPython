#functions with output
## .title() helps you to modify a word which first caracter in capital and other are small 
def format_name(f_name, l_name):
	format_f=f_name.title()
	format_l=l_name.title()
	return f"{format_f} {format_l}"

print(format_name("angela", "ANGELA"))
