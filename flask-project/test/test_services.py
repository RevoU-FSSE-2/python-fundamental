def test_success_get_todo(todo_get_all_stub):
#     todo_get_all_stub.get_all_todo.return_value = {
#    "error": "not found"
# }
    # schenario error
    # kita hit api
    # kita cek response == {"message": "cannot call third party apps"}
    # kita cek response code == 400
    
    # scenario success
    # kita hit api
    # kita cek response == {
#     "todos": [
#         {
#             "id": 1,
#             "todo": "Do something nice for someone you care about",
#             "completed": True,
#             "userId": 152
#         },
#         {
#             "id": 2,
#             "todo": "Memorize a poem",
#             "completed": True,
#             "userId": 13
#         }
#     ],
#     "total": 254,
#     "skip": 0,
#     "limit": 2
# }
    # kita cek response code == 200
    ...