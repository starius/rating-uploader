import config
from repoze.lru import lru_cache

@lru_cache(maxsize=500)
def get_logins(worksheet):
    return worksheet.col_values(config.logins_col)

@lru_cache(maxsize=500)
def get_tasks(worksheet):
    return worksheet.row_values(config.tasks_row)

def get_cell_indexes(worksheet, login, task):
    logins = get_logins(worksheet)
    login_index = logins.index(login) + 1
    tasks = get_tasks(worksheet)
    task_index = tasks.index(task) + 1
    return (login_index, task_index)

def get_rating(worksheet, login, task):
    i, j = get_cell_indexes(worksheet, login, task)
    return worksheet.cell(i, j).value

def set_rating(worksheet, login, task, rating):
    i, j = get_cell_indexes(worksheet, login, task)
    worksheet.update_cell(i, j, rating)

def update_rating(worksheet, login, task, rating):
    prev = float(get_rating(worksheet, login, task))
    if float(rating) > prev:
        set_rating(worksheet, login, task, rating)
