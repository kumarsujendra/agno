from agno.tools import Toolkit
import json
import httpx

class MathToolKit(Toolkit):

    def __init__(self, name="toolkit"):
        super().__init__(name="math_toolkit")
        self.register(self.add_numbers)
        self.register(self.subtract_numbers)
        self.register(self.multiply_numbers)
        self.register(self.divide_numbers)
        self.register(self.product_search)
        

    def add_numbers(self, a: int, b: int) -> int:
        """Returns the sum of two numbers."""
        return str(a + b)

    def subtract_numbers(self, a: int, b: int) -> int:
        """Returns the difference between two numbers."""
        return str(a - b)

    def multiply_numbers(self, a: int, b: int) -> int:
        """Returns the product of two numbers."""
        return str(a * b)

    def divide_numbers(self, a: int, b: int) -> float:
        """Returns the division of two numbers, raises an error if dividing by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return str(a / b)
    
    def product_search(self, query: str, num_stories: int = 10) -> str:
        response = httpx.get(f'https://dummyjson.com/products/search?q={query}&limit={num_stories}')
        results = response.json()
        return json.dumps(results)
    

