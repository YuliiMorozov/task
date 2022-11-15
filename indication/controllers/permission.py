# from flask import request
# import jwt



# # def permission(f):
# #     def perm_two(*args, **kwargs):
# #         # print(request)
# #         print("hello permission")
# #     return perm_two
# def permission(role):
#     def decorator(f):
#         def permission_function():
#             # Do something with your request here
#             token = request.headers.get('Authorization') 
#             token_data = jwt.decode(token, "my_secret", algorithms=["HS256"])
#             print(token_data['role'])

    
#             return role
#         return permission_function
#     return decorator
    