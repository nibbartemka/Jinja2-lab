from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))

template = env.get_template('lab2.html')

books = [
    {"title" : "Мастер и Маргарита",
     "author": "Булгаков М.А.",
     "price": 581.50},
    {"title" : "Белая гвардия",
    "author": "Булгаков М.А.", 
     "price": 600.00},
    {"title" : "Война и мир", 
    "author": "Толстой Л.Н.",
     "price": 899.99},
    {"title" : "Анна Каренина",
    "author": "Толстой Л.Н.", 
     "price": 450.10},
    {"title" : "Игрок",
    "author": "Достоевский Ф.М.",
    "price":  234.55},
    {"title" : "Мастер и Маргарита",
     "author": "Булгаков М.А.",
     "price": 581.50},
    {"title" : "Белая гвардия",
    "author": "Булгаков М.А.", 
     "price": 600.00},
    {"title" : "Война и мир", 
    "author": "Толстой Л.Н.",
     "price": 899.99},
    {"title" : "Анна Каренина",
    "author": "Толстой Л.Н.", 
     "price": 450.10},
    {"title" : "Игрок",
    "author": "Достоевский Ф.М.",
    "price":  234.55},
    {"title" : "Мастер и Маргарита",
     "author": "Булгаков М.А.",
     "price": 581.50},
    {"title" : "Белая гвардия",
    "author": "Булгаков М.А.", 
     "price": 600.00},
    {"title" : "Война и мир", 
    "author": "Толстой Л.Н.",
     "price": 899.99},
    {"title" : "Анна Каренина",
    "author": "Толстой Л.Н.", 
     "price": 450.10},
    {"title" : "Игрок",
    "author": "Достоевский Ф.М.",
    "price":  234.55},
]

result_html = template.render(
    books=books,
    n=100
)

with open('lab_res2.html', 'w', encoding='utf-8-sig') as o_file:
    print(result_html, file=o_file)