from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))

template = env.get_template('lab.html')

result_html = template.render(
    select_name="color",
    option_line="синий зеленый красный",
    selected_num=1
 )

with open('lab_res1.html', 'w', encoding='utf-8-sig') as o_file:
    print(result_html, file=o_file)