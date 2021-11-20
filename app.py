from flask import Flask, request, render_template, redirect, url_for

from forms import TodoFormProject
from models import projects

app = Flask(__name__)
app.config['SECRET_KEY']='nininini'

@app.route('/todos/', methods = ['GET', 'POST'])
def projects_list():
    form = TodoFormProject()
    error = ''
    if request.method == 'POST':
        print(form.data.values())
        if form.validate_on_submit():
            data = tuple(form.data.values())[:2]
            projects.create_project(data)
        else:
            errors =form.errors
            print(errors)
        return redirect(url_for('projects_list'))

    return render_template('todos.html', form=form, projects=projects.all_projects(), error = error)



"""
@app.route('/todos/<int:todo_id>/', methods = ["POST", 'GET'])
def todo_details(todo_id):
    todo = todos.get(todo_id -1)
    form = TodoForm(data=todo)

    if request.method == 'POST':
        if form.validate_on_submit():
            todos.update(todo_id -1, form.data)
        return redirect(url_for('todos_list'))
    return render_template('todo.html', form=form, todo_id= todo_id)
"""

if __name__ == '__main__':
    app.run(debug=True)