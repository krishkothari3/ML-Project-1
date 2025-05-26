import sys

def error_message_detail(exception, error_detail: sys):
    """
    This function takes an exception and returns a detailed error message.
    :param exception: The exception object
    :param error_detail: The sys module for accessing exception details
    :return: A string containing the error message
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] with message: [{str(exception)}]"
    return error_message

class CustomException(Exception):
    """
    Custom exception class to handle exceptions with detailed error messages.
    """
    def __init__(self, exception, error_detail: sys):
        super().__init__(exception)
        self.error_message = error_message_detail(exception, error_detail)
    
    def __str__(self):
        return self.error_message