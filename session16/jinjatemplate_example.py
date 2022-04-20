from jinja2 import Template
nombre = "rafa"
altura = 182
tm = Template("Hi my name is {{ name }} and my height in cms is {{ height }}")
msg = tm.render(name=nombre, height=altura)
print(msg)

person = {'name' : 'Rafa', 'age': 34}
tm  = Template("My name is {{ per['name' ] }} and I am {{ per ['age'] }} ... or so")
msg = tm.render(per=person)
print(msg)
