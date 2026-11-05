def read_int(prompt, minimum=None, maximum=None):
    try:
        value = int(input(prompt))
        if minimum is not None and value < minimum:
            raise ValueError(f"Value must be at least {minimum}.")
        if maximum is not None and value > maximum:
            raise ValueError(f"Value must be at most {maximum}.")
        return value
    
    except ValueError:
        print("Invalid input. Please enter an integer.")
    finally: 
        return read_int(prompt, minimum, maximum)
    
        
    
        
    
    


