import os
import re

from answer.trainlog import mylogger


logger = mylogger(__name__)


class IllegalNumberError(Exception):
    pass


class Answer:
    
    @classmethod
    def check(cls, problem_number: int):
        pass
    
    @classmethod
    def show(
            cls,
            problem_number: int,
            directory_path: str = "answer",
            file_base_name: str = "training",
            extension: str = ".py") -> str:
        
        if isinstance(problem_number, str):
            if re.fullmatch(r"^\d+-\d+", problem_number):
                pass
            elif problem_number.isdigit():
                pass
            else:
                raise IllegalNumberError(f"問題番号の指定が正しくありません.{problem_number}")
        elif isinstance(problem_number, int):
            problem_number = str(problem_number)
            if not problem_number.isdigit():
                logger.debug("問題番号の指定が正しくありません")
                raise IllegalNumberError(f"問題番号の指定が正しくありません.{problem_number}")
        else:
            logger.debug("問題番号の指定が正しくありません")
            raise IllegalNumberError(f"問題番号の指定が正しくありません.{problem_number}") 
        
        
        filepath = os.path.join(
                directory_path,
                file_base_name + str(problem_number) + extension)
        
        if os.path.exists(filepath):
            with open(filepath, mode="r", encoding="utf-8") as f:
                 return f.read()
        else:
            msg = f"FileNotFound: {filepath}"
            logger.debug(msg)
            return f"ファイルが見つかりません{filepath}"
    
        
            