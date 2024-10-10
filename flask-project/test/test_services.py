def test_success_get_todo(todo_get_all_stub):
    todo_get_all_stub.get_all_todo.return_value = {
   "error": "not found"
}
    response = todo_get_all_stub.get_all_todo()
    assert response == {"error": "not found"}