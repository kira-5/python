**ChatGPT:**

In FastAPI, functions and decorators play a crucial role in defining and managing the behavior of your API endpoints. Here's a brief overview of how they work and some common use cases:

### Functions in FastAPI

1. **Endpoint Functions**:
    
    * These are the core functions that handle HTTP requests. They are decorated with HTTP method decorators such as `@app.get()`, `@app.post()`, etc.
    * Example:
        
        ```python
        from fastapi import FastAPI
        
        app = FastAPI()
        
        @app.get("/items/{item_id}")
        def read_item(item_id: int, q: str = None):
            return {"item_id": item_id, "q": q}
        ```
        
2. **Dependency Functions**:
    
    * Used to provide reusable logic that can be shared across multiple endpoints. Dependencies are defined using functions and are injected into endpoint functions.
    * Example:
        
        ```python
        from fastapi import Depends, FastAPI
        
        app = FastAPI()
        
        def common_parameters(q: str = None):
            return {"q": q}
        
        @app.get("/items/")
        def read_items(commons: dict = Depends(common_parameters)):
            return commons
        ```
        
3. **Background Tasks**:
    
    * FastAPI supports background tasks that can be run after returning a response to the client.
    * Example:
        
        ```python
        from fastapi import FastAPI, BackgroundTasks
        
        app = FastAPI()
        
        def background_task(name: str):
            print(f"Hello {name}")
        
        @app.post("/send-notification/")
        def send_notification(name: str, background_tasks: BackgroundTasks):
            background_tasks.add_task(background_task, name)
            return {"message": "Notification sent"}
        ```
        

### Decorators in FastAPI

1. **Path Operation Decorators**:
    
    * These are used to define the HTTP methods (GET, POST, PUT, DELETE) and their routes.
    * Example:
        
        ```python
        @app.get("/users/")
        def get_users():
            return {"users": ["user1", "user2"]}
        ```
        
2. **Dependency Injection Decorators**:
    
    * `Depends` is used to declare dependencies for an endpoint, making it easy to reuse logic.
    * Example:
        
        ```python
        from fastapi import Depends, FastAPI
        
        app = FastAPI()
        
        def verify_token(token: str):
            if token != "secret":
                raise HTTPException(status_code=400, detail="Invalid token")
        
        @app.get("/secure-data/")
        def secure_data(token: str = Depends(verify_token)):
            return {"data": "This is secured"}
        ```
        
3. **Custom Decorators**:
    
    * You can create custom decorators for common logic or preprocessing tasks.
    * Example:
        
        ```python
        from fastapi import FastAPI
        
        app = FastAPI()
        
        def log_requests(func):
            async def wrapper(*args, **kwargs):
                print("Request received")
                return await func(*args, **kwargs)
            return wrapper
        
        @app.get("/items/")
        @log_requests
        async def read_items():
            return {"items": ["item1", "item2"]}
        ```
        
4. **Middleware**:
    
    * Although not strictly decorators, middleware functions are used to process requests before they reach your endpoint functions.
    * Example:
        
        ```python
        from fastapi import FastAPI
        from starlette.middleware.base import BaseHTTPMiddleware
        
        app = FastAPI()
        
        class CustomMiddleware(BaseHTTPMiddleware):
            async def dispatch(self, request, call_next):
                response = await call_next(request)
                response.headers['X-Custom-Header'] = 'Value'
                return response
        
        app.add_middleware(CustomMiddleware)
        ```
        

By using functions and decorators effectively, you can create modular, maintainable, and well-structured FastAPI applications.